# ai-prompts-skills-docs

Repositório pessoal para versionar **skills**, **prompts**, **contexto
reutilizável por IA** e **documentação de processo** usados em fluxos de
trabalho com IA (Claude, ChatGPT, Gemini e outras ferramentas).

> **Reorganização de 2026-07-16:** este README reflete uma reestruturação
> completa do repositório. Veja `CHANGELOG.md` para o histórico detalhado
> de mudanças e `relatorio-setup-repositorio-ia(2026-07-13).md` (arquivado
> junto ao histórico deste projeto) para o contexto original de criação.

## Estrutura

```
ai-prompts-skills-docs/
├── docs/          # Documentação para humanos (arquitetura, workflows, style-guides, integrações, decisões)
├── context/       # Conhecimento reutilizável por IAs (personas, estilo de escrita, convenções, políticas)
├── prompts/       # Prompts prontos, organizados por ferramenta-alvo
├── skills/        # Skills no formato SKILL.md
├── templates/     # Modelos para criar prompts, contexto, personas e skills novos
├── examples/      # Exemplos concretos de entrada/saída
├── resources/     # Links e referências externas
├── scripts/       # Validação, lint, export e geração de índice
├── .github/       # Workflows de CI e templates de issue/PR
└── assets/        # Diagramas, imagens, logos
```

Detalhes de cada pasta em `docs/architecture/repository-structure.md`.

## Skills

| Skill | O que faz |
|-------|-----------|
| [`karpathy-guidelines`](skills/karpathy-guidelines/) | Diretrizes de comportamento para reduzir erros comuns de LLMs ao programar (pensar antes de codar, simplicidade, mudanças cirúrgicas, execução orientada a objetivo). Também distribuída como plugin de Claude Code e regra de projeto do Cursor. |
| [`revisor-abnt`](skills/revisor-abnt/) | Revisa e formata trabalhos acadêmicos (TCC, artigo, monografia) nas normas ABNT, a partir de um documento no Google Drive. |
| [`organizador-de-anotacoes`](skills/organizador-de-anotacoes/) | Organiza e padroniza anotações de estudo para o concurso CFO CBMERJ, no Notion. |
| [`prompt-master`](skills/prompt-master/) | Gera prompts otimizados para qualquer ferramenta de IA (Claude, ChatGPT, Cursor, Midjourney, agentes de código e mais). |

Use `skills/_template/` como ponto de partida para uma skill nova.

## Sobre o Notion

Este repositório **removeu toda integração, referência e configuração
ligada ao Notion** nesta reorganização — o conteúdo que antes dependia do
Notion como fonte de verdade (manuais de estilo, registro de sincronização)
agora vive localmente em `context/` e foi reescrito sem essa dependência.

**Única exceção, mantida por decisão explícita:** a skill
`skills/organizador-de-anotacoes/` continua Notion-nativa, porque sua
função inteira depende de uma base de anotações de estudo que ainda vive
lá, sem substituto local equivalente. Essa exceção está documentada no
início do próprio `SKILL.md` dessa skill.

A skill `organizador-de-prompts` (que também dependia do Notion, para uma
biblioteca de prompts diferente) foi **removida completamente** desta
reorganização — pasta, arquivos e todas as referências em outros documentos.

## Relação com integrações externas

- **GitHub** — autenticação via SSH (ver `docs/integrations/github.md`).
- **Agenta.ai** — plataforma de gerenciamento de prompts, com integração
  planejada (Agenta → GitHub, não o contrário — ver
  `docs/integrations/agenta.md`).
- **Google Drive** — usado pela skill `revisor-abnt`.
- **Claude Cowork** — planejado como executor futuro de atualizações de
  conteúdo (ver `docs/workflows/claude-cowork.md`).

## Começando

- Para escrever ou revisar algo neste repositório, veja `CONTRIBUTING.md`.
- Para entender as convenções de nomenclatura e estrutura, veja
  `docs/style-guides/naming.md` e `context/project/conventions.md`.
- Para o histórico completo de decisões e mudanças, veja `CHANGELOG.md`.

## Licença

MIT — veja `LICENSE`. Skills importadas de terceiros
(`karpathy-guidelines`, `prompt-master`) mantêm sua própria licença MIT
original dentro de suas respectivas pastas.
