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

Ao gerar ou editar qualquer conteúdo em documentação, README ou guia de
contribuição, as regras abaixo não são sugestões de estilo. São requisitos
verificados por CI, e várias delas existem especificamente porque texto
gerado por IA tende a violá-las por padrão.

- **Travessão, meia-risca, seta, ponto e vírgula: proibidos, sem exceção
  nenhuma.** Não é "com moderação". É zero, em toda página. Antes de
  escrever qualquer um desses, pare e use ponto final, vírgula ou
  dois-pontos. Não encadeie orações com esses caracteres só porque é mais
  rápido de gerar. Ponto e vírgula segue permitido dentro de bloco de
  código, onde é sintaxe real, não pontuação de prosa. Regra completa e
  exemplos de antes e depois em docs/contribuindo/convencoes-de-escrita.md,
  seção "Pontuação", e em docs/contribuindo/voz-e-tom.md.
- **Reticências: só três pontos digitados (`...`), nunca o glifo único.**
  O glifo único de reticências some da maioria dos teclados brasileiros e
  aparece sobretudo em texto gerado por máquina.
- **Nenhum emoji, em nenhuma circunstância**, mesmo que pareça ajudar a
  escanear uma lista. Documentação técnica deste projeto não usa emoji.
- **Aspas retas, nunca tipográficas.** `"..."` e `'...'`, não a versão
  curva das mesmas aspas.
- **Crase só para literal, e mesmo assim com moderação.** Nome de
  arquivo, comando, flag, chave de configuração, identificador de código:
  sim. Destacar uma palavra comum só porque soa técnica: não. E mesmo para
  literais, não repita a mesma crase várias vezes seguidas no mesmo
  parágrafo: cite uma vez, depois siga em prosa comum. Marcar quase todo
  substantivo com crase é um tic comum de texto gerado por IA, tanto
  quanto o travessão. Antes de terminar, releia e pergunte de cada trecho
  entre crases: é algo que alguém digitaria literalmente? Se não, tire a
  crase. Se sim mas já apareceu antes no parágrafo, também tire. Regra
  completa em docs/contribuindo/convencoes-de-escrita.md, seção "Código
  inline".
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

- Os quatro tipos Diátaxis (`docs/tutoriais/`, `docs/guias-como-fazer/`,
  `docs/referencia/`, `docs/explicacoes/`) têm conteúdo real sobre como
  operar este próprio template: clonar, rodar, publicar, manter.
- `docs/contribuindo/` é o guia de estilo vivo. Leia antes de editar
  qualquer prosa.
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
