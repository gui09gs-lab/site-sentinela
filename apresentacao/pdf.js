// Gera os PDFs: node apresentacao/pdf.js [pasta-para-imagens-de-conferencia]
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  for (const [f, w, h] of [['celular', 1080, 1920], ['computador', 1920, 1080]]) {
    const pg = await b.newPage({ viewport: { width: w, height: h } });
    await pg.goto('file://' + path.join(__dirname, f + '.html'), { waitUntil: 'networkidle' });
    await pg.evaluate(() => document.fonts.ready);
    await pg.pdf({ path: path.join(__dirname, `Sentinela-case-${f}.pdf`), width: w + 'px', height: h + 'px', printBackground: true, preferCSSPageSize: true });
    if (process.argv[2]) {
      const n = await pg.$$('.s');
      for (let i = 0; i < n.length; i++) await n[i].screenshot({ path: `${process.argv[2]}/${f}-${i + 1}.png` });
    }
    await pg.close();
  }
  await b.close();
})();
