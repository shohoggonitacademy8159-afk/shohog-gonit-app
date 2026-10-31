// Renders the app icon, adaptive-icon foreground and splash screens to PNG with headless Chromium.
const { chromium } = require('playwright');
const fs = require('fs');
const path = require('path');
const root = path.resolve(__dirname, '..');
const res = path.join(root, 'android/app/src/main/res');

const LOGO = `<path d="M5 42c9-4 18-4 27 2 9-6 18-6 27-2v12c-9-4-18-4-27 2-9-6-18-6-27-2z" fill="#FFFFFF"/><path d="M32 44v12" stroke="#1F6FE5" stroke-width="2"/><path d="M9 46c7-2 14-2 20 2M35 48c6-4 13-4 20-2" stroke="#9CC0F5" stroke-width="1.5" fill="none"/><path d="M6 22l26-11 26 11-26 11z" fill="#0F2E6B"/><path d="M17 27v9c9 5 21 5 30 0v-9l-15 6z" fill="#173E8C"/><path d="M55 23v13" stroke="#FACC15" stroke-width="2.5"/><circle cx="55" cy="38" r="3" fill="#FACC15"/><text x="32" y="25" font-size="9" font-weight="700" fill="#FACC15" text-anchor="middle" font-family="serif">π</text>`;
const FONT = process.env.BN_FONT ? `<style>@font-face{font-family:'BN';src:url('file://${process.env.BN_FONT}') format('woff2');font-weight:700}</style>` : '';
const BLUE = '#1F6FE5', BLUE2 = '#3F8BF0';

// full icon: rounded blue square, logo centered (scale = share of canvas taken by logo)
const icon = (size, round, logoShare) => `<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}" viewBox="0 0 100 100">
  <defs><linearGradient id="g" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="${BLUE2}"/><stop offset="1" stop-color="${BLUE}"/></linearGradient></defs>
  ${round ? '<circle cx="50" cy="50" r="50" fill="url(#g)"/>' : '<rect width="100" height="100" rx="22" fill="url(#g)"/>'}
  <g transform="translate(${50 - logoShare / 2} ${50 - logoShare / 2 - 2}) scale(${logoShare / 64})">${LOGO}</g></svg>`;
// adaptive foreground: transparent, logo inside the 66/108 safe zone
const fg = size => `<svg xmlns="http://www.w3.org/2000/svg" width="${size}" height="${size}" viewBox="0 0 108 108">
  <g transform="translate(${54 - 30} ${54 - 32}) scale(${60 / 64})">${LOGO}</g></svg>`;
const splash = (w, h) => {
  const s = Math.min(w, h) * 0.32;
  return `<div style="width:${w}px;height:${h}px;background:linear-gradient(180deg,${BLUE2},${BLUE});display:flex;flex-direction:column;align-items:center;justify-content:center;gap:${s * 0.12}px;font-family:'BN','Noto Sans Bengali',sans-serif;color:#fff">
    <svg width="${s}" height="${s}" viewBox="0 0 64 64">${LOGO}</svg>
    <div style="font-size:${s * 0.2}px;font-weight:700">সহগ গণিত একাডেমি</div></div>`;
};

(async () => {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  const shot = async (html, w, h, file, transparent) => {
    await page.setViewportSize({ width: w, height: h });
    await page.setContent(`<html><head>${FONT}</head><body style="margin:0;background:transparent">${html}</body></html>`);
    await page.evaluate(() => document.fonts.ready);
    await page.screenshot({ path: file, omitBackground: !!transparent, clip: { x: 0, y: 0, width: w, height: h } });
  };
  const dens = { mdpi: 1, hdpi: 1.5, xhdpi: 2, xxhdpi: 3, xxxhdpi: 4 };
  for (const [d, k] of Object.entries(dens)) {
    const dir = path.join(res, 'mipmap-' + d);
    const L = Math.round(48 * k), F = Math.round(108 * k);
    await shot(icon(L, false, 64), L, L, path.join(dir, 'ic_launcher.png'), true);
    await shot(icon(L, true, 60), L, L, path.join(dir, 'ic_launcher_round.png'), true);
    await shot(fg(F), F, F, path.join(dir, 'ic_launcher_foreground.png'), true);
  }
  // splash screens
  const base = { mdpi: [320, 480], hdpi: [480, 800], xhdpi: [720, 1280], xxhdpi: [960, 1600], xxxhdpi: [1280, 1920] };
  await shot(splash(480, 800), 480, 800, path.join(res, 'drawable/splash.png'));
  for (const [d, [w, h]] of Object.entries(base)) {
    const pd = path.join(res, 'drawable-port-' + d), ld = path.join(res, 'drawable-land-' + d);
    if (fs.existsSync(pd)) await shot(splash(w, h), w, h, path.join(pd, 'splash.png'));
    if (fs.existsSync(ld)) await shot(splash(h, w), h, w, path.join(ld, 'splash.png'));
  }
  // web icons
  await shot(icon(192, false, 64), 192, 192, path.join(root, 'www/icon-192.png'), true);
  await shot(icon(512, false, 64), 512, 512, path.join(root, 'www/icon-512.png'), true);
  await browser.close();
  console.log('icons done');
})();
