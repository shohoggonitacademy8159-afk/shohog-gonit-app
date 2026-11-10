#!/usr/bin/env python3
"""৫ম শ্রেণি গণিত (p5)। প্রতিটি অধ্যায়ে 150টি MCQ (সহজ 75, মধ্যম 60, কঠিন 15)। আউটপুট: chw1.json … chw10.json
১ গুণ ও ভাগ · ২ গাণিতিক বাক্য · ৩ গুণিতক ও গুণনীয়ক · ৪ সাধারণ ভগ্নাংশ · ৫ দশমিক ভগ্নাংশ · ৬ শতকরা · ৭ গড় · ৮ পরিমাপ · ৯ জ্যামিতি · ১০ উপাত্ত বিন্যস্তকরণ"""
import random, pathlib, sys, math
from fractions import Fraction as F
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from mcqlib import Bank, save as _save, E, M, H, fr, num, pfmt, pmul, padd, pscale, ppow, lin, sup

R = random.Random(2026110705)
import re as _re
def _clean(t):
    t = _re.sub(r'\^(\d+)', lambda m: m.group(1).translate(str.maketrans('0123456789', '⁰¹²³⁴⁵⁶⁷⁸⁹')), t)
    t = _re.sub(r'(?<![\d.])(\d+)/1(?![\d.])', r'\1', t)
    return t
_BN = str.maketrans('0123456789', '০১২৩৪৫৬৭৮৯')   # ৫ম শ্রেণি: সব সংখ্যা বাংলায়
def save(ch, items):
    for x in items:
        x['q'] = _clean(x['q']).translate(_BN); x['o'] = [_clean(o).translate(_BN) for o in x['o']]; x['e'] = _clean(x['e']).translate(_BN)
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

TOT = 150
def IND(n):
    s = str(n); out = []; first = True
    while s:
        k = 3 if first else 2; out.insert(0, s[-k:]); s = s[:-k]; first = False
    return ','.join(out)
def tk_(v): return f"{IND(v)} টাকা"

