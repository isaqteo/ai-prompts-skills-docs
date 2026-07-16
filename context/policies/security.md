---
titulo: Segurança
categoria: policies
tags: [seguranca, tokens, ssh]
versao: 1.0
data_criacao: 2026-07-16
ultima_revisao: 2026-07-16
---

## O que este contexto descreve

Regras de segurança para autenticação e manuseio de credenciais neste
repositório, baseadas nas decisões já tomadas na configuração original (ver
`relatorio-setup-repositorio-ia(2026-07-13).md`, seções 2.2–2.3).

## Conteúdo

- **Autenticação com o GitHub é feita via SSH, não via token embutido em
  URL HTTPS.** O repositório migrou de HTTPS + Personal Access Token (PAT)
  para SSH especificamente para eliminar a exposição do token na
  configuração do Git (`git remote -v` nunca deve mostrar um token em texto
  puro).
- **Tokens PAT gerados durante testes devem ser revisados periodicamente.**
  Ao configurar este repositório, foram gerados tokens classic com escopo
  `repo` completo para testes de push via HTTPS antes da migração para SSH.
  Revise em GitHub → Settings → Developer settings → Tokens se algum desses
  tokens de teste ainda está ativo e sem uso — revogue os que não forem mais
  necessários.
- **Nunca commitar segredos.** `.env`, chaves de API e tokens ficam fora do
  controle de versão (ver `.gitignore` na raiz do repositório).
- **Chaves SSH** — a chave usada para autenticar neste repositório foi
  gerada com `ssh-keygen -t ed25519` e cadastrada em GitHub → Settings →
  SSH Keys. Se a máquina de desenvolvimento mudar, gere uma chave nova em
  vez de copiar a chave privada entre máquinas.
- **Integrações externas (Agenta, futuros webhooks do GitHub Actions)**
  devem usar tokens dedicados e com escopo mínimo necessário, nunca o mesmo
  token usado para push manual.

## Quando incluir este contexto

- Ao configurar qualquer nova integração ou automação que precise de
  credenciais para este repositório (ex.: GitHub Actions, webhook do
  Agenta).
- Em uma revisão de segurança periódica do repositório.

## Notas de manutenção
- Registre aqui qualquer nova forma de autenticação adotada pelo
  repositório (ex.: quando a automação Agenta → GitHub Actions do future
  path 3 do relatório for implementada, documente o escopo do token
  dedicado usado).
