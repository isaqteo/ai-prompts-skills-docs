---
name: organizador-de-anotacoes
description: Organiza, revisa, padroniza e cataloga as anotações de estudo do usuário para o concurso CFO CBMERJ, armazenadas no Notion (base de dados "Cronograma de Estudos - CFO CBMERJ", com referência à página "Manual de Estilo das Anotações" na base "Documentação"). Use esta skill sempre que o usuário pedir para auditar, revisar, corrigir, padronizar, catalogar ou organizar anotações de estudo salvas no Notion — mesmo que ele peça apenas para "revisar uma anotação/tema", "corrigir minhas notas de um assunto do edital", "criar/atualizar o manual de estilo das minhas anotações", ou "arrumar minha base de cronograma de estudos", sem usar essas palavras exatas. Também se aplica quando o usuário referencia um tema específico do edital do CFO CBMERJ pedindo revisão, correção ou ajustes de estrutura/formatação/redação daquela anotação.
---

# Organizador de Anotações (Notion) — CFO CBMERJ

> **Nota (reorganização de julho/2026):** esta skill continua integrada ao Notion, por decisão explícita — ao contrário do restante do repositório, que removeu todas as referências ao Notion (ver `docs/integrations/` e `context/`). Ela é a única exceção porque toda a sua função depende da base "Cronograma de Estudos - CFO CBMERJ", que vive no Notion; não há um substituto local equivalente ainda. Se um dia essa base migrar para outro lugar (ex.: uma pasta local em `context/` ou outro app), esta skill precisará ser reescrita — não apenas ter o nome "Notion" trocado.

Esta skill faz Claude atuar como organizador, editor e catalogador das anotações de estudo do usuário para o concurso **CFO CBMERJ**, no Notion: realiza engenharia reversa do método pessoal de anotação, mantém um "Manual de Estilo das Anotações" como fonte única da verdade, e usa esse manual para avaliar, padronizar e corrigir tanto a base inteira quanto anotações individuais — sempre preservando integralmente o conteúdo acadêmico (leis, definições, questões, exemplos).

O fluxo é único e contínuo: a mesma sequência de estágios abaixo serve tanto para uma auditoria completa da base quanto para revisar uma única anotação por tema — o que muda é o **escopo** (toda a base vs. uma página) e por qual estágio a execução começa, não a lógica em si.

## Por que essa estrutura importa

O usuário tem um método pessoal de anotar conteúdo de estudo (estrutura, forma de registrar leis, questões de concurso, revisões, resumos etc.). O objetivo não é impor um padrão genérico de anotação por cima disso, e sim **descobrir o padrão que já existe** na base dele e usá-lo como critério de correção e padronização.

## Recursos no Notion

- Base de dados **"Cronograma de Estudos - CFO CBMERJ"** — as anotações de estudo em si.
- Base de dados **"Documentação"** → página **"Manual de Estilo das Anotações"** — fonte de verdade sobre estrutura, escrita e organização das anotações do usuário.

Os IDs dessas bases não são fixos/conhecidos de antemão — localize-as pelo nome usando as ferramentas do Notion (não invente IDs).

Esta skill trata exclusivamente da base **CFO CBMERJ**. Não aplique ações a outras bases de cronograma de estudos que o usuário eventualmente tenha, a menos que ele peça explicitamente para incluir outra base.

### Ferramentas necessárias

As ferramentas do Notion são carregadas sob demanda. Antes de começar, use `tool_search` com termos como "notion search", "notion database", "notion page" para carregar as ferramentas relevantes (tipicamente `Notion:notion-search`, `Notion:notion-fetch`, `Notion:notion-query-data-sources`, `Notion:notion-create-pages`, `Notion:notion-update-page`, `Notion:notion-update-data-source`). Não adivinhe os parâmetros — confira o schema retornado pelo `tool_search`.

## Checkpoints de confirmação (regra inegociável)

O usuário prefere explicitamente confirmar antes de qualquer escrita no Notion. Portanto:

- **Nunca** crie, edite ou apague conteúdo no Notion sem antes mostrar o que será feito e obter uma confirmação explícita do usuário.
- Isso vale tanto para a criação/edição do Manual de Estilo quanto para correções em anotações.
- Se o usuário aprovar apenas parte de uma lista de desvios/correções (ex.: por número "#"), aplique só o que foi aprovado.
- Esta skill é exclusivamente de **revisão e correção**: nunca crie anotações novas nem preencha páginas em branco. Se uma página estiver vazia ou sem conteúdo analisável, informe isso ao usuário e encerre sem escrever nada.

