"""Gera os posts do Instagram da Sentinela após o rebranding (identidade do cliente).
Uso: python3 apresentacao/instagram.py && node apresentacao/ig.js
Saída: apresentacao/instagram/post-1.jpg ... post-9.jpg
"""
import pathlib

AQUI = pathlib.Path(__file__).parent
OUT = AQUI / 'instagram'
OUT.mkdir(exist_ok=True)

LOGO = ('<svg viewBox="0 0 20 20" fill="none" stroke="#fff" stroke-width="2"><circle cx="10" cy="10" r="7"/>'
        '<circle cx="10" cy="10" r="2.4" fill="#fff" stroke="none"/></svg>')


def marca(escuro):
    cor = '#fff' if escuro else '#111214'
    return f'<div class="brand" style="color:{cor}"><i>{LOGO}</i>Sentinela</div>'


def chk(t):
    return f'<li><span class="ck"></span>{t}</li>'


# (tipo, conteúdo)
POSTS = [
    ('claro', f'''<div class="lbl">Dica · Segurança em casa</div>
      <h2>3 pontos que toda casa precisa ter na câmera<em>.</em></h2>
      <ul class="lst">{chk('Portão e entrada principal')}{chk('Garagem e área do carro')}{chk('Fundos e muros laterais')}</ul>
      <p class="sm">Salva para depois e confere na sua casa.</p>{marca(False)}'''),
    ('foto', f'''<img class="bg" src="../../img/casa-noite.jpg" alt="">
      <div class="live"><span class="dot"></span>Ao vivo · CAM 01</div>
      <div class="band"><div class="lbl" style="color:#FF8A95">Monitoramento 24h</div><h2 style="color:#fff">Sua casa vista de qualquer lugar.</h2>{marca(True)}</div>'''),
    ('red', f'''<div class="lbl" style="color:#fff">Novo no site</div>
      <h2 style="color:#fff">Monte o projeto da sua casa no nosso simulador.</h2>
      <p class="sm" style="color:rgba(255,255,255,.9)">Escolha as câmeras, veja o que cada uma enxerga e mande o projeto pelo WhatsApp.</p>
      <span class="cta">Link na bio</span>{marca(True)}'''),
    ('dark', f'''<div class="lbl" style="color:#FF8A95">Tira-dúvidas</div>
      <h2 style="color:#fff">Bullet ou Dome: qual câmera escolher<em>?</em></h2>
      <div class="vs"><div><b>Bullet</b><span>Área externa, portões e garagem. Mais visível, inibe a ação.</span></div>
      <div><b>Dome</b><span>Ambiente interno. Discreta, cobre bem salas amplas.</span></div></div>{marca(True)}'''),
    ('foto', f'''<img class="bg" src="../../img/cam-poste.jpg" alt="">
      <div class="band"><div class="lbl" style="color:#FF8A95">Visão noturna</div><h2 style="color:#fff">Imagem nítida de dia e de noite.</h2>{marca(True)}</div>'''),
    ('claro', f'''<div class="lbl">Como funciona</div>
      <h2>Do primeiro contato ao app no seu celular<em>.</em></h2>
      <ol class="steps"><li><b>01</b>Visita técnica grátis</li><li><b>02</b>Projeto sob medida</li><li><b>03</b>Instalação limpa</li><li><b>04</b>Tudo no celular</li></ol>
      {marca(False)}'''),
    ('dark', f'''<div class="lbl" style="color:#FF8A95">Sentinela</div>
      <h2 class="big" style="color:#fff">Seus olhos em casa <span style="color:#FF3B4E">24 horas</span>.</h2>
      <p class="sm" style="color:rgba(255,255,255,.75)">Câmeras, alarmes e monitoramento para quem quer viajar tranquilo.</p>{marca(True)}'''),
    ('foto', f'''<img class="bg" src="../../img/tecnico.jpg" alt="">
      <div class="band"><div class="lbl" style="color:#FF8A95">Bastidores</div><h2 style="color:#fff">Instalação limpa, sem fios à mostra.</h2>{marca(True)}</div>'''),
    ('red', f'''<div class="lbl" style="color:#fff">Checklist</div>
      <h2 style="color:#fff">Antes de viajar, confira:</h2>
      <ul class="lst w">{chk('Câmeras online no app')}{chk('Alarme ativado')}{chk('Notificações ligadas')}{chk('Vizinho de confiança avisado')}</ul>
      <p class="sm" style="color:rgba(255,255,255,.9)">Manda para quem vai viajar.</p>{marca(True)}'''),
]

