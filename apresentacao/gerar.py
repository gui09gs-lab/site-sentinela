"""Gera as duas apresentações do case Sentinela (identidade Eikóna).
Uso: python3 apresentacao/gerar.py  ->  apresentacao/celular.html e apresentacao/computador.html
Depois o PDF é gerado com Playwright (ver apresentacao/pdf.js).
"""
import pathlib

AQUI = pathlib.Path(__file__).parent
TOTAL = 8

BASE_CSS = """
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@400;500;700&display=swap');
:root{--marmore:#F3EFE9;--marmore-claro:#FBF9F6;--areia:#E8E0D5;--veio:#D8CFC4;--tinta:#2A1D16;--tinta-suave:#6A5A4D;
--terra:#6E4530;--sobre-terra:#FBF9F6;--terra-escura:#2A1D16;--sobre-escura:#F3EFE9;--sec-escura:#D9CFC4;--egeu:#1F5C8F;--egeu-claro:#7FB3DF;
--f:"Space Grotesk",system-ui,-apple-system,"Segoe UI",Arial,sans-serif}
*{box-sizing:border-box;margin:0}
html,body{background:#cfc7bc}
body{font-family:var(--f);color:var(--tinta);-webkit-font-smoothing:antialiased}
.s{width:var(--W);height:var(--H);position:relative;overflow:hidden;background:var(--marmore);page-break-after:always;break-after:page}
.s.escuro{background:var(--terra-escura);color:var(--sobre-escura)}
.s.terra{background:var(--terra);color:var(--sobre-terra)}
.s.areia{background:var(--areia)}
.mark{position:absolute;width:var(--mk);height:var(--mk);opacity:.07;pointer-events:none}
.top{position:absolute;left:var(--m);right:var(--m);top:var(--mt);display:flex;justify-content:space-between;font-weight:500;font-size:var(--rot);letter-spacing:.16em;text-transform:uppercase;color:var(--tinta-suave)}
.escuro .top{color:var(--sec-escura)} .terra .top{color:var(--sobre-terra)}
.logo{position:absolute;left:var(--m);bottom:var(--mb);height:var(--lg)}
h1,h2{font-weight:700;letter-spacing:-.045em;line-height:.98}
h1 .p,h2 .p{color:var(--egeu)} .escuro .p{color:var(--egeu-claro)}
.escuro em,.escuro .az{font-style:normal;color:var(--egeu-claro)}
p.txt{font-weight:400;color:var(--tinta-suave)} .escuro p.txt{color:var(--sec-escura)} .terra p.txt{color:var(--sobre-terra)}
a.lk{white-space:nowrap;color:var(--egeu);font-weight:500;text-decoration:none;border-bottom:2px solid currentColor}
.escuro a.lk{color:var(--egeu-claro)}
.chips{display:flex;flex-wrap:wrap;gap:var(--cg)}
.chip{border:2px solid var(--tinta);border-radius:4px;padding:var(--cp);font-weight:500;font-size:var(--cf)}
.escuro .chip{border-color:var(--sobre-escura)}
.browser{background:var(--marmore-claro);border:2px solid var(--tinta);border-radius:4px;overflow:hidden}
.browser .bar{height:var(--bb);display:flex;align-items:center;gap:10px;padding:0 18px;border-bottom:2px solid var(--tinta);background:var(--areia)}
.browser .bar i{width:14px;height:14px;border-radius:50%;border:2px solid var(--tinta)}
.browser img{display:block;width:100%}
.phone{background:var(--tinta);border-radius:var(--pr);padding:var(--pp)}
.phone img{display:block;width:100%;border-radius:calc(var(--pr) - var(--pp))}
.escuro .browser,.escuro .browser .bar{border-color:var(--sobre-escura)}
.lista{list-style:none;padding:0;display:grid;gap:var(--lgp)}
.lista li{display:flex;gap:var(--lgp);align-items:baseline;font-size:var(--lf);line-height:1.3}
.lista b{font-weight:500;font-size:var(--rot);letter-spacing:.16em;color:var(--egeu-claro);flex:none}
.cards{display:grid;gap:var(--cg)}
.card{background:var(--marmore-claro);border-radius:4px;padding:var(--cpad);border:2px solid var(--veio)}
.card .ic{width:var(--icw);height:var(--icw)}
.card h3{font-weight:700;letter-spacing:-.02em;font-size:var(--h3);margin-top:16px}
.card .ang{font-weight:700;color:var(--terra);font-size:var(--h3);letter-spacing:-.02em}
.card p{color:var(--tinta-suave);font-size:var(--cf);line-height:1.35;margin-top:8px}
.passos{display:grid;gap:var(--cg)}
.passo{border-top:3px solid var(--sobre-terra);padding-top:var(--cp2)}
.passo b{display:block;font-size:var(--rot);letter-spacing:.16em;font-weight:500}
.passo span{display:block;font-weight:700;letter-spacing:-.03em;font-size:var(--h3);margin-top:10px;line-height:1.1}
@page{margin:0}
@media screen{
  body{display:flex;flex-direction:column;align-items:center;gap:24px;padding:24px 0}
}
"""

