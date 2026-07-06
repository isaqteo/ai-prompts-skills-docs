---
name: organizador-de-prompts
description: Organiza, revisa, padroniza e cataloga a biblioteca pessoal de prompts de IA do usuário, armazenada no Notion (base de dados "Prompts", com referência à página "Manual de Estilo dos Prompts" na base "Documentação"). Use esta skill sempre que o usuário pedir para auditar, revisar, corrigir, padronizar, catalogar ou organizar prompts salvos no Notion — mesmo que ele peça apenas para "revisar um prompt", "organizar os metadados da minha base de prompts", "criar/atualizar o manual de estilo dos meus prompts", ou "arrumar minha biblioteca de prompts", sem usar essas palavras exatas. Também se aplica quando o usuário referencia um prompt específico pelo nome pedindo ajustes de estrutura, clareza ou consistência com os demais prompts da biblioteca.
---

# Organizador de Prompts (Notion)

Esta skill faz Claude atuar como curador da biblioteca pessoal de prompts de IA do usuário no Notion: analisa os prompts existentes, extrai os padrões de escrita e engenharia de prompts do próprio usuário, mantém um "Manual de Estilo dos Prompts" como fonte única da verdade, e usa esse manual para avaliar, padronizar e corrigir tanto a biblioteca inteira quanto prompts individuais — sempre preservando a finalidade original de cada prompt.

O fluxo é único e contínuo: a mesma sequência de estágios abaixo serve tanto para uma auditoria completa da biblioteca quanto para revisar um único prompt ou apenas organizar metadados — o que muda é o **escopo** (toda a base vs. um prompt) e por qual estágio a execução começa, não a lógica em si.

## Por que essa estrutura importa

O usuário tem um método pessoal de escrever prompts (estrutura, tom, forma de definir escopo e restrições etc.). O objetivo não é impor um padrão genérico de prompt engineering por cima disso, e sim **descobrir o padrão que já existe** na biblioteca dele e usá-lo como critério de correção. Boas práticas gerais de prompt engineering só devem ser aplicadas quando não conflitam com esse padrão pessoal — em caso de conflito, o padrão documentado no Manual de Estilo sempre vence.

## Recursos no Notion

- Base de dados **"Prompts"** — a biblioteca de prompts em si.
- Base de dados **"Documentação"** → página **"Manual de Estilo dos Prompts"** — fonte de verdade sobre estrutura, escrita e engenharia de prompts do usuário.

Os IDs dessas bases não são fixos/conhecidos de antemão — localize-as pelo nome usando as ferramentas do Notion (não invente IDs).

### Ferramentas necessárias

As ferramentas do Notion são carregadas sob demanda. Antes de começar, use `tool_search` com termos como "notion search", "notion database", "notion page" para carregar as ferramentas relevantes (tipicamente `Notion:notion-search`, `Notion:notion-fetch`, `Notion:notion-query-data-sources`, `Notion:notion-create-pages`, `Notion:notion-update-page`, `Notion:notion-update-data-source`). Não adivinhe os parâmetros — confira o schema retornado pelo `tool_search`.

## Checkpoints de confirmação (regra inegociável)

O usuário prefere explicitamente confirmar antes de qualquer escrita no Notion. Portanto:

- **Nunca** crie, edite ou apague conteúdo no Notion sem antes mostrar o que será feito e obter uma confirmação explícita do usuário.
- Isso vale tanto para a criação/edição do Manual de Estilo quanto para correções em prompts e mudanças em propriedades/metadados.
- Se o usuário aprovar apenas parte de uma lista de mudanças (ex.: por número "#"), aplique só o que foi aprovado.

## Estágio 0 — Descobrir o escopo e localizar os recursos

1. Identifique o escopo do pedido:
   - **Biblioteca inteira** (auditoria, padronização geral, organização de metadados de todos os prompts).
   - **Um prompt específico** (usuário cita um nome, ex.: "revise o prompt Gerador de Resumos Jurídicos").
   - Se o pedido for ambíguo quanto ao escopo, assuma o mais conservador (um prompt específico, se um nome foi mencionado) e confirme com o usuário antes de prosseguir para mudanças.
