# Referências

Esta seção "Contribuindo" não inventa regras do zero: sintetiza práticas já
documentadas por frameworks, guias de estilo e comunidades de documentação
técnica estabelecidas. Cada norma nas páginas seguintes é rastreável a uma
fonte listada aqui, citada inline como `(Organização/Autor, Ano)`, e
**parafraseada em português**, não copiada. Citações diretas, quando
aparecem, vêm entre aspas, curtas, com atribuição.

Isso é proposital. Um guia de estilo de documentação técnica é, por
natureza, um trabalho coletivo. Assim como um artigo acadêmico reúne e
credita as fontes em que se apoia, esta seção credita os "autores" cujas
ideias moldam as regras práticas do template.

## Frameworks de organização de conteúdo

<a id="diataxis"></a>
**Diátaxis**: Daniele Procida. Framework que classifica documentação
técnica em quatro tipos (tutorial, guia prático, referência, explicação) a
partir de duas dimensões: ação vs. cognição, estudo vs. trabalho. Publicado
originalmente como sistema de documentação da Divio e depois formalizado de
forma independente em [diataxis.fr](https://diataxis.fr/). É a fonte
estrutural de toda a divisão `docs/tutoriais/`, `docs/guias-como-fazer/`,
`docs/referencia/`, `docs/explicacoes/` deste template.

<a id="good-docs-project"></a>
**The Good Docs Project**: comunidade open source mantenedora de templates
de documentação técnica (README, guia de instalação, referência de API,
etc.), com curadoria de boas práticas de estrutura e conteúdo mínimo
esperado por tipo de documento. Disponível em
[thegooddocsproject.dev](https://www.thegooddocsproject.dev/).

## Guias de estilo de escrita técnica

<a id="google-style"></a>
**Google Developer Documentation Style Guide**: guia de estilo público do
Google para documentação de desenvolvedores, cobrindo voz, tom, gramática,
formatação e acessibilidade. Disponível em
[developers.google.com/style](https://developers.google.com/style).

<a id="microsoft-style"></a>
**Microsoft Writing Style Guide**: guia de estilo público da Microsoft,
com princípios de voz e tom ("caloroso e acolhedor, direto e claro, pronto
para ajudar") e regras práticas de bias-free e inclusive language. Disponível
em [learn.microsoft.com/style-guide](https://learn.microsoft.com/style-guide/welcome/).

<a id="gitlab-style"></a>
**GitLab Documentation Style Guide**: guia de estilo da documentação do
GitLab, um dos exemplos mais maduros de documentação tratada como código em
escala (docs-as-code, revisão obrigatória, linters de prosa). Disponível em
[docs.gitlab.com](https://docs.gitlab.com/development/documentation/styleguide/).

<a id="k8s-style"></a>
**Kubernetes Documentation Style Guide**: guia de estilo do projeto
Kubernetes (CNCF), com regras específicas para documentação técnica de
infraestrutura/software de sistemas. Disponível em
[kubernetes.io/docs/contribute/style](https://kubernetes.io/docs/contribute/style/style-guide/).

<a id="gov-uk"></a>
**GOV.UK Content Design / Style guide**: guia de redação do governo
britânico para conteúdo digital voltado ao cidadão, referência amplamente
citada em linguagem simples aplicada a serviços públicos digitais.
Disponível em
[gov.uk/guidance/content-design](https://www.gov.uk/guidance/content-design/writing-for-gov-uk).

## Linguagem simples e acessibilidade

<a id="plain-language"></a>
**Plain Language Guidelines**: diretrizes de linguagem simples do governo
dos EUA (Plain Writing Act de 2010), com técnicas concretas: frases curtas,
voz ativa, evitar nominalizações, uma ideia por frase. Disponível em
[plainlanguage.gov/guidelines](https://www.plainlanguage.gov/guidelines/).

## Normas de nível de obrigatoriedade

<a id="rfc2119"></a>
**RFC 2119**: Scott Bradner, *"Key words for use in RFCs to Indicate
Requirement Levels"* (1997). Define o vocabulário-padrão para expressar
obrigatoriedade em especificações técnicas: MUST, MUST NOT, SHOULD, SHOULD
NOT, MAY. Disponível em
[rfc-editor.org/rfc/rfc2119](https://www.rfc-editor.org/rfc/rfc2119).
Este template traduz e adota esse vocabulário. Ver
[Convenções de escrita](convencoes-de-escrita.md#niveis-de-obrigatoriedade).

<a id="rfc8174"></a>
**RFC 8174**: Barry Leiba, *"Ambiguity of Uppercase vs Lowercase in RFC
2119 Key Words"* (2017). Esclarece que apenas as palavras em maiúsculas
carregam o significado normativo de RFC 2119. Disponível em
[rfc-editor.org/rfc/rfc8174](https://www.rfc-editor.org/rfc/rfc8174).

## Comunidade de documentação

<a id="write-the-docs"></a>
**Write the Docs**: comunidade internacional de profissionais de
documentação técnica, mantenedora de um guia coletivo de práticas
("Documentation Guide") e de conferências dedicadas ao tema. Disponível em
[writethedocs.org/guide](https://www.writethedocs.org/guide/).

## Exemplos de adoção em projetos reais

<a id="django-docs"></a>
**Documentação do Django**: a página "How the documentation is organized"
do projeto Django é um exemplo público e amplamente citado de adoção da
estrutura de quatro tipos em um projeto open source de grande porte.
Disponível em
[docs.djangoproject.com](https://docs.djangoproject.com/en/stable/#how-the-documentation-is-organized).

---

Encontrou uma regra sem citação, ou uma citação que não reflete bem a fonte?
Abra uma issue ou PR. Ver [`CONTRIBUTING.md`](https://github.com/guesant/template-documentacao-tecnica/blob/main/CONTRIBUTING.md).
