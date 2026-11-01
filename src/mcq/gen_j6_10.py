#!/usr/bin/env python3
"""দ্বাদশ শ্রেণি উচ্চতর গণিত ২য় পত্র (h12), অধ্যায় ৬–১০। প্রতি অনুশীলনী 200, হার 30/50/20।"""
import random, pathlib, sys, math
from fractions import Fraction as F
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from mcqlib import run, save as _save, E, M, H, fr, num, pfmt, surd, sup
import re
_D1 = re.compile(r'²/1(?![\d/])')
def save(ch, items):
    for x in items:
        x['q'] = _D1.sub('²', x['q']); x['o'] = [_D1.sub('²', o) for o in x['o']]
        assert len(set(x['o'])) == 4, x
    _save(ch, items)

R = random.Random(2026110206)
def W(c, pool):
    out = []
    for w in pool:
        w = str(w)
        if w != str(c) and w not in out: out.append(w)
    return out
def nz(a, b): return R.choice([v for v in range(a, b + 1) if v])
def sq(v):
    """√v সরল রূপে (v ভগ্নাংশও হতে পারে)"""
    v = F(v)
    if v < 0: return '?'
    if v.denominator == 1:
        r = math.isqrt(v.numerator)
        return str(r) if r * r == v.numerator else surd(v.numerator)
    n, d = v.numerator, v.denominator
    rn, rd = math.isqrt(n), math.isqrt(d)
    if rn * rn == n and rd * rd == d: return fr(F(rn, rd))
    if rd * rd == d: return f"{sq(n)}/{rd}"
    return f"{sq(n * d)}/{d}"
def kx(k, v):
    k = F(k)
    if k == 1: return v
    if k == -1: return '−' + v
    return f"({num(k)}){v}" if k.denominator > 1 else f"{num(k)}{v}"
def dv(d, v): return v if d == 1 else f"{v}/{d}"
def P(x, y): return f"({num(x)}, {num(y)})"
def dec(x, k=2):
    s = f"{float(x):.{k}f}".rstrip('0').rstrip('.')
    return s.replace('-', '−')
def piF(v):
    v = F(v)
    if v == 0: return '0'
    sg = '−' if v < 0 else ''; v = abs(v)
    if v == 1: return sg + 'π'
    if v.denominator == 1: return f"{sg}{v.numerator}π"
    return f"{sg}{v.numerator if v.numerator != 1 else ''}π/{v.denominator}"
def sh(v, s):   # (x − h) রূপ
    v = F(v)
    if v == 0: return s
    return f"({s} {'−' if v > 0 else '+'} {num(abs(v))})"

# ================= 6.A পরাবৃত্ত =================
fx6a = [
 ("কণিকের উৎকেন্দ্রিকতা e = 1 হলে কণিকটি কী?", "পরাবৃত্ত", ["উপবৃত্ত", "অধিবৃত্ত", "বৃত্ত"], "", E),
 ("y² = 4ax পরাবৃত্তের শীর্ষবিন্দু কোনটি?", "(0, 0)", ["(a, 0)", "(0, a)", "(−a, 0)"], "", E),
 ("y² = 4ax পরাবৃত্তের অক্ষরেখার সমীকরণ কোনটি?", "y = 0", ["x = 0", "x = a", "y = x"], "", E),
 ("y² = 4ax পরাবৃত্তের নিয়ামকরেখা কোনটি?", "x = −a", ["x = a", "y = −a", "y = a"], "", E),
 ("y² = 4ax পরাবৃত্তের উপকেন্দ্রিক লম্বের দৈর্ঘ্য কত?", "4a", ["2a", "a", "8a"], "", E),
 ("পরাবৃত্তের উপর যেকোনো বিন্দু থেকে উপকেন্দ্র ও নিয়ামকরেখার দূরত্বের সম্পর্ক কী?", "সমান", ["দ্বিগুণ", "অর্ধেক", "যোগফল ধ্রুবক"], "", E),
 ("y² = 4ax পরাবৃত্তের পরামিতিক স্থানাঙ্ক কোনটি?", "(at², 2at)", ["(2at, at²)", "(a cos t, a sin t)", "(at, 2at²)"], "", M),
 ("x² = 4ay পরাবৃত্তের উপকেন্দ্র কোনটি?", "(0, a)", ["(a, 0)", "(0, −a)", "(−a, 0)"], "", E),
]
def e_focus(b):
    a = F(R.choice(range(1, 21)), R.choice([1, 1, 1, 2, 4])) * R.choice([1, -1]); k = 4 * a
    t = R.choice(['y', 'x'])
    eq = f"y² = {kx(k, 'x')}" if t == 'y' else f"x² = {kx(k, 'y')}"
    ok = P(a, 0) if t == 'y' else P(0, a)
    b.add(f"{eq} পরাবৃত্তের উপকেন্দ্রের স্থানাঙ্ক কোনটি?", ok, W(ok, [P(0, a) if t == 'y' else P(a, 0), P(-a, 0) if t == 'y' else P(0, -a), P(k, 0) if t == 'y' else P(0, k), P(2 * a, 0) if t == 'y' else P(0, 2 * a)]), f"4a = {num(k)} ⇒ a = {num(a)}।", E)
def e_dir(b):
    a = F(R.choice(range(1, 21)), R.choice([1, 1, 2])) * R.choice([1, -1]); k = 4 * a
    t = R.choice(['y', 'x'])
    eq = f"y² = {kx(k, 'x')}" if t == 'y' else f"x² = {kx(k, 'y')}"
    v = 'x' if t == 'y' else 'y'; o = 'y' if t == 'y' else 'x'
    ok = f"{v} = {num(-a)}"
    b.add(f"{eq} পরাবৃত্তের নিয়ামকরেখার সমীকরণ কোনটি?", ok, W(ok, [f"{v} = {num(a)}", f"{o} = {num(-a)}", f"{v} = {num(-k)}", f"{o} = {num(a)}"]), "", E)
def e_lr(b):
    a = F(R.choice(range(1, 26)), R.choice([1, 1, 2, 3])); k = 4 * a
    t = R.choice(['y² = {}x', 'x² = {}y', 'y² = −{}x', 'x² = −{}y'])
    b.add(f"{t.format(num(k))} পরাবৃত্তের উপকেন্দ্রিক লম্বের দৈর্ঘ্য কত?", num(k), W(num(k), [num(a), num(2 * a), num(8 * a), num(k + 1)]), "|4a|।", E)
def e_on(b):
    a = R.randint(1, 9); t = nz(-6, 6)
    x, y = a * t * t, 2 * a * t
    b.add(f"y² = {4 * a}x পরাবৃত্তের উপর অবস্থিত বিন্দু কোনটি?", P(x, y), W(P(x, y), [P(y, x), P(x + 1, y), P(x, y + 1), P(2 * x, y)]), f"y² = {y * y} = {4 * a}·{x}।", E)
def m_focal(b):
    a = R.randint(1, 12); x = R.randint(1, 30)
    b.add(f"y² = {4 * a}x পরাবৃত্তের উপর যে বিন্দুর ভুজ {x}, তার উপকেন্দ্রিক দূরত্ব কত?", x + a, W(x + a, [x - a if x != a else x + 2 * a, x, x + 2 * a, 4 * a + x]), "উপকেন্দ্রিক দূরত্ব = x + a।", M)
def m_shift(b):
    h, k, a = nz(-8, 8), nz(-8, 8), nz(-5, 5)
    eq = f"{sh(k, 'y')}² = {num(4 * a)}{sh(h, 'x')}"
    kind = R.choice(['শীর্ষবিন্দু', 'উপকেন্দ্র'])
    ok = P(h, k) if kind == 'শীর্ষবিন্দু' else P(h + a, k)
    b.add(f"{eq} পরাবৃত্তের {kind} কোনটি?", ok, W(ok, [P(-h, -k), P(h, k + a), P(h + a, k) if kind == 'শীর্ষবিন্দু' else P(h, k), P(h - a, k), P(k, h)]), f"X = x − ({num(h)}), Y = y − ({num(k)}), a = {num(a)}।", M)
def m_expand(b):
    k, h, a = R.randint(-6, 6), R.randint(-6, 6), nz(-4, 4)
    # y² − 2ky + k² = 4a x − 4a h ⇒ y² − 2ky − 4ax + (k² + 4ah) = 0
    eq = pfmt({kk: v for kk, v in {(0, 2): 1, (0, 1): -2 * k, (1, 0): -4 * a, (0, 0): k * k + 4 * a * h}.items() if v}, ('x', 'y'))
    ok = P(h, k)
    b.add(f"{eq} = 0 পরাবৃত্তের শীর্ষবিন্দু কোনটি?", ok, W(ok, [P(-h, -k), P(k, h), P(h + a, k), P(h, -k) if k else P(h, 1)]), "পূর্ণবর্গ করে।", M)
def m_from_focus(b):
    a = nz(-9, 9)
    ok = f"y² = {num(4 * a)}x"
    b.add(f"যে পরাবৃত্তের শীর্ষ মূলবিন্দু ও উপকেন্দ্র {P(a, 0)}, তার সমীকরণ কোনটি?", ok, W(ok, [f"y² = {num(-4 * a)}x", f"x² = {num(4 * a)}y", f"y² = {num(2 * a)}x", f"y² = {num(a)}x"]), "", M)
def m_through(b):
    x, y = R.randint(1, 12), nz(-12, 12)
    k = F(y * y, x)
    ok = f"y² = {kx(k, 'x')}"
    b.add(f"x-অক্ষ যার অক্ষ ও শীর্ষ মূলবিন্দু, এমন পরাবৃত্ত {P(x, y)} বিন্দু দিয়ে গেলে তার সমীকরণ কোনটি?", ok, W(ok, [f"x² = {kx(F(x * x, y), 'y')}", f"y² = {kx(-k, 'x')}", f"y² = {kx(k * 2, 'x')}", f"y² = {kx(k + 1, 'x')}"]), f"{y * y} = k·{x}।", M)
def m_lr_end(b):
    a = R.randint(1, 15)
    ok = f"({a}, ±{2 * a})"
    b.add(f"y² = {4 * a}x পরাবৃত্তের উপকেন্দ্রিক লম্বের প্রান্তবিন্দুদ্বয় কোনটি?", ok, W(ok, [f"({a}, ±{a})", f"({2 * a}, ±{a})", f"(±{2 * a}, {a})", f"({a}, ±{4 * a})"]), "(a, ±2a)।", M)
def h_dir_focus(b):
    # উপকেন্দ্র (p, q), নিয়ামক x = d
    p, q, d = R.randint(-6, 6), R.randint(-6, 6), R.randint(-6, 6)
    if p == d: return
    # (y − q)² = 2(p − d)(x − (p + d)/2)
    a2 = 2 * (p - d); h = F(p + d, 2)
    ok = f"{sh(q, 'y')}² = {num(a2)}{sh(h, 'x')}"
    b.add(f"যে পরাবৃত্তের উপকেন্দ্র {P(p, q)} ও নিয়ামকরেখা x = {num(d)}, তার সমীকরণ কোনটি?", ok, W(ok, [f"{sh(q, 'y')}² = {num(-a2)}{sh(h, 'x')}", f"{sh(q, 'y')}² = {num(2 * a2)}{sh(h, 'x')}", f"{sh(-q, 'y')}² = {num(a2)}{sh(-h, 'x')}" if (q or h) else f"y² = {num(a2 + 2)}x"]), "PS = PM।", H)
def h_chord(b):
    a = R.randint(1, 8); x0 = R.randint(1, 20)
    L = 2 * math.sqrt(4 * a * x0)
    ok = f"{num(2)}√{4 * a * x0}" if math.isqrt(4 * a * x0) ** 2 != 4 * a * x0 else str(2 * math.isqrt(4 * a * x0))
    ok = sq(16 * a * x0)
    b.add(f"y² = {4 * a}x পরাবৃত্তের x = {x0} জ্যা-এর দৈর্ঘ্য কত?", ok, W(ok, [sq(4 * a * x0), sq(16 * a * x0 + 4), str(4 * a * x0), sq(8 * a * x0)]), "y = ±√(4a·x₀)।", H)
def h_ptfocal(b):
    a = R.randint(1, 10); d = R.randint(a + 1, 40)
    x = d - a; y2 = 4 * a * x
    ok = f"({x}, ±{sq(y2)})"
    b.add(f"y² = {4 * a}x পরাবৃত্তের যে বিন্দুর উপকেন্দ্রিক দূরত্ব {d}, তার স্থানাঙ্ক কোনটি?", ok, W(ok, [f"({d}, ±{sq(4 * a * d)})", f"({x + 2 * a}, ±{sq(4 * a * (x + 2 * a))})", f"({x}, {sq(y2)})"]), "x + a = d।", H)
def h_param(b):
    a, t = R.randint(1, 9), nz(-5, 5)
    ok = P(a * t * t, 2 * a * t)
    b.add(f"y² = {4 * a}x পরাবৃত্তের পরামিতি t = {num(t)} বিন্দুর স্থানাঙ্ক কোনটি?", ok, W(ok, [P(2 * a * t, a * t * t), P(a * t, 2 * a * t), P(a * t * t, a * t), P(4 * a * t * t, 2 * a * t)]), "(at², 2at)।", H)
p6a = run('6.A', R, fx6a, [e_focus, e_dir, e_lr, e_on], [m_focal, m_shift, m_expand, m_from_focus, m_through, m_lr_end], [h_dir_focus, h_chord, h_ptfocal, h_param], caps=(40, 40, 30), mult=2)

# ================= 6.B উপবৃত্ত =================
fx6b = [
 ("উপবৃত্তের উৎকেন্দ্রিকতা e-এর সীমা কোনটি?", "0 < e < 1", ["e = 1", "e > 1", "e = 0"], "", E),
 ("x²/a² + y²/b² = 1 (a > b) উপবৃত্তের বৃহৎ অক্ষের দৈর্ঘ্য কত?", "2a", ["2b", "a", "a + b"], "", E),
 ("x²/a² + y²/b² = 1 (a > b) উপবৃত্তের উপকেন্দ্রিক লম্বের দৈর্ঘ্য কত?", "2b²/a", ["2a²/b", "b²/a", "2b/a"], "", E),
 ("উপবৃত্তের যেকোনো বিন্দু থেকে উপকেন্দ্রদ্বয়ের দূরত্বের যোগফল কত?", "বৃহৎ অক্ষের দৈর্ঘ্য", ["ক্ষুদ্র অক্ষের দৈর্ঘ্য", "উপকেন্দ্রিক লম্ব", "শূন্য"], "", E),
 ("x²/a² + y²/b² = 1 (a > b) হলে b² = কত?", "a²(1 − e²)", ["a²(e² − 1)", "a²e²", "a(1 − e)"], "", M),
 ("উপবৃত্তের নিয়ামকরেখাদ্বয় কোনটি? (a > b)", "x = ±a/e", ["x = ±ae", "y = ±a/e", "x = ±b/e"], "", M),
 ("e = 0 হলে উপবৃত্তটি কী হয়?", "বৃত্ত", ["পরাবৃত্ত", "সরলরেখা", "অধিবৃত্ত"], "", M),
]
TR = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29), (9, 40, 41), (12, 35, 37), (6, 8, 10), (9, 12, 15)]
def ell():
    """a > b, c² = a² − b²"""
    if R.random() < .6:
        p, q, r = R.choice(TR); k = R.choice([1, 1, 2])
        c, bb = (p, q) if R.random() < .5 else (q, p)
        return r * k, bb * k, F(c * k)
    a = R.randint(3, 13); bb = R.randint(1, a - 1)
    return a, bb, None
def ebq(a, bb): return f"{dv(a * a, 'x²')} + {dv(bb * bb, 'y²')} = 1"
def e_axis(b):
    a, bb, c = ell(); t = R.choice(['বৃহৎ', 'ক্ষুদ্র'])
    v = 2 * a if t == 'বৃহৎ' else 2 * bb
    b.add(f"{ebq(a, bb)} উপবৃত্তের {t} অক্ষের দৈর্ঘ্য কত?", v, W(v, [2 * bb if t == 'বৃহৎ' else 2 * a, a if t == 'বৃহৎ' else bb, a * a if t == 'বৃহৎ' else bb * bb, v + 2]), "", E)
def e_ecc(b):
    a, bb, c = ell()
    ok = fr(F(c, a)) if c is not None else sq(F(a * a - bb * bb, a * a))
    b.add(f"{ebq(a, bb)} উপবৃত্তের উৎকেন্দ্রিকতা কত?", ok, W(ok, [fr(F(bb, a)), sq(F(a * a + bb * bb, a * a)), sq(F(a * a - bb * bb, bb * bb)) if bb else '1', fr(F(a, a + bb))]), "e = √(1 − b²/a²)।", E)
def e_lr(b):
    a, bb, c = ell(); v = F(2 * bb * bb, a)
    b.add(f"{ebq(a, bb)} উপবৃত্তের উপকেন্দ্রিক লম্বের দৈর্ঘ্য কত?", num(v), W(num(v), [num(F(2 * a * a, bb)), num(F(bb * bb, a)), num(2 * bb), num(v + 1)]), "2b²/a।", E)
def e_cen(b):
    h, k = R.randint(-9, 9), R.randint(-9, 9); a, bb, c = ell()
    ok = P(h, k)
    b.add(f"{sh(h, 'x')}²/{a * a} + {sh(k, 'y')}²/{bb * bb} = 1 উপবৃত্তের কেন্দ্র কোনটি?", ok, W(ok, [P(-h, -k), P(k, h), P(h, -k) if k else P(h, 1), P(a, bb)]), "", E)
def m_foci(b):
    a, bb, c = ell()
    if c is None: c2 = a * a - bb * bb; ok = f"(±{sq(c2)}, 0)"; ws = [f"(0, ±{sq(c2)})", f"(±{sq(a * a + bb * bb)}, 0)", f"(±{a}, 0)"]
    else: ok = f"(±{num(c)}, 0)"; ws = [f"(0, ±{num(c)})", f"(±{a}, 0)", f"(±{bb}, 0)", f"(±{num(c + 1)}, 0)"]
    b.add(f"{ebq(a, bb)} উপবৃত্তের উপকেন্দ্রদ্বয় কোনটি?", ok, W(ok, ws), "(±ae, 0), ae = √(a² − b²)।", M)