ICONES = {
  'bullet': '<svg class="ic" viewBox="0 0 64 64" fill="none" stroke="#2A1D16" stroke-width="4"><rect x="8" y="22" width="34" height="16"/><path d="M42 25h10v10H42"/><path d="M16 38v12h12"/><circle cx="56" cy="30" r="3" fill="#1F5C8F" stroke="none"/></svg>',
  'dome': '<svg class="ic" viewBox="0 0 64 64" fill="none" stroke="#2A1D16" stroke-width="4"><path d="M10 26h44"/><path d="M14 26a18 18 0 0 0 36 0"/><circle cx="32" cy="34" r="4" fill="#1F5C8F" stroke="none"/></svg>',
  'ptz': '<svg class="ic" viewBox="0 0 64 64" fill="none" stroke="#2A1D16" stroke-width="4"><path d="M26 8h12v8H26z"/><circle cx="32" cy="34" r="16"/><path d="M8 34a24 24 0 0 1 4-13M56 34a24 24 0 0 0-4-13"/><circle cx="38" cy="34" r="4" fill="#1F5C8F" stroke="none"/></svg>',
  'pano': '<svg class="ic" viewBox="0 0 64 64" fill="none" stroke="#2A1D16" stroke-width="4"><ellipse cx="32" cy="36" rx="22" ry="9"/><path d="M10 36v-6h44v6"/><circle cx="32" cy="34" r="4" fill="#1F5C8F" stroke="none"/></svg>',
}
TIPOS = [('bullet', 'Bullet', '53° a 98°', 'Externa. Portões, garagens e corredores.'),
         ('dome', 'Dome', '80° a 110°', 'Interna. Discreta, para salas e cômodos.'),
         ('ptz', 'Speed Dome / PTZ', 'Gira 360°', 'Zoom óptico para pátios e áreas grandes.'),
         ('pano', 'Panorâmica', '360°', 'No centro do teto, sem pontos cegos.')]
ENTREGAS = ['Site responsivo', 'Simulador de câmeras', 'Pedidos pelo WhatsApp', 'Fotos otimizadas',
            'Perguntas frequentes', 'Briefing do cliente', 'Prévia para aprovação']
SIMULADOR = ['Planta da casa com áreas internas e externas', 'Quatro tipos de câmera com a área de visão',
             'A visão para nas paredes, como na vida real', 'Pontos cegos e cobertura de cada cômodo',
             'Projeto enviado pronto pelo WhatsApp']
PASSOS = [('01', 'Abre o site e entende o serviço.'), ('02', 'Monta a casa no simulador.'),
          ('03', 'Envia o projeto pelo WhatsApp.'), ('04', 'Recebe a visita técnica.')]


def topo(rotulo, n):
    return f'<div class="top"><span>{rotulo}</span><span>{n:02d} / {TOTAL:02d}</span></div>'


def logo(claro):
    return f'<img class="logo" src="marca/eikona-logotipo{"-claro" if claro else ""}.svg" alt="eikóna.">'


def marca(claro, pos):
    return f'<img class="mark" style="{pos}" src="marca/eikona-simbolo{"-claro" if claro else ""}.svg" alt="">'


