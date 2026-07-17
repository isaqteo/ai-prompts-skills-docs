---
titulo: Glossário
categoria: project
tags: [glossario, termos]
versao: 1.0
data_criacao: 2026-07-16
ultima_revisao: 2026-07-16
---

## O que este contexto descreve

Definições curtas dos termos técnicos usados em várias partes deste
repositório, para consulta rápida por humanos e por IAs.

## Conteúdo

- **SKILL.md** — arquivo com front-matter YAML (`name`, `description`) que
  define uma skill: um conjunto de instruções que ensina Claude a executar
  uma tarefa específica de forma consistente. Ver `skills/_template/SKILL.md`.
- **MCP (Model Context Protocol)** — protocolo que permite a Claude se
  conectar a ferramentas externas (ex.: Notion, Google Drive) como
  servidores de ferramentas.
- **ADR (Architecture Decision Record)** — registro curto de uma decisão de
  arquitetura/estrutura relevante, guardado em `docs/decisions/`, incluindo
  o porquê da decisão e as alternativas consideradas.
- **Agenta** — plataforma de gerenciamento e versionamento de prompts. Neste
  repositório, funciona como fonte de verdade para prompts em produção; o
  GitHub funciona como espelho/histórico do que é publicado no Agenta (ver
  `docs/integrations/agenta.md`) — não o contrário.
- **Claude Cowork** — app de trabalho agêntico para tarefas não-técnicas de
  múltiplas etapas, considerado neste repositório como futuro executor das
  edições de conteúdo (ver `docs/workflows/claude-cowork.md`).
- **Bloco de Memória** — bloco de contexto (`## Contexto (manter adiante)`)
  usado pela skill `prompt-master` para evitar que um prompt gerado
  contradiga decisões já tomadas em uma sessão anterior.
- **Prompt Master** — nome da skill em `skills/prompt-master/` (pasta
  historicamente batizada de `prompt-mestre-main` no download original).
- **Karpathy Guidelines** — nome da skill em `skills/karpathy-guidelines/`,
  com quatro princípios de comportamento para reduzir erros comuns de LLMs
  ao programar (pensar antes de codar, simplicidade, mudanças cirúrgicas,
  execução orientada a objetivo).
- **PAT (Personal Access Token)** — token de autenticação do GitHub usado
  temporariamente via HTTPS antes da migração para SSH neste repositório
  (ver `docs/integrations/github.md`).

## Quando incluir este contexto

- Quando uma IA nova (ou uma pessoa nova) precisar de definições rápidas de
  termos usados no restante do repositório, sem precisar ler todos os docs.

## Notas de manutenção
- Adicione um termo aqui sempre que introduzir uma sigla ou conceito novo
  em qualquer doc, skill ou prompt deste repositório.
