// Schnelltest für alle Lernseiten: JS-Fehler und Überlauf auf Handy-Breite.
// Aufruf: node tools/check.js   (braucht Playwright mit Chromium)
// Tailwind und Google Fonts werden blockiert, damit der Test auch ohne Internet läuft.
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');

const root = path.join(__dirname, '..');
const pages = fs.readdirSync(root).filter(f => f.endsWith('.html'));

(async () => {
  const browser = await chromium.launch();
  let failed = 0;
  for (const file of pages) {
    const errors = [];
    const page = await browser.newPage({ viewport: { width: 390, height: 800 } });
    page.on('pageerror', e => errors.push(e.message));
    await page.route(/cdn\.tailwindcss\.com|fonts\.(googleapis|gstatic)\.com/, r =>
      r.request().resourceType() === 'script' ? r.fulfill({ contentType: 'text/javascript', body: '' }) : r.abort());
    await page.goto('file://' + path.join(root, file));
    await page.waitForTimeout(300);
    // Jeden Reiter einmal öffnen, falls die Seite welche hat
    const tabs = await page.$$('[onclick^="switchTab"]');
    for (const t of tabs) { try { await t.click({ timeout: 1000 }); } catch (e) { /* unsichtbar */ } }
    const width = await page.evaluate(() => document.documentElement.scrollWidth);
    if (width > 390) errors.push(`Seite ist ${width}px breit (Handy: 390px) – etwas läuft seitlich über`);
    console.log(`${errors.length ? '❌' : '✅'} ${file}${errors.map(e => '\n   - ' + e).join('')}`);
    failed += errors.length ? 1 : 0;
    await page.close();
  }
  await browser.close();
  process.exit(failed ? 1 : 0);
})();
