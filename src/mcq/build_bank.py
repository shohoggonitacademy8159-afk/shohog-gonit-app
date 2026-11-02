#!/usr/bin/env python3
"""প্রশ্নব্যাংক জোড়া লাগানো: src/mcq/mcq.json-এর আগের অধ্যায়গুলো অপরিবর্তিত রেখে
নতুন অধ্যায়ের ফাইল (যেমন ch2.json) যোগ করে www/mcq.js লেখে।
(gen.py আবার চালালে অপশনের ক্রম বদলে যেতে পারে, আর প্রকাশিত PDF-এর সাথে মিলবে না; তাই সেটি আর চালানো হয় না।)"""
import json, pathlib
root = pathlib.Path(__file__).resolve().parents[2]
bank = json.loads((root / 'src/mcq/mcq.json').read_text(encoding='utf-8'))
for ch in ('2', '3', '4', '5', '6', '7', '9', '10', '11', '12', '13', '14', '15', '16', '17'):
    f = root / f'src/mcq/ch{ch}.json'
    if f.exists(): bank['c10'][ch] = json.loads(f.read_text(encoding='utf-8'))
# অধ্যায় 8: আগের 100টি (অনুশীলনী-ট্যাগ ছাড়া, PDF-এর সাথে মেলানো) অপরিবর্তিত রেখে অনুশীলনীভিত্তিক প্রশ্ন যোগ
f8 = root / 'src/mcq/ch8x.json'
if f8.exists():
    old8 = [x for x in bank['c10']['8'] if not x.get('ex')]
    new8 = json.loads(f8.read_text(encoding='utf-8'))
    for i, x in enumerate(new8): x['n'] = len(old8) + 1 + i   # প্রশ্ন নম্বর অধ্যায়ের ভিতরে অনন্য রাখতে হবে (পরীক্ষা n দিয়ে প্রশ্ন খোঁজে)
    bank['c10']['8'] = old8 + new8
# উচ্চতর গণিত (দশম, c10h): chh1.json … chh14.json
bank['c10h'] = {}
for ch in range(1, 15):
    f = root / f'src/mcq/chh{ch}.json'
    if f.exists(): bank['c10h'][str(ch)] = json.loads(f.read_text(encoding='utf-8'))
bank['h11'] = {}
for ch in range(1, 11):
    f = root / f'src/mcq/chi{ch}.json'
    if f.exists(): bank['h11'][str(ch)] = json.loads(f.read_text(encoding='utf-8'))
bank['h12'] = {}
for ch in range(1, 11):
    f = root / f'src/mcq/chj{ch}.json'
    if f.exists(): bank['h12'][str(ch)] = json.loads(f.read_text(encoding='utf-8'))
bank['c8'] = {}
for ch in range(1, 12):
    f = root / f'src/mcq/chk{ch}.json'
    if f.exists(): bank['c8'][str(ch)] = json.loads(f.read_text(encoding='utf-8'))
bank['c6'] = {}   # ৬ষ্ঠ শ্রেণি গণিত (gen_m.py)
for ch in range(1, 9):
    f = root / f'src/mcq/chm{ch}.json'
    if f.exists(): bank['c6'][str(ch)] = json.loads(f.read_text(encoding='utf-8'))
bank['c8s'] = {}   # ৮ম শ্রেণি বিজ্ঞান: প্রতি পাঠে 30টি (sci8/*.txt → build_sci8.py)
for ch in range(1, 15):
    f = root / f'src/mcq/chs{ch}.json'
    if f.exists(): bank['c8s'][str(ch)] = json.loads(f.read_text(encoding='utf-8'))
bank['c6s'] = {}   # ৬ষ্ঠ শ্রেণি বিজ্ঞান: প্রতি পাঠে 40টি (sci6/*.txt → build_sci8.py sci6)
for ch in range(1, 15):
    f = root / f'src/mcq/cht{ch}.json'
    if f.exists(): bank['c6s'][str(ch)] = json.loads(f.read_text(encoding='utf-8'))
(root / 'src/mcq/mcq.json').write_text(json.dumps(bank, ensure_ascii=False, indent=1), encoding='utf-8')   # মূল ব্যাংক (PDF এটি থেকে)
# বর্ধিত প্রশ্ন (ext/*.json): প্রতি অংশে আরও 100টি (সহজ 40, মধ্যম 50, কঠিন 10); আগের প্রশ্ন ও নম্বর অপরিবর্তিত
import re as _re
def _cc(lbl):
    m = _re.match(r'S\d*_(\w+?)_(\d+)$', lbl)
    if m: return m.group(1), m.group(2)
    if lbl == '8x': return 'c10', '8'
    if lbl[0] in 'hij': return {'h': 'c10h', 'i': 'h11', 'j': 'h12'}[lbl[0]], lbl[1:]
    return 'c10', lbl
_add = {}
for f in sorted((root / 'src/mcq/ext').glob('*.json')):
    if f.stem.startswith('need'): continue
    c, ch = _cc(f.stem)
    _add.setdefault((c, ch), []).extend(json.loads(f.read_text(encoding='utf-8')))
for (c, ch), items in sorted(_add.items()):
    cur = bank[c][ch]; n0 = max(x['n'] for x in cur)
    order = {lv: i for i, lv in enumerate(('সহজ', 'মধ্যম', 'কঠিন'))}
    items = sorted(items, key=lambda x: (str(x.get('ex') or ''), order[x['lv']]))
    for i, x in enumerate(items):
        x = dict(x); x['n'] = n0 + 1 + i
        if not x.get('ex'): x.pop('ex', None)
        cur.append(x)
(root / 'www/mcq.js').write_text('// সহগ গণিত একাডেমি — MCQ প্রশ্নব্যাংক (src/mcq/build_bank.py থেকে তৈরি)\nwindow.SOHOG_MCQ = ' + json.dumps(bank, ensure_ascii=False) + ';\n', encoding='utf-8')
print({k: len(v) for k, v in bank['c10'].items()}); print('c10h', {k: len(v) for k, v in bank['c10h'].items()}); print('h11', {k: len(v) for k, v in bank['h11'].items()}); print('h12', {k: len(v) for k, v in bank['h12'].items()})