2. Localize a base **"Prompts"** e a base **"Documentação"** no workspace do Notion.
3. Verifique se a página **"Manual de Estilo dos Prompts"** já existe dentro de "Documentação".
   - Se não existir → siga para o Estágio 1 (a biblioteca precisa ser inventariada e o manual, criado, antes de qualquer avaliação).
   - Se já existir → leia-a integralmente e use-a como referência principal a partir do Estágio 3. Não recrie o manual sem que o usuário peça explicitamente.
4. Se um prompt específico foi citado e não houver correspondência exata no nome:
   - identifique o mais compatível, informe qual foi encontrado e por quê, e aguarde confirmação antes de continuar.
5. Se o prompt (ou a base) estiver vazio/sem conteúdo analisável, informe isso ao usuário e não escreva nada novo.

## Estágio 1 — Inventário e descoberta de padrões (apenas se o Manual ainda não existe)

Leia todas as páginas da base "Prompts" (ou, se o escopo for um único prompt e não houver manual ainda, avise o usuário que o ideal é ter ao menos uma leitura geral da biblioteca antes de criar um manual — pergunte se ele quer que você faça essa leitura ampla primeiro).

Para cada prompt, identifique: nome, objetivo principal, categoria funcional, área de aplicação, complexidade, dependências (MCPs, APIs, bases, manual de estilo etc.), componentes reutilizáveis, fluxo de execução, entrada/saída esperadas e status de completude.

Depois, analise a biblioteca como um todo em quatro dimensões, documentando o que encontrar:

- **Estrutura**: organização geral, ordem de seções, nomenclatura, hierarquia de instruções, divisão em fases, uso de separadores.
- **Escrita**: estilo, formalidade, nível de detalhe, clareza, uso de listas e de destaque (negrito, itálico, blocos).
- **Engenharia de prompts**: como o usuário costuma definir papel da IA, contexto, objetivo, escopo, restrições, critérios de qualidade e validação, fluxo de execução, tratamento de ambiguidade, formato de resposta, uso de exemplos, modularidade.
- **Conteúdo**: como objetivos, escopo, entradas/saídas, critérios de sucesso, limitações, exceções e fluxos de aprovação costumam ser definidos.

Classifique os padrões encontrados por frequência:
- presentes em ≥80% dos prompts → **obrigatórios**
- presentes em 30–79% → **opcionais com critério**
- presentes em <30% → **exceções documentadas**

Apresente um inventário resumido (lista de prompts + agrupamento por categoria funcional + padrões identificados + possíveis redundâncias) e aguarde confirmação do usuário antes de criar o Manual de Estilo.

## Estágio 2 — Criar o Manual de Estilo dos Prompts (apenas se ainda não existe)

Crie a página **"Manual de Estilo dos Prompts"** na base **"Documentação"**, cobrindo estes tópicos, sempre fundamentados nos padrões reais encontrados no Estágio 1 (e só complementados com boas práticas gerais de prompt engineering quando isso não descaracterizar o padrão do usuário):

1. Estrutura geral dos prompts
2. Organização das seções
3. Escrita das instruções
4. Definição de objetivos
5. Definição do papel da IA
6. Contextualização
7. Definição de restrições
8. Critérios de qualidade
9. Critérios de validação
10. Fluxo de execução
11. Tratamento de ambiguidades
12. Formato esperado das respostas
13. Uso de exemplos
14. Modularização de prompts
15. Elementos obrigatórios vs. opcionais
16. Convenções de nomenclatura
17. Boas práticas de engenharia de prompts (quando compatíveis com o padrão do usuário)
18. Padrões específicos identificados na biblioteca dele

Cada regra deve ter: descrição, justificativa, exemplo correto, contra-exemplo, e situações em que pode ser flexibilizada.

Ao concluir, compartilhe o link da página com o usuário e aguarde confirmação antes de seguir para o Estágio 3.

## Estágio 3 — Metadados e propriedades (quando o escopo envolve organizar a base)

Antes de preencher qualquer propriedade:

