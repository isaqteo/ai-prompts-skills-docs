---
titulo: Estilo Acadêmico (ABNT)
categoria: writing-style
tags: [abnt, academico, escrita-cientifica]
versao: 2.0
data_criacao: 2026-07-13
ultima_revisao: 2026-07-16
---

## Origem deste arquivo

Este arquivo substitui `docs/manual-de-estilo-anotacoes.md`, que era apenas
um placeholder ("conteúdo a ser migrado/sincronizado da base 'Documentação'
no Notion"). Na reorganização de julho/2026, todas as integrações com o
Notion foram removidas do repositório (com uma única exceção documentada: a
skill `skills/organizador-de-anotacoes/`, que continua Notion-nativa por
decisão explícita). Como esse placeholder nunca chegou a ser preenchido com
conteúdo migrado do Notion, o conteúdo abaixo **não vem de uma migração real**
— foi escrito a partir do conhecimento de normas ABNT já documentado em
`skills/revisor-abnt/SKILL.md`, a única fonte de verdade sobre escrita
acadêmica que já existe de fato neste repositório. Trate como um ponto de
partida, não como um manual definitivo.

## O que este contexto descreve

Convenções de escrita acadêmica (normas ABNT) para colar em prompts que
envolvam redigir, revisar ou formatar texto acadêmico — resumo do
conhecimento normativo já usado pela skill `revisor-abnt`.

## Conteúdo

**Normas ABNT centrais relevantes** (podem ter sido revisadas desde o
conhecimento-base; em caso de dúvida sobre a edição vigente, pesquise antes
de aplicar — ver `context/personas/researcher.md`):

- **NBR 14724** — estrutura geral de trabalhos acadêmicos
- **NBR 6024** — numeração progressiva de seções
- **NBR 6027** — sumário
- **NBR 6028** — resumo e palavras-chave
- **NBR 10520** — citações (diretas e indiretas)
- **NBR 6023** — referências
- **NBR 6034** — índice (quando aplicável)

**Convenções de redação:**
- Linguagem formal, impessoal (evite primeira pessoa fora da seção de
  agradecimentos/apresentação).
- Coesão e coerência acima de tudo — prefira reescrever um trecho confuso a
  apenas corrigir pontuação.
- Nunca invente autores, obras, datas, páginas ou qualquer dado
  bibliográfico ausente; sinalize a lacuna em vez de preenchê-la.

**Configuração padrão de formatação** (apenas quando a ABNT não determinar
algo específico para aquele elemento):
- Fonte Arial ou Times New Roman, tamanho 12 (tamanho 10 para citações
  longas, notas de rodapé e legendas).
- Margens: superior 3 cm, esquerda 3 cm, inferior 2 cm, direita 2 cm.
- Espaçamento 1,5 entre linhas (simples em citações longas, notas de
  rodapé, legendas e referências).
- Texto justificado, recuo de 1,25 cm na primeira linha dos parágrafos.

## Quando incluir este contexto

- Em qualquer prompt de revisão, formatação ou redação de trabalho
  acadêmico brasileiro.
- Como complemento rápido à skill `skills/revisor-abnt/SKILL.md`, quando não
  for prático carregar a skill inteira.

## Notas de manutenção
- Fonte da verdade completa e operacional: `skills/revisor-abnt/SKILL.md`.
- Se o usuário confirmar que quer migrar conteúdo real de anotações de
  estudo (fora do escopo ABNT/TCC) para cá, crie um arquivo separado — este
  aqui é especificamente sobre normas ABNT, não sobre o método pessoal de
  anotação de estudo do usuário (que continua vivendo em
  `skills/organizador-de-anotacoes/`, no Notion).
