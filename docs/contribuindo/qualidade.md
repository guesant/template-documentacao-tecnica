# Quality gates

As regras em [Convenções de escrita](convencoes-de-escrita.md) e
[Voz e tom](voz-e-tom.md) só valem alguma coisa se forem verificadas. Regra
que depende só de memória humana em revisão de PR degrada com o tempo:
quem revisa cansa, novos colaboradores não conhecem a regra, exceções viram
norma. Este projeto automatiza o que dá para automatizar e usa revisão
humana só para o que exige julgamento (tom, clareza, se o conteúdo está no
tipo certo de página).

Quatro verificações rodam em CI (`.github/workflows/lint.yml`) a cada push
e pull request para `main`.

## 1. markdownlint

**O que verifica:** estrutura e formatação Markdown. Cabeçalhos sem linha
em branco ao redor, listas numeradas com prefixo inconsistente, blocos de
código sem fechamento, entre outras dezenas de regras.

**Ferramenta:** [`markdownlint-cli2`](https://github.com/DavidAnson/markdownlint-cli2),
configurado em [`.markdownlint-cli2.jsonc`](https://github.com/guesant/template-documentacao-tecnica/blob/main/.markdownlint-cli2.jsonc).

**Rodar localmente:**

```bash
docker run --rm -v "$PWD:/work" -w /work node:24-alpine sh -c "npm ci && npm run lint:md"
```

## 2. cspell (ortografia em pt-BR)

**O que verifica:** palavras que não existem em português nem estão na
lista de termos técnicos do projeto. Pega erro de digitação real, não
estilo.

**Ferramenta:** [`cspell`](https://cspell.org/) com o dicionário
[`@cspell/dict-pt-br`](https://www.npmjs.com/package/@cspell/dict-pt-br),
configurado em [`cspell.json`](https://github.com/guesant/template-documentacao-tecnica/blob/main/cspell.json).
Termos técnicos que não existem em nenhum dicionário de idioma (nomes de
ferramentas, siglas, nomes próprios) vão em
[`cspell-termos-do-projeto.txt`](https://github.com/guesant/template-documentacao-tecnica/blob/main/cspell-termos-do-projeto.txt),
não em exceções soltas espalhadas pelo texto.

**Rodar localmente:**

```bash
docker run --rm -v "$PWD:/work" -w /work node:24-alpine sh -c "npm ci && npm run lint:spell"
```

## 3. Tipografia (emoji, pontuação banida, caractere invisível)

**O que verifica:** cinco classes de problema, em ordem de gravidade.

1. <a id="emojis"></a>**Emoji.** Nunca permitido em conteúdo publicado (ver
   [Convenções de escrita](convencoes-de-escrita.md)). Documentação técnica
   não usa emoji como substituto de clareza de texto.
2. **Caractere invisível.** Espaço de largura zero, hífen suave, BOM no
   meio do arquivo. Normalmente artefato de copiar e colar de outra
   ferramenta (editor de texto rico, PDF, página web). Nunca deveria estar
   num arquivo de texto corrido, e é praticamente impossível notar a olho
   nu.
3. **Pontuação banida.** Travessão, meia-risca, seta (em qualquer
   direção), ponto e vírgula fora de bloco de código, e reticências como
   caractere Unicode único em vez de três pontos digitados. Regra completa
   em [Convenções de escrita](convencoes-de-escrita.md#pontuacao-banida).
4. **Aspa tipográfica.** Aspas curvas em vez de aspas retas (`"..."`,
   `'...'`).
5. **Qualquer caractere fora do alfabeto latino padrão de prosa técnica em
   português.** A lista aprovada é curta: letras acentuadas (á, ç, ã, ...)
   e reticências digitadas como três pontos. Qualquer coisa fora disso é
   reportada, desde um homóglifo cirílico que imita uma letra latina até
   arte ASCII de caixa (os caracteres Unicode de desenho de linha usados
   para montar diagramas de árvore de diretório à mão) num diagrama
   desenhado manualmente, que é justamente o tipo de coisa difícil de
   manter sincronizada. Esse problema específico é o motivo de este
   template não ter mais um diagrama de árvore manual no `README.md`.

**Ferramenta:** [`scripts/check_tipografia.py`](https://github.com/guesant/template-documentacao-tecnica/blob/main/scripts/check_tipografia.py),
script Python puro escrito para este template (sem dependência externa,
para não exigir toolchain além do que o projeto já usa para o MkDocs).

**Rodar localmente:**

```bash
python3 scripts/check_tipografia.py
```

## 4. `mkdocs build --strict`

**O que verifica:** link interno quebrado, referência a página que não
existe na navegação. Já documentado em
[Convenções de escrita](convencoes-de-escrita.md#links).

**Rodar localmente:**

```bash
pip install -r requirements.txt
mkdocs build --strict
```

## O que não é automatizado (e por quê)

Nenhuma das quatro verificações lê o texto pelo sentido. Elas não pegam:

- Se o parágrafo repete a mesma palavra entre crases várias vezes seguidas
  em vez de nomear uma vez e seguir em prosa comum (ver
  [Convenções de escrita](convencoes-de-escrita.md#uso-de-codigo-inline)).
- Se o tom está certo para o tipo de página (ver [Voz e tom](voz-e-tom.md)).
- Se o conteúdo está, de fato, no tipo certo de página segundo
  [Diátaxis](diataxis.md), e não só na pasta certa.
- Se uma explicação é clara para quem não tem o contexto de quem escreveu.

Isso continua sendo trabalho de revisão humana em PR. O objetivo dos
quality gates não é substituir revisão, é eliminar da revisão humana o
trabalho mecânico que uma máquina faz melhor, para sobrar atenção para o
que só um humano julga.

## Ver também

- [Convenções de escrita](convencoes-de-escrita.md)
- [Voz e tom](voz-e-tom.md)
- [Como escrever uma página de documentação](como-escrever-documentacao.md)