def m_form(b):
    p, q = R.randint(1, 12), R.randint(1, 12)
    if p == q: return
    r = p * q * R.randint(1, 4)
    # px² + qy² = r ⇒ x²/(r/p) + y²/(r/q) = 1
    A2, B2 = F(r, p), F(r, q)
    big = max(A2, B2); small = min(A2, B2)
    e = sq(1 - small / big)
    b.add(f"{kx(p, 'x²')} + {kx(q, 'y²')} = {r} উপবৃত্তের উৎকেন্দ্রিকতা কত?", e, W(e, [sq(small / big), sq(1 + small / big), fr(small / big), sq(1 - small / big + F(1, 4))]), f"x²/{num(A2)} + y²/{num(B2)} = 1।", M)
def m_sum(b):
    a, bb, c = ell()
    b.add(f"{ebq(a, bb)} উপবৃত্তের উপর যেকোনো বিন্দু থেকে উপকেন্দ্রদ্বয়ের দূরত্বের যোগফল কত?", 2 * a, W(2 * a, [2 * bb, a, a + bb, 2 * a + 2]), "2a।", M)
def m_dir(b):
    a, bb, c = ell()
    if c is None: return
    v = F(a * a) / c
    ok = f"x = ±{num(v)}"
    b.add(f"{ebq(a, bb)} উপবৃত্তের নিয়ামকরেখাদ্বয়ের সমীকরণ কোনটি?", ok, W(ok, [f"x = ±{num(c)}", f"y = ±{num(v)}", f"x = ±{num(F(bb * bb) / c)}", f"x = ±{a}"]), "x = ±a/e = ±a²/c।", M)
def m_build(b):
    a, bb, c = ell()
    if c is None: return
    kind = R.choice(['ae', 'ax'])
    q = f"যে উপবৃত্তের কেন্দ্র মূলবিন্দু, বৃহৎ অক্ষ x-অক্ষ বরাবর, বৃহৎ অক্ষের দৈর্ঘ্য {2 * a} ও উৎকেন্দ্রিকতা {fr(F(c, a))}, তার সমীকরণ কোনটি?" if kind == 'ae' else f"যে উপবৃত্তের কেন্দ্র মূলবিন্দু, উপকেন্দ্র (±{num(c)}, 0) ও ক্ষুদ্র অক্ষের দৈর্ঘ্য {2 * bb}, তার সমীকরণ কোনটি?"
    ok = ebq(a, bb)
    b.add(q, ok, W(ok, [f"x²/{bb * bb} + y²/{a * a} = 1", f"x²/{a * a} − y²/{bb * bb} = 1", f"x²/{a * a} + y²/{int(c * c)} = 1", f"x²/{4 * a * a} + y²/{4 * bb * bb} = 1"]), "b² = a² − c²।", M)
def m_ydir(b):
    a, bb, c = ell()
    ok = f"(0, ±{a})"
    b.add(f"x²/{bb * bb} + y²/{a * a} = 1 উপবৃত্তের বৃহৎ অক্ষের প্রান্তবিন্দুদ্বয় কোনটি?", ok, W(ok, [f"(±{a}, 0)", f"(0, ±{bb})", f"(±{bb}, 0)", f"(0, ±{a * a})"]), "a > b হওয়ায় বৃহৎ অক্ষ y-অক্ষ বরাবর।", M)
def h_focal(b):
    a, bb, c = ell()
    if c is None: return
    x = R.choice([v for v in range(-a + 1, a) if v])
    e = F(c, a); d1, d2 = a - e * x, a + e * x
    ok = f"{num(d1)} ও {num(d2)}"
    b.add(f"{ebq(a, bb)} উপবৃত্তের উপর যে বিন্দুর ভুজ {num(x)}, তার উপকেন্দ্রিক দূরত্বদ্বয় কত?", ok, W(ok, [f"{num(a - x)} ও {num(a + x)}", f"{num(bb - e * x)} ও {num(bb + e * x)}", f"{num(d1 + 1)} ও {num(d2 - 1)}"]), "a ± ex।", H)
def h_area(b):
    a, bb, c = ell()
    ok = f"{a * bb}π"
    b.add(f"{ebq(a, bb)} উপবৃত্ত দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল কত বর্গ একক?", ok, W(ok, [f"{a * a}π", f"{2 * a * bb}π", f"{a + bb}π", f"{bb * bb}π"]), "πab।", H)
def h_shift(b):
    h, k = R.randint(-6, 6), R.randint(-6, 6); a, bb, c = ell()
    if c is None: return
    ok = f"{P(h + c, k)} ও {P(h - c, k)}"
    b.add(f"{sh(h, 'x')}²/{a * a} + {sh(k, 'y')}²/{bb * bb} = 1 উপবৃত্তের উপকেন্দ্রদ্বয় কোনটি?", ok, W(ok, [f"{P(c, 0)} ও {P(-c, 0)}", f"{P(h, k + c)} ও {P(h, k - c)}", f"{P(h + a, k)} ও {P(h - a, k)}"]), "কেন্দ্র থেকে ±c।", H)
def h_dist_ecc(b):
    # উপকেন্দ্রদ্বয়ের দূরত্ব = নিয়ামকদ্বয়ের দূরত্বের k ভাগ ⇒ e² = k
    e = R.choice([F(1, 2), F(1, 3), F(2, 3), F(3, 4), F(1, 4), F(3, 5), F(4, 5), F(2, 5)])
    b.add(f"কোনো উপবৃত্তের উপকেন্দ্রদ্বয়ের দূরত্ব নিয়ামকরেখাদ্বয়ের দূরত্বের {fr(e * e)} গুণ হলে উৎকেন্দ্রিকতা কত?", fr(e), W(fr(e), [fr(e * e), sq(e), fr(1 - e)]), "2ae / (2a/e) = e²।", H)
p6b = run('6.B', R, fx6b, [e_axis, e_ecc, e_lr, e_cen], [m_foci, m_form, m_sum, m_dir, m_build, m_ydir], [h_focal, h_area, h_shift, h_dist_ecc], caps=(40, 40, 30), mult=2)

# ================= 6.C অধিবৃত্ত =================
fx6c = [
 ("অধিবৃত্তের উৎকেন্দ্রিকতা কেমন?", "e > 1", ["e < 1", "e = 1", "e = 0"], "", E),
 ("x²/a² − y²/b² = 1 অধিবৃত্তের অসীমতটদ্বয় কোনটি?", "y = ±(b/a)x", ["y = ±(a/b)x", "x = ±a", "y = ±bx"], "", E),
 ("আয়তাকার অধিবৃত্তের উৎকেন্দ্রিকতা কত?", "√2", ["1", "2", "1/√2"], "a = b।", E),
 ("x²/a² − y²/b² = 1 হলে b² = কত?", "a²(e² − 1)", ["a²(1 − e²)", "a²e²", "a(e − 1)"], "", M),
 ("অধিবৃত্তের যেকোনো বিন্দু থেকে উপকেন্দ্রদ্বয়ের দূরত্বের অন্তর কত?", "আড় অক্ষের দৈর্ঘ্য (2a)", ["2b", "0", "উপকেন্দ্রিক লম্ব"], "", E),
 ("xy = c² কোন ধরনের কণিক?", "আয়তাকার অধিবৃত্ত", ["বৃত্ত", "পরাবৃত্ত", "উপবৃত্ত"], "", M),
 ("e₁ ও e₂ অনুবন্ধী অধিবৃত্তের উৎকেন্দ্রিকতা হলে 1/e₁² + 1/e₂² = কত?", "1", ["2", "0", "e₁e₂"], "", H),
]
def hyp():
    if R.random() < .6:
        p, q, r = R.choice(TR); k = R.choice([1, 1, 2])
        a, bb = (p, q) if R.random() < .5 else (q, p)
        return a * k, bb * k, F(r * k)
    return R.randint(1, 12), R.randint(1, 12), None
def hbq(a, bb): return f"{dv(a * a, 'x²')} − {dv(bb * bb, 'y²')} = 1"
def e_hecc(b):
    a, bb, c = hyp()
    ok = fr(F(c, a)) if c is not None else sq(F(a * a + bb * bb, a * a))
    b.add(f"{hbq(a, bb)} অধিবৃত্তের উৎকেন্দ্রিকতা কত?", ok, W(ok, [sq(F(abs(a * a - bb * bb), a * a)) if a != bb else '1', fr(F(bb, a)), sq(F(a * a + bb * bb, bb * bb)), fr(F(a + bb, a))]), "e = √(1 + b²/a²)।", E)
def e_hax(b):
    a, bb, c = hyp(); t = R.choice(['আড়', 'অনুবন্ধী'])
    v = 2 * a if t == 'আড়' else 2 * bb
    b.add(f"{hbq(a, bb)} অধিবৃত্তের {t} অক্ষের দৈর্ঘ্য কত?", v, W(v, [2 * bb if t == 'আড়' else 2 * a, a * a if t == 'আড়' else bb * bb, v + 2, a + bb]), "", E)
def e_asym(b):
    a, bb, c = hyp()
    ok = f"y = ±{fr(F(bb, a))}x".replace('±1x', '±x')
    b.add(f"{hbq(a, bb)} অধিবৃত্তের অসীমতটদ্বয়ের সমীকরণ কোনটি?", ok, W(ok, [f"y = ±{fr(F(a, bb))}x".replace('±1x', '±x'), f"y = ±{fr(F(bb * bb, a * a))}x".replace('±1x', '±x'), f"x = ±{a}", f"y = ±{fr(F(bb, a) + 1)}x"]), "y = ±(b/a)x।", E)
def e_hlr(b):
    a, bb, c = hyp(); v = F(2 * bb * bb, a)
    b.add(f"{hbq(a, bb)} অধিবৃত্তের উপকেন্দ্রিক লম্বের দৈর্ঘ্য কত?", num(v), W(num(v), [num(F(2 * a * a, bb)), num(F(bb * bb, a)), num(2 * bb), num(v + 2)]), "2b²/a।", E)
def m_hfoci(b):
    a, bb, c = hyp()
    s = num(c) if c is not None else sq(a * a + bb * bb)
    ok = f"(±{s}, 0)"
    b.add(f"{hbq(a, bb)} অধিবৃত্তের উপকেন্দ্রদ্বয় কোনটি?", ok, W(ok, [f"(0, ±{s})", f"(±{sq(abs(a * a - bb * bb))}, 0)" if a != bb else f"(±{a}, 0)", f"(±{a}, 0)", f"(±{bb}, 0)"]), "c² = a² + b²।", M)
def m_hform(b):
    p, q = R.randint(1, 12), R.randint(1, 12); r = p * q * R.randint(1, 4)
    A2, B2 = F(r, p), F(r, q)
    e = sq(1 + B2 / A2)
    b.add(f"{kx(p, 'x²')} − {kx(q, 'y²')} = {r} অধিবৃত্তের উৎকেন্দ্রিকতা কত?", e, W(e, [sq(1 + A2 / B2) if A2 != B2 else '2', sq(abs(1 - B2 / A2)) if A2 != B2 else '1', fr(B2 / A2 + 1), sq(B2 / A2)]), f"x²/{num(A2)} − y²/{num(B2)} = 1।", M)
def m_diff(b):
    a, bb, c = hyp()
    b.add(f"{hbq(a, bb)} অধিবৃত্তের উপর যেকোনো বিন্দু থেকে উপকেন্দ্রদ্বয়ের দূরত্বের অন্তর কত?", 2 * a, W(2 * a, [2 * bb, a, a + bb, 2 * a + 2]), "2a।", M)
def m_hdir(b):
    a, bb, c = hyp()
    if c is None: return
    ok = f"x = ±{num(F(a * a) / c)}"
    b.add(f"{hbq(a, bb)} অধিবৃত্তের নিয়ামকরেখাদ্বয় কোনটি?", ok, W(ok, [f"x = ±{num(c)}", f"y = ±{num(F(a * a) / c)}", f"x = ±{num(c / a)}", f"x = ±{a}"]), "x = ±a/e।", M)
def m_hbuild(b):
    a, bb, c = hyp()
    if c is None: return
    ok = hbq(a, bb)
    b.add(f"যে অধিবৃত্তের কেন্দ্র মূলবিন্দু, উপকেন্দ্র (±{num(c)}, 0) ও আড় অক্ষের দৈর্ঘ্য {2 * a}, তার সমীকরণ কোনটি?", ok, W(ok, [f"x²/{a * a} + y²/{bb * bb} = 1", f"x²/{bb * bb} − y²/{a * a} = 1", f"x²/{a * a} − y²/{int(c * c)} = 1", f"y²/{a * a} − x²/{bb * bb} = 1"]), "b² = c² − a²।", M)
def m_conj(b):
    a, bb, c = hyp()
    ok = f"y²/{bb * bb} − x²/{a * a} = 1"
    b.add(f"{hbq(a, bb)}-এর অনুবন্ধী অধিবৃত্ত কোনটি?", ok, W(ok, [f"x²/{bb * bb} − y²/{a * a} = 1", f"x²/{a * a} + y²/{bb * bb} = 1", f"y²/{a * a} − x²/{bb * bb} = 1"]), "", M)
def h_rect(b):
    a = R.randint(1, 15)
    ok = f"(±{sq(2 * a * a)}, 0)"
    b.add(f"x² − y² = {a * a} আয়তাকার অধিবৃত্তের উপকেন্দ্রদ্বয় কোনটি?", ok, W(ok, [f"(±{a}, 0)", f"(0, ±{sq(2 * a * a)})", f"(±{2 * a}, 0)", f"(±{a * a}, 0)"]), "e = √2, ae = a√2।", H)
def h_hfocal(b):
    a, bb, c = hyp()
    if c is None: return
    x = R.randint(a + 1, 4 * a + 6); e = F(c, a)
    ok = f"{num(e * x - a)} ও {num(e * x + a)}"
    b.add(f"{hbq(a, bb)} অধিবৃত্তের উপর যে বিন্দুর ভুজ {x} (x > 0), তার উপকেন্দ্রিক দূরত্বদ্বয় কত?", ok, W(ok, [f"{num(x - a)} ও {num(x + a)}", f"{num(a - e * x)} ও {num(a + e * x)}", f"{num(e * x - bb)} ও {num(e * x + bb)}"]), "ex ∓ a।", H)
def h_angle(b):
    a = R.randint(1, 9); k = R.choice([1, 3])
    bb = a * k if k == 1 else None
    if k == 1:
        q, ok = f"x²/{a * a} − y²/{a * a} = 1", '90°'
    else:
        q, ok = f"x²/{3 * a * a} − y²/{a * a} = 1", '60°'
    b.add(f"{q} অধিবৃত্তের অসীমতটদ্বয়ের অন্তর্ভুক্ত কোণ কত?", ok, W(ok, ['90°', '60°', '45°', '30°', '120°']), "tan θ = b/a; কোণ 2θ।", H)
def h_hshift(b):
    h, k = R.randint(-6, 6), R.randint(-6, 6); a, bb, c = hyp()
    ok = P(h, k)
    b.add(f"{sh(h, 'x')}²/{a * a} − {sh(k, 'y')}²/{bb * bb} = 1 অধিবৃত্তের কেন্দ্র কোনটি?", ok, W(ok, [P(-h, -k), P(k, h), P(h, -k) if k else P(h, 2), P(a, bb)]), "", H)
p6c = run('6.C', R, fx6c, [e_hecc, e_hax, e_asym, e_hlr], [m_hfoci, m_hform, m_diff, m_hdir, m_hbuild, m_conj], [h_rect, h_hfocal, h_angle, h_hshift], caps=(40, 40, 30), mult=2)
save('j6', p6a + p6b + p6c)

# ================= 7.A বিপরীত ত্রিকোণমিতিক ফাংশন =================
fx7a = [
 ("sin⁻¹x-এর মুখ্য মানের সীমা কোনটি?", "[−π/2, π/2]", ["[0, π]", "(−π/2, π/2)", "[0, 2π]"], "", E),
 ("cos⁻¹x-এর মুখ্য মানের সীমা কোনটি?", "[0, π]", ["[−π/2, π/2]", "(0, π)", "[−π, π]"], "", E),
 ("tan⁻¹x-এর মুখ্য মানের সীমা কোনটি?", "(−π/2, π/2)", ["[0, π]", "[−π/2, π/2]", "(0, π)"], "", E),
 ("sin⁻¹x + cos⁻¹x = কত?", "π/2", ["π", "0", "π/4"], "", E), ("tan⁻¹x + cot⁻¹x = কত?", "π/2", ["π", "0", "1"], "", E),
 ("sin⁻¹x-এর ডোমেন কোনটি?", "[−1, 1]", ["R", "[0, 1]", "(−1, 1)"], "", E), ("tan⁻¹x-এর ডোমেন কোনটি?", "R", ["[−1, 1]", "(0, ∞)", "[0, π]"], "", E),
 ("sin⁻¹(−x) = কত?", "−sin⁻¹x", ["sin⁻¹x", "π − sin⁻¹x", "π + sin⁻¹x"], "", M), ("cos⁻¹(−x) = কত?", "π − cos⁻¹x", ["−cos⁻¹x", "cos⁻¹x", "π + cos⁻¹x"], "", M),
 ("2tan⁻¹x = কত? (|x| < 1)", "tan⁻¹(2x/(1 − x²))", ["tan⁻¹(2x/(1 + x²))", "tan⁻¹(x²)", "tan⁻¹(2x)"], "", M),
]
SV = [('0', 0), ('1/2', F(1, 6)), ('1/√2', F(1, 4)), ('√3/2', F(1, 3)), ('1', F(1, 2))]
TV = [('0', 0), ('1/√3', F(1, 6)), ('1', F(1, 4)), ('√3', F(1, 3))]
def neg(s): return '−' + s if s != '0' else s
def e_sin(b):
    s, v = R.choice(SV); sg = R.choice([1, -1])
    f = R.choice(['sin', 'cos', 'tan'])
    if f == 'sin': arg, ans = (s if sg > 0 else neg(s)), v * sg
    elif f == 'cos': arg, ans = (s if sg > 0 else neg(s)), (F(1, 2) - v if sg > 0 else F(1, 2) + v)
    else:
        s, v = R.choice(TV); arg, ans = (s if sg > 0 else neg(s)), v * sg
    ok = piF(ans)
    b.add(f"{f}⁻¹({arg})-এর মুখ্য মান কত?", ok, W(ok, [piF(-ans) if ans else 'π/2', piF(1 - ans) if ans != F(1, 2) else 'π/6', piF(F(1, 2) - ans) if ans != F(1, 4) else 'π/3', 'π/3', 'π/6', '2π/3']), "মুখ্য মানের সীমায়।", E)