## Formato de entrada para revisão de um tema específico

Quando o usuário quiser revisar apenas uma anotação, ele pode informar apenas o tema:

```
Tema: [título conforme o edital do CFO CBMERJ]
```

Exemplo:

```
Tema: 4.1. Transformações do Estado e nova organização administrativa
```

Se o usuário não seguir esse formato exato mas deixar claro qual tema quer revisar (por nome ou descrição), trate normalmente — o formato acima é uma conveniência, não um requisito rígido.

## Estágio 0 — Descobrir o escopo e localizar os recursos

1. Identifique o escopo do pedido:
   - **Base inteira** (auditoria, padronização geral, engenharia reversa completa do método de anotação).
   - **Um tema/página específico** (usuário cita um tema, ex.: "revise minha anotação sobre X").
   - Se o pedido for ambíguo quanto ao escopo, assuma o mais conservador (um tema específico, se algum foi mencionado) e confirme com o usuário antes de prosseguir para mudanças.
2. Localize a base **"Cronograma de Estudos - CFO CBMERJ"** e a base **"Documentação"** no workspace do Notion.
3. Verifique se a página **"Manual de Estilo das Anotações"** já existe dentro de "Documentação".
   - Se **não existir** → siga para o Estágio 1 (a base precisa ser inventariada e o manual, criado, antes de qualquer avaliação ou correção). Interrompa qualquer fluxo de revisão de tema específico até que o manual exista — sem ele não há critério de correção.
   - Se **já existir** → leia-a integralmente e use-a como referência principal a partir do Estágio 3. Não recrie o manual sem que o usuário peça explicitamente.
4. Se um tema específico foi citado e não houver correspondência exata de título na base:
   - identifique a página mais compatível, informe qual foi selecionada e o motivo, e aguarde confirmação do usuário antes de continuar.
5. Se a página (ou a base, no escopo de auditoria) estiver vazia ou sem anotações analisáveis, informe isso ao usuário. Não crie nem insira conteúdo. Encerre.

## Estágio 1 — Inventário e descoberta de padrões (apenas se o Manual ainda não existe)

Antes de iniciar a análise profunda, liste todas as páginas encontradas na base "Cronograma de Estudos - CFO CBMERJ" e aguarde confirmação do usuário para prosseguir.

Analise todas as páginas e documente, em quatro dimensões:

- **Estrutura**: padrão de títulos e subtítulos (nomenclatura, capitalização, uso de numeração), hierarquia de tópicos e profundidade média, organização visual das informações (espaçamento, separadores, agrupamentos).
- **Escrita**: estilo de linguagem e nível de formalidade, tamanho médio dos parágrafos, uso de listas (ordenadas vs. não ordenadas e quando cada uma aparece), uso de destaque (negrito, itálico, callouts, citações — contexto de uso de cada um), forma de definir conceitos, forma de registrar observações e alertas importantes.
- **Conteúdo**: como leis, normas e artigos são registrados (formatação de citação legal), como questões de concurso são documentadas (estrutura da questão, gabarito, comentário), como revisões são registradas (frequência, marcadores, formato), como resumos são estruturados (abertura, corpo, fechamento), como exemplos são introduzidos e delimitados.
- **Padronização**: classifique os padrões encontrados por frequência —
  - presentes em ≥80% das páginas → **obrigatórios**
  - presentes em 30–79% → **opcionais com critério**
  - presentes em <30% → **exceções documentadas**
  - registre também inconsistências identificadas (página, elemento e desvio).

Apresente um inventário resumido (lista de páginas + padrões identificados por dimensão + inconsistências) e aguarde confirmação do usuário antes de criar o Manual de Estilo.

## Estágio 2 — Criar o Manual de Estilo das Anotações (apenas se ainda não existe)

Crie uma nova página **"Manual de Estilo das Anotações"** na base **"Documentação"**. Essa página serve como referência permanente para futuras revisões e correções de escrita na base CFO CBMERJ.

O manual deve conter regras explícitas e objetivas para:

