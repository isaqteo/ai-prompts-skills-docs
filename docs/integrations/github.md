# Integração — GitHub

Como este repositório se conecta ao GitHub, e o histórico de como essa
configuração evoluiu.

## Repositório

- URL: <https://github.com/isaqteo/ai-prompts-skills-docs>
- Owner: `isaqteo`

## Histórico de configuração

1. **Criação do repositório** no GitHub, vazio, sob o usuário `isaqteo`.
2. **Primeira tentativa de push: HTTPS + Personal Access Token (PAT).**
   - Dificuldade inicial para colar o token no terminal, resolvida com
     `Ctrl+Shift+V` ou clique do meio do mouse.
   - Erro `403 Write access to repository not granted` — corrigido gerando
     um novo token **classic** com escopo `repo` completo.
   - Push concluído com sucesso via HTTPS + token embutido na URL do
     remote.
3. **Migração para SSH**, para eliminar a exposição do token na
   configuração do Git. Detalhes completos do procedimento em
   `docs/workflows/git-workflow.md`.

## Estado atual

Autenticação via SSH, sem token exposto na configuração do remote. Ver
`context/policies/security.md` para as regras de segurança derivadas dessa
configuração, incluindo a recomendação de revisar periodicamente se algum
dos tokens PAT gerados durante os testes com HTTPS ainda está ativo sem uso.

## Futuro: GitHub Actions

Ainda não configurado. Previsto para quando a automação Agenta → GitHub for
implementada (ver `docs/integrations/agenta.md` e
`docs/workflows/agenta-workflow.md`): um workflow acionado por
`workflow_dispatch` ou `repository_dispatch`, autenticado com um Personal
Access Token dedicado e de escopo mínimo (não o token/chave usada para push
manual). Os arquivos `.github/workflows/markdown-lint.yml`,
`.github/workflows/validate.yml` e `.github/workflows/release.yml` já
existem como scaffolding inicial de CI, independente dessa automação futura
com o Agenta.
