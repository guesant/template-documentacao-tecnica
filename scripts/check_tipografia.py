#!/usr/bin/env python3
"""Valida emojis e caracteres não padronizados na documentação Markdown.

Sem dependências externas (só stdlib), para não exigir instalação de
toolchain extra além do Python que o projeto já usa para o MkDocs.

Verifica quatro coisas, nessa ordem de gravidade.

1. Emojis. Nunca permitidos em conteúdo publicado (ver convenção em
   docs/contribuindo/convencoes-de-escrita.md).
2. Caracteres invisíveis ou de controle (zero-width space, soft hyphen,
   BOM no meio do arquivo, etc.). Nunca deveriam existir. Costumam ser
   artefato de copiar e colar de outra ferramenta.
3. Travessão, meia-risca e seta. Este template bane os três em qualquer
   página, sem exceção. Prosa técnica em português usa ponto final,
   vírgula, dois-pontos e ponto e vírgula para tudo o que essas marcas
   fariam.
4. Qualquer caractere fora da faixa ASCII que não esteja na lista de
   caracteres explicitamente aprovados para prosa em português técnico
   (acentuação, cedilha, reticências). Isso pega erro de digitação de
   teclado, homóglifo (ex.: um "a" cirílico no lugar de um "a" latino) e
   arte ASCII de caixa, que é justamente o tipo de coisa difícil de notar
   a olho nu e difícil de manter sincronizada.
"""

from __future__ import annotations

import pathlib
import re
import sys
import unicodedata

REPO_ROOT = pathlib.Path(__file__).resolve().parent.parent

SCAN_GLOBS = ["docs/**/*.md", "README.md", "CONTRIBUTING.md", "AGENTS.md"]

# Caracteres > U+007F explicitamente aprovados para prosa em português
# técnico. Qualquer coisa fora dessa lista (e fora das letras acentuadas
# verificadas via unicodedata, abaixo) é reportada como suspeita.
# Travessão, meia-risca, seta e reticências como caractere único ficam de
# fora de propósito: são banidos desta documentação. Ver BANNED_PUNCTUATION.
ALLOWED_EXTRA_CHARS: set[str] = set()

# Travessão, meia-risca, seta e reticências como caractere único: nunca
# permitidos, mesmo em paráfrase ou exemplo. Reportados com uma mensagem
# própria (mais direta do que a genérica de "caractere não padronizado").
# O caractere único de reticências (U+2026) é digitado por autocorreção de
# editor de texto ou gerado por modelo de linguagem; em um teclado comum
# no Brasil, "..." sai como três pontos separados, não como um glifo só.
BANNED_PUNCTUATION = {
    "—": "TRAVESSÃO (em dash)",
    "–": "MEIA-RISCA (en dash)",
    "→": "SETA PARA A DIREITA",
    "←": "SETA PARA A ESQUERDA",
    "↔": "SETA DUPLA",
    "…": "RETICÊNCIAS COMO CARACTERE ÚNICO (use três pontos: ...)",
}

# Pontuação ASCII banida por ser um tique de escrita mais comum em texto
# gerado por IA do que em prosa técnica humana em português: o ponto e
# vírgula quase sempre junta duas orações que deveriam ser duas frases
# separadas por ponto final. Verificado à parte porque é ASCII (<= 0x7F),
# fora do escopo da varredura de caracteres não latinos abaixo.
ASCII_BANNED_PUNCTUATION = {
    ";": "PONTO E VÍRGULA (quase sempre deveria ser ponto final ou vírgula)",
}

# Faixas de emoji (Unicode Consortium): pictogramas, emoticons, dingbats,
# símbolos diversos, seletores de variação e bandeiras.
EMOJI_RANGES = [
    (0x1F300, 0x1FAFF),  # pictogramas diversos até "Symbols and Pictographs Extended-A"
    (0x1F1E6, 0x1F1FF),  # indicadores regionais (bandeiras)
    (0x2600, 0x27BF),  # símbolos diversos + dingbats
    (0x2B00, 0x2BFF),  # símbolos e setas diversos (estrelas, etc.)
    (0xFE00, 0xFE0F),  # seletores de variação (forçam apresentação emoji)
    (0x1F900, 0x1F9FF),  # símbolos suplementares
]

# Caracteres invisíveis ou de controle que não deveriam aparecer em texto
# corrido. Normalmente artefato de copiar e colar de outra ferramenta.
INVISIBLE_CHARS = {
    0x00AD: "SOFT HYPHEN",
    0x200B: "ZERO WIDTH SPACE",
    0x200C: "ZERO WIDTH NON-JOINER",
    0x200D: "ZERO WIDTH JOINER",
    0x2060: "WORD JOINER",
    0xFEFF: "ZERO WIDTH NO-BREAK SPACE (BOM)",
}

