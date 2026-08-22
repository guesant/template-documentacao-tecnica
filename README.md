# Template de Documentação Técnica

Template para começar um projeto de documentação técnica com **docs-as-code**.
Organizado segundo o framework [Diátaxis](https://diataxis.fr/): tutoriais,
guias práticos, referência e explicações. Inclui quality gates automatizados
(lint, ortografia, tipografia) e instruções prontas para agentes de IA
(`AGENTS.md`).

## Estrutura

Todo o conteúdo do site fica em `docs/`. Fora dela: `mkdocs.yml` (configuração
do site), `CONTRIBUTING.md` (fluxo de contribuição), `AGENTS.md` (instruções
para agentes de IA), `package.json` + `cspell.json` +
`.markdownlint-cli2.jsonc` (quality gates) e `.github/workflows/` (CI e
deploy).

O site tem duas abas, para separar quem lê de quem escreve:

- **Documentação** — `docs/tutoriais/`, `docs/guias-como-fazer/`,
  `docs/referencia/` e `docs/explicacoes/`, os quatro tipos do Diátaxis, já
  preenchidos com conteúdo real sobre como clonar, rodar, publicar e manter
  este próprio template. Substitua por conteúdo do seu projeto quando for
  usar o template para valer.
- **Contribuindo** — `docs/contribuindo/`, com as regras de quem escreve:
  por que a estrutura é assim, voz e tom, convenções de escrita, quality
  gates. Essa aba acompanha o template permanentemente. É o guia de estilo
  vivo da sua documentação. Edite-a para as regras da sua equipe em vez de
  removê-la.

A navegação real (fonte da verdade sobre quais páginas existem e onde) é a
seção `nav:` do [`mkdocs.yml`](mkdocs.yml).

## Quality gates

Quatro verificações automatizadas rodam em CI a cada PR (workflow
`.github/workflows/lint.yml`), detalhadas em
[`docs/contribuindo/qualidade.md`](docs/contribuindo/qualidade.md):

1. `markdownlint-cli2`: estrutura e formatação Markdown.
2. `cspell` com dicionário pt-BR: ortografia.
3. `scripts/check_tipografia.py`: bane emoji, caractere invisível, aspa
   tipográfica e qualquer caractere fora do alfabeto latino padrão de prosa
   técnica em português.
4. `mkdocs build --strict`: link interno quebrado.

Rode tudo localmente com Docker (não precisa instalar Node no seu sistema):

```bash
docker run --rm -v "$PWD:/work" -w /work node:24-alpine npm ci
docker run --rm -v "$PWD:/work" -w /work node:24-alpine npm run lint
```

## Usando este template

Clique em **Use this template** no GitHub, ou:

```bash
git clone https://github.com/guesant/template-documentacao-tecnica.git meu-projeto-docs
cd meu-projeto-docs
rm -rf .git && git init
```

Depois:

1. Ajuste `mkdocs.yml` (`site_name`, `repo_url`, `repo_name`).
2. Substitua o conteúdo de exemplo em cada pasta de `docs/`.
3. Ajuste `docs/contribuindo/` às regras da sua equipe.
4. Rode localmente:

   ```bash
   pip install -r requirements.txt
   mkdocs serve
   ```

5. Habilite o GitHub Pages nas configurações do repositório (Settings → Pages →
   Source: GitHub Actions). O workflow já publica a cada push em `main`.
6. O Dependabot (`.github/dependabot.yml`) já está configurado para manter
   npm, pip e as GitHub Actions atualizados semanalmente.

## Referências

- [Diátaxis](https://diataxis.fr/)

## Licença

Sem licença definida. Todos os direitos reservados por padrão. Adicione um
arquivo `LICENSE` se quiser permitir reuso.
