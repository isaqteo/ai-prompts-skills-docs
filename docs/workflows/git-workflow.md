# Workflow de Git

Como este repositório é configurado e operado no dia a dia, com base na
configuração original feita em julho de 2026 (ZorinOS 18.1).

## Instalação e configuração inicial

- Git instalado via `apt`.
- Se a instalação for interrompida no meio (pacote quebrado), corrija com:
  ```bash
  sudo dpkg --configure -a
  sudo apt --fix-broken install
  ```
- Configure a identidade antes do primeiro commit:
  ```bash
  git config --global user.name "seu-nome"
  git config --global user.email "seu-email"
  ```

## Autenticação: SSH (não HTTPS + token)

Este repositório usa **SSH** para autenticar no GitHub, não HTTPS com token
embutido na URL. Isso evita exposição de credenciais na configuração do Git.
Ver `context/policies/security.md` para o raciocínio completo.

Configuração:
```bash
ssh-keygen -t ed25519
eval "$(ssh-agent -s)"
ssh-add ~/.ssh/id_ed25519
```
Cadastre a chave pública em **GitHub → Settings → SSH Keys**, depois aponte
o remote para SSH:
```bash
git remote set-url origin git@github.com:isaqteo/ai-prompts-skills-docs.git
ssh -T git@github.com   # deve confirmar autenticação sem pedir token
```

> Se você chegou até aqui vindo de uma configuração HTTPS + Personal
> Access Token (PAT) mais antiga, revise `context/policies/security.md`
> quanto a tokens de teste que possam ainda estar ativos e sem uso.

## Fluxo de edição local (VSCode)

1. Antes de começar a editar, rode `git pull` — especialmente importante se
   o Claude Cowork também estiver editando este repositório em paralelo
   (ver `docs/workflows/claude-cowork.md`).
2. Use o painel **Source Control** (`Ctrl+Shift+G`) para stage, commit e
   sync das alterações.
3. **Não confunda** o painel Source Control com o painel **GitHub Pull
   Requests and Issues** — são extensões/painéis diferentes do VSCode: o
   primeiro é o controle de versão local (Git puro), o segundo é uma
   integração com a API do GitHub para PRs e issues.

## Convenção de commits e branches

- Commits pequenos e descritivos, um assunto por commit quando possível.
- Para mudanças estruturais grandes (como uma reorganização de pastas),
  prefira um branch dedicado e um Pull Request, usando
  `.github/PULL_REQUEST_TEMPLATE.md` como checklist.
