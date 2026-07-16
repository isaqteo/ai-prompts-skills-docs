---
titulo: Visão Geral do Repositório
categoria: project
tags: [visao-geral, contexto-do-projeto]
versao: 1.0
data_criacao: 2026-07-16
ultima_revisao: 2026-07-16
---

## O que este contexto descreve

Um resumo do que é este repositório e como ele está organizado, para colar
como contexto inicial em prompts que peçam para uma IA trabalhar em
qualquer parte dele (criar uma skill nova, revisar um prompt, editar docs).

## Conteúdo

Este é um repositório pessoal para versionar **skills**, **prompts** e
**documentação/contexto** usados em fluxos de trabalho com IA (Claude,
ChatGPT, Gemini e outras ferramentas). Ele nasceu de uma pasta local
organizada manualmente e foi versionado no GitHub em julho de 2026 (ver o
relatório de configuração original para o histórico completo de decisões).

Estrutura de alto nível:

| Pasta | Para quem | O que contém |
|-------|-----------|--------------|
| `docs/` | Humanos | Documentação de processo, arquitetura, workflows, integrações |
| `context/` | IAs | Conhecimento reutilizável (personas, estilo de escrita, convenções, políticas) para colar em prompts |
| `prompts/` | Humanos + IAs | Prompts prontos, organizados por ferramenta-alvo |
| `skills/` | Claude | Skills no formato `SKILL.md`, uma pasta por skill |
| `templates/` | Humanos | Modelos para criar novos prompts, contextos, personas e skills |
| `examples/` | Humanos + IAs | Pares de entrada/saída e outros exemplos concretos |
| `resources/` | Humanos | Links e referências externas relevantes |
| `scripts/` | CI/automação | Scripts de validação, lint, export e geração de índice |
| `.github/` | GitHub | Workflows de CI e templates de issue/PR |
| `assets/` | Humanos | Diagramas, imagens e logos |

Este repositório **não tem mais integração com o Notion** (removida na
reorganização de julho/2026), com uma única exceção documentada: a skill
`skills/organizador-de-anotacoes/`, que continua Notion-nativa por decisão
explícita do usuário, já que sua função inteira depende de uma base que
ainda vive lá.

## Quando incluir este contexto

- Como primeira mensagem/system prompt de qualquer sessão que vá trabalhar
  na estrutura do repositório.
- Ao integrar este repositório a outra ferramenta (ex.: Agenta.ai, Claude
  Cowork) que precise de um resumo do que ele é.

## Notas de manutenção
- Atualize a tabela de pastas sempre que um nível novo for adicionado à
  árvore (mantenha sincronizado com `docs/architecture/repository-structure.md`).
