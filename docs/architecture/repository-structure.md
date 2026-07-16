# Estrutura do Repositório

Este documento descreve a árvore de pastas do repositório `ai-prompts-skills-docs`
e o propósito de cada uma, após a reorganização de julho/2026.

## Visão geral

```
ai-prompts-skills-docs/
├── docs/          # Documentação para humanos
├── context/       # Conhecimento reutilizável por IAs
├── prompts/       # Prompts prontos, por ferramenta
├── skills/        # Skills no formato SKILL.md
├── templates/     # Modelos para criar prompts/contexto/personas/skills novos
├── examples/      # Exemplos concretos de entrada/saída
├── resources/     # Links e referências externas
├── scripts/       # Automação (validação, lint, export, índice)
├── .github/       # CI e templates de issue/PR
└── assets/        # Diagramas, imagens, logos
```

## `docs/` — Documentação para humanos

- `architecture/` — este documento e futuros registros de arquitetura.
- `workflows/` — como o repositório é operado no dia a dia (Git, Agenta,
  Claude Cowork).
- `style-guides/` — guias de estilo para quem escreve neste repositório
  (Markdown, prompts, nomenclatura).
- `integrations/` — como cada integração externa funciona (GitHub, Agenta,
  OpenAI, Anthropic/Claude).
- `decisions/` — ADRs (Architecture Decision Records), registros curtos de
  decisões estruturais relevantes e o porquê de cada uma.

## `context/` — Conhecimento reutilizável por IAs

Diferente de `docs/` (escrito para humanos lerem), `context/` guarda
conteúdo pensado para ser colado diretamente em prompts ou system prompts:

- `personas/` — identidades de especialista reutilizáveis (ex.: arquiteto
  de software, redator técnico, pesquisador).
- `writing-style/` — convenções de escrita em formato direto/imperativo
  (Markdown, código limpo, estilo acadêmico ABNT).
- `project/` — visão geral do projeto, convenções de nomenclatura e
  glossário.
- `policies/` — regras de segurança e privacidade.

## `prompts/` — Prompts por ferramenta

Subpastas por ferramenta-alvo: `coding/`, `writing/`, `research/`,
`productivity/`, `education/`, `chatgpt/`, `claude/`, `gemini/`, `shared/`
(prompts que funcionam em qualquer ferramenta, sem adaptação).

## `skills/` — Skills do Claude

Uma pasta por skill, cada uma com seu `SKILL.md`. Use `skills/_template/`
como ponto de partida para uma skill nova. Skills atuais:

- `karpathy-guidelines/` — diretrizes de comportamento para código.
- `revisor-abnt/` — revisão de trabalhos acadêmicos (Google Drive).
- `organizador-de-anotacoes/` — organização de anotações de estudo
  (Notion — única exceção à remoção geral de integração com Notion neste
  repositório, ver `docs/integrations/` e a nota no topo do próprio
  `SKILL.md` dessa skill).
- `prompt-master/` — geração de prompts otimizados para qualquer
  ferramenta de IA.

## `templates/` — Modelos

Modelos em branco para criar prompts (`prompt-template.md`), contexto
(`context-template.md`), personas (`persona-template.md`) e skills
(`skill-template/`) novos, seguindo as convenções documentadas em
`context/project/conventions.md`.

## `examples/`, `resources/`, `scripts/`, `.github/`, `assets/`

- `examples/` — pares de entrada/saída reais (ex.: um prompt ruim e sua
  versão corrigida pelo `prompt-master`), exemplos de skill e de conversas.
- `resources/` — links e catálogo de referências bibliográficas externas.
- `scripts/` — utilitários de manutenção do próprio repositório (validação
  de front-matter, lint de Markdown, exportação de índice).
- `.github/` — workflows de CI (lint, validação, release) e templates de
  issue/PR.
- `assets/` — diagramas, imagens e logos usados na documentação.

## Por que esta estrutura

A separação `docs/` (humanos) vs. `context/` (IAs) é a mudança mais
importante desta reorganização em relação à estrutura anterior: antes, o
conteúdo reutilizável por IA (manuais de estilo) vivia misturado com
documentação de processo dentro de `docs/`, e dependia do Notion como fonte
de verdade. Agora esse conhecimento tem um lugar próprio e local, versionado
junto com o resto do repositório.
