---
titulo: Convenções de Escrita de Prompts e Nomenclatura
categoria: project
tags: [prompts, nomenclatura, convencoes]
versao: 2.0
data_criacao: 2026-07-13
ultima_revisao: 2026-07-16
---

## Origem deste arquivo

Este arquivo substitui `docs/manual-de-estilo-prompts.md`, que era apenas um
placeholder ("conteúdo a ser migrado/sincronizado da base 'Documentação' no
Notion"). Como esse placeholder nunca chegou a ser preenchido, o conteúdo
abaixo foi escrito a partir de duas fontes reais já existentes no
repositório: as convenções de nomenclatura registradas no relatório de
configuração (renomeação de `andrej-karpathy-skills` para
`karpathy-guidelines`, seguindo o padrão descritivo já usado por
`organizador-de-anotacoes` e `revisor-abnt`) e a estrutura de intenção usada
pela skill `skills/prompt-master/`.

## O que este contexto descreve

Convenções para nomear pastas/arquivos neste repositório e para estruturar
prompts em `prompts/`, a colar como contexto ao criar prompts ou skills
novos.

## Conteúdo

**Nomenclatura de pastas e skills:**
- kebab-case sempre (`karpathy-guidelines`, não `karpathyGuidelines` nem
  `karpathy_guidelines`).
- Nome descritivo da função, não do autor/origem — por isso
  `andrej-karpathy-skills` (nome do repositório de origem) virou
  `karpathy-guidelines` (o que a skill faz) ao ser importado.
- O nome da pasta da skill deve ser idêntico ao campo `name:` do
  front-matter do seu `SKILL.md`.

**Estrutura de um prompt** (ver `templates/prompt-template.md`):
- Front-matter obrigatório: `titulo`, `ferramenta`, `tags`, `versao`,
  `data_criacao`, `ultima_revisao`.
- Seção "Objetivo do prompt" antes do prompt em si — declare a intenção em
  1-2 frases antes de qualquer texto copiável.
- O prompt em si sempre dentro de um bloco de código, isolado e pronto para
  copiar/colar.
- Seção "Notas de uso" ao final, para pré-requisitos, dicas de configuração
  ou observações de uso — nunca misturadas com o texto do prompt.

**Escrita de prompts** (alinhado com `skills/prompt-master/SKILL.md`):
- Verbo de tarefa preciso, nunca vago ("refatore X" em vez de "ajuda com
  meu código").
- Critérios de sucesso explícitos sempre que a tarefa for não trivial.
- Escopo de arquivo/função travado para IA de edição de código.
- Nenhum Chain-of-Thought forçado em modelos de raciocínio nativo (o3,
  DeepSeek-R1, Qwen3-thinking).

## Quando incluir este contexto

- Ao criar um prompt novo em `prompts/`.
- Ao nomear uma skill, pasta ou arquivo novo em qualquer parte do
  repositório.
- Como contexto complementar da skill `skills/prompt-master/` quando não for
  prático carregar a skill inteira.

## Notas de manutenção
- Se a skill `prompt-master` mudar sua lista de padrões/técnicas seguras,
  revise se este resumo ainda reflete o que ela ensina.
