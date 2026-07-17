# Changelog

Formato baseado em [Keep a Changelog](https://keepachangelog.com/pt-BR/1.1.0/).

## [2.0.0] - 2026-07-16

### Reorganização estrutural completa

- Nova árvore de pastas: `docs/`, `context/` (novo — conhecimento
  reutilizável por IA, separado de `docs/`), `prompts/` (subpastas por
  ferramenta expandidas: `coding`, `writing`, `research`, `productivity`,
  `education`, `chatgpt`, `claude`, `gemini`, `shared`), `skills/`,
  `templates/` (novo), `examples/` (novo), `resources/` (novo), `scripts/`
  (novo), `.github/` (novo), `assets/` (novo).
- **Removido:** toda integração, referência e menção ao Notion, exceto a
  skill `organizador-de-anotacoes/`, mantida Notion-nativa por decisão
  explícita (documentada no próprio `SKILL.md` dela).
- **Removido:** skill `organizador-de-prompts` (pasta, arquivos e
  referências em outros documentos).
- **Removido:** `docs/notion-sync-notes.md` (registro de sincronização com
  o Notion, sem substituto — a funcionalidade não existe mais).
- **Corrigido:** duplicação estrutural interna da skill
  `skills/karpathy-guidelines/` — o `SKILL.md`, antes aninhado em
  `skills/karpathy-guidelines/skills/karpathy-guidelines/SKILL.md`, foi
  movido para a raiz da pasta da skill.
- **Migrado:** `docs/manual-de-estilo-prompts.md` (placeholder vazio) →
  `context/project/conventions.md`, com conteúdo real e sem menções ao
  Notion.
- **Migrado:** `docs/manual-de-estilo-anotacoes.md` (placeholder vazio) →
  `context/writing-style/academic-style.md`, com conteúdo real (normas
  ABNT) e sem menções ao Notion.
- **Renomeado:** `skills/prompt-mestre-main/` → `skills/prompt-master/`,
  para coincidir com o `name:` já declarado no front-matter do `SKILL.md`.

## [1.0.0] - 2026-07-13

### Configuração inicial do repositório

- Git instalado, configurado e sincronizado com o GitHub
  (`isaqteo/ai-prompts-skills-docs`).
- Autenticação migrada de HTTPS + Personal Access Token para SSH.
- Estrutura inicial de pastas criada: `docs/`, `prompts/`, `skills/`.
- Skill de terceiros `karpathy-guidelines` (originalmente
  `andrej-karpathy-skills`) importada e corrigida (problema de submódulo
  Git resolvido).
- Skills `organizador-de-prompts`, `organizador-de-anotacoes` e
  `revisor-abnt` estabelecidas.
- Pesquisa sobre a integração Agenta.ai ↔ GitHub documentada.
