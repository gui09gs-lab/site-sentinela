# Memória · site-sentinela

## Eu (usuário)
Freelancer que cria sites para clientes. Conta GitHub `gui09gs-lab`. Escreve em português (às vezes em CAIXA ALTA): **responder e escrever tudo sempre em português do Brasil**, inclusive narração de trabalho.

## Projeto ativo
| Nome | O que é |
|------|---------|
| **Sentinela** | Site de prévia para um cliente de CFTV e segurança residencial remota (câmeras). Nome, contatos e números são **fictícios** até o cliente responder o briefing. |
→ Histórico completo, decisões e caminhos: `memory/projects/site-sentinela.md`

## Estado atual (nov/2026)
- Site principal = layout **Opção 1 "Confiança"** (`index.html`), claro, vermelho #E11D2E, fonte Manrope.
- **Simulador de câmeras** em `simulador.html` (planta, 4 tipos de câmera, cobertura com paredes, pontos cegos, envio pelo WhatsApp).
- **Modo prévia ligado** (`preview.js`): tela de aviso, marca-d'água, envios bloqueados, `noindex` + `robots.txt`.
- Briefing do cliente pronto (Planilha Google no Drive do usuário + doc no Claude + script do Forms em `ferramentas/`).
- **Próximo passo:** receber as respostas do briefing → trocar conteúdo real → tirar modo prévia → domínio no GitHub Pages.

## Termos rápidos
| Termo | Significado |
|------|---------|
| **prévia** | versão de demonstração com `preview.js` ativo |
| **Opção 1/2/3** | Confiança (claro) / Central ao vivo (escuro, painel de câmeras) / Editorial (tipografia grande) — em `opcoes/` |
| **briefing** | questionário de 115 perguntas para o cliente personalizar o site |
| **Sekron** | sekrondigital.com.br — só referência de **estilo e tom**, nunca copiar imagens/textos |
| **Almeida Segurança** | projeto anterior citado pelo usuário; nunca foi encontrado (não está no GitHub dele) |
| **VELA** | briefing original de anel 3D que serviu de base para a 1ª versão (descartada) |
→ Glossário completo: `memory/glossary.md`

## Preferências do usuário
- Quer **moderno, mas sem 3D/vídeo 3D** (rejeitou a versão com câmera 3D em canvas).
- Gosta de receber **opções lado a lado + recomendação**, depois escolhe.
- Prefere que eu **faça sozinho** o máximo possível e só explique o que depende dele.
- Vermelho e branco, caixas de texto com bordas visíveis, nada escuro demais.

## Regras técnicas do projeto
- Tudo **sem build**: HTML/CSS/JS puros, um arquivo por página, fontes do Google Fonts.
- Fotos **locais** em `img/` (Unsplash, licença comercial livre). Nunca usar imagens de outra empresa.
- Antes de publicar: testar com Playwright em 1440px e 390px (erros de console, `scrollWidth` sem rolagem lateral).
- Commit + push no `main` ao terminar cada etapa (há hook que exige isso).
- Nunca colocar dados privados do usuário (e-mail, links privados do Drive) no repositório: ele é **público**.
→ Soluções técnicas e armadilhas: `memory/projects/site-sentinela.md` · limites do ambiente: `memory/context/ambiente.md`
