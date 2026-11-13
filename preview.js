/*
 * PRÉVIA NÃO OFICIAL
 * Tela de aviso, marca-d'água e bloqueio de envios para a versão de demonstração.
 * Para publicar o site oficial: apague este arquivo, a linha <script src="...preview.js">
 * de cada página e a meta "robots" noindex; depois troque o robots.txt.
 */
(() => {
  'use strict';
  if (window.__previewOn) return; window.__previewOn = true;
  const RM = matchMedia('(prefers-reduced-motion: reduce)').matches;
  const KEY = 'sentinela-previa-vista';

  const css = `
  .pv-mark{position:fixed;inset:0;z-index:2147483000;pointer-events:none;
    background-image:url("data:image/svg+xml,${encodeURIComponent(
      `<svg xmlns='http://www.w3.org/2000/svg' width='360' height='220'><text x='180' y='110' text-anchor='middle' dominant-baseline='middle' transform='rotate(-24 180 110)' font-family='Arial,Helvetica,sans-serif' font-size='17' font-weight='700' letter-spacing='3' fill='rgb(128,128,128)' fill-opacity='.16'>PRÉVIA NÃO OFICIAL</text></svg>`)}");
    background-repeat:repeat}
  .pv-tag{position:fixed;left:max(14px,env(safe-area-inset-left,0px));bottom:calc(14px + env(safe-area-inset-bottom,0px));z-index:2147483001;
    display:flex;align-items:center;gap:8px;max-width:calc(100vw - 110px);padding:8px 14px 8px 10px;border-radius:999px;
    background:#111214;color:#fff;font:700 11.5px/1.2 Arial,Helvetica,sans-serif;letter-spacing:.06em;text-transform:uppercase;
    box-shadow:0 8px 24px rgba(0,0,0,.25);border:1.5px solid #F2B705;cursor:pointer}
  .pv-tag i{flex:none;width:18px;height:18px;border-radius:50%;background:#F2B705;color:#111214;display:grid;place-items:center;font-style:normal;font-size:12px}
  .pv-tag span{overflow:hidden;text-overflow:ellipsis;white-space:nowrap}
  .pv-tag em{font-style:normal}
  @media (max-width:520px){.pv-tag em{display:none}}
  .pv-ov{position:fixed;inset:0;z-index:2147483002;display:grid;place-items:center;padding:20px;
    background:rgba(12,13,16,.72);-webkit-backdrop-filter:blur(10px);backdrop-filter:blur(10px);opacity:0;transition:opacity .3s}
  .pv-ov.on{opacity:1}
  .pv-card{width:min(520px,100%);max-height:calc(100vh - 40px);overflow:auto;background:#fff;color:#111214;border-radius:22px;
    padding:30px 28px 26px;box-shadow:0 30px 80px rgba(0,0,0,.4);font:400 15px/1.55 Arial,Helvetica,sans-serif;
    transform:translateY(14px) scale(.98);transition:transform .35s cubic-bezier(.2,.8,.2,1);border-top:6px solid #F2B705}
  .pv-ov.on .pv-card{transform:none}
  .pv-badge{display:inline-flex;align-items:center;gap:8px;background:#FFF4CC;color:#7A5A00;border-radius:999px;padding:6px 12px;
    font-weight:700;font-size:12px;letter-spacing:.1em;text-transform:uppercase}
  .pv-card h2{margin:16px 0 10px;font:800 26px/1.15 Arial,Helvetica,sans-serif;letter-spacing:-.01em}
  .pv-card p{margin:0 0 12px;color:#43464D}
  .pv-card ul{margin:4px 0 18px;padding-left:20px;color:#43464D}
  .pv-card li{margin:4px 0}
  .pv-btn{width:100%;height:50px;border:0;border-radius:999px;background:#111214;color:#fff;font:700 15px Arial,Helvetica,sans-serif;cursor:pointer;margin-top:4px}
  .pv-btn:hover{background:#2A2C31}
  .pv-btn:focus-visible{outline:3px solid #F2B705;outline-offset:3px}
  .pv-small{display:block;margin-top:12px;text-align:center;font-size:12px;color:#83868F}
  .pv-toast{position:fixed;left:50%;bottom:calc(70px + env(safe-area-inset-bottom,0px));z-index:2147483003;transform:translate(-50%,10px);opacity:0;
    width:max-content;max-width:calc(100vw - 32px);background:#111214;color:#fff;border:1.5px solid #F2B705;border-radius:14px;padding:12px 16px;
    font:600 13.5px/1.4 Arial,Helvetica,sans-serif;text-align:center;box-shadow:0 14px 34px rgba(0,0,0,.3);transition:opacity .25s,transform .25s;pointer-events:none}
  .pv-toast.on{opacity:1;transform:translate(-50%,0)}
  @media (prefers-reduced-motion:reduce){.pv-ov,.pv-card,.pv-toast{transition:none}}
  @media print{.pv-mark{background-size:360px 220px}}`;

  const style = document.createElement('style'); style.textContent = css; document.head.appendChild(style);

  const mount = () => {
    const mark = document.createElement('div'); mark.className = 'pv-mark'; mark.setAttribute('aria-hidden', 'true');
    const tag = document.createElement('button'); tag.type = 'button'; tag.className = 'pv-tag';
    tag.innerHTML = '<i aria-hidden="true">!</i><span>Prévia não oficial<em> · demonstração</em></span>';
    tag.setAttribute('aria-label', 'Prévia não oficial. Ver aviso');
    const toast = document.createElement('div'); toast.className = 'pv-toast'; toast.setAttribute('role', 'status'); toast.setAttribute('aria-live', 'polite');
    document.body.append(mark, tag, toast);

    let tt = 0;
    const say = msg => { toast.textContent = msg; toast.classList.add('on'); clearTimeout(tt); tt = setTimeout(() => toast.classList.remove('on'), 3400); };
    const BLOCK = 'Prévia de demonstração: contatos e envios estão desativados. Os dados exibidos são fictícios.';

    // block outgoing contact actions
    document.addEventListener('click', e => {
      const a = e.target.closest && e.target.closest('a[href]');
      if (!a) return;
      const h = a.getAttribute('href') || '';
      if (/wa\.me|whatsapp|^tel:|^mailto:|^sms:/i.test(h)) { e.preventDefault(); e.stopImmediatePropagation(); say(BLOCK); }
    }, true);
    document.addEventListener('submit', e => { e.preventDefault(); e.stopImmediatePropagation(); say(BLOCK); }, true);
    const nativeOpen = window.open;
    window.open = function (url, ...rest) {
      if (/wa\.me|whatsapp|^tel:|^mailto:/i.test(String(url || ''))) { say(BLOCK); return null; }
      return nativeOpen.call(window, url, ...rest);
    };

    // splash screen
    const open = () => {
      const last = document.activeElement;
      const ov = document.createElement('div'); ov.className = 'pv-ov';
      ov.setAttribute('role', 'dialog'); ov.setAttribute('aria-modal', 'true'); ov.setAttribute('aria-labelledby', 'pv-t');
      ov.innerHTML = `<div class="pv-card">
        <span class="pv-badge">Prévia não oficial</span>
        <h2 id="pv-t">Site em demonstração</h2>
        <p>Esta é uma <b>prévia criada apenas para apresentação ao cliente</b>. Ela ainda não é o site oficial de nenhuma empresa.</p>
        <ul>
          <li>Nome, contatos, números, depoimentos e textos são <b>ilustrativos</b>.</li>
          <li>As fotos são de banco de imagens e serão trocadas pelas fotos reais.</li>
          <li>WhatsApp, telefone e formulários estão <b>desativados</b>. Não envie dados pessoais.</li>
        </ul>
        <button type="button" class="pv-btn">Entendi, ver a prévia</button>
        <span class="pv-small">Versão de demonstração · sujeita a alterações</span>
      </div>`;
      document.body.appendChild(ov);
      const btn = ov.querySelector('.pv-btn');
      const prevOverflow = document.documentElement.style.overflow;
      document.documentElement.style.overflow = 'hidden';
      requestAnimationFrame(() => { ov.classList.add('on'); btn.focus({ preventScroll: true }); });
      const close = () => {
        try { sessionStorage.setItem(KEY, '1'); } catch (e) {}
        document.documentElement.style.overflow = prevOverflow;
        ov.classList.remove('on');
        setTimeout(() => ov.remove(), RM ? 0 : 300);
        document.removeEventListener('keydown', onKey, true);
        if (last && last.focus) last.focus({ preventScroll: true });
      };
      const onKey = e => {
        if (e.key === 'Escape') { e.preventDefault(); close(); }
        else if (e.key === 'Tab') { e.preventDefault(); btn.focus(); }
      };
      btn.addEventListener('click', close);
      document.addEventListener('keydown', onKey, true);
    };
    tag.addEventListener('click', open);
    let seen = false;
    try { seen = sessionStorage.getItem(KEY) === '1'; } catch (e) {}
    if (!seen) open();
  };
  if (document.body) mount(); else document.addEventListener('DOMContentLoaded', mount);
})();
