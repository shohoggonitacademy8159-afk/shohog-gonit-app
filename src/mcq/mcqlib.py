"""MCQ তৈরির সাধারণ সরঞ্জাম: প্রশ্নব্যাংক, বৈচিত্র্য-সীমা, বহুপদী লেখা।"""
import random
from fractions import Fraction as F
from itertools import product

E, M, H = 'সহজ', 'মধ্যম', 'কঠিন'
SUP = {1: '', 2: '²', 3: '³', 4: '⁴', 5: '⁵', 6: '⁶'}

def fr(x):
    x = F(x)
    return str(x.numerator) if x.denominator == 1 else f'{x.numerator}/{x.denominator}'

def money(x):
    x = F(x)
    if x.denominator == 1: return f'{x.numerator:,}'.replace(',', ',')
    return f'{float(x):,.2f}'

class Bank:
    def __init__(s, ex, rnd):
        s.ex, s.R, s.items, s.seen = ex, rnd, [], set()
    def add(s, q, c, wrong, e, lv):
        c = str(c); opts = [c]
        for w in wrong:
            w = str(w)
            if w and w not in opts: opts.append(w)
        if len(opts) < 4: return False
        opts = opts[:4]
        key = q + '|' + c
        if key in s.seen: return False
        s.seen.add(key)
        s.R.shuffle(opts)
        s.items.append({'q': q, 'o': opts, 'a': opts.index(c), 'e': e, 'lv': lv, 'ex': s.ex})
        return True
    def count(s, lv): return sum(1 for x in s.items if x['lv'] == lv)
    def fill(s, lv, need, gens, cap=7):
        tries, used, miss = 0, {}, {}
        while s.count(lv) < need:
            tries += 1
            assert tries < 60000, (s.ex, lv, s.count(lv))
            alive = [g for g in gens if miss.get(g.__name__, 0) < 300] or gens   # নতুন প্রশ্ন আর দিতে না পারা টেমপ্লেট বাদ
            live = [g for g in alive if used.get(g.__name__, 0) < cap] or alive
            g = s.R.choice(live); before = s.count(lv); g()
            if s.count(lv) > before: used[g.__name__] = used.get(g.__name__, 0) + 1; miss[g.__name__] = 0
            else: miss[g.__name__] = miss.get(g.__name__, 0) + 1
    def final(s, mult=1):
        out = []
        for lv, n in ((E, 30 * mult), (M, 50 * mult), (H, 20 * mult)):
            got = [x for x in s.items if x['lv'] == lv][:n]
            assert len(got) == n, (s.ex, lv, len(got))
            out += got
        for x in out:
            assert len(set(x['o'])) == 4 and 0 <= x['a'] < 4 and all(o.strip() for o in x['o']), x
        return out

def near(v, k=3):
    out = []
    for d in (1, -1, 2, -2, 3, 4, -3, 5, 6, -4):
        w = v + d
        if w != v and w not in out: out.append(w)
        if len(out) == k: break
    return out

# ---------- বহুপদী (একাধিক চলক) ----------
def pmul(p, q):
    r = {}
    for (e1, c1), (e2, c2) in product(p.items(), q.items()):
        e = tuple(a + b for a, b in zip(e1, e2)); r[e] = r.get(e, 0) + c1 * c2
    return {e: c for e, c in r.items() if c != 0}
def padd(*ps):
    r = {}
    for p in ps:
        for e, c in p.items(): r[e] = r.get(e, 0) + c
    return {e: c for e, c in r.items() if c != 0}
def pscale(p, k): return {e: c * k for e, c in p.items() if c * k != 0}
def ppow(p, n):
    r = {tuple(0 for _ in next(iter(p))): 1}
    for _ in range(n): r = pmul(r, p)
    return r
