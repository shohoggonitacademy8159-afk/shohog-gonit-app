// প্রতিটি অনুশীলনী (অনুশীলনী না থাকলে পুরো অধ্যায়) থেকে 40টি MCQ (সহজ 12, মধ্যম 20, কঠিন 8) নিয়ে
// স্টাডি ম্যাটেরিয়াল PDF: www/pdf/study/<course>-<অংশ>.pdf, আর অ্যাপের তালিকা src/study-index.json
// ব্যবহার: FONT_DIR=<hind-siliguri woff2 ফোল্ডার> node src/mcq/make_study_pdfs.js
const { chromium } = require('playwright');
const fs = require('fs'), path = require('path');
const root = path.resolve(__dirname, '../..');
const bank = JSON.parse(fs.readFileSync(path.join(root, 'src/mcq/mcq.json'), 'utf8'));
const src = fs.readFileSync(path.join(root, 'src/app-source.html'), 'utf8');
const FD = process.env.FONT_DIR;
if (!FD) throw new Error('FONT_DIR দিন');
function course(cid) {
  const line = src.split('\n').find(l => l.trimStart().startsWith(cid + ':{'));
  const chapters = eval(line.match(/chapters:(\[[^\]]*\])/)[1]);
  const m = line.match(/exs:(\{[^}]*\})/);
  return { chapters, exs: m ? eval('(' + m[1] + ')') : {}, subj: eval(line.match(/subj:('[^']*')/)[1]) };
}
const COURSES = { c10: course('c10'), c10h: course('c10h'), h11: course('h11') };
const CLS = { c10: 'দশম শ্রেণি (এসএসসি ২৭)', c10h: 'দশম শ্রেণি (এসএসসি ২৭)', h11: 'একাদশ শ্রেণি (এইচএসসি ২৮)' };
const exName = ex => String(ex).replace(/^(\d+)\.([A-Z])$/, '$1($2)');
const ONLY = process.env.ONLY ? process.env.ONLY.split(',') : null;
const BN = s => String(s).replace(/\d/g, d => '০১২৩৪৫৬৭৮৯'[d]);
// নির্ধারিত ক্রম (প্রতিবার একই প্রশ্ন)
function rng(seed) { let x = seed >>> 0 || 1; return () => (x = (x * 1103515245 + 12345) >>> 0) / 4294967296; }
function hash(s) { let h = 2166136261; for (const c of s) h = Math.imul(h ^ c.codePointAt(0), 16777619); return h >>> 0; }
function pick(qs, key) {
  const r = rng(hash(key)), out = [];
  for (const [lv, n] of [['সহজ', 12], ['মধ্যম', 20], ['কঠিন', 8]]) {
    const pool = qs.filter(q => q.lv === lv).map(q => [r(), q]).sort((a, b) => a[0] - b[0]).map(x => x[1]);
    out.push(...pool.slice(0, n));
  }
  if (out.length < 40) {   // কোনো স্তরে কম থাকলে বাকি প্রশ্ন থেকে পূরণ
    const rest = qs.filter(q => !out.includes(q)).map(q => [r(), q]).sort((a, b) => a[0] - b[0]).map(x => x[1]);
    out.push(...rest.slice(0, 40 - out.length));
  }
  return out;
}
const face = w => ['bengali', 'latin', 'latin-ext'].filter(s => fs.existsSync(`${FD}/hind-siliguri-${s}-${w}-normal.woff2`))
  .map(s => `@font-face{font-family:'HS';font-weight:${w};src:url('file://${FD}/hind-siliguri-${s}-${w}-normal.woff2') format('woff2')}`).join('');
const esc = s => String(s).replace(/[&<>]/g, c => ({ '&': '&amp;', '<': '&lt;', '>': '&gt;' }[c]));
const L = ['ক', 'খ', 'গ', 'ঘ'];
function html(c, cid, title, sub, data) {
  return `<!doctype html><html lang="bn"><head><meta charset="utf-8"><style>
${face(400)}${face(600)}${face(700)}
body{font-family:'HS','Noto Sans','DejaVu Sans',sans-serif;color:#10233F;font-size:10.5pt;line-height:1.45;margin:0}
.head{display:flex;justify-content:space-between;align-items:flex-end;border-bottom:2.5px solid #1F5FBF;padding-bottom:6px;margin-bottom:10px}
.head h1{margin:0;font-size:18pt;font-weight:700;color:#1F5FBF}
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
<div class="head"><div><h1>সহগ গণিত একাডেমি</h1><p>${CLS[cid]} · ${esc(c.subj)} · ${esc(title)}</p><p style="font-size:9.5pt;color:#4A5B73">${esc(sub)}</p></div>
<div class="r">স্টাডি ম্যাটেরিয়াল<br>${BN(data.length)}টি MCQ · উত্তর ও ব্যাখ্যাসহ</div></div>
<div class="info"><span>প্রতিটি প্রশ্নের মান ১</span><span>সহজ ${BN(12)} · মধ্যম ${BN(20)} · কঠিন ${BN(8)}</span><span>উত্তরমালা ও ব্যাখ্যা শেষে</span></div>
<div class="cols">${data.map((q, i) => `<div class="q"><div class="t">${BN(i + 1)}. ${esc(q.q)} <span class="lv">(${q.lv})</span></div>
<div class="opts">${q.o.map((o, k) => `<span>(${L[k]}) ${esc(o)}</span>`).join('')}</div></div>`).join('')}</div>
<h2 class="sec">উত্তরমালা</h2>
<table class="key">${Array.from({ length: Math.ceil(data.length / 10) }, (_, r) => `<tr>${data.slice(r * 10, r * 10 + 10).map((q, j) => `<td>${BN(r * 10 + j + 1)}. <b>${L[q.a]}</b></td>`).join('')}</tr>`).join('')}</table>
<h2 class="sec" style="break-before:auto;margin-top:14px">ব্যাখ্যা</h2>
<div class="cols">${data.map((q, i) => `<div class="ex"><b>${BN(i + 1)}. (${L[q.a]}) ${esc(q.o[q.a])}</b> — ${esc(q.e)}</div>`).join('')}</div>
</body></html>`;
}
(async () => {
  const outDir = path.join(root, 'www/pdf/study'); fs.mkdirSync(outDir, { recursive: true });
  const b = await chromium.launch(); const p = await b.newPage();
  const index = {};
  for (const cid of Object.keys(COURSES)) {
    const c = COURSES[cid]; index[cid] = {};
    for (let ch = 1; ch <= c.chapters.length; ch++) {
      const qs = (bank[cid] || {})[String(ch)] || [];
      if (!qs.length) continue;
      const exs = c.exs[ch] || [];
      const units = exs.length ? exs.map(ex => [ex, qs.filter(q => q.ex === ex), `অনুশীলনী ${exName(ex)}`]) : [['ch' + ch, qs.filter(q => !q.ex).length ? qs.filter(q => !q.ex) : qs, `অধ্যায় ${ch}`]];
      for (const [key, pool, title] of units) {
        if (pool.length < 10) continue;
        const data = pick(pool, cid + key);
        const file = `${cid}-${key.replace('.', '-')}.pdf`;
        await p.setContent(html(c, cid, `${title}: ${c.chapters[ch - 1]}`, `অধ্যায় ${BN(ch)}: ${c.chapters[ch - 1]}`, data));
        await p.evaluate(() => document.fonts.ready);
        await p.pdf({ path: path.join(outDir, file), format: 'A4', printBackground: true, displayHeaderFooter: true, headerTemplate: '<span></span>',
          footerTemplate: `<div style="font-size:8px;width:100%;text-align:center;color:#4A5B73">Sohog Ganit Academy · ${cid === 'c10h' ? 'Higher Math' : cid === 'h11' ? 'HSC Higher Math 1st Paper' : 'General Math'} · ${key.replace('ch', 'Chapter ')} · <span class="pageNumber"></span>/<span class="totalPages"></span></div>`,
          margin: { top: '14mm', bottom: '16mm', left: '13mm', right: '13mm' } });
        const kb = Math.round(fs.statSync(path.join(outDir, file)).size / 1024);
        index[cid][key] = { f: file, n: data.length, kb, ch, q: data.map(x => x.n) };
        process.stdout.write(`${file} ${kb}KB\n`);
      }
    }
  }
  await b.close();
  fs.writeFileSync(path.join(root, 'src/study-index.json'), JSON.stringify(index));
  const app = path.join(root, 'src/app-source.html');
  fs.writeFileSync(app, fs.readFileSync(app, 'utf8').replace(/\/\*STUDY\*\/[\s\S]*?\/\*END\*\//, '/*STUDY*/' + JSON.stringify(index) + '/*END*/'));
  console.log('done', Object.values(index).reduce((n, o) => n + Object.keys(o).length, 0), 'PDF');
})();
