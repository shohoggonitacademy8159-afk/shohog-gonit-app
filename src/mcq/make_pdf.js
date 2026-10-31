// অধ্যায়ের MCQ প্রশ্নব্যাংক থেকে ছাপার উপযোগী PDF (প্রশ্ন, উত্তরমালা, ব্যাখ্যা)
// ব্যবহার: FONT_DIR=<hind-siliguri woff2 ফোল্ডার> node src/mcq/make_pdf.js 1
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const root = path.resolve(__dirname, '../..');
const ch = process.argv[2] || '1';
const NAMES = { '1': 'বাস্তব সংখ্যা', '8': 'বৃত্ত' };
const data = JSON.parse(fs.readFileSync(path.join(root, 'src/mcq/mcq.json'), 'utf8')).c10[ch];
const FD = process.env.FONT_DIR;
const face = (w) => ['bengali', 'latin'].map(s => `@font-face{font-family:'HS';font-weight:${w};src:url('file://${FD}/hind-siliguri-${s}-${w}-normal.woff2') format('woff2')}`).join('');
const esc = s => String(s).replace(/[&<>]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' }[c]));
const L = ['ক', 'খ', 'গ', 'ঘ'];
const html = `<!doctype html><html lang="bn"><head><meta charset="utf-8"><style>
${face(400)}${face(600)}${face(700)}
@page{size:A4;margin:14mm 13mm 16mm}
body{font-family:'HS',sans-serif;color:#10233F;font-size:10.5pt;line-height:1.45;margin:0}
.head{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:2.5px solid #1F5FBF;padding-bottom:6px;margin-bottom:10px}
.head h1{margin:0;font-size:19pt;font-weight:700;color:#1F5FBF}
.head p{margin:2px 0 0;font-size:10.5pt}
.head .r{text-align:right;font-size:9.5pt;color:#4A5B73}
.info{display:flex;gap:16px;font-size:9.5pt;color:#4A5B73;margin-bottom:10px}
.cols{column-count:2;column-gap:9mm;column-rule:0.5px solid #D6E3F3}
.q{break-inside:avoid;margin:0 0 9px}
.q .t{font-weight:600}
.q .lv{font-size:8pt;color:#4A5B73;font-weight:400}
.opts{display:grid;grid-template-columns:1fr 1fr;gap:1px 10px;margin-top:2px}
.sec{break-before:page;margin:0 0 8px;font-size:15pt;color:#1F5FBF;border-bottom:1.5px solid #D6E3F3;padding-bottom:4px}
table.key{width:100%;border-collapse:collapse;font-size:10pt;margin-bottom:6px}
table.key td{border:0.5px solid #C5D6EC;padding:3px 0;text-align:center;width:10%}
table.key td b{color:#1F5FBF}
.ex{break-inside:avoid;margin:0 0 5px;font-size:9.5pt}
.ex b{color:#1F5FBF}
</style></head><body>
<div class="head"><div><h1>সহগ গণিত একাডেমি</h1><p>দশম শ্রেণি (এসএসসি 27) · সাধারণ গণিত · অধ্যায় ${ch}: ${NAMES[ch]}</p></div>
<div class="r">বহুনির্বাচনি প্রশ্ন (MCQ)<br>মোট ${data.length}টি · সহজ ও মধ্যম</div></div>
<div class="info"><span>প্রতিটি প্রশ্নের মান 1</span><span>সঠিক উত্তরের তালিকা ও ব্যাখ্যা শেষে দেওয়া আছে</span></div>
<div class="cols">${data.map((q, i) => `<div class="q"><div class="t">${i + 1}. ${esc(q.q)} <span class="lv">(${q.lv})</span></div>
<div class="opts">${q.o.map((o, k) => `<span>(${L[k]}) ${esc(o)}</span>`).join('')}</div></div>`).join('')}</div>
<h2 class="sec">উত্তরমালা</h2>
<table class="key">${Array.from({ length: Math.ceil(data.length / 10) }, (_, r) => `<tr>${data.slice(r * 10, r * 10 + 10).map((q, j) => `<td>${r * 10 + j + 1}. <b>${L[q.a]}</b></td>`).join('')}</tr>`).join('')}</table>
<h2 class="sec" style="break-before:auto;margin-top:14px">ব্যাখ্যা</h2>
<div class="cols">${data.map((q, i) => `<div class="ex"><b>${i + 1}. (${L[q.a]}) ${esc(q.o[q.a])}</b> — ${esc(q.e)}</div>`).join('')}</div>
</body></html>`;
(async () => {
  const b = await chromium.launch(); const p = await b.newPage();
  await p.setContent(html); await p.evaluate(() => document.fonts.ready);
  const out = path.join(root, `www/pdf/c10-ch${ch}-mcq.pdf`);
  fs.mkdirSync(path.dirname(out), { recursive: true });
  await p.pdf({ path: out, format: 'A4', printBackground: true, displayHeaderFooter: true, headerTemplate: '<span></span>',
    footerTemplate: `<div style="font-size:8px;width:100%;text-align:center;color:#4A5B73">Sohog Ganit Academy · Class 10 General Math · Chapter ${ch} MCQ · <span class="pageNumber"></span>/<span class="totalPages"></span></div>`,
    margin: { top: '14mm', bottom: '16mm', left: '13mm', right: '13mm' } });
  await b.close(); console.log('written', out);
})();