def chips():
    return '<div class="chips">' + ''.join(f'<span class="chip">{c}</span>' for c in ENTREGAS) + '</div>'


def cards():
    return '<div class="cards">' + ''.join(
        f'<div class="card">{ICONES[k]}<h3>{n}</h3><div class="ang">{a}</div><p>{d}</p></div>' for k, n, a, d in TIPOS) + '</div>'


def lista():
    return '<ul class="lista">' + ''.join(f'<li><b>{i + 1:02d}</b><span>{t}</span></li>' for i, t in enumerate(SIMULADOR)) + '</ul>'


def passos():
    return '<div class="passos">' + ''.join(f'<div class="passo"><b>{n}</b><span>{t}</span></div>' for n, t in PASSOS) + '</div>'


def pagina(titulo, css, slides):
    return f"""<!doctype html><html lang="pt-BR"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="robots" content="noindex, nofollow">
<title>{titulo}</title><style>{BASE_CSS}{css}</style></head><body>
{''.join(slides)}
</body></html>"""


# ---------------- CELULAR 1080 x 1920 (área segura: 260 topo, 340 base) ----------------
CEL = """
:root{--W:1080px;--H:1920px;--m:88px;--mt:150px;--mb:150px;--lg:64px;--mk:1150px;--rot:24px;--cg:16px;--cp:14px 22px;--cf:30px;
--bb:44px;--pr:56px;--pp:14px;--lgp:22px;--lf:40px;--cpad:34px;--icw:84px;--h3:40px;--cp2:22px}
@page{size:1080px 1920px}
.c{position:absolute;left:var(--m);right:var(--m)}
h1{font-size:112px} h2{font-size:92px}
p.txt{font-size:38px;line-height:1.4}
.cards{grid-template-columns:1fr 1fr}
.passos{grid-template-columns:1fr}
"""

cel = []
cel.append(f"""<section class="s escuro">{marca(True, 'right:-420px;top:-200px')}{topo('Case · Sites', 1)}
<div class="c" style="top:560px"><h1>Um site que mostra a <em>segurança</em> antes da visita<span class="p">.</span></h1>
<p class="txt" style="margin-top:56px;max-width:820px">Site e simulador de câmeras para a Sentinela Segurança, empresa de CFTV e monitoramento residencial.</p></div>
<img class="logo" style="height:120px" src="marca/eikona-assinatura-claro.svg" alt="eikóna. marketing & comunicação"></section>""")
cel.append(f"""<section class="s">{marca(False, 'right:-500px;bottom:-380px')}{topo('O cliente', 2)}
<div class="c" style="top:420px"><h2>Câmeras e monitoramento para residências<span class="p">.</span></h2>
<p class="txt" style="margin-top:48px">A empresa instala câmeras, alarmes e acompanha as casas dos clientes 24 horas. Ela precisava de um site que passasse confiança logo de cara e trouxesse pedidos de orçamento.</p>
<p class="txt" style="margin-top:40px">O desafio: explicar algo técnico, como ângulo de câmera e ponto cego, para quem só quer a casa protegida.</p></div>{logo(False)}</section>""")
cel.append(f"""<section class="s areia">{topo('O site', 3)}
<div class="c" style="top:300px"><h2>Claro, direto e feito para o celular<span class="p">.</span></h2></div>
<div class="c" style="top:640px"><div class="browser" style="width:860px"><div class="bar"><i></i><i></i><i></i></div><img src="prints/site-desktop.jpg" alt=""></div></div>
<div style="position:absolute;right:70px;top:930px;width:330px" class="phone"><img src="prints/site-celular.jpg" alt=""></div>
<div class="c" style="top:1420px"><p class="txt" style="font-size:32px;max-width:560px">Hero com a casa protegida, avisos ao vivo e o botão de orçamento sempre à mão.</p><p class="txt" style="font-size:32px;margin-top:24px"><a class="lk" href="https://gui09gs-lab.github.io/site-sentinela/">gui09gs-lab.github.io/site-sentinela</a></p></div>{logo(False)}</section>""")
cel.append(f"""<section class="s escuro">{marca(True, 'left:-560px;bottom:-460px')}{topo('O diferencial', 4)}
<div class="c" style="top:300px"><h2>O visitante monta o projeto da <em>própria</em> casa<span class="p">.</span></h2></div>
<div class="c" style="top:600px"><div class="browser"><div class="bar"><i></i><i></i><i></i></div><img style="height:520px;object-fit:cover;object-position:top" src="prints/simulador-planta.jpg" alt=""></div></div>
<div class="c" style="top:1180px">{lista()}<p class="txt" style="font-size:30px;margin-top:28px">Teste: <a class="lk" href="https://gui09gs-lab.github.io/site-sentinela/simulador.html">site-sentinela/simulador.html</a></p></div>{logo(True)}</section>""")
cel.append(f"""<section class="s">{topo('Simulador', 5)}
<div class="c" style="top:300px"><h2>Cada câmera com a sua área de visão<span class="p">.</span></h2></div>
<div class="c" style="top:700px">{cards()}</div>{logo(False)}</section>""")
cel.append(f"""<section class="s terra">{topo('Para o cliente final', 6)}
<div class="c" style="top:300px"><h2>Do site ao orçamento em quatro passos.</h2></div>
<div class="c" style="top:820px">{passos()}</div>{logo(True)}</section>""")
cel.append(f"""<section class="s">{marca(False, 'right:-520px;top:-260px')}{topo('Entregas', 7)}
<div class="c" style="top:420px"><h2>O que entregamos<span class="p">.</span></h2>
<div style="margin-top:72px">{chips()}</div>
<p class="txt" style="margin-top:80px">Tudo em páginas leves, sem sistema para manter, prontas para publicar no domínio do cliente.</p></div>{logo(False)}</section>""")
cel.append(f"""<section class="s escuro">{marca(True, 'right:-420px;bottom:-300px')}{topo('Eikóna', 8)}
<div class="c" style="top:640px"><h1>Quer um site que traz <em>orçamento</em><span class="p">.</span></h1>
<p class="txt" style="margin-top:56px">Veja o site no ar:<br><a class="lk" href="https://gui09gs-lab.github.io/site-sentinela/">gui09gs-lab.github.io/site-sentinela</a></p><p class="txt" style="margin-top:20px">Chama no WhatsApp ou no @eikona.mkt.</p></div>
<img class="logo" style="height:120px" src="marca/eikona-assinatura-claro.svg" alt="eikóna. marketing & comunicação"></section>""")