TRI = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29), (9, 40, 41), (12, 35, 37), (11, 60, 61)]
def e_comp(b):
    p, q, r = R.choice(TRI)
    if R.random() < .5: p, q = q, p
    f, g = R.choice([('sin', 'cos'), ('cos', 'sin'), ('tan', 'sin'), ('sin', 'tan'), ('cos', 'tan'), ('tan', 'cos')])
    arg = {'sin': F(p, r), 'cos': F(q, r), 'tan': F(p, q)}[g]
    ans = {'sin': F(p, r), 'cos': F(q, r), 'tan': F(p, q)}[f]
    b.add(f"{f}({g}⁻¹({fr(arg)})) = কত?", fr(ans), W(fr(ans), [fr(F(q, r)), fr(F(p, r)), fr(F(q, p)), fr(F(p, q)), fr(F(r, q))]), "সমকোণী ত্রিভুজ এঁকে।", E)
def e_inv(b):
    x = F(R.randint(-9, 9), R.randint(10, 20))
    f = R.choice(['sin', 'cos', 'tan'])
    if f == 'tan': x = F(R.randint(-30, 30), R.randint(1, 9))
    b.add(f"{f}({f}⁻¹({num(x)})) = কত?", num(x), W(num(x), [num(-x) if x else '1', num(1 / x) if x else '−1', num(x + 1), '0' if x else '1']), "", E)
def m_sum(b):
    pairs = [(F(1, 2), F(1, 3), 'π/4'), (1, 2, None), (F(1, 2), 3, None), (2, 3, '3π/4'), (F(1, 4), F(3, 5), 'π/4'), (F(1, 5), F(2, 3), 'π/4'), (F(1, 7), F(3, 4), 'π/4'), (1, F(1, 2), None), (F(1, 3), F(1, 2), 'π/4'), (3, F(1, 2), None)]
    a, c = F(R.randint(1, 9), R.randint(1, 9)), F(R.randint(1, 9), R.randint(1, 9))
    if a * c >= 1: return
    s = (a + c) / (1 - a * c)
    ok = f"tan⁻¹({num(s)})"
    b.add(f"tan⁻¹({num(a)}) + tan⁻¹({num(c)}) = কত?", ok, W(ok, [f"tan⁻¹({num(a + c)})", f"tan⁻¹({num((a - c) / (1 + a * c))})", f"tan⁻¹({num((a + c) / (1 + a * c))})", f"tan⁻¹({num(a * c)})"]), "(x + y)/(1 − xy)।", M)
def m_pi4(b):
    # tan⁻¹(1/a) + tan⁻¹(1/b) = π/4 যখন (a − 1)(b − 1) = 2
    a, c = R.choice([(2, 3), (3, 2)])
    k = R.randint(2, 15)
    # tan⁻¹(1/k) + tan⁻¹((k − 1)/(k + 1)) = π/4
    x, y = F(1, k), F(k - 1, k + 1)
    b.add(f"tan⁻¹({fr(x)}) + tan⁻¹({fr(y)}) = কত?", 'π/4', W('π/4', ['π/2', 'π/3', 'π/6', '3π/4']), "(x + y)/(1 − xy) = 1।", M)
def m_out(b):
    n = R.choice([F(2, 3), F(3, 4), F(5, 6), F(5, 4), F(7, 6), F(4, 3), F(5, 3), F(7, 4), F(11, 6)])
    f = R.choice(['sin', 'cos', 'tan'])
    t = n % (2 if f != 'tan' else 1)
    if f == 'sin': ans = t if t <= F(1, 2) else (1 - t if t <= F(3, 2) else t - 2)
    elif f == 'cos': ans = t if t <= 1 else 2 - t
    else:
        if t == F(1, 2): return
        ans = t if t < F(1, 2) else t - 1
    ok = piF(ans)
    b.add(f"{f}⁻¹({f} {piF(n)}) = কত?", ok, W(ok, [piF(n), piF(-ans) if ans else 'π', piF(1 - ans), piF(F(1, 2) - ans) if ans != F(1, 4) else 'π/6', 'π/3']), "মুখ্য মানের সীমায় আনতে হবে।", M)
def m_dbl(b):
    p, q, r = R.choice(TRI)
    if R.random() < .5: p, q = q, p
    # sin(2 sin⁻¹(p/r)) = 2pq/r²
    f = R.choice(['sin', 'cos'])
    ans = F(2 * p * q, r * r) if f == 'sin' else F(q * q - p * p, r * r)
    b.add(f"{f}(2 sin⁻¹({fr(F(p, r))})) = কত?", fr(ans), W(fr(ans), [fr(F(2 * p, r)), fr(F(p * q, r * r)), fr(-ans), fr(F(p * p - q * q, r * r)) if f == 'sin' else fr(F(2 * p * q, r * r))]), "দ্বিগুণ কোণের সূত্র।", M)
def m_eqn(b):
    s, v = R.choice(SV[1:]); f = R.choice(['sin', 'tan'])
    if f == 'tan': s, v = R.choice(TV[1:])
    k = R.randint(1, 4)
    # f⁻¹(x/k) = v·π ⇒ x = k·s
    def mul(k, s):
        return {'1/2': fr(F(k, 2)), '1': str(k), '1/√2': f"{k}/√2" if k > 1 else '1/√2', '√3/2': f"{k}√3/2".replace('2√3/2', '√3').replace('4√3/2', '2√3') if k > 1 else '√3/2', '1/√3': f"{k}/√3" if k > 1 else '1/√3', '√3': f"{k}√3" if k > 1 else '√3'}[s]
    ok = mul(k, s)
    b.add(f"{f}⁻¹(x/{k}) = {piF(v)} হলে x = কত?".replace('x/1', 'x'), ok, W(ok, [mul(k + 1, s), mul(k + 2, s), piF(v), mul(2 * k if k > 1 else 3, s)]), "", M)
def h_cos_sum(b):
    p1, q1, r1 = R.choice(TRI); p2, q2, r2 = R.choice(TRI)
    # sin⁻¹(p1/r1) + sin⁻¹(p2/r2) = sin⁻¹(p1q2 + q1p2)/(r1r2)
    v = F(p1 * q2 + q1 * p2, r1 * r2)
    if v > 1: return
    ok = f"sin⁻¹({fr(v)})"
    b.add(f"sin⁻¹({fr(F(p1, r1))}) + sin⁻¹({fr(F(p2, r2))}) = কত?", ok, W(ok, [f"sin⁻¹({fr(F(p1 * q2 - q1 * p2, r1 * r2))})", f"sin⁻¹({fr(F(p1, r1) + F(p2, r2))})" if F(p1, r1) + F(p2, r2) <= 1 else f"cos⁻¹({fr(v)})", f"cos⁻¹({fr(F(p1 * p2, r1 * r2))})", f"sin⁻¹({fr(F(p1 * p2, r1 * r2))})"]), "x√(1 − y²) + y√(1 − x²)।", H)
def h_solve(b):
    k = R.randint(2, 20)
    # tan⁻¹(x + 1) + tan⁻¹(x − 1) = tan⁻¹(2x/(2 − x²)) ; সরল প্রশ্ন: tan⁻¹x + tan⁻¹(1/x) = π/2 (x > 0)
    b.add(f"tan⁻¹({k}) + tan⁻¹(1/{k}) = কত?", 'π/2', W('π/2', ['π/4', 'π', '0', 'π/3']), "x > 0 হলে tan⁻¹x + cot⁻¹x।", H)
def h_3tan(b):
    a = F(R.randint(1, 5), R.randint(1, 7)); c = F(R.randint(1, 5), R.randint(1, 7))
    if a * c >= 1: return
    s = (a + c) / (1 - a * c)
    if s >= 1 or s.denominator > 60: return
    t = F(1) - s; t = (1 - s) / (1 + s)
    ok = fr(t)
    b.add(f"tan⁻¹({fr(a)}) + tan⁻¹({fr(c)}) + tan⁻¹(x) = π/4 হলে x = কত?", ok, W(ok, [fr(1 - s), fr(s), fr(1 / t) if t else '1', fr(t + 1)]), f"tan⁻¹x = π/4 − tan⁻¹({fr(s)})।", H)
def h_cot(b):
    p, q, r = R.choice(TRI)
    v = F(q, p)
    ok = f"cot⁻¹({fr(v)})"
    b.add(f"sin⁻¹({fr(F(p, r))})-কে cot⁻¹ আকারে প্রকাশ করলে কোনটি?", ok, W(ok, [f"cot⁻¹({fr(F(p, q))})", f"cot⁻¹({fr(F(r, q))})", f"cot⁻¹({fr(F(q, r))})"]), "", H)
p7a = run('7.A', R, fx7a, [e_sin, e_comp, e_inv], [m_sum, m_pi4, m_out, m_dbl, m_eqn], [h_cos_sum, h_solve, h_3tan, h_cot], caps=(50, 50, 30), mult=2)

# ================= 7.B ত্রিকোণমিতিক সমীকরণ =================
fx7b = [
 ("sin θ = 0 সমীকরণের সাধারণ সমাধান কোনটি?", "θ = nπ", ["θ = 2nπ", "θ = (2n + 1)π/2", "θ = nπ/2"], "", E),
 ("cos θ = 0 সমীকরণের সাধারণ সমাধান কোনটি?", "θ = (2n + 1)π/2", ["θ = nπ", "θ = 2nπ", "θ = nπ/2"], "", E),
 ("tan θ = 0 সমীকরণের সাধারণ সমাধান কোনটি?", "θ = nπ", ["θ = (2n + 1)π/2", "θ = 2nπ", "θ = nπ/4"], "", E),
 ("sin θ = sin α হলে সাধারণ সমাধান কোনটি?", "θ = nπ + (−1)ⁿα", ["θ = 2nπ ± α", "θ = nπ + α", "θ = nπ − α"], "", E),
 ("cos θ = cos α হলে সাধারণ সমাধান কোনটি?", "θ = 2nπ ± α", ["θ = nπ + (−1)ⁿα", "θ = nπ + α", "θ = 2nπ + α"], "", E),
 ("tan θ = tan α হলে সাধারণ সমাধান কোনটি?", "θ = nπ + α", ["θ = 2nπ ± α", "θ = nπ + (−1)ⁿα", "θ = 2nπ + α"], "", E),
 ("cos θ = 1 সমীকরণের সাধারণ সমাধান কোনটি?", "θ = 2nπ", ["θ = nπ", "θ = (2n + 1)π", "θ = nπ/2"], "", E),
 ("sin θ = 1 সমীকরণের সাধারণ সমাধান কোনটি?", "θ = (4n + 1)π/2", ["θ = nπ", "θ = 2nπ", "θ = (2n + 1)π"], "", M),
 ("cos θ = −1 সমীকরণের সাধারণ সমাধান কোনটি?", "θ = (2n + 1)π", ["θ = 2nπ", "θ = nπ", "θ = (4n + 1)π/2"], "", M),
]
SA = {'1/2': F(1, 6), '1/√2': F(1, 4), '√3/2': F(1, 3)}
TA = {'1/√3': F(1, 6), '1': F(1, 4), '√3': F(1, 3)}
def e_gen(b):
    f = R.choice(['sin', 'cos', 'tan']); k = R.choice([1, 1, 2, 3])
    s, a = R.choice(list((TA if f == 'tan' else SA).items()))
    th = 'θ' if k == 1 else f"{k}θ"
    if f == 'sin': ok = f"{th} = nπ + (−1)ⁿ{piF(a)}"; ws = [f"{th} = 2nπ ± {piF(a)}", f"{th} = nπ + {piF(a)}", f"{th} = nπ + (−1)ⁿ{piF(F(1, 2) - a)}"]
    elif f == 'cos': ok = f"{th} = 2nπ ± {piF(a)}"; ws = [f"{th} = nπ + (−1)ⁿ{piF(a)}", f"{th} = nπ ± {piF(a)}", f"{th} = 2nπ ± {piF(F(1, 2) - a)}"]
    else: ok = f"{th} = nπ + {piF(a)}"; ws = [f"{th} = 2nπ + {piF(a)}", f"{th} = nπ − {piF(a)}", f"{th} = nπ + {piF(F(1, 2) - a)}"]
    b.add(f"{f} {th} = {s} সমীকরণের সাধারণ সমাধান কোনটি?", ok, W(ok, ws), "", E)
def e_basic(b):
    f = R.choice(['sin', 'cos', 'tan'])
    s, a = R.choice(list((TA if f == 'tan' else SA).items()))
    sols = {'sin': [a, 1 - a], 'cos': [a, 2 - a], 'tan': [a, 1 + a]}[f]
    ok = ', '.join(piF(x) for x in sols)
    alt = {'sin': [a, 1 + a], 'cos': [a, 1 - a], 'tan': [a, 1 - a]}[f]
    b.add(f"0 ≤ θ ≤ 2π ব্যবধিতে {f} θ = {s} সমীকরণের সমাধান কোনটি?", ok, W(ok, [', '.join(piF(x) for x in alt), piF(a), ', '.join(piF(x) for x in [a, 2 - a]) if f != 'cos' else ', '.join(piF(x) for x in [a, 1 + a]), ', '.join(piF(x) for x in [F(1, 2) - a, 1 - (F(1, 2) - a)])]), "", E)
def e_neg(b):
    f = R.choice(['sin', 'cos'])
    s, a = R.choice(list(SA.items()))
    sols = [1 + a, 2 - a] if f == 'sin' else [1 - a, 1 + a]
    ok = ', '.join(piF(x) for x in sols)
    b.add(f"0 ≤ θ ≤ 2π ব্যবধিতে {f} θ = −{s} সমীকরণের সমাধান কোনটি?", ok, W(ok, [', '.join(piF(x) for x in [a, 1 - a]), ', '.join(piF(x) for x in [a, 2 - a]), ', '.join(piF(x) for x in [1 - a, 2 - a]) if f == 'sin' else ', '.join(piF(x) for x in [1 + a, 2 - a])]), "", E)
def m_count(b):
    k = R.randint(2, 9); f = R.choice(['sin', 'cos', 'tan'])
    n = {'sin': 2 * k + 1, 'cos': 2 * k, 'tan': 2 * k + 1}[f]
    b.add(f"0 ≤ θ ≤ 2π ব্যবধিতে {f} {k}θ = 0 সমীকরণের কয়টি সমাধান আছে?", n, W(n, [2 * k, 2 * k + 1, 2 * k - 1, k, 4 * k]), "", M)
def m_quad(b):
    f = R.choice(['sin', 'cos'])
    # 2f² − 3f + 1 = 0 ⇒ f = 1, 1/2
    if f == 'sin': ok = 'π/6, π/2, 5π/6'; ws = ['π/6, 5π/6', 'π/2', 'π/3, π/2, 2π/3']
    else: ok = '0, π/3, 5π/3, 2π'; ws = ['π/3, 5π/3', '0, 2π', 'π/6, 11π/6']
    q = R.choice([f"2{f}²θ − 3{f} θ + 1 = 0", f"2{f}²θ + 1 = 3{f} θ"])
    b.add(f"0 ≤ θ ≤ 2π ব্যবধিতে {q} সমীকরণের সমাধান কোনটি?", ok, W(ok, ws), "উৎপাদকে বিশ্লেষণ।", M)
def m_dbl(b):
    k = R.choice([2, 3, 4]); f = R.choice(['sin', 'cos', 'tan'])
    s, a = R.choice(list((TA if f == 'tan' else SA).items()))
    v = a / k
    ok = piF(v)
    b.add(f"{f} {k}θ = {s} সমীকরণের ক্ষুদ্রতম ধনাত্মক সমাধান কত?", ok, W(ok, [piF(a), piF(a * k), piF(v * 2), piF(F(1, 2) / k)]), "", M)
def m_sincos(b):
    c = R.choice([('sin θ + cos θ = √2', 'π/4'), ('sin θ − cos θ = 0', 'π/4'), ('√3 sin θ + cos θ = 2', 'π/3'), ('sin θ + √3 cos θ = 2', 'π/6'), ('√3 sin θ − cos θ = 0', 'π/6'), ('sin θ − √3 cos θ = 0', 'π/3'), ('tan θ = cot θ', 'π/4'), ('sin 2θ = cos θ', 'π/6'), ('sin θ = cos 2θ', 'π/6')])
    q, ok = c
    b.add(f"{q} সমীকরণের ক্ষুদ্রতম ধনাত্মক সমাধান কত?", ok, W(ok, ['π/6', 'π/4', 'π/3', 'π/2', '2π/3']), "", M)
def m_gen2(b):
    f = R.choice(['sin²', 'cos²', 'tan²'])
    s, a = R.choice([('1/4', F(1, 6)), ('1/2', F(1, 4)), ('3/4', F(1, 3))]) if f != 'tan²' else R.choice([('1/3', F(1, 6)), ('1', F(1, 4)), ('3', F(1, 3))])
    if f == 'cos²': a = {F(1, 6): F(1, 3), F(1, 3): F(1, 6), F(1, 4): F(1, 4)}[a]
    ok = f"θ = nπ ± {piF(a)}"
    b.add(f"{f}θ = {s} সমীকরণের সাধারণ সমাধান কোনটি?", ok, W(ok, [f"θ = 2nπ ± {piF(a)}", f"θ = nπ + {piF(a)}", f"θ = nπ ± {piF(F(1, 2) - a)}" if a != F(1, 4) else f"θ = nπ ± π/3"]), "", M)
def h_range(b):
    k = R.randint(1, 30)
    a, c = R.choice([(3, 4), (5, 12), (8, 15), (1, 1), (1, 2), (2, 3), (6, 8), (7, 24)])
    m = sq(a * a + c * c)
    ok = f"[−{m}, {m}]"
    b.add(f"{a} sin θ + {c} cos θ-এর মানের পরিসর কোনটি?".replace('1 sin', 'sin').replace('+ 1 cos', '+ cos'), ok, W(ok, [f"[−{a + c}, {a + c}]", f"[−1, 1]", f"[0, {m}]", f"[−{a * a + c * c}, {a * a + c * c}]"]), "±√(a² + b²)।", H)
def h_cnt(b):
    k = R.randint(1, 6); f = R.choice(['sin', 'cos']); s, a = R.choice(list(SA.items()))
    # f(kθ) = s, 0 ≤ θ < 2π: 2k সমাধান
    n = 2 * k
    b.add(f"0 ≤ θ < 2π ব্যবধিতে {f} {k}θ = {s} সমীকরণের কয়টি সমাধান আছে?".replace(' 1θ', ' θ'), n, W(n, [k, 2 * k + 1, 4 * k, 2 * k - 1, 3 * k]), "প্রতি পর্যায়ে 2টি।", H)
