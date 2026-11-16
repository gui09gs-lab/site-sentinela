# Projeto Sentinela · site de segurança residencial

**Repositório:** github.com/gui09gs-lab/site-sentinela (público, branch `main`)
**Publicação:** GitHub Pages (o usuário ativa em Settings → Pages; `main` / root) → gui09gs-lab.github.io/site-sentinela/
**Cliente:** empresa de CFTV e segurança residencial remota (câmeras). Dados reais ainda não recebidos.
**Marca provisória:** "Sentinela" · WhatsApp/telefone `5500000000000` · e-mail `contato@exemplo.com.br`

---

## Linha do tempo e caminhos traçados

| # | Etapa | Resultado |
|---|-------|-----------|
| 1 | Pedido inicial: adaptar um briefing de landing page 3D (anel "VELA", vídeos rolando com o scroll) para câmeras de segurança, "com base no projeto Almeida Segurança" | Projeto Almeida não existia no ambiente nem no GitHub; segui só o briefing |
| 2 | **v1 – câmera 3D em canvas**: os vídeos do briefing eram de um anel, então desenhei uma câmera bullet em 3D procedural (JS puro) com intro, giro, explosão em 6 camadas | Funcionou, mas depois o usuário **não gostou** |
| 3 | Pedido: "mais real" | Expliquei que realismo de foto só com vídeo gerado por IA (Google Flow/Veo/Runway); deixei slot `CLIPS` para vídeos all-intra; conector Runway estava com falha |
| 4 | Pedido: "muito escuro, bordas vermelhas/brancas, melhorar animação" + referência **sekrondigital.com.br** | Clareei, bordas vermelhas/brancas, sombreado suave, LEDs IR, feixe de visão, flutuação, parallax. Usei a Sekron só como referência de estilo/tom; **recusei copiar imagens deles** (direitos autorais de terceiro) |
| 5 | "Não gostei, mudar estratégia, moderno mas sem 3D, monte opções" | Criei **3 opções** em `opcoes/` com fotos Unsplash locais + página de comparação |
| 6 | Escolheu **Opção 1 "Confiança"** | Virou o `index.html`; fotos movidas para `img/`; 3D removido (fica no histórico do git) |
| 7 | Pediu **simulador de câmeras** (planta da casa, áreas internas/externas, tipos Bullet/Dome/PTZ/360 com área de captura) | `simulador.html` + seção-convite e link no menu do site |
| 8 | Perguntou quanto cobrar | Orientação de preço (ver abaixo) |
| 9 | Pediu documento com tudo que o cliente precisa responder | Doc "Briefing do site · Questionário" no Claude Docs (12 seções) |
| 10 | "Pode deixar como link do Forms?" / "não consegue fazer sozinho?" | Sem ferramenta de Forms: (a) script Apps Script que cria o Forms (`ferramentas/criar-formulario-briefing.gs`); (b) **Planilha Google criada no Drive do usuário** a partir de um .xlsx gerado. Compartilhamento público foi bloqueado → usuário compartilha manualmente |
| 11 | Pediu "proteção de tela" de prévia não oficial | `preview.js` em todas as páginas + `noindex` + `robots.txt` |
| 12 | Pediu passo a passo para virar site real | Roteiro em 7 fases (ver "Caminho para produção") |

---

## Decisões técnicas e por quê

### Arquitetura geral
- **Sem build, sem framework**: cada página é um HTML autossuficiente (CSS e JS inline). Motivo: o briefing original exigia isso e facilita hospedar grátis no GitHub Pages.
- **Fotos baixadas para `img/`** (não hotlink): site não depende de servidor externo. IDs Unsplash usados: casa-noite `1600585154340-be6161a56a0c`, casa-branca `1600596542815-ffad4c1539a9`, casa-piscina `1613490493576-7fde63acd811`, casa-madeira `1600566753190-17f0baa2a6c3`, casa-classica `1570129477492-45c003edd2be`, sala `1600607687939-ce8a6c25118c`, sala-2 `1586023492125-27b2c045efd7`, cam-poste `1589935447067-5531094415d1`, cam-parede `1557597774-9d273605dfa9`, fechadura `1558002038-1055907df827`, tecnico `1621905251189-08b45d6a269e`, celular `1580910051074-3eb694886505`. URL: `https://images.unsplash.com/photo-<ID>?w=1600&q=72&fm=jpg`.
- **Formulários sem backend**: o submit monta a mensagem e abre `https://wa.me/<numero>?text=...`. Nenhum dado é guardado (bom para LGPD; limitação: sem e-mail/CRM).

