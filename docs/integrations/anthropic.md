# Integração — Anthropic / Claude

Como este repositório se relaciona com Claude e produtos da Anthropic.

## Skills

A pasta `skills/` contém skills no formato `SKILL.md` consumidas
diretamente por Claude (claude.ai, Claude API, Claude Code). Ver
`docs/architecture/repository-structure.md` para a lista de skills atuais e
`skills/_template/` para o modelo de uma skill nova.

Duas das skills deste repositório também têm distribuição adicional fora do
formato "skill de usuário" simples:

- `skills/karpathy-guidelines/` é distribuída também como **plugin de
  Claude Code** (via `.claude-plugin/marketplace.json` e `plugin.json`) e
  como **regra de projeto do Cursor** (via `.cursor/rules/`) — ver
  `skills/karpathy-guidelines/CURSOR.md` para como cada formato se
  relaciona com os outros.

## Prompts

`prompts/claude/` guarda prompts escritos especificamente para o
comportamento de Claude (uso de tags XML, instruções explícitas sobre não
superengenheirar por padrão etc.) — ver a seção "Claude" em
`skills/prompt-master/SKILL.md` para as heurísticas usadas ao gerar esses
prompts.

## Claude Cowork (planejado)

Há intenção de longo prazo de usar o **Claude Cowork** como executor de
atualizações de conteúdo neste repositório, após a assinatura do plano
correspondente. Ver `docs/workflows/claude-cowork.md` para as boas práticas
já definidas para quando isso for adotado (principalmente: `git pull` antes
de qualquer sessão, para evitar conflito entre edição manual e edição via
Cowork).

## Sem uso de API da Anthropic neste repositório (ainda)

Não há, até o momento, nenhum script ou automação neste repositório que
chame a API da Anthropic diretamente — o consumo de Claude acontece via
claude.ai/Claude Code lendo os arquivos deste repositório, não via chamadas
de API feitas a partir dele.
