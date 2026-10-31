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
        tries, used = 0, {}
        while s.count(lv) < need:
            tries += 1
            assert tries < 60000, (s.ex, lv, s.count(lv))
            live = [g for g in gens if used.get(g.__name__, 0) < cap] or gens
            g = s.R.choice(live); before = s.count(lv); g()
            if s.count(lv) > before: used[g.__name__] = used.get(g.__name__, 0) + 1
    def final(s):
        out = []
        for lv, n in ((E, 30), (M, 50), (H, 20)):
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
