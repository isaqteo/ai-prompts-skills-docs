# Workflow do Claude Cowork

Plano de adoção do Claude Cowork como executor de atualizações de conteúdo
neste repositório, em paralelo à edição manual via VSCode.

## Status atual

Ainda não adotado. A intenção de longo prazo, registrada desde a
configuração inicial deste repositório, é usar o Cowork para realizar
atualizações de conteúdo (prompts, skills, docs) depois de assinado o Plano
Pro correspondente.

## Boas práticas previstas para quando o Cowork for adotado

Para evitar conflitos entre edições manuais (VSCode + `git push` local) e
edições feitas pelo Cowork:

1. **Sempre `git pull` antes de iniciar qualquer sessão de edição** —
   tanto manual quanto via Cowork. Esta é a mesma recomendação já registrada
   em `docs/workflows/git-workflow.md`, e passa a valer com dobro de
   importância quando duas "fontes de edição" diferentes (uma pessoa e um
   agente) trabalham no mesmo repositório.
2. Evite sessões manuais e sessões do Cowork simultâneas sobre os mesmos
   arquivos. Se precisar rodar as duas em paralelo, mantenha-as em partes
   diferentes da árvore (ex.: uma pessoa em `docs/`, o Cowork em `prompts/`).
3. Revise o diff gerado pelo Cowork antes de aceitar/commitar, do mesmo jeito
   que se revisaria uma mudança de qualquer outro colaborador.
4. Trate o Cowork como mais um consumidor das convenções já documentadas em
   `context/project/conventions.md` e `context/writing-style/` — ele deve
   seguir os mesmos padrões de nomenclatura e formatação que uma edição
   manual seguiria.

## Relação com o Agenta

O Cowork e o Agenta (ver `docs/workflows/agenta-workflow.md`) são dois
mecanismos de atualização de conteúdo distintos, com fontes de verdade
diferentes: o Agenta é fonte de verdade para prompts publicados/versionados
na plataforma; o Cowork é um executor de tarefas sobre o repositório local
como um todo. Se os dois passarem a operar ao mesmo tempo sobre `prompts/`,
esse é um ponto que precisará de uma convenção explícita adicional (ainda
não definida).
