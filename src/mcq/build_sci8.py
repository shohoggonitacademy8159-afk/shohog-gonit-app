#!/usr/bin/env python3
"""৮ম শ্রেণি বিজ্ঞান (c8s): sci8/chN.txt → chsN.json
ফরম্যাট: '## 1.1' দিয়ে পাঠ শুরু; প্রতিটি লাইন: স্তর|প্রশ্ন|সঠিক|ভুল১|ভুল২|ভুল৩  (স্তর: e/m/h)"""
import json, random, pathlib, re, collections
D = pathlib.Path(__file__).resolve().parent
LV = {'e': 'সহজ', 'm': 'মধ্যম', 'h': 'কঠিন'}
R = random.Random(8008)
tot = 0
for f in sorted((D / 'sci8').glob('ch*.txt'), key=lambda p: int(p.stem[2:])):
    ch = int(f.stem[2:]); items = []; ex = None; cnt = collections.Counter()
    for ln, line in enumerate(f.read_text(encoding='utf-8').splitlines(), 1):
        line = line.strip()
        if not line or line.startswith('#!'): continue
        if line.startswith('## '): ex = line[3:].strip(); continue
        p = [x.strip() for x in line.split('|')]
        assert len(p) == 6 and p[0] in LV and ex, (f.name, ln, line)
        opts = p[2:]; assert len(set(opts)) == 4, (f.name, ln, line)
        c = opts[0]; o = opts[:]; R.shuffle(o)
        items.append({'q': p[1], 'o': o, 'a': o.index(c), 'e': '', 'lv': LV[p[0]], 'ex': ex}); cnt[ex] += 1
    bad = {k: v for k, v in cnt.items() if v != 30}
    assert not bad, (f.name, bad)
    qs = [x['q'] + '|' + x['o'][x['a']] for x in items]; dup = [q for q, n in collections.Counter(qs).items() if n > 1]
    assert not dup, (f.name, dup)
    order = {'সহজ': 0, 'মধ্যম': 1, 'কঠিন': 2}
    items.sort(key=lambda x: ([int(t) for t in x['ex'].split('.')], order[x['lv']]))
    for i, x in enumerate(items): x['n'] = i + 1
    (D / f'chs{ch}.json').write_text(json.dumps(items, ensure_ascii=False, indent=1), encoding='utf-8')
    tot += len(items); print(f.name, len(items), dict(cnt))
print('total', tot)
