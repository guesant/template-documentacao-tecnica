# Convenções de escrita

Referência das regras de estilo e formatação usadas em toda a documentação
deste template. Cada regra cita a fonte de onde vem; a lista completa está em
[Referências](referencias.md). Para princípios de personalidade e tom, veja
[Voz e tom](voz-e-tom.md). Esta página trata do que é objetivamente
verificável: gramática, pontuação, estrutura, formatação, terminologia.

<a id="niveis-de-obrigatoriedade"></a>

## Níveis de obrigatoriedade

Para não deixar ambíguo o que é regra e o que é sugestão, esta seção adota o
vocabulário de [RFC 2119](referencias.md#rfc2119) (Bradner, 1997), traduzido
para português na convenção comum em documentos normativos técnicos. O
esclarecimento de [RFC 8174](referencias.md#rfc8174) (Leiba, 2017) também se
aplica: só as palavras em **maiúsculas** carregam o significado normativo.

| Palavra-chave | Significado |
|---|---|
| **DEVE** / **É OBRIGATÓRIO** | Requisito absoluto. Uma página que viola isso não deve ser mesclada. |
| **NÃO DEVE** | Proibição absoluta. |
| **DEVERIA** / **RECOMENDA-SE** | Forte recomendação. Ignorar exige justificativa explícita no PR. |
| **NÃO DEVERIA** | Forte desaconselhamento, mesma lógica acima. |
| **PODE** | Opcional, a critério de quem escreve. |

As regras abaixo usam esse vocabulário explicitamente sempre que a
obrigatoriedade não for óbvia pelo contexto.

## Idioma, pessoa e tempo verbal

| Regra | Detalhe | Obrigatoriedade |
|---|---|---|
| Idioma | Português (pt-BR) | DEVE |
| Pessoa gramatical | Segunda pessoa ("você"), nunca terceira pessoa distante ("o usuário") | DEVE |
| Voz | Ativa, não passiva ("o comando gera" em vez de "é gerado pelo comando") | DEVERIA |
| Tempo verbal em instruções | Imperativo direto ("execute", "abra") | DEVE |
| Frases | Curtas, uma ideia principal por frase | DEVERIA |

A preferência por segunda pessoa, imperativo e voz ativa aparece de forma
convergente no [Google Developer Documentation Style Guide](referencias.md#google-style),
no [Microsoft Writing Style Guide](referencias.md#microsoft-style) e nas
[Plain Language Guidelines](referencias.md#plain-language). Não é
peculiaridade deste template: é o denominador comum entre guias de estilo de
documentação técnica em português e inglês.

## Pontuação

<a id="uso-do-travessao"></a>

**Travessão (—) com moderação.** É fácil abusar do travessão como muleta
para encadear ideias sem parar para pontuar de verdade, e o resultado é
prosa que cansa de ler. Regra prática:

- NÃO DEVERIA haver mais de um travessão por parágrafo curto (até 4 frases).
- Antes de usar um travessão, teste se um ponto final, vírgula ou dois-pontos
  resolve melhor. Na maioria das vezes resolve.
- PODE usar travessão para uma interrupção genuína no meio da frase (um
  aposto que muda de assunto por um instante), não como conector padrão
  entre duas ideias que já teriam uma pontuação mais simples.
- Revisão de PR DEVE sinalizar parágrafos com uso repetitivo de travessão
  como ponto de atenção de qualidade de prosa, do mesmo jeito que sinaliza
  erro de digitação.

**Aspas retas, não tipográficas.** Use `"..."` e `'...'`, não `"..."` /
`'...'`. Aspas retas copiam e colam sem quebrar em terminais e blocos de
código; é o motivo prático por trás da preferência, não uma questão estética.
O [quality gate de tipografia](qualidade.md) garante isso automaticamente.

<a id="uso-de-codigo-inline"></a>

**Código inline (crase) só para literais, não para ênfase.** Use crase
para nome de arquivo, comando, flag, chave de configuração, valor literal
ou identificador de código: `mkdocs.yml`, `npm run lint`, `timeout`. NÃO
DEVE usar crase para dar destaque a uma palavra comum só porque ela soa
técnica. Se a palavra não é algo que alguém digitaria literalmente num
terminal ou num arquivo de configuração, ela não leva crase; use itálico
ou negrito para ênfase, ou nenhuma marcação. Marcar quase todo substantivo
com crase é um padrão comum em texto gerado por IA e o motivo prático de
banir isso aqui é o mesmo do travessão: dificulta a leitura e sinaliza
descuido em vez de precisão.

## Estrutura de página

| Regra | Detalhe | Obrigatoriedade |
|---|---|---|
| Um assunto por página | Se o título precisa de "e" para descrever o conteúdo, considere dividir | DEVERIA |
| Título | `# Título` único por página (`h1`), descreve o conteúdo sem ambiguidade | DEVE |
| Hierarquia de seções | Sem pular nível (não ir de `##` direto para `####`) | DEVE |
| Nome de arquivo | Minúsculas, hífen como separador, sem acentos (ex.: `configurar-ci.md`) | DEVE |
| Tipo único de conteúdo | Uma página não mistura tutorial, guia, referência e explicação. Ver [Diátaxis](diataxis.md) | DEVE |

Misturar tipos de conteúdo é, segundo a própria origem do framework, a causa
mais comum de documentação confusa (paráfrase de
[Diátaxis](referencias.md#diataxis)). Um "tutorial" cheio de ramificações
condicionais é, na prática, um guia prático disfarçado.

## Formatação

| Situação | Use | Obrigatoriedade |
|---|---|---|
| Sequência de passos | Lista numerada | DEVE |
| Dados comparáveis / tabulares | Tabela | DEVERIA |
| Comando a ser executado | Bloco de código com a linguagem/shell identificada | DEVE |
| Termo técnico na primeira ocorrência | Link para a página de referência que o define | DEVERIA |
| Aviso importante | Bloco `!!! warning` (admonition do MkDocs Material) | DEVERIA |
| Passo opcional dentro de um fluxo | Bloco `!!! note` ou texto explícito "(opcional)" | DEVE |
| Emoji | Nunca. Ver [Quality gates](qualidade.md#emojis) | NÃO DEVE |

## Terminologia

- Cada termo técnico específico do projeto DEVE ter uma definição única em
  `docs/referencia/`. Se duas páginas definem o mesmo termo de formas
  diferentes, isso é um bug de documentação, não uma questão de estilo.
- Um glossário centralizado é recomendado. O [Google Developer Documentation
  Style Guide](referencias.md#google-style) e o [Kubernetes Documentation
  Style Guide](referencias.md#k8s-style) sugerem manter um único ponto de
  verdade para nomes de conceitos, evitando sinônimos concorrentes para a
  mesma coisa.
- Use sempre o mesmo termo para o mesmo conceito ao longo de toda a
  documentação. Não alterne "usuário", "pessoa usuária" e "cliente" para a
  mesma entidade sem motivo.
- Siglas DEVEM ser expandidas por extenso na primeira ocorrência de cada
  página, mesmo que já tenham aparecido em outra.

## Acessibilidade e inclusão

- Texto alternativo (`alt`) DEVE ser escrito para toda imagem que carregue
  informação (não decorativa).
- Links NÃO DEVEM usar texto genérico como "clique aqui". O texto do link
  DEVE descrever o destino, prática recomendada tanto pelo
  [Google Developer Documentation Style Guide](referencias.md#google-style)
  quanto pelo [GOV.UK Style guide](referencias.md#gov-uk), por afetar
  diretamente leitores de tela.
- Linguagem inclusiva e livre de viés DEVE ser usada. Evite termos que
  presumam gênero, capacidade física ou contexto cultural não universal,
  seguindo a orientação de bias-free communication do
  [Microsoft Writing Style Guide](referencias.md#microsoft-style).
- Prefira frases curtas e vocabulário comum a construções rebuscadas. Texto
  mais simples é mais acessível a leitores não nativos, a pessoas
  neurodivergentes e a ferramentas de tradução automática, argumento central
  das [Plain Language Guidelines](referencias.md#plain-language).

## Código de exemplo

- Todo bloco de código DEVE ser executável como está. Teste antes de
  commitar.
- Exemplos mínimos e reais são preferíveis a pseudocódigo (DEVERIA).
- A linguagem do bloco DEVE ser identificada (` ```bash `, ` ```yaml `, etc.),
  tanto para realce de sintaxe quanto para leitores de tela.
- Placeholders em exemplos DEVEM seguir um padrão visualmente óbvio (ex.:
  `<seu-token>`, `SEU_PROJETO`), nunca valores reais nem que pareçam reais.

## Links

- Links internos DEVEM ser relativos ao arquivo atual (ex.:
  `../referencia/index.md`), não absolutos ao domínio publicado.
- `mkdocs build --strict` DEVE passar sem erros antes do merge. Ele falha
  o build se houver link interno quebrado.
- Links externos para fontes citadas DEVEM apontar para a origem primária
  (documentação oficial, RFC, especificação), não para resumos de terceiros.

## O que é permitido

- PODE haver opinião e comparação de alternativas em páginas de
  [Explicação](../explicacoes/index.md). É o único tipo de conteúdo em que
  isso é esperado.
- PODE haver reformulação de uma regra desta página para o contexto
  específico de um projeto que adote este template. Ver
  [Contribuindo](index.md).
- PODE haver mais de um exemplo de código por página quando ilustram
  variações relevantes (ex.: dois shells diferentes).

## O que não é permitido

- NÃO DEVE haver TODOs ou rascunhos em conteúdo publicado na branch `main`.
  Use branch/PR de rascunho até o texto estar pronto.
- NÃO DEVE haver duplicação de conteúdo entre páginas. Prefira linkar para
  a fonte única (princípio DRY aplicado à documentação, defendido também
  pelo [GitLab Documentation Style Guide](referencias.md#gitlab-style)).
- NÃO DEVE haver mistura de tipos de conteúdo Diátaxis na mesma página.
- NÃO DEVE haver captura de tela ou trecho de código com dado sensível real
  (token, senha, PII), nem mesmo "para depois trocar".
- NÃO DEVE haver link "clique aqui" ou equivalente sem valor descritivo.
- NÃO DEVE haver emoji em nenhum conteúdo publicado.
- NÃO DEVE haver caractere invisível, aspa tipográfica ou caractere fora do
  alfabeto latino padrão de prosa em português técnico. Ver
  [Quality gates](qualidade.md).

## Ver também

- [Voz e tom](voz-e-tom.md)
- [Por que a documentação é organizada em quatro tipos](diataxis.md)
- [Como escrever uma página de documentação](como-escrever-documentacao.md)
- [Quality gates: como essas regras são verificadas automaticamente](qualidade.md)
- [Referências](referencias.md)
