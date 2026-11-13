# Sentinela · Segurança residencial

Landing page de CFTV e monitoramento remoto de câmeras. Um único `index.html`, sem build nem dependências: CSS inline, ícones SVG e JavaScript puro. A câmera em 3D é desenhada em tempo real num canvas e acompanha a rolagem da página.

## Publicar no GitHub Pages
Settings → Pages → Source: **Deploy from a branch** → Branch: `main` / `(root)` → Save.

## Personalizar
- Nome da marca: `<title>`, logo e rodapé em `index.html`.
- WhatsApp e telefone: troque `5500000000000` pelo número real.
- Vídeos próprios (opcional): preencha `const CLIPS = { intro, turn, explode }` no script com três MP4 all-intra; o site passa a usá-los no lugar da câmera 3D.

## Opções de layout (sem 3D)
A pasta `opcoes/` tem três direções visuais para comparar:
- `opcoes/index.html`: página de comparação
- `opcao-1-confianca.html`: claro e corporativo moderno
- `opcao-2-central.html`: escuro e tecnológico, com painel de câmeras ao vivo
- `opcao-3-editorial.html`: tipografia grande, creme e vermelho

Fotos em `opcoes/img/` são do Unsplash (licença Unsplash: uso comercial livre, sem necessidade de atribuição). Troque por fotos reais do cliente quando possível.
