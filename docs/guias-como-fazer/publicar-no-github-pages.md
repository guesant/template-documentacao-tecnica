# Como publicar no GitHub Pages

Este guia assume que você já tem o repositório no GitHub e já rodou o
tutorial [Clonar e rodar este template](../tutoriais/index.md) pelo menos
uma vez localmente.

## Habilite o GitHub Pages

1. No GitHub, abra **Settings** do repositório.
2. No menu lateral, abra **Pages**.
3. Em **Build and deployment**, mude **Source** para **GitHub Actions**.

Não escolha "Deploy from a branch". O workflow deste template
(`.github/workflows/docs.yml`) já faz o build e o deploy via Actions.

## Confirme que o workflow está ativo

O workflow roda automaticamente a cada push na branch `main`. Para
confirmar que ele existe e está habilitado:

1. Abra a aba **Actions** do repositório.
2. Procure o workflow chamado **docs**.
3. Se ele aparece na lista, está ativo. Se a aba Actions mostra um aviso de
   que Actions está desabilitado para o repositório, habilite em Settings,
   Actions, General.

## Publique

Faça um push para `main` (ou faça merge de um PR nela). O workflow gera o
site com `mkdocs build --strict` e publica o resultado.

Acompanhe o progresso na aba **Actions**. Quando o job **deploy** terminar
com sucesso, a URL do site aparece no resumo do workflow e em Settings,
Pages.

## Verificando o resultado

- A URL segue o padrão `https://SEU-USUARIO.github.io/SEU-REPOSITORIO/`.
- Se o build falhar em `mkdocs build --strict`, a causa mais comum é um
  link interno quebrado. O log do job mostra qual arquivo e qual link.
- Se o job `deploy` falhar mas o `build` passou, confirme que a Source em
  Settings, Pages está mesmo em GitHub Actions, não em branch.

## Ver também

- [Como rodar os quality gates localmente](rodar-quality-gates-localmente.md),
  para pegar esse tipo de erro antes de dar push.
- [Referência de configuração](../referencia/index.md), para o que cada
  campo de `mkdocs.yml` faz.
