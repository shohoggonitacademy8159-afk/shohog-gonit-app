#!/usr/bin/env python3
"""৭ম শ্রেণি গণিত (c7)। প্রতিটি অনুশীলনীতে 150টি, অনুশীলনী-বিহীন অধ্যায়ে (3, 8, 11) 250টি MCQ।
হার: সহজ 50%, মধ্যম 40%, কঠিন 10%। আউটপুট: chv1.json … chv11.json
1.1 বর্গ, পূর্ণবর্গ, মূলদ ও অমূলদ · 1.2 বর্গমূল · 2.1 অনুপাত ও সমানুপাত · 2.2 ঐকিক নিয়ম, সমানুপাতিক ভাগ, কাজ ও সময় · 2.3 লাভ-ক্ষতি
3 পরিমাপ · 4.1 গুণ · 4.2 ভাগ · 4.3 বন্ধনী ও সরলীকরণ · 5.1 বর্গের সূত্রাবলি · 5.2 উৎপাদকে বিশ্লেষণ · 5.3 গ.সা.গু. · 5.4 ল.সা.গু.
6.1 লঘিষ্ঠকরণ ও সাধারণ হর · 6.2 যোগ, বিয়োগ, গুণ, ভাগ · 7.1 সমীকরণ সমাধান · 7.2 ভগ্নাংশযুক্ত সমীকরণ · 7.3 সমীকরণ গঠন (কথায় প্রশ্ন)
8 সমান্তরাল সরলরেখা · 9.1 ত্রিভুজের কোণ · 9.2 ত্রিভুজের বাহু · 9.3 ত্রিভুজ অঙ্কন · 10.1 সর্বসমতা · 10.2 সদৃশতা · 10.3 সদৃশতার প্রয়োগ · 11 তথ্য ও উপাত্ত"""
import random, pathlib, sys, math
from fractions import Fraction as F
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from mcqlib import Bank, save as _save, E, M, H, fr, num, pfmt, pmul, padd, pscale, ppow, lin, sup

R = random.Random(2026110707)
import re as _re
def _clean(t):
    t = _re.sub(r'\^(\d+)', lambda m: m.group(1).translate(str.maketrans('0123456789', '⁰¹²³⁴⁵⁶⁷⁸⁹')), t)
    t = _re.sub(r'(?<![\d.])(\d+)/1(?![\d.])', r'\1', t)
    return t
def save(ch, items):
    for x in items:
        x['q'] = _clean(x['q']); x['o'] = [_clean(o) for o in x['o']]; x['e'] = _clean(x['e'])
        assert len(set(x['o'])) == 4, x
    _save(ch, items)
import re as _rw
_FR = _rw.compile(r'^−?\d+/\d+(%| টাকা)?$')
def W(c, pool):
    out = []; c = str(c); cf_ = '/' in c
    for w in pool:
        w = str(w)
        if not cf_ and _FR.match(w): continue   # উত্তর পূর্ণসংখ্যা/দশমিক হলে ভগ্নাংশের ভুল অপশন বাদ
        if w != c and w not in out: out.append(w)
    return out
def nz(a, b): return R.choice([v for v in range(a, b + 1) if v])

class B2(Bank):
    """একই প্রশ্ন-বাক্য (ভিন্ন অপশনে) একটি অনুশীলনীতে সর্বোচ্চ 5 বার"""
    def add(s, q, c, wrong, e, lv):
        st = s.__dict__.setdefault('stems', {})
        if st.get(q, 0) >= 5: return False
        ok = Bank.add(s, q, c, wrong, e, lv)
        if ok: st[q] = st.get(q, 0) + 1
        return ok