### v1 3D (descartada, mas as soluções valem)
- Renderizador 3D próprio em canvas 2D: malhas por "lathe" no eixo X, projeção perspectiva, ordenação por profundidade (painter's), backface culling pela normal.
- **Faixas no sombreado**: resolvido com gradiente linear por face entre as normais das duas bordas da faixa, **com o eixo do gradiente perpendicular às bordas longas** (senão aparece serrilhado nas emendas) e **vetor de visão constante** (0,0,-1) para o especular não mudar por segmento.
- Partes internas atrás da carcaça: subdividir os cilindros ao longo do comprimento para a ordenação funcionar.
- Slot `CLIPS = {intro, turn, explode}` para vídeos **all-intra** (todo quadro é keyframe) com motor de seek encadeado no evento `seeked` — scroll fica suave nos dois sentidos.

### Opção 1 "Confiança" (site atual)
- Seções: hero com foto e notificações "ao vivo" rotativas, faixa de números com contador, 6 soluções, como funciona, simulador (convite), dúvidas (`<details>`), CTA escuro com formulário, rodapé, botão flutuante WhatsApp.
- Animações leves: `IntersectionObserver` para revelar, contadores, relógio ao vivo; tudo respeita `prefers-reduced-motion`.

### Simulador (`simulador.html`)
- Planta em **SVG em metros** (viewBox = terreno + 1 m de margem); conversão de clique via `getScreenCTM().inverse()`.
- Plantas modelo: casa térrea 22×18 m, apartamento 14×11 m, em branco 20×15 m. Modo "Editar áreas": arrastar para desenhar retângulos (snap 0,5 m), nome, interna/externa, tamanho do terreno.
- **Paredes automáticas**: geradas nas bordas das áreas **internas**; onde a borda é compartilhada com outra área por ≥ 1,2 m, abre uma **porta de 0,9 m** no meio. Limite do terreno também bloqueia.
- **Cobertura**: ray casting (≈1 raio por grau; 240 raios para 360°), ignorando interseções < 6 cm (câmera na parede). Toggle "Paredes bloqueiam".
- **Estatísticas**: grade de 0,25 m por área, ponto-em-polígono contra as áreas de visão; % por área, interna, externa e total; pontos cegos em hachura vermelha (células mescladas em faixas para poucos nós SVG).
- Tipos: Bullet 53–98°, alcance 5–30 m; Dome 80–120°, 3–15 m; PTZ zoom → abertura `lerp(110,16,z)` e alcance `lerp(14,45,z)`, opção "Girar 360°" (patrulha anima 24°/s e a estatística conta o círculo inteiro); Panorâmica 360°, 3–12 m.
- Dicas automáticas (Dome/360 em área externa, Bullet em interna, PTZ em interna, 360 fora do centro, área < 50%).
- Estado salvo em `localStorage` chave `sentinela-sim-v1` (try/catch). Exporta PNG (SVG → canvas). Envia resumo pelo WhatsApp.
- Celular: paleta de câmeras vai para logo abaixo da planta (`order:-1`); nomes de áreas estreitas giram 90°.

### Modo prévia (`preview.js`)
- Um único arquivo injetado no `<head>` de todas as páginas: tela de aviso (uma vez por sessão, `sessionStorage` `sentinela-previa-vista`), marca-d'água SVG repetida, etiqueta fixa no canto, toast.
- Bloqueio de envios: listener de `click` e `submit` em **fase de captura** no `document` + wrapper de `window.open` para wa.me/tel/mailto.
- `meta robots noindex, nofollow` em cada página + `robots.txt` `Disallow: /`.
- Para tirar: apagar `preview.js`, as linhas `<script src="preview.js">` e a meta robots, liberar `robots.txt` (está no README).

### Briefing do cliente
- 12 seções: empresa, contato, serviços, público/região, diferenciais e prova social, identidade visual, fotos, simulador (modelos, ângulos, preços), domínio, integrações, LGPD, checklist.
- Três formatos: doc no Claude Docs; **Planilha Google** "Briefing do site · Questionário" no Drive do usuário (abas "Leia primeiro" e "Questionário", 115 perguntas, 19 obrigatórias, listas suspensas) — gerada como .xlsx com openpyxl a partir do script e enviada com conversão; script Apps Script `ferramentas/criar-formulario-briefing.gs` que cria o Google Forms + planilha de respostas (124 itens, 11 páginas).
- Uploads de arquivo não podem ser criados por Apps Script → pedir links do Drive/WeTransfer.

---

## Problemas encontrados e como resolvemos
| Problema | Causa | Solução |
|---|---|---|
| Teste no celular não instalava câmeras | Clique no tipo rola suavemente até a planta; teste clicava antes | Esperar ~700 ms após armar a câmera no teste |
| Faixa vermelha e manifesto quebrados na Opção 3 | Colisão de classes `.t` (faixa × bento) e `.r` (palavra × linha de serviço) | Renomear para `.mq-t` e `.wr` |
| Rolagem lateral | Faixa girada (`rotate`) e textos `nowrap` (toast, URL do console) | Envolver em contêiner com `overflow:hidden`; `max-width` + quebra no toast; esconder URL no celular |
| Círculo da PTZ saindo do terreno | Desenho sem recorte | `clipPath` do terreno no grupo de cobertura |
| Números do 3D lentos no headless | Gradiente por face | Aceitável (headless sem GPU); real fica fluido |

---

## Preço sugerido ao usuário (estimativa de mercado BR)
Site R$ 2.500–4.500 + simulador R$ 4.000–8.000 → **projeto ≈ R$ 8.500** (faixa 6.500–12.000), 50% entrada / 50% entrega. Manutenção R$ 150–400/mês. Upsells: preço no simulador, planta de sobrado, painel de leads, Google Meu Negócio/anúncios.

## Caminho para produção (roteiro combinado)
1. Contrato e briefing → 2. aplicar respostas (eu) + política de privacidade (revisão jurídica) → 3. domínio no registro.br no CNPJ do cliente; GitHub Pages com arquivo `CNAME`, DNS: 4 registros A `185.199.108.153` / `.109.153` / `.110.153` / `.111.153` e CNAME `www` → `gui09gs-lab.github.io`, depois "Enforce HTTPS" → 4. tirar modo prévia, sitemap, remover `opcoes/` → 5. testes (celular, WhatsApp real, PageSpeed) → 6. Search Console, Google Meu Negócio, GA4/Pixel + aviso de cookies se anunciar, WhatsApp Business → 7. entrega de acessos e manutenção.

## Pendências
- Respostas do briefing (dados reais, logo, fotos, depoimentos, tabela de câmeras e preços).
- Usuário ativar GitHub Pages e compartilhar a planilha com o cliente.
- Ideias futuras do simulador: estimativa de preço, sobrado (2 andares), upload da planta do cliente, registro de leads.