# Aspas tipográficas ("curvas"): a convenção deste template é aspas retas
# ("...", '...'), por consistência e para copiar/colar sem quebrar em
# terminais e blocos de código. Ver docs/contribuindo/convencoes-de-escrita.md.
CURLY_QUOTES = {
    0x2018: "LEFT SINGLE QUOTATION MARK",
    0x2019: "RIGHT SINGLE QUOTATION MARK",
    0x201C: "LEFT DOUBLE QUOTATION MARK",
    0x201D: "RIGHT DOUBLE QUOTATION MARK",
}


def is_emoji(codepoint: int) -> bool:
    return any(lo <= codepoint <= hi for lo, hi in EMOJI_RANGES)


def is_accepted_letter(ch: str) -> bool:
    """Letras acentuadas latinas (á, ç, ã, ...) são sempre aceitas.

    Verifica que o caractere se decompõe (NFKD) numa letra ASCII base mais
    apenas marcas combinantes (acento, til, cedilha), ou seja, é uma letra
    latina acentuada de verdade, não um homóglifo de outro alfabeto.
    """
    if unicodedata.category(ch) not in ("Ll", "Lu"):
        return False
    decomposed = unicodedata.normalize("NFKD", ch)
    if len(decomposed) < 2:
        return False
    base, marks = decomposed[0], decomposed[1:]
    return base.isascii() and base.isalpha() and all(
        unicodedata.category(mark) == "Mn" for mark in marks
    )


def code_fence_lines(lines: list[str]) -> set[int]:
    """Números de linha (1-indexado) dentro de blocos ```...```.

    Ponto e vírgula e travessão são sintaxe legítima em exemplos de shell
    ou de outra linguagem (ex.: `for f in *; do ...; done`), então as
    checagens de pontuação de prosa não se aplicam dentro de blocos de
    código. As demais checagens (emoji, caractere invisível) continuam
    valendo em qualquer lugar do arquivo.
    """
    inside: set[int] = set()
    open_fence = False
    for i, line in enumerate(lines, start=1):
        if line.strip().startswith("```"):
            open_fence = not open_fence
            continue
        if open_fence:
            inside.add(i)
    return inside


def scan_file(path: pathlib.Path) -> list[str]:
    problems: list[str] = []
    text = path.read_text(encoding="utf-8")
    rel = path.relative_to(REPO_ROOT)
    lines = text.splitlines()
    fenced = code_fence_lines(lines)

    for lineno, line in enumerate(lines, start=1):
        for col, ch in enumerate(line, start=1):
            if ch in ASCII_BANNED_PUNCTUATION and lineno not in fenced:
                problems.append(
                    f"{rel}:{lineno}:{col}: {ASCII_BANNED_PUNCTUATION[ch]} "
                    f"{ch!r}."
                )
                continue

            codepoint = ord(ch)
            if codepoint <= 0x7F:
                continue

            if is_emoji(codepoint):
                problems.append(
                    f"{rel}:{lineno}:{col}: emoji não permitido: {ch!r} (U+{codepoint:04X})"
                )
                continue

            if codepoint in INVISIBLE_CHARS:
                problems.append(
                    f"{rel}:{lineno}:{col}: caractere invisível "
                    f"{INVISIBLE_CHARS[codepoint]} (U+{codepoint:04X}), remova"
                )
                continue

            if codepoint in CURLY_QUOTES:
                problems.append(
                    f"{rel}:{lineno}:{col}: aspa tipográfica {ch!r} "
                    f"(U+{codepoint:04X}), use aspa reta \" ou '"
                )
                continue

            if ch in BANNED_PUNCTUATION:
                problems.append(
                    f"{rel}:{lineno}:{col}: {BANNED_PUNCTUATION[ch]} banido "
                    f"nesta documentação {ch!r} (U+{codepoint:04X}). "
                    "Reescreva com ponto final, vírgula ou dois-pontos."
                )
                continue

            if ch in ALLOWED_EXTRA_CHARS or is_accepted_letter(ch):
                continue

            try:
                name = unicodedata.name(ch)
            except ValueError:
                name = "sem nome Unicode"
            problems.append(
                f"{rel}:{lineno}:{col}: caractere não padronizado {ch!r} "
                f"(U+{codepoint:04X} {name}), fora da lista de caracteres "
                "aprovados para prosa técnica em pt-BR"
            )

    return problems


def main() -> int:
    files: list[pathlib.Path] = []
    for pattern in SCAN_GLOBS:
        files.extend(sorted(REPO_ROOT.glob(pattern)))

    all_problems: list[str] = []
    for f in files:
        all_problems.extend(scan_file(f))

    if all_problems:
        print(f"check_tipografia: {len(all_problems)} problema(s) encontrado(s)\n")
        print("\n".join(all_problems))
        return 1

    print(f"check_tipografia: ok ({len(files)} arquivo(s) verificado(s))")
    return 0


if __name__ == "__main__":
    sys.exit(main())