def h_sum(b):
    f = R.choice(['sin', 'cos', 'tan']); s, a = R.choice(list((TA if f == 'tan' else SA).items()))
    sols = {'sin': [a, 1 - a], 'cos': [a, 2 - a], 'tan': [a, 1 + a]}[f]
    v = sum(sols)
    b.add(f"0 ≤ θ ≤ 2π ব্যবধিতে {f} θ = {s} সমীকরণের সমাধানগুলোর যোগফল কত?", piF(v), W(piF(v), ['π', '2π', piF(2 * a), piF(v + F(1, 2)), '3π/2']), "", H)
def e_genneg(b):
    f = R.choice(['sin', 'cos', 'tan']); k = R.choice([1, 2, 3, 4])
    s, a = R.choice(list((TA if f == 'tan' else SA).items()))
    th = 'θ' if k == 1 else f"{k}θ"
    if f == 'sin': ok = f"{th} = nπ + (−1)ⁿ({piF(-a)})"; ws = [f"{th} = nπ + (−1)ⁿ{piF(a)}", f"{th} = 2nπ ± {piF(a)}", f"{th} = nπ − {piF(a)}"]
    elif f == 'cos': ok = f"{th} = 2nπ ± {piF(1 - a)}"; ws = [f"{th} = 2nπ ± {piF(a)}", f"{th} = nπ + (−1)ⁿ{piF(1 - a)}", f"{th} = nπ ± {piF(1 - a)}"]
    else: ok = f"{th} = nπ − {piF(a)}"; ws = [f"{th} = nπ + {piF(a)}", f"{th} = 2nπ − {piF(a)}", f"{th} = nπ + {piF(F(1, 2) - a)}"]
    b.add(f"{f} {th} = −{s} সমীকরণের সাধারণ সমাধান কোনটি?", ok, W(ok, ws), "", E)
def e_small(b):
    f = R.choice(['sin', 'cos', 'tan']); sg = R.choice([1, -1])
    s, a = R.choice(list((TA if f == 'tan' else SA).items()))
    if sg > 0: v = a
    else: v = {'sin': 1 + a, 'cos': 1 - a, 'tan': 1 - a}[f]
    ok = piF(v)
    b.add(f"{f} θ = {'' if sg > 0 else '−'}{s} সমীকরণের ক্ষুদ্রতম ধনাত্মক সমাধান কত?", ok, W(ok, [piF(a), piF(1 - a), piF(1 + a), piF(2 - a), piF(F(1, 2) + a)]), "", E)
RV = {'sec': {'2': F(1, 3), '√2': F(1, 4), '2/√3': F(1, 6)}, 'cosec': {'2': F(1, 6), '√2': F(1, 4), '2/√3': F(1, 3)}, 'cot': {'√3': F(1, 6), '1': F(1, 4), '1/√3': F(1, 3)}}
def m_rec(b):
    f = R.choice(['sec', 'cosec', 'cot']); k = R.choice([1, 2, 3])
    s, a = R.choice(list(RV[f].items()))
    th = 'θ' if k == 1 else f"{k}θ"
    if f == 'cosec': ok = f"{th} = nπ + (−1)ⁿ{piF(a)}"; ws = [f"{th} = 2nπ ± {piF(a)}", f"{th} = nπ + {piF(a)}", f"{th} = nπ + (−1)ⁿ{piF(F(1, 2) - a)}"]
    elif f == 'sec': ok = f"{th} = 2nπ ± {piF(a)}"; ws = [f"{th} = nπ + (−1)ⁿ{piF(a)}", f"{th} = nπ ± {piF(a)}", f"{th} = 2nπ ± {piF(F(1, 2) - a)}"]
    else: ok = f"{th} = nπ + {piF(a)}"; ws = [f"{th} = 2nπ + {piF(a)}", f"{th} = nπ − {piF(a)}", f"{th} = nπ + {piF(F(1, 2) - a)}"]
    b.add(f"{f} {th} = {s} সমীকরণের সাধারণ সমাধান কোনটি?", ok, W(ok, ws), "বিপরীত অনুপাতে রূপান্তর।", M)
def m_interval(b):
    f = R.choice(['sin', 'cos', 'tan']); m = R.randint(2, 6)
    s, a = R.choice(list((TA if f == 'tan' else SA).items()))
    n = m if f == 'tan' else m   # [0, mπ]: sin/cos: প্রতি 2π-তে 2টি ⇒ m টি (m জোড়/বিজোড় উভয়ক্ষেত্রে)
    if f == 'sin': n = sum(1 for j in range(m + 1) for x in (2 * j + a, 2 * j + 1 - a) if x <= m)
    elif f == 'cos': n = sum(1 for j in range(m + 1) for x in (2 * j + a, 2 * j + 2 - a) if x <= m)
    else: n = sum(1 for j in range(m + 1) if j + a <= m)
    b.add(f"0 ≤ θ ≤ {m}π ব্যবধিতে {f} θ = {s} সমীকরণের কয়টি সমাধান আছে?", n, W(n, [n + 1, n - 1, 2 * m, m + 2, n + 2]), "", M)
p7b = run('7.B', R, fx7b, [e_gen, e_basic, e_neg, e_genneg, e_small], [m_count, m_quad, m_dbl, m_sincos, m_gen2, m_rec, m_interval], [h_range, h_cnt, h_sum], caps=(50, 50, 40), mult=2)
save('j7', p7a + p7b)

# ================= 8 স্থিতিবিদ্যা =================
S60 = [(p, q, math.isqrt(p * p + q * q + p * q)) for p in range(1, 41) for q in range(p + 1, 61) if math.isqrt(p * p + q * q + p * q) ** 2 == p * p + q * q + p * q]
S120 = [(p, q, math.isqrt(p * p + q * q - p * q)) for p in range(1, 41) for q in range(p + 1, 61) if math.isqrt(p * p + q * q - p * q) ** 2 == p * p + q * q - p * q]
S90 = [(p * k, q * k, r * k) for p, q, r in TRI for k in (1, 2, 3) if r * k <= 80]
def triple(ang):
    p, q, r = R.choice({60: S60, 120: S120, 90: S90}[ang])
    return (p, q, r) if R.random() < .5 else (q, p, r)
def rt(ang): return {60: '√3', 45: '√2', 30: ''}
fx8a = [
 ("দুটি বলের লব্ধি সর্বোচ্চ হয় যখন তাদের মধ্যবর্তী কোণ কত?", "0°", ["90°", "180°", "60°"], "", E),
 ("দুটি বলের লব্ধি সর্বনিম্ন হয় যখন তাদের মধ্যবর্তী কোণ কত?", "180°", ["0°", "90°", "120°"], "", E),
 ("P ও Q বলের মধ্যবর্তী কোণ α হলে লব্ধি R² = কত?", "P² + Q² + 2PQ cos α", ["P² + Q² − 2PQ cos α", "P² + Q²", "(P + Q)² cos α"], "", E),
 ("বলের সামান্তরিক সূত্রে লব্ধি কোনটি দ্বারা নির্দেশিত হয়?", "সামান্তরিকের কর্ণ", ["সামান্তরিকের বাহু", "উচ্চতা", "ক্ষেত্রফল"], "", E),
 ("দুটি সমান বলের মধ্যবর্তী কোণ 120° হলে লব্ধির মান কত?", "প্রত্যেক বলের সমান", ["শূন্য", "দ্বিগুণ", "অর্ধেক"], "", M),
 ("বলের SI একক কোনটি?", "নিউটন", ["জুল", "ওয়াট", "পাস্কাল"], "", E),
 ("P ও Q বলের লব্ধি P-এর সাথে θ কোণ উৎপন্ন করলে tan θ = কত?", "Q sin α/(P + Q cos α)", ["P sin α/(Q + P cos α)", "Q cos α/(P + Q sin α)", "Q/P"], "", M),
]
def e_res(b):
    ang = R.choice([60, 90, 120]); p, q, r = triple(ang)
    b.add(f"{p} N ও {q} N মানের দুটি বল {ang}° কোণে ক্রিয়াশীল হলে লব্ধির মান কত নিউটন?", r, W(r, [p + q, abs(q - p), sq(p * p + q * q) if ang != 90 else math.isqrt(p * p + q * q + p * q) if False else r + 1, r + 2, r - 1]), "R² = P² + Q² + 2PQ cos α।", E)
def e_maxmin(b):
    p, q = R.sample(range(2, 60), 2); t = R.choice(['বৃহত্তম', 'ক্ষুদ্রতম'])
    v = p + q if t == 'বৃহত্তম' else abs(p - q)
    b.add(f"{p} N ও {q} N মানের দুটি বলের লব্ধির {t} মান কত নিউটন?", v, W(v, [abs(p - q) if t == 'বৃহত্তম' else p + q, sq(p * p + q * q), v + 1, max(p, q)]), "", E)
def e_equal(b):
    p = R.randint(2, 40); ang = R.choice([60, 90, 120, 180, 0])
    ok = {60: f"{p}√3", 90: f"{p}√2", 120: str(p), 180: '0', 0: str(2 * p)}[ang]
    b.add(f"{p} N মানের দুটি সমান বল {ang}° কোণে ক্রিয়াশীল হলে লব্ধি কত নিউটন?", ok, W(ok, [f"{p}√3", f"{p}√2", str(p), str(2 * p), '0', f"{2 * p}√3"]), "R = 2P cos(α/2)।", E)
