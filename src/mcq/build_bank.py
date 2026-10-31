#!/usr/bin/env python3
"""প্রশ্নব্যাংক জোড়া লাগানো: src/mcq/mcq.json-এর আগের অধ্যায়গুলো অপরিবর্তিত রেখে
নতুন অধ্যায়ের ফাইল (যেমন ch2.json) যোগ করে www/mcq.js লেখে।
(gen.py আবার চালালে অপশনের ক্রম বদলে যেতে পারে, আর প্রকাশিত PDF-এর সাথে মিলবে না; তাই সেটি আর চালানো হয় না।)"""
import json, pathlib
root = pathlib.Path(__file__).resolve().parents[2]
bank = json.loads((root / 'src/mcq/mcq.json').read_text(encoding='utf-8'))
for ch in ('2', '3', '4', '5', '6', '7', '9', '11', '12', '13', '14', '16'):
    f = root / f'src/mcq/ch{ch}.json'
    if f.exists(): bank['c10'][ch] = json.loads(f.read_text(encoding='utf-8'))
# অধ্যায় 8: আগের 100টি (অনুশীলনী-ট্যাগ ছাড়া, PDF-এর সাথে মেলানো) অপরিবর্তিত রেখে অনুশীলনীভিত্তিক প্রশ্ন যোগ
f8 = root / 'src/mcq/ch8x.json'
if f8.exists():
    old8 = [x for x in bank['c10']['8'] if not x.get('ex')]
    new8 = json.loads(f8.read_text(encoding='utf-8'))
    for i, x in enumerate(new8): x['n'] = len(old8) + 1 + i   # প্রশ্ন নম্বর অধ্যায়ের ভিতরে অনন্য রাখতে হবে (পরীক্ষা n দিয়ে প্রশ্ন খোঁজে)
    bank['c10']['8'] = old8 + new8
(root / 'src/mcq/mcq.json').write_text(json.dumps(bank, ensure_ascii=False, indent=1), encoding='utf-8')
(root / 'www/mcq.js').write_text('// সহগ গণিত একাডেমি — MCQ প্রশ্নব্যাংক (src/mcq/build_bank.py থেকে তৈরি)\nwindow.SOHOG_MCQ = ' + json.dumps(bank, ensure_ascii=False) + ';\n', encoding='utf-8')
print({k: len(v) for k, v in bank['c10'].items()})
