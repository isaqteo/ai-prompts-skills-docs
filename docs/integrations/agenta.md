# Integração — Agenta.ai

Agenta é a plataforma de gerenciamento de prompts para a qual há intenção de
integração de longo prazo com este repositório.

## Como a integração funciona (esclarecido via pesquisa na documentação oficial)

O fluxo é **inverso** ao que se poderia supor à primeira vista:

- Prompts são criados e versionados **dentro** do Agenta (no Playground de
  uma Completion ou Chat Application), não editados neste repositório e
  depois "importados" para lá.
- Ao publicar (deploy) uma versão no Agenta, a plataforma pode **notificar
  o GitHub** via webhook/GitHub Actions — atualizando arquivos deste
  repositório diretamente ou abrindo Pull Requests.
- Este repositório funciona como **espelho/histórico versionado** do que já
  foi publicado no Agenta, não como fonte de importação.

Ver `docs/workflows/agenta-workflow.md` para o que isso significa na
prática para quem edita `prompts/` localmente.

## Problema já encontrado: `RateLimitError`

Ao testar um app de exemplo no Agenta, foi encontrado um erro de cota
(`RateLimitError`). Causa raiz identificada: falta de crédito/billing
configurado na conta OpenAI vinculada ao Agenta — não um problema do Agenta
em si. Ver `docs/integrations/openai.md`.

## Status e próximos passos

Nenhuma conta com prompts reais ainda existe no Agenta. Próximos passos:

1. Criar conta e os primeiros prompts reais (Completion ou Chat
   Application), testar no Playground.
2. Resolver a configuração de billing do provedor de modelo (OpenAI) — ou
   avaliar trocar de provedor para evitar depender de billing pago se isso
   não for desejado.
3. Configurar a automação Agenta → GitHub Actions (`workflow_dispatch` ou
   `repository_dispatch`) com um Personal Access Token dedicado.