# ===================================================== ১ গুণ ও ভাগ
fx1 = [
 ("কোনো সংখ্যাকে 1 দিয়ে গুণ করলে গুণফল কী হয়?", "সংখ্যাটিই", ["1", "0", "সংখ্যাটির দ্বিগুণ"], "", E),
 ("কোনো সংখ্যাকে 0 দিয়ে গুণ করলে গুণফল কত?", "0", ["1", "সংখ্যাটিই", "10"], "", E),
 ("ভাজ্য = কত?", "ভাজক × ভাগফল + ভাগশেষ", ["ভাজক + ভাগফল", "ভাগফল − ভাগশেষ", "ভাজক ÷ ভাগফল"], "", E),
 ("ভাগশেষ সবসময় কোনটি অপেক্ষা ছোট হয়?", "ভাজক", ["ভাগফল", "ভাজ্য", "1"], "", E),
 ("0 কে যেকোনো অশূন্য সংখ্যা দিয়ে ভাগ করলে ভাগফল কত?", "0", ["1", "সংখ্যাটিই", "অসংজ্ঞায়িত"], "", E),
 ("কোনো সংখ্যাকে 100 দিয়ে গুণ করলে সংখ্যাটির ডানে কয়টি শূন্য বসে?", "2টি", ["1টি", "3টি", "কোনোটিই না"], "", E),
]
def g1_mul(b, lv):
    a = R.randint(101, 999); c = R.randint(11, 99) if lv == E else R.randint(101, 999); v = a * c
    b.add(f"{a} × {c} = কত?", IND(v), W(IND(v), [IND(v + 10), IND(v - 100), IND(a * (c + 1)), IND(v + a // 10 * 10 if a // 10 * 10 else v + 1)]), "", lv)
def g1_div(b, lv):
    d = R.randint(12, 99); q = R.randint(21, 999); v = d * q
    b.add(f"{IND(v)} ÷ {d} = কত?", q, W(q, [q + 1, q - 1, q + 10, q * 10 if q * 10 < 10000 else q - 10]), f"{d} × {q} = {v}।", lv)
def g1_rem(b, lv):
    d = R.randint(6, 99); q = R.randint(20, 999); r = R.randint(1, d - 1); n = d * q + r
    t = R.randrange(2)
    if t == 0: b.add(f"{IND(n)} কে {d} দিয়ে ভাগ করলে ভাগশেষ কত?", r, W(r, [r + 1, d - r if d - r != r else r + 2, q % d if q % d != r else r + 3, 0]), f"{d} × {q} = {d * q}; {n} − {d * q} = {r}।", lv)
    else: b.add(f"{IND(n)} কে {d} দিয়ে ভাগ করলে ভাগফল কত?", q, W(q, [q + 1, q - 1, q + 10, r]), f"{d} × {q} + {r} = {n}।", lv)
def g1_dividend(b, lv):
    d = R.randint(12, 99); q = R.randint(25, 500); r = R.randint(1, d - 1); n = d * q + r
    b.add(f"ভাজক {d}, ভাগফল {q} এবং ভাগশেষ {r} হলে ভাজ্য কত?", IND(n), W(IND(n), [IND(d * q), IND(d * q - r), IND(n + d), IND(d + q + r)]), "ভাজ্য = ভাজক × ভাগফল + ভাগশেষ।", lv)
def g1_divisor(b, lv):
    d = R.randint(12, 99); q = R.randint(25, 500); r = R.randint(1, d - 1); n = d * q + r
    b.add(f"ভাজ্য {IND(n)}, ভাগফল {q} এবং ভাগশেষ {r} হলে ভাজক কত?", d, W(d, [d + 1, d - 1, q, r + d]), f"({n} − {r}) ÷ {q} = {d}।", lv)
def g1_ten(b, lv):
    a = R.randint(12, 9999); k = R.choice([10, 100, 1000]); t = R.randrange(2)
    if t == 0: v = a * k; b.add(f"{IND(a)} × {IND(k)} = কত?", IND(v), W(IND(v), [IND(a * k // 10), IND(a * k * 10), IND(a + k), IND(v + k)]), "", lv)
    else:
        v = a * k; b.add(f"{IND(v)} ÷ {IND(k)} = কত?", IND(a), W(IND(a), [IND(a * 10), IND(a // 10) if a >= 100 else IND(a + 10), IND(v - k), IND(a + 1)]), "", lv)
def g1_cost(b, lv):
    n = R.randint(12, 250); p = R.randint(12, 450); t = R.randrange(2)
    it, g = R.choice([('খাতা', 'খাতার'), ('কলম', 'কলমের'), ('বই', 'বইয়ের'), ('চেয়ার', 'চেয়ারের'), ('ব্যাগ', 'ব্যাগের'), ('ছাতা', 'ছাতার')])
    if t == 0: b.add(f"একটি {g} দাম {p} টাকা হলে {n}টি {g} দাম কত টাকা?", IND(n * p), W(IND(n * p), [IND(n + p), IND(n * p + p), IND(n * p - n), IND((n + 1) * p + 10)]), f"{n} × {p}।", lv)
    else: b.add(f"{n}টি {g} দাম {IND(n * p)} টাকা হলে একটি {g} দাম কত টাকা?", p, W(p, [p + 1, p - 1, p + 10, n]), f"{n * p} ÷ {n}।", lv)
def g1_share(b, lv):
    n = R.randint(5, 60); per = R.randint(12, 300); r = R.randint(1, n - 1); tot = n * per + r
    b.add(f"{IND(tot)}টি চকলেট {n} জন শিশুর মধ্যে সমানভাবে ভাগ করে দিলে প্রত্যেকে সর্বোচ্চ কয়টি করে পাবে এবং কয়টি অবশিষ্ট থাকবে?", f"{per}টি; {r}টি", W(f"{per}টি; {r}টি", [f"{per + 1}টি; {r}টি", f"{per}টি; {r + 1}টি", f"{per - 1}টি; {r + n}টি", f"{r}টি; {per}টি"]), f"{tot} ÷ {n} = {per}, ভাগশেষ {r}।", lv)
def g1_extreme(b, lv):
    d = R.randint(3, 5); k = R.randint(11, 97); t = R.randrange(2)
    if t == 0:
        v = (10 ** d - 1) // k * k
        b.add(f"{d} অঙ্কের বৃহত্তম কোন সংখ্যা {k} দ্বারা নিঃশেষে বিভাজ্য?", IND(v), W(IND(v), [IND(10 ** d - 1), IND(v - k), IND(v + k) if v + k < 10 ** d else IND(v - 2 * k), IND(v - 1)]), f"{IND(10 ** d - 1)} কে {k} দিয়ে ভাগ করে ভাগশেষ বাদ।", lv)
    else:
        v = -(-(10 ** (d - 1)) // k) * k
        b.add(f"{d} অঙ্কের ক্ষুদ্রতম কোন সংখ্যা {k} দ্বারা নিঃশেষে বিভাজ্য?", IND(v), W(IND(v), [IND(10 ** (d - 1)), IND(v + k), IND(v - k) if v - k >= 10 ** (d - 1) else IND(v + 2 * k), IND(v + 1)]), "", lv)
def g1_two(b, lv):
    a, c = R.randint(10, 99), R.randint(10, 99); p, q = R.randint(5, 40), R.randint(5, 40)
    v = a * p + c * q
    b.add(f"প্রতিটি {p} টাকা দরে {a}টি কলম এবং প্রতিটি {q} টাকা দরে {c}টি পেনসিল কেনা হলো। মোট কত টাকা লাগল?", IND(v), W(IND(v), [IND((a + c) * (p + q)), IND(a * q + c * p) if a * q + c * p != v else IND(v + 10), IND(v + p), IND(a * p)]), f"{a * p} + {c * q}।", lv)
def g1_rows(b, lv):
    r_, c = R.randint(12, 60), R.randint(12, 60); t = R.randrange(2)
    if t == 0: b.add(f"একটি হলরুমে {r_}টি সারিতে প্রতি সারিতে {c}টি করে চেয়ার আছে। মোট চেয়ার কয়টি?", IND(r_ * c), W(IND(r_ * c), [IND(r_ + c), IND(r_ * c + r_), IND(r_ * c - c), IND((r_ + 1) * (c - 1))]), "", lv)
    else: b.add(f"{IND(r_ * c)}টি চারাগাছ {r_}টি সারিতে সমান সংখ্যায় লাগালে প্রতি সারিতে কয়টি গাছ থাকবে?", c, W(c, [c + 1, c - 1, r_, c + 10]), "", lv)
P1 = part(None, TOT, fx1, [g1_mul, g1_div, g1_ten, g1_cost, g1_rows], [g1_rem, g1_dividend, g1_share, g1_two, g1_mul], [g1_divisor, g1_extreme, g1_share])
save('w1', P1)

# ===================================================== ২ গাণিতিক বাক্য (সরলীকরণ)
fx2 = [
 ("সরলীকরণে কোন ক্রমে কাজ করতে হয়?", "বন্ধনী, ভাগ, গুণ, যোগ, বিয়োগ", ["যোগ, বিয়োগ, গুণ, ভাগ", "গুণ, ভাগ, বন্ধনী, যোগ", "বাম থেকে ডানে সব একসাথে"], "", E),
 ("প্রথম বন্ধনীর চিহ্ন কোনটি?", "( )", ["{ }", "[ ]", "| |"], "", E),
 ("দ্বিতীয় বন্ধনীর চিহ্ন কোনটি?", "{ }", ["( )", "[ ]", "< >"], "", E),
 ("তৃতীয় বন্ধনীর চিহ্ন কোনটি?", "[ ]", ["( )", "{ }", "/ /"], "", E),
 ("একাধিক বন্ধনী থাকলে প্রথমে কোন বন্ধনীর কাজ করতে হয়?", "প্রথম বন্ধনী ( )", ["দ্বিতীয় বন্ধনী { }", "তৃতীয় বন্ধনী [ ]", "যেকোনোটি"], "", E),
]
def s2_ops(b, lv):
    a, c, d = R.randint(10, 99), R.randint(2, 12), R.randint(2, 12)
    t = R.randrange(4)
    if t == 0: v = a + c * d; q = f"{a} + {c} × {d} = কত?"; w = [(a + c) * d, a * c + d, v + 1]
    elif t == 1:
        if a - c * d < 0: return
        v = a - c * d; q = f"{a} − {c} × {d} = কত?"; w = [(a - c) * d, abs(a * c - d), v + 2]
    elif t == 2: x = c * d; v = a + x // c; q = f"{a} + {x} ÷ {c} = কত?"; w = [(a + x) // c if (a + x) % c == 0 else v + 3, a + x, v - 1]
    else: x = c * d; v = x // c * R.randint(2, 9); k = v // (x // c); q = f"{x} ÷ {c} × {k} = কত?"; w = [x // (c * k) if x % (c * k) == 0 else v + 1, v + k, x * k]
    b.add(q, v, W(v, w), "আগে গুণ/ভাগ, পরে যোগ/বিয়োগ।", lv)
def s2_br(b, lv):
    a, c, d, e = R.randint(10, 60), R.randint(2, 20), R.randint(2, 9), R.randint(1, 30)
    v = a + (c + e) * d; t = R.randrange(2)
    if t == 0: b.add(f"{a} + ({c} + {e}) × {d} = কত?", v, W(v, [a + c + e * d, (a + c + e) * d, v + d, v - d]), "আগে বন্ধনী।", lv)
    else:
        if a * d - c < 0: return
        v = (a - c) * d if a > c else None
        if v is None: return
        b.add(f"({a} − {c}) × {d} = কত?", v, W(v, [a - c * d if a - c * d > 0 else v + 2, a * d - c, v + d, v - c]), "", lv)
def s2_nest(b, lv):
    a, c, d, e, f = R.randint(40, 120), R.randint(10, 40), R.randint(2, 6), R.randint(2, 9), R.randint(1, 9)
    inner = e - f
    if inner <= 0: return
    mid = c - d * inner
    if mid <= 0: return
    v = a - mid
    if v <= 0: return
    b.add(f"{a} − [{c} − {{{d} × ({e} − {f})}}] = কত?", v, W(v, [a - c - d * inner, a - c + d * e - f, v + 2 * d, v - inner]), "ভিতরের বন্ধনী থেকে শুরু।", lv)
def s2_word(b, lv):
    a, c, d = R.randint(2, 20), R.randint(2, 20), R.randint(2, 9)
    t = R.randrange(3)
    if t == 0: c0 = f"({a} + {c}) × {d}"; q = f"{a} ও {c} এর যোগফলকে {d} দিয়ে গুণ করার গাণিতিক বাক্য কোনটি?"; w = [f"{a} + {c} × {d}", f"{a} × {d} + {c}", f"({a} × {c}) + {d}"]
    elif t == 1: c0 = f"({a * d} − {c}) ÷ {d}" ; q = f"{a * d} থেকে {c} বিয়োগ করে বিয়োগফলকে {d} দিয়ে ভাগ করার গাণিতিক বাক্য কোনটি?"; w = [f"{a * d} − {c} ÷ {d}", f"{a * d} ÷ {d} − {c}", f"({a * d} ÷ {c}) − {d}"]
    else: c0 = f"{a} × {c} − {d}"; q = f"{a} ও {c} এর গুণফল থেকে {d} বিয়োগ করার গাণিতিক বাক্য কোনটি?"; w = [f"{a} × ({c} − {d})", f"({a} − {d}) × {c}", f"{a} + {c} − {d}"]
    b.add(q, c0, W(c0, w), "", lv)
def s2_story(b, lv):
    tot = R.randint(200, 900); p = R.randint(5, 40); n = R.randint(2, 9)
    if tot - p * n <= 0: return
    v = tot - p * n
    b.add(f"রিনার কাছে {tot} টাকা ছিল। সে প্রতিটি {p} টাকা দরে {n}টি খাতা কিনল। তার কাছে কত টাকা রইল?", v, W(v, [tot - p - n, (tot - p) * n if (tot - p) * n < 10000 else v + 10, tot - p * n + p, p * n]), f"{tot} − {p} × {n}।", lv)
def s2_frac(b, lv):
    a, c = R.randint(2, 9), R.randint(2, 9); d = R.randint(2, 9) * a * c
    v = d // a + d // c
    b.add(f"{d} ÷ {a} + {d} ÷ {c} = কত?", v, W(v, [d // (a + c) if d % (a + c) == 0 else v + 1, d * 2 // (a * c), v - 1, (d // a) * (d // c) if (d // a) * (d // c) < 5000 else v + 5]), "আগে দুটি ভাগ, পরে যোগ।", lv)
def s2_true(b, lv):
    a, c, d = R.randint(2, 15), R.randint(2, 15), R.randint(2, 9)
    good = f"{a} + {c} × {d} = {a + c * d}"
    bad = [f"{a} + {c} × {d} = {(a + c) * d}", f"({a} + {c}) × {d} = {a + c * d}", f"{a} × {d} + {c} = {(a + c) * d}" if a * d + c != (a + c) * d else f"{a} × {c} + {d} = {a * c + d + 1}"]
    b.add("নিচের কোন গাণিতিক বাক্যটি সঠিক?", good, W(good, bad + [f"{a} + {c} × {d} = {a + c * d + 1}"]), "", lv)
def s2_long(b, lv):
    a, c, d, e = R.randint(2, 9), R.randint(2, 9), R.randint(2, 9), R.randint(2, 9)
    x = a * c * d
    v = x // c - d + e * a
    if v <= 0: return
    b.add(f"{x} ÷ {c} − {d} + {e} × {a} = কত?", v, W(v, [x // (c - d) if c != d and x % (c - d) == 0 and c > d else v + 2, (x // c - d + e) * a, v - 2 * a, v + d]), "ভাগ ও গুণ আগে, পরে বাম থেকে যোগ-বিয়োগ।", lv)
P2 = part(None, TOT, fx2, [s2_ops, s2_br, s2_word, s2_true], [s2_story, s2_frac, s2_br, s2_long, s2_ops], [s2_nest, s2_long])
save('w2', P2)

# ===================================================== ৩ গুণিতক ও গুণনীয়ক
fx3 = [
 ("যে সংখ্যার 1 ও ঐ সংখ্যা ছাড়া অন্য কোনো গুণনীয়ক নেই, তাকে কী বলে?", "মৌলিক সংখ্যা", ["যৌগিক সংখ্যা", "জোড় সংখ্যা", "বিজোড় সংখ্যা"], "", E),
 ("ক্ষুদ্রতম মৌলিক সংখ্যা কোনটি?", "2", ["1", "3", "0"], "", E),
 ("একমাত্র জোড় মৌলিক সংখ্যা কোনটি?", "2", ["4", "6", "0"], "", E),
 ("1 সংখ্যাটি কী?", "মৌলিকও নয়, যৌগিকও নয়", ["মৌলিক", "যৌগিক", "জোড়"], "", E),
 ("দুটি সংখ্যার গুণফল = কত?", "সংখ্যা দুটির গ.সা.গু. × ল.সা.গু.", ["গ.সা.গু. + ল.সা.গু.", "ল.সা.গু. ÷ গ.সা.গু.", "গ.সা.গু. − ল.সা.গু."], "", M),
 ("কোনো সংখ্যার অঙ্কগুলোর যোগফল 3 দ্বারা বিভাজ্য হলে সংখ্যাটি কোন সংখ্যা দ্বারা বিভাজ্য?", "3", ["2", "5", "4"], "", E),
 ("কোনো সংখ্যার একক স্থানে 0 বা 5 থাকলে সংখ্যাটি কোন সংখ্যা দ্বারা বিভাজ্য?", "5", ["2", "3", "9"], "", E),
]
PR = [p for p in range(2, 200) if all(p % d for d in range(2, int(p ** .5) + 1))]
def pf3(n):
    out, d = [], 2
    while n > 1:
        while n % d == 0: out.append(d); n //= d
        d += 1
    return out
def m3_prime(b, lv):
    p = R.choice([x for x in PR if 10 < x < 100]); w = R.sample([x for x in range(21, 100, 2) if x not in PR], 3)
    b.add("নিচের কোনটি মৌলিক সংখ্যা?", p, W(p, w), "", lv)
def m3_comp(b, lv):
    c = R.choice([x for x in range(21, 100, 2) if x not in PR]); w = R.sample([x for x in PR if 10 < x < 100], 3)
    b.add("নিচের কোনটি যৌগিক সংখ্যা?", c, W(c, w), f"{c} = {' × '.join(map(str, pf3(c)))}।", lv)
def m3_nfac(b, lv):
    n = R.randint(12, 100); v = sum(1 for d in range(1, n + 1) if n % d == 0)
    if v < 4: return
    b.add(f"{n} এর গুণনীয়ক কয়টি?", v, W(v, [v + 1, v - 1, v + 2, v - 2]), f"{n} এর গুণনীয়ক: {', '.join(str(d) for d in range(1, n + 1) if n % d == 0)}।", lv)
def m3_mult(b, lv):
    k = R.randint(3, 15); i = R.randint(3, 10); v = k * i
    b.add(f"{k} এর {i}তম গুণিতক কোনটি?" if False else f"নিচের কোনটি {k} এর গুণিতক?", v, W(v, [v + 1, v - 1, v + 2, v + k // 2 if k > 2 else v + 3]), "", lv)
def m3_hcf(b, lv):
    g = R.randint(2, 20); a, c = R.sample(range(2, 12), 2)
    if math.gcd(a, c) != 1: return
    A, C = g * a, g * c
    b.add(f"{A} ও {C} এর গ.সা.গু. কত?", g, W(g, [g * 2, A * C // g, g + 1, a * c]), "", lv)
def m3_lcm(b, lv):
    a, c = R.sample(range(4, 40), 2); l = a * c // math.gcd(a, c)
    if l > 600: return
    b.add(f"{a} ও {c} এর ল.সা.গু. কত?", l, W(l, [a * c if a * c != l else l * 2, math.gcd(a, c), l + a, l // 2 if l % 2 == 0 and l // 2 not in (a, c) else l + c]), "", lv)
def m3_lcm3(b, lv):
    xs = R.sample(range(2, 16), 3); l = xs[0]
    for x in xs[1:]: l = l * x // math.gcd(l, x)
    if l > 1000: return
    g = math.gcd(math.gcd(xs[0], xs[1]), xs[2])
    b.add(f"{xs[0]}, {xs[1]} ও {xs[2]} এর ল.সা.গু. কত?", l, W(l, [xs[0] * xs[1] * xs[2] if xs[0] * xs[1] * xs[2] != l else l * 2, l + xs[0], g, l * 2 if l * 2 != xs[0] * xs[1] * xs[2] else l * 3]), "", lv)
def m3_hcf3(b, lv):
    g = R.randint(2, 15); xs = R.sample(range(2, 15), 3)
    if math.gcd(math.gcd(xs[0], xs[1]), xs[2]) != 1: return
    ns = [g * x for x in xs]
    b.add(f"{ns[0]}, {ns[1]} ও {ns[2]} এর গ.সা.গু. কত?", g, W(g, [g * 2, g + 1, min(ns), g * xs[0]]), "", lv)
def m3_pf(b, lv):
    n = R.randint(24, 500); f = pf3(n)
    if len(f) < 3 or max(f) > 13: return
    c = ' × '.join(map(str, f)); fx = f[:]; fx[-1] = fx[-1] + 1 if fx[-1] + 1 not in (4, 6, 8, 9, 10) else fx[-1] + 2
    b.add(f"{n} কে মৌলিক উৎপাদকে প্রকাশ করলে কোনটি হবে?", c, W(c, [' × '.join(map(str, fx)), ' × '.join(map(str, f[:-1])), ' × '.join(map(str, f + [2])), ' × '.join(map(str, [f[0] * f[1]] + f[2:]))]), "", lv)
def m3_prod(b, lv):
    g = R.randint(2, 12); a, c = R.sample(range(2, 10), 2)
    if math.gcd(a, c) != 1: return
    A, C = g * a, g * c; l = g * a * c; t = R.randrange(2)
    if t == 0: b.add(f"দুটি সংখ্যার গ.সা.গু. {g} এবং ল.সা.গু. {l}। একটি সংখ্যা {A} হলে অপরটি কত?", C, W(C, [l // g, A, C + g, l - A]), f"অপর সংখ্যা = ({g} × {l}) ÷ {A}।", lv)
    else: b.add(f"দুটি সংখ্যার গুণফল {A * C} এবং গ.সা.গু. {g} হলে ল.সা.গু. কত?", l, W(l, [A * C * g if A * C * g < 100000 else l + g, A * C, l // 2 if l % 2 == 0 else l + 1, l + g]), "ল.সা.গু. = গুণফল ÷ গ.সা.গু.।", lv)
def m3_bell(b, lv):
    xs = R.sample([4, 5, 6, 8, 9, 10, 12, 15, 18, 20], 3); l = xs[0]
    for x in xs[1:]: l = l * x // math.gcd(l, x)
    if l > 180: return
    b.add(f"তিনটি ঘণ্টা যথাক্রমে {xs[0]}, {xs[1]} ও {xs[2]} মিনিট পরপর বাজে। একসাথে বাজার কত মিনিট পর আবার একসাথে বাজবে?", l, W(l, [sum(xs), xs[0] * xs[1] * xs[2] if xs[0] * xs[1] * xs[2] != l else l * 2, l // 2 if l % 2 == 0 else l + 10, max(xs)]), "ল.সা.গু.।", lv)
def m3_rem(b, lv):
    xs = R.sample([4, 5, 6, 8, 9, 10, 12, 15], 2); r = R.randint(1, min(xs) - 1); l = xs[0] * xs[1] // math.gcd(xs[0], xs[1])
    v = l + r
    b.add(f"কোন ক্ষুদ্রতম সংখ্যাকে {xs[0]} ও {xs[1]} দিয়ে ভাগ করলে প্রতিক্ষেত্রে {r} অবশিষ্ট থাকে?", v, W(v, [l, l - r, l + r + 1, xs[0] * xs[1] + r if xs[0] * xs[1] + r != v else v + l]), f"ল.সা.গু. {l} + {r}।", lv)
def m3_big(b, lv):
    g = R.randint(3, 25); a, c = R.sample(range(3, 15), 2)
    if math.gcd(a, c) != 1: return
    r = R.randint(1, g - 1) if g > 2 else 1
    A, C = g * a + r, g * c + r
    b.add(f"কোন বৃহত্তম সংখ্যা দিয়ে {A} ও {C} কে ভাগ করলে প্রতিক্ষেত্রে {r} অবশিষ্ট থাকে?", g, W(g, [g + r, g * 2, math.gcd(A, C) if math.gcd(A, C) != g else g + 1, g - 1]), f"{A - r} ও {C - r} এর গ.সা.গু.।", lv)
P3 = part(None, TOT, fx3, [m3_prime, m3_comp, m3_hcf, m3_lcm, m3_mult], [m3_nfac, m3_pf, m3_lcm3, m3_hcf3, m3_prod, m3_bell], [m3_rem, m3_big, m3_prod])
save('w3', P3)

# ===================================================== ৪ সাধারণ ভগ্নাংশ
fx4 = [
 ("যে ভগ্নাংশের লব হর অপেক্ষা ছোট, তাকে কী বলে?", "প্রকৃত ভগ্নাংশ", ["অপ্রকৃত ভগ্নাংশ", "মিশ্র ভগ্নাংশ", "দশমিক ভগ্নাংশ"], "", E),
 ("যে ভগ্নাংশের লব হর অপেক্ষা বড়, তাকে কী বলে?", "অপ্রকৃত ভগ্নাংশ", ["প্রকৃত ভগ্নাংশ", "লঘিষ্ঠ ভগ্নাংশ", "সমহর ভগ্নাংশ"], "", E),
 ("ভগ্নাংশের লব ও হরকে একই অশূন্য সংখ্যা দিয়ে গুণ করলে ভগ্নাংশের মানের কী হয়?", "অপরিবর্তিত থাকে", ["বাড়ে", "কমে", "দ্বিগুণ হয়"], "", E),
 ("ভিন্ন হরবিশিষ্ট ভগ্নাংশ যোগ করতে প্রথমে কী করতে হয়?", "হরগুলোর ল.সা.গু. নিয়ে সমহর করতে হয়", ["লবগুলো যোগ করতে হয়", "হরগুলো যোগ করতে হয়", "লব ও হর গুণ করতে হয়"], "", E),
 ("একটি ভগ্নাংশকে অন্য একটি ভগ্নাংশ দিয়ে ভাগ করতে কী করতে হয়?", "ভাজক ভগ্নাংশটি উল্টিয়ে গুণ করতে হয়", ["লবকে লব দিয়ে ভাগ করতে হয়", "হরগুলো যোগ করতে হয়", "দুটিই উল্টাতে হয়"], "", M),
]
def FR(x): return mixed(x) if R.random() < 0 else fr(x)
def f4_simp(b, lv):
    p, q = R.randint(1, 15), R.randint(2, 20); k = R.randint(2, 12)
    if math.gcd(p, q) != 1 or p >= q: return
    b.add(f"{p * k}/{q * k} এর লঘিষ্ঠ আকার কোনটি?", f"{p}/{q}", W(f"{p}/{q}", [f"{q}/{p}", f"{p * 2}/{q}" if math.gcd(2 * p, q) == 1 else f"{p + 1}/{q}", f"{p}/{q + 1}", f"{p * k}/{q}"]), f"লব ও হরকে {k} দিয়ে ভাগ।", lv)
def f4_add(b, lv):
    a, c, d, e = R.randint(1, 9), R.randint(2, 12), R.randint(1, 9), R.randint(2, 12)
    x, y = F(a, c), F(d, e); s_ = R.choice(['+', '−'])
    if x.numerator != a or y.numerator != d: return
    v = x + y if s_ == '+' else x - y
    if v <= 0: return
    b.add(f"{a}/{c} {s_} {d}/{e} = কত?", fr(v), W(fr(v), [f"{a + d if s_ == '+' else abs(a - d)}/{c + e}", fr(x - y if s_ == '+' else x + y) if x - y > 0 or s_ == '−' else fr(v + 1), fr(v * 2), fr(x * y)]), "হরগুলোর ল.সা.গু. নিয়ে সমহর করো।", lv)
def f4_mul(b, lv):
    a, c, d, e = R.randint(1, 9), R.randint(2, 12), R.randint(1, 9), R.randint(2, 12)
    if math.gcd(a, c) != 1 or math.gcd(d, e) != 1: return
    v = F(a, c) * F(d, e)
    b.add(f"{a}/{c} × {d}/{e} = কত?", fr(v), W(fr(v), [fr(F(a, c) + F(d, e)), fr(F(a * e, c * d)), f"{a * d}/{c + e}", fr(v * 2)]), "লব × লব, হর × হর।", lv)
def f4_div(b, lv):
    a, c, d, e = R.randint(1, 9), R.randint(2, 12), R.randint(1, 9), R.randint(2, 12)
    if math.gcd(a, c) != 1 or math.gcd(d, e) != 1: return
    v = F(a, c) / F(d, e)
    b.add(f"{a}/{c} ÷ {d}/{e} = কত?", fr(v), W(fr(v), [fr(F(a, c) * F(d, e)), fr(1 / v), fr(F(a * d, c + e)) if c + e else fr(v + 1), fr(v + 1)]), "ভাজক উল্টিয়ে গুণ।", lv)
def f4_mixed(b, lv):
    w_, p, q = R.randint(1, 9), R.randint(1, 8), R.randint(2, 9)
    if p >= q or math.gcd(p, q) != 1: return
    x = w_ + F(p, q); t = R.randrange(2)
    if t == 0: b.add(f"{w_} {p}/{q} কে অপ্রকৃত ভগ্নাংশে প্রকাশ করলে কোনটি হবে?", fr(x), W(fr(x), [f"{w_ * p + q}/{q}", f"{w_ + p}/{q}", f"{w_ * q}/{p}", f"{w_ * q + p}/{p}"]), f"({w_} × {q} + {p})/{q}।", lv)
    else: b.add(f"{fr(x)} কে মিশ্র ভগ্নাংশে প্রকাশ করলে কোনটি হবে?", mixed(x), W(mixed(x), [f"{w_ + 1} {p}/{q}", f"{w_} {q - p}/{q}" if q - p != p else f"{w_} {p}/{q + 1}", f"{p} {w_}/{q}" if w_ < q else f"{w_ - 1} {p}/{q}", f"{w_} {p}/{x.numerator}"]), "", lv)
def f4_of(b, lv):
    p, q = R.randint(1, 8), R.randint(2, 12)
    if p >= q or math.gcd(p, q) != 1: return
    n = q * R.randint(2, 50); v = n * p // q
    it, g = R.choice([('টাকা', 'টাকার'), ('কেজি চাল', 'কেজি চালের'), ('মিটার কাপড়', 'মিটার কাপড়ের'), ('জন শিক্ষার্থী', 'জন শিক্ষার্থীর')])
    b.add(f"{n} {g} {p}/{q} অংশ কত {it}?", v, W(v, [n // q, v + p, n - v, n * q // p if (n * q) % p == 0 and n * q // p < 100000 else v * 2]), f"{n} × {p}/{q}।", lv)
def f4_cmp(b, lv):
    fs = []
    while len(fs) < 4:
        p, q = R.randint(1, 11), R.randint(2, 12)
        if p < q and math.gcd(p, q) == 1 and F(p, q) not in fs: fs.append(F(p, q))
    big = R.random() < .5; c = max(fs) if big else min(fs)
    b.add(f"নিচের কোন ভগ্নাংশটি {'বৃহত্তম' if big else 'ক্ষুদ্রতম'}?", fr(c), W(fr(c), [fr(x) for x in fs]), "সমহর করে তুলনা।", lv)
def f4_story(b, lv):
    tot = R.randint(4, 40) * 12; p1, q1 = R.choice([(1, 2), (1, 3), (1, 4), (1, 6), (2, 3), (3, 4)]); p2, q2 = R.choice([(1, 3), (1, 4), (1, 6), (1, 12), (1, 2)])
    a = tot * p1 // q1; rest = tot - a; c = rest * p2 // q2
    if (tot * p1) % q1 or (rest * p2) % q2: return
    v = rest - c
    b.add(f"রাজুর {tot} টাকা ছিল। সে তার {p1}/{q1} অংশ দিয়ে বই এবং বাকি টাকার {p2}/{q2} অংশ দিয়ে খাতা কিনল। তার কাছে কত টাকা অবশিষ্ট রইল?", v, W(v, [tot - a - tot * p2 // q2 if (tot * p2) % q2 == 0 else v + 5, rest, c, v + 6]), f"বই {a}, বাকি {rest}; খাতা {c}; অবশিষ্ট {v}।", lv)
def f4_part(b, lv):
    p, q = R.randint(1, 8), R.randint(2, 12)
    if p >= q or math.gcd(p, q) != 1: return
    whole = q * R.randint(2, 40); part_ = whole * p // q
    b.add(f"কোনো সংখ্যার {p}/{q} অংশ {part_} হলে সংখ্যাটি কত?", whole, W(whole, [part_ * p // q if (part_ * p) % q == 0 and part_ * p // q != whole else whole + q, part_ + q, whole - q, part_ * q]), f"{part_} × {q}/{p}।", lv)
P4 = part(None, TOT, fx4, [f4_simp, f4_add, f4_mul, f4_mixed, f4_of], [f4_div, f4_cmp, f4_add, f4_of, f4_part], [f4_story, f4_part, f4_div])
save('w4', P4)

# ===================================================== ৫ দশমিক ভগ্নাংশ
fx5 = [
 ("দশমিক বিন্দুর ডান দিকের প্রথম স্থানকে কী বলে?", "দশমাংশ", ["শতাংশ", "সহস্রাংশ", "একক"], "", E),
 ("দশমিক বিন্দুর ডান দিকের দ্বিতীয় স্থানকে কী বলে?", "শতাংশ", ["দশমাংশ", "সহস্রাংশ", "দশক"], "", E),
 ("দশমিক সংখ্যাকে 10 দিয়ে গুণ করলে দশমিক বিন্দু কোন দিকে সরে?", "এক ঘর ডানে", ["এক ঘর বামে", "দুই ঘর ডানে", "সরে না"], "", E),
 ("দশমিক সংখ্যাকে 100 দিয়ে ভাগ করলে দশমিক বিন্দু কোন দিকে সরে?", "দুই ঘর বামে", ["দুই ঘর ডানে", "এক ঘর বামে", "সরে না"], "", E),
 ("0.5 এর সমান কোনটি?", "1/2", ["1/5", "5/100", "2/5"], "", E),
]
def dec_(k, p): return D(F(k, 10 ** p))
def d5_tofrac(b, lv):
    p = R.choice([1, 2]); k = R.randint(1, 10 ** p - 1)
    if k % 10 == 0 and p == 2: return
    x = F(k, 10 ** p)
    b.add(f"{D(x)} কে সাধারণ ভগ্নাংশে প্রকাশ করলে লঘিষ্ঠ আকারে কোনটি হবে?", fr(x), W(fr(x), [f"{k}/{10 ** (p + 1)}", f"{k}/{10 ** (p - 1)}" if p > 1 else f"{k + 1}/10", fr(x + F(1, 10)), f"{x.denominator}/{x.numerator}" if x.numerator != 1 else f"1/{x.denominator * 10}"]), "", lv)
def d5_todec(b, lv):
    q = R.choice([2, 4, 5, 8, 20, 25, 50, 10, 100]); p = R.randint(1, q - 1)
    if math.gcd(p, q) != 1: return
    x = F(p, q)
    b.add(f"{p}/{q} কে দশমিক ভগ্নাংশে প্রকাশ করলে কোনটি হবে?", D(x), W(D(x), [D(x * 10), D(x / 10), D(x + F(1, 100)), f"{p}.{q}"]), "", lv)
def d5_add(b, lv):
    a, c = F(R.randint(11, 9999), R.choice([10, 100])), F(R.randint(11, 9999), R.choice([10, 100, 1000])); s_ = R.choice(['+', '−'])
    if s_ == '−' and c > a: a, c = c, a
    v = a + c if s_ == '+' else a - c
    b.add(f"{D(a)} {s_} {D(c)} = কত?", D(v), W(D(v), [D(v * 10), D(v / 10), D(abs(a - c) if s_ == '+' else a + c), D(v + F(1, 10))]), "দশমিক বিন্দু বরাবর সাজিয়ে।", lv)
def d5_mul(b, lv):
    a = F(R.randint(2, 99), R.choice([10, 100])); c = R.choice([F(R.randint(2, 9)), F(R.randint(2, 99), 10)])
    v = a * c
    b.add(f"{D(a)} × {D(c)} = কত?", D(v), W(D(v), [D(v * 10), D(v / 10), D(a + c), D(v * 100) if v * 100 != a + c else D(v + 1)]), "দশমিকের পর মোট অঙ্কসংখ্যা গুনে বিন্দু বসাও।", lv)
def d5_div(b, lv):
    c = R.choice([2, 4, 5, 8, F(1, 10), F(5, 10), F(2, 10), F(25, 100)]); q = F(R.randint(2, 99), R.choice([1, 10]))
    a = q * c
    b.add(f"{D(a)} ÷ {D(c)} = কত?", D(q), W(D(q), [D(q * 10), D(q / 10), D(a * c), D(q + 1)]), "", lv)
def d5_ten(b, lv):
    a = F(R.randint(11, 99999), R.choice([10, 100, 1000])); k = R.choice([10, 100, 1000]); t = R.randrange(2)
    v = a * k if t == 0 else a / k
    b.add(f"{D(a)} {'×' if t == 0 else '÷'} {k} = কত?", D(v), W(D(v), [D(a / k if t == 0 else a * k), D(v * 10), D(v / 10), D(a)]), "", lv)
def d5_ord(b, lv):
    xs = list({F(R.randint(1, 999), 1000) for _ in range(6)})[:4]
    if len(xs) < 4: return
    big = R.random() < .5; c = max(xs) if big else min(xs)
    b.add(f"{', '.join(D(x) for x in xs)} এর মধ্যে {'বৃহত্তম' if big else 'ক্ষুদ্রতম'} কোনটি?", D(c), W(D(c), [D(x) for x in xs]), "", lv)
def d5_place(b, lv):
    ds = [R.randint(1, 9) for _ in range(5)]; x = F(int(''.join(map(str, ds))), 1000)
    pos = R.randrange(3); names = ['দশমাংশ', 'শতাংশ', 'সহস্রাংশ']; d = ds[2 + pos]
    if ds.count(d) > 1: return
    b.add(f"{D(x)} সংখ্যায় {d} অঙ্কটি কোন স্থানে আছে?", f"{names[pos]} স্থানে", W(f"{names[pos]} স্থানে", [f"{n} স্থানে" for n in names] + ["একক স্থানে", "দশক স্থানে"]), "", lv)
def d5_money(b, lv):
    p = F(R.randint(1050, 9999), 100); n = R.randint(2, 12); tot = F(R.randint(500, 2000))
    if tot < p * n: return
    v = tot - p * n
    b.add(f"প্রতি কেজি {D(p)} টাকা দরে {n} কেজি ডাল কিনে দোকানিকে {D(tot)} টাকার নোট দিলে কত টাকা ফেরত পাওয়া যাবে?", D(v), W(D(v), [D(p * n), D(v + 1), D(tot - p), D(v + F(1, 10))]), f"দাম {D(p * n)} টাকা।", lv)
def d5_len(b, lv):
    a, c = F(R.randint(101, 999), 100), F(R.randint(11, 99), 100); n = R.randint(2, 9)
    v = a * n - c * n if a > c else None
    if v is None: return
    b.add(f"একটি ফিতার দৈর্ঘ্য {D(a)} মিটার। এরকম {n}টি ফিতা থেকে প্রত্যেকটির {D(c)} মিটার করে কেটে নিলে মোট কত মিটার ফিতা থাকবে?", D(v), W(D(v), [D(a * n), D(a * n - c), D(v + c), D(v * 10)]), f"({D(a)} − {D(c)}) × {n}।", lv)
P5 = part(None, TOT, fx5, [d5_tofrac, d5_todec, d5_add, d5_ten, d5_place], [d5_mul, d5_div, d5_ord, d5_money, d5_add], [d5_len, d5_money, d5_div])
save('w5', P5)

# ===================================================== ৬ শতকরা
fx6 = [
 ("শতকরা শব্দের অর্থ কী?", "প্রতি একশতে", ["প্রতি দশে", "প্রতি হাজারে", "প্রতি একে"], "", E),
 ("শতকরার প্রতীক কোনটি?", "%", ["‰", "#", "&"], "", E),
 ("100% = কত?", "1", ["100", "10", "1/100"], "", E),
 ("শতকরা কে কোন ধরনের ভগ্নাংশ হিসেবে প্রকাশ করা যায়?", "যার হর 100", ["যার হর 10", "যার লব 100", "যার হর 1000"], "", E),
]
def p6_of(b, lv):
    r = R.choice([5, 10, 12, 15, 20, 25, 30, 40, 50, 60, 75, 80]); n = R.randint(2, 60) * 20; v = F(n * r, 100)
    b.add(f"{n} এর {r}% কত?", D(v), W(D(v), [D(v * 10), D(F(n, r)) if n % r == 0 else D(v + 5), D(v + r), D(n - v)]), f"{n} × {r}/100।", lv)
def p6_tofrac(b, lv):
    r = R.choice([5, 10, 12, 15, 20, 25, 30, 40, 45, 50, 60, 75, 80, 35, 64, 72]); x = F(r, 100)
    t = R.randrange(2)
    if t == 0: b.add(f"{r}% কে লঘিষ্ঠ সাধারণ ভগ্নাংশে প্রকাশ করলে কোনটি হবে?", fr(x), W(fr(x), [f"{r}/10", fr(x * 2), f"1/{r}", fr(F(r, 1000))]), "", lv)
    else: b.add(f"{r}% কে দশমিক ভগ্নাংশে প্রকাশ করলে কোনটি হবে?", D(x), W(D(x), [D(x * 10), D(x / 10), str(r), D(x + F(1, 10))]), "", lv)
def p6_frac2p(b, lv):
    q = R.choice([2, 4, 5, 10, 20, 25, 50]); p = R.randint(1, q - 1)
    if math.gcd(p, q) != 1: return
    v = F(p * 100, q)
    b.add(f"{p}/{q} কে শতকরায় প্রকাশ করলে কোনটি হবে?", f"{D(v)}%", W(f"{D(v)}%", [f"{D(v / 10)}%", f"{p * q}%", f"{D(v + 5)}%", f"{D(100 - v)}%"]), f"{p}/{q} × 100।", lv)
def p6_what(b, lv):
    n = R.randint(2, 50) * 20; r = R.choice([5, 10, 15, 20, 25, 30, 40, 50, 60, 75]); part_ = n * r // 100
    if (n * r) % 100: return
    b.add(f"{n} এর কত শতাংশ {part_}?", f"{r}%", W(f"{r}%", [f"{r + 5}%", f"{r * 2}%", f"{part_}%", f"{100 - r}%"]), f"({part_} ÷ {n}) × 100।", lv)
def p6_marks(b, lv):
    tot = R.choice([50, 80, 100, 120, 150, 200, 400, 500]); r = R.choice([40, 50, 60, 70, 75, 80, 85, 90]); v = tot * r // 100
    if (tot * r) % 100: return
    t = R.randrange(2)
    if t == 0: b.add(f"একজন শিক্ষার্থী {tot} নম্বরের পরীক্ষায় {v} নম্বর পেয়েছে। সে শতকরা কত নম্বর পেয়েছে?", f"{r}%", W(f"{r}%", [f"{v}%", f"{100 - r}%", f"{r + 5}%", f"{r - 5}%"]), "", lv)
    else: b.add(f"একটি পরীক্ষায় মোট নম্বর {tot}। পাস করতে {r}% নম্বর লাগলে কমপক্ষে কত নম্বর পেতে হবে?", v, W(v, [r, v + 5, tot - v, v - 5]), "", lv)
def p6_people(b, lv):
    n = R.randint(4, 60) * 20; r = R.choice([5, 10, 15, 20, 25, 30, 35, 40, 45, 55, 60, 65]); v = n * r // 100
    if (n * r) % 100: return
    t = R.randrange(2)
    if t == 0: b.add(f"একটি বিদ্যালয়ের {n} জন শিক্ষার্থীর {r}% মেয়ে। ছেলে শিক্ষার্থী কতজন?", n - v, W(n - v, [v, n - r, (n - v) + 10, n // 2 if n // 2 != n - v else n // 2 + 5]), f"মেয়ে {v} জন; ছেলে {n} − {v}।", lv)
    else: b.add(f"একটি গ্রামের {n} জন লোকের {r}% শিক্ষিত। শিক্ষিত লোক কতজন?", v, W(v, [n - v, v + r, v * 10 if v * 10 < n else v + 10, r]), "", lv)
def p6_inc(b, lv):
    n = R.randint(2, 50) * 100; r = R.choice([5, 10, 15, 20, 25]); t = R.randrange(2)
    v = n * (100 + r) // 100 if t == 0 else n * (100 - r) // 100
    b.add(f"একটি জিনিসের দাম {n} টাকা। দাম {r}% {'বাড়লে' if t == 0 else 'কমলে'} নতুন দাম কত টাকা?", v, W(v, [n * (100 - r) // 100 if t == 0 else n * (100 + r) // 100, n + r if t == 0 else n - r, n * r // 100, v + 10]), "", lv)
def p6_whole(b, lv):
    r = R.choice([5, 10, 20, 25, 40, 50]); n = R.randint(2, 50) * 20; part_ = n * r // 100
    if (n * r) % 100: return
    b.add(f"কোনো সংখ্যার {r}% = {part_} হলে সংখ্যাটি কত?", n, W(n, [part_ * r, n + part_, n // 2 if n // 2 != part_ else n * 2, part_ + 100]), f"{part_} × 100/{r}।", lv)
P6 = part(None, TOT, fx6, [p6_of, p6_tofrac, p6_frac2p, p6_people], [p6_what, p6_marks, p6_inc, p6_of, p6_people], [p6_whole, p6_inc, p6_marks])
save('w6', P6)

# ===================================================== ৭ গড়
fx7 = [
 ("গড় নির্ণয়ের সূত্র কোনটি?", "রাশিগুলোর সমষ্টি ÷ রাশির সংখ্যা", ["রাশিগুলোর গুণফল ÷ রাশির সংখ্যা", "বৃহত্তম − ক্ষুদ্রতম", "রাশিগুলোর সমষ্টি × রাশির সংখ্যা"], "", E),
 ("রাশিগুলোর সমষ্টি = কত?", "গড় × রাশির সংখ্যা", ["গড় ÷ রাশির সংখ্যা", "গড় + রাশির সংখ্যা", "গড় − রাশির সংখ্যা"], "", E),
 ("সবগুলো রাশি সমান হলে গড় কত হয়?", "ঐ রাশির সমান", ["0", "রাশির সংখ্যার সমান", "1"], "", E),
]
def a7_mean(b, lv):
    n = R.randint(3, 7)
    while True:
        xs = [R.randint(5, 99) for _ in range(n)]
        if sum(xs) % n == 0: break
    m = sum(xs) // n
    b.add(f"{', '.join(map(str, xs))} সংখ্যাগুলোর গড় কত?", m, W(m, [m + 1, m - 1, sum(xs), m + 2]), f"{sum(xs)} ÷ {n}।", lv)
def a7_total(b, lv):
    n = R.randint(5, 60); m = R.randint(20, 95)
    b.add(f"{n} জন শিক্ষার্থীর গণিতে প্রাপ্ত নম্বরের গড় {m}। তাদের মোট নম্বর কত?", n * m, W(n * m, [n + m, n * m + m, n * m - n, m * 10]), "", lv)
def a7_miss(b, lv):
    n = R.randint(4, 7); m = R.randint(10, 80); xs = [R.randint(5, 99) for _ in range(n - 1)]; last = m * n - sum(xs)
    if not 1 <= last <= 200: return
    b.add(f"{n}টি সংখ্যার গড় {m}। এর {n - 1}টি সংখ্যা {', '.join(map(str, xs))} হলে অপর সংখ্যাটি কত?", last, W(last, [last + 1, m, last - n, m * n]), "", lv)
def a7_cons(b, lv):
    a = R.randint(1, 200); n = R.choice([3, 5, 7, 9]); xs = list(range(a, a + n)); m = a + n // 2
    t = R.randrange(2)
    if t == 0: b.add(f"{a} থেকে {a + n - 1} পর্যন্ত ক্রমিক স্বাভাবিক সংখ্যাগুলোর গড় কত?", m, W(m, [m + 1, m - 1, sum(xs), a + n]), "ক্রমিক সংখ্যার গড় = মাঝের সংখ্যা।", lv)
    else: b.add(f"ক্রমিক {n}টি স্বাভাবিক সংখ্যার গড় {m}। সবচেয়ে বড় সংখ্যাটি কত?", a + n - 1, W(a + n - 1, [m + n, a, m + 1, a + n]), "", lv)
def a7_age(b, lv):
    n = R.randint(3, 6); m = R.randint(8, 40); x = R.randint(20, 70); tot = n * m + x
    if tot % (n + 1): return
    v = tot // (n + 1)
    b.add(f"{n} জনের বয়সের গড় {m} বছর। তাদের সাথে {x} বছর বয়সের একজন যোগ দিলে গড় বয়স কত হবে?", v, W(v, [m, v + 1, (m + x) // 2 if (m + x) // 2 != v else v + 2, v - 1]), f"({n * m} + {x}) ÷ {n + 1}।", lv)
def a7_days(b, lv):
    days = ['শনিবার', 'রবিবার', 'সোমবার', 'মঙ্গলবার', 'বুধবার', 'বৃহস্পতিবার']; n = R.randint(3, 6)
    while True:
        xs = [R.randint(20, 60) for _ in range(n)]
        if sum(xs) % n == 0: break
    m = sum(xs) // n
    b.add(f"একটি শ্রেণিতে {', '.join(f'{d} {x} জন' for d, x in zip(days, xs))} শিক্ষার্থী উপস্থিত ছিল। গড়ে প্রতিদিন কতজন উপস্থিত ছিল?", m, W(m, [m + 1, m - 1, sum(xs), max(xs)]), "", lv)
def a7_comb(b, lv):
    n1, n2 = R.randint(5, 30), R.randint(5, 30); m1, m2 = R.randint(30, 90), R.randint(30, 90)
    tot = n1 * m1 + n2 * m2
    if tot % (n1 + n2) or m1 == m2: return
    v = tot // (n1 + n2)
    b.add(f"একটি শ্রেণির {n1} জন ছাত্রের গড় নম্বর {m1} এবং {n2} জন ছাত্রীর গড় নম্বর {m2}। সকলের গড় নম্বর কত?", v, W(v, [(m1 + m2) // 2 if (m1 + m2) // 2 != v else v + 1, v + 2, v - 2, m1 + m2]), "মোট নম্বর ÷ মোট শিক্ষার্থী।", lv)
def a7_teacher(b, lv):
    n = R.randint(10, 40); m = R.randint(8, 12); t_ = R.randint(25, 60)
    new = F(n * m + t_, n + 1)
    if new.denominator != 1: return
    b.add(f"একটি শ্রেণির {n} জন শিক্ষার্থীর গড় বয়স {m} বছর। শিক্ষকের বয়স যোগ করলে গড় বয়স {new} বছর হয়। শিক্ষকের বয়স কত বছর?", t_, W(t_, [int(new) * (n + 1), t_ + 1, t_ - n // 2, int(new) + m]), f"{int(new)} × {n + 1} − {n} × {m}।", lv)
P7 = part(None, TOT, fx7, [a7_mean, a7_total, a7_cons, a7_days], [a7_miss, a7_age, a7_mean, a7_comb], [a7_teacher, a7_comb, a7_miss])
save('w7', P7)

# ===================================================== ৮ পরিমাপ
fx8 = [
 ("দৈর্ঘ্য পরিমাপের আন্তর্জাতিক একক কোনটি?", "মিটার", ["কিলোগ্রাম", "লিটার", "সেকেন্ড"], "", E),
 ("ওজন পরিমাপের আন্তর্জাতিক একক কোনটি?", "কিলোগ্রাম", ["মিটার", "লিটার", "গজ"], "", E),
 ("তরল পদার্থের আয়তন পরিমাপের একক কোনটি?", "লিটার", ["মিটার", "গ্রাম", "বর্গমিটার"], "", E),
 ("1 কিলোমিটার = কত মিটার?", "1000", ["100", "10", "10000"], "", E),
 ("1 কিলোগ্রাম = কত গ্রাম?", "1000", ["100", "10", "10000"], "", E),
 ("1 লিটার = কত মিলিলিটার?", "1000", ["100", "10", "10000"], "", E),
 ("1 মিটার = কত সেন্টিমিটার?", "100", ["10", "1000", "50"], "", E),
 ("1 কুইন্টাল = কত কিলোগ্রাম?", "100", ["1000", "10", "50"], "", E),
 ("1 মেট্রিক টন = কত কিলোগ্রাম?", "1000", ["100", "10000", "500"], "", E),
 ("আয়তক্ষেত্রের ক্ষেত্রফল নির্ণয়ের সূত্র কোনটি?", "দৈর্ঘ্য × প্রস্থ", ["2 × (দৈর্ঘ্য + প্রস্থ)", "দৈর্ঘ্য + প্রস্থ", "দৈর্ঘ্য ÷ প্রস্থ"], "", E),
 ("বর্গক্ষেত্রের পরিসীমা নির্ণয়ের সূত্র কোনটি?", "4 × বাহুর দৈর্ঘ্য", ["বাহু × বাহু", "2 × বাহুর দৈর্ঘ্য", "3 × বাহুর দৈর্ঘ্য"], "", E),
 ("1 বর্গমিটার = কত বর্গসেন্টিমিটার?", "10000", ["100", "1000", "1000000"], "", M),
 ("1 ঘন্টা = কত সেকেন্ড?", "3600", ["60", "360", "6000"], "", M),
]
LEN5 = [('কিলোমিটার', 1000), ('মিটার', 1), ('সেন্টিমিটার', F(1, 100)), ('মিলিমিটার', F(1, 1000))]
MAS5 = [('কিলোগ্রাম', 1000), ('গ্রাম', 1)]
VOL5 = [('লিটার', 1), ('মিলিলিটার', F(1, 1000))]
def r8_conv(b, lv):
    tab = R.choice([LEN5, LEN5, MAS5, VOL5]); (u1, k1), (u2, k2) = R.sample(tab, 2)
    x = R.randint(2, 99); v = F(x) * F(k1) / F(k2)
    if len(D(v)) > 9: return
    b.add(f"{x} {u1} = কত {u2}?", D(v), W(D(v), [D(v * 10), D(v / 10), D(v * 100), D(v / 100)]), f"1 {u1} = {D(F(k1) / F(k2))} {u2}।", lv)
def r8_mix(b, lv):
    t = R.randrange(3); a, c = R.randint(1, 20), R.randint(1, 999)
    q, v, u = [(f"{a} কিলোমিটার {c} মিটার = কত মিটার?", a * 1000 + c, 'মিটার'), (f"{a} কিলোগ্রাম {c} গ্রাম = কত গ্রাম?", a * 1000 + c, 'গ্রাম'), (f"{a} লিটার {c} মিলিলিটার = কত মিলিলিটার?", a * 1000 + c, 'মিলিলিটার')][t]
    b.add(q, IND(v), W(IND(v), [IND(a * 100 + c), IND(a + c), IND(a * 1000 + c * 10) if c < 100 else IND(v + 100), IND(v - 1000) if a > 1 else IND(v + 1000)]), "", lv)
def r8_rect(b, lv):
    l, w_ = R.randint(5, 80), R.randint(3, 60)
    if l == w_: return
    t = R.randrange(2)
    if t == 0: b.add(f"একটি আয়তাকার মাঠের দৈর্ঘ্য {l} মিটার ও প্রস্থ {w_} মিটার। মাঠটির ক্ষেত্রফল কত বর্গমিটার?", l * w_, W(l * w_, [2 * (l + w_), l + w_, l * w_ + l, l * w_ - w_]), "", lv)
    else: b.add(f"একটি আয়তাকার মাঠের দৈর্ঘ্য {l} মিটার ও প্রস্থ {w_} মিটার। মাঠটির পরিসীমা কত মিটার?", 2 * (l + w_), W(2 * (l + w_), [l * w_, l + w_, 2 * l + w_, 4 * l]), "", lv)
def r8_sq(b, lv):
    s_ = R.randint(3, 60); t = R.randrange(3)
    if t == 0: b.add(f"একটি বর্গক্ষেত্রের এক বাহু {s_} সেমি। এর ক্ষেত্রফল কত বর্গসেমি?", s_ * s_, W(s_ * s_, [4 * s_, 2 * s_, s_ * s_ + s_, s_ * s_ - 1]), "", lv)
    elif t == 1: b.add(f"একটি বর্গক্ষেত্রের এক বাহু {s_} সেমি। এর পরিসীমা কত সেমি?", 4 * s_, W(4 * s_, [s_ * s_, 2 * s_, 3 * s_, 4 * s_ + 4]), "", lv)
    else: b.add(f"একটি বর্গক্ষেত্রের পরিসীমা {4 * s_} সেমি। এর এক বাহুর দৈর্ঘ্য কত সেমি?", s_, W(s_, [2 * s_, 4 * s_, s_ + 4, s_ * s_]), "", lv)
def r8_side(b, lv):
    l, w_ = R.randint(5, 80), R.randint(3, 60)
    if l == w_: return
    b.add(f"একটি আয়তাকার বাগানের ক্ষেত্রফল {l * w_} বর্গমিটার এবং দৈর্ঘ্য {l} মিটার। এর প্রস্থ কত মিটার?", w_, W(w_, [l * w_ - l, l, w_ + 2, 2 * w_]), "", lv)
def r8_cost(b, lv):
    l, w_ = R.randint(4, 20), R.randint(3, 15); r = R.randint(2, 20) * 10; t = R.randrange(2)
    if t == 0: v = l * w_ * r; b.add(f"{l} মিটার দৈর্ঘ্য ও {w_} মিটার প্রস্থের একটি মেঝে প্রতি বর্গমিটার {r} টাকা দরে পাকা করতে কত টাকা লাগবে?", IND(v), W(IND(v), [IND(2 * (l + w_) * r), IND(l * w_ + r), IND(v + r), IND((l + w_) * r)]), "", lv)
    else: v = 2 * (l + w_) * r // 10; b.add(f"{l} মিটার দৈর্ঘ্য ও {w_} মিটার প্রস্থের একটি বাগানের চারদিকে প্রতি মিটার {r // 10} টাকা দরে বেড়া দিতে কত টাকা লাগবে?", IND(v), W(IND(v), [IND(l * w_ * r // 10), IND((l + w_) * r // 10), IND(v + r // 10), IND(4 * l * r // 10)]), "", lv)
def r8_time(b, lv):
    t = R.randrange(3)
    if t == 0: h, m = R.randint(1, 9), R.randint(1, 59); b.add(f"{h} ঘণ্টা {m} মিনিট = কত মিনিট?", h * 60 + m, W(h * 60 + m, [h * 100 + m, h + m, h * 60, h * 60 + m + 60]), "", lv)
    elif t == 1: d = R.randint(2, 30); b.add(f"{d} দিন = কত ঘণ্টা?", d * 24, W(d * 24, [d * 12, d * 60, d * 24 + 24, d * 7]), "", lv)
    else: mm = R.randint(70, 600); b.add(f"{mm} মিনিট = কত ঘণ্টা কত মিনিট?", f"{mm // 60} ঘণ্টা {mm % 60} মিনিট", W(f"{mm // 60} ঘণ্টা {mm % 60} মিনিট", [f"{mm // 100} ঘণ্টা {mm % 100} মিনিট", f"{mm // 60 + 1} ঘণ্টা {mm % 60} মিনিট", f"{mm // 60} ঘণ্টা {(mm % 60 + 10) % 60} মিনিট", f"{mm // 60 - 1} ঘণ্টা {mm % 60} মিনিট" if mm // 60 > 1 else f"{mm // 60} ঘণ্টা {mm % 60 + 1} মিনিট"]), "", lv)
def r8_path(b, lv):
    l, w_ = R.randint(10, 60), R.randint(8, 40); p = R.randint(1, 3)
    if l == w_: return
    v = (l + 2 * p) * (w_ + 2 * p) - l * w_
    b.add(f"{l} মিটার দৈর্ঘ্য ও {w_} মিটার প্রস্থের একটি বাগানের বাইরে চারদিকে {p} মিটার চওড়া রাস্তা আছে। রাস্তার ক্ষেত্রফল কত বর্গমিটার?", v, W(v, [(l + p) * (w_ + p) - l * w_, 2 * (l + w_) * p, l * w_ - (l - 2 * p) * (w_ - 2 * p), v + 4 * p * p]), f"({l + 2 * p} × {w_ + 2 * p}) − ({l} × {w_})।", lv)
def r8_bottle(b, lv):
    c = R.choice([250, 500, 200, 750, 300]); n = R.randint(2, 20)
    tot = c * n
    b.add(f"একটি বোতলে {c} মিলিলিটার পানি ধরে। {D(F(tot, 1000))} লিটার পানি দিয়ে এরকম কয়টি বোতল পূর্ণ করা যাবে?", n, W(n, [n + 1, n * 2, n - 1 if n > 2 else n + 3, tot // 100]), f"{tot} মিলিলিটার ÷ {c}।", lv)
P8 = part(None, TOT, fx8, [r8_conv, r8_mix, r8_rect, r8_sq, r8_time], [r8_side, r8_cost, r8_bottle, r8_conv, r8_time], [r8_path, r8_cost, r8_bottle])
save('w8', P8)

# ===================================================== ৯ জ্যামিতি
fx9 = [
 ("এক সমকোণ = কত ডিগ্রি?", "90°", ["180°", "45°", "60°"], "", E),
 ("এক সরলকোণ = কত ডিগ্রি?", "180°", ["90°", "360°", "270°"], "", E),
 ("90° অপেক্ষা ছোট কোণকে কী বলে?", "সূক্ষ্মকোণ", ["স্থূলকোণ", "সমকোণ", "প্রবৃদ্ধ কোণ"], "", E),
 ("90° অপেক্ষা বড় কিন্তু 180° অপেক্ষা ছোট কোণকে কী বলে?", "স্থূলকোণ", ["সূক্ষ্মকোণ", "সমকোণ", "প্রবৃদ্ধ কোণ"], "", E),
 ("180° অপেক্ষা বড় কিন্তু 360° অপেক্ষা ছোট কোণকে কী বলে?", "প্রবৃদ্ধ কোণ", ["স্থূলকোণ", "সরলকোণ", "সূক্ষ্মকোণ"], "", E),
 ("ত্রিভুজের তিন কোণের সমষ্টি কত?", "180°", ["90°", "360°", "270°"], "", E),
 ("চতুর্ভুজের চার কোণের সমষ্টি কত?", "360°", ["180°", "270°", "540°"], "", E),
 ("বৃত্তের ব্যাস ব্যাসার্ধের কত গুণ?", "2 গুণ", ["অর্ধেক", "3 গুণ", "4 গুণ"], "", E),
 ("বৃত্তের কেন্দ্রগামী জ্যাকে কী বলে?", "ব্যাস", ["ব্যাসার্ধ", "চাপ", "পরিধি"], "", E),
 ("বৃত্তের কেন্দ্র থেকে পরিধি পর্যন্ত দূরত্বকে কী বলে?", "ব্যাসার্ধ", ["ব্যাস", "জ্যা", "চাপ"], "", E),
 ("যে ত্রিভুজের তিনটি বাহু সমান তাকে কী বলে?", "সমবাহু ত্রিভুজ", ["সমদ্বিবাহু ত্রিভুজ", "বিষমবাহু ত্রিভুজ", "সমকোণী ত্রিভুজ"], "", E),
 ("যে চতুর্ভুজের চারটি বাহু সমান ও প্রতিটি কোণ সমকোণ তাকে কী বলে?", "বর্গক্ষেত্র", ["আয়তক্ষেত্র", "রম্বস", "সামান্তরিক"], "", E),
 ("যে চতুর্ভুজের বিপরীত বাহুগুলো সমান ও প্রতিটি কোণ সমকোণ, কিন্তু সব বাহু সমান নয়, তাকে কী বলে?", "আয়তক্ষেত্র", ["বর্গক্ষেত্র", "রম্বস", "ট্রাপিজিয়াম"], "", E),
 ("কোণ মাপার যন্ত্রের নাম কী?", "চাঁদা", ["কম্পাস", "রুলার", "সেটস্কয়ার"], "", E),
 ("বৃত্ত আঁকার যন্ত্রের নাম কী?", "কম্পাস", ["চাঁদা", "রুলার", "ডিভাইডার"], "", E),
]
def j9_kind(b, lv):
    a = R.randint(1, 359)
    k = 'সূক্ষ্মকোণ' if a < 90 else 'সমকোণ' if a == 90 else 'স্থূলকোণ' if a < 180 else 'সরলকোণ' if a == 180 else 'প্রবৃদ্ধ কোণ'
    b.add(f"{a}° কোণটি কোন ধরনের কোণ?", k, W(k, ['সূক্ষ্মকোণ', 'স্থূলকোণ', 'প্রবৃদ্ধ কোণ', 'সমকোণ', 'সরলকোণ']), "", lv)
def j9_third(b, lv):
    a, c = R.randint(20, 110), R.randint(20, 110)
    if a + c >= 170: return
    v = 180 - a - c
    b.add(f"একটি ত্রিভুজের দুটি কোণ {a}° ও {c}° হলে তৃতীয় কোণটি কত?", ANG(v), W(ANG(v), [ANG(a + c), ANG(360 - a - c), ANG(v + 10), ANG(abs(a - c)) if abs(a - c) != v else ANG(v - 5)]), "", lv)
def j9_comp(b, lv):
    a = R.randint(5, 175); t = R.randrange(2)
    if t == 0 and a < 90 and a != 45: b.add(f"{a}° কোণের পূরক কোণ কত?", ANG(90 - a), W(ANG(90 - a), [ANG(180 - a), ANG(a), ANG(90 + a), ANG(90 - a + 10)]), "পূরক কোণের সমষ্টি 90°।", lv)
    elif a != 90: b.add(f"{a}° কোণের সম্পূরক কোণ কত?", ANG(180 - a), W(ANG(180 - a), [ANG(abs(90 - a)), ANG(360 - a), ANG(a), ANG(180 - a + 10)]), "সম্পূরক কোণের সমষ্টি 180°।", lv)
def j9_quad(b, lv):
    xs = [R.randint(50, 130) for _ in range(3)]; v = 360 - sum(xs)
    if not 30 < v < 170: return
    b.add(f"একটি চতুর্ভুজের তিনটি কোণ {xs[0]}°, {xs[1]}° ও {xs[2]}° হলে চতুর্থ কোণটি কত?", ANG(v), W(ANG(v), [ANG(180 - v if 180 - v > 0 else v + 20), ANG(v + 10), ANG(360 - v), ANG(v - 10)]), "", lv)
def j9_circle(b, lv):
    r = R.randint(2, 30); t = R.randrange(2)
    if t == 0: b.add(f"একটি বৃত্তের ব্যাসার্ধ {r} সেমি হলে ব্যাস কত সেমি?", 2 * r, W(2 * r, [r, r // 2 if r > 2 else r + 1, 3 * r, 4 * r]), "", lv)
    else: b.add(f"একটি বৃত্তের ব্যাস {2 * r} সেমি হলে ব্যাসার্ধ কত সেমি?", r, W(r, [2 * r, 4 * r, r + 2, r // 2 if r > 2 else r + 3]), "", lv)
def j9_tri(b, lv):
    s = R.choice(['eq', 'iso', 'sc'])
    if s == 'eq': x = R.randint(3, 20); sd = [x, x, x]; c = 'সমবাহু'
    elif s == 'iso': x, y = R.randint(4, 20), R.randint(2, 20); sd = [x, x, y]; c = 'সমদ্বিবাহু'
    else: sd = R.sample(range(3, 20), 3); c = 'বিষমবাহু'
    ss = sorted(sd)
    if ss[0] + ss[1] <= ss[2] or (s == 'iso' and len(set(sd)) != 2): return
    R.shuffle(sd)
    b.add(f"একটি ত্রিভুজের বাহুগুলো {sd[0]} সেমি, {sd[1]} সেমি ও {sd[2]} সেমি হলে এটি কোন ধরনের ত্রিভুজ?", f"{c} ত্রিভুজ", W(f"{c} ত্রিভুজ", ['সমবাহু ত্রিভুজ', 'সমদ্বিবাহু ত্রিভুজ', 'বিষমবাহু ত্রিভুজ', 'সমকোণী ত্রিভুজ']), "", lv)
def j9_trikind(b, lv):
    a, c = R.randint(10, 120), R.randint(10, 120); v = 180 - a - c
    if v <= 0: return
    m = max(a, c, v); k = 'সমকোণী' if m == 90 else 'স্থূলকোণী' if m > 90 else 'সূক্ষ্মকোণী'
    b.add(f"একটি ত্রিভুজের দুটি কোণ {a}° ও {c}° হলে ত্রিভুজটি কোন ধরনের?", f"{k} ত্রিভুজ", W(f"{k} ত্রিভুজ", ['সমকোণী ত্রিভুজ', 'স্থূলকোণী ত্রিভুজ', 'সূক্ষ্মকোণী ত্রিভুজ', 'সমবাহু ত্রিভুজ']), f"তৃতীয় কোণ {v}°।", lv)
def j9_clock(b, lv):
    h = R.randint(1, 11); v = 30 * min(h, 12 - h)
    b.add(f"ঘড়িতে যখন {h}টা বাজে তখন ঘণ্টার কাঁটা ও মিনিটের কাঁটার মধ্যবর্তী (ছোট) কোণ কত?", ANG(v), W(ANG(v), [ANG(v + 30), ANG(360 - v), ANG(h * 6), ANG(abs(v - 30)) if v != 30 else ANG(15)]), "প্রতি ঘণ্টার ঘরে 30°।", lv)
def j9_ratio(b, lv):
    p, q, r = R.randint(1, 9), R.randint(1, 9), R.randint(1, 9); s = p + q + r
    if 180 % s or len({p, q, r}) < 3: return
    k = 180 // s; v = max(p, q, r) * k
    b.add(f"একটি ত্রিভুজের কোণগুলোর অনুপাত {p} : {q} : {r} হলে বৃহত্তম কোণটি কত?", ANG(v), W(ANG(v), [ANG(min(p, q, r) * k), ANG(sorted([p, q, r])[1] * k), ANG(k), ANG(v + 10)]), f"{s} ভাগ = 180°।", lv)
def j9_iso(b, lv):
    a = R.randint(20, 85)
    b.add(f"একটি সমদ্বিবাহু ত্রিভুজের ভূমিসংলগ্ন প্রতিটি কোণ {a}° হলে শীর্ষকোণ কত?", ANG(180 - 2 * a), W(ANG(180 - 2 * a), [ANG(180 - a), ANG(2 * a), ANG(a), ANG(90 - a) if 90 - a != 180 - 2 * a else ANG(a + 5)]), "", lv)
P9 = part(None, TOT, fx9, [j9_kind, j9_third, j9_comp, j9_circle, j9_tri], [j9_quad, j9_trikind, j9_clock, j9_iso, j9_third], [j9_ratio, j9_clock, j9_quad])
save('w9', P9)

# ===================================================== ১০ উপাত্ত বিন্যস্তকরণ
fx10 = [
 ("সংখ্যাভিত্তিক তথ্যকে কী বলে?", "উপাত্ত", ["গণসংখ্যা", "ট্যালি", "লেখচিত্র"], "", E),
 ("উপাত্তকে ছোট থেকে বড় ক্রমে সাজানোকে কী বলে?", "ঊর্ধ্বক্রম", ["অধঃক্রম", "গণসংখ্যা", "ট্যালি"], "", E),
 ("উপাত্তকে বড় থেকে ছোট ক্রমে সাজানোকে কী বলে?", "অধঃক্রম", ["ঊর্ধ্বক্রম", "গণসংখ্যা", "পরিসর"], "", E),
 ("কোনো উপাত্ত কতবার এসেছে তাকে কী বলে?", "গণসংখ্যা", ["ট্যালি", "গড়", "ক্রম"], "", E),
 ("ট্যালি চিহ্নে প্রতি পাঁচটি গণনার পঞ্চমটি কীভাবে দেওয়া হয়?", "আগের চারটি দাগ আড়াআড়ি কেটে", ["নতুন খাড়া দাগ দিয়ে", "বৃত্ত এঁকে", "তারকা দিয়ে"], "", E),
 ("উপাত্ত উপস্থাপনের জন্য আয়তাকার স্তম্ভ ব্যবহার করে যে লেখচিত্র আঁকা হয় তাকে কী বলে?", "স্তম্ভলেখ", ["রেখালেখ", "পাইচিত্র", "ট্যালি"], "", E),
]
def u10_asc(b, lv):
    xs = R.sample(range(1, 99), 6); s = sorted(xs); up = R.random() < .5
    c = ', '.join(map(str, s if up else s[::-1]))
    w = [', '.join(map(str, s[::-1] if up else s)), ', '.join(map(str, (s[:2] + [s[3], s[2]] + s[4:]) if up else (s[:2] + [s[3], s[2]] + s[4:])[::-1])), ', '.join(map(str, xs)) if xs not in (s, s[::-1]) else ', '.join(map(str, s[1:] + s[:1]))]
    b.add(f"{', '.join(map(str, xs))} সংখ্যাগুলোকে {'ঊর্ধ্বক্রমে' if up else 'অধঃক্রমে'} সাজালে কোনটি হবে?", c, W(c, w + [', '.join(map(str, sorted(xs, key=lambda v: v % 10)))]), "", lv)
def u10_tally(b, lv):
    n = R.randint(6, 33); f, r = divmod(n, 5)
    s = '  '.join(['||||/'] * f + (['|' * r] if r else []))
    b.add(f"ট্যালি চিহ্ন  {s}  দ্বারা কোন সংখ্যা বোঝায়? (||||/ = আড়াআড়ি কাটা চারটি দাগ, অর্থাৎ 5)", n, W(n, [n + 1, n - 1, f + r, n + 5]), "", lv)
def u10_freq(b, lv):
    vals = R.sample(range(1, 10), 3); xs = [R.choice(vals) for _ in range(R.randint(10, 18))]
    t = R.choice(vals); v = xs.count(t)
    if v == 0: return
    b.add(f"{', '.join(map(str, xs))} উপাত্তে {t} সংখ্যাটির গণসংখ্যা কত?", v, W(v, [v + 1, max(0, v - 1), len(xs), v + 2]), "", lv)
def u10_most(b, lv):
    fr_ = ['লাল', 'নীল', 'সবুজ', 'হলুদ', 'সাদা']; ns = R.sample(range(3, 30), 5)
    desc = ', '.join(f"{c} {n} জন" for c, n in zip(fr_, ns)); t = R.randrange(3)
    if t == 0: c0 = fr_[ns.index(max(ns))]; q = 'কোন রং সবচেয়ে বেশি শিক্ষার্থীর পছন্দ?'; w = fr_
    elif t == 1: c0 = str(sum(ns)); q = 'মোট কতজন শিক্ষার্থীর মতামত নেওয়া হয়েছে?'; w = [str(sum(ns) + 5), str(max(ns) * 5), str(sum(ns) - min(ns))]
    else: c0 = str(max(ns) - min(ns)); q = 'সবচেয়ে বেশি ও সবচেয়ে কম পছন্দের রঙের শিক্ষার্থী সংখ্যার পার্থক্য কত?'; w = [str(max(ns)), str(max(ns) + min(ns)), str(max(ns) - min(ns) + 1)]
    b.add(f"একটি জরিপে পছন্দের রং: {desc}। {q}", c0, W(c0, w), "", lv)
def u10_bar(b, lv):
    days = ['শনি', 'রবি', 'সোম', 'মঙ্গল', 'বুধ']; xs = R.sample(range(10, 60), 5); t = R.randrange(2)
    desc = ', '.join(f"{d}বার {x} জন" for d, x in zip(days, xs))
    if t == 0: c0 = days[xs.index(min(xs))] + 'বার'; q = 'কোন দিন সবচেয়ে কম শিক্ষার্থী উপস্থিত ছিল?'; w = [d + 'বার' for d in days]
    else:
        i, j = R.sample(range(5), 2); c0 = str(xs[i] + xs[j]); q = f"{days[i]}বার ও {days[j]}বার মিলিয়ে কতজন উপস্থিত ছিল?"; w = [str(xs[i] + xs[j] + 10), str(abs(xs[i] - xs[j])), str(sum(xs))]
    b.add(f"একটি স্তম্ভলেখে পাঁচ দিনের উপস্থিতি দেখানো হয়েছে: {desc}। {q}", c0, W(c0, w), "", lv)
def u10_rng(b, lv):
    xs = R.sample(range(1, 150), R.randint(6, 9)); t = R.randrange(2)
    if t == 0: v = max(xs); b.add(f"{', '.join(map(str, xs))} উপাত্তের সর্বোচ্চ মান কত?", v, W(v, [min(xs), sorted(xs)[-2], v + 1, sum(xs) // len(xs)]), "", lv)
    else: v = max(xs) - min(xs); b.add(f"{', '.join(map(str, xs))} উপাত্তের সর্বোচ্চ ও সর্বনিম্ন মানের পার্থক্য কত?", v, W(v, [max(xs), v + 1, max(xs) + min(xs), v - 1]), "", lv)
def u10_mid(b, lv):
    n = R.choice([5, 7, 9]); xs = R.sample(range(1, 99), n); s = sorted(xs); v = s[n // 2]
    b.add(f"{', '.join(map(str, xs))} সংখ্যাগুলোকে ঊর্ধ্বক্রমে সাজালে মাঝের সংখ্যাটি কোনটি?", v, W(v, [xs[n // 2] if xs[n // 2] != v else s[0], s[n // 2 + 1], s[n // 2 - 1], sum(xs) // n]), "", lv)
def u10_class(b, lv):
    xs = [R.randint(30, 79) for _ in range(R.randint(12, 18))]; k = R.randrange(5); a = 30 + 10 * k; v = sum(1 for x in xs if a <= x <= a + 9)
    b.add(f"{', '.join(map(str, xs))} নম্বরগুলোর মধ্যে {a} থেকে {a + 9} এর মধ্যে কয়টি নম্বর আছে?", v, W(v, [v + 1, max(0, v - 1), v + 2, len(xs) // 5 if len(xs) // 5 != v else v + 3]), "", lv)
P10 = part(None, TOT, fx10, [u10_asc, u10_tally, u10_freq, u10_most], [u10_bar, u10_rng, u10_mid, u10_freq, u10_most], [u10_class, u10_bar, u10_mid])
save('w10', P10)