def lin(coefs, const=0):
    """coefs: প্রতিটি চলকের সহগ; যেমন lin([2, 3]) = 2x + 3y"""
    n = len(coefs); p = {}
    for i, c in enumerate(coefs):
        if c: p[tuple(1 if j == i else 0 for j in range(n))] = c
    if const: p[tuple(0 for _ in range(n))] = const
    return p
def pfmt(p, vars=('x', 'y')):
    if not p: return '0'
    keys = sorted(p, key=lambda e: tuple(-x for x in e))
    keys = sorted(keys, key=lambda e: -sum(e), reverse=False) if False else keys
    s = ''
    for i, e in enumerate(keys):
        c = p[e]; body = ''.join(v + SUP.get(k, f'^{k}') for v, k in zip(vars, e) if k)
        mag = abs(c); cs = fr(mag)
        if body and mag == 1: cs = ''
        term = cs + body
        if i == 0: s = ('−' if c < 0 else '') + term
        else: s += (' − ' if c < 0 else ' + ') + term
    return s

def dec(x):
    """সসীম দশমিক হলে দশমিকে (যেমন 2315.25), নইলে ভগ্নাংশে।"""
    x = F(x); d = x.denominator
    while d % 2 == 0: d //= 2
    while d % 5 == 0: d //= 5
    if d != 1: return fr(x)
    s = f'{float(x):.6f}'.rstrip('0').rstrip('.')
    assert F(s) == x, (s, x)
    return s

def run(ex, R, fixed, eg, mg, hg, caps=(7, 7, 6), mult=1):
    """একটি অনুশীলনীর 100 প্রশ্ন: fixed = [(q, c, wrong, e, lv)], eg/mg/hg = টেমপ্লেট ফাংশন (b নেয়)।"""
    b = Bank(ex, R)
    for q, c, w, e, lv in fixed: b.add(q, c, w, e, lv)
    wrap = lambda gs: [(lambda g: (lambda: g(b)))(g) for g in gs]
    for lv, need, gs, cap in ((E, 30 * mult, eg, caps[0]), (M, 50 * mult, mg, caps[1]), (H, 20 * mult, hg, caps[2])):
        ws = wrap(gs)
        for w, g in zip(ws, gs): w.__name__ = g.__name__
        b.fill(lv, need, ws, cap)
    out = b.final(mult)
    if ex is None:
        for x in out: x.pop('ex', None)   # অনুশীলনী নেই: পুরো অধ্যায়ের প্রশ্ন
    return out

def sg(n):
    return '+' if n >= 0 else '−'
def num(n):
    """ঋণাত্মক সংখ্যা যথাযথ চিহ্নে"""
    return ('−' + fr(-F(n))) if F(n) < 0 else fr(n)
def save(ch, items):
    import json, pathlib
    from collections import Counter
    import re
    fix = lambda t: re.sub(r'(?<![\w)\]°])-(?=\d)', '−', t)
    for i, x in enumerate(items):
        x['n'] = i + 1; x['q'] = fix(x['q']); x['o'] = [fix(o) for o in x['o']]; x['e'] = fix(x['e'])
        assert len(set(x['o'])) == 4, x
    root = pathlib.Path(__file__).resolve().parents[2]
    (root / f'src/mcq/ch{ch}.json').write_text(json.dumps(items, ensure_ascii=False, indent=1), encoding='utf-8')
    c = Counter((x.get('ex', '-'), x['lv']) for x in items)
    print(f'ch{ch}:', len(items), dict(sorted(c.items())))

def surd(n, k=1):
    """k√n সরল রূপে (যেমন surd(8) = '2√2', surd(9) = '3')"""
    out, inside = k, n
    for f in range(int(n ** .5) + 1, 1, -1):
        if inside % (f * f) == 0: out *= f; inside //= f * f
    if inside == 1: return str(out)
    return ('' if out == 1 else str(out)) + '√' + str(inside)
SUPD = str.maketrans('0123456789-', '⁰¹²³⁴⁵⁶⁷⁸⁹⁻')
def sup(n): return str(n).translate(SUPD)
