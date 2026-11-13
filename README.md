# Sentinela · Segurança residencial

Landing page de CFTV e monitoramento remoto de câmeras. Um único `index.html`, sem build nem dependências: CSS inline, ícones SVG e JavaScript puro. A câmera em 3D é desenhada em tempo real num canvas e acompanha a rolagem da página.

## Publicar no GitHub Pages
Settings → Pages → Source: **Deploy from a branch** → Branch: `main` / `(root)` → Save.

## Personalizar
- Nome da marca: `<title>`, logo e rodapé em `index.html`.
- WhatsApp e telefone: troque `5500000000000` pelo número real.
- Vídeos próprios (opcional): preencha `const CLIPS = { intro, turn, explode }` no script com três MP4 all-intra; o site passa a usá-los no lugar da câmera 3D.