def part(ex, total, fixed, eg, mg, hg):
    need = {E: total // 2, M: total * 2 // 5, H: total // 10}
    b = B2(ex, R)
    for q, c, w, e, lv in fixed: b.add(q, c, w, e, lv)
    for lv, gs in ((E, eg), (M, mg), (H, hg)):
        tries, miss = 0, {}
        while b.count(lv) < need[lv]:
            tries += 1
            assert tries < 300000, (ex, lv, b.count(lv), need[lv])
            alive = [g for g in gs if miss.get(g.__name__, 0) < 600] or gs
            g = R.choice(alive); before = b.count(lv)
            try: g(b, lv)
            except (IndexError, ZeroDivisionError, ValueError): pass
            miss[g.__name__] = 0 if b.count(lv) > before else miss.get(g.__name__, 0) + 1
    out = []
    for lv in (E, M, H): out += [x for x in b.items if x['lv'] == lv][:need[lv]]
    assert len(out) == total, (ex, len(out))
    for x in out: assert len(set(x['o'])) == 4, x
    if ex is None:
        for x in out: x.pop('ex', None)
    return out

def D(x):
    """সসীম দশমিক হলে দশমিকে, নইলে ভগ্নাংশে; ঋণাত্মকে −"""
    x = F(x); d = x.denominator
    while d % 2 == 0: d //= 2
    while d % 5 == 0: d //= 5
    if d != 1: return num(x)
    neg = x < 0; x = abs(x); p = 0
    while (x * 10 ** p).denominator != 1: p += 1
    n = str((x * 10 ** p).numerator).rjust(p + 1, '0')
    out = n if p == 0 else n[:-p] + '.' + n[-p:]
    return ('−' if neg else '') + out
def mixed(x):
    x = F(x)
    if x.denominator == 1 or x < 1: return fr(x)
    w = x.numerator // x.denominator; r = x - w
    return f"{w} {fr(r)}" if r else str(w)
def sqfree(n):
    out = 1; d = 2
    while d * d <= n:
        while n % (d * d) == 0: n //= d * d
        d += 1
    return n
def pf(n):
    out, d = [], 2
    while n > 1:
        while n % d == 0: out.append(d); n //= d
        d += 1
    return out
def tk(v): return f"{D(v)} টাকা"
X = ('x',); XY = ('x', 'y'); AB = ('a', 'b')
def P(p, v=XY): return pfmt(p, v)
def deg(c, e): return {e: c}
def mono(c, ex, ey=0): return {(ex, ey): c}
def xl(a):   # x + a  (এক চলক)
    return {(1, 0): 1, (0, 0): a} if a else {(1, 0): 1}
def lf(a):   # (x + a) লেখা
    return f"(x {'+' if a > 0 else '−'} {abs(a)})"
ANG = lambda v: f"{v}°"
def cf(n, v): return ('−' if n < 0 else '') + ('' if abs(n) == 1 else str(abs(n))) + v
SUPX = str.maketrans('0123456789', '⁰¹²³⁴⁵⁶⁷⁸⁹')

# ===================================================== 1.1 বর্গ, পূর্ণবর্গ, মূলদ ও অমূলদ
fx11 = [
 ("কোনো সংখ্যাকে সেই সংখ্যা দিয়ে গুণ করলে গুণফলকে কী বলে?", "সংখ্যাটির বর্গ", ["সংখ্যাটির বর্গমূল", "সংখ্যাটির ঘন", "সংখ্যাটির গুণিতক"], "a × a = a²।", E),
 ("কোনো পূর্ণবর্গ সংখ্যার একক স্থানীয় অঙ্ক কোনটি হতে পারে না?", "7", ["1", "6", "9"], "পূর্ণবর্গের শেষ অঙ্ক 0, 1, 4, 5, 6, 9 হয়; 2, 3, 7, 8 হয় না।", E),
 ("যে সংখ্যাকে p/q (p, q পূর্ণসংখ্যা, q ≠ 0) আকারে লেখা যায়, তাকে কী বলে?", "মূলদ সংখ্যা", ["অমূলদ সংখ্যা", "মৌলিক সংখ্যা", "যৌগিক সংখ্যা"], "মূলদ সংখ্যার সংজ্ঞা।", E),
 ("যে সংখ্যাকে p/q আকারে প্রকাশ করা যায় না, তাকে কী বলে?", "অমূলদ সংখ্যা", ["মূলদ সংখ্যা", "পূর্ণসংখ্যা", "স্বাভাবিক সংখ্যা"], "যেমন √2, √3।", E),
 ("অসীম অনাবৃত্ত দশমিক সংখ্যা কোন ধরনের সংখ্যা?", "অমূলদ", ["মূলদ", "পূর্ণসংখ্যা", "স্বাভাবিক"], "অসীম ও অনাবৃত্ত দশমিক অমূলদ।", E),
 ("আবৃত্ত দশমিক সংখ্যা কোন ধরনের সংখ্যা?", "মূলদ", ["অমূলদ", "মৌলিক", "যৌগিক"], "আবৃত্ত দশমিককে ভগ্নাংশে লেখা যায়।", E),
 ("বিজোড় সংখ্যার বর্গ কী রকম সংখ্যা হয়?", "বিজোড়", ["জোড়", "মৌলিক", "শূন্য"], "বিজোড় × বিজোড় = বিজোড়।", E),
 ("কোনো সংখ্যার শেষে বিজোড় সংখ্যক শূন্য থাকলে সংখ্যাটি কী?", "পূর্ণবর্গ নয়", ["পূর্ণবর্গ", "মৌলিক", "অমূলদ"], "পূর্ণবর্গের শেষে জোড় সংখ্যক শূন্য থাকে।", M),
 ("π সংখ্যাটি কোন ধরনের?", "অমূলদ", ["মূলদ", "পূর্ণসংখ্যা", "পূর্ণবর্গ"], "π = 3.14159… অসীম অনাবৃত্ত।", M),
]
def a11_sq(b, lv):
    n = R.randint(11, 99); v = n * n
    b.add(f"{n} এর বর্গ কত?", v, W(v, [2 * n, v + 1, v - 10, (n + 1) ** 2, (n - 1) ** 2]), f"{n} × {n} = {v}।", lv)
def a11_isq(b, lv):
    k = R.randint(11, 60); c = k * k
    w = []
    while len(w) < 3:
        x = c + R.choice([-1, 1]) * R.randint(1, 2 * k - 1)
        if int(math.isqrt(x)) ** 2 != x and x not in w and x % 10 in (1, 4, 5, 6, 9, 0): w.append(x)
    b.add("নিচের কোনটি পূর্ণবর্গ সংখ্যা?", c, W(c, w), f"{c} = {k}²।", lv)
def a11_notsq(b, lv):
    ks = R.sample(range(11, 70), 3); w = [k * k for k in ks]
    while True:
        x = R.randint(150, 4800)
        if math.isqrt(x) ** 2 != x and x % 10 in (2, 3, 7, 8): break
    b.add("নিচের কোনটি পূর্ণবর্গ সংখ্যা নয়?", x, W(x, w), f"{x} এর একক অঙ্ক {x % 10}; পূর্ণবর্গের শেষে {x % 10} থাকে না।", lv)
def a11_irr(b, lv):
    n = R.choice([v for v in range(2, 99) if math.isqrt(v) ** 2 != v]); c = f"√{n}"
    sq = R.sample([k * k for k in range(2, 11)], 2)
    w = [f"√{sq[0]}", f"{R.randint(2, 9)}/{R.randint(2, 9)}", f"√{sq[1]}", f"{R.randint(1, 9)}.{R.randint(1, 9)}{R.randint(1, 9)}"]
    b.add("নিচের কোনটি অমূলদ সংখ্যা?", c, W(c, w), f"{n} পূর্ণবর্গ নয়, তাই √{n} অমূলদ।", lv)
def a11_rat(b, lv):
    k = R.randint(2, 15); c = f"√{k * k}"
    ns = R.sample([v for v in range(2, 99) if math.isqrt(v) ** 2 != v], 3)
    b.add("নিচের কোনটি মূলদ সংখ্যা?", c, W(c, [f"√{v}" for v in ns]), f"√{k * k} = {k}, যা মূলদ।", lv)
def a11_mul(b, lv):
    m = R.choice([2, 3, 5, 6, 7, 10, 11, 13, 14, 15]); k = R.randint(2, 15); n = k * k * m
    if math.isqrt(n) ** 2 == n: return
    fs = pf(n)
    b.add(f"{n} কে ক্ষুদ্রতম কোন সংখ্যা দ্বারা গুণ করলে গুণফল পূর্ণবর্গ সংখ্যা হবে?", m, W(m, [2 * m, k, m + 1, m * m, 2, 3]), f"{n} = {' × '.join(map(str, fs))}; জোড়া ছাড়া উৎপাদকের গুণফল {m}।", lv)
def a11_div(b, lv):
    m = R.choice([2, 3, 5, 6, 7, 10, 11, 13, 14, 15]); k = R.randint(2, 15); n = k * k * m
    b.add(f"{n} কে ক্ষুদ্রতম কোন সংখ্যা দ্বারা ভাগ করলে ভাগফল পূর্ণবর্গ সংখ্যা হবে?", m, W(m, [2 * m, k, m + 1, k * k, 2, 3]), f"জোড়া ছাড়া মৌলিক উৎপাদকের গুণফল {m}; ভাগফল {k * k} = {k}²।", lv)
def a11_dec(b, lv):
    k = R.randint(1, 15); p = R.choice([1, 2]); x = F(k, 10 ** p); v = x * x
    b.add(f"({D(x)})² = কত?", D(v), W(D(v), [D(2 * x), D(v * 10), D(v / 10), D(x * x * 100) if p == 2 else D(v + F(1, 100))]), "দশমিকের পর অঙ্কসংখ্যা দ্বিগুণ হয়।", lv)
def a11_frac(b, lv):
    p, q = R.randint(1, 12), R.randint(2, 15)
    if math.gcd(p, q) != 1: return
    v = F(p * p, q * q)
    b.add(f"({p}/{q})² = কত?", fr(v), W(fr(v), [fr(F(2 * p, q)), f"{p * p}/{q}", f"{p}/{q * q}", fr(F(p * p, 2 * q))]), "লব ও হর উভয়ের বর্গ।", lv)
def a11_between(b, lv):
    n = R.randint(5, 60); v = 2 * n
    b.add(f"{n}² এবং {n + 1}² এর মধ্যে কয়টি স্বাভাবিক সংখ্যা আছে?", v, W(v, [v + 1, v - 1, n, 2 * n + 2]), "n² ও (n + 1)² এর মধ্যে 2n টি সংখ্যা।", lv)
def a11_odd(b, lv):
    n = R.randint(5, 40); v = n * n
    b.add(f"প্রথম {n}টি বিজোড় স্বাভাবিক সংখ্যার যোগফল কত?", v, W(v, [n * (n + 1), v + n, 2 * n, v - 1]), "প্রথম n টি বিজোড় সংখ্যার যোগফল n²।", lv)
def a11_unit(b, lv):
    n = R.randint(12, 999); u = (n % 10) ** 2 % 10
    b.add(f"{n}² এর একক স্থানীয় অঙ্ক কোনটি?", u, W(u, [n % 10, (u + 1) % 10, (u + 3) % 10, (2 * (n % 10)) % 10, (u + 5) % 10]), f"{n % 10}² = {(n % 10) ** 2}, তাই একক অঙ্ক {u}।", lv)
def a11_add(b, lv):
    n = R.randint(120, 9000); r = math.isqrt(n)
    if r * r == n: return
    v = (r + 1) ** 2 - n
    b.add(f"{n} এর সাথে ক্ষুদ্রতম কোন সংখ্যা যোগ করলে যোগফল পূর্ণবর্গ সংখ্যা হবে?", v, W(v, [n - r * r, v + 1, v + 2 * r, 2 * r + 1]), f"{r + 1}² = {(r + 1) ** 2}; {(r + 1) ** 2} − {n} = {v}।", lv)
def a11_sub(b, lv):
    n = R.randint(120, 9000); r = math.isqrt(n)
    if r * r == n: return
    v = n - r * r
    b.add(f"{n} থেকে ক্ষুদ্রতম কোন সংখ্যা বিয়োগ করলে বিয়োগফল পূর্ণবর্গ সংখ্যা হবে?", v, W(v, [(r + 1) ** 2 - n, v + 1, v - 1 if v > 1 else v + 3, 2 * r]), f"{r}² = {r * r}; {n} − {r * r} = {v}।", lv)
def a11_digits(b, lv):
    d = R.randint(2, 6); v = 2 * d - 1 if R.random() < .5 else 2 * d
    k = R.randint(10 ** (d - 1), 10 ** d - 1)
    sq = k * k; v = len(str(sq))
    b.add(f"{k} এর বর্গে কয়টি অঙ্ক থাকবে?", v, W(v, [d, v + 1, v - 1, 2 * d + 1 if v != 2 * d + 1 else 2 * d - 2]), f"{k}² = {sq}।", lv)
P11 = part('1.1', 150, fx11, [a11_sq, a11_isq, a11_notsq, a11_irr, a11_rat, a11_unit], [a11_mul, a11_div, a11_dec, a11_frac, a11_between, a11_odd, a11_digits], [a11_add, a11_sub, a11_mul, a11_div])

# ===================================================== 1.2 বর্গমূল
fx12 = [
 ("বর্গমূলের প্রতীক কোনটি?", "√", ["²", "∛", "%"], "", E),
 ("√1 = কত?", "1", ["0", "2", "1/2"], "", E),
 ("কোনো পূর্ণবর্গ সংখ্যার বর্গমূল নির্ণয়ের একটি পদ্ধতি কোনটি?", "মৌলিক উৎপাদকে বিশ্লেষণ", ["ল.সা.গু. নির্ণয়", "ঐকিক নিয়ম", "শতকরা নির্ণয়"], "জোড়া মৌলিক উৎপাদক থেকে একটি করে নিয়ে গুণ।", E),
 ("ভাগ পদ্ধতিতে বর্গমূল নির্ণয়ের সময় ডান দিক থেকে কয়টি করে অঙ্ক জোড় বাঁধা হয়?", "2টি", ["1টি", "3টি", "4টি"], "ডান থেকে দুই অঙ্ক করে।", E),
 ("দশমিক ভগ্নাংশের বর্গমূল নির্ণয়ে দশমিক বিন্দুর পরের অঙ্কগুলো কোন দিক থেকে জোড় বাঁধা হয়?", "বাম দিক থেকে", ["ডান দিক থেকে", "মাঝখান থেকে", "জোড় বাঁধা হয় না"], "দশমিকের পরে বাম থেকে দুই অঙ্ক করে।", M),
]
def b12_root(b, lv):
    k = R.randint(11, 99); n = k * k
    b.add(f"√{n} = কত?", k, W(k, [k + 1, k - 1, n // 2, k + 10, k - 10]), f"{k} × {k} = {n}।", lv)
def b12_pf(b, lv):
    ps = sorted(R.sample([2, 3, 5, 7, 11], R.randint(2, 3))); es = [R.choice([1, 2]) for _ in ps]
    n = 1; r = 1
    for p, e in zip(ps, es): n *= p ** (2 * e); r *= p ** e
    if n > 200000: return
    fs = ' × '.join(f"{p}" for p, e in zip(ps, es) for _ in range(2 * e))
    b.add(f"√{n} = কত?", r, W(r, [r * 2, r + ps[0], n // r if n // r != r else r * 3, r // ps[0] if r // ps[0] != r else r + 1]), f"{n} = {fs}; জোড়া থেকে একটি করে নিয়ে {r}।", lv)
def b12_dec(b, lv):
    k = R.randint(2, 99); p = R.choice([1, 2]); x = F(k, 10 ** p); v = x * x
    if k % 10 == 0: return
    b.add(f"√{D(v)} = কত?", D(x), W(D(x), [D(x * 10), D(x / 10), D(v / 2), D(x + F(1, 10 ** p))]), f"{D(x)} × {D(x)} = {D(v)}।", lv)
def b12_frac(b, lv):
    p, q = R.randint(1, 20), R.randint(2, 25)
    if math.gcd(p, q) != 1: return
    b.add(f"√({p * p}/{q * q}) = কত?", f"{p}/{q}", W(f"{p}/{q}", [f"{q}/{p}", f"{p * p}/{q}", f"{p}/{q * q}", f"{p + 1}/{q}"]), "লব ও হরের আলাদা বর্গমূল।", lv)
def b12_mix(b, lv):
    p, q = R.randint(5, 20), R.randint(2, 9)
    if math.gcd(p, q) != 1 or p <= q: return
    x = F(p, q); v = x * x
    b.add(f"√({mixed(v)}) = কত?", mixed(x), W(mixed(x), [mixed(x + 1), mixed(F(q, p)) if q < p else '1', mixed(x * 2), mixed(v / 2)]), f"{mixed(v)} = {fr(v)}; বর্গমূল {fr(x)} = {mixed(x)}।", lv)
def b12_area(b, lv):
    s = R.randint(5, 90); a = s * s
    t = R.randrange(2)
    if t == 0: b.add(f"একটি বর্গাকার মাঠের ক্ষেত্রফল {a} বর্গমিটার। মাঠটির এক বাহুর দৈর্ঘ্য কত মিটার?", s, W(s, [a // 4, s + 1, 4 * s, s - 1]), f"বাহু = √{a} = {s}।", lv)
    else: b.add(f"একটি বর্গাকার বাগানের ক্ষেত্রফল {a} বর্গমিটার। বাগানটির পরিসীমা কত মিটার?", 4 * s, W(4 * s, [s, 2 * s, a // 4, 4 * s + 4]), f"বাহু = √{a} = {s}; পরিসীমা = 4 × {s}।", lv)
def b12_rows(b, lv):
    k = R.randint(12, 60); n = k * k
    b.add(f"{n} জন শিক্ষার্থীকে এমনভাবে সারিতে দাঁড় করানো হলো যে প্রতি সারিতে যতজন, সারির সংখ্যাও ততটি। সারির সংখ্যা কত?", k, W(k, [k + 1, k - 1, n // 10, 2 * k]), f"সারি = √{n} = {k}।", lv)
def b12_chanda(b, lv):
    k = R.randint(15, 90); n = k * k
    b.add(f"একটি সমিতির প্রত্যেক সদস্য সদস্যসংখ্যার সমান টাকা চাঁদা দেওয়ায় মোট {n} টাকা উঠল। সমিতির সদস্যসংখ্যা কত?", k, W(k, [k + 1, k - 1, n // 100 if n // 100 != k else k + 5, 2 * k]), f"সদস্য = √{n} = {k}।", lv)
def b12_paisa(b, lv):
    k = R.randint(15, 90); n = k * k
    if n % 100 == 0: return
    b.add(f"একদল শিক্ষার্থীর প্রত্যেকে দলের সদস্যসংখ্যার সমান পয়সা চাঁদা দেওয়ায় মোট {D(F(n, 100))} টাকা উঠল। দলের সদস্যসংখ্যা কত?", k, W(k, [k + 1, k - 1, k * 10, k + 10]), f"{D(F(n, 100))} টাকা = {n} পয়সা; √{n} = {k}।", lv)
def b12_digits(b, lv):
    d = R.randint(3, 9); v = (d + 1) // 2
    b.add(f"{d} অঙ্কবিশিষ্ট কোনো পূর্ণবর্গ সংখ্যার বর্গমূলে কয়টি অঙ্ক থাকবে?", v, W(v, [d, v + 1, v - 1 if v > 1 else v + 2, d // 3 + 2]), f"ডান থেকে দুই অঙ্ক করে জোড়ায় {v}টি জোড় (বা একক)।", lv)
def b12_eq(b, lv):
    k = R.randint(3, 40); t = R.randrange(2)
    if t == 0: b.add(f"√x = {k} হলে x = কত?", k * k, W(k * k, [2 * k, k, k * k + k, (k + 1) ** 2]), f"x = {k}² = {k * k}।", lv)
    else:
        a = R.randint(2, 9); b.add(f"√(x + {a}) = {k} হলে x = কত?", k * k - a, W(k * k - a, [k * k + a, k - a, k * k, (k - 1) ** 2]), f"x + {a} = {k * k}।", lv)
def b12_prod(b, lv):
    a, c = R.randint(2, 15), R.randint(2, 15)
    if a == c: return
    v = a * c
    b.add(f"√{a * a} × √{c * c} = কত?", v, W(v, [a + c, a * a * c * c, v + 1, v * 2]), f"{a} × {c} = {v}।", lv)
def b12_subroot(b, lv):
    n = R.randint(300, 9000); r = math.isqrt(n)
    if r * r == n: return
    v = n - r * r
    b.add(f"{n} থেকে ক্ষুদ্রতম কত বিয়োগ করলে বিয়োগফল পূর্ণবর্গ হবে এবং সেই পূর্ণবর্গের বর্গমূল কত?", f"{v}; {r}", W(f"{v}; {r}", [f"{(r + 1) ** 2 - n}; {r + 1}", f"{v + 1}; {r}", f"{v}; {r + 1}", f"{v - 1}; {r - 1}"]), f"{r}² = {r * r}; {n} − {r * r} = {v}।", lv)
def b12_sum(b, lv):
    a, c = R.randint(3, 20), R.randint(3, 20)
    v = a + c
    b.add(f"√{a * a} + √{c * c} = কত?", v, W(v, [math.isqrt(a * a + c * c) if math.isqrt(a * a + c * c) != v else v + 2, a * c, v + 1, v * v]), f"{a} + {c} = {v}।", lv)
P12 = part('1.2', 150, fx12, [b12_root, b12_pf, b12_area, b12_rows, b12_eq, b12_sum], [b12_dec, b12_frac, b12_mix, b12_chanda, b12_digits, b12_prod, b12_pf], [b12_paisa, b12_subroot, b12_mix])
save('v1', P11 + P12)

# ===================================================== 2.1 অনুপাত ও সমানুপাত
fx21 = [
 ("a : b = c : d হলে a ও d কে কী বলে?", "প্রান্তীয় রাশি", ["মধ্য রাশি", "ক্রমিক রাশি", "চতুর্থ সমানুপাতী"], "প্রথম ও চতুর্থ রাশি প্রান্তীয় রাশি।", E),
 ("a : b = c : d হলে b ও c কে কী বলে?", "মধ্য রাশি", ["প্রান্তীয় রাশি", "পূর্বরাশি", "উত্তররাশি"], "দ্বিতীয় ও তৃতীয় রাশি মধ্য রাশি।", E),
 ("সমানুপাতের ক্ষেত্রে কোনটি সঠিক?", "প্রান্তীয় রাশিদ্বয়ের গুণফল = মধ্য রাশিদ্বয়ের গুণফল", ["প্রান্তীয় রাশিদ্বয়ের যোগফল = মধ্য রাশিদ্বয়ের যোগফল", "সব রাশি সমান", "প্রথম রাশি = শেষ রাশি"], "a : b = c : d হলে ad = bc।", E),
 ("a : b অনুপাতে a কে কী বলে?", "পূর্ব রাশি", ["উত্তর রাশি", "মধ্য রাশি", "প্রান্তীয় রাশি"], "", E),
 ("a : b অনুপাতে b কে কী বলে?", "উত্তর রাশি", ["পূর্ব রাশি", "মধ্য রাশি", "চতুর্থ রাশি"], "", E),
 ("a : b = b : c হলে b কে a ও c এর কী বলে?", "মধ্য সমানুপাতী", ["তৃতীয় সমানুপাতী", "চতুর্থ সমানুপাতী", "প্রান্তীয় রাশি"], "b² = ac।", E),
 ("a, b, c ক্রমিক সমানুপাতী হলে কোনটি সঠিক?", "b² = ac", ["a² = bc", "c² = ab", "a + c = 2b"], "a : b = b : c থেকে b² = ac।", M),
 ("অনুপাতের রাশি দুটি কেমন হতে হয়?", "একই জাতীয়", ["ভিন্ন জাতীয়", "সবসময় পূর্ণসংখ্যা", "সবসময় মৌলিক"], "অনুপাত একই এককের রাশির মধ্যে।", M),
]
def c21_simp(b, lv):
    a, c = R.randint(1, 12), R.randint(1, 12); k = R.randint(2, 15)
    if math.gcd(a, c) != 1 or a == c: return
    b.add(f"{a * k} : {c * k} এর সরল রূপ কোনটি?", f"{a} : {c}", W(f"{a} : {c}", [f"{c} : {a}", f"{a * 2} : {c}", f"{a} : {c * 2}", f"{a + 1} : {c + 1}"]), f"উভয় রাশিকে {k} দিয়ে ভাগ।", lv)
def c21_fourth(b, lv):
    a, c = R.randint(2, 15), R.randint(2, 30); k = R.randint(2, 12); bb = a * k // math.gcd(a, k) if False else R.randint(2, 30)
    if (bb * c) % a: return
    v = bb * c // a
    b.add(f"{a}, {bb} ও {c} এর চতুর্থ সমানুপাতী কত?", v, W(v, [a * c // bb if (a * c) % bb == 0 and a * c // bb != v else v + 2, v + 1, bb * c, v * 2]), f"{a} : {bb} = {c} : x ⇒ x = ({bb} × {c}) / {a} = {v}।", lv)
def c21_third(b, lv):
    a = R.randint(2, 12); bb = a * R.randint(2, 6)
    v = bb * bb // a
    b.add(f"{a} ও {bb} এর তৃতীয় সমানুপাতী কত?", v, W(v, [bb * 2 - a, a * bb, v + a, bb + a]), f"{a} : {bb} = {bb} : x ⇒ x = {bb}²/{a} = {v}।", lv)
def c21_mean(b, lv):
    p, q = R.randint(1, 12), R.randint(1, 12); k = R.randint(1, 6)
    if p == q: return
    a, c = k * p * p, k * q * q; v = k * p * q
    b.add(f"{a} ও {c} এর মধ্য সমানুপাতী কত?", v, W(v, [(a + c) // 2 if (a + c) // 2 != v else v + 1, a * c, v + k, abs(c - a)]), f"√({a} × {c}) = {v}।", lv)
def c21_miss(b, lv):
    a, bb = R.randint(2, 15), R.randint(2, 15); k = R.randint(2, 9)
    if a == bb: return
    c, d = a * k, bb * k; pos = R.randrange(4); vals = [a, bb, c, d]; ans = vals[pos]
    s = ' : '.join('x' if i == pos else str(v) for i, v in enumerate(vals[:2])) + ' = ' + ' : '.join('x' if i + 2 == pos else str(v) for i, v in enumerate(vals[2:]))
    b.add(f"{s} হলে x = কত?", ans, W(ans, [ans + 1, ans * 2, ans + k, max(1, ans - k), ans + 3]), "প্রান্তীয় রাশির গুণফল = মধ্য রাশির গুণফল।", lv)
def c21_unit(b, lv):
    t = R.randrange(4)
    if t == 0: a, c = R.randint(2, 9) * 25, R.randint(1, 9); q = f"{a} পয়সা : {c} টাকা"; x, y = a, c * 100
    elif t == 1: a, c = R.randint(1, 9) * 50, R.randint(1, 5); q = f"{a} গ্রাম : {c} কেজি"; x, y = a, c * 1000
    elif t == 2: a, c = R.randint(1, 9) * 10, R.randint(1, 5); q = f"{a} সেমি : {c} মিটার"; x, y = a, c * 100
    else: a, c = R.randint(1, 11) * 5, R.randint(1, 4); q = f"{a} মিনিট : {c} ঘণ্টা"; x, y = a, c * 60
    g = math.gcd(x, y); cc = f"{x // g} : {y // g}"
    b.add(f"{q} = কত?", cc, W(cc, [f"{a} : {c}", f"{y // g} : {x // g}", f"{x // g} : {y // g * 10}", f"{x // g * 10} : {y // g}"]), "একই এককে এনে সরল।", lv)
def c21_check(b, lv):
    a, bb = R.randint(2, 12), R.randint(2, 12); k = R.randint(2, 6)
    if a == bb: return
    c = f"{a}, {bb}, {a * k}, {bb * k}"
    w = [f"{a}, {bb}, {a * k}, {bb * k + 1}", f"{a}, {bb}, {bb * k}, {a * k}" if a * k != bb * k else f"{a}, {bb + 1}, {a * k}, {bb * k}", f"{a}, {bb}, {a + k}, {bb + k}", f"{a + 1}, {bb}, {a * k}, {bb * k}"]
    b.add("নিচের কোন চারটি সংখ্যা ক্রমানুসারে সমানুপাতী?", c, W(c, w), f"{a} × {bb * k} = {bb} × {a * k}।", lv)
def c21_abc(b, lv):
    p, q, r, s = R.randint(1, 9), R.randint(1, 9), R.randint(1, 9), R.randint(1, 9)
    if p == q or r == s: return
    A, B, C = p * r, q * r, q * s; g = math.gcd(A, math.gcd(B, C)); A, B, C = A // g, B // g, C // g
    cc = f"{A} : {B} : {C}"
    b.add(f"a : b = {p} : {q} এবং b : c = {r} : {s} হলে a : b : c = কত?", cc, W(cc, [f"{p} : {q * r} : {s}", f"{p * r} : {q * s} : {q * r}", f"{p} : {q} : {s}", f"{A} : {C} : {B}", f"{C} : {B} : {A}"]), f"b কে সমান করে: {p}×{r} : {q}×{r} : {q}×{s}।", lv)
def c21_ac(b, lv):
    p, q, r, s = R.randint(1, 9), R.randint(1, 9), R.randint(1, 9), R.randint(1, 9)
    if p == q or r == s: return
    A, C = p * r, q * s; g = math.gcd(A, C); cc = f"{A // g} : {C // g}"
    b.add(f"a : b = {p} : {q} এবং b : c = {r} : {s} হলে a : c = কত?", cc, W(cc, [f"{p} : {s}", f"{C // g} : {A // g}", f"{p * s} : {q * r}", f"{p + r} : {q + s}"]), f"a/c = (a/b) × (b/c) = ({p}/{q}) × ({r}/{s})।", lv)
def c21_add(b, lv):
    p, q = R.randint(1, 8), R.randint(2, 9); k = R.randint(2, 12)
    if p >= q or math.gcd(p, q) != 1: return
    x = R.randint(1, 15); r1, r2 = p * k + x, q * k + x; g = math.gcd(r1, r2)
    b.add(f"দুটি সংখ্যার অনুপাত {p} : {q}। প্রত্যেকটির সাথে {x} যোগ করলে অনুপাত {r1 // g} : {r2 // g} হয়। ছোট সংখ্যাটি কত?", p * k, W(p * k, [q * k, p * k + x, k, (p + 1) * k]), f"({p}k + {x}) : ({q}k + {x}) = {r1 // g} : {r2 // g} ⇒ k = {k}।", lv)
def c21_sumr(b, lv):
    p, q = R.randint(1, 9), R.randint(1, 9); k = R.randint(2, 20)
    if p == q: return
    s = (p + q) * k
    b.add(f"দুটি সংখ্যার অনুপাত {p} : {q} এবং এদের যোগফল {s}। বড় সংখ্যাটি কত?", max(p, q) * k, W(max(p, q) * k, [min(p, q) * k, s // 2 if s // 2 != max(p, q) * k else s // 2 + 1, max(p, q) * k + k, s - k]), f"বড়টি = {s} × {max(p, q)}/{p + q}।", lv)
P21 = part('2.1', 150, fx21, [c21_simp, c21_fourth, c21_miss, c21_unit, c21_sumr], [c21_third, c21_mean, c21_check, c21_abc, c21_ac, c21_fourth], [c21_add, c21_abc, c21_mean])

# ===================================================== 2.2 ঐকিক নিয়ম, সমানুপাতিক ভাগ, কাজ ও সময়
fx22 = [
 ("লোকসংখ্যা বাড়লে একই কাজ শেষ করতে সময় কেমন লাগে?", "কম লাগে", ["বেশি লাগে", "একই লাগে", "দ্বিগুণ লাগে"], "লোক ও সময় ব্যস্তানুপাতিক।", E),
 ("জিনিসের পরিমাণ বাড়লে মোট দাম কেমন হয়?", "বাড়ে", ["কমে", "একই থাকে", "অর্ধেক হয়"], "পরিমাণ ও দাম সরলানুপাতিক।", E),
 ("একটি গাড়ির গতিবেগ বাড়লে নির্দিষ্ট দূরত্ব যেতে সময়ের কী হয়?", "কমে", ["বাড়ে", "একই থাকে", "দ্বিগুণ হয়"], "গতিবেগ ও সময় ব্যস্তানুপাতিক।", E),
 ("একজন লোক একটি কাজ d দিনে করলে 1 দিনে কাজের কত অংশ করে?", "1/d অংশ", ["d অংশ", "d/2 অংশ", "2/d অংশ"], "", M),
]
ITEMS = [("কেজি চাল", "টাকা", 40, 90), ("টি কলম", "টাকা", 5, 25), ("টি খাতা", "টাকা", 20, 60), ("লিটার দুধ", "টাকা", 60, 110), ("কেজি আলু", "টাকা", 20, 50), ("ডজন ডিম", "টাকা", 110, 170), ("মিটার কাপড়", "টাকা", 80, 300)]
def d22_unit(b, lv):
    it, u, lo, hi = R.choice(ITEMS); p = R.randint(lo, hi); n, m = R.sample(range(2, 25), 2)
    v = p * m
    b.add(f"{n} {it} এর দাম {p * n} টাকা হলে {m} {it} এর দাম কত টাকা?", v, W(v, [p * n, v + p, v - p, p * (m + 1), p * n * m]), f"1 এককের দাম {p} টাকা; {m} × {p}।", lv)
def d22_inv(b, lv):
    m, d = R.randint(4, 30), R.randint(4, 30); k = R.choice([x for x in range(2, 60) if (m * d) % x == 0 and x != m])
    v = m * d // k
    b.add(f"{m} জন লোক একটি কাজ {d} দিনে করতে পারে। {k} জন লোক কাজটি কত দিনে করতে পারবে?", v, W(v, [d * k // m if (d * k) % m == 0 and d * k // m != v else v + 2, v + 1, m + d - k if m + d - k > 0 and m + d - k != v else v + 3, d]), f"মোট কাজ {m} × {d} = {m * d} জন-দিন; ÷ {k}।", lv)
def d22_need(b, lv):
    m, d = R.randint(4, 30), R.randint(6, 30); k = R.choice([x for x in range(2, d) if (m * d) % x == 0] or [0])
    if not k: return
    v = m * d // k
    b.add(f"{m} জন লোক একটি কাজ {d} দিনে করে। কাজটি {k} দিনে শেষ করতে কত জন লোক লাগবে?", v, W(v, [v - m if v - m > 0 else v + 4, v + 1, m * k // d if (m * k) % d == 0 and m * k // d != v else v + 2, m + d - k]), f"{m} × {d} ÷ {k} = {v}।", lv)
def d22_more(b, lv):
    m, d = R.randint(4, 30), R.randint(6, 30); k = R.choice([x for x in range(2, d) if (m * d) % x == 0] or [0])
    if not k: return
    v = m * d // k - m
    if v <= 0: return
    b.add(f"{m} জন লোক একটি কাজ {d} দিনে করে। কাজটি {k} দিনে শেষ করতে আরও কত জন লোক লাগবে?", v, W(v, [v + m, v + 1, v - 1 if v > 1 else v + 3, m]), f"মোট লোক {m * d // k}; অতিরিক্ত {m * d // k} − {m} = {v}।", lv)
def d22_div(b, lv):
    k = R.randint(3, 4); rs = R.sample(range(1, 10), k - 1) if k == 4 else R.sample(range(1, 10), 3)
    u = R.randint(10, 500); tot = sum(rs) * u; i = R.randrange(len(rs)); v = rs[i] * u
    names = ['প্রথম', 'দ্বিতীয়', 'তৃতীয়']
    b.add(f"{tot} টাকা তিনজনের মধ্যে {' : '.join(map(str, rs))} অনুপাতে ভাগ করে দিলে {names[i]} জন কত টাকা পাবে?", v, W(v, [rs[(i + 1) % 3] * u, rs[(i + 2) % 3] * u, tot // 3 if tot // 3 != v else v + u, v + u]), f"{tot} × {rs[i]}/{sum(rs)} = {v}।", lv)
def d22_div2(b, lv):
    p, q = R.randint(1, 9), R.randint(1, 9)
    if p == q: return
    u = R.randint(20, 900); tot = (p + q) * u; v = abs(p - q) * u
    b.add(f"{tot} টাকা দুই ভাইয়ের মধ্যে {p} : {q} অনুপাতে ভাগ করলে তাদের প্রাপ্ত টাকার পার্থক্য কত?", v, W(v, [p * u, q * u, v + u, tot // 2]), f"এক ভাগ = {u}; পার্থক্য {abs(p - q)} ভাগ।", lv)
def d22_two(b, lv):
    a, c = R.randint(2, 30), R.randint(2, 30)
    if a == c: return
    v = F(a * c, a + c)
    if v.denominator not in (1, 2, 4, 5): return
    b.add(f"রহিম একটি কাজ {a} দিনে এবং করিম {c} দিনে করতে পারে। দুজনে একত্রে কাজটি কত দিনে করবে?", D(v), W(D(v), [D(F(a + c, 2)), D(v + 1), str(a + c), D(abs(a - c)) if a != c else '1']), f"1 দিনে 1/{a} + 1/{c} = {fr(F(a + c, a * c))}; সময় = {D(v)} দিন।", lv)
def d22_food(b, lv):
    n, d = R.randint(20, 300), R.randint(10, 60); add = R.choice([x for x in range(5, 200) if (n * d) % (n + x) == 0] or [0])
    if not add: return
    v = n * d // (n + add)
    b.add(f"একটি ছাত্রাবাসে {n} জন ছাত্রের {d} দিনের খাবার আছে। আরও {add} জন ছাত্র এলে ঐ খাবারে কত দিন চলবে?", v, W(v, [x for x in [d - add // 10 if d - add // 10 != v else v + 3, v + 1, v - 1, d, v + 2] if x > 0]), f"{n} × {d} = {n * d} জন-দিন; ÷ {n + add}।", lv)
def d22_left(b, lv):
    n, d = R.randint(20, 300), R.randint(10, 60); x = R.randint(1, d - 2); go = R.choice([g for g in range(5, n // 2 + 1) if (n * (d - x)) % (n - g) == 0] or [0])
    if not go: return
    v = n * (d - x) // (n - go)
    b.add(f"একটি দুর্গে {n} জন সৈন্যের {d} দিনের খাদ্য আছে। {x} দিন পর {go} জন সৈন্য চলে গেল। বাকি খাদ্যে অবশিষ্ট সৈন্যদের কত দিন চলবে?", v, W(v, [v + x, d - x, v - 1, v + 1]), f"বাকি খাদ্য {n} × {d - x}; ÷ {n - go}।", lv)
def d22_speed(b, lv):
    s, t = R.randint(20, 80), R.randint(2, 9); s2 = R.choice([x for x in range(15, 100) if (s * t) % x == 0 and x != s])
    v = s * t // s2
    b.add(f"ঘণ্টায় {s} কিমি বেগে চলে একটি বাস {t} ঘণ্টায় একটি পথ অতিক্রম করে। ঘণ্টায় {s2} কিমি বেগে চললে ঐ পথ যেতে কত ঘণ্টা লাগবে?", D(v), W(D(v), [D(F(s2 * t, s)), D(v + 1), D(t), D(v + 2)]), f"পথ = {s * t} কিমি; সময় = {s * t}/{s2}।", lv)
def d22_three(b, lv):
    m, h, d = R.randint(4, 20), R.randint(4, 10), R.randint(4, 30); m2, h2 = R.randint(4, 30), R.randint(4, 12)
    tot = m * h * d
    if tot % (m2 * h2): return
    v = tot // (m2 * h2)
    b.add(f"{m} জন লোক দৈনিক {h} ঘণ্টা কাজ করে একটি কাজ {d} দিনে শেষ করে। {m2} জন লোক দৈনিক {h2} ঘণ্টা কাজ করলে কাজটি কত দিনে শেষ করবে?", v, W(v, [v + 1, v + 2, d, max(1, v - 1), tot // m2 if tot // m2 != v else v + 3]), f"{m} × {h} × {d} = {tot}; ÷ ({m2} × {h2})।", lv)
P22 = part('2.2', 150, fx22, [d22_unit, d22_inv, d22_div2, d22_speed], [d22_need, d22_more, d22_div, d22_two, d22_food, d22_inv], [d22_left, d22_three, d22_two])

# ===================================================== 2.3 লাভ-ক্ষতি
fx23 = [
 ("বিক্রয়মূল্য ক্রয়মূল্যের চেয়ে বেশি হলে কী হয়?", "লাভ", ["ক্ষতি", "লাভ-ক্ষতি কিছুই না", "মুনাফা কমে"], "", E),
 ("লাভ বা ক্ষতি সাধারণত কিসের উপর হিসাব করা হয়?", "ক্রয়মূল্যের উপর", ["বিক্রয়মূল্যের উপর", "লাভের উপর", "মোট আয়ের উপর"], "", E),
 ("বিক্রয়মূল্য = ক্রয়মূল্য হলে কী হয়?", "লাভ বা ক্ষতি কিছুই হয় না", ["লাভ হয়", "ক্ষতি হয়", "দ্বিগুণ লাভ হয়"], "", E),
 ("লাভ = কত?", "বিক্রয়মূল্য − ক্রয়মূল্য", ["ক্রয়মূল্য − বিক্রয়মূল্য", "বিক্রয়মূল্য + ক্রয়মূল্য", "বিক্রয়মূল্য ÷ ক্রয়মূল্য"], "", E),
 ("শতকরা লাভ নির্ণয়ের সূত্র কোনটি?", "(লাভ ÷ ক্রয়মূল্য) × 100", ["(লাভ ÷ বিক্রয়মূল্য) × 100", "(ক্রয়মূল্য ÷ লাভ) × 100", "লাভ × 100"], "", M),
]
def e23_pl(b, lv):
    cp = R.randint(50, 5000); d = R.randint(5, 900); g = R.random() < .5; sp = cp + d if g else cp - d
    if sp <= 0: return
    b.add(f"একটি জিনিস {cp} টাকায় কিনে {sp} টাকায় বিক্রয় করলে কত টাকা {'লাভ' if g else 'ক্ষতি'} হবে?", d, W(d, [d + 10, d - 10 if d > 10 else d + 5, cp + sp, d * 2]), f"{max(cp, sp)} − {min(cp, sp)} = {d}।", lv)
def e23_pct(b, lv):
    cp = R.choice([100, 120, 150, 200, 250, 300, 400, 500, 600, 750, 800, 1000, 1200, 1500, 2000, 2500]); r = R.choice([4, 5, 8, 10, 12, 15, 16, 20, 24, 25, 30]); g = R.random() < .5
    d = cp * r // 100
    if cp * r % 100: return
    sp = cp + d if g else cp - d
    b.add(f"একটি জিনিস {cp} টাকায় কিনে {sp} টাকায় বিক্রয় করলে শতকরা কত {'লাভ' if g else 'ক্ষতি'} হবে?", f"{r}%", W(f"{r}%", [f"{D(F(d * 100, sp))}%", f"{r + 5}%", f"{d}%", f"{r * 2}%"]), f"({d} ÷ {cp}) × 100 = {r}%।", lv)
def e23_sp(b, lv):
    cp = R.randint(2, 80) * 25; r = R.choice([5, 8, 10, 12, 15, 20, 25]); g = R.random() < .5
    v = F(cp * (100 + r if g else 100 - r), 100)
    b.add(f"একটি জিনিস {cp} টাকায় কিনে শতকরা {r} টাকা {'লাভে' if g else 'ক্ষতিতে'} বিক্রয় করলে বিক্রয়মূল্য কত টাকা?", D(v), W(D(v), [D(F(cp * (100 - r if g else 100 + r), 100)), D(cp + r), D(v + 10), D(F(cp * r, 100))]), f"{cp} × ({100 + r if g else 100 - r}/100) = {D(v)}।", lv)
def e23_cp(b, lv):
    r = R.choice([5, 10, 12, 15, 20, 25]); g = R.random() < .5; k = 100 + r if g else 100 - r
    cp = R.randint(2, 80) * 20; sp = F(cp * k, 100)
    if sp.denominator != 1: return
    b.add(f"একটি জিনিস {sp} টাকায় বিক্রয় করায় শতকরা {r} টাকা {'লাভ' if g else 'ক্ষতি'} হলো। জিনিসটির ক্রয়মূল্য কত টাকা?", cp, W(cp, [int(sp) - r if g else int(sp) + r, D(F(int(sp) * (100 - r if g else 100 + r), 100)), cp + 20, cp - 20]), f"ক্রয়মূল্য = {sp} × 100/{k} = {cp}।", lv)
def e23_bulk(b, lv):
    n, p = R.randint(5, 30), R.randint(2, 20); m, s = R.randint(3, 25), R.randint(2, 20)
    cp1, sp1 = F(p, n), F(s, m)
    if cp1 == sp1: return
    r = (sp1 - cp1) / cp1 * 100
    if r.denominator not in (1, 2, 4, 5): return
    g = r > 0
    b.add(f"টাকায় {n}টি করে কলা কিনে টাকায় {m}টি করে বিক্রয় করলে শতকরা কত {'লাভ' if g else 'ক্ষতি'} হবে?" if p == 1 and s == 1 else f"{p} টাকায় {n}টি করে কলা কিনে {s} টাকায় {m}টি করে বিক্রয় করলে শতকরা কত {'লাভ' if g else 'ক্ষতি'} হবে?", f"{D(abs(r))}%", W(f"{D(abs(r))}%", [f"{D(abs(r) + 5)}%", f"{D(abs(sp1 - cp1) / sp1 * 100)}%", f"{D(abs(r) * 2)}%", f"{abs(n - m)}%"]), f"1টির ক্রয়মূল্য {fr(cp1)}, বিক্রয়মূল্য {fr(sp1)} টাকা।", lv)
def e23_target(b, lv):
    cp = R.randint(4, 60) * 50; r1 = R.choice([5, 8, 10, 12, 15]); r2 = R.choice([10, 12, 15, 20, 25])
    sp1 = F(cp * (100 - r1), 100); sp2 = F(cp * (100 + r2), 100); v = sp2 - sp1
    b.add(f"একটি জিনিস {D(sp1)} টাকায় বিক্রয় করায় {r1}% ক্ষতি হলো। আর কত টাকা বেশি দামে বিক্রয় করলে {r2}% লাভ হতো?", D(v), W(D(v), [D(sp2), D(abs(F(cp * (r2 - r1), 100))), D(v + 10), D(F(cp * r2, 100)), D(v - 10)]), f"ক্রয়মূল্য {cp}; {r2}% লাভে {D(sp2)}; পার্থক্য {D(v)}।", lv)
def e23_scp(b, lv):
    n = R.randint(5, 40); c = R.randint(10, 200); s = c + R.randint(-c // 3, c // 2)
    if s == c: return
    d = abs(s - c) * n
    b.add(f"একজন দোকানদার প্রতিটি {c} টাকা দরে {n}টি জিনিস কিনে প্রতিটি {s} টাকা দরে বিক্রয় করল। তার মোট কত টাকা {'লাভ' if s > c else 'ক্ষতি'} হলো?", d, W(d, [abs(s - c), d + n, d - n if d > n else d + 2 * n, s * n]), f"প্রতিটিতে {abs(s - c)} টাকা; × {n}।", lv)
def e23_eq(b, lv):
    cp = R.randint(10, 80) * 25; r = R.choice([5, 10, 15, 20]); d = F(cp * r, 100)
    b.add(f"একটি জিনিস {r}% লাভে বিক্রয় করায় {D(d)} টাকা লাভ হলো। জিনিসটির ক্রয়মূল্য কত টাকা?", cp, W(cp, [D(cp + d), D(d * r), cp + 100, cp - 50]), f"ক্রয়মূল্য = {D(d)} × 100/{r} = {cp}।", lv)
P23 = part('2.3', 150, fx23, [e23_pl, e23_pct, e23_scp, e23_sp], [e23_sp, e23_cp, e23_eq, e23_pct, e23_bulk], [e23_target, e23_bulk, e23_cp])
save('v2', P21 + P22 + P23)

# ===================================================== 3 পরিমাপ (250)
fx3 = [
 ("1 কিলোমিটার = কত মিটার?", "1000", ["100", "10", "10000"], "", E),
 ("1 মিটার = কত সেন্টিমিটার?", "100", ["10", "1000", "50"], "", E),
 ("1 সেন্টিমিটার = কত মিলিমিটার?", "10", ["100", "1", "1000"], "", E),
 ("1 কিলোগ্রাম = কত গ্রাম?", "1000", ["100", "10", "10000"], "", E),
 ("1 কুইন্টাল = কত কিলোগ্রাম?", "100", ["1000", "10", "50"], "", E),
 ("1 মেট্রিক টন = কত কিলোগ্রাম?", "1000", ["100", "10000", "500"], "", E),
 ("1 লিটার = কত মিলিলিটার?", "1000", ["100", "10", "10000"], "", E),
 ("1 লিটার = কত ঘন সেন্টিমিটার?", "1000", ["100", "10", "10000"], "1 ঘন সেমি = 1 মিলিলিটার।", E),
 ("দৈর্ঘ্য পরিমাপের মূল একক কোনটি?", "মিটার", ["গ্রাম", "লিটার", "সেকেন্ড"], "", E),
 ("ওজন পরিমাপের মূল একক কোনটি?", "গ্রাম", ["মিটার", "লিটার", "বর্গমিটার"], "", E),
 ("তরল পদার্থের আয়তন পরিমাপের মূল একক কোনটি?", "লিটার", ["গ্রাম", "মিটার", "হেক্টর"], "", E),
 ("1 হেক্টর = কত বর্গমিটার?", "10000", ["1000", "100", "100000"], "", M),
 ("1 বর্গমিটার = কত বর্গসেন্টিমিটার?", "10000", ["100", "1000", "1000000"], "100 × 100।", M),
 ("1 ঘনমিটার = কত লিটার?", "1000", ["100", "10000", "10"], "", M),
 ("1 ইঞ্চি = প্রায় কত সেন্টিমিটার?", "2.54", ["2.45", "1.54", "3.28"], "", M),
 ("1 মিটার = প্রায় কত ইঞ্চি?", "39.37", ["36", "12", "3.28"], "", M),
 ("1 কিলোগ্রাম = প্রায় কত পাউন্ড?", "2.2", ["1.2", "0.45", "3.5"], "", M),
 ("1 গজ = কত ফুট?", "3", ["12", "36", "2"], "", E),
 ("1 ফুট = কত ইঞ্চি?", "12", ["10", "3", "36"], "", E),
 ("আয়তাকার ক্ষেত্রের ক্ষেত্রফলের সূত্র কোনটি?", "দৈর্ঘ্য × প্রস্থ", ["2(দৈর্ঘ্য + প্রস্থ)", "দৈর্ঘ্য + প্রস্থ", "(দৈর্ঘ্য × প্রস্থ) / 2"], "", E),
 ("ত্রিভুজক্ষেত্রের ক্ষেত্রফলের সূত্র কোনটি?", "½ × ভূমি × উচ্চতা", ["ভূমি × উচ্চতা", "ভূমি + উচ্চতা", "2 × ভূমি × উচ্চতা"], "", E),
 ("আয়তাকার ঘনবস্তুর আয়তনের সূত্র কোনটি?", "দৈর্ঘ্য × প্রস্থ × উচ্চতা", ["2(দৈর্ঘ্য + প্রস্থ) × উচ্চতা", "দৈর্ঘ্য × প্রস্থ", "দৈর্ঘ্য + প্রস্থ + উচ্চতা"], "", E),
]
LEN = [('কিলোমিটার', 1000), ('মিটার', 1), ('সেন্টিমিটার', F(1, 100)), ('মিলিমিটার', F(1, 1000)), ('ডেসিমিটার', F(1, 10)), ('হেক্টোমিটার', 100), ('ডেকামিটার', 10)]
MAS = [('মেট্রিক টন', 1000000), ('কুইন্টাল', 100000), ('কিলোগ্রাম', 1000), ('গ্রাম', 1), ('মিলিগ্রাম', F(1, 1000))]
VOL = [('কিলোলিটার', 1000), ('লিটার', 1), ('মিলিলিটার', F(1, 1000)), ('ডেসিলিটার', F(1, 10))]
def f3_conv(b, lv):
    tab = R.choice([LEN, MAS, VOL]); (u1, k1), (u2, k2) = R.sample(tab, 2)
    if lv == E and abs(math.log10(float(F(k1) / F(k2)))) > 3: return
    x = R.choice([R.randint(2, 99), F(R.randint(11, 999), 10)]); v = F(x) * F(k1) / F(k2)
    if len(D(v)) > 12: return
    b.add(f"{D(x)} {u1} = কত {u2}?", D(v), W(D(v), [D(v * 10), D(v / 10), D(v * 100), D(v / 100)]), f"1 {u1} = {D(F(k1) / F(k2))} {u2}।", lv)
def f3_mix(b, lv):
    t = R.randrange(3)
    if t == 0: a, c = R.randint(1, 20), R.randint(1, 999); v = F(a * 1000 + c, 1000); q = f"{a} কিলোমিটার {c} মিটার = কত কিলোমিটার?"
    elif t == 1: a, c = R.randint(1, 50), R.randint(1, 999); v = F(a * 1000 + c, 1000); q = f"{a} কিলোগ্রাম {c} গ্রাম = কত কিলোগ্রাম?"
    else: a, c = R.randint(1, 30), R.randint(1, 999); v = F(a * 1000 + c, 1000); q = f"{a} লিটার {c} মিলিলিটার = কত লিটার?"
    b.add(q, D(v), W(D(v), [D(a + F(c, 100)), D(a + F(c, 10000)), D(a * 1000 + c), D(a + F(c, 10)) if c < 100 else D(v + 1)]), "1000 ভাগের হিসাবে দশমিকে লেখো।", lv)
def f3_rect(b, lv):
    l, w = R.randint(5, 120), R.randint(3, 80)
    if l == w: return
    t = R.randrange(2)
    if t == 0: b.add(f"একটি আয়তাকার ক্ষেত্রের দৈর্ঘ্য {l} মিটার ও প্রস্থ {w} মিটার। এর ক্ষেত্রফল কত বর্গমিটার?", l * w, W(l * w, [2 * (l + w), l + w, l * w + l, l * w // 2]), f"{l} × {w} = {l * w}।", lv)
    else: b.add(f"একটি আয়তাকার ক্ষেত্রের দৈর্ঘ্য {l} মিটার ও প্রস্থ {w} মিটার। এর পরিসীমা কত মিটার?", 2 * (l + w), W(2 * (l + w), [l * w, l + w, 2 * l + w, 4 * l]), f"2({l} + {w}) = {2 * (l + w)}।", lv)
def f3_sq(b, lv):
    s = R.randint(4, 99); t = R.randrange(3)
    if t == 0: b.add(f"একটি বর্গক্ষেত্রের এক বাহুর দৈর্ঘ্য {s} মিটার। এর ক্ষেত্রফল কত বর্গমিটার?", s * s, W(s * s, [4 * s, 2 * s, s * s + s, s * s - s]), "", lv)
    elif t == 1: b.add(f"একটি বর্গক্ষেত্রের পরিসীমা {4 * s} মিটার। এর ক্ষেত্রফল কত বর্গমিটার?", s * s, W(s * s, [4 * s, s, (4 * s) ** 2 // 16 + s, 2 * s * s]), f"বাহু = {4 * s}/4 = {s}।", lv)
    else: b.add(f"একটি বর্গক্ষেত্রের ক্ষেত্রফল {s * s} বর্গমিটার। এর পরিসীমা কত মিটার?", 4 * s, W(4 * s, [s, 2 * s, s * s // 4 if s * s // 4 != 4 * s else 3 * s, 4 * s + 4]), f"বাহু = √{s * s} = {s}।", lv)
def f3_tri(b, lv):
    bs, h = R.randint(4, 60), R.randint(3, 50)
    v = F(bs * h, 2)
    b.add(f"একটি ত্রিভুজের ভূমি {bs} সেমি এবং উচ্চতা {h} সেমি। এর ক্ষেত্রফল কত বর্গসেমি?", D(v), W(D(v), [bs * h, bs + h, D(v + bs), D(v * 3 / 2)]), f"½ × {bs} × {h}।", lv)
def f3_side(b, lv):
    l, w = R.randint(5, 120), R.randint(3, 80)
    if l == w: return
    t = R.randrange(2)
    if t == 0: b.add(f"একটি আয়তাকার জমির ক্ষেত্রফল {l * w} বর্গমিটার এবং দৈর্ঘ্য {l} মিটার। জমিটির প্রস্থ কত মিটার?", w, W(w, [l * w - l, w + 2, l, w * 2]), f"{l * w} ÷ {l} = {w}।", lv)
    else: b.add(f"একটি আয়তাকার বাগানের পরিসীমা {2 * (l + w)} মিটার এবং দৈর্ঘ্য {l} মিটার। বাগানটির প্রস্থ কত মিটার?", w, W(w, [2 * (l + w) - l, l + w, w + 2, 2 * w]), f"{2 * (l + w)}/2 − {l} = {w}।", lv)
def f3_cost(b, lv):
    l, w = R.randint(4, 30), R.randint(3, 20); r = R.randint(2, 30) * 10
    v = l * w * r
    b.add(f"একটি ঘরের মেঝে {l} মিটার লম্বা ও {w} মিটার চওড়া। প্রতি বর্গমিটারে {r} টাকা হিসাবে মেঝে পাকা করতে মোট কত টাকা খরচ হবে?", v, W(v, [2 * (l + w) * r, l * w + r, v + r, (l + w) * r]), f"ক্ষেত্রফল {l * w} বর্গমিটার × {r}।", lv)
def f3_fence(b, lv):
    l, w = R.randint(10, 120), R.randint(5, 80); r = R.randint(5, 60)
    if l == w: return
    v = 2 * (l + w) * r
    b.add(f"{l} মিটার দৈর্ঘ্য ও {w} মিটার প্রস্থবিশিষ্ট একটি আয়তাকার মাঠের চারদিকে প্রতি মিটার {r} টাকা দরে বেড়া দিতে কত টাকা খরচ হবে?", v, W(v, [l * w * r, (l + w) * r, v + r, 4 * l * r]), f"পরিসীমা {2 * (l + w)} মিটার × {r}।", lv)
def f3_path_out(b, lv):
    l, w = R.randint(10, 80), R.randint(6, 60); p = R.randint(1, 5)
    if l == w: return
    v = (l + 2 * p) * (w + 2 * p) - l * w
    b.add(f"{l} মিটার দৈর্ঘ্য ও {w} মিটার প্রস্থবিশিষ্ট একটি আয়তাকার বাগানের বাইরে চারদিকে {p} মিটার চওড়া একটি রাস্তা আছে। রাস্তাটির ক্ষেত্রফল কত বর্গমিটার?", v, W(v, [(l + p) * (w + p) - l * w, l * w - (l - 2 * p) * (w - 2 * p), 2 * (l + w) * p, v + 4 * p * p]), f"({l + 2 * p} × {w + 2 * p}) − ({l} × {w}) = {v}।", lv)
def f3_path_in(b, lv):
    l, w = R.randint(15, 90), R.randint(10, 60); p = R.randint(1, 4)
    if l == w: return
    v = l * w - (l - 2 * p) * (w - 2 * p)
    b.add(f"{l} মিটার দৈর্ঘ্য ও {w} মিটার প্রস্থবিশিষ্ট একটি আয়তাকার মাঠের ভিতরে চারদিকে {p} মিটার চওড়া একটি রাস্তা আছে। রাস্তাটির ক্ষেত্রফল কত বর্গমিটার?", v, W(v, [(l + 2 * p) * (w + 2 * p) - l * w, (l - p) * (w - p), 2 * (l + w) * p, v - 4 * p * p]), f"({l} × {w}) − ({l - 2 * p} × {w - 2 * p}) = {v}।", lv)
def f3_vol(b, lv):
    l, w, h = R.randint(2, 30), R.randint(2, 20), R.randint(2, 15)
    v = l * w * h
    b.add(f"একটি আয়তাকার বাক্সের দৈর্ঘ্য {l} সেমি, প্রস্থ {w} সেমি ও উচ্চতা {h} সেমি। বাক্সটির আয়তন কত ঘন সেমি?", v, W(v, [l * w + w * h + h * l, 2 * (l * w + w * h + h * l), l + w + h, v + l * w]), f"{l} × {w} × {h}।", lv)
def f3_tank(b, lv):
    l, w, h = R.randint(1, 6), R.randint(1, 5), R.randint(1, 4)
    t = R.randrange(2)
    if t == 0: v = l * w * h * 1000; b.add(f"একটি চৌবাচ্চার দৈর্ঘ্য {l} মিটার, প্রস্থ {w} মিটার ও গভীরতা {h} মিটার। চৌবাচ্চাটিতে কত লিটার পানি ধরবে?", v, W(v, [l * w * h, v // 10, v * 10, v + 1000]), f"আয়তন {l * w * h} ঘনমিটার; 1 ঘনমিটার = 1000 লিটার।", lv)
    else:
        l, w, h = R.randint(10, 60), R.randint(10, 50), R.randint(10, 40); v = F(l * w * h, 1000)
        b.add(f"{l} সেমি দৈর্ঘ্য, {w} সেমি প্রস্থ ও {h} সেমি উচ্চতার একটি পাত্রে কত লিটার পানি ধরবে?", D(v), W(D(v), [D(v * 10), D(v / 10), str(l * w * h), D(v * 100)]), f"আয়তন {l * w * h} ঘন সেমি = {D(v)} লিটার।", lv)
def f3_tiles(b, lv):
    l, w = R.randint(3, 12), R.randint(3, 10); s = R.choice([20, 25, 40, 50])
    if (l * 100) % s or (w * 100) % s: return
    v = (l * 100 // s) * (w * 100 // s)
    b.add(f"{l} মিটার দৈর্ঘ্য ও {w} মিটার প্রস্থের একটি ঘরের মেঝেতে {s} সেমি বাহুবিশিষ্ট বর্গাকার টাইলস বসাতে কয়টি টাইলস লাগবে?", v, W(v, [l * w, v // 2, v * 2, (l + w) * 100 // s]), f"({l * 100}/{s}) × ({w * 100}/{s}) = {v}।", lv)
def f3_area_conv(b, lv):
    t = R.randrange(3)
    if t == 0: x = R.randint(2, 50); b.add(f"{x} হেক্টর = কত বর্গমিটার?", x * 10000, W(x * 10000, [x * 1000, x * 100, x * 100000]), "1 হেক্টর = 10000 বর্গমিটার।", lv)
    elif t == 1: x = R.randint(2, 90); b.add(f"{x} বর্গমিটার = কত বর্গসেন্টিমিটার?", x * 10000, W(x * 10000, [x * 100, x * 1000, x * 1000000]), "1 বর্গমিটার = 10000 বর্গসেমি।", lv)
    else: x = R.randint(2, 30); b.add(f"{x} ঘনমিটার = কত লিটার?", x * 1000, W(x * 1000, [x * 100, x * 10000, x * 10]), "1 ঘনমিটার = 1000 লিটার।", lv)
def f3_walk(b, lv):
    l, w = R.randint(20, 200), R.randint(10, 150); n = R.randint(2, 10)
    if l == w: return
    v = F(2 * (l + w) * n, 1000)
    b.add(f"{l} মিটার দৈর্ঘ্য ও {w} মিটার প্রস্থের একটি মাঠের চারদিকে {n} বার ঘুরলে কত কিলোমিটার হাঁটা হবে?", D(v), W(D(v), [D(F(l * w * n, 1000)), D(v * 10), D(F((l + w) * n, 1000)), D(v + 1)]), f"{n} × পরিসীমা {2 * (l + w)} মিটার = {D(v)} কিমি।", lv)
def f3_ratio_area(b, lv):
    p, q = R.randint(2, 7), R.randint(2, 7)
    if p == q or math.gcd(p, q) != 1: return
    k = R.randint(2, 10); a = p * q * k * k
    b.add(f"একটি আয়তক্ষেত্রের দৈর্ঘ্য ও প্রস্থের অনুপাত {max(p, q)} : {min(p, q)} এবং ক্ষেত্রফল {a} বর্গমিটার। এর দৈর্ঘ্য কত মিটার?", max(p, q) * k, W(max(p, q) * k, [min(p, q) * k, a // max(p, q), max(p, q) * k + k, 2 * k]), f"{max(p, q)}k × {min(p, q)}k = {a} ⇒ k = {k}।", lv)
def f3_cube(b, lv):
    s = R.randint(2, 20); t = R.randrange(2)
    if t == 0: b.add(f"একটি ঘনকের এক ধারের দৈর্ঘ্য {s} সেমি। এর আয়তন কত ঘন সেমি?", s ** 3, W(s ** 3, [6 * s * s, s * s, 3 * s, s ** 3 + s]), f"{s}³ = {s ** 3}।", lv)
    else: b.add(f"একটি ঘনকের আয়তন {s ** 3} ঘন সেমি। এর এক ধারের দৈর্ঘ্য কত সেমি?", s, W(s, [s ** 3 // 3 if s ** 3 // 3 != s else s + 3, s * s, s + 1, 2 * s]), f"∛{s ** 3} = {s}।", lv)
K3 = part(None, 250, fx3, [f3_conv, f3_mix, f3_rect, f3_sq, f3_tri, f3_area_conv, f3_cube], [f3_side, f3_cost, f3_fence, f3_path_out, f3_vol, f3_tank, f3_tiles, f3_walk, f3_conv], [f3_path_in, f3_path_out, f3_ratio_area, f3_tiles, f3_tank])
save('v3', K3)

# ===================================================== 4.1 গুণ
fx41 = [
 ("aᵐ × aⁿ = কত?", "aᵐ⁺ⁿ", ["aᵐⁿ", "aᵐ⁻ⁿ", "2aᵐ⁺ⁿ"], "সূচকের যোগ।", E),
 ("(+) × (−) = কত?", "(−)", ["(+)", "0", "নির্ণয় করা যায় না"], "", E),
 ("(−) × (−) = কত?", "(+)", ["(−)", "0", "1"], "", E),
 ("বহুপদীকে বহুপদী দ্বারা গুণ করতে কোন নিয়ম কাজে লাগে?", "বণ্টন বিধি", ["বিনিময় বিধি নয়", "ভাগ বিধি", "বিয়োগ বিধি"], "একটির প্রতিটি পদ দিয়ে অপরটির প্রতিটি পদকে গুণ।", M),
]
def g41_idx(b, lv):
    v = R.choice('abxyzmp'); m, n = R.randint(2, 12), R.randint(2, 12)
    c = f"{v}{sup(m + n)}"
    b.add(f"{v}{sup(m)} × {v}{sup(n)} = কত?", c, W(c, [f"{v}{sup(m * n)}", f"{v}{sup(abs(m - n))}" if m != n else f"2{v}{sup(m)}", f"2{v}{sup(m + n)}", f"{v}{sup(m + n + 1)}"]), "সূচক যোগ হয়।", lv)
def g41_mm(b, lv):
    a, c = nz(-9, 9), nz(-9, 9); e1, e2, f1, f2 = R.randint(0, 4), R.randint(1, 4), R.randint(1, 4), R.randint(0, 4)
    p1, p2 = mono(a, e1, e2), mono(c, f1, f2); r = pmul(p1, p2)
    q = f"({P(p1)}) × ({P(p2)}) = কত?"
    cc = P(r)
    b.add(q, cc, W(cc, [P(pscale(r, -1)), P(mono(a * c, e1 * f1, e2 * f2)) if (e1 * f1, e2 * f2) != (e1 + f1, e2 + f2) else P(mono(a * c + 1, e1 + f1, e2 + f2)), P(mono(a + c, e1 + f1, e2 + f2)) if a + c else P(mono(a * c, e1 + f1 + 1, e2 + f2)), P(mono(a * c, e1 + f1, e2 + f2 + 1))]), "সহগ গুণ, সূচক যোগ।", lv)
def g41_mp(b, lv):
    m = mono(nz(-6, 6), R.randint(1, 3), R.randint(0, 2)); p = padd(mono(nz(-7, 7), R.randint(0, 3), R.randint(0, 2)), mono(nz(-7, 7), R.randint(0, 3), R.randint(0, 2)), lin([0, 0], nz(-9, 9)))
    if len(p) < 2: return
    r = pmul(m, p); cc = P(r)
    keys = list(p); bad1 = padd(pmul(m, {keys[0]: p[keys[0]]}), {k: p[k] for k in keys[1:]})
    bad2 = pmul(pscale(m, -1), p); bad3 = padd(r, pmul(m, lin([0, 0], 1)))
    b.add(f"{P(m)}({P(p)}) = কত?", cc, W(cc, [P(bad1), P(bad2), P(bad3), P(padd(r, mono(1, 1, 1)))]), "একপদী দিয়ে প্রতিটি পদকে গুণ।", lv)
def g41_bb(b, lv):
    a, c = nz(-9, 9), nz(-9, 9); k1, k2 = R.choice([1, 1, 2, 3]), R.choice([1, 1, 2, 3])
    p1 = padd(mono(k1, 1, 0), lin([0, 0], a)); p2 = padd(mono(k2, 1, 0), lin([0, 0], c)); r = pmul(p1, p2); cc = P(r, X + ('y',))
    bad = [padd(mono(k1 * k2, 2, 0), lin([0, 0], a * c)), padd(r, mono(2, 1, 0)), padd(mono(k1 * k2, 2, 0), mono(k1 * c - k2 * a, 1, 0) if k1 * c - k2 * a else mono(1, 1, 0), lin([0, 0], a * c)), padd(mono(k1 * k2, 2, 0), mono(k1 * c + k2 * a, 1, 0), lin([0, 0], -a * c))]
    b.add(f"({P(p1)})({P(p2)}) = কত?", cc, W(cc, [P(x) for x in bad]), "প্রথম বন্ধনীর প্রতিটি পদ দিয়ে দ্বিতীয়টির প্রতিটি পদকে গুণ।", lv)
def g41_coef(b, lv):
    a, c, d = nz(-6, 6), nz(-6, 6), nz(-6, 6)
    p1 = padd(mono(1, 1, 0), lin([0, 0], a)); p2 = padd(mono(1, 2, 0), mono(c, 1, 0), lin([0, 0], d)); r = pmul(p1, p2)
    k = R.choice([(2, 0), (1, 0)]); v = r.get(k, 0)
    nm = 'x²' if k == (2, 0) else 'x'
    b.add(f"({P(p1)})({P(p2)}) গুণফলে {nm} এর সহগ কত?", num(v), W(num(v), [num(v + 1), num(-v) if v else '1', num(a * c), num(c + d) if c + d != v else num(v - 2)]), f"গুণফল = {P(r)}।", lv)
def g41_three(b, lv):
    a = R.randint(1, 6)
    p1 = padd(mono(1, 1, 0), lin([0, 0], a)); p2 = padd(mono(1, 2, 0), mono(-a, 1, 0), lin([0, 0], a * a))
    if R.random() < .5: p1 = padd(mono(1, 1, 0), lin([0, 0], -a)); p2 = padd(mono(1, 2, 0), mono(a, 1, 0), lin([0, 0], a * a))
    r = pmul(p1, p2); cc = P(r)
    b.add(f"({P(p1)})({P(p2)}) = কত?", cc, W(cc, [P(pscale(r, -1)), P(padd(mono(1, 3, 0), lin([0, 0], -r.get((0, 0), 0)))), P(padd(r, mono(2 * a, 2, 0))), P(padd(mono(1, 3, 0), mono(a, 2, 0), lin([0, 0], r.get((0, 0), 0))))]), "গুণ করে সদৃশ পদ যোগ করলে মাঝের পদ বাদ যায়।", lv)
def g41_val(b, lv):
    a, c = nz(-5, 5), nz(-5, 5); x = nz(-4, 4)
    p1 = padd(mono(1, 1, 0), lin([0, 0], a)); p2 = padd(mono(2, 1, 0), lin([0, 0], c)); v = (x + a) * (2 * x + c)
    b.add(f"x = {num(x)} হলে ({P(p1)})({P(p2)}) এর মান কত?", num(v), W(num(v), [num(v + 2), num(-v) if v else '2', num((x + a) + (2 * x + c)), num(v - 4)]), f"({num(x + a)}) × ({num(2 * x + c)})।", lv)
def g41_xy(b, lv):
    a, c, d, e = nz(-5, 5), nz(-5, 5), nz(-5, 5), nz(-5, 5)
    p1 = lin([a, c]); p2 = lin([d, e]); r = pmul(p1, p2); cc = P(r)
    b.add(f"({P(p1)})({P(p2)}) = কত?", cc, W(cc, [P(padd(mono(a * d, 2, 0), mono(c * e, 0, 2))), P(pscale(r, -1)), P(padd(r, mono(1, 1, 1))), P(padd(mono(a * d, 2, 0), mono(-(a * e + c * d), 1, 1) if a * e + c * d else mono(1, 1, 1), mono(c * e, 0, 2)))]), "", lv)
P41 = part('4.1', 150, fx41, [g41_idx, g41_mm, g41_mp], [g41_bb, g41_mp, g41_xy, g41_val], [g41_coef, g41_three, g41_val])

# ===================================================== 4.2 ভাগ
fx42 = [
 ("aᵐ ÷ aⁿ = কত? (a ≠ 0)", "aᵐ⁻ⁿ", ["aᵐ⁺ⁿ", "aᵐ/ⁿ", "aᵐⁿ"], "সূচকের বিয়োগ।", E),
 ("a⁰ = কত? (a ≠ 0)", "1", ["0", "a", "অসংজ্ঞায়িত"], "", E),
 ("(−) ÷ (−) = কত?", "(+)", ["(−)", "0", "1"], "", E),
 ("(+) ÷ (−) = কত?", "(−)", ["(+)", "0", "1"], "", E),
 ("ভাজ্য = কত?", "ভাজক × ভাগফল + ভাগশেষ", ["ভাজক + ভাগফল", "ভাগফল ÷ ভাজক", "ভাজক × ভাগশেষ"], "", M),
]
def h42_idx(b, lv):
    v = R.choice('abxyzmp'); m = R.randint(4, 15); n = R.randint(1, m - 1)
    c = f"{v}{sup(m - n)}" if m - n > 1 else v
    b.add(f"{v}{sup(m)} ÷ {v}{sup(n)} = কত?", c, W(c, [f"{v}{sup(m + n)}", f"{v}{sup(m // n)}" if m % n == 0 and m // n != m - n else f"{v}{sup(m - n + 1)}", f"{v}{sup(m * n)}", f"1/{v}{sup(m - n)}" if m - n > 1 else f"1/{v}"]), "সূচক বিয়োগ হয়।", lv)
def h42_mm(b, lv):
    a, c = nz(-9, 9), nz(-6, 6); f1, f2 = R.randint(1, 3), R.randint(0, 3); g1, g2 = R.randint(0, 3), R.randint(0, 3)
    q = mono(a, g1, g2); d = mono(c, f1, f2); n = pmul(q, d); cc = P(q)
    if not g1 and not g2: return
    b.add(f"({P(n)}) ÷ ({P(d)}) = কত?", cc, W(cc, [P(pscale(q, -1)), P(mono(a, g1 + f1, g2 + f2)), P(mono(a * c, g1, g2)) if c not in (1, -1) else P(mono(a + 1, g1, g2)), P(mono(a, g1 + 1, g2))]), "সহগ ভাগ, সূচক বিয়োগ।", lv)
def h42_pm(b, lv):
    d = mono(nz(-5, 5), R.randint(1, 2), R.randint(0, 2)); q = padd(mono(nz(-6, 6), R.randint(1, 3), R.randint(0, 2)), mono(nz(-6, 6), R.randint(0, 2), R.randint(0, 2)), lin([0, 0], nz(-7, 7)))
    if len(q) < 2: return
    n = pmul(d, q); cc = P(q)
    keys = list(q)
    b.add(f"({P(n)}) ÷ ({P(d)}) = কত?", cc, W(cc, [P(pscale(q, -1)), P(padd(q, {keys[0]: -2 * q[keys[0]]})), P(padd(q, lin([0, 0], 1))), P(pmul(q, mono(1, 1, 0)))]), "প্রতিটি পদকে আলাদা করে ভাগ।", lv)
def h42_pb(b, lv):
    a = nz(-7, 7); c, e = nz(-7, 7), nz(-9, 9)
    d = padd(mono(1, 1, 0), lin([0, 0], a)); q = padd(mono(R.choice([1, 2, 3]), 1, 0), lin([0, 0], c))
    if R.random() < .4: q = padd(mono(1, 2, 0), mono(c, 1, 0), lin([0, 0], e))
    n = pmul(d, q); cc = P(q)
    b.add(f"({P(n)}) ÷ ({P(d)}) = কত?", cc, W(cc, [P(pscale(q, -1)), P(padd(q, lin([0, 0], 2 * a))), P(padd(q, mono(1, 1, 0))), P(padd(q, lin([0, 0], -1)))]), f"({P(d)}) × ({cc}) = {P(n)}।", lv)
def h42_find(b, lv):
    a, c = nz(-7, 7), nz(-7, 7)
    if a == c: return
    d = padd(mono(1, 1, 0), lin([0, 0], a)); q = padd(mono(1, 1, 0), lin([0, 0], c)); n = pmul(d, q)
    b.add(f"কোন রাশিকে ({P(d)}) দ্বারা গুণ করলে গুণফল {P(n)} হবে?", P(q), W(P(q), [P(padd(mono(1, 1, 0), lin([0, 0], -c))), P(padd(mono(1, 1, 0), lin([0, 0], c + 1))), P(d), P(padd(mono(1, 1, 0), lin([0, 0], a + c)))]), "গুণফলকে প্রদত্ত রাশি দিয়ে ভাগ।", lv)
def h42_rem(b, lv):
    a, c, r = nz(-6, 6), nz(-6, 6), nz(-9, 9)
    d = padd(mono(1, 1, 0), lin([0, 0], a)); q = padd(mono(1, 1, 0), lin([0, 0], c)); n = padd(pmul(d, q), lin([0, 0], r))
    b.add(f"{P(n)} কে ({P(d)}) দ্বারা ভাগ করলে ভাগশেষ কত?", num(r), W(num(r), [num(-r), "0", num(r + a), num(r - 1) if r - 1 else '2']), f"{P(n)} = ({P(d)})({P(q)}) + ({num(r)})।", lv)
def h42_xy(b, lv):
    a, c = nz(-4, 4), nz(-4, 4)
    d = lin([1, a]); q = lin([R.choice([1, 2, 3]), c]); n = pmul(d, q); cc = P(q)
    b.add(f"({P(n)}) ÷ ({P(d)}) = কত?", cc, W(cc, [P(pscale(q, -1)), P(lin([q.get((1, 0), 0), -c])), P(lin([q.get((1, 0), 0) + 1, c])), P(d)]), "", lv)
P42 = part('4.2', 150, fx42, [h42_idx, h42_mm, h42_pm], [h42_pm, h42_pb, h42_find, h42_xy], [h42_rem, h42_pb, h42_xy])

# ===================================================== 4.3 বন্ধনী ও সরলীকরণ
fx43 = [
 ("বন্ধনীর আগে (−) চিহ্ন থাকলে বন্ধনী তুলে দিলে ভিতরের পদগুলোর চিহ্নের কী হয়?", "পরিবর্তিত হয়", ["অপরিবর্তিত থাকে", "সব (+) হয়", "সব (−) হয়"], "", E),
 ("বন্ধনীর আগে (+) চিহ্ন থাকলে বন্ধনী তুলে দিলে ভিতরের পদগুলোর চিহ্নের কী হয়?", "অপরিবর্তিত থাকে", ["পরিবর্তিত হয়", "সব (−) হয়", "শূন্য হয়"], "", E),
 ("একাধিক বন্ধনী থাকলে কোন বন্ধনী আগে তুলতে হয়?", "প্রথম বন্ধনী ( )", ["তৃতীয় বন্ধনী [ ]", "দ্বিতীয় বন্ধনী { }", "যেকোনোটি"], "ভিতর থেকে বাইরের দিকে: ( ), { }, [ ]।", E),
 ("সরলীকরণে ক্রম হিসেবে কোনটি সঠিক?", "বন্ধনী, ভাগ, গুণ, যোগ, বিয়োগ", ["যোগ, বিয়োগ, গুণ, ভাগ", "গুণ, যোগ, ভাগ, বন্ধনী", "বিয়োগ, যোগ, ভাগ, গুণ"], "", M),
]
VV = ('a', 'b')
def i43_rm(b, lv):
    a, c, d = nz(-9, 9), nz(-9, 9), nz(-9, 9)
    p = lin([a, 0]); q = lin([c, d]); r = padd(p, pscale(q, -1)); cc = P(r, VV)
    if not r: return
    b.add(f"{P(p, VV)} − ({P(q, VV)}) = কত?", cc, W(cc, [P(padd(p, q), VV), P(padd(p, lin([-c, d])), VV), P(padd(p, lin([c, -d])), VV), P(pscale(r, -1), VV)]), "বন্ধনীর আগে (−) থাকায় ভিতরের চিহ্ন বদলায়।", lv)
def i43_nest(b, lv):
    a, c, d, e = nz(-9, 9), nz(-9, 9), nz(-9, 9), nz(-9, 9)
    A, B, C, Dd = lin([a, 0]), lin([0, c]), lin([d, 0]), lin([0, e])
    r = padd(A, pscale(padd(B, pscale(padd(C, pscale(Dd, -1)), -1)), -1))
    if not r: return
    cc = P(r, VV)
    wrong1 = padd(A, pscale(padd(B, pscale(padd(C, Dd), -1)), -1)); wrong2 = padd(A, pscale(B, -1), pscale(C, -1), pscale(Dd, -1)); wrong3 = padd(A, B, C, Dd)
    b.add(f"{P(A, VV)} − [{P(B, VV)} − {{{P(C, VV)} − ({P(Dd, VV)})}}] = কত?", cc, W(cc, [P(x, VV) for x in (wrong1, wrong2, wrong3)] + [P(pscale(r, -1), VV)]), "ভিতরের বন্ধনী থেকে শুরু করে একে একে তোলো।", lv)
def i43_comb(b, lv):
    p, q = nz(-6, 6), nz(-6, 6); a, c = nz(-6, 6), nz(-6, 6)
    e1 = pmul(mono(p, 1, 0), padd(mono(1, 1, 0), lin([0, 0], a))); e2 = pmul(mono(q, 1, 0), padd(mono(1, 1, 0), lin([0, 0], c)))
    r = padd(e1, pscale(e2, -1))
    if not r: return
    cc = P(r, X + ('y',))
    b.add(f"{P(mono(p, 1, 0))}(x {'+' if a > 0 else '−'} {abs(a)}) {'−' if q > 0 else '+'} {P(mono(abs(q), 1, 0))}(x {'+' if c > 0 else '−'} {abs(c)}) = কত?", cc, W(cc, [P(padd(e1, e2)), P(pscale(r, -1)), P(padd(e1, pscale(pmul(mono(q, 1, 0), padd(mono(1, 1, 0), lin([0, 0], -c))), -1))), P(padd(r, mono(1, 2, 0)))]), "গুণ করে সদৃশ পদ একত্র।", lv)
def i43_val(b, lv):
    a, c = nz(-5, 5), nz(-5, 5); x, y = nz(-4, 4), nz(-4, 4)
    p, q = nz(-4, 4), nz(-4, 4)
    v = p * x - (q * y - (a * x - c * y))
    b.add(f"a = {num(x)}, b = {num(y)} হলে {P(mono(p, 1, 0), VV)} − {{{P(mono(q, 0, 1), VV)} − ({P(lin([a, -c]), VV)})}} এর মান কত?", num(v), W(num(v), [num(-v) if v else '1', num(v + 2), num(p * x - q * y - a * x + c * y) if p * x - q * y - a * x + c * y != v else num(v - 2), num(v + 4)]), "মান বসানোর আগে বা পরে বন্ধনী তুলে হিসাব।", lv)
def i43_sum(b, lv):
    ps = [padd(mono(nz(-9, 9), 2, 0), mono(nz(-9, 9), 1, 0), lin([0, 0], nz(-9, 9))) for _ in range(2)]
    r = padd(*ps); cc = P(r)
    if len(r) < 2: return
    b.add(f"({P(ps[0])}) + ({P(ps[1])}) = কত?", cc, W(cc, [P(padd(ps[0], pscale(ps[1], -1))), P(pscale(r, -1)), P(padd(r, mono(1, 1, 0))), P(padd(r, lin([0, 0], 2)))]), "সদৃশ পদের সহগ যোগ।", lv)
def i43_diff(b, lv):
    ps = [padd(mono(nz(-9, 9), 2, 0), mono(nz(-9, 9), 1, 0), lin([0, 0], nz(-9, 9))) for _ in range(2)]
    r = padd(ps[0], pscale(ps[1], -1))
    if len(r) < 2: return
    cc = P(r)
    b.add(f"{P(ps[0])} থেকে {P(ps[1])} বিয়োগ করলে বিয়োগফল কত?", cc, W(cc, [P(padd(ps[1], pscale(ps[0], -1))), P(padd(*ps)), P(padd(r, mono(2, 1, 0))), P(padd(r, lin([0, 0], -2)))]), "বিয়োজ্যের চিহ্ন বদলে যোগ।", lv)
def i43_what(b, lv):
    p = padd(mono(nz(-9, 9), 2, 0), mono(nz(-9, 9), 1, 0), lin([0, 0], nz(-9, 9))); s = padd(mono(nz(-9, 9), 2, 0), lin([0, 0], nz(-9, 9)))
    r = padd(s, pscale(p, -1))
    if len(r) < 2: return
    cc = P(r)
    b.add(f"{P(p)} এর সাথে কত যোগ করলে যোগফল {P(s)} হবে?", cc, W(cc, [P(padd(s, p)), P(pscale(r, -1)), P(padd(r, mono(1, 1, 0))), P(padd(r, lin([0, 0], 1)))]), "যোগফল − প্রদত্ত রাশি।", lv)
P43 = part('4.3', 150, fx43, [i43_rm, i43_sum, i43_diff], [i43_nest, i43_comb, i43_what, i43_rm], [i43_val, i43_nest, i43_comb])
save('v4', P41 + P42 + P43)

# ===================================================== 5.1 বর্গের সূত্রাবলি
fx51 = [
 ("(a + b)² = কত?", "a² + 2ab + b²", ["a² + b²", "a² − 2ab + b²", "a² + ab + b²"], "", E),
 ("(a − b)² = কত?", "a² − 2ab + b²", ["a² − b²", "a² + 2ab + b²", "a² − ab + b²"], "", E),
 ("a² − b² = কত?", "(a + b)(a − b)", ["(a − b)²", "(a + b)²", "(a − b)(a − b)"], "", E),
 ("(x + a)(x + b) = কত?", "x² + (a + b)x + ab", ["x² + abx + (a + b)", "x² + ab", "x² − (a + b)x + ab"], "", E),
 ("(a + b)² − (a − b)² = কত?", "4ab", ["2ab", "2(a² + b²)", "0"], "", M),
 ("(a + b)² + (a − b)² = কত?", "2(a² + b²)", ["4ab", "a² + b²", "2ab"], "", M),
 ("(a − b)² = (a + b)² − কত?", "4ab", ["2ab", "ab", "a² + b²"], "", M),
]
def j51_sqp(b, lv):
    k, m = R.choice([1, 1, 2, 3, 4, 5]), R.choice([1, 2, 3, 4, 5, 6, 7]); s = R.choice([1, -1])
    p = lin([k, s * m]); r = ppow(p, 2); cc = P(r)
    b.add(f"({P(p)})² = কত?", cc, W(cc, [P(padd(mono(k * k, 2, 0), mono(m * m, 0, 2))), P(padd(mono(k * k, 2, 0), mono(-s * 2 * k * m, 1, 1), mono(m * m, 0, 2))), P(padd(mono(k * k, 2, 0), mono(s * k * m, 1, 1), mono(m * m, 0, 2))), P(padd(mono(k * k, 2, 0), mono(s * 2 * k * m, 1, 1), mono(-m * m, 0, 2)))]), "(a ± b)² = a² ± 2ab + b²।", lv)
def j51_sqc(b, lv):
    k, a = R.choice([1, 1, 2, 3]), nz(-9, 9)
    p = padd(mono(k, 1, 0), lin([0, 0], a)); r = ppow(p, 2); cc = P(r)
    b.add(f"({P(p)})² = কত?", cc, W(cc, [P(padd(mono(k * k, 2, 0), lin([0, 0], a * a))), P(padd(mono(k * k, 2, 0), mono(-2 * k * a, 1, 0), lin([0, 0], a * a))), P(padd(mono(k * k, 2, 0), mono(k * a, 1, 0), lin([0, 0], a * a))), P(padd(mono(k * k, 2, 0), mono(2 * k * a, 1, 0), lin([0, 0], -a * a)))]), "", lv)
def j51_num(b, lv):
    base = R.choice([10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 200, 1000]); d = R.choice([1, 2, 3, 4, 5]); s = R.choice([1, -1]); n = base + s * d
    v = n * n
    b.add(f"সূত্র প্রয়োগ করে {n}² এর মান কত?", v, W(v, [base * base + d * d, v + 2 * d, v - 2 * d * base // 10 if v - 2 * d * base // 10 != v else v + 1, base * base + s * 2 * base * d - d * d]), f"({base} {'+' if s > 0 else '−'} {d})² = {base * base} {'+' if s > 0 else '−'} {2 * base * d} + {d * d}।", lv)
def j51_diffsq(b, lv):
    base = R.choice([20, 30, 40, 50, 60, 70, 80, 100, 200]); d = R.randint(1, 9)
    v = base * base - d * d
    b.add(f"{base + d} × {base - d} = কত?", v, W(v, [base * base + d * d, v + 1, v - d, base * base]), f"(a + b)(a − b) = a² − b² = {base * base} − {d * d}।", lv)
def j51_xab(b, lv):
    a, c = nz(-9, 9), nz(-9, 9)
    if a == c: return
    p1, p2 = padd(mono(1, 1, 0), lin([0, 0], a)), padd(mono(1, 1, 0), lin([0, 0], c)); r = pmul(p1, p2); cc = P(r)
    b.add(f"({P(p1)})({P(p2)}) = কত?", cc, W(cc, [P(padd(mono(1, 2, 0), mono(a * c, 1, 0), lin([0, 0], a + c))), P(padd(mono(1, 2, 0), mono(-(a + c), 1, 0) if a + c else mono(1, 1, 0), lin([0, 0], a * c))), P(padd(mono(1, 2, 0), mono(a + c, 1, 0), lin([0, 0], -a * c))), P(padd(mono(1, 2, 0), lin([0, 0], a * c)))]), "x² + (a + b)x + ab।", lv)
def j51_sp(b, lv):
    a, c = R.randint(1, 12), R.randint(1, 12)
    s, p = a + c, a * c; t = R.randrange(3)
    if t == 0: v = a * a + c * c; q = f"a + b = {s} এবং ab = {p} হলে a² + b² = কত?"; w = [s * s, s * s + 2 * p, s * s - p, v + 2]
    elif t == 1: v = (a - c) ** 2; q = f"a + b = {s} এবং ab = {p} হলে (a − b)² = কত?"; w = [s * s - 2 * p, s * s, s * s - p, v + 4]
    else: v = s * s; q = f"a² + b² = {a * a + c * c} এবং ab = {p} হলে (a + b)² = কত?"; w = [a * a + c * c, a * a + c * c - 2 * p, s, v + p]
    b.add(q, v, W(v, w), "(a + b)² = a² + 2ab + b² সূত্র ব্যবহার।", lv)
def j51_dp(b, lv):
    a, c = R.randint(2, 15), R.randint(1, 14)
    if a <= c: return
    d, p = a - c, a * c; t = R.randrange(2)
    if t == 0: v = a * a + c * c; q = f"a − b = {d} এবং ab = {p} হলে a² + b² = কত?"; w = [d * d, d * d - 2 * p if d * d - 2 * p > 0 else d * d + p, v + 2, d * d + p]; e = f"a² + b² = (a − b)² + 2ab = {d * d} + {2 * p}।"
    else: v = (a + c) ** 2; q = f"a − b = {d} এবং ab = {p} হলে (a + b)² = কত?"; w = [d * d + 2 * p, d * d, v - 4, d * d + p]; e = f"(a + b)² = (a − b)² + 4ab = {d * d} + {4 * p}।"
    b.add(q, v, W(v, w), e, lv)
def j51_recip(b, lv):
    k = R.randint(2, 12); t = R.randrange(2)
    if t == 0: v = k * k - 2; b.add(f"x + 1/x = {k} হলে x² + 1/x² = কত?", v, W(v, [k * k, k * k + 2, 2 * k, k * k - 1]), f"(x + 1/x)² − 2 = {k * k} − 2।", lv)
    else: v = k * k + 2; b.add(f"x − 1/x = {k} হলে x² + 1/x² = কত?", v, W(v, [k * k, k * k - 2, 2 * k, k * k + 1]), f"(x − 1/x)² + 2 = {k * k} + 2।", lv)
def j51_val(b, lv):
    a, c = R.randint(-9, 12), R.randint(-9, 12)
    if not a or not c or a == c: return
    t = R.randrange(2)
    if t == 0: v = (a + c) ** 2; b.add(f"a = {num(a)}, b = {num(c)} হলে a² + 2ab + b² এর মান কত?", v, W(v, [a * a + c * c, (a - c) ** 2, v + 2, abs(a + c)]), f"(a + b)² = ({num(a + c)})²।", lv)
    else: v = (a - c) ** 2; b.add(f"a = {num(a)}, b = {num(c)} হলে a² − 2ab + b² এর মান কত?", v, W(v, [a * a + c * c, (a + c) ** 2, v + 2, abs(a - c)]), f"(a − b)² = ({num(a - c)})²।", lv)
def j51_perf(b, lv):
    k, a = R.choice([1, 2, 3, 4]), R.randint(1, 9)
    m = 2 * k * a; c0 = a * a
    b.add(f"{k * k if k > 1 else ''}x² + {m}x + k রাশিটি পূর্ণবর্গ হলে k এর মান কত?", c0, W(c0, [a, 2 * a, c0 + 1, m]), f"({k if k > 1 else ''}x + {a})² = {k * k if k > 1 else ''}x² + {m}x + {c0}।", lv)
P51 = part('5.1', 150, fx51, [j51_sqc, j51_sqp, j51_diffsq, j51_xab], [j51_num, j51_sp, j51_val, j51_sqp, j51_dp], [j51_recip, j51_perf, j51_dp, j51_sp])

# ===================================================== 5.2 উৎপাদকে বিশ্লেষণ
fx52 = [
 ("কোনো রাশিকে দুই বা ততোধিক রাশির গুণফলরূপে প্রকাশ করাকে কী বলে?", "উৎপাদকে বিশ্লেষণ", ["সরলীকরণ", "গ.সা.গু. নির্ণয়", "বিস্তৃতি"], "", E),
 ("a² − b² এর উৎপাদক কোনগুলো?", "(a + b) ও (a − b)", ["(a − b) ও (a − b)", "(a + b) ও (a + b)", "a ও b"], "", E),
 ("a² + 2ab + b² এর উৎপাদকে বিশ্লেষিত রূপ কোনটি?", "(a + b)(a + b)", ["(a + b)(a − b)", "(a − b)(a − b)", "a(a + 2b)"], "", E),
]
def k52_common(b, lv):
    g = R.choice([2, 3, 4, 5, 6]); e = R.choice([(1, 0), (1, 1), (2, 0), (0, 1)])
    p, q = nz(-7, 7), nz(-7, 7)
    if math.gcd(p, q) != 1: return
    inner = padd(mono(p, 1, 0), mono(q, 0, 1)); m = mono(g, *e); full = pmul(m, inner)
    cc = f"{P(m)}({P(inner)})"
    b.add(f"{P(full)} এর উৎপাদকে বিশ্লেষিত রূপ কোনটি?", cc, W(cc, [f"{P(mono(g, *e))}({P(padd(mono(p, 1, 0), mono(-q, 0, 1)))})", f"{g}({P(pmul(mono(1, *e), inner))})" if e != (0, 0) else f"{P(m)}({P(inner)} + 1)", f"{P(mono(g * 2, *e))}({P(inner)})", f"{P(mono(g, e[0] + 1, e[1]))}({P(inner)})"]), "সাধারণ উৎপাদক বাইরে আনো।", lv)
def k52_dsq(b, lv):
    k, m = R.randint(1, 9), R.randint(1, 9)
    A, B = P(mono(k, 1, 0)), P(mono(m, 0, 1)); full = padd(mono(k * k, 2, 0), mono(-m * m, 0, 2))
    cc = f"({A} + {B})({A} − {B})"
    b.add(f"{P(full)} এর উৎপাদক কোনটি?", cc, W(cc, [f"({A} − {B})²", f"({A} + {B})²", f"({P(mono(k * k, 1, 0))} + {B})({A} − {B})", f"({A} + {P(mono(m * m, 0, 1))})({A} − {B})"]), "a² − b² = (a + b)(a − b)।", lv)
def k52_tri(b, lv):
    a, c = nz(-9, 9), nz(-9, 9)
    if a == c or a == -c: return
    full = pmul(xl(a), xl(c)); cc = f"{lf(a)}{lf(c)}" if a > c else f"{lf(c)}{lf(a)}"
    b.add(f"{P(full)} এর উৎপাদকে বিশ্লেষিত রূপ কোনটি?", cc, W(cc, [f"{lf(-a)}{lf(-c)}", f"{lf(a)}{lf(-c)}", f"{lf(-a)}{lf(c)}", f"{lf(a + c)}{lf(1)}" if a + c and a + c != 1 else f"{lf(a * c)}{lf(1)}"]), f"গুণফল {a * c} ও যোগফল {a + c} এমন দুটি সংখ্যা {a} ও {c}।", lv)
def k52_perf(b, lv):
    k, a = R.choice([1, 2, 3, 4, 5]), nz(-9, 9)
    p = padd(mono(k, 1, 0), lin([0, 0], a)); full = ppow(p, 2); cc = f"({P(p)})²"
    b.add(f"{P(full)} এর উৎপাদকে বিশ্লেষিত রূপ কোনটি?", cc, W(cc, [f"({P(padd(mono(k, 1, 0), lin([0, 0], -a)))})²", f"({P(p)})({P(padd(mono(k, 1, 0), lin([0, 0], -a)))})", f"({P(padd(mono(k * k, 1, 0), lin([0, 0], a)))})²" if k > 1 else f"({P(padd(mono(1, 1, 0), lin([0, 0], 2 * a)))})²", f"({P(padd(mono(k, 1, 0), lin([0, 0], a * a)))})²"]), "a² ± 2ab + b² = (a ± b)²।", lv)
def k52_which(b, lv):
    a, c = nz(-9, 9), nz(-9, 9)
    if a == c or a == -c: return
    full = pmul(xl(a), xl(c)); cc = lf(a)
    b.add(f"নিচের কোনটি {P(full)} এর একটি উৎপাদক?", cc, W(cc, [lf(-a), lf(-c), lf(a + c) if a + c else lf(a * c), lf(a * c) if a * c != a else lf(a + 1)]), f"{P(full)} = {lf(a)}{lf(c)}।", lv)
def k52_quad(b, lv):
    p, q = R.choice([2, 3, 5]), R.choice([1, 2, 3])
    a, c = nz(-7, 7), nz(-7, 7)
    f1, f2 = padd(mono(p, 1, 0), lin([0, 0], a)), padd(mono(q, 1, 0), lin([0, 0], c))
    if math.gcd(p, abs(a)) != 1 or math.gcd(q, abs(c)) != 1: return
    full = pmul(f1, f2); cc = f"({P(f1)})({P(f2)})"
    b.add(f"{P(full)} এর উৎপাদকে বিশ্লেষিত রূপ কোনটি?", cc, W(cc, [f"({P(padd(mono(p, 1, 0), lin([0, 0], -a)))})({P(padd(mono(q, 1, 0), lin([0, 0], -c)))})", f"({P(padd(mono(p, 1, 0), lin([0, 0], c)))})({P(padd(mono(q, 1, 0), lin([0, 0], a)))})", f"({P(padd(mono(p, 1, 0), lin([0, 0], -a)))})({P(f2)})", f"({P(f1)})({P(padd(mono(q, 1, 0), lin([0, 0], -c)))})"]), "মধ্যপদ বিভক্তি করে।", lv)
def k52_four(b, lv):
    k = R.choice([1, 2, 3]); a = R.randint(1, 4)
    if k == 1: full = padd(mono(1, 4, 0), lin([0, 0], -a ** 4)); cc = f"(x² + {a * a})(x + {a})(x − {a})" if a > 1 else "(x² + 1)(x + 1)(x − 1)"
    else: return
    w = [f"(x² − {a * a})²" if a > 1 else "(x² − 1)²", f"(x² + {a * a})²" if a > 1 else "(x² + 1)²", f"(x + {a})²(x − {a})²" if a > 1 else "(x + 1)²(x − 1)²", f"(x² + {a * a})(x² + {a * a})" if a > 1 else "(x² + 1)(x² + 1)"]
    b.add(f"{P(full)} এর উৎপাদকে বিশ্লেষিত রূপ কোনটি?", cc, W(cc, w), "দুবার a² − b² সূত্র।", lv)
def k52_dsqk(b, lv):
    g = R.choice([2, 3, 5, 7]); k, m = R.randint(1, 6), R.randint(1, 9)
    full = pmul(lin([0, 0], g), padd(mono(k * k, 2, 0), lin([0, 0], -m * m))); A = P(mono(k, 1, 0))
    cc = f"{g}({A} + {m})({A} − {m})"
    b.add(f"{P(full)} এর উৎপাদক কোনটি?", cc, W(cc, [f"({A} + {g * m})({A} − {m})", f"{g}({A} − {m})²", f"({P(mono(g * k, 1, 0))} + {m})({A} − {m})", f"{g}({A} + {m})²"]), "আগে সাধারণ উৎপাদক, পরে a² − b²।", lv)
P52 = part('5.2', 150, fx52, [k52_common, k52_dsq, k52_tri, k52_which], [k52_tri, k52_perf, k52_dsqk, k52_which, k52_common], [k52_quad, k52_four, k52_dsqk])

# ===================================================== 5.3 গ.সা.গু. ও 5.4 ল.সা.গু.
def fprod(fs):
    """fs: [(a, power)] → (x + a)ᵖ গুণফলের লেখা"""
    out = ''
    for a, k in fs: out += lf(a) + (sup(k) if k > 1 else '')
    return out
def fpoly(fs, c=1):
    p = {(0, 0): c}
    for a, k in fs:
        for _ in range(k): p = pmul(p, xl(a))
    return p
def lpx(n): return mono(1, 0, 0) if n == 0 else mono(1, n, 0)
fx53 = [
 ("দুই বা ততোধিক রাশির সাধারণ উৎপাদকগুলোর মধ্যে সর্বোচ্চ মাত্রার রাশিকে কী বলে?", "গ.সা.গু.", ["ল.সা.গু.", "ভাগফল", "গুণিতক"], "", E),
 ("দুটি রাশির গ.সা.গু. × ল.সা.গু. = কত?", "রাশি দুটির গুণফল", ["রাশি দুটির যোগফল", "রাশি দুটির বিয়োগফল", "রাশি দুটির ভাগফল"], "", M),
]
def l53_mono(b, lv):
    c1, c2 = R.randint(2, 30), R.randint(2, 30); e = [R.randint(1, 5) for _ in range(4)]
    g = math.gcd(c1, c2); r = mono(g, min(e[0], e[2]), min(e[1], e[3])); cc = P(r)
    b.add(f"{P(mono(c1, e[0], e[1]))} ও {P(mono(c2, e[2], e[3]))} এর গ.সা.গু. কত?", cc, W(cc, [P(mono(g, max(e[0], e[2]), max(e[1], e[3]))), P(mono(c1 * c2 // g, min(e[0], e[2]), min(e[1], e[3]))), P(mono(g, min(e[0], e[2]) + 1, min(e[1], e[3]))), P(mono(g * 2, min(e[0], e[2]), min(e[1], e[3])))]), "সহগের গ.সা.গু. ও প্রতিটি চলকের ক্ষুদ্রতম ঘাত।", lv)
def l53_mono3(b, lv):
    cs = [R.randint(2, 40) for _ in range(3)]; es = [(R.randint(1, 4), R.randint(1, 4)) for _ in range(3)]
    g = math.gcd(math.gcd(cs[0], cs[1]), cs[2]); r = mono(g, min(x for x, _ in es), min(y for _, y in es)); cc = P(r)
    b.add(f"{', '.join(P(mono(c, *e)) for c, e in zip(cs, es))} এর গ.সা.গু. কত?", cc, W(cc, [P(mono(g, max(x for x, _ in es), max(y for _, y in es))), P(mono(g + 1, min(x for x, _ in es), min(y for _, y in es))), P(mono(g, min(x for x, _ in es) + 1, min(y for _, y in es))), P(mono(g, min(x for x, _ in es), min(y for _, y in es) + 1))]), "", lv)
def l53_poly(b, lv):
    a, c, d = R.sample([v for v in range(-9, 10) if v], 3)
    p1, p2 = fpoly([(a, 1), (c, 1)]), fpoly([(a, 1), (d, 1)]); cc = lf(a)
    b.add(f"{P(p1)} ও {P(p2)} এর গ.সা.গু. কত?", cc, W(cc, [lf(c), lf(d), lf(-a), f"{lf(a)}{lf(c)}{lf(d)}"]), f"{P(p1)} = {lf(a)}{lf(c)}, {P(p2)} = {lf(a)}{lf(d)}।", lv)
def l53_dsq(b, lv):
    a, c = R.sample(range(1, 10), 2)
    p1 = fpoly([(a, 1), (-a, 1)]); p2 = fpoly([(a, 1), (c, 1)]); cc = lf(a)
    b.add(f"{P(p1)} ও {P(p2)} এর গ.সা.গু. কত?", cc, W(cc, [lf(-a), lf(c), f"{lf(a)}{lf(-a)}", lf(a + c)]), f"{P(p1)} = {lf(a)}{lf(-a)}।", lv)
def l53_three(b, lv):
    a, c, d, e = R.sample([v for v in range(-8, 9) if v], 4)
    ps = [fpoly([(a, 1), (c, 1)]), fpoly([(a, 1), (d, 1)]), fpoly([(a, 1), (e, 1)])]
    cc = lf(a)
    b.add(f"{P(ps[0])}, {P(ps[1])} ও {P(ps[2])} এর গ.সা.গু. কত?", cc, W(cc, [lf(c), lf(d), lf(e), "1"]), "তিনটিতেই সাধারণ উৎপাদক।", lv)
def l53_sq(b, lv):
    a, c = R.sample([v for v in range(-8, 9) if v], 2)
    p1 = fpoly([(a, 2)]); p2 = fpoly([(a, 1), (c, 1)]); cc = lf(a)
    b.add(f"{P(p1)} ও {P(p2)} এর গ.সা.গু. কত?", cc, W(cc, [f"{lf(a)}²", lf(c), f"{lf(a)}²{lf(c)}", lf(-a)]), f"{P(p1)} = {lf(a)}²।", lv)
P53 = part('5.3', 150, fx53, [l53_mono, l53_poly, l53_mono3], [l53_poly, l53_dsq, l53_sq, l53_mono3], [l53_three, l53_sq, l53_dsq])
fx54 = [
 ("দুই বা ততোধিক রাশির সাধারণ গুণিতকগুলোর মধ্যে সর্বনিম্ন মাত্রার রাশিকে কী বলে?", "ল.সা.গু.", ["গ.সা.গু.", "উৎপাদক", "ভাগশেষ"], "", E),
 ("দুটি রাশির গ.সা.গু. 1 হলে তাদের ল.সা.গু. কী?", "রাশি দুটির গুণফল", ["1", "রাশি দুটির যোগফল", "বড় রাশিটি"], "", M),
]
def m54_mono(b, lv):
    c1, c2 = R.randint(2, 20), R.randint(2, 20); e = [R.randint(1, 5) for _ in range(4)]
    l = c1 * c2 // math.gcd(c1, c2); r = mono(l, max(e[0], e[2]), max(e[1], e[3])); cc = P(r)
    b.add(f"{P(mono(c1, e[0], e[1]))} ও {P(mono(c2, e[2], e[3]))} এর ল.সা.গু. কত?", cc, W(cc, [P(mono(l, min(e[0], e[2]), min(e[1], e[3]))), P(mono(c1 * c2, max(e[0], e[2]), max(e[1], e[3]))) if c1 * c2 != l else P(mono(l * 2, max(e[0], e[2]), max(e[1], e[3]))), P(mono(math.gcd(c1, c2), max(e[0], e[2]), max(e[1], e[3]))) if math.gcd(c1, c2) != l else P(mono(l + 1, max(e[0], e[2]), max(e[1], e[3]))), P(mono(l, e[0] + e[2], e[1] + e[3]))]), "সহগের ল.সা.গু. ও প্রতিটি চলকের বৃহত্তম ঘাত।", lv)
def m54_mono3(b, lv):
    cs = [R.randint(2, 15) for _ in range(3)]; es = [(R.randint(1, 4), R.randint(0, 4)) for _ in range(3)]
    l = cs[0] * cs[1] // math.gcd(cs[0], cs[1]); l = l * cs[2] // math.gcd(l, cs[2])
    r = mono(l, max(x for x, _ in es), max(y for _, y in es)); cc = P(r)
    b.add(f"{', '.join(P(mono(c, *e)) for c, e in zip(cs, es))} এর ল.সা.গু. কত?", cc, W(cc, [P(mono(l, min(x for x, _ in es), min(y for _, y in es))), P(mono(l * 2, max(x for x, _ in es), max(y for _, y in es))), P(mono(l, max(x for x, _ in es) + 1, max(y for _, y in es))), P(mono(cs[0] * cs[1] * cs[2], max(x for x, _ in es), max(y for _, y in es))) if cs[0] * cs[1] * cs[2] != l else P(mono(l + 1, max(x for x, _ in es), max(y for _, y in es)))]), "", lv)
def m54_poly(b, lv):
    a, c, d = R.sample([v for v in range(-9, 10) if v], 3)
    p1, p2 = fpoly([(a, 1), (c, 1)]), fpoly([(a, 1), (d, 1)])
    order = sorted([a, c, d], reverse=True); cc = ''.join(lf(v) for v in order)
    b.add(f"{P(p1)} ও {P(p2)} এর ল.সা.গু. কত?", cc, W(cc, [lf(a), f"{lf(a)}²{lf(c)}{lf(d)}", f"{lf(c)}{lf(d)}", ''.join(lf(-v) for v in order)]), "সব উৎপাদক, সাধারণটি একবার।", lv)
def m54_dsq(b, lv):
    a, c = R.sample(range(1, 10), 2)
    p1 = fpoly([(a, 1), (-a, 1)]); p2 = fpoly([(a, 1), (c, 1)])
    order = sorted([a, -a, c], reverse=True); cc = ''.join(lf(v) for v in order)
    b.add(f"{P(p1)} ও {P(p2)} এর ল.সা.গু. কত?", cc, W(cc, [lf(a), f"{lf(a)}²{lf(-a)}{lf(c)}", f"{lf(-a)}{lf(c)}", f"{lf(a)}{lf(c)}"]), f"{P(p1)} = {lf(a)}{lf(-a)}।", lv)
def m54_sq(b, lv):
    a, c = R.sample([v for v in range(-8, 9) if v], 2)
    p1 = fpoly([(a, 2)]); p2 = fpoly([(a, 1), (c, 1)]); cc = f"{lf(a)}²{lf(c)}"
    b.add(f"{P(p1)} ও {P(p2)} এর ল.সা.গু. কত?", cc, W(cc, [f"{lf(a)}{lf(c)}", lf(a), f"{lf(a)}³{lf(c)}", f"{lf(a)}²{lf(-c)}"]), "প্রত্যেক উৎপাদকের বৃহত্তম ঘাত।", lv)
def m54_coef(b, lv):
    g1, g2 = R.randint(2, 9), R.randint(2, 9); a = nz(-9, 9)
    l = g1 * g2 // math.gcd(g1, g2)
    p1 = pmul(lin([0, 0], g1), xl(a)); p2 = pmul(lin([0, 0], g2), fpoly([(a, 2)]))
    cc = f"{l}{lf(a)}²"
    b.add(f"{P(p1)} ও {P(p2)} এর ল.সা.গু. কত?", cc, W(cc, [f"{g1 * g2}{lf(a)}²" if g1 * g2 != l else f"{l * 2}{lf(a)}²", f"{l}{lf(a)}", f"{math.gcd(g1, g2)}{lf(a)}" if math.gcd(g1, g2) > 1 else f"{lf(a)}", f"{l}{lf(a)}³"]), "সহগের ল.সা.গু. ও উৎপাদকের বৃহত্তম ঘাত।", lv)
P54 = part('5.4', 150, fx54, [m54_mono, m54_poly, m54_mono3], [m54_poly, m54_dsq, m54_sq, m54_coef], [m54_sq, m54_coef, m54_dsq])
save('v5', P51 + P52 + P53 + P54)

# ===================================================== 6.1 লঘিষ্ঠকরণ ও সাধারণ হর
fx61 = [
 ("লব ও হরে বীজগণিতীয় রাশি থাকলে ভগ্নাংশটিকে কী বলে?", "বীজগণিতীয় ভগ্নাংশ", ["সাধারণ ভগ্নাংশ", "দশমিক ভগ্নাংশ", "মিশ্র ভগ্নাংশ"], "", E),
 ("লব ও হরের মধ্যে 1 ছাড়া কোনো সাধারণ উৎপাদক না থাকলে ভগ্নাংশটিকে কী বলে?", "লঘিষ্ঠ আকারের ভগ্নাংশ", ["অপ্রকৃত ভগ্নাংশ", "সমহরবিশিষ্ট ভগ্নাংশ", "যৌগিক ভগ্নাংশ"], "", E),
 ("ভগ্নাংশের লব ও হরকে একই রাশি (শূন্য ছাড়া) দিয়ে গুণ করলে ভগ্নাংশের মানের কী হয়?", "অপরিবর্তিত থাকে", ["দ্বিগুণ হয়", "শূন্য হয়", "অর্ধেক হয়"], "", E),
 ("ভগ্নাংশগুলোকে সমহরবিশিষ্ট করতে সাধারণ হর হিসেবে কী নেওয়া হয়?", "হরগুলোর ল.সা.গু.", ["হরগুলোর গ.সা.গু.", "লবগুলোর ল.সা.গু.", "হরগুলোর যোগফল"], "", M),
]
def fr_txt(n, d): return f"{n}/{d}" if d not in ('1', '') else n
def wrap(s): return s if all(ch not in s for ch in ' +−') else f"({s})"
def n61_mono(b, lv):
    p, q = R.randint(1, 9), R.randint(1, 9); g = R.randint(2, 9)
    if math.gcd(p, q) != 1 or p == q: return
    e = [R.randint(0, 4) for _ in range(4)]
    if e[0] == e[2] and e[1] == e[3]: return
    num_ = mono(p * g, e[0], e[1]); den = mono(q * g, e[2], e[3])
    ax, ay = e[0] - min(e[0], e[2]), e[1] - min(e[1], e[3]); bx, by = e[2] - min(e[0], e[2]), e[3] - min(e[1], e[3])
    top, bot = P(mono(p, ax, ay)), P(mono(q, bx, by))
    cc = top if bot == '1' else f"{top}/{wrap(bot)}"
    alt = f"{P(mono(q, ax, ay))}/{wrap(P(mono(p, bx, by)))}" if P(mono(p, bx, by)) != '1' else P(mono(q, ax, ay))
    b.add(f"{P(num_)}/{P(den)} এর লঘিষ্ঠ রূপ কোনটি?", cc, W(cc, [alt, f"{P(mono(p * g, ax, ay))}/{wrap(P(mono(q, bx, by)))}", f"{P(mono(p, bx, by))}/{wrap(P(mono(q, ax, ay)))}" if (ax, ay) != (0, 0) else f"{p}/{wrap(P(mono(q, bx + 1, by)))}", f"{P(mono(p, ax + 1, ay))}/{wrap(bot)}"]), "সাধারণ উৎপাদক দিয়ে লব ও হর ভাগ।", lv)
def n61_fac(b, lv):
    a, c, d = R.sample([v for v in range(-8, 9) if v], 3)
    nm, dn = fpoly([(a, 1), (c, 1)]), fpoly([(a, 1), (d, 1)])
    cc = f"{lf(c)}/{lf(d)}"
    b.add(f"({P(nm)})/({P(dn)}) এর লঘিষ্ঠ রূপ কোনটি?", cc, W(cc, [f"{lf(d)}/{lf(c)}", f"{lf(-c)}/{lf(-d)}", f"{lf(a)}/{lf(d)}", f"{lf(c)}/{lf(a)}"]), f"লব = {lf(a)}{lf(c)}, হর = {lf(a)}{lf(d)}।", lv)
def n61_dsq(b, lv):
    a = R.randint(1, 9); c = nz(-9, 9)
    if c in (a, -a): return
    nm = fpoly([(a, 1), (-a, 1)]); dn = fpoly([(a, 1), (c, 1)])
    cc = f"{lf(-a)}/{lf(c)}"
    b.add(f"({P(nm)})/({P(dn)}) এর লঘিষ্ঠ রূপ কোনটি?", cc, W(cc, [f"{lf(a)}/{lf(c)}", f"{lf(-a)}/{lf(-c)}", f"{lf(c)}/{lf(-a)}", f"{lf(-a)}/{lf(a)}"]), f"{P(nm)} = {lf(a)}{lf(-a)}।", lv)
def n61_den(b, lv):
    c1, c2 = R.randint(2, 12), R.randint(2, 12); e1, e2 = (R.randint(1, 3), R.randint(0, 3)), (R.randint(0, 3), R.randint(1, 3))
    l = c1 * c2 // math.gcd(c1, c2); r = P(mono(l, max(e1[0], e2[0]), max(e1[1], e2[1])))
    b.add(f"a/{P(mono(c1, *e1))} ও b/{P(mono(c2, *e2))} কে সমহরবিশিষ্ট করলে সাধারণ হর কত হবে?", r, W(r, [P(mono(c1 * c2, e1[0] + e2[0], e1[1] + e2[1])) if c1 * c2 != l or e1[0] + e2[0] != max(e1[0], e2[0]) or e1[1] + e2[1] != max(e1[1], e2[1]) else P(mono(l * 2, max(e1[0], e2[0]), max(e1[1], e2[1]))), P(mono(math.gcd(c1, c2), min(e1[0], e2[0]), min(e1[1], e2[1]))), P(mono(l, min(e1[0], e2[0]), min(e1[1], e2[1]))), P(mono(l + 1, max(e1[0], e2[0]), max(e1[1], e2[1])))]), "হরগুলোর ল.সা.গু.।", lv)
def n61_pden(b, lv):
    a, c, d = R.sample([v for v in range(-8, 9) if v], 3)
    h1, h2 = fpoly([(a, 1), (c, 1)]), fpoly([(a, 1), (d, 1)])
    order = sorted([a, c, d], reverse=True); cc = ''.join(lf(v) for v in order)
    b.add(f"1/({P(h1)}) ও 1/({P(h2)}) এর সাধারণ হর কোনটি?", cc, W(cc, [lf(a), f"{lf(a)}²{lf(c)}{lf(d)}", f"{lf(c)}{lf(d)}", ''.join(lf(-v) for v in order)]), "হরগুলোর ল.সা.গু.।", lv)
def n61_mult(b, lv):
    p, q = R.randint(1, 9), R.randint(2, 9); k = R.randint(2, 6); v = R.choice('abxy')
    if math.gcd(p, q) != 1: return
    cc = cf(p * k, v)
    b.add(f"{p}/{q} = ?/{q * k}{v} হলে ? এর স্থানে কী বসবে?", cc, W(cc, [cf(p, v), f"{p * k}", f"{q * k}{v}", cf(p + k, v)]), f"হরকে {k}{v} দিয়ে গুণ করা হয়েছে, তাই লবকেও।", lv)
P61 = part('6.1', 150, fx61, [n61_mono, n61_den, n61_mult], [n61_fac, n61_dsq, n61_pden, n61_mono], [n61_fac, n61_dsq, n61_pden])

# ===================================================== 6.2 যোগ, বিয়োগ, গুণ, ভাগ
fx62 = [
 ("সমহরবিশিষ্ট ভগ্নাংশ যোগ করতে কী করতে হয়?", "লবগুলো যোগ করে হর একই রাখতে হয়", ["হরগুলো যোগ করতে হয়", "লব ও হর উভয়ই যোগ করতে হয়", "লবগুলো গুণ করতে হয়"], "", E),
 ("দুটি ভগ্নাংশ গুণ করতে কী করতে হয়?", "লবকে লব দিয়ে এবং হরকে হর দিয়ে গুণ", ["আড়াআড়ি গুণ", "লব যোগ ও হর গুণ", "হর একই রেখে লব গুণ"], "", E),
 ("a/b ÷ c/d = কত?", "ad/bc", ["ac/bd", "bc/ad", "ab/cd"], "ভাজককে উল্টে গুণ।", E),
]
def o62_same(b, lv):
    p, q = nz(-9, 9), nz(-9, 9); v = R.choice('xyab'); k = R.randint(2, 9); s = R.choice(['+', '−'])
    r = p + q if s == '+' else p - q
    if r == 0: return
    cc = f"{num(r)}/{k}{v}"
    b.add(f"{num(p)}/{k}{v} {s} {q if q > 0 else '(' + num(q) + ')'}/{k}{v} = কত?", cc, W(cc, [f"{num(p - q if s == '+' else p + q)}/{k}{v}", f"{num(r)}/{2 * k}{v}", f"{num(r)}/{k}{v}²", f"{num(-r)}/{k}{v}"]), "হর একই, লব যোগ/বিয়োগ।", lv)
def o62_diff(b, lv):
    a, c = R.randint(1, 9), R.randint(1, 9); s = R.choice(['+', '−'])
    top = f"{a}y {s} {c}x" if s == '+' else f"{a}y − {c}x"
    cc = f"({top.replace('1y', 'y').replace(' 1x', ' x')})/xy"
    b.add(f"{a}/x {s} {c}/y = কত?", cc, W(cc, [f"{a + c if s == '+' else a - c}/(x {s} y)", f"({a}x {s} {c}y)/xy".replace(' 1y', ' y').replace('(1x', '(x'), f"{a * c}/xy", f"({top.replace('1y', 'y').replace(' 1x', ' x')})/(x + y)"]), "সাধারণ হর xy।", lv)
def o62_pm(b, lv):
    a = R.randint(1, 9); t = R.randrange(2)
    if t == 0: cc = f"2x/(x² − {a * a})"; q = f"1/(x + {a}) + 1/(x − {a}) = কত?"; w = [f"2/(x² − {a * a})", f"{2 * a}/(x² − {a * a})", f"2x/(x² + {a * a})", f"x/(x² − {a * a})"]
    else: cc = f"{2 * a}/(x² − {a * a})"; q = f"1/(x − {a}) − 1/(x + {a}) = কত?"; w = [f"2x/(x² − {a * a})", f"−{2 * a}/(x² − {a * a})", f"{2 * a}/(x² + {a * a})", f"2/(x² − {a * a})"]
    b.add(q, cc, W(cc, w), f"সাধারণ হর (x + {a})(x − {a}) = x² − {a * a}।", lv)
def o62_mul(b, lv):
    p, q, r, s_ = R.randint(1, 9), R.randint(2, 9), R.randint(1, 9), R.randint(2, 9)
    if math.gcd(p, q) != 1 or math.gcd(r, s_) != 1: return
    def fx(n, d, top, bot):
        g = math.gcd(n, d); n, d = n // g, d // g
        t = cf(n, top) if top else str(n)
        return t if d == 1 and not bot else f"{t}/{cf(d, bot) if bot else d}"
    cc = fx(p * r, q * s_, 'x', 'y')
    b.add(f"({cf(p, 'x')}/{q}y) × ({r}/{s_}) = কত?", cc, W(cc, [fx(p * s_, q * r, 'x', 'y'), fx(p * r, q * s_, '', 'y'), fx(p * r, q * s_, 'x', ''), fx(p + r, q + s_, 'x', 'y'), fx(q * s_, p * r, 'x', 'y')]), "লব × লব, হর × হর, তারপর লঘিষ্ঠ।", lv)
def o62_div(b, lv):
    a, c = R.sample([v for v in range(-8, 9) if v], 2)
    cc = f"{lf(a)}/{lf(c)}"
    num1 = P(fpoly([(a, 1), (-a, 1)]) if a > 0 else fpoly([(a, 1), (-a, 1)]))
    b.add(f"({num1})/{lf(c)} ÷ {lf(-a)} = কত?", cc, W(cc, [f"{lf(-a)}/{lf(c)}", f"{lf(c)}/{lf(a)}", f"({num1})/{lf(c)}{lf(-a)}", f"{lf(a)}{lf(-a)}/{lf(c)}"]), f"{num1} = {lf(a)}{lf(-a)}; ভাজক উল্টে গুণ।", lv)
def o62_x1(b, lv):
    a, c = R.sample(range(1, 10), 2)
    cc = f"{c - a}/{lf(a)}{lf(c)}" if c > a else f"−{a - c}/{lf(a)}{lf(c)}"
    b.add(f"1/(x + {a}) − 1/(x + {c}) = কত?", cc, W(cc, [f"{c + a}/{lf(a)}{lf(c)}", f"(2x + {a + c})/{lf(a)}{lf(c)}", f"{a - c if a > c else '−' + str(c - a)}/{lf(a)}{lf(c)}", f"1/{lf(c - a) if c != a else lf(1)}"]), f"(x + {c} − x − {a}) / {lf(a)}{lf(c)}।", lv)
def o62_val(b, lv):
    a = R.randint(1, 6); x = R.choice([v for v in range(-9, 10) if v not in (a, -a, 0)])
    v = F(2 * x, x * x - a * a)
    b.add(f"x = {num(x)} হলে 1/(x + {a}) + 1/(x − {a}) এর মান কত?", num(v) if v.denominator == 1 else (('−' if v < 0 else '') + fr(abs(v))), W((num(v) if v.denominator == 1 else (('−' if v < 0 else '') + fr(abs(v)))), [fr(abs(v) + 1), ('−' if v > 0 else '') + fr(abs(v)), fr(F(2, abs(x * x - a * a))), fr(abs(v) * 2)]), f"রাশিটি = 2x/(x² − {a * a})।", lv)
P62 = part('6.2', 150, fx62, [o62_same, o62_diff, o62_mul], [o62_pm, o62_x1, o62_mul, o62_div, o62_diff], [o62_val, o62_div, o62_x1])
save('v6', P61 + P62)

# ===================================================== 7 সরল সমীকরণ
fx71 = [
 ("যে সমীকরণে অজ্ঞাত রাশির সর্বোচ্চ ঘাত 1, তাকে কী বলে?", "সরল সমীকরণ", ["দ্বিঘাত সমীকরণ", "অভেদ", "অসমতা"], "", E),
 ("সমীকরণের উভয় পক্ষে একই সংখ্যা যোগ করলে সমীকরণের কী হয়?", "সমীকরণ অপরিবর্তিত থাকে", ["সমীকরণ বদলে যায়", "সমাধান দ্বিগুণ হয়", "সমাধান থাকে না"], "", E),
 ("সমীকরণে অজ্ঞাত রাশির যে মান সমীকরণকে সিদ্ধ করে তাকে কী বলে?", "সমাধান বা মূল", ["সহগ", "ধ্রুবক", "চলক"], "", E),
 ("একচলকবিশিষ্ট সরল সমীকরণের কয়টি সমাধান থাকে?", "1টি", ["2টি", "3টি", "অসংখ্য"], "", E),
 ("পক্ষান্তর করলে পদের চিহ্নের কী হয়?", "পরিবর্তিত হয়", ["অপরিবর্তিত থাকে", "সব (+) হয়", "সব (−) হয়"], "", E),
]
def sgn(v): return f"+ {v}" if v > 0 else f"− {-v}"
def p71_ab(b, lv):
    a, x, c = R.randint(2, 12), nz(-15, 15), nz(-30, 30); rhs = a * x + c
    b.add(f"{a}x {sgn(c)} = {rhs} হলে x = কত?", num(x), W(num(x), [num(-x), num(x + 1), num(F(rhs + c, a)) if (rhs + c) % a == 0 else num(x + 2), num(rhs - c)]), f"{a}x = {rhs - c} ⇒ x = {num(x)}।", lv)
def p71_both(b, lv):
    a, c = R.sample(range(2, 12), 2); x = nz(-12, 12); d = nz(-20, 20); e = (a - c) * x + d
    b.add(f"{a}x {sgn(d)} = {c}x {sgn(e)} হলে x = কত?", num(x), W(num(x), [num(-x), num(x + 1), num(x - 1), num(e - d)]), f"({a} − {c})x = {e} − ({num(d)}) ⇒ x = {num(x)}।", lv)
def p71_br(b, lv):
    a, c = R.randint(2, 9), nz(-9, 9); x = nz(-12, 12); rhs = a * (x + c)
    b.add(f"{a}(x {sgn(c)}) = {rhs} হলে x = কত?", num(x), W(num(x), [num(x + 2 * c) if c else num(x + 1), num(-x), num(F(rhs, a)), num(x + 1)]), f"x {sgn(c)} = {num(x + c)}।", lv)
def p71_check(b, lv):
    a, x, c = R.randint(2, 9), nz(-9, 9), nz(-20, 20); rhs = a * x + c
    w = []
    for d in (1, -1, 2, -2, 3):
        if x + d != x: w.append(num(x + d))
    b.add(f"নিচের কোনটি {a}x {sgn(c)} = {rhs} সমীকরণের সমাধান?", num(x), W(num(x), w), f"{a} × ({num(x)}) {sgn(c)} = {rhs}।", lv)
def p71_br2(b, lv):
    a, c, d, e = R.randint(2, 6), nz(-6, 6), R.randint(2, 6), nz(-6, 6); x = nz(-9, 9)
    if a == d: return
    k = a * (x + c) - d * (x + e)
    b.add(f"{a}(x {sgn(c)}) − {d}(x {sgn(e)}) = {k} হলে x = কত?", num(x), W(num(x), [num(-x), num(x + 1), num(x - 2), num(k)]), "বন্ধনী তুলে সদৃশ পদ একত্র।", lv)
def p71_val(b, lv):
    a, x, c = R.randint(2, 9), nz(-9, 9), nz(-20, 20); rhs = a * x + c; m, n = R.randint(2, 5), nz(-9, 9)
    v = m * x + n
    b.add(f"{a}x {sgn(c)} = {rhs} হলে {m}x {sgn(n)} এর মান কত?", num(v), W(num(v), [num(x), num(v + m), num(-v) if v else '1', num(m * x - n)]), f"x = {num(x)}।", lv)
P71 = part('7.1', 150, fx71, [p71_ab, p71_check, p71_br], [p71_both, p71_br, p71_ab, p71_val], [p71_br2, p71_val])

fx72 = [
 ("ভগ্নাংশযুক্ত সমীকরণ সমাধানের সুবিধার জন্য প্রথমে কী করা হয়?", "হরগুলোর ল.সা.গু. দিয়ে উভয় পক্ষকে গুণ", ["লবগুলো যোগ", "হরগুলো বাদ দেওয়া", "উভয় পক্ষকে শূন্য দিয়ে গুণ"], "", E),
 ("x/a = b হলে x = কত?", "ab", ["a/b", "b/a", "a + b"], "", E),
]
def q72_xa(b, lv):
    a, c = R.sample(range(2, 10), 2); x = math.lcm(a, c) * nz(-5, 5); r = F(x, a) + F(x, c)
    if r.denominator != 1: return
    b.add(f"x/{a} + x/{c} = {num(r)} হলে x = কত?", num(x), W(num(x), [num(-x), num(x // 2) if x % 2 == 0 else num(x + 1), num(r * a), num(x + math.lcm(a, c))]), f"উভয় পক্ষকে {math.lcm(a, c)} দিয়ে গুণ।", lv)
def q72_xd(b, lv):
    a, c = R.sample(range(2, 10), 2); x = math.lcm(a, c) * nz(-5, 5); r = F(x, a) - F(x, c)
    if r == 0 or r.denominator != 1: return
    b.add(f"x/{a} − x/{c} = {num(r)} হলে x = কত?", num(x), W(num(x), [num(-x), num(r * a * c), num(x + math.lcm(a, c)), num(r)]), f"উভয় পক্ষকে {math.lcm(a, c)} দিয়ে গুণ।", lv)
def q72_frac(b, lv):
    a, c = R.randint(2, 9), R.randint(2, 9); p, q = nz(-9, 9), nz(-9, 9)
    if a == c: return
    # (x + p)/a = (x + q)/c ⇒ c(x+p) = a(x+q) ⇒ x = (aq - cp)/(c - a)
    xv = F(a * q - c * p, c - a)
    if xv.denominator != 1: return
    b.add(f"(x {sgn(p)})/{a} = (x {sgn(q)})/{c} হলে x = কত?", num(xv), W(num(xv), [num(-xv) if xv else '1', num(xv + 1), num(F(c * p - a * q, c - a) + 1), num(q - p)]), f"{c}(x {sgn(p)}) = {a}(x {sgn(q)})।", lv)
def q72_one(b, lv):
    a = R.randint(2, 9); k = nz(-9, 9); x = a * k + R.randint(-5, 5); c = nz(-9, 9)
    r = F(x + c, a)
    if r.denominator != 1: return
    b.add(f"(x {sgn(c)})/{a} = {num(r)} হলে x = কত?", num(x), W(num(x), [num(r * a + c), num(x + 1), num(-x), num(r)]), f"x {sgn(c)} = {num(r * a)}।", lv)
def q72_mix(b, lv):
    a, c = R.sample(range(2, 7), 2); d = R.randint(2, 7); x = math.lcm(a, c) * R.randint(1, 4)
    r = F(x, a) + F(x, c) - d
    if r.denominator != 1: return
    b.add(f"x/{a} + x/{c} − {d} = {num(r)} হলে x = কত?", num(x), W(num(x), [num(x + math.lcm(a, c)), num(-x), num(x - math.lcm(a, c)) if x != math.lcm(a, c) else num(2 * x), num(r + d)]), "", lv)
def q72_dec(b, lv):
    a = R.choice([F(1, 2), F(1, 5), F(3, 10), F(1, 4), F(3, 4), F(2, 5)]); x = R.randint(2, 30) * a.denominator; c = R.randint(1, 20)
    rhs = a * x + c
    b.add(f"{D(a)}x + {c} = {D(rhs)} হলে x = কত?", x, W(x, [D(rhs - c), x + a.denominator, D(x * a), x * 2]), f"{D(a)}x = {D(rhs - c)}।", lv)
P72 = part('7.2', 150, fx72, [q72_one, q72_xa, q72_dec], [q72_xa, q72_xd, q72_frac, q72_one], [q72_mix, q72_frac])

fx73 = [
 ("কোনো সংখ্যার তিনগুণ থেকে 5 বিয়োগ করলে 10 হয়। সমীকরণটি কোনটি?", "3x − 5 = 10", ["5 − 3x = 10", "3(x − 5) = 10", "x/3 − 5 = 10"], "", E),
 ("ক্রমিক তিনটি পূর্ণসংখ্যার প্রথমটি x হলে তৃতীয়টি কত?", "x + 2", ["x + 1", "x + 3", "2x"], "", E),
 ("ক্রমিক দুটি জোড় সংখ্যার ছোটটি x হলে বড়টি কত?", "x + 2", ["x + 1", "2x", "x + 4"], "", E),
]
def r73_sum(b, lv):
    x = R.randint(5, 80); k = R.randint(2, 5); c = R.randint(1, 30)
    b.add(f"কোনো সংখ্যার {k} গুণের সাথে {c} যোগ করলে {k * x + c} হয়। সংখ্যাটি কত?", x, W(x, [x + 1, k * x, x - 1, (k * x + c) // k if (k * x + c) // k != x else x + 2]), f"{k}x + {c} = {k * x + c}।", lv)
def r73_cons(b, lv):
    x = R.randint(5, 200); n = R.choice([2, 3, 4]); s = sum(x + i for i in range(n)); t = R.randrange(2)
    if t == 0: b.add(f"ক্রমিক {n}টি স্বাভাবিক সংখ্যার যোগফল {s}। সবচেয়ে ছোট সংখ্যাটি কত?", x, W(x, [x + 1, x - 1, s // n, x + n - 1]), f"x + (x + 1) + … = {s}।", lv)
    else: b.add(f"ক্রমিক {n}টি স্বাভাবিক সংখ্যার যোগফল {s}। সবচেয়ে বড় সংখ্যাটি কত?", x + n - 1, W(x + n - 1, [x, x + n, s // n if s // n != x + n - 1 else x + n + 1, x + 1]), "", lv)
def r73_even(b, lv):
    x = 2 * R.randint(3, 100); n = R.choice([2, 3]); s = sum(x + 2 * i for i in range(n))
    b.add(f"ক্রমিক {n}টি জোড় সংখ্যার যোগফল {s}। ক্ষুদ্রতম সংখ্যাটি কত?", x, W(x, [x + 2, x - 2, s // n, x + 1]), f"x + (x + 2){' + (x + 4)' if n == 3 else ''} = {s}।", lv)
def r73_age(b, lv):
    s = R.randint(5, 20); k = R.randint(2, 5); f = k * s; t = R.randrange(2)
    if t == 0: b.add(f"পিতার বয়স পুত্রের বয়সের {k} গুণ। তাদের বয়সের সমষ্টি {f + s} বছর। পুত্রের বয়স কত বছর?", s, W(s, [f, s + 2, (f + s) // 2, s - 1]), f"x + {k}x = {f + s}।", lv)
    else:
        y = R.randint(2, 10); f2, s2 = f + y, s + y
        if f2 % s2: return
        m = f2 // s2
        b.add(f"পিতার বয়স পুত্রের বয়সের {k} গুণ। {y} বছর পর পিতার বয়স পুত্রের বয়সের {m} গুণ হবে। পুত্রের বর্তমান বয়স কত বছর?", s, W(s, [s + y, f, s - 1, s + 1]), f"{k}x + {y} = {m}(x + {y})।", lv)
def r73_rect(b, lv):
    w = R.randint(3, 40); d = R.randint(1, 20); l = w + d; p = 2 * (l + w)
    b.add(f"একটি আয়তক্ষেত্রের দৈর্ঘ্য প্রস্থ অপেক্ষা {d} মিটার বেশি এবং পরিসীমা {p} মিটার। প্রস্থ কত মিটার?", w, W(w, [l, p // 4, w + 1, w - 1 if w > 1 else w + 2]), f"2(x + {d} + x) = {p}।", lv)
def r73_money(b, lv):
    x = R.randint(20, 500); d = R.randint(5, 200); t = x * 2 + d
    b.add(f"রনি ও রুমার টাকার সমষ্টি {t} টাকা। রনির টাকা রুমার চেয়ে {d} টাকা বেশি। রুমার কাছে কত টাকা আছে?", x, W(x, [x + d, t // 2, x - d if x > d else x + 2 * d, x + 1]), f"x + (x + {d}) = {t}।", lv)
def r73_coins(b, lv):
    n5, n2 = R.randint(2, 30), R.randint(2, 30); tot = n5 * 5 + n2 * 2; cnt = n5 + n2
    b.add(f"একটি থলিতে 5 টাকা ও 2 টাকার মোট {cnt}টি মুদ্রা আছে, যাদের মোট মূল্য {tot} টাকা। 5 টাকার মুদ্রা কয়টি?", n5, W(n5, [n2, n5 + 1, cnt // 2 if cnt // 2 != n5 else n5 + 2, n5 - 1]), f"5x + 2({cnt} − x) = {tot}।", lv)
def r73_frac(b, lv):
    p, q = R.randint(1, 5), R.randint(2, 9); k = R.randint(2, 20); x = q * k; c = R.randint(1, 30)
    if p >= q or math.gcd(p, q) != 1: return
    b.add(f"কোনো সংখ্যার {p}/{q} অংশের সাথে {c} যোগ করলে {p * k + c} হয়। সংখ্যাটি কত?", x, W(x, [p * k, x + q, (p * k + c) * q // p if (p * k + c) * q % p == 0 and (p * k + c) * q // p != x else x + 2 * q, x - q]), f"({p}/{q})x + {c} = {p * k + c}।", lv)
def r73_digit(b, lv):
    t, u = R.randint(1, 8), R.randint(1, 9)
    if t >= u: return
    n = 10 * t + u; d = 9 * (u - t)
    b.add(f"দুই অঙ্কের একটি সংখ্যার অঙ্কদ্বয়ের যোগফল {t + u}। অঙ্কদ্বয় স্থান বিনিময় করলে নতুন সংখ্যাটি মূল সংখ্যা থেকে {d} বেশি হয়। মূল সংখ্যাটি কত?", n, W(n, [10 * u + t, n + 9, n - 9 if n > 18 else n + 18, 10 * (t + 1) + u - 1 if t + 1 < u else n + 1]), "দশক অঙ্ক x হলে একক অঙ্ক যোগফল − x।", lv)
P73 = part('7.3', 150, fx73, [r73_sum, r73_cons, r73_money], [r73_even, r73_age, r73_rect, r73_frac, r73_coins], [r73_digit, r73_age, r73_coins])
save('v7', P71 + P72 + P73)

# ===================================================== 8 সমান্তরাল সরলরেখা (250)
fx8 = [
 ("একই সমতলে অবস্থিত যে দুটি সরলরেখা কখনো পরস্পর ছেদ করে না, তাদের কী বলে?", "সমান্তরাল সরলরেখা", ["ছেদক রেখা", "লম্ব রেখা", "তির্যক রেখা"], "", E),
 ("দুটি সরলরেখাকে অপর একটি সরলরেখা ছেদ করলে তৃতীয় রেখাটিকে কী বলে?", "ছেদক", ["সমান্তরাল", "লম্ব", "কর্ণ"], "", E),
 ("দুটি সমান্তরাল সরলরেখাকে একটি ছেদক ছেদ করলে কয়টি কোণ উৎপন্ন হয়?", "8টি", ["4টি", "6টি", "2টি"], "", E),
 ("দুটি সমান্তরাল সরলরেখাকে একটি ছেদক ছেদ করলে একান্তর কোণগুলো কেমন হয়?", "পরস্পর সমান", ["সম্পূরক", "পূরক", "অসমান"], "", E),
 ("দুটি সমান্তরাল সরলরেখাকে একটি ছেদক ছেদ করলে অনুরূপ কোণগুলো কেমন হয়?", "পরস্পর সমান", ["সম্পূরক", "পূরক", "সমকোণ"], "", E),
 ("দুটি সমান্তরাল সরলরেখাকে একটি ছেদক ছেদ করলে ছেদকের একই পাশের অন্তঃস্থ কোণদ্বয়ের সমষ্টি কত?", "180°", ["90°", "360°", "120°"], "", E),
 ("দুটি সরলরেখা পরস্পরকে ছেদ করলে বিপ্রতীপ কোণগুলো কেমন হয়?", "পরস্পর সমান", ["সম্পূরক", "পূরক", "অসমান"], "", E),
 ("সরল কোণের পরিমাণ কত?", "180°", ["90°", "360°", "270°"], "", E),
 ("দুটি সমান্তরাল রেখার মধ্যবর্তী লম্ব দূরত্ব সব জায়গায় কেমন?", "সমান", ["ক্রমশ বাড়ে", "ক্রমশ কমে", "শূন্য"], "", E),
 ("দুটি কোণের সমষ্টি 180° হলে কোণ দুটিকে কী বলে?", "সম্পূরক কোণ", ["পূরক কোণ", "বিপ্রতীপ কোণ", "সন্নিহিত কোণ"], "", E),
 ("দুটি কোণের সমষ্টি 90° হলে কোণ দুটিকে কী বলে?", "পূরক কোণ", ["সম্পূরক কোণ", "বিপ্রতীপ কোণ", "সরল কোণ"], "", E),
 ("দুটি সরলরেখাকে একটি ছেদক ছেদ করলে যদি একান্তর কোণদ্বয় সমান হয়, তবে রেখা দুটি কেমন?", "সমান্তরাল", ["লম্ব", "পরস্পরছেদী", "সমাপতিত"], "", M),
 ("দুটি সরলরেখাকে একটি ছেদক ছেদ করলে যদি ছেদকের একই পাশের অন্তঃস্থ কোণদ্বয়ের সমষ্টি 180° হয়, তবে রেখা দুটি কেমন?", "সমান্তরাল", ["লম্ব", "পরস্পরছেদী", "বক্র"], "", M),
 ("একটি সরলরেখার সাথে সমান্তরাল দুটি সরলরেখা পরস্পর কেমন?", "সমান্তরাল", ["লম্ব", "ছেদী", "কোনো সম্পর্ক নেই"], "", M),
 ("একটি ছেদক দুটি সমান্তরাল রেখার একটির উপর লম্ব হলে অপরটির উপর কেমন হবে?", "লম্ব", ["সমান্তরাল", "সূক্ষ্মকোণে আনত", "স্থূলকোণে আনত"], "", M),
 ("রৈখিক যুগল কোণের সমষ্টি কত?", "180°", ["90°", "360°", "270°"], "", E),
 ("একটি বিন্দুতে উৎপন্ন সকল কোণের সমষ্টি কত?", "360°", ["180°", "90°", "270°"], "", E),
]
def s8_alt(b, lv):
    a = R.randint(20, 160); kind = R.choice(['একান্তর', 'অনুরূপ', 'বিপ্রতীপ'])
    b.add(f"দুটি সমান্তরাল সরলরেখাকে একটি ছেদক ছেদ করেছে। একটি কোণ {a}° হলে এর {kind} কোণটি কত?", ANG(a), W(ANG(a), [ANG(180 - a) if 180 - a != a else ANG(90), ANG(90 - a) if a < 90 else ANG(a - 90), ANG(360 - a), ANG(a + 10)]), f"{kind} কোণগুলো সমান।", lv)
def s8_co(b, lv):
    a = R.randint(20, 160)
    if a == 90: return
    b.add(f"দুটি সমান্তরাল সরলরেখাকে একটি ছেদক ছেদ করেছে। ছেদকের একই পাশের একটি অন্তঃস্থ কোণ {a}° হলে অপর অন্তঃস্থ কোণটি কত?", ANG(180 - a), W(ANG(180 - a), [ANG(a), ANG(360 - a), ANG(abs(90 - a)), ANG(180 - a + 10)]), f"সমষ্টি 180°; 180° − {a}°।", lv)
def s8_lin(b, lv):
    a = R.randint(10, 170)
    if a == 90: return
    t = R.randrange(2)
    if t == 0: b.add(f"একটি রৈখিক যুগল কোণের একটি {a}° হলে অপরটি কত?", ANG(180 - a), W(ANG(180 - a), [ANG(a), ANG(abs(90 - a)), ANG(360 - a), ANG(180 - a + 5)]), "", lv)
    else: b.add(f"{a}° কোণের সম্পূরক কোণ কত?", ANG(180 - a), W(ANG(180 - a), [ANG(abs(90 - a)), ANG(360 - a), ANG(a), ANG(180 - a - 10)]), "", lv)
def s8_comp(b, lv):
    a = R.randint(5, 85)
    if a == 45: return
    b.add(f"{a}° কোণের পূরক কোণ কত?", ANG(90 - a), W(ANG(90 - a), [ANG(180 - a), ANG(a), ANG(360 - a), ANG(90 - a + 10)]), "", lv)
def s8_vert(b, lv):
    a = R.randint(15, 165)
    if a == 90: return
    b.add(f"দুটি সরলরেখা পরস্পর ছেদ করায় উৎপন্ন একটি কোণ {a}°। বাকি তিনটি কোণ কত?", f"{180 - a}°, {a}°, {180 - a}°", W(f"{180 - a}°, {a}°, {180 - a}°", [f"{a}°, {a}°, {a}°", f"{90 - a % 90}°, {a}°, {90 - a % 90}°", f"{180 - a}°, {180 - a}°, {180 - a}°", f"{360 - a}°, {a}°, {180 - a}°"]), "বিপ্রতীপ কোণ সমান, সন্নিহিত কোণ সম্পূরক।", lv)
def s8_xalt(b, lv):
    x = R.randint(5, 40); p, q = R.randint(2, 5), R.randint(1, 4)
    if p == q: return
    c1 = R.randint(-20, 40); c2 = (p - q) * x + c1
    a = p * x - c2 if False else None
    kind = R.choice(['একান্তর', 'অনুরূপ'])
    ang = q * x + c2
    if not (5 < ang < 175): return
    b.add(f"দুটি সমান্তরাল সরলরেখাকে একটি ছেদক ছেদ করেছে। দুটি {kind} কোণ যথাক্রমে ({cf(p, 'x')} {sgn(c1)})° ও ({cf(q, 'x')} {sgn(c2)})° হলে x এর মান কত?", x, W(x, [x + 2, x - 2 if x > 2 else x + 4, ang, F(180 - c1 - c2, p + q) if (180 - c1 - c2) % (p + q) == 0 and (180 - c1 - c2) // (p + q) != x else x + 5]), f"{kind} কোণ সমান: {p}x {sgn(c1)} = {q}x {sgn(c2)}।", lv)
def s8_xco(b, lv):
    p, q = R.randint(1, 5), R.randint(1, 5); x = R.randint(5, 40); c1 = R.randint(-20, 40)
    c2 = 180 - (p + q) * x - c1
    a1, a2 = p * x + c1, q * x + c2
    if not (5 < a1 < 175 and 5 < a2 < 175) or abs(c2) > 120: return
    b.add(f"দুটি সমান্তরাল সরলরেখাকে একটি ছেদক ছেদ করেছে। ছেদকের একই পাশের অন্তঃস্থ কোণদ্বয় ({p if p > 1 else ''}x {sgn(c1)})° ও ({q if q > 1 else ''}x {sgn(c2)})° হলে x = কত?", x, W(x, [x + 5, x - 5 if x > 5 else x + 10, a1, x + 1]), f"সমষ্টি 180°: {p + q}x {sgn(c1 + c2)} = 180।", lv)
def s8_find(b, lv):
    a = R.randint(25, 155)
    if a == 90: return
    pos = R.choice([('একান্তর অন্তঃস্থ', a), ('অনুরূপ', a), ('ছেদকের একই পাশের অন্তঃস্থ', 180 - a), ('একান্তর বহিঃস্থ', a), ('ছেদকের একই পাশের বহিঃস্থ', 180 - a)])
    b.add(f"AB ∥ CD এবং EF ছেদক। ∠1 = {a}° হলে ∠1 এর {pos[0]} কোণটি কত?", ANG(pos[1]), W(ANG(pos[1]), [ANG(180 - pos[1]) if 180 - pos[1] != pos[1] else ANG(90 + 10), ANG(abs(90 - a)), ANG(360 - a), ANG(pos[1] + 15)]), "", lv)
def s8_ratio(b, lv):
    p, q = R.randint(1, 8), R.randint(1, 8)
    if p == q or 180 % (p + q): return
    k = 180 // (p + q)
    b.add(f"দুটি সমান্তরাল রেখাকে একটি ছেদক ছেদ করেছে। ছেদকের একই পাশের অন্তঃস্থ কোণদ্বয়ের অনুপাত {p} : {q} হলে বৃহত্তর কোণটি কত?", ANG(max(p, q) * k), W(ANG(max(p, q) * k), [ANG(min(p, q) * k), ANG(max(p, q) * 90 // (p + q)) if (max(p, q) * 90) % (p + q) == 0 else ANG(max(p, q) * k + 10), ANG(360 * max(p, q) // (p + q)) if (360 * max(p, q)) % (p + q) == 0 else ANG(max(p, q) * k - 10), ANG(180 - k)]), f"{p}k + {q}k = 180° ⇒ k = {k}°।", lv)
def s8_zig(b, lv):
    a, c = R.randint(20, 80), R.randint(20, 80)
    b.add(f"AB ∥ CD। AB ও CD এর মাঝে একটি বিন্দু O এমনভাবে নেওয়া হলো যে ∠BAO = {a}° এবং ∠DCO = {c}° (একই দিকে)। ∠AOC = কত?", ANG(a + c), W(ANG(a + c), [ANG(abs(a - c)) if a != c else ANG(10), ANG(180 - a - c), ANG(360 - a - c), ANG(90)]), "O দিয়ে AB এর সমান্তরাল রেখা টেনে দুই একান্তর কোণের যোগফল।", lv)
def s8_four(b, lv):
    a = R.randint(20, 160)
    if a == 90: return
    s = a * 2 + (180 - a) * 2
    b.add(f"দুটি সমান্তরাল রেখাকে একটি ছেদক ছেদ করায় উৎপন্ন একটি কোণ {a}°। উৎপন্ন 8টি কোণের মধ্যে কয়টি কোণ {a}° এর সমান?", "4টি", ["2টি", "3টি", "8টি", "6টি"], f"একান্তর, অনুরূপ ও বিপ্রতীপ মিলিয়ে 4টি।", lv)
def s8_sum4(b, lv):
    a = R.randint(20, 160)
    if a == 90: return
    t = R.randrange(2)
    if t == 0: v = 2 * a; b.add(f"দুটি সমান্তরাল রেখার একটি ছেদকের দ্বারা উৎপন্ন একান্তর কোণযুগলের একটি {a}° হলে কোণযুগলের সমষ্টি কত?", ANG(v), W(ANG(v), [ANG(180), ANG(a), ANG(360 - a), ANG(180 - a)]), "", lv)
    else: v = 180; b.add(f"দুটি সমান্তরাল রেখাকে একটি ছেদক ছেদ করেছে। একটি কোণ {a}° এবং এর সন্নিহিত কোণের সমষ্টি কত?", ANG(v), W(ANG(v), [ANG(2 * a) if 2 * a != 180 else ANG(90), ANG(360), ANG(a), ANG(180 - a)]), "রৈখিক যুগল।", lv)
K8 = part(None, 250, fx8, [s8_alt, s8_co, s8_lin, s8_comp, s8_vert, s8_find], [s8_xalt, s8_xco, s8_find, s8_ratio, s8_sum4, s8_vert], [s8_zig, s8_xalt, s8_xco, s8_ratio])
save('v8', K8)

# ===================================================== 9.1 ত্রিভুজের কোণ
fx91 = [
 ("ত্রিভুজের তিন কোণের সমষ্টি কত?", "দুই সমকোণ (180°)", ["এক সমকোণ", "তিন সমকোণ", "চার সমকোণ"], "", E),
 ("ত্রিভুজের একটি বাহু বর্ধিত করলে উৎপন্ন বহিঃস্থ কোণ অন্তঃস্থ বিপরীত কোণদ্বয়ের কী?", "সমষ্টির সমান", ["অন্তরের সমান", "গুণফলের সমান", "যেকোনো একটির সমান"], "", E),
 ("যে ত্রিভুজের একটি কোণ সমকোণ, তাকে কী বলে?", "সমকোণী ত্রিভুজ", ["স্থূলকোণী ত্রিভুজ", "সূক্ষ্মকোণী ত্রিভুজ", "সমবাহু ত্রিভুজ"], "", E),
 ("যে ত্রিভুজের তিনটি কোণই সূক্ষ্মকোণ, তাকে কী বলে?", "সূক্ষ্মকোণী ত্রিভুজ", ["স্থূলকোণী ত্রিভুজ", "সমকোণী ত্রিভুজ", "বিষমবাহু ত্রিভুজ"], "", E),
 ("একটি ত্রিভুজে সর্বাধিক কয়টি স্থূলকোণ থাকতে পারে?", "1টি", ["2টি", "3টি", "0টি"], "", E),
 ("সমবাহু ত্রিভুজের প্রতিটি কোণ কত?", "60°", ["90°", "45°", "30°"], "", E),
 ("সমকোণী ত্রিভুজের সূক্ষ্মকোণদ্বয়ের সমষ্টি কত?", "90°", ["180°", "60°", "45°"], "", E),
 ("সমদ্বিবাহু ত্রিভুজের সমান বাহুদ্বয়ের বিপরীত কোণদ্বয় কেমন?", "সমান", ["সম্পূরক", "পূরক", "অসমান"], "", E),
 ("একটি ত্রিভুজের বহিঃস্থ কোণগুলোর (প্রতিটি শীর্ষে একটি করে) সমষ্টি কত?", "360°", ["180°", "270°", "540°"], "", M),
 ("ত্রিভুজের বহিঃস্থ কোণ অন্তঃস্থ বিপরীত যেকোনো কোণ অপেক্ষা কেমন?", "বৃহত্তর", ["ক্ষুদ্রতর", "সমান", "অর্ধেক"], "", M),
]
def t91_third(b, lv):
    a, c = R.randint(20, 110), R.randint(20, 110)
    if a + c >= 170: return
    v = 180 - a - c
    b.add(f"একটি ত্রিভুজের দুটি কোণ {a}° ও {c}° হলে তৃতীয় কোণটি কত?", ANG(v), W(ANG(v), [ANG(a + c), ANG(360 - a - c), ANG(abs(a - c)) if abs(a - c) != v else ANG(v + 10), ANG(v + 5)]), f"180° − ({a}° + {c}°)।", lv)
def t91_right(b, lv):
    a = R.randint(10, 80)
    if a == 45: return
    b.add(f"একটি সমকোণী ত্রিভুজের একটি সূক্ষ্মকোণ {a}° হলে অপর সূক্ষ্মকোণটি কত?", ANG(90 - a), W(ANG(90 - a), [ANG(180 - a), ANG(a), ANG(90 + a), ANG(90 - a + 10)]), "", lv)
def t91_ext(b, lv):
    a, c = R.randint(20, 100), R.randint(20, 100)
    if a + c >= 170: return
    b.add(f"ΔABC এর ∠A = {a}° ও ∠B = {c}°। BC বাহুকে D পর্যন্ত বর্ধিত করলে বহিঃস্থ ∠ACD = কত?", ANG(a + c), W(ANG(a + c), [ANG(180 - a - c), ANG(abs(a - c)) if a != c else ANG(a + 10), ANG(180 - a), ANG(360 - a - c)]), "বহিঃস্থ কোণ = অন্তঃস্থ বিপরীত কোণদ্বয়ের সমষ্টি।", lv)
def t91_extin(b, lv):
    e, a = R.randint(60, 170), R.randint(15, 90)
    if a >= e: return
    b.add(f"একটি ত্রিভুজের একটি বহিঃস্থ কোণ {e}° এবং এর একটি অন্তঃস্থ বিপরীত কোণ {a}°। অপর অন্তঃস্থ বিপরীত কোণটি কত?", ANG(e - a), W(ANG(e - a), [ANG(180 - e), ANG(e + a) if e + a < 360 else ANG(e), ANG(180 - a), ANG(e - a + 10)]), f"{e}° − {a}°।", lv)
def t91_ratio(b, lv):
    p, q, r = R.randint(1, 9), R.randint(1, 9), R.randint(1, 9)
    s = p + q + r
    if 180 % s or len({p, q, r}) < 3: return
    k = 180 // s; t = R.choice(['বৃহত্তম', 'ক্ষুদ্রতম'])
    v = (max if t == 'বৃহত্তম' else min)(p, q, r) * k
    b.add(f"একটি ত্রিভুজের কোণগুলোর অনুপাত {p} : {q} : {r} হলে {t} কোণটি কত?", ANG(v), W(ANG(v), [ANG((min if t == 'বৃহত্তম' else max)(p, q, r) * k), ANG(sorted([p, q, r])[1] * k), ANG(k), ANG(v + 10)]), f"{s}k = 180° ⇒ k = {k}°।", lv)
def t91_iso(b, lv):
    t = R.randrange(2)
    if t == 0:
        a = R.randint(10, 160)
        if (180 - a) % 2: return
        b.add(f"একটি সমদ্বিবাহু ত্রিভুজের শীর্ষকোণ {a}° হলে ভূমিসংলগ্ন প্রতিটি কোণ কত?", ANG((180 - a) // 2), W(ANG((180 - a) // 2), [ANG(180 - a), ANG(a), ANG(90 - a // 2 + 5), ANG((180 - a) // 2 + 10)]), f"(180° − {a}°)/2।", lv)
    else:
        a = R.randint(20, 85)
        b.add(f"একটি সমদ্বিবাহু ত্রিভুজের ভূমিসংলগ্ন প্রতিটি কোণ {a}° হলে শীর্ষকোণ কত?", ANG(180 - 2 * a), W(ANG(180 - 2 * a), [ANG(180 - a), ANG(a), ANG(90 - a) if 90 - a != 180 - 2 * a else ANG(a + 10), ANG(2 * a)]), f"180° − 2 × {a}°।", lv)
def t91_x(b, lv):
    x = R.randint(5, 40); p, q, r = R.randint(1, 4), R.randint(1, 4), R.randint(1, 4)
    c1, c2 = R.randint(-10, 30), R.randint(-10, 30); c3 = 180 - (p + q + r) * x - c1 - c2
    angs = [p * x + c1, q * x + c2, r * x + c3]
    if any(a <= 5 for a in angs) or abs(c3) > 90: return
    fm = lambda k, c: f"({k if k > 1 else ''}x {sgn(c)})°" if c else f"{k if k > 1 else ''}x°"
    b.add(f"একটি ত্রিভুজের কোণ তিনটি {fm(p, c1)}, {fm(q, c2)} ও {fm(r, c3)} হলে x = কত?", x, W(x, [x + 5, x - 5 if x > 5 else x + 10, angs[0], x + 2]), f"সমষ্টি 180°।", lv)
def t91_kind(b, lv):
    a, c = R.randint(10, 120), R.randint(10, 120)
    v = 180 - a - c
    if v <= 0: return
    m = max(a, c, v); kind = 'সমকোণী' if m == 90 else 'স্থূলকোণী' if m > 90 else 'সূক্ষ্মকোণী'
    b.add(f"একটি ত্রিভুজের দুটি কোণ {a}° ও {c}° হলে ত্রিভুজটি কোন ধরনের?", f"{kind} ত্রিভুজ", W(f"{kind} ত্রিভুজ", ["সমকোণী ত্রিভুজ", "স্থূলকোণী ত্রিভুজ", "সূক্ষ্মকোণী ত্রিভুজ", "সমবাহু ত্রিভুজ"]), f"তৃতীয় কোণ {v}°।", lv)
def t91_bis(b, lv):
    a = R.randint(20, 140)
    if a % 2: return
    v = 90 + a // 2
    b.add(f"ΔABC এর ∠A = {a}°। ∠B ও ∠C এর সমদ্বিখণ্ডকদ্বয় O বিন্দুতে মিলিত হলে ∠BOC = কত?", ANG(v), W(ANG(v), [ANG(180 - a), ANG(90 - a // 2), ANG(a), ANG(90 + a)]), f"∠BOC = 90° + ∠A/2 = 90° + {a // 2}°।", lv)
P91 = part('9.1', 150, fx91, [t91_third, t91_right, t91_ext, t91_iso], [t91_extin, t91_ratio, t91_kind, t91_iso, t91_ext], [t91_x, t91_bis, t91_ratio])

# ===================================================== 9.2 ত্রিভুজের বাহু
fx92 = [
 ("ত্রিভুজের যেকোনো দুই বাহুর সমষ্টি তৃতীয় বাহু অপেক্ষা কেমন?", "বৃহত্তর", ["ক্ষুদ্রতর", "সমান", "অর্ধেক"], "", E),
 ("ত্রিভুজের যেকোনো দুই বাহুর অন্তর তৃতীয় বাহু অপেক্ষা কেমন?", "ক্ষুদ্রতর", ["বৃহত্তর", "সমান", "দ্বিগুণ"], "", E),
 ("যে ত্রিভুজের তিনটি বাহুই সমান, তাকে কী বলে?", "সমবাহু ত্রিভুজ", ["সমদ্বিবাহু ত্রিভুজ", "বিষমবাহু ত্রিভুজ", "সমকোণী ত্রিভুজ"], "", E),
 ("যে ত্রিভুজের দুটি বাহু সমান, তাকে কী বলে?", "সমদ্বিবাহু ত্রিভুজ", ["সমবাহু ত্রিভুজ", "বিষমবাহু ত্রিভুজ", "স্থূলকোণী ত্রিভুজ"], "", E),
 ("যে ত্রিভুজের তিনটি বাহুই অসমান, তাকে কী বলে?", "বিষমবাহু ত্রিভুজ", ["সমবাহু ত্রিভুজ", "সমদ্বিবাহু ত্রিভুজ", "সমকোণী ত্রিভুজ"], "", E),
 ("ত্রিভুজের বৃহত্তর বাহুর বিপরীত কোণ ক্ষুদ্রতর বাহুর বিপরীত কোণ অপেক্ষা কেমন?", "বৃহত্তর", ["ক্ষুদ্রতর", "সমান", "অর্ধেক"], "", E),
 ("সমকোণী ত্রিভুজের বৃহত্তম বাহু কোনটি?", "অতিভুজ", ["ভূমি", "লম্ব", "মধ্যমা"], "", E),
 ("সমকোণী ত্রিভুজের সমকোণের বিপরীত বাহুকে কী বলে?", "অতিভুজ", ["ভূমি", "উচ্চতা", "মধ্যমা"], "", E),
]
def u92_can(b, lv):
    while True:
        s = sorted(R.sample(range(2, 30), 3))
        if s[0] + s[1] > s[2]: break
    w = []
    while len(w) < 3:
        t = sorted(R.sample(range(1, 30), 3))
        if t[0] + t[1] <= t[2] and ', '.join(map(str, t)) not in w: w.append(', '.join(map(str, t)))
    c = ', '.join(map(str, s))
    b.add("নিচের কোন বাহুগুলো (সেমি) দিয়ে ত্রিভুজ আঁকা সম্ভব?", c, W(c, w), f"{s[0]} + {s[1]} > {s[2]}।", lv)
def u92_cannot(b, lv):
    while True:
        s = sorted(R.sample(range(1, 30), 3))
        if s[0] + s[1] <= s[2]: break
    w = []
    while len(w) < 3:
        t = sorted(R.sample(range(2, 30), 3))
        if t[0] + t[1] > t[2] and ', '.join(map(str, t)) not in w: w.append(', '.join(map(str, t)))
    c = ', '.join(map(str, s))
    b.add("নিচের কোন বাহুগুলো (সেমি) দিয়ে ত্রিভুজ আঁকা সম্ভব নয়?", c, W(c, w), f"{s[0]} + {s[1]} = {s[0] + s[1]} ≯ {s[2]}।", lv)
def u92_range(b, lv):
    a, c = R.randint(3, 30), R.randint(3, 30)
    if a == c: return
    lo, hi = abs(a - c), a + c; cc = f"{lo} < x < {hi}"
    b.add(f"একটি ত্রিভুজের দুটি বাহু {a} সেমি ও {c} সেমি হলে তৃতীয় বাহু x এর সীমা কোনটি?", cc, W(cc, [f"{lo} ≤ x ≤ {hi}", f"0 < x < {hi}", f"{lo} < x < {max(a, c)}", f"x > {hi}"]), "অন্তর < তৃতীয় বাহু < সমষ্টি।", lv)
def u92_count(b, lv):
    a, c = R.randint(3, 20), R.randint(3, 20)
    if a == c: return
    v = (a + c - 1) - abs(a - c)
    b.add(f"একটি ত্রিভুজের দুটি বাহু {a} সেমি ও {c} সেমি। তৃতীয় বাহুর দৈর্ঘ্য পূর্ণসংখ্যা হলে কতগুলো ভিন্ন মান সম্ভব?", v, W(v, [v + 1, v - 1, a + c, 2 * min(a, c)]), f"{abs(a - c) + 1} থেকে {a + c - 1} পর্যন্ত।", lv)
def u92_per(b, lv):
    a, c, d = R.randint(3, 40), R.randint(3, 40), R.randint(3, 40)
    s = sorted([a, c, d])
    if s[0] + s[1] <= s[2]: return
    t = R.randrange(3)
    if t == 0: b.add(f"একটি ত্রিভুজের বাহুগুলো {a} সেমি, {c} সেমি ও {d} সেমি হলে পরিসীমা কত সেমি?", a + c + d, W(a + c + d, [a + c, (a + c + d) // 2, a + c + d + 1, a * 3]), "", lv)
    elif t == 1: b.add(f"একটি ত্রিভুজের পরিসীমা {a + c + d} সেমি। দুটি বাহু {a} সেমি ও {c} সেমি হলে তৃতীয় বাহু কত সেমি?", d, W(d, [a + c, d + 1, abs(a - c) if abs(a - c) != d else d + 2, (a + c + d) // 3 if (a + c + d) // 3 != d else d - 1]), "", lv)
    else:
        s = R.randint(3, 40); b.add(f"একটি সমবাহু ত্রিভুজের পরিসীমা {3 * s} সেমি হলে প্রতিটি বাহু কত সেমি?", s, W(s, [3 * s, s + 3, 2 * s, s - 1]), "", lv)
def u92_iso(b, lv):
    e, bs = R.randint(4, 40), R.randint(2, 40)
    if 2 * e <= bs: return
    t = R.randrange(2)
    if t == 0: b.add(f"একটি সমদ্বিবাহু ত্রিভুজের পরিসীমা {2 * e + bs} সেমি এবং ভূমি {bs} সেমি। সমান বাহুদ্বয়ের প্রতিটি কত সেমি?", e, W(e, [2 * e, e + bs, (2 * e + bs) // 3 if (2 * e + bs) // 3 != e else e + 1, e - 1]), f"({2 * e + bs} − {bs})/2।", lv)
    else: b.add(f"একটি সমদ্বিবাহু ত্রিভুজের সমান বাহুদ্বয়ের প্রতিটি {e} সেমি এবং পরিসীমা {2 * e + bs} সেমি। ভূমি কত সেমি?", bs, W(bs, [e, bs + e, 2 * e, bs + 1]), "", lv)
def u92_kind(b, lv):
    s = R.choice(['eq', 'iso', 'sc'])
    if s == 'eq': x = R.randint(3, 30); sd = [x, x, x]; c = 'সমবাহু'
    elif s == 'iso': x, y = R.randint(3, 30), R.randint(2, 30); sd = [x, x, y]; c = 'সমদ্বিবাহু'
    else:
        sd = R.sample(range(3, 30), 3); c = 'বিষমবাহু'
    ss = sorted(sd)
    if ss[0] + ss[1] <= ss[2] or (s == 'iso' and len(set(sd)) != 2): return
    R.shuffle(sd)
    b.add(f"একটি ত্রিভুজের বাহুগুলো {sd[0]} সেমি, {sd[1]} সেমি ও {sd[2]} সেমি হলে ত্রিভুজটি কোন ধরনের?", f"{c} ত্রিভুজ", W(f"{c} ত্রিভুজ", ["সমবাহু ত্রিভুজ", "সমদ্বিবাহু ত্রিভুজ", "বিষমবাহু ত্রিভুজ", "সমকোণী সমবাহু ত্রিভুজ"]), "", lv)
def u92_big(b, lv):
    sd = R.sample(range(3, 30), 3); ss = sorted(sd)
    if ss[0] + ss[1] <= ss[2]: return
    names = ['AB', 'BC', 'CA']; opp = {'AB': '∠C', 'BC': '∠A', 'CA': '∠B'}
    t = R.choice(['বৃহত্তম', 'ক্ষুদ্রতম']); i = sd.index(max(sd) if t == 'বৃহত্তম' else min(sd))
    b.add(f"ΔABC এ AB = {sd[0]} সেমি, BC = {sd[1]} সেমি ও CA = {sd[2]} সেমি। কোন কোণটি {t}?", opp[names[i]], W(opp[names[i]], ['∠A', '∠B', '∠C', '∠A + ∠B']), f"{t} বাহুর বিপরীত কোণ {t}।", lv)
def u92_right(b, lv):
    trip = R.choice([(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (6, 8, 10), (9, 12, 15), (20, 21, 29), (12, 16, 20)]); k = R.randint(1, 3)
    a, c, h = [k * v for v in trip]; t = R.randrange(2)
    if t == 0: b.add(f"একটি সমকোণী ত্রিভুজের সমকোণ সংলগ্ন বাহুদ্বয় {a} সেমি ও {c} সেমি হলে অতিভুজ কত সেমি?", h, W(h, [a + c, h + 1, c + 1, h - 2]), f"√({a}² + {c}²) = {h}।", lv)
    else: b.add(f"একটি সমকোণী ত্রিভুজের অতিভুজ {h} সেমি এবং একটি বাহু {a} সেমি হলে অপর বাহু কত সেমি?", c, W(c, [h - a, c + 1, h + a, c - 2]), f"√({h}² − {a}²) = {c}।", lv)
P92 = part('9.2', 150, fx92, [u92_can, u92_cannot, u92_per, u92_kind], [u92_range, u92_iso, u92_big, u92_count, u92_per], [u92_count, u92_right, u92_range])

# ===================================================== 9.3 ত্রিভুজ অঙ্কন
fx93 = [
 ("তিনটি বাহু দেওয়া থাকলে কয়টি নির্দিষ্ট ত্রিভুজ আঁকা যায়?", "1টি", ["2টি", "3টি", "অসংখ্য"], "", E),
 ("ত্রিভুজ আঁকার জন্য কমপক্ষে কয়টি পরিমাপ জানা দরকার?", "3টি", ["2টি", "4টি", "6টি"], "", E),
 ("শুধু তিনটি কোণ দেওয়া থাকলে কেমন ত্রিভুজ আঁকা যায়?", "অসংখ্য ত্রিভুজ, নির্দিষ্ট নয়", ["একটি নির্দিষ্ট ত্রিভুজ", "কোনো ত্রিভুজ আঁকা যায় না", "দুটি ত্রিভুজ"], "আকৃতি একই হলেও আকার নির্দিষ্ট হয় না।", E),
 ("দুটি বাহু ও তাদের অন্তর্ভুক্ত কোণ দেওয়া থাকলে কয়টি ত্রিভুজ আঁকা যায়?", "1টি নির্দিষ্ট ত্রিভুজ", ["2টি", "অসংখ্য", "আঁকা যায় না"], "", E),
 ("দুটি কোণ ও তাদের সংলগ্ন বাহু দেওয়া থাকলে কয়টি ত্রিভুজ আঁকা যায়?", "1টি নির্দিষ্ট ত্রিভুজ", ["2টি", "অসংখ্য", "আঁকা যায় না"], "", E),
 ("সমকোণী ত্রিভুজ আঁকতে অতিভুজ ও একটি বাহু দেওয়া থাকলে কয়টি নির্দিষ্ট ত্রিভুজ আঁকা যায়?", "1টি", ["2টি", "অসংখ্য", "কোনোটিই নয়"], "", M),
 ("ত্রিভুজ অঙ্কনে সাধারণত কোন যন্ত্রগুলো লাগে?", "রুলার, কম্পাস ও চাঁদা", ["শুধু পেনসিল", "ক্যালকুলেটর", "শুধু রুলার"], "", E),
 ("সমবাহু ত্রিভুজ আঁকতে কয়টি উপাত্ত জানলেই যথেষ্ট?", "একটি বাহু", ["তিনটি কোণ", "দুটি কোণ", "উচ্চতা ও কোণ"], "", M),
 ("কোনো রেখাংশের লম্বদ্বিখণ্ডক আঁকতে কম্পাসের ব্যাসার্ধ রেখাংশের কত অংশের চেয়ে বেশি নিতে হয়?", "অর্ধেকের", ["এক-তৃতীয়াংশের", "এক-চতুর্থাংশের", "দ্বিগুণের"], "", M),
]
def v93_sides(b, lv):
    while True:
        s = sorted(R.sample(range(2, 20), 3))
        if s[0] + s[1] > s[2]: break
    t = sorted(R.sample(range(1, 20), 3))
    if t[0] + t[1] > t[2]:
        return
    if R.random() < .5:
        b.add(f"{s[0]} সেমি, {s[1]} সেমি ও {s[2]} সেমি বাহুবিশিষ্ট ত্রিভুজ আঁকা সম্ভব কি?", "হ্যাঁ, কারণ যেকোনো দুই বাহুর সমষ্টি তৃতীয় বাহু অপেক্ষা বৃহত্তর", ["না, কারণ দুই বাহুর সমষ্টি তৃতীয় বাহুর চেয়ে ছোট", "না, কারণ বাহুগুলো অসমান", "হ্যাঁ, কারণ বাহুগুলো পূর্ণসংখ্যা"], f"{s[0]} + {s[1]} > {s[2]}।", lv)
    else:
        b.add(f"{t[0]} সেমি, {t[1]} সেমি ও {t[2]} সেমি বাহুবিশিষ্ট ত্রিভুজ আঁকা সম্ভব কি?", "না, কারণ ছোট দুই বাহুর সমষ্টি তৃতীয় বাহু অপেক্ষা বৃহত্তর নয়", ["হ্যাঁ, অবশ্যই সম্ভব", "হ্যাঁ, কারণ বাহুগুলো ভিন্ন", "হ্যাঁ, তবে সমকোণী হবে"], f"{t[0]} + {t[1]} = {t[0] + t[1]} ≯ {t[2]}।", lv)
def v93_angles(b, lv):
    a, c = R.randint(20, 150), R.randint(20, 150)
    ok = a + c < 180
    if a + c == 180: return
    c0 = "হ্যাঁ, সম্ভব" if ok else "না, সম্ভব নয়"
    b.add(f"দুটি কোণ {a}° ও {c}° এবং এদের সংলগ্ন বাহু 6 সেমি দিয়ে ত্রিভুজ আঁকা সম্ভব কি?", c0, W(c0, ["হ্যাঁ, সম্ভব", "না, সম্ভব নয়", "শুধু সমকোণী হলে সম্ভব", "শুধু সমবাহু হলে সম্ভব"]), f"দুই কোণের সমষ্টি {a + c}° {'< 180°' if ok else '> 180°'}।", lv)
def v93_third(b, lv):
    a, c = R.randint(20, 100), R.randint(20, 100)
    if a + c >= 170: return
    l = R.randint(3, 12)
    b.add(f"ΔABC আঁকা হলো যেখানে ∠B = {a}°, ∠C = {c}° এবং BC = {l} সেমি। আঁকার পর ∠A মাপলে কত পাওয়া যাবে?", ANG(180 - a - c), W(ANG(180 - a - c), [ANG(a + c), ANG(90), ANG(abs(a - c)) if abs(a - c) != 180 - a - c else ANG(10), ANG(180 - a)]), "তিন কোণের সমষ্টি 180°।", lv)
def v93_data(b, lv):
    opts = [("দুটি বাহু ও তাদের অন্তর্ভুক্ত কোণ", True), ("তিনটি বাহু", True), ("দুটি কোণ ও তাদের সংলগ্ন বাহু", True), ("সমকোণী ত্রিভুজের অতিভুজ ও একটি বাহু", True), ("শুধু তিনটি কোণ", False), ("শুধু দুটি বাহু", False), ("শুধু একটি বাহু ও একটি কোণ", False), ("শুধু দুটি কোণ", False)]
    good = [o for o, k in opts if k]; bad = [o for o, k in opts if not k]
    if R.random() < .5:
        c = R.choice(good); w = R.sample(bad, 3)
        b.add("নিচের কোন উপাত্ত দিয়ে একটি নির্দিষ্ট ত্রিভুজ আঁকা যায়?", c, W(c, w), "", lv)
    else:
        c = R.choice(bad); w = R.sample(good, 3)
        b.add("নিচের কোন উপাত্ত দিয়ে একটি নির্দিষ্ট ত্রিভুজ আঁকা যায় না?", c, W(c, w), "", lv)
def v93_eq(b, lv):
    s = R.randint(3, 15); t = R.randrange(3)
    if t == 0: b.add(f"{s} সেমি বাহুবিশিষ্ট একটি সমবাহু ত্রিভুজ আঁকলে প্রতিটি কোণ কত হবে?", ANG(60), W(ANG(60), [ANG(90), ANG(45), ANG(s * 10) if s * 10 not in (60, 90, 45) else ANG(30), ANG(120)]), "", lv)
    elif t == 1: b.add(f"{s} সেমি বাহুবিশিষ্ট একটি সমবাহু ত্রিভুজ আঁকলে এর পরিসীমা কত সেমি হবে?", 3 * s, W(3 * s, [s, 2 * s, 4 * s, s * s]), "", lv)
    else:
        a = R.randint(20, 80)
        b.add(f"ভূমি {s} সেমি এবং ভূমিসংলগ্ন কোণদ্বয় {a}° ও {a}° নিয়ে একটি ত্রিভুজ আঁকা হলো। ত্রিভুজটি কোন ধরনের?", "সমদ্বিবাহু", W("সমদ্বিবাহু", ["সমবাহু" if a != 60 else "বিষমবাহু", "বিষমবাহু", "সমকোণী সমবাহু", "স্থূলকোণী সমবাহু"]), "ভূমিসংলগ্ন কোণ সমান হলে বিপরীত বাহু সমান।", lv)
def v93_iso(b, lv):
    a = R.randint(20, 85); l = R.randint(3, 12)
    b.add(f"ভূমি {l} সেমি এবং ভূমিসংলগ্ন প্রতিটি কোণ {a}° নিয়ে একটি সমদ্বিবাহু ত্রিভুজ আঁকা হলো। শীর্ষকোণ কত হবে?", ANG(180 - 2 * a), W(ANG(180 - 2 * a), [ANG(180 - a), ANG(2 * a), ANG(90 - a) if 90 - a != 180 - 2 * a else ANG(a), ANG(a + 10)]), "", lv)
def v93_right(b, lv):
    a = R.randint(10, 80); l = R.randint(3, 15)
    if a == 45: return
    b.add(f"অতিভুজ {l} সেমি এবং একটি সূক্ষ্মকোণ {a}° নিয়ে একটি সমকোণী ত্রিভুজ আঁকলে অপর সূক্ষ্মকোণটি কত হবে?", ANG(90 - a), W(ANG(90 - a), [ANG(180 - a), ANG(a), ANG(90 + a), ANG(90 - a + 5)]), "", lv)
def v93_sumcheck(b, lv):
    a, c, d = R.randint(20, 120), R.randint(20, 120), R.randint(20, 120)
    ok = a + c + d == 180
    if not ok and R.random() < .6:
        d = 180 - a - c
        if d <= 0: return
        ok = True
    c0 = "হ্যাঁ, কারণ কোণগুলোর সমষ্টি 180°" if ok else f"না, কারণ কোণগুলোর সমষ্টি {a + c + d}°"
    b.add(f"{a}°, {c}° ও {d}° কোণবিশিষ্ট ত্রিভুজ আঁকা সম্ভব কি?", c0, W(c0, ["হ্যাঁ, কারণ কোণগুলোর সমষ্টি 180°", f"না, কারণ কোণগুলোর সমষ্টি {a + c + d}°" if ok else "হ্যাঁ, যেকোনো তিনটি কোণে সম্ভব", "হ্যাঁ, কারণ সব কোণ ধনাত্মক", "না, কারণ কোণগুলো অসমান"]), "", lv)
P93 = part('9.3', 150, fx93, [v93_sides, v93_data, v93_eq, v93_third], [v93_angles, v93_third, v93_iso, v93_right, v93_sumcheck, v93_sides], [v93_angles, v93_sumcheck, v93_iso])
save('v9', P91 + P92 + P93)

# ===================================================== 10 সর্বসমতা ও সদৃশতা
fx101 = [
 ("দুটি ত্রিভুজ সর্বসম হলে তাদের অনুরূপ বাহু ও কোণগুলো কেমন হয়?", "সমান", ["সমানুপাতিক কিন্তু অসমান", "সম্পূরক", "অসমান"], "", E),
 ("সর্বসমতার প্রতীক কোনটি?", "≅", ["~", "≈", "∥"], "", E),
 ("দুটি ত্রিভুজের তিন বাহু যথাক্রমে সমান হলে কোন উপপাদ্য অনুযায়ী তারা সর্বসম?", "বাহু-বাহু-বাহু (SSS)", ["কোণ-কোণ-কোণ", "বাহু-কোণ-কোণ নয় এমন", "শুধু দুই বাহু"], "", E),
 ("দুটি ত্রিভুজের দুই বাহু ও তাদের অন্তর্ভুক্ত কোণ যথাক্রমে সমান হলে কোন নিয়মে তারা সর্বসম?", "বাহু-কোণ-বাহু (SAS)", ["বাহু-বাহু-বাহু", "কোণ-বাহু-কোণ", "অতিভুজ-বাহু"], "", E),
 ("দুটি ত্রিভুজের দুই কোণ ও তাদের সংলগ্ন বাহু যথাক্রমে সমান হলে কোন নিয়মে তারা সর্বসম?", "কোণ-বাহু-কোণ (ASA)", ["বাহু-কোণ-বাহু", "বাহু-বাহু-বাহু", "কোণ-কোণ-কোণ"], "", E),
 ("দুটি সমকোণী ত্রিভুজের অতিভুজ ও একটি বাহু যথাক্রমে সমান হলে কোন নিয়মে তারা সর্বসম?", "অতিভুজ-বাহু (RHS)", ["কোণ-কোণ-কোণ", "বাহু-বাহু-বাহু নয়", "কোণ-বাহু-কোণ নয়"], "", M),
 ("দুটি ত্রিভুজের তিন কোণ যথাক্রমে সমান হলে ত্রিভুজ দুটি কী হবেই?", "সদৃশ", ["সর্বসম", "সমবাহু", "সমকোণী"], "কোণ সমান হলে সর্বসম হওয়া জরুরি নয়।", M),
 ("দুটি সর্বসম ত্রিভুজের ক্ষেত্রফল কেমন?", "সমান", ["দ্বিগুণ", "অর্ধেক", "অসমান"], "", E),
]
TRI = [('ABC', 'DEF'), ('PQR', 'XYZ'), ('ABC', 'PQR'), ('LMN', 'XYZ'), ('ABC', 'DEF')]
def w101_side(b, lv):
    t1, t2 = R.choice(TRI); i, j = sorted(R.sample(range(3), 2)); v = R.randint(3, 20)
    s1, s2 = t1[i] + t1[j], t2[i] + t2[j]
    others = [t2[a] + t2[c] for a, c in ((0, 1), (1, 2), (0, 2)) if (a, c) != (i, j)]
    b.add(f"Δ{t1} ≅ Δ{t2} এবং {s1} = {v} সেমি হলে নিচের কোনটি {v} সেমি?", s2, W(s2, others + [t1[j] + t2[i], s2[::-1] + "'"]), "অনুরূপ বাহু সমান।", lv)
def w101_ang(b, lv):
    t1, t2 = R.choice(TRI); i = R.randrange(3); v = R.randint(20, 120)
    b.add(f"Δ{t1} ≅ Δ{t2} এবং ∠{t1[i]} = {v}° হলে ∠{t2[i]} = কত?", ANG(v), W(ANG(v), [ANG(180 - v), ANG(90 - v) if v < 90 else ANG(v - 10), ANG(v + 10), ANG(2 * v) if 2 * v < 180 else ANG(v // 2)]), "অনুরূপ কোণ সমান।", lv)
def w101_rule(b, lv):
    t1, t2 = R.choice(TRI)
    rules = [("SSS", f"{t1[0]}{t1[1]} = {t2[0]}{t2[1]}, {t1[1]}{t1[2]} = {t2[1]}{t2[2]}, {t1[0]}{t1[2]} = {t2[0]}{t2[2]}"),
             ("SAS", f"{t1[0]}{t1[1]} = {t2[0]}{t2[1]}, ∠{t1[1]} = ∠{t2[1]}, {t1[1]}{t1[2]} = {t2[1]}{t2[2]}"),
             ("ASA", f"∠{t1[1]} = ∠{t2[1]}, {t1[1]}{t1[2]} = {t2[1]}{t2[2]}, ∠{t1[2]} = ∠{t2[2]}"),
             ("RHS", f"∠{t1[1]} = ∠{t2[1]} = 90°, অতিভুজ {t1[0]}{t1[2]} = {t2[0]}{t2[2]}, {t1[1]}{t1[2]} = {t2[1]}{t2[2]}")]
    r, d = R.choice(rules); names = {"SSS": "বাহু-বাহু-বাহু", "SAS": "বাহু-কোণ-বাহু", "ASA": "কোণ-বাহু-কোণ", "RHS": "অতিভুজ-বাহু"}
    c = names[r]
    b.add(f"Δ{t1} ও Δ{t2} এ {d} হলে কোন উপপাদ্য অনুযায়ী ত্রিভুজ দুটি সর্বসম?", c, W(c, list(names.values()) + ["কোণ-কোণ-কোণ"]), "", lv)
def w101_val(b, lv):
    t1, t2 = R.choice(TRI); a, c = R.randint(20, 100), R.randint(20, 100)
    if a + c >= 170: return
    b.add(f"Δ{t1} ≅ Δ{t2}। ∠{t1[0]} = {a}° ও ∠{t1[1]} = {c}° হলে ∠{t2[2]} = কত?", ANG(180 - a - c), W(ANG(180 - a - c), [ANG(a), ANG(c), ANG(a + c), ANG(180 - a)]), f"∠{t1[2]} = 180° − {a}° − {c}° এবং ∠{t2[2]} = ∠{t1[2]}।", lv)
def w101_per(b, lv):
    t1, t2 = R.choice(TRI); s = R.sample(range(3, 25), 3); ss = sorted(s)
    if ss[0] + ss[1] <= ss[2]: return
    b.add(f"Δ{t1} ≅ Δ{t2}। {t1[0]}{t1[1]} = {s[0]} সেমি, {t1[1]}{t1[2]} = {s[1]} সেমি, {t1[0]}{t1[2]} = {s[2]} সেমি হলে Δ{t2} এর পরিসীমা কত সেমি?", sum(s), W(sum(s), [sum(s) * 2, s[0] + s[1], sum(s) + 1, max(s) * 3]), "সর্বসম ত্রিভুজের পরিসীমা সমান।", lv)
def w101_x(b, lv):
    t1, t2 = R.choice(TRI); x = R.randint(2, 15); p, q = R.randint(2, 5), R.randint(1, 4)
    if p == q: return
    c1 = R.randint(-5, 10); c2 = (p - q) * x + c1
    if p * x + c1 <= 0: return
    b.add(f"Δ{t1} ≅ Δ{t2}। {t1[0]}{t1[1]} = ({p}x {sgn(c1)}) সেমি এবং {t2[0]}{t2[1]} = ({q if q > 1 else ''}x {sgn(c2)}) সেমি হলে x = কত?", x, W(x, [x + 1, x + 2, p * x + c1, x - 1 if x > 1 else x + 3]), "অনুরূপ বাহু সমান।", lv)
P101 = part('10.1', 150, fx101, [w101_side, w101_ang, w101_rule], [w101_val, w101_per, w101_rule, w101_side], [w101_x, w101_val])

fx102 = [
 ("সদৃশতার প্রতীক কোনটি?", "~", ["≅", "∥", "⊥"], "", E),
 ("দুটি ত্রিভুজ সদৃশ হলে তাদের অনুরূপ কোণগুলো কেমন হয়?", "সমান", ["সম্পূরক", "অসমান", "পূরক"], "", E),
 ("দুটি ত্রিভুজ সদৃশ হলে তাদের অনুরূপ বাহুগুলো কেমন হয়?", "সমানুপাতিক", ["সবসময় সমান", "সম্পূরক", "লম্ব"], "", E),
 ("সব সর্বসম ত্রিভুজ কী?", "সদৃশ", ["সমবাহু", "সমকোণী", "বিষমবাহু"], "", E),
 ("সব সদৃশ ত্রিভুজ কি সর্বসম?", "না, সবসময় নয়", ["হ্যাঁ, সবসময়", "শুধু সমকোণী হলে না", "শুধু সমবাহু হলে না"], "", M),
 ("দুটি সমবাহু ত্রিভুজ সবসময় কী?", "সদৃশ", ["সর্বসম", "সমান ক্ষেত্রফলবিশিষ্ট", "সমান পরিসীমাবিশিষ্ট"], "সব কোণ 60°।", M),
]
def x102_side(b, lv):
    t1, t2 = R.choice(TRI); p, q = R.randint(2, 9), R.randint(2, 9)
    if p == q: return
    a = p * R.randint(1, 5); k = F(q, p); c = p * R.randint(1, 6); v = c * k
    if v.denominator != 1: return
    i, j = R.sample(range(3), 2)
    s1, s2 = t1[i] + t1[(i + 1) % 3], t2[i] + t2[(i + 1) % 3]; r1, r2 = t1[j] + t1[(j + 1) % 3], t2[j] + t2[(j + 1) % 3]
    if s1 == r1: return
    A, B = a, a * k
    if B.denominator != 1: return
    b.add(f"Δ{t1} ~ Δ{t2}। {s1} = {A} সেমি, {s2} = {int(B)} সেমি এবং {r1} = {c} সেমি হলে {r2} = কত সেমি?", int(v), W(int(v), [x for x in [c, int(v) + 1, c + int(B) - A, c * A // int(B) if (c * A) % int(B) == 0 and c * A // int(B) != int(v) else int(v) + 2, int(v) + 3] if x > 0]), f"অনুপাত {A} : {int(B)}; {c} × {int(B)}/{A}।", lv)
def x102_ratio(b, lv):
    p, q = R.randint(1, 9), R.randint(1, 9)
    if p == q or math.gcd(p, q) != 1: return
    k = R.randint(1, 6); t1, t2 = R.choice(TRI)
    b.add(f"Δ{t1} ~ Δ{t2} এবং {t1[0]}{t1[1]} = {p * k} সেমি, {t2[0]}{t2[1]} = {q * k} সেমি হলে Δ{t1} ও Δ{t2} এর অনুরূপ বাহুর অনুপাত কত?", f"{p} : {q}", W(f"{p} : {q}", [f"{q} : {p}", f"{p * p} : {q * q}", f"{p * k} : {q}", f"{p + 1} : {q + 1}"]), "", lv)
def x102_per(b, lv):
    p, q = R.randint(1, 9), R.randint(1, 9)
    if p == q or math.gcd(p, q) != 1: return
    P1 = p * R.randint(3, 12); P2 = F(P1 * q, p)
    if P2.denominator != 1: return
    b.add(f"দুটি সদৃশ ত্রিভুজের অনুরূপ বাহুর অনুপাত {p} : {q}। প্রথমটির পরিসীমা {P1} সেমি হলে দ্বিতীয়টির পরিসীমা কত সেমি?", int(P2), W(int(P2), [P1, int(P2) + q, P1 * q, P1 * p // q if (P1 * p) % q == 0 and P1 * p // q != int(P2) else int(P2) + 1]), "পরিসীমার অনুপাত = বাহুর অনুপাত।", lv)
def x102_ang(b, lv):
    t1, t2 = R.choice(TRI); a, c = R.randint(20, 100), R.randint(20, 100)
    if a + c >= 170: return
    t = R.randrange(2)
    if t == 0: b.add(f"Δ{t1} ~ Δ{t2} এবং ∠{t1[1]} = {a}° হলে ∠{t2[1]} = কত?", ANG(a), W(ANG(a), [ANG(180 - a), ANG(2 * a) if 2 * a < 180 else ANG(a - 10), ANG(90 - a) if a < 90 else ANG(a + 10), ANG(a + 5)]), "অনুরূপ কোণ সমান।", lv)
    else: b.add(f"Δ{t1} ~ Δ{t2}। ∠{t1[0]} = {a}° ও ∠{t2[1]} = {c}° হলে ∠{t1[2]} = কত?", ANG(180 - a - c), W(ANG(180 - a - c), [ANG(a), ANG(c), ANG(a + c), ANG(180 - c)]), f"∠{t1[1]} = ∠{t2[1]} = {c}°।", lv)
def x102_check(b, lv):
    a, c, d = R.sample(range(2, 12), 3); k = R.randint(2, 4)
    if sorted([a, c, d])[0] + sorted([a, c, d])[1] <= max(a, c, d): return
    cc = f"{a * k}, {c * k}, {d * k}"
    w = [f"{a * k}, {c * k}, {d * k + 1}", f"{a + k}, {c + k}, {d + k}", f"{a * k}, {c * k + k}, {d * k}", f"{a * k + 1}, {c * k}, {d * k}"]
    b.add(f"{a} সেমি, {c} সেমি ও {d} সেমি বাহুবিশিষ্ট ত্রিভুজের সদৃশ ত্রিভুজের বাহু (সেমি) কোনটি হতে পারে?", cc, W(cc, w), f"প্রতিটি বাহু {k} গুণ।", lv)
P102 = part('10.2', 150, fx102, [x102_ang, x102_ratio, x102_side], [x102_side, x102_per, x102_check, x102_ang], [x102_per, x102_check, x102_side])

fx103 = [
 ("ΔABC এর AB ও AC বাহুর উপর যথাক্রমে D ও E বিন্দু এবং DE ∥ BC হলে কোনটি সঠিক?", "ΔADE ~ ΔABC", ["ΔADE ≅ ΔABC", "ΔADE ~ ΔBCE", "DE = BC"], "", E),
 ("একই সময়ে দুটি খাড়া বস্তুর উচ্চতা ও তাদের ছায়ার দৈর্ঘ্য কেমন?", "সমানুপাতিক", ["সমান", "ব্যস্তানুপাতিক", "সম্পর্কহীন"], "সূর্যরশ্মির কোণ একই, তাই সদৃশ ত্রিভুজ।", E),
 ("মানচিত্রে স্কেল 1 : 100000 হলে 1 সেমি দূরত্ব প্রকৃতপক্ষে কত?", "1 কিমি", ["100 মিটার", "10 কিমি", "1 মিটার"], "100000 সেমি = 1 কিমি।", M),
]
def y103_shadow(b, lv):
    h1 = R.randint(1, 6); s1 = R.randint(1, 8); k = R.randint(3, 15)
    if math.gcd(h1, s1) != 1: return
    h2, s2 = h1 * k, s1 * k; t = R.randrange(2)
    if t == 0: b.add(f"একই সময়ে {h1} মিটার লম্বা একটি খুঁটির ছায়া {s1} মিটার এবং একটি গাছের ছায়া {s2} মিটার। গাছটির উচ্চতা কত মিটার?", h2, W(h2, [s2, h2 + h1, s2 * s1 // h1 if (s2 * s1) % h1 == 0 and s2 * s1 // h1 != h2 else h2 + 2, h1 * s2]), f"{h1}/{s1} = x/{s2}।", lv)
    else: b.add(f"একই সময়ে {h1} মিটার লম্বা একটি খুঁটির ছায়া {s1} মিটার। {h2} মিটার উঁচু একটি টাওয়ারের ছায়ার দৈর্ঘ্য কত মিটার?", s2, W(s2, [h2, s2 + s1, h2 * h1 // s1 if (h2 * h1) % s1 == 0 and h2 * h1 // s1 != s2 else s2 + 2, s2 - s1]), f"{h1}/{s1} = {h2}/x।", lv)
def y103_par(b, lv):
    ad, db = R.randint(1, 9), R.randint(1, 9); ae = R.randint(1, 9) * ad
    ec = F(ae * db, ad)
    if ec.denominator != 1: return
    b.add(f"ΔABC এর AB ও AC বাহুর উপর যথাক্রমে D ও E বিন্দু এবং DE ∥ BC। AD = {ad} সেমি, DB = {db} সেমি, AE = {ae} সেমি হলে EC = কত সেমি?", int(ec), W(int(ec), [ae, int(ec) + 1, ae + db - ad if ae + db - ad > 0 and ae + db - ad != int(ec) else int(ec) + 2, db]), f"AD/DB = AE/EC।", lv)
def y103_bc(b, lv):
    ad, db = R.randint(1, 9), R.randint(1, 9); de = R.randint(1, 9) * ad
    bc = F(de * (ad + db), ad)
    if bc.denominator != 1: return
    b.add(f"ΔABC এ DE ∥ BC, যেখানে D, AB এর উপর ও E, AC এর উপর। AD = {ad} সেমি, DB = {db} সেমি এবং DE = {de} সেমি হলে BC = কত সেমি?", int(bc), W(int(bc), [de + db, de * db // ad if (de * db) % ad == 0 and de * db // ad != int(bc) else int(bc) + 1, de, int(bc) + ad]), f"DE/BC = AD/AB = {ad}/{ad + db}।", lv)
def y103_map(b, lv):
    k = R.choice([10000, 50000, 100000, 200000, 500000]); d = R.randint(2, 20)
    km = F(d * k, 100000)
    b.add(f"একটি মানচিত্রের স্কেল 1 : {k}। মানচিত্রে দুটি শহরের দূরত্ব {d} সেমি হলে প্রকৃত দূরত্ব কত কিলোমিটার?", D(km), W(D(km), [D(km * 10), D(km / 10), str(d * k), D(km + 1)]), f"{d} × {k} সেমি = {D(km)} কিমি।", lv)
def y103_model(b, lv):
    s = R.choice([20, 25, 40, 50, 100]); h = R.randint(2, 30)
    t = R.randrange(2)
    if t == 0: b.add(f"একটি ভবনের মডেল প্রকৃত ভবনের 1 : {s} অনুপাতে তৈরি। মডেলের উচ্চতা {h} সেমি হলে ভবনের উচ্চতা কত মিটার?", D(F(h * s, 100)), W(D(F(h * s, 100)), [str(h * s), D(F(h * s, 1000)), D(F(h * s, 10)), D(F(h, s))]), f"{h} × {s} = {h * s} সেমি।", lv)
    else:
        H = s * h; b.add(f"{D(F(H, 100))} মিটার উঁচু একটি মিনারের 1 : {s} অনুপাতের মডেল বানালে মডেলের উচ্চতা কত সেমি হবে?", h, W(h, [H, h * 10, h + s, D(F(H, s * 100))]), f"{H} সেমি ÷ {s}।", lv)
def y103_mirror(b, lv):
    e = R.randint(12, 18) * 10; d1 = R.randint(1, 5); d2 = R.randint(2, 30)
    H = F(e * d2, d1 * 100)
    if H.denominator not in (1, 2, 4, 5, 10): return
    b.add(f"একজন লোকের চোখের উচ্চতা {D(F(e, 100))} মিটার। মাটিতে রাখা একটি আয়না থেকে {d1} মিটার দূরে দাঁড়িয়ে তিনি আয়নায় {d2} মিটার দূরের একটি গাছের মাথা দেখলেন। গাছটির উচ্চতা কত মিটার?", D(H), W(D(H), [D(H + 1), D(H + 2), D(H * 2), str(d2)]), f"{D(F(e, 100))}/{d1} = h/{d2}।", lv)
def y103_ratio(b, lv):
    p, q = R.randint(1, 6), R.randint(1, 6)
    if p == q: return
    k = R.randint(2, 6); A = p * k; B = q * k; s = R.randint(2, 12) * p; v = F(s * q, p)
    if v.denominator != 1: return
    b.add(f"দুটি সদৃশ ত্রিভুজের উচ্চতা যথাক্রমে {A} সেমি ও {B} সেমি। প্রথমটির ভূমি {s} সেমি হলে দ্বিতীয়টির ভূমি কত সেমি?", int(v), W(int(v), [s, int(v) + 1, s + B - A if s + B - A > 0 and s + B - A != int(v) else int(v) + 2, s * p // q if (s * p) % q == 0 and s * p // q != int(v) else int(v) + 3]), f"ভূমির অনুপাত = উচ্চতার অনুপাত = {A} : {B}।", lv)
P103 = part('10.3', 150, fx103, [y103_shadow, y103_map, y103_model], [y103_par, y103_bc, y103_ratio, y103_shadow], [y103_mirror, y103_bc, y103_par])
save('v10', P101 + P102 + P103)

# ===================================================== 11 তথ্য ও উপাত্ত (250)
fx11 = [
 ("উপাত্তের সর্বোচ্চ ও সর্বনিম্ন মানের পার্থক্যের সাথে 1 যোগ করলে কী পাওয়া যায়?", "পরিসর", ["গড়", "মধ্যক", "প্রচুরক"], "", E),
 ("উপাত্তে যে মান সবচেয়ে বেশিবার আসে তাকে কী বলে?", "প্রচুরক", ["মধ্যক", "গড়", "পরিসর"], "", E),
 ("উপাত্তগুলোকে মানের ক্রমানুসারে সাজালে মাঝের মানকে কী বলে?", "মধ্যক", ["প্রচুরক", "গড়", "পরিসর"], "", E),
 ("গড় নির্ণয়ের সূত্র কোনটি?", "উপাত্তগুলোর সমষ্টি ÷ উপাত্তের সংখ্যা", ["বৃহত্তম − ক্ষুদ্রতম", "মাঝের মান", "সবচেয়ে বেশিবার আসা মান"], "", E),
 ("কেন্দ্রীয় প্রবণতার পরিমাপ কোনটি নয়?", "পরিসর", ["গড়", "মধ্যক", "প্রচুরক"], "", M),
 ("শ্রেণিবিন্যস্ত উপাত্তে শ্রেণিসংখ্যা নির্ণয়ের সূত্র কোনটি?", "পরিসর ÷ শ্রেণিব্যাপ্তি (পরের পূর্ণসংখ্যা)", ["পরিসর × শ্রেণিব্যাপ্তি", "শ্রেণিব্যাপ্তি ÷ পরিসর", "পরিসর + শ্রেণিব্যাপ্তি"], "", M),
 ("ট্যালি চিহ্নে প্রতি পাঁচটি গণনার পঞ্চমটি কীভাবে দেওয়া হয়?", "আগের চারটি দাগ আড়াআড়ি কেটে", ["নতুন খাড়া দাগ দিয়ে", "বৃত্ত এঁকে", "তারকা দিয়ে"], "", E),
 ("সংখ্যাসূচক তথ্যকে কী বলে?", "উপাত্ত", ["চলক", "শ্রেণি", "গণসংখ্যা"], "", E),
 ("অবিন্যস্ত উপাত্তকে কী বলে?", "কাঁচা উপাত্ত", ["বিন্যস্ত উপাত্ত", "শ্রেণিবদ্ধ উপাত্ত", "গণসংখ্যা"], "", E),
 ("একটি উপাত্তে একাধিক প্রচুরক থাকতে পারে কি?", "হ্যাঁ, পারে", ["না, কখনো না", "শুধু জোড় সংখ্যক উপাত্তে", "শুধু বিজোড় সংখ্যক উপাত্তে"], "", M),
]
def z11_mean(b, lv):
    n = R.randint(3, 8)
    while True:
        xs = [R.randint(1, 90) for _ in range(n)]
        if sum(xs) % n == 0: break
    m = sum(xs) // n
    b.add(f"{', '.join(map(str, xs))} সংখ্যাগুলোর গড় কত?", m, W(m, [m + 1, m - 1, sorted(xs)[n // 2] if sorted(xs)[n // 2] != m else m + 2, sum(xs)]), f"{sum(xs)} ÷ {n} = {m}।", lv)
def z11_median(b, lv):
    n = R.choice([5, 7, 9, 6, 8, 10]); xs = R.sample(range(1, 99), n); s = sorted(xs)
    med = F(s[n // 2]) if n % 2 else F(s[n // 2 - 1] + s[n // 2], 2)
    b.add(f"{', '.join(map(str, xs))} উপাত্তের মধ্যক কত?", D(med), W(D(med), [D(F(xs[n // 2])) if F(xs[n // 2]) != med else D(med + 1), D(F(sum(xs), n)), D(med + 1), D(F(s[0] + s[-1], 2))]), f"সাজালে: {', '.join(map(str, s))}।", lv)
def z11_mode(b, lv):
    base = R.sample(range(1, 80), R.randint(5, 7)); m = R.choice(base)
    xs = base + [m] * R.randint(1, 2); R.shuffle(xs)
    b.add(f"{', '.join(map(str, xs))} উপাত্তের প্রচুরক কত?", m, W(m, [x for x in base if x != m] + [max(xs)]), "সবচেয়ে বেশিবার আসা মান।", lv)
def z11_range(b, lv):
    xs = R.sample(range(1, 150), R.randint(6, 10)); v = max(xs) - min(xs) + 1
    b.add(f"{', '.join(map(str, xs))} উপাত্তের পরিসর কত?", v, W(v, [v - 1, max(xs), max(xs) + min(xs), v + 1]), f"({max(xs)} − {min(xs)}) + 1 = {v}।", lv)
def z11_classes(b, lv):
    lo = R.randint(10, 50); hi = lo + R.randint(30, 90); w = R.choice([5, 10]); r = hi - lo + 1; v = -(-r // w)
    b.add(f"কোনো উপাত্তের সর্বনিম্ন মান {lo} ও সর্বোচ্চ মান {hi}। শ্রেণিব্যাপ্তি {w} হলে শ্রেণিসংখ্যা কত?", v, W(v, [v + 1, v - 1, r, r // w if r // w != v else v + 2]), f"পরিসর {r}; {r}/{w} এর পরের পূর্ণসংখ্যা {v}।", lv)
def z11_sort(b, lv):
    xs = R.sample(range(1, 99), 6); s = sorted(xs); c = ', '.join(map(str, s))
    w = [', '.join(map(str, sorted(xs, reverse=True))), ', '.join(map(str, s[:2] + [s[3], s[2]] + s[4:])), ', '.join(map(str, sorted(xs, key=lambda v: v % 10)))]
    b.add(f"{', '.join(map(str, xs))} উপাত্তকে মানের ঊর্ধ্বক্রমে সাজালে কোনটি হবে?", c, W(c, w + [', '.join(map(str, s[1:] + s[:1]))]), "", lv)
def z11_tally(b, lv):
    n = R.randint(6, 33); f, r = divmod(n, 5)
    s = '  '.join(['||||/'] * f + (['|' * r] if r else []))
    b.add(f"ট্যালি চিহ্ন  {s}  দ্বারা কোন সংখ্যা বোঝায়? (||||/ = আড়াআড়ি কাটা চারটি দাগ, অর্থাৎ 5)", n, W(n, [n + 1, n - 1, f + r, n + 5]), "প্রতিটি কাটা গুচ্ছ = 5।", lv)
def z11_freq(b, lv):
    vals = R.sample(range(1, 10), 3); xs = [R.choice(vals) for _ in range(R.randint(10, 18))]
    t = R.choice(vals); v = xs.count(t)
    if v == 0: return
    b.add(f"{', '.join(map(str, xs))} উপাত্তে {t} সংখ্যাটির গণসংখ্যা কত?", v, W(v, [v + 1, max(0, v - 1), len(xs), v + 2]), "কতবার এসেছে গুনে দেখো।", lv)
def z11_classf(b, lv):
    lo = R.choice([20, 30, 40, 50]); w = 10; xs = [R.randint(lo, lo + 49) for _ in range(R.randint(12, 18))]
    k = R.randrange(5); a = lo + k * w; v = sum(1 for x in xs if a <= x <= a + w - 1)
    b.add(f"{', '.join(map(str, xs))} উপাত্তে {a} − {a + w - 1} শ্রেণির গণসংখ্যা কত?", v, W(v, [v + 1, max(0, v - 1), v + 2, len(xs) // 5 if len(xs) // 5 != v else v + 3]), "শ্রেণিসীমার মধ্যে থাকা মান গোনো।", lv)
def z11_missing(b, lv):
    n = R.randint(4, 8); m = R.randint(10, 70)
    xs = [R.randint(1, 99) for _ in range(n - 1)]; last = m * n - sum(xs)
    if last <= 0 or last > 200: return
    b.add(f"{n}টি সংখ্যার গড় {m}। এর {n - 1}টি সংখ্যা {', '.join(map(str, xs))} হলে অপর সংখ্যাটি কত?", last, W(last, [last + 1, m, last - n, m * n]), "মোট = গড় × সংখ্যা।", lv)
def z11_total(b, lv):
    n = R.randint(5, 60); m = R.randint(20, 95)
    b.add(f"একটি শ্রেণির {n} জন শিক্ষার্থীর গড় নম্বর {m}। তাদের মোট নম্বর কত?", n * m, W(n * m, [n + m, n * m + n, n * m - m, m * 10]), "গড় × সংখ্যা।", lv)
def z11_combined(b, lv):
    n1, n2 = R.randint(5, 40), R.randint(5, 40); m1, m2 = R.randint(20, 95), R.randint(20, 95)
    v = F(n1 * m1 + n2 * m2, n1 + n2)
    if v.denominator not in (1, 2, 4, 5, 10, 20, 25, 50) or m1 == m2: return
    b.add(f"{n1} জন শিক্ষার্থীর গড় নম্বর {m1} এবং অন্য {n2} জনের গড় নম্বর {m2} হলে সকলের গড় নম্বর কত?", D(v), W(D(v), [D(F(m1 + m2, 2)), D(v + 1), D(v - 1), D(v + 2)]), "মোট নম্বর ÷ মোট শিক্ষার্থী।", lv)
def z11_change(b, lv):
    n = R.randint(4, 12); m = R.randint(15, 60); x = R.randint(1, 120)
    tot = n * m + x
    if tot % (n + 1): return
    v = tot // (n + 1)
    b.add(f"{n}টি সংখ্যার গড় {m}। এদের সাথে {x} যোগ করলে নতুন গড় কত হবে?", v, W(v, [m, v + 1, (n * m + x) // n if (n * m + x) // n != v else v - 1, m + x]), "নতুন সমষ্টি ÷ নতুন সংখ্যা।", lv)
def z11_wrong(b, lv):
    n = R.randint(5, 40); m = R.randint(20, 80); a, c = R.randint(10, 99), R.randint(10, 99)
    if a == c: return
    v = F(n * m - a + c, n)
    if v.denominator not in (1, 2, 4, 5, 10): return
    b.add(f"{n}টি সংখ্যার গড় {m}। পরে দেখা গেল একটি সংখ্যা {c} এর স্থলে ভুলে {a} ধরা হয়েছিল। সঠিক গড় কত?", D(v), W(D(v), [m, D(v + 1), D(F(n * m + a - c, n)), D(v - 1)]), f"সঠিক সমষ্টি = {n * m} − {a} + {c}।", lv)
def z11_bar(b, lv):
    days = ['শনি', 'রবি', 'সোম', 'মঙ্গল', 'বুধ']; xs = R.sample(range(10, 60), 5)
    ask = R.randrange(3)
    desc = ', '.join(f"{d}বার {x}" for d, x in zip(days, xs))
    if ask == 0: c = days[xs.index(max(xs))] + 'বার'; q = 'কোন দিন সবচেয়ে বেশি শিক্ষার্থী উপস্থিত ছিল?'; w = [d + 'বার' for d in days]
    elif ask == 1: c = str(sum(xs)); q = 'পাঁচ দিনে মোট কতজন উপস্থিত ছিল?'; w = [str(sum(xs) + 10), str(max(xs) * 5), str(sum(xs) - min(xs))]
    else: c = str(max(xs) - min(xs)); q = 'সর্বোচ্চ ও সর্বনিম্ন উপস্থিতির পার্থক্য কত?'; w = [str(max(xs)), str(max(xs) + min(xs)), str(max(xs) - min(xs) + 1)]
    b.add(f"একটি আয়তলেখে পাঁচ দিনের উপস্থিতি দেখানো হয়েছে: {desc} জন। {q}", c, W(c, w), "", lv)
K11 = part(None, 250, fx11, [z11_mean, z11_median, z11_mode, z11_range, z11_sort, z11_tally, z11_freq], [z11_mean, z11_median, z11_classes, z11_classf, z11_missing, z11_total, z11_bar, z11_range], [z11_combined, z11_change, z11_wrong, z11_missing])
save('v11', K11)
