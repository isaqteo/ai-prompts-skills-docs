---
titulo: Privacidade
categoria: policies
tags: [privacidade, dados-pessoais]
versao: 1.0
data_criacao: 2026-07-16
ultima_revisao: 2026-07-16
---

## Nota sobre este arquivo

Diferente dos outros arquivos em `context/policies/`, este não tem uma base
direta no relatório de configuração original — não havia uma política de
privacidade explícita documentada até esta reorganização. O conteúdo abaixo
é um ponto de partida mínimo e deliberadamente conservador, pensado para as
necessidades já visíveis no repositório (dados de estudo pessoais na skill
`organizador-de-anotacoes`, documentos acadêmicos na skill `revisor-abnt`).
Revise e ajuste antes de tratar como política definitiva.

## O que este contexto descreve

Regras básicas sobre como skills e prompts deste repositório devem tratar
dados pessoais do usuário.

## Conteúdo

- Este é um repositório **pessoal**, não destinado a conter dados de
  terceiros. Skills que processam conteúdo pessoal do usuário
  (`organizador-de-anotacoes`, `revisor-abnt`) devem continuar operando
  apenas sobre os próprios documentos/bases do usuário, nunca compartilhar
  esse conteúdo para fora do fluxo pedido (ex.: não republicar anotações de
  estudo pessoais em nenhum lugar além do destino explicitamente pedido).
- Nenhuma skill deste repositório deve enviar dados pessoais para um
  serviço externo que não seja explicitamente parte do seu fluxo já
  documentado (Notion, Google Drive, GitHub, Agenta — conforme já
  autorizado em cada `SKILL.md`).
- Documentos acadêmicos e anotações de estudo processados pelas skills
  `revisor-abnt` e `organizador-de-anotacoes` não devem ser usados como
  exemplo em `examples/` ou citados em `docs/` sem anonimização, caso
  contenham informação identificável.

## Quando incluir este contexto

- Ao criar uma skill nova que leia ou escreva dados pessoais do usuário em
  qualquer serviço externo.

## Notas de manutenção
- Este arquivo precisa de revisão humana — foi criado como esqueleto mínimo
  na reorganização de julho/2026, não como política já validada pelo
  usuário.
