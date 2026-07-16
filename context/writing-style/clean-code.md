---
titulo: Código Limpo (contexto para IA)
categoria: writing-style
tags: [codigo, simplicidade, karpathy-guidelines]
versao: 1.0
data_criacao: 2026-07-16
ultima_revisao: 2026-07-16
---

## O que este contexto descreve

Um resumo, em formato de contexto reutilizável, dos princípios de "Simplicity
First" e "Surgical Changes" já documentados de forma completa na skill
`skills/karpathy-guidelines/SKILL.md`. Este arquivo existe para ser colado
diretamente em prompts de código sem precisar carregar a skill inteira —
para o conteúdo completo (com exemplos de antes/depois), use a skill.

## Conteúdo

**Simplicidade primeiro:**
- Escreva o mínimo de código que resolve o problema pedido. Nada
  especulativo.
- Não adicione abstrações para código de uso único.
- Não adicione "flexibilidade" ou "configurabilidade" que não foi pedida.
- Se 200 linhas podem virar 50, reescreva.

**Mudanças cirúrgicas:**
- Toque apenas no que precisa ser tocado.
- Não "melhore" código, comentários ou formatação adjacentes.
- Combine com o estilo existente, mesmo que você faria diferente.
- Remova apenas imports/variáveis/funções que suas próprias mudanças
  tornaram órfãos — não remova código morto pré-existente sem avisar.

**O teste:** cada linha alterada deve ser rastreável diretamente ao pedido
do usuário.

## Quando incluir este contexto

- Em qualquer prompt que peça para escrever, revisar ou refatorar código.
- Quando não for prático carregar a skill `karpathy-guidelines` inteira, mas
  o comportamento dela ainda for desejado.

## Notas de manutenção
- Fonte da verdade completa: `skills/karpathy-guidelines/SKILL.md`. Se os
  quatro princípios lá mudarem, atualize este resumo também.