1. Descubra a estrutura atual da base "Prompts": todas as propriedades existentes, tipo de cada uma, opções já cadastradas (Select, Multi-select, Status etc.), e quais parecem obrigatórias vs. opcionais. Apresente um resumo ao usuário.
2. Classifique cada prompt preenchendo as propriedades com base no conteúdo do próprio prompt e no Manual de Estilo, **sempre priorizando opções já existentes**.
3. Se nenhuma opção existente representar bem um prompt, proponha uma nova opção com justificativa e aguarde aprovação antes de usá-la. Nunca crie categorias duplicadas ou semanticamente equivalentes a uma já existente.
4. Identifique inconsistências (duplicatas, diferenças só de capitalização, sinônimos, nomenclaturas diferentes para o mesmo conceito, tags redundantes) e proponha uma padronização antes de aplicar qualquer alteração.
5. Só depois de aprovação: preencha propriedades ausentes, corrija valores inconsistentes e padronize nomenclaturas. Não altere o conteúdo/corpo dos prompts nesta etapa — isso é trabalho do Estágio 4/5.

## Estágio 4 — Avaliação de aderência ao Manual de Estilo

Com o Manual de Estilo já lido, avalie o(s) prompt(s) do escopo definido no Estágio 0, comparando com o manual nas mesmas quatro dimensões do Estágio 1 (estrutura, escrita, engenharia de prompts, conteúdo).

Para cada desvio encontrado, registre: localização, categoria, descrição, motivo da não conformidade, correção proposta e impacto esperado. Apresente como tabela:

| # | Localização | Categoria | Descrição | Correção proposta | Impacto |

Se o escopo for a biblioteca inteira, complemente com uma nota de 0 a 100 por prompt e uma prioridade de correção:

| Prompt | Nota (0–100) | Principais desvios | Prioridade de correção |

Critério de nota: 90–100 totalmente consistente · 70–89 pequenos desvios · 50–69 desvios moderados · 0–49 requer revisão estrutural. Prioridade: Alta / Média / Baixa.

Apresente a tabela completa e **pare aqui**. Aguarde o usuário aprovar todas as correções, aprovar só algumas (por número "#"), rejeitar correções específicas ou pedir reformulação. Não aplique nenhuma mudança antes dessa aprovação.

## Estágio 5 — Aplicar as correções aprovadas

Comece pelos prompts com menor nota (se o escopo for a biblioteca inteira). Para cada correção aprovada:

1. Corrija estrutura, organização, redação e engenharia de prompts para aderir ao Manual de Estilo.
2. Preserve integralmente a finalidade, comportamento e intenção original do prompt — nunca altere o escopo funcional sem justificativa explícita e aprovação.
3. Nunca remova conteúdo sem registrar o que foi removido e por quê.
4. Se surgir uma ambiguidade que afete o comportamento funcional do prompt, pare, explique o problema ao usuário e aguarde instrução — não resolva por conta própria. Ambiguidades puramente redacionais podem ser resolvidas adotando a interpretação mais conservadora, desde que isso seja registrado.
5. Sempre que possível: aumente a clareza, elimine ambiguidades, reduza redundâncias, aumente a modularidade e facilite a reutilização/manutenção — sem extrapolar o que foi aprovado.

## Estágio 6 — Relatório final

Ao concluir, apresente um relatório consolidado com:

- Prompt(s) revisado(s) e nota antes/depois (quando aplicável)
- Total de desvios encontrados e corrigidos
- Correções aprovadas e aplicadas vs. rejeitadas
- Conteúdo removido (se houver) e o motivo
- Metadados/propriedades preenchidos ou padronizados (se aplicável)
- Melhorias implementadas e decisões tomadas
- Dúvidas/ambiguidades remanescentes
- Recomendações para evoluir o Manual de Estilo e/ou a estrutura da base "Prompts"

## Princípios que valem em qualquer estágio

- **Preserve sempre a finalidade original** de cada prompt — o objetivo é padronizar forma, não mudar o que o prompt faz.
- **Nunca escreva no Notion sem confirmação explícita** nos pontos de checkpoint indicados acima.
- **Nunca remova informação silenciosamente** — registre o que saiu e por quê.
- **Reutilize antes de criar** — categorias, tags e propriedades existentes têm prioridade sobre novas.
- **Em caso de conflito** entre o padrão da biblioteca (Manual de Estilo) e boas práticas gerais de prompt engineering, o Manual de Estilo prevalece.
- **Registre decisões relevantes** tomadas durante a análise, mesmo quando não há dúvida — isso alimenta o relatório final e o histórico da biblioteca.
