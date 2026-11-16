# Ambiente e ferramentas · o que funciona e o que não funciona

Aprendizados desta sessão de trabalho (sessão na nuvem do Claude Code, contêiner temporário).

## Funciona
| Recurso | Uso |
|---|---|
| Playwright + Chromium pré-instalados | Testes e screenshots (`require('playwright')`, `chromium.launch()`) |
| `images.unsplash.com` | Baixar fotos por ID (a busca `unsplash.com/napi` redireciona e não serve) |
| ffmpeg | Disponível para converter vídeos em all-intra, se o cliente gerar vídeos |
| openpyxl (Python) | Gerar .xlsx formatado com listas suspensas |
| Google Drive (conector) | Criar Docs/Planilhas (enviar .xlsx com conversão), ler metadados |
| Claude Docs (conector) | Documentos editáveis compartilháveis (doc do briefing) |
| Git push no `main` | Funciona; usar `git -c push.negotiate=true push origin main` |

## Não funciona / bloqueado
| Tentativa | O que aconteceu | Alternativa usada |
|---|---|---|
| Ativar GitHub Pages via `gh api` | Bloqueado pela permissão da sessão | Usuário ativa em Settings → Pages |
| Compartilhar arquivo do Drive como "qualquer pessoa com o link" | Bloqueado pela permissão da sessão | Usuário compartilha (ou passar o e-mail do cliente) |
| Criar Google Forms com perguntas | Não há ferramenta de Forms; Drive API só cria Forms vazio | Script Apps Script + Planilha Google |
| Formulário como Artifact com banco de dados | Visitante sem login no Claude não salva | Descartado para clientes externos |
| Conector Runway (vídeo IA) | Falha de conexão (502) | Gerar vídeos no Google Flow/Veo manualmente |
| Pexels / picsum | 403 / 522 pelo proxy | Unsplash |
| Projeto "Almeida Segurança" | Não existe no ambiente nem no GitHub do usuário | Pedir link/arquivos ao usuário |

## Observações
- `~/.claude` não persiste entre sessões na nuvem: a memória durável é este repositório (`CLAUDE.md` + `memory/`).
- O repositório é **público**: não registrar e-mail do usuário nem links privados (Drive, artifacts).