CSS = """
@import url('https://fonts.googleapis.com/css2?family=Manrope:wght@500;600;700;800&display=swap');
*{box-sizing:border-box;margin:0;padding:0}
body{background:#888;font-family:"Manrope",Arial,sans-serif;display:flex;flex-wrap:wrap;gap:20px;padding:20px}
.p{width:1080px;height:1350px;position:relative;overflow:hidden;padding:88px;display:flex;flex-direction:column;justify-content:center;gap:36px}
.claro{background:#F6F5F2;color:#111214}
.red{background:#E11D2E}
.dark{background:#121316}
.foto{padding:0;justify-content:flex-end}
.lbl{font-size:30px;font-weight:800;letter-spacing:.14em;text-transform:uppercase;color:#E11D2E;display:flex;align-items:center;gap:16px}
.lbl::before{content:"";width:18px;height:18px;background:currentColor;border-radius:4px}
h2{font-size:92px;line-height:1.02;font-weight:800;letter-spacing:-.035em}
h2.big{font-size:130px}
h2 em{font-style:normal;color:#E11D2E}
.dark h2 em{color:#FF3B4E}
.sm{font-size:36px;line-height:1.4;color:#4A4D55;font-weight:500}
.lst{list-style:none;display:grid;gap:26px}
.lst li{display:flex;align-items:center;gap:24px;font-size:44px;font-weight:700}
.ck{width:52px;height:52px;border-radius:50%;background:#E11D2E;flex:none;position:relative}
.ck::after{content:"";position:absolute;left:17px;top:11px;width:14px;height:24px;border:solid #fff;border-width:0 6px 6px 0;transform:rotate(45deg)}
.lst.w li{color:#fff}.lst.w .ck{background:#fff}.lst.w .ck::after{border-color:#E11D2E}
.steps{list-style:none;display:grid;grid-template-columns:1fr 1fr;gap:20px}
.steps li{background:#fff;border:2px solid #E4E2DD;border-radius:24px;padding:30px;font-size:38px;font-weight:700;line-height:1.2}
.steps b{display:block;color:#E11D2E;font-size:30px;margin-bottom:10px}
.vs{display:grid;gap:20px}
.vs div{border:2px solid rgba(255,255,255,.25);border-left:8px solid #E11D2E;border-radius:20px;padding:30px 34px;color:#fff}
.vs b{display:block;font-size:48px;margin-bottom:8px}
.vs span{font-size:32px;line-height:1.4;color:rgba(255,255,255,.78);font-weight:500}
.cta{align-self:flex-start;background:#fff;color:#E11D2E;font-size:38px;font-weight:800;padding:24px 44px;border-radius:999px}
.brand{position:absolute;left:88px;bottom:72px;display:flex;align-items:center;gap:16px;font-size:40px;font-weight:800;letter-spacing:-.02em}
.brand i{width:58px;height:58px;border-radius:16px;background:#E11D2E;display:grid;place-items:center}
.brand i svg{width:32px;height:32px}
.red .brand i{background:#fff}.red .brand i svg{stroke:#E11D2E}.red .brand i svg circle:last-child{fill:#E11D2E}
.bg{position:absolute;inset:0;width:100%;height:100%;object-fit:cover}
.band{position:relative;background:#121316;padding:64px 88px 190px;display:flex;flex-direction:column;gap:24px}
.band h2{font-size:80px}
.live{position:absolute;left:60px;top:60px;background:rgba(17,18,20,.75);color:#fff;font-size:30px;font-weight:700;padding:16px 26px;border-radius:999px;display:flex;align-items:center;gap:14px}
.dot{width:16px;height:16px;border-radius:50%;background:#FF3B4E}
"""

html = '<!doctype html><html lang="pt-BR"><head><meta charset="utf-8"><title>Posts Sentinela</title><style>' + CSS + '</style></head><body>'
for i, (tipo, corpo) in enumerate(POSTS, 1):
    html += f'<section class="p {tipo}" id="post-{i}">{corpo}</section>'
html += '</body></html>'
(OUT / 'posts.html').write_text(html, encoding='utf8')
print('ok', len(POSTS))
