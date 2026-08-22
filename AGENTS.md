# AGENTS.md

Instruções para agentes de IA (Claude, Gemini, Copilot, Codex ou qualquer
outro) trabalhando neste repositório. CLAUDE.md e GEMINI.md são symlinks
para este arquivo: edite só este, os outros dois atualizam junto.

## O que é este projeto

Template docs-as-code de documentação técnica, organizado pelo framework
Diátaxis (tutorial, guia prático, referência, explicação), com MkDocs
Material, quality gates automatizados e uma seção de contribuição que
funciona como guia de estilo vivo. Detalhes completos em
[docs/contribuindo/index.md](docs/contribuindo/index.md).

## Regras de escrita: siga estritamente, não apenas "na maior parte"

**Escopo: todo arquivo `.md` deste repositório, sem exceção.** As regras
abaixo valem para qualquer página em `docs/` e valem igualmente para
`README.md`, `CONTRIBUTING.md` e este próprio `AGENTS.md` (e os symlinks
`CLAUDE.md`, `GEMINI.md`). Não existe arquivo "fora da docs" onde
travessão, crase em excesso ou lista numerada mal usada ficam liberados.
Ao editar qualquer `.md` deste repositório, aplique as mesmas regras.

Estas regras não são sugestões de estilo. São requisitos verificados por
CI, e várias delas existem especificamente porque texto gerado por IA
tende a violá-las por padrão.

Cada bullet abaixo cita a regra real (a mesma que vale para qualquer
pessoa que escreva neste projeto, documentada em `docs/contribuindo/`) e
acrescenta o motivo de reforçar isso especificamente com você, agente:
várias dessas regras existem porque texto gerado por IA tende a violá-las
por padrão, então a checagem manual extra vale a pena.

- **Travessão, meia-risca, seta, ponto e vírgula: proibidos, sem exceção
  nenhuma.** Regra completa e exemplos de antes e depois:
  [Convenções de escrita, seção Pontuação](docs/contribuindo/convencoes-de-escrita.md#pontuacao-banida)
  e [Voz e tom](docs/contribuindo/voz-e-tom.md). Reforço para você: não
  encadeie orações com esses caracteres só porque é mais rápido de gerar.
  Ponto e vírgula segue permitido dentro de bloco de código, onde é
  sintaxe real, não pontuação de prosa.
- **Reticências: só três pontos digitados (`...`), nunca o glifo único.**
  Mesma regra, mesma seção. Reforço: o glifo único de reticências some da
  maioria dos teclados brasileiros e aparece sobretudo em texto gerado por
  máquina.
- **Nenhum emoji, em nenhuma circunstância.** Ver
  [Convenções de escrita](docs/contribuindo/convencoes-de-escrita.md).
- **Aspas retas, nunca tipográficas.** `"..."` e `'...'`, não a versão
  curva das mesmas aspas. Mesma seção de Pontuação.
- **Crase só para literal, e mesmo assim com moderação.** Regra completa:
  [Convenções de escrita, seção Código inline](docs/contribuindo/convencoes-de-escrita.md#uso-de-codigo-inline).
  Reforço para você: marcar quase todo substantivo com crase é um tic
  comum de texto gerado por IA, tanto quanto o travessão. Antes de
  terminar, releia e pergunte de cada trecho entre crases: é algo que
  alguém digitaria literalmente? Se não, tire a crase. Se sim mas já
  apareceu antes no parágrafo, também tire.
- **Nenhum caractere invisível** (espaço de largura zero, hífen suave,
  BOM). Se você copiou texto de outro lugar antes de adaptar, verifique.
- **Voz ativa e segunda pessoa por padrão.** Ver
  [Voz e tom](docs/contribuindo/voz-e-tom.md). Evite passiva burocrática
  ("foi decidido que...", "recomenda-se que..."). Diga quem faz o quê.
- **Confiança, não hedging.** Evite "talvez", "possivelmente", "pode ser
  que" em instruções. Se a informação é incerta, isso é um problema de
  conteúdo a resolver antes de publicar, não algo para suavizar com tom.
- **Um tipo de conteúdo por página** (tutorial, guia, referência ou
  explicação). Ver [Diátaxis](docs/contribuindo/diataxis.md). Não misture.
- **Linke sem medo, no estilo Wikipédia.** Regra completa:
  [Convenções de escrita, âncora links-liberais](docs/contribuindo/convencoes-de-escrita.md#links-liberais).
  Reforço: não economize link achando que "polui" o texto. Cada página
  DEVE terminar com uma seção "Continue por aqui" apontando o próximo
  passo lógico.
- **Todo diagrama de fluxo, decisão ou estrutura DEVE ser Mermaid**, não
  descrição só em texto. Cada página de `docs/` DEVE ter pelo menos um
  diagrama que ajude a visualizar o conteúdo, não decoração.
- **Lista numerada só quando a ordem importa de verdade, e no máximo sete
  itens (ordenada ou não).** Regra completa, com fontes:
  [Convenções de escrita, âncora listas-vs-prosa](docs/contribuindo/convencoes-de-escrita.md#listas-vs-prosa).
  Reforço: enumerar tudo em lista numerada, mesmo coisas paralelas, é um
  tique comum de texto gerado por IA. Se a lista que você gerou passou de
  sete itens, isso é sinal de que você despejou uma lista de ideias em vez
  de escrever prosa ou agrupar em subseções: pare e reestruture.

Antes de considerar uma tarefa de documentação terminada, rode os quality
gates (ver abaixo) e corrija tudo que falhar. Não proponha uma mudança em
documentação sem ter rodado pelo menos o checker de tipografia.

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

- Os quatro tipos Diátaxis (`docs/documentacao/tutoriais/`, `docs/documentacao/guias-como-fazer/`,
  `docs/documentacao/referencia/`, `docs/documentacao/explicacoes/`) têm conteúdo real sobre como
  operar este próprio template: clonar, rodar, publicar, manter.
- [`docs/contribuindo/`](docs/contribuindo/index.md) é o guia de estilo
  vivo. Leia antes de editar qualquer prosa.
- A navegação do site fica em `mkdocs.yml`. Toda página nova DEVE ser
  adicionada lá, senão o build não falha mas a página fica órfã.
- Os workflows de CI ficam em `.github/workflows/`: um gera e publica o
  site, o outro roda os quality gates.
- A configuração dos quality gates em si (dependências Node, regras de
  markdownlint, dicionário de ortografia, script de tipografia) fica na
  raiz do repositório e em `scripts/`.

## Commits

Conventional Commits (`tipo(escopo): assunto`, imperativo, sem ponto
final). Não faça commit nem push sem confirmação explícita de quem está
pedindo a tarefa, mesmo que a mudança pareça pequena.