def e_comp(b):
    Fv = R.randint(2, 50) * 2; ang = R.choice([30, 60, 45])
    ok = {30: (f"{Fv // 2}√3", str(Fv // 2)), 60: (str(Fv // 2), f"{Fv // 2}√3"), 45: (f"{Fv // 2}√2", f"{Fv // 2}√2")}[ang]
    okS = f"{ok[0]} N ও {ok[1]} N"
    b.add(f"{Fv} N বল অনুভূমিকের সাথে {ang}° কোণে ক্রিয়া করলে এর অনুভূমিক ও উল্লম্ব অংশক কত?", okS, W(okS, [f"{ok[1]} N ও {ok[0]} N", f"{Fv} N ও {Fv // 2} N", f"{Fv // 2} N ও {Fv // 2} N", f"{Fv}√3 N ও {Fv} N"]), "F cos α ও F sin α।", E)
def m_angle(b):
    ang = R.choice([60, 90, 120]); p, q, r = triple(ang)
    b.add(f"{p} N ও {q} N মানের দুটি বলের লব্ধি {r} N হলে বলদ্বয়ের মধ্যবর্তী কোণ কত?", f"{ang}°", W(f"{ang}°", ['60°', '90°', '120°', '45°', '30°', '150°']), "cos α = (R² − P² − Q²)/2PQ।", M)
def m_gen(b):
    p, q = R.randint(2, 20), R.randint(2, 20); ang = R.choice([60, 120, 90])
    v = p * p + q * q + {60: p * q, 120: -p * q, 90: 0}[ang]
    if math.isqrt(v) ** 2 == v: return
    ok = sq(v)
    b.add(f"{p} N ও {q} N বল {ang}° কোণে ক্রিয়াশীল হলে লব্ধি কত নিউটন?", ok, W(ok, [sq(p * p + q * q + {60: -p * q, 120: p * q, 90: 2 * p * q}[ang]), str(p + q), sq(v + 1), sq(p * p + q * q) if ang != 90 else sq(v + p * q)]), "", M)
def m_dir90(b):
    p, q, r = triple(90)
    ok = f"tan⁻¹({fr(F(q, p))})"
    b.add(f"পরস্পর লম্ব {p} N ও {q} N বলের লব্ধি {p} N বলের সাথে কত কোণ উৎপন্ন করে?", ok, W(ok, [f"tan⁻¹({fr(F(p, q))})", f"sin⁻¹({fr(F(p, r))})", f"cos⁻¹({fr(F(q, r))})", f"tan⁻¹({fr(F(q, r))})"]), "tan θ = Q/P।", M)
def m_eqang(b):
    p = R.randint(2, 30); ang = R.choice([60, 90, 120, 40, 100, 150, 70])
    ok = f"{F(ang, 2)}°".replace('/2', '')
    ok = f"{num(F(ang, 2))}°"
    b.add(f"{p} N মানের দুটি সমান বল {ang}° কোণে ক্রিয়াশীল হলে লব্ধি প্রথম বলের সাথে কত কোণ উৎপন্ন করে?", ok, W(ok, [f"{ang}°", f"{num(F(180 - ang, 2))}°", f"{num(F(ang, 3))}°", '90°']), "সমান বলের লব্ধি কোণকে সমদ্বিখণ্ডিত করে।", M)
def m_perp(b):
    # লব্ধি P-এর সাথে লম্ব হলে cos α = −P/Q
    p, q = R.choice([(1, 2), (2, 4), (3, 6), (5, 10), (4, 8), (6, 12), (7, 14), (10, 20)])
    p2, q2 = p, q
    ok = '120°'
    r = sq(q * q - p * p)
    b.add(f"{p} N ও {q} N বলের লব্ধি {p} N বলের উপর লম্ব হলে লব্ধির মান কত নিউটন?", r, W(r, [str(p + q), sq(p * p + q * q), str(q - p), sq(q * q - p * p + 1)]), "R² = Q² − P²।", M)
def h_ratio(b):
    # দুটি বলের লব্ধির বৃহত্তম ও ক্ষুদ্রতম মান দেওয়া
    p, q = sorted(R.sample(range(2, 40), 2))
    ok = f"{q} N ও {p} N"
    b.add(f"দুটি বলের লব্ধির বৃহত্তম মান {p + q} N ও ক্ষুদ্রতম মান {q - p} N হলে বলদ্বয় কত?", ok, W(ok, [f"{p + q} N ও {q - p} N", f"{q + 1} N ও {p - 1} N", f"{q} N ও {q - p} N"]), "P + Q ও P − Q।", H)
def h_double(b):
    # P ও Q-এর লব্ধি R; Q দ্বিগুণ করলে লব্ধি লম্ব…; সহজ সংস্করণ: লব্ধি = P, Q = P√3?
    ang = R.choice([60, 90, 120]); p, q, r = triple(ang)
    v = p * p + 4 * q * q + {60: 2 * p * q, 120: -2 * p * q, 90: 0}[ang]
    ok = sq(v)
    b.add(f"{p} N ও {q} N বল {ang}° কোণে ক্রিয়াশীল। দ্বিতীয় বলটি দ্বিগুণ করলে নতুন লব্ধি কত নিউটন?", ok, W(ok, [str(2 * r), sq(v + 4 * p * q) if ang != 120 else sq(v - 2 * p * q), str(r + q), sq(4 * p * p + q * q + {60: 2 * p * q, 120: -2 * p * q, 90: 0}[ang])]), "", H)
def h_three(b):
    p = R.randint(2, 30)
    ang = R.choice([(0, 120, 240, '0'), (0, 90, 180, str(p)), (0, 60, 120, str(2 * p)), (0, 90, 270, str(p))])
    ok = ang[3]
    b.add(f"{p} N মানের তিনটি সমান বল একটি বিন্দুতে x-অক্ষের সাথে যথাক্রমে {ang[0]}°, {ang[1]}° ও {ang[2]}° কোণে ক্রিয়াশীল হলে লব্ধি কত নিউটন?", ok, W(ok, ['0', str(p), str(2 * p), str(3 * p), f"{p}√3", f"{p}√2"]), "অংশকে বিভাজন করে।", H)
p8a = run('8.A', R, fx8a, [e_res, e_maxmin, e_equal, e_comp], [m_angle, m_gen, m_dir90, m_eqang, m_perp], [h_ratio, h_double, h_three], caps=(40, 50, 40), mult=2)

fx8b = [
 ("লামির উপপাদ্য কয়টি সমবিন্দু বলের ক্ষেত্রে প্রযোজ্য?", "তিনটি", ["দুটি", "চারটি", "যেকোনো সংখ্যক"], "", E),
 ("লামির উপপাদ্য অনুযায়ী P/sin α = Q/sin β = R/sin γ, যেখানে α কী?", "Q ও R-এর মধ্যবর্তী কোণ", ["P ও Q-এর মধ্যবর্তী কোণ", "P ও R-এর মধ্যবর্তী কোণ", "P-এর দিক"], "", M),
 ("তিনটি বল ভারসাম্যে থাকলে যেকোনো দুটির লব্ধি তৃতীয়টির সাথে কেমন?", "সমান ও বিপরীতমুখী", ["সমান ও একমুখী", "লম্ব", "দ্বিগুণ"], "", E),
 ("বলের ত্রিভুজ সূত্র অনুযায়ী ভারসাম্যে থাকা তিনটি বল ত্রিভুজের বাহুগুলোর কেমন?", "সমানুপাতিক", ["বিপরীত সমানুপাতিক", "সমান", "লম্ব"], "", E),
 ("মসৃণ আনত তলে W ওজনের বস্তুর উপর অভিলম্ব প্রতিক্রিয়া কত? (আনতি α)", "W cos α", ["W sin α", "W tan α", "W"], "", M),
 ("তিনটি সমান বল ভারসাম্যে থাকলে প্রতি দুটির মধ্যবর্তী কোণ কত?", "120°", ["90°", "60°", "180°"], "", E),
]
def e_three(b):
    ang = R.choice([60, 90, 120]); p, q, r = triple(ang)
    # P, Q, R ভারসাম্যে ⇒ P, Q-এর লব্ধি R, তাই P ও Q-এর মধ্যবর্তী কোণ ang
    b.add(f"{p} N, {q} N ও {r} N মানের তিনটি বল একটি বিন্দুতে ক্রিয়া করে ভারসাম্যে আছে। প্রথম দুটি বলের মধ্যবর্তী কোণ কত?", f"{ang}°", W(f"{ang}°", ['60°', '90°', '120°', '150°', '45°']), "প্রথম দুটির লব্ধি তৃতীয়টির সমান।", E)
def e_incl(b):
    Wt = R.randint(2, 40) * 2; a = R.choice([30, 60, 45]); t = R.choice(['তল বরাবর', 'অভিলম্ব'])
    tbl = {30: (str(Wt // 2), f"{Wt // 2}√3"), 60: (f"{Wt // 2}√3", str(Wt // 2)), 45: (f"{Wt // 2}√2", f"{Wt // 2}√2")}
    ok = tbl[a][0] if t == 'তল বরাবর' else tbl[a][1]
    q = f"{Wt} N ওজনের একটি বস্তু {a}° আনতির মসৃণ তলে তল বরাবর বল দ্বারা স্থির রাখা হয়েছে। প্রয়োজনীয় বল কত নিউটন?" if t == 'তল বরাবর' else f"{Wt} N ওজনের একটি বস্তু {a}° আনতির মসৃণ তলে স্থির আছে। তলের অভিলম্ব প্রতিক্রিয়া কত নিউটন?"
    b.add(q, ok, W(ok, [tbl[a][1] if t == 'তল বরাবর' else tbl[a][0], str(Wt), f"{Wt}√3", str(2 * Wt)]), "W sin α ও W cos α।", E)
def e_sym(b):
    Wt = R.randint(2, 60); th = R.choice([60, 45, 30])
    ok = {60: str(Wt), 45: f"{Wt}/√2", 30: f"{Wt}/√3"}[th]
    b.add(f"{Wt} N ওজনের একটি বস্তু দুটি সমান দৈর্ঘ্যের সুতা দ্বারা ঝুলানো, প্রতিটি সুতা উল্লম্বের সাথে {th}° কোণ করে। প্রতিটি সুতার টান কত নিউটন?", ok, W(ok, [str(Wt), f"{Wt}/√2", f"{Wt}/√3", fr(F(Wt, 2)), f"{Wt}√3"]), "2T cos θ = W।", E)
def m_perp_str(b):
    Wt = R.randint(1, 40) * 2; a = R.choice([30, 60])
    t1, t2 = (f"{Wt // 2}√3", str(Wt // 2)) if a == 30 else (str(Wt // 2), f"{Wt // 2}√3")
    ok = f"{t1} N ও {t2} N"
    b.add(f"{Wt} N ওজনের একটি বস্তু পরস্পর লম্ব দুটি সুতা দ্বারা ঝুলানো; প্রথম সুতাটি উল্লম্বের সাথে {a}° কোণ করে। সুতাদ্বয়ের টান যথাক্রমে কত?", ok, W(ok, [f"{t2} N ও {t1} N", f"{Wt} N ও {Wt} N", f"{Wt // 2} N ও {Wt // 2} N"]), "লামির উপপাদ্য: T₁ = W cos θ, T₂ = W sin θ।", M)
def m_horiz(b):
    Wt = R.randint(2, 50); a = R.choice([30, 45, 60])
    ok = {30: f"{Wt}/√3", 45: str(Wt), 60: f"{Wt}√3"}[a]
    b.add(f"{Wt} N ওজনের একটি বস্তু {a}° আনতির মসৃণ তলে অনুভূমিক বল দ্বারা স্থির রাখা হয়েছে। অনুভূমিক বলটি কত নিউটন?", ok, W(ok, [f"{Wt}/√3", str(Wt), f"{Wt}√3", f"{Wt}/2", f"{Wt}/√2"]), "F = W tan α।", M)
def m_lami(b):
    ang = R.choice([60, 90, 120]); p, q, r = triple(ang)
    # বিপরীত: তৃতীয় বল নির্ণয়
    b.add(f"তিনটি সমবিন্দু বল ভারসাম্যে আছে। দুটি বল {p} N ও {q} N এবং এদের মধ্যবর্তী কোণ {ang}° হলে তৃতীয় বলটি কত নিউটন?", r, W(r, [p + q, abs(q - p), r + 1, r + 2]), "", M)
def m_lami2(b):
    P0 = R.randint(2, 30)
    a, bb, c = R.choice([(150, 120, 90), (120, 150, 90), (120, 120, 120), (135, 135, 90), (150, 150, 60)])
    sinv = {90: F(1), 150: F(1, 2), 30: F(1, 2)}
    sv = {90: ('1', 1), 150: ('1/2', F(1, 2)), 120: ('√3/2', None), 135: ('1/√2', None), 60: ('√3/2', None)}
    # P বিপরীতে α; Q = P sin β / sin α
    def val(x):
        return {90: (1, ''), 150: (F(1, 2), ''), 120: (F(1, 2), '√3'), 135: (F(1, 2), '√2'), 60: (F(1, 2), '√3')}[x]
    ka, ra = val(a); kb, rb = val(bb)
    if ra == rb: ok = num(P0 * kb / ka)
    elif ra == '': ok = f"{num(P0 * kb / ka)}{rb}"
    elif rb == '': ok = f"{num(P0 * kb / ka)}/{ra[1:] and ra}".replace('/√', '/√')
    else: return
    b.add(f"তিনটি বল P, Q, R ভারসাম্যে আছে। Q ও R-এর মধ্যবর্তী কোণ {a}°, R ও P-এর মধ্যবর্তী কোণ {bb}° এবং P = {P0} N হলে Q = কত নিউটন?", ok, W(ok, [str(P0), str(2 * P0), f"{P0}√3", fr(F(P0, 2)), f"{P0}/√3"]), "লামির উপপাদ্য: P/sin α = Q/sin β।", M)
def h_tri(b):
    # বলের ত্রিভুজ: ABC বাহু বরাবর বল
    k = R.randint(2, 9); p, q, r = R.choice(TRI)
    b.add(f"তিনটি বল একটি ত্রিভুজের বাহু {p}, {q}, {r} একক-এর সমানুপাতিক ও সমান্তরাল হয়ে ভারসাম্যে আছে। ক্ষুদ্রতম বল {p * k} N হলে বৃহত্তম বল কত নিউটন?", r * k, W(r * k, [q * k, r, p * k + q * k, r * k + k]), "বলের ত্রিভুজ সূত্র।", H)
def h_string(b):
    # দৈর্ঘ্য L সুতার দুই প্রান্ত একই অনুভূমিক রেখায় d দূরত্বে, মাঝে W
    p, q, r = R.choice(TRI); k = R.randint(1, 4); Wt = 2 * q * R.randint(1, 6)
    # অর্ধ সুতা r, অনুভূমিক অর্ধ দূরত্ব p, উল্লম্ব q ⇒ T = W r /(2q)
    T = F(Wt * r, 2 * q)
    b.add(f"{2 * r * k} cm দীর্ঘ একটি হালকা সুতার দুই প্রান্ত একই অনুভূমিক রেখায় {2 * p * k} cm দূরে দুটি বিন্দুতে বাঁধা। সুতার মধ্যবিন্দুতে {Wt} N ওজন ঝুলালে প্রতিটি অংশের টান কত নিউটন?", num(T), W(num(T), [num(F(Wt * r, 2 * p)), num(F(Wt, 2)), num(F(Wt * q, 2 * r)), num(T + 1)]), f"cos θ = {q}/{r}; 2T cos θ = W।", H)
def h_eqforces(b):
    # দুটি সমান বল P ও তৃতীয় বল R ভারসাম্যে: R = 2P cos(θ/2)
    p = R.randint(2, 30); th = R.choice([60, 90, 120])
    ok = {60: f"{p}√3", 90: f"{p}√2", 120: str(p)}[th]
    b.add(f"{p} N মানের দুটি সমান বল {th}° কোণে ক্রিয়াশীল; তৃতীয় একটি বল এদের সাথে ভারসাম্য রক্ষা করলে তৃতীয় বলটি কত নিউটন?", ok, W(ok, [f"{p}√3", f"{p}√2", str(p), str(2 * p)]), "", H)
p8b = run('8.B', R, fx8b, [e_three, e_incl, e_sym], [m_perp_str, m_horiz, m_lami, m_lami2], [h_tri, h_string, h_eqforces], caps=(50, 50, 40), mult=2)

fx8c = [
 ("দুটি সদৃশ সমান্তরাল বলের লব্ধি কত?", "বলদ্বয়ের যোগফল", ["বলদ্বয়ের অন্তর", "শূন্য", "গুণফল"], "", E),
 ("দুটি অসদৃশ সমান্তরাল বলের লব্ধি কত?", "বলদ্বয়ের অন্তর", ["বলদ্বয়ের যোগফল", "শূন্য", "গুণফল"], "", E),
 ("দ্বন্দ্ব (couple) কী দ্বারা গঠিত?", "সমান, অসদৃশ ও অসমরেখ দুটি সমান্তরাল বল", ["সমান ও সদৃশ দুটি বল", "একই রেখায় দুটি বল", "তিনটি সমবিন্দু বল"], "", E),
 ("বলের ভ্রামকের একক কোনটি?", "নিউটন-মিটার", ["নিউটন", "জুল/সেকেন্ড", "কিলোগ্রাম"], "", E),
 ("দ্বন্দ্বের লব্ধি বল কত?", "শূন্য", ["বলদ্বয়ের যোগফল", "বলের দ্বিগুণ", "অসীম"], "", E),
 ("একটি বিন্দুর সাপেক্ষে বলের ভ্রামক = কত?", "বল × বিন্দু থেকে ক্রিয়ারেখার লম্ব দূরত্ব", ["বল × সরণ", "বল/দূরত্ব", "বল + দূরত্ব"], "", E),
]
def e_like(b):
    p, q = R.randint(2, 40), R.randint(2, 40); d = (p + q) * R.randint(1, 3)
    x = F(q * d, p + q)
    b.add(f"{p} N ও {q} N মানের দুটি সদৃশ সমান্তরাল বলের ক্রিয়ারেখার দূরত্ব {d} cm। লব্ধি {p} N বল থেকে কত দূরে ক্রিয়া করে?", f"{num(x)} cm", W(f"{num(x)} cm", [f"{num(d - x)} cm", f"{num(F(d, 2))} cm", f"{num(x + 1)} cm", f"{d} cm"]), "P·x = Q·(d − x)।", E)
def e_moment(b):
    Fv, d = R.randint(2, 60), R.randint(1, 20)
    b.add(f"{Fv} N বলের ক্রিয়ারেখা থেকে একটি বিন্দুর লম্ব দূরত্ব {d} m হলে বিন্দুটির সাপেক্ষে বলের ভ্রামক কত?", f"{Fv * d} N·m", W(f"{Fv * d} N·m", [f"{num(F(Fv, d))} N·m", f"{Fv + d} N·m", f"{Fv * d * 2} N·m"]), "", E)
def e_lres(b):
    p, q = R.sample(range(2, 60), 2); t = R.choice(['সদৃশ', 'অসদৃশ'])
    v = p + q if t == 'সদৃশ' else abs(p - q)
    b.add(f"{p} N ও {q} N মানের দুটি {t} সমান্তরাল বলের লব্ধি কত নিউটন?", v, W(v, [abs(p - q) if t == 'সদৃশ' else p + q, sq(p * p + q * q), v + 1, max(p, q)]), "", E)
def e_couple(b):
    Fv, d = R.randint(2, 50), R.randint(1, 20)
    b.add(f"একটি দ্বন্দ্বের প্রতিটি বল {Fv} N এবং বাহুর দৈর্ঘ্য {d} m হলে দ্বন্দ্বের ভ্রামক কত?", f"{Fv * d} N·m", W(f"{Fv * d} N·m", [f"{2 * Fv * d} N·m", f"{num(F(Fv * d, 2))} N·m", f"{Fv + d} N·m"]), "", E)
def m_unlike(b):
    q, p = sorted(R.sample(range(2, 40), 2)); d = (p - q) * R.randint(1, 4)
    x = F(q * d, p - q)
    b.add(f"{p} N ও {q} N মানের দুটি অসদৃশ সমান্তরাল বলের ক্রিয়ারেখার দূরত্ব {d} cm। লব্ধি বৃহত্তর বল থেকে কত দূরে ক্রিয়া করে?", f"{num(x)} cm", W(f"{num(x)} cm", [f"{num(x + d)} cm", f"{num(F(q * d, p + q))} cm", f"{num(F(p * d, p - q))} cm"]), "P·x = Q·(x + d)।", M)
def m_lever(b):
    w1, d1 = R.randint(2, 40), R.randint(1, 15); d2 = R.randint(1, 15)
    w2 = F(w1 * d1, d2)
    b.add(f"একটি হালকা দণ্ডের অবলম্বন থেকে {d1} cm দূরে {w1} N ওজন ঝুলানো। অপর পাশে {d2} cm দূরে কত ওজন ঝুলালে দণ্ডটি অনুভূমিক থাকবে?", f"{num(w2)} N", W(f"{num(w2)} N", [f"{num(F(w1 * d2, d1))} N", f"{w1} N", f"{num(w2 + 1)} N"]), "ভ্রামক সমান।", M)
def m_rod(b):
    L = R.randint(2, 12) * 2; Wt = R.randint(2, 30) * 2; w = R.randint(1, 30); x = R.randint(1, L - 1)
    RA = F(Wt, 2) + F(w * (L - x), L); RB = Wt + w - RA
    ok = f"{num(RA)} N ও {num(RB)} N"
    b.add(f"{L} m দীর্ঘ ও {Wt} N ওজনের একটি সুষম দণ্ড A ও B প্রান্তে অবলম্বনের উপর আছে। A থেকে {x} m দূরে {w} N ওজন রাখলে A ও B-এর প্রতিক্রিয়া যথাক্রমে কত?", ok, W(ok, [f"{num(RB)} N ও {num(RA)} N", f"{num(F(Wt + w, 2))} N ও {num(F(Wt + w, 2))} N", f"{num(RA + 1)} N ও {num(RB - 1)} N"]), "B-এর সাপেক্ষে ভ্রামক নিয়ে।", M)
def m_find(b):
    p, q = R.randint(2, 30), R.randint(2, 30); d = (p + q) * R.randint(1, 3)
    x = F(q * d, p + q)
    b.add(f"দুটি সদৃশ সমান্তরাল বলের লব্ধি {p + q} N এবং এটি {p} N বল থেকে {num(x)} cm দূরে ক্রিয়া করে। বলদ্বয়ের ক্রিয়ারেখার দূরত্ব {d} cm হলে অপর বলটি কত?", f"{q} N", W(f"{q} N", [f"{p} N", f"{p + q} N", f"{q + 1} N"]), "", M)
def h_pos(b):
    # দণ্ডের ভারকেন্দ্র: দুই প্রান্তে ওজন
    L = R.randint(2, 20); w1, w2 = R.randint(1, 30), R.randint(1, 30)
    x = F(w2 * L, w1 + w2)
    b.add(f"{L} m দীর্ঘ একটি হালকা দণ্ডের A প্রান্তে {w1} N ও B প্রান্তে {w2} N ওজন ঝুলানো। দণ্ডটি A থেকে কত দূরে অবলম্বন দিলে অনুভূমিক থাকবে?", f"{num(x)} m", W(f"{num(x)} m", [f"{num(L - x)} m", f"{num(F(L, 2))} m", f"{num(F(w1 * L, w2)) if w2 else 1} m"]), "", H)
def h_shift(b):
    # একটি বল Q-কে k গুণ করলে লব্ধি কত সরে
    p, q = R.randint(2, 20), R.randint(2, 20); d = R.randint(1, 10) * 6
    x1 = F(q * d, p + q); x2 = F(2 * q * d, p + 2 * q)
    ok = f"{num(x2 - x1)} cm"
    b.add(f"{p} N ও {q} N মানের দুটি সদৃশ সমান্তরাল বলের দূরত্ব {d} cm। দ্বিতীয় বলটি দ্বিগুণ করলে লব্ধির ক্রিয়াবিন্দু কত সরে যাবে?", ok, W(ok, [f"{num(x1)} cm", f"{num(x2)} cm", f"{num(x2 - x1 + 1)} cm"]), "", H)
def h_couple2(b):
    # বর্গের বাহু a, বাহু বরাবর বল: দুটি দ্বন্দ্ব
    a, P1, P2 = R.randint(1, 10), R.randint(1, 20), R.randint(1, 20)
    v = abs(P1 - P2) * a
    b.add(f"{a} m বাহুবিশিষ্ট বর্গ ABCD-এর AB ও CD বাহু বরাবর বিপরীতমুখী {P1} N বল এবং BC ও DA বাহু বরাবর বিপরীতমুখী {P2} N বল এমনভাবে ক্রিয়া করে যে দ্বন্দ্ব দুটি বিপরীত দিকে ঘোরায়। লব্ধি দ্বন্দ্বের ভ্রামক কত?", f"{v} N·m", W(f"{v} N·m", [f"{(P1 + P2) * a} N·m", f"{abs(P1 - P2)} N·m", f"{2 * v + a} N·m"]), "", H)
p8c = run('8.C', R, fx8c, [e_like, e_moment, e_lres, e_couple], [m_unlike, m_lever, m_rod, m_find], [h_pos, h_shift, h_couple2], caps=(40, 50, 40), mult=2)
save('j8', p8a + p8b + p8c)

# ================= 9 সমতলে বস্তুকণার গতি =================
def ms(v): return f"{dec(v)} m/s"
def mm(v): return f"{dec(v)} m"
def se(v): return f"{dec(v)} s"
fx9a = [
 ("সমত্বরণে চলমান বস্তুর ক্ষেত্রে v = কত?", "u + at", ["u − at", "ut + ½at²", "u² + 2as"], "", E),
 ("সমত্বরণে চলমান বস্তুর অতিক্রান্ত দূরত্ব s = কত?", "ut + ½at²", ["u + at", "vt + at²", "½ut²"], "", E),
 ("সমত্বরণে v² = কত?", "u² + 2as", ["u² − as", "u + 2as", "2as − u²"], "", E),
 ("t-তম সেকেন্ডে অতিক্রান্ত দূরত্ব কোনটি?", "u + ½a(2t − 1)", ["u + at", "ut + ½at²", "u + a(t − 1)"], "", M),
 ("বেগ-সময় লেখচিত্রের ঢাল কী নির্দেশ করে?", "ত্বরণ", ["সরণ", "বেগ", "দূরত্ব"], "", E),
 ("বেগ-সময় লেখচিত্রের নিচের ক্ষেত্রফল কী নির্দেশ করে?", "সরণ", ["ত্বরণ", "বেগ", "বল"], "", E),
 ("36 km/h = কত m/s?", "10 m/s", ["36 m/s", "1 m/s", "100 m/s"], "", E),
 ("সুষম বেগে চলমান বস্তুর ত্বরণ কত?", "শূন্য", ["ধ্রুবক অশূন্য", "অসীম", "বেগের সমান"], "", E),
]
def e_v(b):
    u, a, t = R.randint(0, 30), R.randint(1, 10), R.randint(1, 20)
    v = u + a * t
    b.add(f"একটি বস্তু {u} m/s আদিবেগ ও {a} m/s² সমত্বরণে চলছে। {t} সেকেন্ড পর বেগ কত?", ms(v), W(ms(v), [ms(u * t + a), ms(a * t), ms(u + a * t * t), ms(v + a)]), "v = u + at।", E)
def e_s(b):
    u, a, t = R.randint(0, 20), R.randint(1, 10) * 2, R.randint(1, 15)
    s = u * t + a * t * t // 2
    b.add(f"{u} m/s আদিবেগ ও {a} m/s² ত্বরণে চলমান বস্তু {t} সেকেন্ডে কত দূরত্ব অতিক্রম করে?", mm(s), W(mm(s), [mm(u * t + a * t * t), mm(u * t), mm(u + a * t), mm(s + a)]), "s = ut + ½at²।", E)
def e_kmh(b):
    k = R.randint(1, 30) * 18
    v = k * 5 // 18
    b.add(f"{k} km/h = কত m/s?", ms(v), W(ms(v), [ms(k * 18 // 5) if k * 18 % 5 == 0 else ms(v * 2), ms(v + 5), ms(k), ms(v * 10)]), "×5/18।", E)
def e_stop(b):
    a = R.randint(1, 10); t = R.randint(1, 20); u = a * t
    b.add(f"{u} m/s বেগে চলমান একটি গাড়ি {a} m/s² মন্দনে কত সেকেন্ডে থামবে?", se(t), W(se(t), [se(u * a), se(t * 2), se(t + 1), se(u)]), "0 = u − at।", E)
def m_v2(b):
    u, a, s = R.randint(0, 20), R.randint(1, 10), R.randint(1, 40)
    v2 = u * u + 2 * a * s
    ok = ms(math.isqrt(v2)) if math.isqrt(v2) ** 2 == v2 else f"{sq(v2)} m/s"
    b.add(f"{u} m/s আদিবেগ ও {a} m/s² ত্বরণে {s} m যাওয়ার পর বেগ কত?", ok, W(ok, [f"{sq(v2 + 2 * a)} m/s", f"{sq(u * u + a * s)} m/s" if u * u + a * s != v2 else '0 m/s', ms(u + a * s), f"{sq(abs(u * u - 2 * a * s))} m/s"]), "v² = u² + 2as।", M)
def m_nth(b):
    u, a, n = R.randint(0, 20), R.randint(1, 10) * 2, R.randint(2, 15)
    s = u + a * (2 * n - 1) // 2
    b.add(f"{u} m/s আদিবেগ ও {a} m/s² ত্বরণে চলমান বস্তু {n}-তম সেকেন্ডে কত দূরত্ব অতিক্রম করে?", mm(s), W(mm(s), [mm(u * n + a * n * n // 2), mm(u + a * n), mm(u + a * (n - 1)), mm(s + a)]), "sₙ = u + ½a(2n − 1)।", M)
def m_stopdist(b):
    a = R.randint(1, 10); u = a * R.randint(1, 10) * 2
    s = F(u * u, 2 * a)
    b.add(f"{u} m/s বেগে চলমান একটি বস্তু {a} m/s² মন্দনে থামার আগে কত দূরত্ব অতিক্রম করবে?", mm(s), W(mm(s), [mm(F(u * u, a)), mm(F(u, a)), mm(s / 2), mm(s + u)]), "0 = u² − 2as।", M)
def m_acc(b):
    u, v, t = R.randint(0, 30), R.randint(31, 90), R.randint(1, 20)
    a = F(v - u, t)
    b.add(f"একটি বস্তুর বেগ {t} সেকেন্ডে {u} m/s থেকে {v} m/s হয়। ত্বরণ কত?", f"{num(a)} m/s²", W(f"{num(a)} m/s²", [f"{num(F(v + u, t))} m/s²", f"{num(F(v, t))} m/s²", f"{v - u} m/s²", f"{num(a * 2)} m/s²"]), "a = (v − u)/t।", M)
def m_avg(b):
    u, a, t = R.randint(0, 30), R.randint(1, 10) * 2, R.randint(1, 15)
    v = u + a * t; av = F(u + v, 2)
    b.add(f"{u} m/s আদিবেগ ও {a} m/s² সমত্বরণে {t} সেকেন্ড চললে গড় বেগ কত?", ms(av), W(ms(av), [ms(v), ms(F(v, 2)), ms(av + a), ms(u + a)]), "(u + v)/2।", M)
def h_ratio(b):
    # স্থির অবস্থা থেকে: প্রথম, দ্বিতীয়, তৃতীয় সেকেন্ডের দূরত্বের অনুপাত
    n = R.randint(2, 6)
    ok = ' : '.join(str(2 * i - 1) for i in range(1, n + 1))
    b.add(f"স্থির অবস্থা থেকে সমত্বরণে চলমান বস্তুর প্রথম {n} টি ধারাবাহিক সেকেন্ডে অতিক্রান্ত দূরত্বের অনুপাত কোনটি?", ok, W(ok, [' : '.join(str(i) for i in range(1, n + 1)), ' : '.join(str(i * i) for i in range(1, n + 1)), ' : '.join(str(2 * i) for i in range(1, n + 1))]), "", H)
def h_two(b):
    # t₁ ও t₂ সেকেন্ডে s₁, s₂ দূরত্ব থেকে u, a
    u, a = R.randint(1, 15), R.randint(1, 6) * 2; t1 = R.randint(1, 5); t2 = t1 + R.randint(1, 5)
    s1, s2 = u * t1 + a * t1 * t1 // 2, u * t2 + a * t2 * t2 // 2
    ok = f"{u} m/s ও {a} m/s²"
    b.add(f"সমত্বরণে চলমান একটি বস্তু প্রথম {t1} সেকেন্ডে {s1} m এবং প্রথম {t2} সেকেন্ডে {s2} m যায়। আদিবেগ ও ত্বরণ কত?", ok, W(ok, [f"{a} m/s ও {u} m/s²", f"{u + 1} m/s ও {a - 1} m/s²", f"{u} m/s ও {a * 2} m/s²"]), "s = ut + ½at² দুটি সমীকরণ।", H)
def h_chase(b):
    # একটি গাড়ি স্থির থেকে a ত্বরণে, অপরটি সুষম v বেগে একই সময়ে একই স্থান থেকে
    a = R.randint(1, 6) * 2; v = R.randint(2, 30)
    t = F(2 * v, a)
    b.add(f"একটি গাড়ি স্থির অবস্থা থেকে {a} m/s² ত্বরণে এবং অপর একটি গাড়ি {v} m/s সুষম বেগে একই সময়ে একই স্থান থেকে একই দিকে যাত্রা শুরু করে। কত সেকেন্ড পর প্রথম গাড়িটি দ্বিতীয়টিকে ধরবে?", se(t), W(se(t), [se(F(v, a)), se(t * 2), se(t + 1), se(v)]), "½at² = vt।", H)
p9a = run('9.A', R, fx9a, [e_v, e_s, e_kmh, e_stop], [m_v2, m_nth, m_stopdist, m_acc, m_avg], [h_ratio, h_two, h_chase], caps=(40, 50, 40), mult=2)

fx9b = [
 ("অভিকর্ষজ ত্বরণ g-এর আদর্শ মান কত?", "9.8 m/s²", ["10.8 m/s²", "8.9 m/s²", "98 m/s²"], "", E),
 ("u বেগে খাড়া উপরে নিক্ষিপ্ত বস্তুর সর্বোচ্চ উচ্চতা কত?", "u²/2g", ["u²/g", "2u/g", "u/2g"], "", E),
 ("u বেগে খাড়া উপরে নিক্ষিপ্ত বস্তুর সর্বোচ্চ উচ্চতায় পৌঁছাতে সময় কত?", "u/g", ["2u/g", "u²/g", "u/2g"], "", E),
 ("খাড়া উপরে নিক্ষিপ্ত বস্তুর সর্বোচ্চ উচ্চতায় বেগ কত?", "শূন্য", ["u", "g", "u/2"], "", E),
 ("বায়ুশূন্য স্থানে পালক ও পাথর একসাথে ছেড়ে দিলে কী ঘটে?", "একসাথে মাটিতে পড়ে", ["পাথর আগে পড়ে", "পালক আগে পড়ে", "পালক ভাসতে থাকে"], "", E),
 ("u বেগে খাড়া উপরে নিক্ষিপ্ত বস্তু কত সময় পর নিক্ষেপ বিন্দুতে ফিরে আসে?", "2u/g", ["u/g", "u²/2g", "4u/g"], "", E),
]
def e_maxh(b):
    k = R.randint(1, 10); u = F(98, 10) * k
    Hh = F(49, 10) * k * k
    b.add(f"একটি বস্তুকে {dec(u)} m/s বেগে খাড়া উপরের দিকে নিক্ষেপ করা হলো। সর্বোচ্চ উচ্চতা কত? (g = 9.8 m/s²)", mm(Hh), W(mm(Hh), [mm(2 * Hh), mm(Hh / 2), mm(u * k), mm(Hh + F(49, 10))]), "H = u²/2g।", E)
def e_tup(b):
    k = R.randint(1, 15); g = R.choice([10, F(98, 10)]); u = g * k
    b.add(f"{dec(u)} m/s বেগে খাড়া উপরে নিক্ষিপ্ত বস্তু কত সময় পর নিক্ষেপ বিন্দুতে ফিরে আসবে? (g = {dec(g)} m/s²)", se(2 * k), W(se(2 * k), [se(k), se(4 * k), se(2 * k + 1), se(u)]), "T = 2u/g।", E)
def e_fall(b):
    t = R.randint(1, 10); g = R.choice([10, F(98, 10)])
    v = g * t
    b.add(f"স্থির অবস্থা থেকে মুক্তভাবে পড়ন্ত বস্তুর {t} সেকেন্ড পর বেগ কত? (g = {dec(g)} m/s²)", ms(v), W(ms(v), [ms(g * t * t / 2), ms(g / t), ms(v + g), ms(2 * v)]), "v = gt।", E)
def e_fallh(b):
    t = R.randint(1, 10); g = R.choice([10, F(98, 10)])
    h = g * t * t / 2
    b.add(f"মুক্তভাবে পড়ন্ত বস্তু {t} সেকেন্ডে কত দূরত্ব অতিক্রম করে? (g = {dec(g)} m/s²)", mm(h), W(mm(h), [mm(g * t * t), mm(g * t), mm(h / 2), mm(h + g)]), "h = ½gt²।", E)
def m_hfrom(b):
    t = R.randint(1, 10); g = R.choice([10, F(98, 10)])
    h = g * t * t / 2
    b.add(f"{dec(h)} m উচ্চতা থেকে একটি বস্তু ছেড়ে দিলে কত সময়ে মাটিতে পৌঁছাবে? (g = {dec(g)} m/s²)", se(t), W(se(t), [se(2 * t), se(t * t), se(t + 1), se(F(t, 2))]), "t = √(2h/g)।", M)
def m_vground(b):
    t = R.randint(1, 10); g = R.choice([10, F(98, 10)])
    h = g * t * t / 2
    b.add(f"{dec(h)} m উচ্চতা থেকে মুক্তভাবে পড়ন্ত বস্তু কত বেগে মাটিতে আঘাত করবে? (g = {dec(g)} m/s²)", ms(g * t), W(ms(g * t), [ms(g * t * 2), ms(h), ms(g * t / 2), ms(g * t + g)]), "v = √(2gh)।", M)
def m_nthfall(b):
    n = R.randint(2, 10); g = R.choice([10, F(98, 10)])
    s = g * (2 * n - 1) / 2
    b.add(f"মুক্তভাবে পড়ন্ত বস্তু {n}-তম সেকেন্ডে কত দূরত্ব অতিক্রম করে? (g = {dec(g)} m/s²)", mm(s), W(mm(s), [mm(g * n * n / 2), mm(g * n), mm(g * (2 * n + 1) / 2), mm(s + g)]), "½g(2n − 1)।", M)
def m_ufromh(b):
    k = R.randint(1, 12); g = R.choice([10, F(98, 10)])
    u = g * k; Hh = g * k * k / 2
    b.add(f"খাড়া উপরে নিক্ষিপ্ত একটি বস্তু সর্বোচ্চ {dec(Hh)} m উচ্চতায় ওঠে। নিক্ষেপ বেগ কত? (g = {dec(g)} m/s²)", ms(u), W(ms(u), [ms(u * 2), ms(Hh / 2), ms(u + g), ms(g * k * k)]), "u = √(2gH)।", M)
def m_height_t(b):
    k = R.randint(2, 10); g = 10; u = g * k; t = R.randint(1, k - 1) if k > 1 else 1
    h = u * t - g * t * t // 2
    b.add(f"{u} m/s বেগে খাড়া উপরে নিক্ষিপ্ত বস্তু {t} সেকেন্ড পর কত উচ্চতায় থাকবে? (g = 10 m/s²)", mm(h), W(mm(h), [mm(u * t), mm(u * t + g * t * t // 2), mm(h + g), mm(g * t * t // 2)]), "h = ut − ½gt²।", M)
def h_twotimes(b):
    t1, t2 = sorted(R.sample(range(1, 12), 2)); g = R.choice([10, F(98, 10)])
    u = g * (t1 + t2) / 2; h = g * t1 * t2 / 2
    b.add(f"খাড়া উপরে নিক্ষিপ্ত একটি বস্তু {t1} s ও {t2} s সময়ে একই উচ্চতায় থাকে। উচ্চতাটি কত? (g = {dec(g)} m/s²)", mm(h), W(mm(h), [mm(g * t1 * t2), mm(g * (t1 + t2) / 2), mm(h + g), mm(g * (t2 - t1) ** 2 / 2) if t2 - t1 > 1 else mm(h * 3)]), "h = ½g t₁t₂।", H)
def h_tower(b):
    # টাওয়ার থেকে u বেগে উপরে নিক্ষেপ, T সময়ে মাটিতে
    g = 10; u = R.randint(1, 6) * 10; T = R.randint(u // 10 * 2 + 1, u // 10 * 2 + 8)
    h = -u * T + g * T * T // 2
    b.add(f"একটি টাওয়ারের চূড়া থেকে {u} m/s বেগে খাড়া উপরে নিক্ষিপ্ত বস্তু {T} সেকেন্ড পর মাটিতে পড়ে। টাওয়ারের উচ্চতা কত? (g = 10 m/s²)", mm(h), W(mm(h), [mm(u * T + g * T * T // 2), mm(g * T * T // 2), mm(h + u), mm(abs(u * T - g * T * T // 2) + 10)]), "−h = uT − ½gT²।", H)
def h_drop2(b):
    # একটি বস্তু ছেড়ে দেওয়ার t₀ s পর অন্যটি
    g = 10; t0 = R.randint(1, 4); t = R.randint(t0 + 1, 10)
    d = F(g * t * t, 2) - F(g * (t - t0) ** 2, 2)
    b.add(f"একটি উঁচু স্থান থেকে একটি বস্তু ছেড়ে দেওয়ার {t0} s পর আরেকটি বস্তু ছেড়ে দেওয়া হলো। প্রথম বস্তু ছাড়ার {t} s পর বস্তুদ্বয়ের দূরত্ব কত? (g = 10 m/s²)", mm(d), W(mm(d), [mm(F(g * t0 * t0, 2)), mm(g * t * t0), mm(d + g), mm(F(g * t * t, 2))]), "", H)
p9b = run('9.B', R, fx9b, [e_maxh, e_tup, e_fall, e_fallh], [m_hfrom, m_vground, m_nthfall, m_ufromh, m_height_t], [h_twotimes, h_tower, h_drop2], caps=(40, 50, 40), mult=2)

fx9c = [
 ("প্রক্ষেপকের গতিপথ কোন আকৃতির?", "পরাবৃত্ত", ["বৃত্ত", "উপবৃত্ত", "সরলরেখা"], "", E),
 ("প্রক্ষেপকের অনুভূমিক পাল্লা R = কত?", "u² sin 2α/g", ["u² sin α/g", "2u sin α/g", "u² sin²α/2g"], "", E),
 ("প্রক্ষেপকের সর্বোচ্চ উচ্চতা H = কত?", "u² sin²α/2g", ["u² sin 2α/g", "u sin α/g", "u²/2g"], "", E),
 ("প্রক্ষেপকের বিচরণকাল T = কত?", "2u sin α/g", ["u sin α/g", "u² sin 2α/g", "2u cos α/g"], "", E),
 ("কোন নিক্ষেপ কোণে প্রক্ষেপকের অনুভূমিক পাল্লা সর্বাধিক হয়?", "45°", ["30°", "60°", "90°"], "", E),
 ("প্রক্ষেপকের গতিপথের সর্বোচ্চ বিন্দুতে বেগ কত?", "u cos α", ["0", "u sin α", "u"], "", M),
 ("α ও (90° − α) কোণে একই বেগে নিক্ষিপ্ত প্রক্ষেপকের কোন রাশি সমান হয়?", "অনুভূমিক পাল্লা", ["সর্বোচ্চ উচ্চতা", "বিচরণকাল", "সর্বোচ্চ উচ্চতায় বেগ"], "", M),
 ("প্রক্ষেপকের অনুভূমিক বেগের অংশক কেমন থাকে?", "ধ্রুবক", ["ক্রমশ কমে", "ক্রমশ বাড়ে", "শূন্য"], "", E),
]
def e_maxr(b):
    k = R.randint(1, 12); g = R.choice([10, F(98, 10)])
    u = 10 * k if g == 10 else 7 * k
    Rr = F(u * u) / g
    b.add(f"{u} m/s বেগে নিক্ষিপ্ত প্রক্ষেপকের সর্বাধিক অনুভূমিক পাল্লা কত? (g = {dec(g)} m/s²)", mm(Rr), W(mm(Rr), [mm(Rr / 2), mm(Rr * 2), mm(F(u * u) / (2 * g)), mm(Rr + 1)]), "R_max = u²/g।", E)
def e_T(b):
    k = R.randint(1, 10); g = R.choice([10, F(98, 10)]); a = R.choice([30, 90])
    u = g * k * (2 if a == 30 else 1)
    T = 2 * k
    b.add(f"{dec(u)} m/s বেগে অনুভূমিকের সাথে {a}° কোণে নিক্ষিপ্ত প্রক্ষেপকের বিচরণকাল কত? (g = {dec(g)} m/s²)", se(T), W(se(T), [se(k), se(2 * T), se(T + 1), se(4 * k + 2)]), "T = 2u sin α/g।", E)
def e_comp(b):
    u = R.randint(1, 30) * 2; a = R.choice([30, 60, 45])
    h, v = {30: (f"{u // 2}√3", str(u // 2)), 60: (str(u // 2), f"{u // 2}√3"), 45: (f"{u // 2}√2", f"{u // 2}√2")}[a]
    ok = f"{h} m/s ও {v} m/s"
    b.add(f"{u} m/s বেগে অনুভূমিকের সাথে {a}° কোণে নিক্ষিপ্ত প্রক্ষেপকের আদিবেগের অনুভূমিক ও উল্লম্ব অংশক কত?", ok, W(ok, [f"{v} m/s ও {h} m/s", f"{u} m/s ও {u // 2} m/s", f"{u // 2} m/s ও {u // 2} m/s"]), "u cos α ও u sin α।", E)
def m_range(b):
    k = R.randint(1, 10); g = R.choice([10, F(98, 10)]); a = R.choice([15, 75, 45])
    u = 10 * k if g == 10 else 7 * k
    Rr = F(u * u) / g * (F(1, 2) if a != 45 else 1)
    b.add(f"{u} m/s বেগে অনুভূমিকের সাথে {a}° কোণে নিক্ষিপ্ত প্রক্ষেপকের অনুভূমিক পাল্লা কত? (g = {dec(g)} m/s²)", mm(Rr), W(mm(Rr), [mm(Rr * 2) if a != 45 else mm(Rr / 2), mm(F(u * u) / g * 3 / 4), mm(Rr + 5), mm(F(u, 1) / g * 2)]), "R = u² sin 2α/g।", M)
def m_H(b):
    k = R.randint(1, 10); g = R.choice([10, F(98, 10)]); a = R.choice([30, 90])
    u = g * k * (2 if a == 30 else 1)
    Hh = g * k * k / 2
    b.add(f"{dec(u)} m/s বেগে অনুভূমিকের সাথে {a}° কোণে নিক্ষিপ্ত প্রক্ষেপকের সর্বোচ্চ উচ্চতা কত? (g = {dec(g)} m/s²)", mm(Hh), W(mm(Hh), [mm(Hh * 2), mm(Hh * 4), mm(Hh / 2), mm(Hh + g)]), "H = u² sin²α/2g।", M)
def m_horiz(b):
    t = R.randint(1, 8); g = R.choice([10, F(98, 10)]); u = R.randint(2, 40)
    h = g * t * t / 2
    b.add(f"{dec(h)} m উঁচু একটি স্থান থেকে {u} m/s বেগে অনুভূমিকভাবে নিক্ষিপ্ত বস্তু ভূমিতে কত দূরে পড়বে? (g = {dec(g)} m/s²)", mm(u * t), W(mm(u * t), [mm(u * t * 2), mm(h), mm(u * t + u), mm(u * t * t)]), "x = u√(2h/g)।", M)
def m_top(b):
    u = R.randint(1, 30) * 2; a = R.choice([30, 60, 45])
    ok = {30: f"{u // 2}√3", 60: str(u // 2), 45: f"{u // 2}√2"}[a] + ' m/s'
    b.add(f"{u} m/s বেগে {a}° কোণে নিক্ষিপ্ত প্রক্ষেপকের সর্বোচ্চ বিন্দুতে বেগ কত?", ok, W(ok, ['0 m/s', f"{u} m/s", {30: str(u // 2), 60: f"{u // 2}√3", 45: f"{u}√2"}[a] + ' m/s']), "u cos α।", M)
def h_RH(b):
    a = R.choice([45, 60, 30])
    ok = {45: '4 : 1', 60: '4 : √3', 30: '4√3 : 1'}[a]
    b.add(f"{a}° কোণে নিক্ষিপ্ত প্রক্ষেপকের অনুভূমিক পাল্লা ও সর্বোচ্চ উচ্চতার অনুপাত কত?", ok, W(ok, ['4 : 1', '4 : √3', '4√3 : 1', '1 : 4', '2 : 1']), "R/H = 4 cot α।", H)
def h_equalRH(b):
    b.add("কোন কোণে নিক্ষেপ করলে প্রক্ষেপকের অনুভূমিক পাল্লা ও সর্বোচ্চ উচ্চতা সমান হয়?", "tan⁻¹4", ["45°", "tan⁻¹(1/4)", "60°"], "4 cot α = 1।", H)
    k = R.randint(2, 12)
    b.add(f"অনুভূমিক পাল্লা সর্বোচ্চ উচ্চতার {k} গুণ হলে নিক্ষেপ কোণ কত?", f"tan⁻¹({fr(F(4, k))})", W(f"tan⁻¹({fr(F(4, k))})", [f"tan⁻¹({fr(F(k, 4))})", f"tan⁻¹({k})", f"tan⁻¹({fr(F(2, k))})"]), "4 cot α = k।", H)
def h_maxR_H(b):
    k = R.randint(1, 12); g = 10; u = 10 * k
    Rm = F(u * u, g); Hm = F(u * u, 2 * g)
    b.add(f"একই বেগে নিক্ষিপ্ত প্রক্ষেপকের সর্বাধিক অনুভূমিক পাল্লা {dec(Rm)} m হলে খাড়া উপরে নিক্ষেপ করলে সর্বোচ্চ কত উচ্চতায় উঠবে?", mm(Hm), W(mm(Hm), [mm(Rm), mm(Rm * 2), mm(Rm / 4), mm(Hm + 5)]), "u²/2g = R_max/2।", H)
def h_horizv(b):
    t = R.randint(1, 6); g = 10; u = R.choice([v * t for v in (3, 4, 5, 6, 8, 12, 15)])
    # ভূমিতে আঘাতের বেগ: √(u² + (gt)²)
    v2 = u * u + (g * t) ** 2
    ok = ms(math.isqrt(v2)) if math.isqrt(v2) ** 2 == v2 else f"{sq(v2)} m/s"
    h = g * t * t // 2
    b.add(f"{h} m উঁচু স্থান থেকে {u} m/s বেগে অনুভূমিকভাবে নিক্ষিপ্ত বস্তু কত বেগে ভূমিতে আঘাত করবে? (g = 10 m/s²)", ok, W(ok, [ms(u + g * t), ms(g * t), f"{sq(v2 + 100)} m/s", ms(u)]), "√(u² + (gt)²)।", H)
p9c = run('9.C', R, fx9c, [e_maxr, e_T, e_comp], [m_range, m_H, m_horiz, m_top], [h_RH, h_equalRH, h_maxR_H, h_horizv], caps=(50, 50, 40), mult=2)

fx9d = [
 ("একই দিকে চলমান দুটি বস্তুর আপেক্ষিক বেগ কত?", "বেগদ্বয়ের অন্তর", ["বেগদ্বয়ের যোগফল", "শূন্য", "গুণফল"], "", E),
 ("বিপরীত দিকে চলমান দুটি বস্তুর আপেক্ষিক বেগ কত?", "বেগদ্বয়ের যোগফল", ["বেগদ্বয়ের অন্তর", "শূন্য", "গুণফল"], "", E),
 ("বেগের সামান্তরিক সূত্রে লব্ধি বেগ কী দ্বারা নির্দেশিত হয়?", "সামান্তরিকের কর্ণ", ["বাহু", "উচ্চতা", "ক্ষেত্রফল"], "", E),
 ("নদী সবচেয়ে কম সময়ে পার হতে হলে নৌকা কোন দিকে চালাতে হবে?", "স্রোতের লম্ব দিকে", ["স্রোতের অনুকূলে", "স্রোতের প্রতিকূলে", "45° কোণে"], "", M),
 ("বেগ কী ধরনের রাশি?", "ভেক্টর", ["স্কেলার", "ধ্রুবক", "মাত্রাহীন"], "", E),
]
def e_rel(b):
    v1, v2 = R.sample(range(10, 120), 2); t = R.choice(['একই', 'বিপরীত'])
    v = abs(v1 - v2) if t == 'একই' else v1 + v2
    b.add(f"দুটি ট্রেন {v1} km/h ও {v2} km/h বেগে {t} দিকে চলছে। একটির সাপেক্ষে অপরটির বেগ কত?", f"{v} km/h", W(f"{v} km/h", [f"{v1 + v2 if t == 'একই' else abs(v1 - v2)} km/h", f"{max(v1, v2)} km/h", f"{v + 10} km/h"]), "", E)
def e_perp(b):
    p, q, r = R.choice(S90)
    b.add(f"একটি নৌকা স্থির পানিতে {q} km/h বেগে চলে। স্রোতের বেগ {p} km/h হলে স্রোতের লম্ব দিকে চালালে লব্ধি বেগ কত?", f"{r} km/h", W(f"{r} km/h", [f"{p + q} km/h", f"{abs(q - p)} km/h", f"{r + 1} km/h"]), "√(u² + v²)।", E)
def e_meet(b):
    v1, v2 = R.randint(10, 80), R.randint(10, 80); t = R.randint(1, 8)
    d = (v1 + v2) * t
    b.add(f"{d} km দূরের দুটি স্থান থেকে দুটি গাড়ি {v1} km/h ও {v2} km/h বেগে পরস্পরের দিকে যাত্রা শুরু করে। কত ঘণ্টা পর মিলিত হবে?", f"{t} ঘণ্টা", W(f"{t} ঘণ্টা", [f"{num(F(d, abs(v1 - v2)))} ঘণ্টা" if v1 != v2 else f"{t * 2} ঘণ্টা", f"{t + 1} ঘণ্টা", f"{t * 2} ঘণ্টা"]), "d/(v₁ + v₂)।", E)
def e_up(b):
    v, u = R.sample(range(3, 30), 2); v, u = max(v, u), min(v, u)
    t = R.choice(['অনুকূলে', 'প্রতিকূলে'])
    w = v + u if t == 'অনুকূলে' else v - u
    b.add(f"স্থির পানিতে নৌকার বেগ {v} km/h ও স্রোতের বেগ {u} km/h হলে স্রোতের {t} নৌকার বেগ কত?", f"{w} km/h", W(f"{w} km/h", [f"{v - u if t == 'অনুকূলে' else v + u} km/h", f"{sq(v * v + u * u)} km/h", f"{v} km/h"]), "", E)
def m_cross(b):
    v, u = R.randint(2, 15), R.randint(1, 10); d = v * R.randint(1, 10) * 10
    t = F(d, v); drift = u * t
    q = R.choice(['t', 'd'])
    if q == 't':
        b.add(f"{d} m চওড়া নদীতে স্রোতের বেগ {u} m/s। স্থির পানিতে {v} m/s বেগের নৌকা ন্যূনতম কত সময়ে নদী পার হবে?", se(t), W(se(t), [se(F(d, u)), se(F(d, v + u)), se(F(d, abs(v - u))) if v != u else se(t * 2), se(t + 10)]), "t = d/v।", M)
    else:
        b.add(f"{d} m চওড়া নদীতে স্রোতের বেগ {u} m/s। স্থির পানিতে {v} m/s বেগের নৌকা স্রোতের লম্ব দিকে চালালে অপর পাড়ে কত দূর ভাটিতে পৌঁছাবে?", mm(drift), W(mm(drift), [mm(d), mm(F(d * v, u)), mm(drift + u), mm(drift * 2)]), "x = u·d/v।", M)
def m_straight(b):
    p, q, r = R.choice(S90)   # u = p (স্রোত), নৌকা r, লব্ধি q
    d = q * R.randint(1, 10) * 10
    b.add(f"{d} m চওড়া নদীতে স্রোতের বেগ {p} m/s এবং স্থির পানিতে নৌকার বেগ {r} m/s। নৌকাটি সোজাসুজি অপর পাড়ে পৌঁছাতে কত সময় লাগবে?", se(F(d, q)), W(se(F(d, q)), [se(F(d, r)), se(F(d, p)), se(F(d, q) + 10), se(F(d, r + p))]), f"লব্ধি বেগ √({r}² − {p}²) = {q}।", M)
def m_train(b):
    L1, L2 = R.randint(5, 30) * 10, R.randint(5, 30) * 10; v1, v2 = R.randint(5, 30), R.randint(5, 30)
    t = R.choice(['বিপরীত', 'একই'])
    if t == 'একই' and v1 == v2: return
    rel = v1 + v2 if t == 'বিপরীত' else abs(v1 - v2)
    tt = F(L1 + L2, rel)
    b.add(f"{L1} m ও {L2} m দীর্ঘ দুটি ট্রেন {v1} m/s ও {v2} m/s বেগে {t} দিকে চলছে। একটি অপরটিকে অতিক্রম করতে কত সময় লাগবে?", se(tt), W(se(tt), [se(F(L1 + L2, v1 + v2 if t == 'একই' else abs(v1 - v2) or 1)), se(F(L1, rel)), se(tt + 1), se(F(L1 + L2, v1))]), "(L₁ + L₂)/আপেক্ষিক বেগ।", M)
def m_rain(b):
    p, q, r = R.choice(S90)
    ok = f"tan⁻¹({fr(F(p, q))})"
    b.add(f"বৃষ্টি {q} m/s বেগে খাড়াভাবে পড়ছে। একজন লোক {p} m/s বেগে হাঁটলে বৃষ্টি থেকে বাঁচতে ছাতা উল্লম্বের সাথে কত কোণে ধরতে হবে?", ok, W(ok, [f"tan⁻¹({fr(F(q, p))})", f"sin⁻¹({fr(F(p, q))})" if p < q else f"cos⁻¹({fr(F(q, r))})", f"tan⁻¹({fr(F(p, r))})"]), "tan θ = লোকের বেগ/বৃষ্টির বেগ।", M)
def h_upangle(b):
    p, q, r = R.choice(S90)
    ok = f"sin⁻¹({fr(F(p, r))})"
    b.add(f"স্রোতের বেগ {p} m/s ও স্থির পানিতে নৌকার বেগ {r} m/s। নৌকাটি সোজাসুজি অপর পাড়ে যেতে চাইলে পাড়ের লম্বের সাথে উজানের দিকে কত কোণে চালাতে হবে?", ok, W(ok, [f"cos⁻¹({fr(F(p, r))})", f"tan⁻¹({fr(F(p, r))})", f"sin⁻¹({fr(F(q, r))})"]), "sin θ = u/v।", H)
def h_round(b):
    v, u = R.randint(4, 20), R.randint(1, 3); d = (v * v - u * u) * R.randint(1, 3)
    t = F(d, v + u) + F(d, v - u)
    b.add(f"স্থির পানিতে {v} km/h বেগের নৌকা {u} km/h স্রোতের নদীতে {d} km উজানে গিয়ে ফিরে আসতে মোট কত ঘণ্টা লাগবে?", f"{num(t)} ঘণ্টা", W(f"{num(t)} ঘণ্টা", [f"{num(F(2 * d, v))} ঘণ্টা", f"{num(F(d, v + u) * 2)} ঘণ্টা", f"{num(t + 1)} ঘণ্টা"]), "", H)
def h_relang(b):
    # দুটি জাহাজ পরস্পর লম্ব দিকে, আপেক্ষিক বেগ
    p, q, r = R.choice(S90)
    b.add(f"দুটি জাহাজ একই বিন্দু থেকে যথাক্রমে {p} km/h বেগে পূর্বে ও {q} km/h বেগে উত্তরে যাত্রা করে। একটির সাপেক্ষে অপরটির বেগের মান কত?", f"{r} km/h", W(f"{r} km/h", [f"{p + q} km/h", f"{abs(q - p)} km/h", f"{r + 2} km/h"]), "√(v₁² + v₂²)।", H)
    t = R.randint(1, 6)
    b.add(f"দুটি জাহাজ একই বিন্দু থেকে যথাক্রমে {p} km/h বেগে পূর্বে ও {q} km/h বেগে উত্তরে যাত্রা করে। {t} ঘণ্টা পর তাদের দূরত্ব কত?", f"{r * t} km", W(f"{r * t} km", [f"{(p + q) * t} km", f"{abs(q - p) * t} km", f"{r} km"]), "", H)
p9d = run('9.D', R, fx9d, [e_rel, e_perp, e_meet, e_up], [m_cross, m_straight, m_train, m_rain], [h_upangle, h_round, h_relang], caps=(50, 50, 40), mult=2)
save('j9', p9a + p9b + p9c + p9d)

# ================= 10 বিস্তার পরিমাপ ও সম্ভাবনা =================
def bnl(xs): return ', '.join(num(x) for x in xs)
def data(n=None):
    n = n or R.randint(4, 7)
    while True:
        xs = [R.randint(1, 40) for _ in range(n)]
        if sum(xs) % n == 0 and len(set(xs)) > 2: return xs
def var(xs):
    m = F(sum(xs), len(xs)); return sum((x - m) ** 2 for x in xs) / len(xs)
fx10a = [
 ("পরিসর = কত?", "বৃহত্তম মান − ক্ষুদ্রতম মান", ["বৃহত্তম মান + ক্ষুদ্রতম মান", "গড় − মধ্যক", "বৃহত্তম মান/ক্ষুদ্রতম মান"], "", E),
 ("পরিমিত ব্যবধান ও ভেদাঙ্কের সম্পর্ক কোনটি?", "পরিমিত ব্যবধান = √ভেদাঙ্ক", ["ভেদাঙ্ক = √পরিমিত ব্যবধান", "সমান", "ভেদাঙ্ক = 2 × পরিমিত ব্যবধান"], "", E),
 ("প্রতিটি মানের সাথে একটি ধ্রুবক যোগ করলে পরিমিত ব্যবধানের কী পরিবর্তন হয়?", "অপরিবর্তিত থাকে", ["ধ্রুবকটি যোগ হয়", "দ্বিগুণ হয়", "শূন্য হয়"], "", M),
 ("সব মান সমান হলে পরিমিত ব্যবধান কত?", "0", ["1", "গড়ের সমান", "অসীম"], "", E),
 ("বিভেদাঙ্ক (CV) = কত?", "(পরিমিত ব্যবধান/গড়) × 100%", ["(গড়/পরিমিত ব্যবধান) × 100%", "ভেদাঙ্ক/গড়", "পরিসর/গড়"], "", M),
 ("বিস্তারের কোন পরিমাপ সবচেয়ে বেশি ব্যবহৃত হয়?", "পরিমিত ব্যবধান", ["পরিসর", "গড় ব্যবধান", "চতুর্থক ব্যবধান"], "", E),
 ("ভেদাঙ্ক কখনো কেমন হতে পারে না?", "ঋণাত্মক", ["শূন্য", "ধনাত্মক", "ভগ্নাংশ"], "", E),
]
def e_range(b):
    xs = [R.randint(1, 99) for _ in range(R.randint(5, 9))]
    v = max(xs) - min(xs)
    b.add(f"{bnl(xs)} উপাত্তের পরিসর কত?", v, W(v, [max(xs) + min(xs), max(xs), v + 1, xs[-1] - xs[0] if xs[-1] != xs[0] else v + 2]), "", E)
def e_mean(b):
    xs = data(); m = F(sum(xs), len(xs))
    b.add(f"{bnl(xs)} উপাত্তের গাণিতিক গড় কত?", num(m), W(num(m), [num(m + 1), num(F(sum(xs), len(xs) - 1)), num(sorted(xs)[len(xs) // 2]) if sorted(xs)[len(xs) // 2] != m else num(m + 2), num(m - 1)]), "", E)
def e_shift(b):
    s, c = R.randint(1, 20), R.randint(1, 50); op = R.choice(['যোগ', 'বিয়োগ', 'গুণ'])
    k = R.randint(2, 6)
    if op == 'গুণ':
        ok = str(k * s)
        b.add(f"কোনো উপাত্তের পরিমিত ব্যবধান {s}। প্রতিটি মানকে {k} দিয়ে গুণ করলে নতুন পরিমিত ব্যবধান কত?", ok, W(ok, [str(s), str(k * k * s), str(s + k)]), "", E)
    else:
        b.add(f"কোনো উপাত্তের পরিমিত ব্যবধান {s}। প্রতিটি মানের সাথে {c} {op} করলে নতুন পরিমিত ব্যবধান কত?", str(s), W(str(s), [str(s + c), str(abs(s - c)) if s != c else '0', str(s * c)]), "স্থানান্তরে অপরিবর্তিত।", E)
def e_var2sd(b):
    s = R.randint(1, 30); t = R.choice(['ভেদাঙ্ক', 'পরিমিত ব্যবধান'])
    if t == 'ভেদাঙ্ক':
        b.add(f"কোনো উপাত্তের ভেদাঙ্ক {s * s} হলে পরিমিত ব্যবধান কত?", s, W(s, [s * s, 2 * s, s + 1, s * s // 2 if s > 2 else 7]), "", E)
    else:
        b.add(f"কোনো উপাত্তের পরিমিত ব্যবধান {s} হলে ভেদাঙ্ক কত?", s * s, W(s * s, [s, 2 * s, s * s + 1, s * s * 2]), "", E)
def m_var(b):
    xs = data(R.randint(4, 6)); v = var(xs)
    b.add(f"{bnl(xs)} উপাত্তের ভেদাঙ্ক কত?", num(v), W(num(v), [num(v * len(xs) / (len(xs) - 1)), num(v + 1), num(v * 2), num(v / 2)]), "Σ(x − x̄)²/n।", M)
def m_sd(b):
    while True:
        xs = data(R.randint(4, 6)); v = var(xs)
        if v.denominator == 1 and math.isqrt(v.numerator) ** 2 == v.numerator: break
    s = math.isqrt(v.numerator)
    b.add(f"{bnl(xs)} উপাত্তের পরিমিত ব্যবধান কত?", s, W(s, [s * s, s + 1, s * 2, s + 2]), "", M)
def m_md(b):
    xs = data(R.randint(4, 7)); m = F(sum(xs), len(xs))
    v = sum(abs(x - m) for x in xs) / len(xs)
    b.add(f"{bnl(xs)} উপাত্তের গড় থেকে গড় ব্যবধান কত?", num(v), W(num(v), [num(v + 1), num(sum(abs(x - m) for x in xs)), num(var(xs)), num(v * 2)]), "Σ|x − x̄|/n।", M)
def m_cv(b):
    m = R.randint(2, 40) * 5; s = R.randint(1, m // 2)
    v = F(100 * s, m)
    b.add(f"কোনো উপাত্তের গড় {m} ও পরিমিত ব্যবধান {s} হলে বিভেদাঙ্ক কত?", f"{num(v)}%", W(f"{num(v)}%", [f"{num(F(100 * m, s))}%", f"{num(F(100 * s * s, m))}%", f"{num(v + 1)}%"]), "", M)
def m_scale(b):
    s, k, c = R.randint(1, 15), nz(-6, 6), R.randint(-20, 20)
    if abs(k) == 1: return
    v = abs(k) * s
    b.add(f"x-এর পরিমিত ব্যবধান {s} হলে y = {num(k)}x {'+' if c >= 0 else '−'} {abs(c)}-এর পরিমিত ব্যবধান কত?", v, W(v, [k * s if k < 0 else v + abs(c), k * k * s, v + abs(c) if c else v + 1, s]), "|k|σ।", M)
def h_sumsq(b):
    n = R.randint(5, 20); m = R.randint(2, 20); s = R.randint(1, 10)
    S2 = n * (s * s + m * m)
    b.add(f"{n} টি সংখ্যার গড় {m} এবং বর্গের যোগফল {S2} হলে পরিমিত ব্যবধান কত?", s, W(s, [s * s, m, s + 1, sq(F(S2, n))]), "σ² = Σx²/n − x̄²।", H)
def h_nat(b):
    n = R.choice([3, 5, 7, 9, 11, 13, 4, 6, 8, 10])
    v = F(n * n - 1, 12)
    b.add(f"প্রথম {n} টি স্বাভাবিক সংখ্যার ভেদাঙ্ক কত?", num(v), W(num(v), [num(F(n * n + 1, 12)), num(F(n + 1, 2)), num(F(n * n - 1, 6)), num(v + 1)]), "(n² − 1)/12।", H)
def h_combine(b):
    # দুটি গ্রুপের মিলিত গড়
    n1, n2 = R.randint(5, 40), R.randint(5, 40); m1, m2 = R.randint(10, 80), R.randint(10, 80)
    m = F(n1 * m1 + n2 * m2, n1 + n2)
    b.add(f"{n1} জন শিক্ষার্থীর গড় নম্বর {m1} এবং {n2} জনের গড় নম্বর {m2} হলে সকলের মিলিত গড় কত?", num(m), W(num(m), [num(F(m1 + m2, 2)), num(m + 1), num(F(n1 * m2 + n2 * m1, n1 + n2)) if m1 != m2 else num(m + 2)]), "", H)
p10a = run('10.A', R, fx10a, [e_range, e_mean, e_shift, e_var2sd], [m_var, m_sd, m_md, m_cv, m_scale], [h_sumsq, h_nat, h_combine], caps=(40, 50, 40), mult=2)

fx10b = [
 ("নিশ্চিত ঘটনার সম্ভাবনা কত?", "1", ["0", "1/2", "অসীম"], "", E), ("অসম্ভব ঘটনার সম্ভাবনা কত?", "0", ["1", "1/2", "−1"], "", E),
 ("P(A) + P(A′) = কত?", "1", ["0", "P(A)", "2"], "", E),
 ("P(A ∪ B) = কত?", "P(A) + P(B) − P(A ∩ B)", ["P(A) + P(B)", "P(A)P(B)", "P(A) − P(B)"], "", E),
 ("A ও B স্বাধীন ঘটনা হলে P(A ∩ B) = কত?", "P(A)·P(B)", ["P(A) + P(B)", "0", "P(A)/P(B)"], "", E),
 ("A ও B পরস্পর বিচ্ছিন্ন ঘটনা হলে P(A ∩ B) = কত?", "0", ["1", "P(A)P(B)", "P(A) + P(B)"], "", E),
 ("একটি ঘটনার সম্ভাবনার সীমা কোনটি?", "0 ≤ P(A) ≤ 1", ["−1 ≤ P(A) ≤ 1", "P(A) > 1", "0 < P(A) < 1 মাত্র"], "", E),
 ("একটি ছক্কা নিক্ষেপে নমুনাক্ষেত্রের উপাদান কয়টি?", "6", ["12", "36", "1"], "", E),
]
def pr(v): return fr(F(v))
def e_die(b):
    ev = R.choice([('জোড় সংখ্যা', {2, 4, 6}), ('বিজোড় সংখ্যা', {1, 3, 5}), ('মৌলিক সংখ্যা', {2, 3, 5}), ('3-এর গুণিতক', {3, 6}), ('4-এর চেয়ে বড় সংখ্যা', {5, 6}), ('2-এর চেয়ে ছোট সংখ্যা', {1}), ('6-এর উৎপাদক', {1, 2, 3, 6}), ('5', {5}), ('3-এর চেয়ে বড় নয় এমন সংখ্যা', {1, 2, 3}), ('7', set())])
    v = F(len(ev[1]), 6)
    b.add(f"একটি নিরপেক্ষ ছক্কা নিক্ষেপে {ev[0]} আসার সম্ভাবনা কত?", pr(v), W(pr(v), [pr(1 - v), pr(F(len(ev[1]) + 1, 6)), pr(F(1, 6)) if v != F(1, 6) else '1/3', '1/2', '0']), "", E)
def e_coin(b):
    n = R.randint(2, 6); k = R.randint(0, n)
    v = F(math.comb(n, k), 2 ** n)
    b.add(f"{n} টি মুদ্রা একসাথে নিক্ষেপ করলে ঠিক {k} টি হেড আসার সম্ভাবনা কত?", pr(v), W(pr(v), [pr(F(1, 2 ** n)) if v != F(1, 2 ** n) else pr(F(2, 2 ** n)), pr(F(k, n)) if F(k, n) != v else pr(v * 2) if v < F(1, 2) else '1/3', pr(F(math.comb(n, k), 2 ** n + 1)), pr(1 - v) if 1 - v != v else '1/4']), f"{n}C{k}/2{sup(n)}।", E)
def e_bag(b):
    r, g, w = R.randint(1, 12), R.randint(1, 12), R.randint(0, 10)
    t = r + g + w; c = R.choice([('লাল', r), ('সবুজ', g)])
    v = F(c[1], t)
    b.add(f"একটি থলিতে {r} টি লাল, {g} টি সবুজ{f' ও {w} টি সাদা' if w else ''} বল আছে। দৈবভাবে একটি বল তুললে সেটি {c[0]} হওয়ার সম্ভাবনা কত?", pr(v), W(pr(v), [pr(1 - v), pr(F(c[1], t - c[1])) if t != 2 * c[1] else '1/3', pr(F(c[1] + 1, t)), pr(F(1, t))]), "", E)
def e_card(b):
    ev = R.choice([('টেক্কা', 4), ('হরতন', 13), ('লাল তাস', 26), ('ছবিযুক্ত তাস (J, Q, K)', 12), ('কালো রাজা', 2), ('হরতনের টেক্কা', 1), ('রাজা বা রানি', 8), ('চিড়িতন বা ইস্কাপন', 26), ('ছবিযুক্ত নয় এমন তাস', 40)])
    v = F(ev[1], 52)
    b.add(f"52 টি তাসের প্যাকেট থেকে দৈবভাবে একটি তাস টানলে সেটি {ev[0]} হওয়ার সম্ভাবনা কত?", pr(v), W(pr(v), [pr(1 - v), pr(F(ev[1], 13)) if F(ev[1], 13) <= 1 and F(ev[1], 13) != v else '1/4', pr(F(ev[1] + 1, 52)), pr(F(1, 52)) if v != F(1, 52) else '1/26']), "", E)
def e_comp(b):
    v = F(R.randint(1, 19), 20)
    b.add(f"P(A) = {pr(v)} হলে P(A′) = কত?", pr(1 - v), W(pr(1 - v), [pr(v), pr(1 + v) if v < 1 else '1', '0', pr(abs(F(1, 2) - v)) if abs(F(1, 2) - v) not in (v, 1 - v) else '1']), "", E)
def m_dice2(b):
    s = R.randint(2, 12)
    n = sum(1 for i in range(1, 7) for j in range(1, 7) if i + j == s)
    v = F(n, 36)
    b.add(f"দুটি নিরপেক্ষ ছক্কা একসাথে নিক্ষেপ করলে সংখ্যা দুটির যোগফল {s} হওয়ার সম্ভাবনা কত?", pr(v), W(pr(v), [pr(F(n + 1, 36)), pr(F(n, 12)) if n < 12 else '1/2', pr(F(1, 11)) if v != F(1, 11) else '1/6', pr(F(max(n - 1, 0) or 2, 36))]), "36টি ফলাফল।", M)
def m_dice_ev(b):
    ev = R.choice([('উভয়টিতে একই সংখ্যা', lambda i, j: i == j), ('যোগফল জোড়', lambda i, j: (i + j) % 2 == 0), ('যোগফল মৌলিক', lambda i, j: i + j in (2, 3, 5, 7, 11)), ('গুণফল জোড়', lambda i, j: i * j % 2 == 0), ('যোগফল 10-এর বেশি', lambda i, j: i + j > 10), ('অন্তত একটিতে 6', lambda i, j: 6 in (i, j)), ('যোগফল 3-এর গুণিতক', lambda i, j: (i + j) % 3 == 0), ('গুণফল 12', lambda i, j: i * j == 12), ('যোগফল 5-এর কম', lambda i, j: i + j < 5), ('উভয়টিতে বিজোড়', lambda i, j: i % 2 and j % 2)])
    n = sum(1 for i in range(1, 7) for j in range(1, 7) if ev[1](i, j)); v = F(n, 36)
    b.add(f"দুটি ছক্কা নিক্ষেপে {ev[0]} হওয়ার সম্ভাবনা কত?", pr(v), W(pr(v), [pr(1 - v), pr(F(n + 1, 36)), pr(F(n - 1, 36)) if n > 1 else '1/12', pr(F(n, 30)) if n <= 30 else '1/2']), "", M)
def m_two(b):
    r, g = R.randint(2, 12), R.randint(2, 12); t = r + g
    k = R.choice(['উভয়টি লাল', 'উভয়টি সবুজ', 'একটি লাল ও একটি সবুজ'])
    n = {'উভয়টি লাল': math.comb(r, 2), 'উভয়টি সবুজ': math.comb(g, 2), 'একটি লাল ও একটি সবুজ': r * g}[k]
    v = F(n, math.comb(t, 2))
    b.add(f"একটি থলিতে {r} টি লাল ও {g} টি সবুজ বল আছে। দৈবভাবে দুটি বল তুললে {k} হওয়ার সম্ভাবনা কত?", pr(v), W(pr(v), [pr(F(r * r, t * t)) if k == 'উভয়টি লাল' else pr(F(g * g, t * t)) if k == 'উভয়টি সবুজ' else pr(F(2 * r * g, t * t)), pr(1 - v), pr(F(n, t * t)), pr(F(n + 1, math.comb(t, 2)))]), "সমাবেশ ব্যবহার করে।", M)
def m_union(b):
    a, c = F(R.randint(2, 9), 20), F(R.randint(2, 9), 20); i = F(R.randint(1, int(min(a, c) * 20)), 20)
    v = a + c - i
    b.add(f"P(A) = {pr(a)}, P(B) = {pr(c)} ও P(A ∩ B) = {pr(i)} হলে P(A ∪ B) = কত?", pr(v), W(pr(v), [pr(a + c), pr(a * c), pr(v - i) if v - i > 0 else '1/20', pr(1 - v)]), "", M)
def m_indep(b):
    a, c = F(R.randint(1, 9), 10), F(R.randint(1, 9), 10)
    t = R.choice(['∩', '∪'])
    v = a * c if t == '∩' else a + c - a * c
    b.add(f"A ও B স্বাধীন ঘটনা, P(A) = {pr(a)} ও P(B) = {pr(c)} হলে P(A {t} B) = কত?", pr(v), W(pr(v), [pr(a + c) if a + c <= 1 else pr(1 - a * c), pr(a * c) if t == '∪' else pr(a + c - a * c), pr(1 - v), pr(abs(a - c)) if a != c else '1/10']), "", M)
def m_numdiv(b):
    N = R.randint(20, 100); k = R.choice([2, 3, 4, 5, 6, 7])
    v = F(N // k, N)
    b.add(f"1 থেকে {N} পর্যন্ত সংখ্যা থেকে দৈবভাবে একটি নিলে সেটি {k}-এর গুণিতক হওয়ার সম্ভাবনা কত?", pr(v), W(pr(v), [pr(F(1, k)) if F(1, k) != v else pr(F(N // k + 1, N)), pr(F(N // k - 1, N)), pr(1 - v), pr(F(k, N))]), "", M)
def h_or(b):
    N = R.randint(20, 100); p, q = R.sample([2, 3, 5, 7], 2)
    n = N // p + N // q - N // (p * q); v = F(n, N)
    b.add(f"1 থেকে {N} পর্যন্ত সংখ্যা থেকে দৈবভাবে একটি নিলে সেটি {p} অথবা {q}-এর গুণিতক হওয়ার সম্ভাবনা কত?", pr(v), W(pr(v), [pr(F(N // p + N // q, N)), pr(F(N // (p * q), N)), pr(1 - v), pr(F(n + 1, N))]), "অন্তর্ভুক্তি-বর্জন।", H)
def h_atleast(b):
    n = R.randint(2, 8)
    v = 1 - F(1, 2 ** n)
    b.add(f"{n} টি মুদ্রা নিক্ষেপে অন্তত একটি হেড আসার সম্ভাবনা কত?", pr(v), W(pr(v), [pr(F(1, 2 ** n)), pr(F(n, 2 ** n)), '1/2', pr(1 - F(1, 2 ** (n + 1)))]), "1 − P(কোনো হেড নয়)।", H)
    p = F(R.randint(1, 5), 6); m = R.randint(2, 4)
    v2 = 1 - (1 - p) ** m
    b.add(f"একটি লক্ষ্যভেদের সম্ভাবনা {pr(p)}। {m} বার চেষ্টায় অন্তত একবার লক্ষ্যভেদের সম্ভাবনা কত?", pr(v2), W(pr(v2), [pr(p ** m), pr(min(m * p, F(1))), pr((1 - p) ** m), pr(1 - p ** m)]), "1 − (1 − p)ⁿ।", H)
def h_cond(b):
    a = F(R.randint(2, 9), 10); i = F(R.randint(1, int(a * 10) - 1), 10)
    v = i / a
    b.add(f"P(A) = {pr(a)} ও P(A ∩ B) = {pr(i)} হলে P(B|A) = কত?", pr(v), W(pr(v), [pr(i * a), pr(a - i), pr(1 - v) if 1 - v != v else '1/3', pr(i)]), "P(A ∩ B)/P(A)।", H)
def h_three(b):
    r, g, w = R.randint(2, 8), R.randint(2, 8), R.randint(2, 8); t = r + g + w
    v = F(r * g * w, math.comb(t, 3))
    b.add(f"একটি থলিতে {r} টি লাল, {g} টি সবুজ ও {w} টি সাদা বল আছে। দৈবভাবে তিনটি বল তুললে তিনটি ভিন্ন রঙের হওয়ার সম্ভাবনা কত?", pr(v), W(pr(v), [pr(F(r * g * w, t ** 3)), pr(1 - v), pr(F(r + g + w, math.comb(t, 3))), pr(F(6 * r * g * w, t ** 3)) if F(6 * r * g * w, t ** 3) != v else '1/3']), "", H)
p10b = run('10.B', R, fx10b, [e_die, e_coin, e_bag, e_card, e_comp], [m_dice2, m_dice_ev, m_two, m_union, m_indep, m_numdiv], [h_or, h_atleast, h_cond, h_three], caps=(40, 40, 40), mult=2)
save('j10', p10a + p10b)
