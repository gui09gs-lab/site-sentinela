# Sentinela · Segurança residencial

Site de câmeras, alarmes e monitoramento 24h. Página única (`index.html`), sem build nem dependências: só HTML, CSS e JavaScript.

## Estrutura
- `index.html`: o site (layout "Confiança")
- `simulador.html`: simulador de câmeras (planta da casa, 4 tipos de câmera, área de cobertura, pontos cegos e envio do projeto pelo WhatsApp)
- `img/`: fotos (Unsplash, licença de uso comercial livre). Troque por fotos reais do cliente quando possível.
- `ferramentas/criar-formulario-briefing.gs`: script do Google Apps Script que cria o Google Forms do briefing para o cliente (não faz parte do site)
- `opcoes/`: as três propostas de layout que foram comparadas, mantidas como referência

## Publicar no GitHub Pages
Settings → Pages → Source: **Deploy from a branch** → Branch: `main` / `(root)` → Save.

## Antes de publicar, trocar
- Nome da marca ("Sentinela"): título, logo e rodapé
- WhatsApp e telefone: `5500000000000` (aparece em `const WA` no script e nos links `wa.me` / `tel:`)
- E-mail: `contato@exemplo.com.br`
- Números da faixa de destaques (24h, 48h, 30 dias, visita grátis): confirmar com o cliente

## Modo prévia (demonstração)
Enquanto o site não é oficial, todas as páginas carregam `preview.js`, que mostra a tela de aviso "Prévia não oficial", a marca-d'água e a etiqueta no canto, e desativa WhatsApp, telefone, e-mail e formulários. A página também é bloqueada para buscadores (`meta robots noindex` e `robots.txt`).

Para publicar o site oficial:
1. Apague `preview.js`.
2. Remova de cada página as linhas `<script src="preview.js"></script>` (ou `../preview.js`) e `<meta name="robots" content="noindex, nofollow">`.
3. Troque o `robots.txt` por `User-agent: *` / `Allow: /`.
