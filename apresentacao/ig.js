// Renderiza os posts do Instagram: node apresentacao/ig.js
const { chromium } = require('playwright');
const path = require('path');
(async () => {
  const b = await chromium.launch();
  const pg = await b.newPage({ viewport: { width: 1200, height: 1400 }, deviceScaleFactor: 0.5 });
  await pg.goto('file://' + path.join(__dirname, 'instagram', 'posts.html'), { waitUntil: 'networkidle' });
  await pg.evaluate(() => document.fonts.ready);
  const posts = await pg.$$('section.p');
  for (const p of posts) {
    const id = await p.getAttribute('id');
    await p.screenshot({ path: path.join(__dirname, 'instagram', id + '.jpg'), type: 'jpeg', quality: 88 });
  }
  await b.close();
  console.log('posts', posts.length);
})();
