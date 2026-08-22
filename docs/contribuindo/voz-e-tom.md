# Voz e tom

**Voz** é a personalidade consistente da documentação. Não muda de página
para página. **Tom** é a inflexão dessa voz conforme o contexto: o mesmo
projeto soa diferente numa mensagem de erro crítico e num tutorial de boas-
vindas. Essa distinção é central em praticamente todo guia de estilo
consultado para este template (ver [Referências](referencias.md)) e vale a
pena manter explícita, porque as duas coisas quebram por motivos diferentes.

## Princípios de voz adotados

| Princípio | O que significa aqui | Fonte |
|---|---|---|
| Direta e sem enrolação | Vá ao ponto na primeira frase do parágrafo; contexto vem depois, se for necessário | [Google Developer Documentation Style Guide](referencias.md#google-style) |
| Acolhedora, não condescendente | Explique sem presumir ignorância nem exibir conhecimento; trate quem lê como colega capaz | [Microsoft Writing Style Guide](referencias.md#microsoft-style) |
| Confiante, não hesitante | Evite "talvez", "provavelmente", "acho que" em instruções. Se não há certeza, isso é um problema de conteúdo, não de tom | [Microsoft Writing Style Guide](referencias.md#microsoft-style) |
| Humana, não corporativa | Prefira linguagem natural a jargão de marketing ou burocratês institucional | [GOV.UK Style guide](referencias.md#gov-uk) |
| Consistente entre páginas | A voz não muda por quem escreveu a página — normalize em revisão | [GitLab Documentation Style Guide](referencias.md#gitlab-style) |

A Microsoft resume seus quatro atributos de voz como algo como "caloroso e
acolhedor", "direto e claro", "pronto para ajudar" e "vivo e interessante"
(paráfrase de [Microsoft Writing Style Guide](referencias.md#microsoft-style)).
Não copiamos os quatro atributos ao pé da letra, mas adotamos o espírito:
calor humano sem perder precisão técnica.

## Segunda pessoa, voz ativa

- Escreva para "você" (segunda pessoa), nunca em terceira pessoa distante
  ("o usuário deve...") nem em primeira pessoa do plural artificial ("nós
  recomendamos que..." quando quem fala é a documentação, não uma equipe
  específica).
- Prefira voz ativa: "o comando gera um arquivo" em vez de "um arquivo é
  gerado pelo comando". Voz passiva esconde quem faz a ação e normalmente
  torna a frase mais longa. É recomendação recorrente em
  [Plain Language Guidelines](referencias.md#plain-language) e no
  [Google Developer Documentation Style Guide](referencias.md#google-style).
- Em instruções, use o imperativo direto ("execute", "abra", "confirme"),
  não construções indiretas ("você deveria executar", "seria necessário
  abrir").

## Tom por contexto

O tom se ajusta ao tipo de página (ver [Diátaxis](diataxis.md)) e à
gravidade do que está sendo comunicado:

| Contexto | Tom esperado | Exemplo de abertura |
|---|---|---|
| Tutorial | Encorajador, passo a passo, comemora pequenas vitórias | "Ao final desta página, você terá..." |
| Guia prático | Direto ao objetivo, sem rodeios | "Para configurar X, faça o seguinte." |
| Referência | Neutro, descritivo, sem opinião | "O campo `timeout` aceita valores em segundos." |
| Explicação | Mais discursivo, pode comparar alternativas e ter posição | "Escolhemos X em vez de Y porque..." |
| Aviso de risco / breaking change | Sério, sem eufemismo, sem tentar suavizar consequência real | "Esta mudança quebra clientes que dependem de Y. Migre antes de atualizar." |

Avisos de risco não seguem o tom acolhedor padrão. Clareza sobre
consequência tem prioridade sobre gentileza de tom, prática alinhada ao que
o [GOV.UK Style guide](referencias.md#gov-uk) chama de ser direto mesmo
quando a notícia é ruim.

## O que evitar

- **Humor que não envelhece bem.** Piadas internas, referências culturais
  datadas ou trocadilhos que dependem de contexto não documentado.
- **Metáforas que substituem definição técnica.** Uma analogia pode ajudar
  a intuição, mas não deve ser a única explicação de um termo técnico.
  Sempre acompanhe de uma definição precisa (ligue para a página de
  [Referência](../referencia/index.md) correspondente).
- **Diminutivos e informalidade excessiva** ("rapidinho", "sem stress").
  Quebram consistência de tom e não traduzem bem para leitura automatizada
  ou tradução futura.
- **Passiva burocrática** ("Foi decidido que...", "Recomenda-se que
  sejam verificados os logs"). Prefira dizer quem decide e o que fazer.
- **Certeza falsa.** Não afirme que algo "nunca falha" ou "sempre funciona".
  Documentação técnica erra menos quando é honesta sobre limites.
- **Travessão como muleta de escrita.** Ver a regra em
  [Convenções de escrita](convencoes-de-escrita.md#uso-do-travessao). É um
  problema de tom, não só de pontuação: encadear ideias com travessão em
  vez de parar para pontuar de verdade é o jeito mais comum de uma frase
  soar apressada em vez de confiante.

## Exemplos: antes e depois

Aplicar as regras acima na prática, com reescritas reais deste próprio
projeto.

**Passiva e travessão em excesso, versão antes:**

> "A configuração é lida pelo comando na inicialização — e caso um valor
> inválido seja encontrado, um erro é reportado — o que pode ser evitado
> validando o arquivo antes."

**Ativa, direta, um travessão a menos, versão depois:**

> "O comando lê a configuração na inicialização. Se encontrar um valor
> inválido, reporta um erro. Valide o arquivo antes para evitar isso."

**Hesitante e passiva burocrática, versão antes:**

> "Talvez seja necessário que o token seja renovado, e recomenda-se que
> isso seja feito antes da expiração."

**Confiante e ativa, versão depois:**

> "Renove o token antes de ele expirar."

## Ver também

- [Convenções de escrita](convencoes-de-escrita.md) — regras objetivas de
  formatação e estrutura, incluindo os níveis de obrigatoriedade (DEVE,
  DEVERIA, PODE).
- [Por que a documentação é organizada em quatro tipos](diataxis.md) —
  como o tipo de página influencia o tom.
