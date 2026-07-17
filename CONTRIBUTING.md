# Como Contribuir

Este é um repositório pessoal, mas segue um processo consistente para
manter skills, prompts e documentação fáceis de navegar e confiáveis.

## Antes de adicionar algo novo

1. Confira `docs/architecture/repository-structure.md` para saber em qual
   pasta o conteúdo novo deve entrar.
2. Confira `docs/style-guides/naming.md` e
   `context/project/conventions.md` para nomenclatura.
3. Use o template correspondente em `templates/` como ponto de partida —
   não comece um arquivo do zero se já existe um modelo para o tipo de
   conteúdo.

## Adicionando uma skill nova

1. Copie `skills/_template/` para `skills/<nome-descritivo>/`.
2. Preencha `SKILL.md` (front-matter `name` idêntico ao nome da pasta,
   `description` com gatilhos claros de quando usar).
3. Rode `python3 scripts/validate.py` antes de commitar.

## Adicionando um prompt novo

1. Copie `templates/prompt-template.md` para
   `prompts/<ferramenta>/<nome-descritivo>.md`.
2. Preencha o front-matter e as seções conforme
   `docs/style-guides/prompt-writing.md`.

## Adicionando contexto reutilizável (`context/`)

1. Escolha a subpasta certa: `personas/`, `writing-style/`, `project/` ou
   `policies/`.
2. Use `templates/context-template.md` (ou `persona-template.md`, para
   personas) como ponto de partida.
3. Lembre-se: `context/` é escrito para uma IA consumir, não para um
   humano ler como prosa — seja direto e imperativo (ver
   `context/writing-style/markdown-style.md`).

## Fluxo de Git

Siga `docs/workflows/git-workflow.md` — em resumo: `git pull` antes de
começar a editar, commits pequenos e descritivos, Pull Request para
mudanças estruturais maiores usando `.github/PULL_REQUEST_TEMPLATE.md`
como checklist.

## Antes de abrir um Pull Request

```bash
python3 scripts/validate.py
python3 scripts/lint.py
```

Ambos devem passar sem erros. Os workflows em `.github/workflows/` rodam
essas mesmas checagens automaticamente em cada PR.

## Sobre integrações externas

- Este repositório **não usa mais o Notion** para nenhum conteúdo novo,
  com a única exceção documentada da skill `skills/organizador-de-anotacoes/`
  (ver a nota no início do próprio `SKILL.md` dela). Não reintroduza
  dependência de Notion em nenhuma outra skill, prompt ou doc sem discutir
  isso explicitamente primeiro.
- Qualquer integração externa nova deve ganhar um documento em
  `docs/integrations/` explicando como ela funciona de fato (não como se
  imagina que funcione) — ver `context/personas/researcher.md` para o
  princípio por trás disso.