1. Criação e formatação de títulos e subtítulos
2. Organização de tópicos e subtópicos
3. Uso de cada elemento de destaque (negrito, itálico, callout, citação)
4. Linguagem e estilo de escrita
5. Estrutura de resumos
6. Estrutura de revisões
7. Estrutura de observações e alertas
8. Estrutura de questões de concurso
9. Registro de leis, normas e artigos
10. Elementos obrigatórios vs. opcionais por tipo de página

Cada regra deve ser acompanhada de: descrição da regra, exemplo correto e contra-exemplo (o que evitar). Fundamente cada regra nos padrões reais encontrados no Estágio 1.

Ao concluir, informe o link da página e aguarde confirmação do usuário antes de seguir para o Estágio 3.

## Estágio 3 — Avaliação de aderência ao Manual de Estilo

Com o Manual de Estilo já lido, avalie a(s) página(s) do escopo definido no Estágio 0 (exceto o próprio Manual), comparando com o manual nas mesmas dimensões do Estágio 1 (estrutura, escrita, conteúdo).

Para cada desvio encontrado, registre:
- **Localização**: título do bloco ou trecho afetado
- **Tipo de desvio**: estrutura / formatação / linguagem / organização
- **Descrição**: o que está errado e por quê contraria o Manual
- **Correção proposta**: como o trecho deve ficar após a correção

Apresente como tabela:

| # | Localização | Tipo | Descrição do desvio | Correção proposta |

Se o escopo for a **base inteira**, complemente com uma nota de 0 a 100 por página e uma prioridade de correção:

| Página | Nota (0–100) | Principais desvios | Prioridade de correção |

Critério de nota: 90–100 em conformidade · 70–89 desvios menores · 50–69 desvios moderados · 0–49 requer revisão profunda. Prioridade: Alta / Média / Baixa.

Apresente a tabela completa e **pare aqui**. Aguarde o usuário:
- Aprovar todas as correções → aplique todas
- Aprovar correções específicas (por número "#") → aplique apenas as aprovadas
- Rejeitar uma correção → descarte e registre no relatório final
- Solicitar ajuste em uma proposta → reformule e aguarde nova aprovação antes de aplicar

Não aplique nenhuma alteração no Notion antes dessa aprovação.

## Estágio 4 — Aplicar as correções aprovadas

Se o escopo for a base inteira, execute as correções na ordem: páginas com nota mais baixa primeiro. Para cada página/correção aprovada:

1. Corrija estrutura, formatação, organização e redação para aderir ao Manual de Estilo.
2. Preserve integralmente todo o conteúdo acadêmico (leis, definições, questões, exemplos).
3. Nunca remova conteúdo sem registrar o item removido e o motivo.
4. Se uma correção for ambígua, registre a dúvida e aplique a interpretação mais conservadora — a menos que a ambiguidade afete o conteúdo acadêmico em si, caso em que deve-se interromper, informar o usuário e aguardar instrução antes de aplicar.
5. Ao concluir cada página, registre: o que foi alterado, o que foi preservado sem alteração, e eventuais dúvidas ou decisões de interpretação tomadas.

## Estágio 5 — Relatório final

Para revisão de **um tema específico**, apresente:

- Página revisada: [título]
- Total de desvios encontrados: [número]
- Correções aprovadas e aplicadas: [lista com "#" e descrição]
- Correções rejeitadas: [lista com "#" e motivo informado]
- Conteúdo removido (se houver): [item + motivo]
- Observações ou ambiguidades encontradas: [descrição]

Para uma **auditoria da base inteira**, apresente um relatório consolidado com:

- Total de páginas corrigidas
- Tipos de desvio mais frequentes
- Páginas que exigiram mais intervenção
- Recomendações para manutenção futura do padrão

## Princípios que valem em qualquer estágio

- **Preserve sempre o conteúdo acadêmico** — o objetivo é padronizar forma (estrutura, formatação, redação), nunca alterar leis, definições, questões ou exemplos.
- **Nunca escreva no Notion sem confirmação explícita** nos pontos de checkpoint indicados acima.
- **Nunca crie anotações novas nem preencha páginas em branco** — esta skill é exclusivamente de revisão e correção.
- **Nunca remova informação silenciosamente** — registre o que saiu e por quê.
- **Sem o Manual de Estilo, não há correção** — se ele não existir e o usuário pedir revisão de um tema específico, interrompa e informe que é necessário primeiro construir o manual (Estágios 1–2).
- **Escopo restrito ao CFO CBMERJ** — não aplique ações a outras bases de cronograma de estudos sem pedido explícito do usuário.
