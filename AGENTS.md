# AGENTS.md

Instruções para agentes de IA (Claude, Gemini, Copilot, Codex ou qualquer
outro) trabalhando neste repositório. `CLAUDE.md` e `GEMINI.md` são
symlinks para este arquivo: edite só este, os outros dois atualizam junto.

## O que é este projeto

Template docs-as-code de documentação técnica, organizado pelo framework
Diátaxis (tutorial, guia prático, referência, explicação), com MkDocs
Material, quality gates automatizados e uma seção `docs/contribuindo/` que
funciona como guia de estilo vivo. Detalhes completos:
[`docs/contribuindo/index.md`](docs/contribuindo/index.md).

## Regras de escrita: siga estritamente, não apenas "na maior parte"

Ao gerar ou editar qualquer conteúdo em `docs/`, `README.md` ou
`CONTRIBUTING.md`, as regras abaixo não são sugestões de estilo. São
requisitos verificados por CI (`.github/workflows/lint.yml`), e várias
delas existem especificamente porque texto gerado por IA tende a violá-las
por padrão.

- **Travessão (—) com moderação real, não nominal.** No máximo um por
  parágrafo curto. Antes de escrever um travessão, pare e pergunte: um
  ponto final, vírgula ou dois-pontos resolve? Quase sempre resolve. Não
  encadeie três ou quatro orações com travessão só porque é mais rápido de
  gerar. Regra completa e exemplos de antes/depois:
  [`docs/contribuindo/convencoes-de-escrita.md#uso-do-travessao`](docs/contribuindo/convencoes-de-escrita.md#uso-do-travessao)
  e [`docs/contribuindo/voz-e-tom.md`](docs/contribuindo/voz-e-tom.md).
- **Nenhum emoji, em nenhuma circunstância**, mesmo que pareça ajudar a
  escanear uma lista. Documentação técnica deste projeto não usa emoji.
- **Aspas retas (`"..."`, `'...'`), nunca tipográficas (`"..."`, `'...'`).**
- **Crase só para literal, nunca para ênfase.** Nome de arquivo, comando,
  flag, chave de config, identificador de código: sim. Destacar uma
  palavra comum só porque soa técnica: não. Marcar quase tudo com crase é
  um tic comum de texto gerado por IA. Antes de terminar, releia e
  pergunte de cada trecho entre crases: "isso é algo que alguém digitaria
  literalmente?" Se não, tire a crase. Regra completa:
  [`docs/contribuindo/convencoes-de-escrita.md#uso-de-codigo-inline`](docs/contribuindo/convencoes-de-escrita.md#uso-de-codigo-inline).
- **Nenhum caractere invisível** (espaço de largura zero, hífen suave, BOM). Se
  você copiou texto de outro lugar antes de adaptar, verifique.
- **Voz ativa e segunda pessoa por padrão.** Evite passiva burocrática
  ("foi decidido que...", "recomenda-se que..."). Diga quem faz o quê.
- **Confiança, não hedging.** Evite "talvez", "possivelmente", "pode ser
  que" em instruções. Se a informação é incerta, isso é um problema de
  conteúdo a resolver antes de publicar, não algo para suavizar com tom.
- **Um tipo de conteúdo por página** (tutorial, guia, referência ou
  explicação). Não misture.

Antes de considerar uma tarefa de documentação terminada, rode os quality
gates (ver abaixo) e corrija tudo que falhar. Não proponha uma mudança em
`docs/` sem ter rodado pelo menos `python3 scripts/check_tipografia.py`.

## Como rodar as verificações

Prefira rodar ferramentas Node dentro de um container, para não instalar
nada globalmente no host:

```bash
docker run --rm -v "$PWD:/work" -w /work node:24-alpine sh -c "npm ci && npm run lint"
```

O checker de tipografia é Python puro (sem dependência), roda direto:

```bash
python3 scripts/check_tipografia.py
```

Para validar a navegação e os links do site:

```bash
pip install -r requirements.txt
mkdocs build --strict
```

## Estrutura do repositório

- `docs/tutoriais/`, `docs/guias-como-fazer/`, `docs/referencia/`,
  `docs/explicacoes/`: os quatro tipos Diátaxis, com conteúdo real sobre
  como operar este próprio template (clonar, rodar, publicar, manter).
- `docs/contribuindo/`: guia de estilo vivo (voz, convenções, quality
  gates, bibliografia). Leia antes de editar qualquer prosa.
- `mkdocs.yml`: navegação do site. Toda página nova DEVE ser adicionada
  aqui em `nav:`, senão `mkdocs build --strict` não falha, mas a página
  fica órfã (inacessível pela navegação).
- `.github/workflows/`: `docs.yml` (build + deploy no GitHub Pages),
  `lint.yml` (quality gates).
- `package.json`, `cspell.json`, `.markdownlint-cli2.jsonc`,
  `cspell-termos-do-projeto.txt`, `scripts/check_tipografia.py`: config e
  código dos quality gates.

## Commits

Conventional Commits (`tipo(escopo): assunto`, imperativo, sem ponto
final). Não faça commit nem push sem confirmação explícita de quem está
pedindo a tarefa, mesmo que a mudança pareça pequena.
