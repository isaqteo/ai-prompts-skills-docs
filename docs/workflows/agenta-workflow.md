# Workflow do Agenta.ai

Como este repositório se relaciona com o Agenta.ai, a plataforma de
gerenciamento de prompts para a qual há intenção de integração de longo
prazo.

## O modelo mental correto: Agenta → GitHub (não o contrário)

A integração entre Agenta e GitHub funciona de forma **inversa** ao que se
poderia imaginar à primeira vista:

- Os prompts são **criados e versionados dentro da plataforma Agenta**
  (no Playground), não editados como arquivo local e depois "importados"
  para o Agenta.
- Ao fazer deploy de uma versão no Agenta, a plataforma pode **notificar o
  GitHub** via webhook/GitHub Actions, atualizando arquivos neste
  repositório ou abrindo Pull Requests.
- Este repositório (a pasta `prompts/`, especificamente) funciona como
  **espelho/histórico versionado** do que foi publicado no Agenta — não
  como a fonte de onde o Agenta importa prompts.

Isso foi esclarecido via pesquisa na documentação oficial do Agenta durante
a configuração inicial deste repositório (ver `context/personas/researcher.md`
para o princípio geral por trás dessa checagem).

## Status atual

Ainda não há uma conta com prompts reais criados no Agenta, nem a automação
Agenta → GitHub Actions configurada. Os próximos passos previstos são:

1. Criar conta e os primeiros prompts reais no Agenta (Completion ou Chat
   Application), testá-los no Playground.
2. Resolver a configuração de billing do provedor de modelo usado pelo
   Agenta (ver `docs/integrations/openai.md` para o erro de cota já
   encontrado) — ou considerar outro provedor.
3. Configurar o workflow do GitHub Actions (`workflow_dispatch` ou
   `repository_dispatch`) e um Personal Access Token dedicado (com escopo
   mínimo — ver `context/policies/security.md`) para que deployments no
   Agenta atualizem automaticamente arquivos em `prompts/` neste
   repositório.

## O que isso significa para quem edita `prompts/` localmente

Enquanto a automação do passo 3 acima não existir, editar arquivos em
`prompts/` diretamente neste repositório é seguro e não conflita com o
Agenta — eles ainda não estão conectados. Depois que a automação existir,
edições locais em prompts que também existam no Agenta podem ser
sobrescritas por um deploy futuro; nesse cenário, o Agenta passa a ser a
fonte de verdade para esses prompts específicos.