# ---------------- COMPUTADOR 1920 x 1080 ----------------
PC = """
:root{--W:1920px;--H:1080px;--m:112px;--mt:80px;--mb:72px;--lg:52px;--mk:1150px;--rot:18px;--cg:16px;--cp:12px 20px;--cf:22px;
--bb:36px;--pr:44px;--pp:11px;--lgp:18px;--lf:28px;--cpad:30px;--icw:64px;--h3:30px;--cp2:20px}
@page{size:1920px 1080px}
.l{position:absolute;left:var(--m);width:760px}
h1{font-size:104px} h2{font-size:76px}
p.txt{font-size:28px;line-height:1.45}
.cards{grid-template-columns:repeat(4,1fr)}
.passos{grid-template-columns:repeat(4,1fr)}
"""

pc = []
pc.append(f"""<section class="s escuro">{marca(True, 'right:-260px;top:-140px')}{topo('Case · Sites', 1)}
<div class="l" style="top:300px;width:1180px"><h1>Um site que mostra a <em>segurança</em> antes da visita<span class="p">.</span></h1>
<p class="txt" style="margin-top:40px;max-width:820px">Site e simulador de câmeras para a Sentinela Segurança, empresa de CFTV e monitoramento residencial.</p></div>
<img class="logo" style="height:100px" src="marca/eikona-assinatura-claro.svg" alt="eikóna. marketing & comunicação"></section>""")
pc.append(f"""<section class="s">{marca(False, 'right:-380px;bottom:-460px')}{topo('O cliente', 2)}
<div class="l" style="top:250px;width:1100px"><h2>Câmeras e monitoramento para residências<span class="p">.</span></h2>
<div style="display:grid;grid-template-columns:1fr 1fr;gap:64px;margin-top:56px">
<p class="txt">A empresa instala câmeras, alarmes e acompanha as casas dos clientes 24 horas. Ela precisava de um site que passasse confiança logo de cara e trouxesse pedidos de orçamento.</p>
<p class="txt">O desafio: explicar algo técnico, como ângulo de câmera e ponto cego, para quem só quer a casa protegida.</p></div></div>{logo(False)}</section>""")
pc.append(f"""<section class="s areia">{topo('O site', 3)}
<div class="l" style="top:250px;width:620px"><h2>Claro, direto e feito para o celular<span class="p">.</span></h2>
<p class="txt" style="margin-top:36px">Hero com a casa protegida, avisos ao vivo e o botão de orçamento sempre à mão.</p><p class="txt" style="margin-top:28px"><a class="lk" href="https://gui09gs-lab.github.io/site-sentinela/">gui09gs-lab.github.io/site-sentinela</a></p></div>
<div style="position:absolute;left:820px;top:170px;width:900px" class="browser"><div class="bar"><i></i><i></i><i></i></div><img src="prints/site-desktop.jpg" alt=""></div>
<div style="position:absolute;right:90px;top:430px;width:250px" class="phone"><img src="prints/site-celular.jpg" alt=""></div>{logo(False)}</section>""")
pc.append(f"""<section class="s escuro">{marca(True, 'left:-640px;bottom:-560px')}{topo('O diferencial', 4)}
<div class="l" style="top:200px;width:660px"><h2>O visitante monta o projeto da <em>própria</em> casa<span class="p">.</span></h2>
<div style="margin-top:48px">{lista()}</div><p class="txt" style="margin-top:36px">Teste: <a class="lk" href="https://gui09gs-lab.github.io/site-sentinela/simulador.html">site-sentinela/simulador.html</a></p></div>
<div style="position:absolute;left:880px;top:190px;width:930px" class="browser"><div class="bar"><i></i><i></i><i></i></div><img style="height:700px;object-fit:cover;object-position:top" src="prints/simulador-planta.jpg" alt=""></div>{logo(True)}</section>""")
pc.append(f"""<section class="s">{topo('Simulador', 5)}
<div class="l" style="top:220px;width:1300px"><h2>Cada câmera com a sua área de visão<span class="p">.</span></h2></div>
<div style="position:absolute;left:var(--m);right:var(--m);top:470px">{cards()}</div>{logo(False)}</section>""")
pc.append(f"""<section class="s terra">{topo('Para o cliente final', 6)}
<div class="l" style="top:250px;width:1200px"><h2>Do site ao orçamento em quatro passos.</h2></div>
<div style="position:absolute;left:var(--m);right:var(--m);top:560px">{passos()}</div>{logo(True)}</section>""")
pc.append(f"""<section class="s">{marca(False, 'right:-420px;top:-300px')}{topo('Entregas', 7)}
<div class="l" style="top:250px;width:1300px"><h2>O que entregamos<span class="p">.</span></h2>
<div style="margin-top:56px;max-width:1150px">{chips()}</div>
<p class="txt" style="margin-top:64px;max-width:900px">Tudo em páginas leves, sem sistema para manter, prontas para publicar no domínio do cliente.</p></div>{logo(False)}</section>""")
pc.append(f"""<section class="s escuro">{marca(True, 'right:-300px;bottom:-360px')}{topo('Eikóna', 8)}
<div class="l" style="top:330px;width:1200px"><h1>Quer um site que traz <em>orçamento</em><span class="p">.</span></h1>
<p class="txt" style="margin-top:40px">Veja o site no ar: <a class="lk" href="https://gui09gs-lab.github.io/site-sentinela/">gui09gs-lab.github.io/site-sentinela</a></p><p class="txt" style="margin-top:16px">Chama no WhatsApp ou no @eikona.mkt.</p></div>
<img class="logo" style="height:100px" src="marca/eikona-assinatura-claro.svg" alt="eikóna. marketing & comunicação"></section>""")

(AQUI / 'celular.html').write_text(pagina('Sentinela · case Eikóna (celular)', CEL, cel), encoding='utf8')
(AQUI / 'computador.html').write_text(pagina('Sentinela · case Eikóna (computador)', PC, pc), encoding='utf8')
print('ok')
