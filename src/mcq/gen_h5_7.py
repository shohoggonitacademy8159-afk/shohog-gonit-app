#!/usr/bin/env python3
"""উচ্চতর গণিত (দশম, c10h) অধ্যায় 5–7:
5.1 দ্বিঘাত সমীকরণ ও মূলের প্রকৃতি · 5.2 মূল-সহগ সম্পর্ক · 5.3 করণী সমীকরণ · 5.4 সূচক সমীকরণ
5.5 দুই চলকের দ্বিঘাত সহসমীকরণ · 5.6 সূচক ও লগারিদমীয় সহসমীকরণ · 5.7 সমীকরণের বাস্তব প্রয়োগ
6.1 এক চলকের রৈখিক অসমতা · 6.2 দ্বিঘাত ও পরমমান অসমতা · 6.3 দুই চলকের অসমতা · 7 অসীম ধারা"""
import random, pathlib, sys, math
from fractions import Fraction as F
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from mcqlib import run, save, E, M, H, fr, near, num, pfmt, lin, surd, sup

R = random.Random(2026110102)
X = ('x',)
def setw(c, pool):
    out = []
    for w in pool:
        w = str(w)
        if w != str(c) and w not in out: out.append(w)
    return out
def quad(a, b, c):
    return pfmt({k: v for k, v in {(2,): a, (1,): b, (0,): c}.items() if v}, X)
def Sx(*v):
    v = sorted(set(v)); return '{' + ', '.join(num(x) for x in v) + '}'
def roots_q(r1, r2, a=1):
    return a, -a * (r1 + r2), a * r1 * r2

# ---------------- 5.1 ----------------
fx51 = [
 ("ax² + bx + c = 0 (a ≠ 0) সমীকরণের নিশ্চায়ক কোনটি?", "b² − 4ac", ["b² + 4ac", "4ac − b²", "√(b² − 4ac)"], "D = b² − 4ac।", E),
 ("নিশ্চায়ক শূন্য হলে দ্বিঘাত সমীকরণের মূলদ্বয় কেমন?", "বাস্তব ও সমান", ["বাস্তব ও অসমান", "অবাস্তব", "মূলদ ও অসমান"], "D = 0 হলে মূল দুটি সমান।", E),
 ("নিশ্চায়ক ঋণাত্মক হলে মূলদ্বয় কেমন?", "অবাস্তব (জটিল)", ["বাস্তব ও সমান", "বাস্তব ও অসমান", "মূলদ"], "D < 0।", E),
 ("নিশ্চায়ক ধনাত্মক ও পূর্ণবর্গ হলে (a, b, c মূলদ) মূলদ্বয় কেমন?", "বাস্তব, অসমান ও মূলদ", ["বাস্তব, অসমান ও অমূলদ", "সমান", "অবাস্তব"], "√D মূলদ।", M),
 ("নিশ্চায়ক ধনাত্মক কিন্তু পূর্ণবর্গ নয় (a, b, c মূলদ) হলে মূলদ্বয় কেমন?", "বাস্তব, অসমান ও অমূলদ", ["বাস্তব, অসমান ও মূলদ", "সমান", "অবাস্তব"], "√D অমূলদ।", M),
 ("ax² + bx + c = 0 সমীকরণের মূল নির্ণয়ের সূত্র কোনটি?", "x = (−b ± √(b² − 4ac))/(2a)", ["x = (b ± √(b² − 4ac))/(2a)", "x = (−b ± √(b² + 4ac))/(2a)", "x = (−b ± √(b² − 4ac))/a"], "দ্বিঘাত সূত্র।", E),
 ("একটি দ্বিঘাত সমীকরণের সর্বোচ্চ কয়টি মূল থাকতে পারে?", "2টি", ["1টি", "3টি", "অসংখ্য"], "দ্বিঘাত তাই দুটি মূল।", E),
]
def e_solve(b):
    r1, r2 = R.sample(range(-9, 10), 2)
    a, bb, c = roots_q(r1, r2)
    ok = Sx(r1, r2)
    b.add(f"{quad(a, bb, c)} = 0 সমীকরণের সমাধান সেট কোনটি?", ok, setw(ok, [Sx(-r1, -r2), Sx(r1, -r2) if r2 else Sx(r1, 1), Sx(-r1, r2) if r1 else Sx(2, r2), Sx(r1 + 1, r2 + 1)]), f"(x {'−' if r1 >= 0 else '+'} {abs(r1)})(x {'−' if r2 >= 0 else '+'} {abs(r2)}) = 0।".replace('(x − 0)', 'x'), E)
def e_disc(b):
    a, bb, c = R.randint(1, 5), R.randint(-9, 9), R.randint(-9, 9)
    if not bb or not c: return
    D = bb * bb - 4 * a * c
    b.add(f"{quad(a, bb, c)} = 0 সমীকরণের নিশ্চায়ক কত?", num(D), setw(num(D), [num(bb * bb + 4 * a * c), num(D + 1), num(-D) if D else '1', num(bb * bb - 2 * a * c)]), f"D = ({num(bb)})² − 4·{a}·({num(c)}) = {num(D)}।", E)
def e_nature(b):
    a, bb, c = R.randint(1, 5), R.randint(-9, 9), R.randint(-9, 9)
    if not bb or not c: return
    D = bb * bb - 4 * a * c
    ok = 'বাস্তব ও সমান' if D == 0 else ('অবাস্তব' if D < 0 else ('বাস্তব, অসমান ও মূলদ' if math.isqrt(D) ** 2 == D else 'বাস্তব, অসমান ও অমূলদ'))
    b.add(f"{quad(a, bb, c)} = 0 সমীকরণের মূলদ্বয়ের প্রকৃতি কেমন?", ok, setw(ok, ['বাস্তব ও সমান', 'অবাস্তব', 'বাস্তব, অসমান ও মূলদ', 'বাস্তব, অসমান ও অমূলদ']), f"D = {num(D)}।", E)
def e_sqroot(b):
    k = R.randint(2, 15)
    ok = f"±{k}"
    b.add(f"x² = {k * k} হলে x = কত?", ok, [str(k), f"±{k * k}", f"{2 * k}"], f"x = ±√{k * k} = ±{k}।", E)
def rootfmt(a, bb, D, sgn=1):
    k, m = 1, D
    for f in range(int(D ** .5) + 1, 1, -1):
        if m % (f * f) == 0: k *= f; m //= f * f
    g = math.gcd(math.gcd(abs(bb), k), 2 * a)
    nb, nk, den = -bb * sgn // g, k // g, 2 * a // g
    rad = f"{nk if nk > 1 else ''}√{m}"
    top = f"{num(nb)} ± {rad}" if nb else f"±{rad}"
    return f"({top})/{den}" if den > 1 else (top if not nb else f"{top}")
def m_formula(b):
    a, bb, c = R.randint(1, 3), R.randint(-8, 8), R.randint(-8, 8)
    D = bb * bb - 4 * a * c
    if D <= 0 or math.isqrt(D) ** 2 == D or not bb: return
    ok = rootfmt(a, bb, D)
    D2 = bb * bb + 4 * a * c
    ws = [rootfmt(a, bb, D, -1), rootfmt(a, bb, D2) if D2 > 0 and math.isqrt(D2) ** 2 != D2 else rootfmt(a, bb, D + 4), rootfmt(a, bb, D + 8) if math.isqrt(D + 8) ** 2 != D + 8 else rootfmt(a, bb, D + 12)]
    b.add(f"{quad(a, bb, c)} = 0 সমীকরণের মূলদ্বয় কোনটি?", ok, setw(ok, ws), f"x = (−b ± √D)/(2a), D = {D} ⇒ x = {ok}।", M)
def m_equal(b):
    a, k = R.randint(1, 5), R.randint(1, 8)
    # ax² + kx·? ; সমান মূলের জন্য p² = 4ac ⇒ c = p²/(4a)
    p = 2 * a * k; c = a * k * k
    b.add(f"{a if a > 1 else ''}x² − px + {c} = 0 সমীকরণের মূলদ্বয় সমান হলে p-এর ধনাত্মক মান কত?", p, setw(p, [p // 2, 2 * p, c, p + 2]), f"p² − 4·{a}·{c} = 0 ⇒ p = {p}।", M)
def m_equal_k(b):
    a, c = R.choice([(1, 4), (1, 9), (4, 1), (9, 1), (1, 16), (4, 9), (9, 4), (1, 25), (16, 1), (4, 25), (25, 4), (1, 36)])
    k2 = 4 * a * c; k = math.isqrt(k2)
    ok = f"±{k}"
    b.add(f"{a if a > 1 else ''}x² + kx + {c} = 0 সমীকরণের মূলদ্বয় সমান হলে k = কত?", ok, setw(ok, [str(k), f"±{k2}", f"±{k // 2}" if k % 2 == 0 else f"±{k + 1}", f"±{2 * k}"]), f"k² = 4·{a}·{c} = {k2} ⇒ k = ±{k}।", M)
def m_complete(b):
    h = R.choice([v for v in range(-7, 8) if v]); c = R.randint(-10, 10)
    # x² + 2hx + c = (x + h)² − (h² − c)
    v = h * h - c
    ok = f"(x {'+' if h > 0 else '−'} {abs(h)})² = {num(v)}"
    b.add(f"x² {'+' if h > 0 else '−'} {abs(2 * h)}x {'+' if c >= 0 else '−'} {abs(c)} = 0 সমীকরণটিকে পূর্ণবর্গ আকারে লিখলে কোনটি হয়?".replace(' + 0 = 0', ' = 0').replace(' − 0 = 0', ' = 0'), ok, setw(ok, [f"(x {'−' if h > 0 else '+'} {abs(h)})² = {num(v)}", f"(x {'+' if h > 0 else '−'} {abs(h)})² = {num(h * h + c)}", f"(x {'+' if h > 0 else '−'} {abs(2 * h)})² = {num(4 * h * h - c)}", f"(x {'+' if h > 0 else '−'} {abs(h)})² = {num(-v) if v else '1'}"]), f"x² + {2 * h}x + {h * h} = {num(v)}।".replace('+ -', '− '), M)
def m_fracroots(b):
    p, q = R.choice([(1, 2), (1, 3), (2, 3), (3, 2), (1, 4), (3, 4), (2, 5)]); s = R.choice([1, -1]); r2 = R.randint(-5, 5)
    # (qx − s p)(x − r2) = 0
    a = q; bb = -(s * p + q * r2); c = s * p * r2
    if not bb or not c: return
    ok = Sx(F(s * p, q), r2)
    b.add(f"{quad(a, bb, c)} = 0 সমীকরণের সমাধান সেট কোনটি?", ok, setw(ok, [Sx(F(-s * p, q), -r2), Sx(F(s * q, p), r2), Sx(F(s * p, q), -r2), Sx(s * p, r2)]), f"উৎপাদকে ({q}x {'−' if s > 0 else '+'} {p})(x {'−' if r2 >= 0 else '+'} {abs(r2)}) = 0।", M)
def m_real_k(b):
    a, c = R.randint(1, 4), R.randint(1, 9)
    v = 4 * a * c; r = math.isqrt(v)
    if r * r != v: return
    ok = f"k ≥ {r} অথবা k ≤ −{r}"
    b.add(f"{a if a > 1 else ''}x² + kx + {c} = 0 সমীকরণের মূলদ্বয় বাস্তব হওয়ার শর্ত কোনটি?", ok, [f"−{r} < k < {r}", f"k > {r}", f"k ≤ {r}"], f"k² − {v} ≥ 0 ⇒ |k| ≥ {r}।", M)
def h_both(b):
    r = R.choice([v for v in range(-6, 7) if v]); s = R.randint(-6, 6)
    # x² + px + q = 0-এর একটি মূল r, অন্য মূল s; p = −(r + s)
    p = -(r + s); q = r * s
    b.add(f"x² + px {'+' if q >= 0 else '−'} {abs(q)} = 0 সমীকরণের একটি মূল {num(r)} হলে p = কত?".replace(' + 0 = 0', ' = 0').replace(' − 0 = 0', ' = 0'), num(p), setw(num(p), [num(-p) if p else '1', num(p + 1), num(r + s + 2), num(q)]), f"{r * r} + {num(r)}p {'+' if q >= 0 else '−'} {abs(q)} = 0 ⇒ p = {num(p)}।", H)
def h_common_root(b):
    r = R.choice([v for v in range(-5, 6) if v]); s1, s2 = R.sample([v for v in range(-6, 7) if v != r], 2)
    q1 = r * s1; p2 = -(r + s2)
    # x² − (r+s1)x + q1 = 0 এবং x² + p2 x + r s2 = 0
    b.add(f"{quad(1, -(r + s1), q1)} = 0 এবং {quad(1, p2, r * s2)} = 0 সমীকরণদ্বয়ের সাধারণ মূল কোনটি?", num(r), setw(num(r), [num(s1), num(s2), num(-r)]), f"উভয় সমীকরণে x = {num(r)} বসালে শূন্য হয়।", H)
def h_disc_param(b):
    m = R.randint(1, 6)
    # x² − 2(m+?)… : (m−1)x² − 2m x + (m+1)... keep: x² − 2kx + (k² − m²) = 0 মূল k ± m
    k = R.randint(-5, 6)
    ok = Sx(k - m, k + m)
    b.add(f"x² {'−' if k > 0 else '+'} {abs(2 * k)}x {'+' if k * k - m * m >= 0 else '−'} {abs(k * k - m * m)} = 0 সমীকরণের মূলদ্বয় কোনটি?".replace(' + 0x', '').replace(' − 0x', '').replace(' + 0 = 0', ' = 0').replace(' − 0 = 0', ' = 0'), ok, setw(ok, [Sx(-k - m, -k + m), Sx(k, m), Sx(k - 2 * m, k + 2 * m), Sx(k - m + 1, k + m - 1)]), f"(x − {num(k)})² = {m * m} ⇒ x = {num(k)} ± {m}।", H)
def h_frac_eq(b):
    a = R.randint(2, 9)
    # x + a²/x = 2a?  → x + k/x = s with roots r1,r2: x² − s x + k = 0 , r1 r2 = k
    r1, r2 = R.sample(range(1, 10), 2); s, k = r1 + r2, r1 * r2
    ok = Sx(r1, r2)
    b.add(f"x + {k}/x = {s} সমীকরণের সমাধান সেট কোনটি?", ok, setw(ok, [Sx(-r1, -r2), Sx(r1, k), Sx(s, 1), Sx(r1 + 1, r2)]), f"x² − {s}x + {k} = 0 ⇒ (x − {r1})(x − {r2}) = 0।", H)
p51 = run('5.1', R, fx51, [e_solve, e_disc, e_nature, e_sqroot], [m_formula, m_equal, m_equal_k, m_complete, m_fracroots, m_real_k], [h_both, h_common_root, h_disc_param, h_frac_eq])

# ---------------- 5.2 মূল-সহগ সম্পর্ক ----------------
fx52 = [
 ("ax² + bx + c = 0-এর মূলদ্বয় α ও β হলে α + β = কত?", "−b/a", ["b/a", "c/a", "−c/a"], "মূলদ্বয়ের যোগফল −b/a।", E),
 ("ax² + bx + c = 0-এর মূলদ্বয় α ও β হলে αβ = কত?", "c/a", ["−c/a", "b/a", "−b/a"], "মূলদ্বয়ের গুণফল c/a।", E),
 ("যে সমীকরণের মূলদ্বয় α ও β, সেটি কোনটি?", "x² − (α + β)x + αβ = 0", ["x² + (α + β)x + αβ = 0", "x² − αβx + (α + β) = 0", "x² + (α + β)x − αβ = 0"], "x² − (যোগফল)x + গুণফল = 0।", E),
 ("α² + β² = কত?", "(α + β)² − 2αβ", ["(α + β)² + 2αβ", "(α − β)² − 2αβ", "(α + β)² − αβ"], "অভেদ।", E),
 ("(α − β)² = কত?", "(α + β)² − 4αβ", ["(α + β)² + 4αβ", "(α + β)² − 2αβ", "α² − β²"], "অভেদ।", M),
 ("দ্বিঘাত সমীকরণের মূলদ্বয় পরস্পর অন্যোন্যক হলে কোনটি সত্য?", "c = a", ["b = 0", "c = 0", "a + b + c = 0"], "αβ = 1 ⇒ c/a = 1।", M),
 ("দ্বিঘাত সমীকরণের মূলদ্বয় সমান কিন্তু বিপরীত চিহ্নের হলে কোনটি সত্য?", "b = 0", ["c = 0", "a = c", "b = c"], "α + β = 0 ⇒ −b/a = 0।", M),
]
def rq():
    a = R.choice([1, 1, 1, 2, 3]); bb = R.choice([v for v in range(-9, 10) if v]); c = R.choice([v for v in range(-9, 10) if v])
    return a, bb, c
def e_sum(b):
    a, bb, c = rq(); v = F(-bb, a)
    b.add(f"{quad(a, bb, c)} = 0-এর মূলদ্বয় α ও β হলে α + β = কত?", num(v), setw(num(v), [num(-v), num(F(c, a)), num(F(-c, a)), num(v + 1)]), f"α + β = −b/a = {num(v)}।", E)
def e_prod(b):
    a, bb, c = rq(); v = F(c, a)
    b.add(f"{quad(a, bb, c)} = 0-এর মূলদ্বয় α ও β হলে αβ = কত?", num(v), setw(num(v), [num(-v), num(F(-bb, a)), num(F(bb, a)), num(v + 1)]), f"αβ = c/a = {num(v)}।", E)
def e_form(b):
    r1, r2 = R.sample([v for v in range(-7, 8) if v], 2)
    a, bb, c = roots_q(r1, r2); ok = f"{quad(a, bb, c)} = 0"
    b.add(f"যে সমীকরণের মূলদ্বয় {num(r1)} ও {num(r2)}, সেটি কোনটি?", ok, setw(ok, [f"{quad(1, -bb, c)} = 0" if bb else f"{quad(1, 1, c)} = 0", f"{quad(1, bb, -c)} = 0", f"{quad(1, -bb, -c)} = 0" if bb else f"{quad(1, 2, -c)} = 0"]), f"x² − ({num(r1 + r2)})x + ({num(r1 * r2)}) = 0।", E)
def m_sq(b):
    a, bb, c = rq(); s, p = F(-bb, a), F(c, a); v = s * s - 2 * p
    b.add(f"{quad(a, bb, c)} = 0-এর মূলদ্বয় α ও β হলে α² + β² = কত?", num(v), setw(num(v), [num(s * s + 2 * p), num(s * s - p), num(s * s), num(v + 1)]), f"(α + β)² − 2αβ = ({num(s)})² − 2({num(p)}) = {num(v)}।", M)
def m_recip(b):
    a, bb, c = rq(); s, p = F(-bb, a), F(c, a); v = s / p
    b.add(f"{quad(a, bb, c)} = 0-এর মূলদ্বয় α ও β হলে 1/α + 1/β = কত?", num(v), setw(num(v), [num(p / s), num(-v), num(s * p), num(v + 1)]), f"(α + β)/αβ = {num(s)}/{num(p)} = {num(v)}।", M)
def m_diff2(b):
    a, bb, c = rq(); s, p = F(-bb, a), F(c, a); v = s * s - 4 * p
    b.add(f"{quad(a, bb, c)} = 0-এর মূলদ্বয় α ও β হলে (α − β)² = কত?", num(v), setw(num(v), [num(s * s + 4 * p), num(s * s - 2 * p), num(-v) if v else '1', num(v + 4)]), f"(α + β)² − 4αβ = {num(v)}।", M)
def m_kroot(b):
    r1 = R.choice([v for v in range(-6, 7) if v]); s = R.randint(-8, 8)
    r2 = s - r1; k = r1 * r2
    b.add(f"x² {'−' if s > 0 else '+'} {abs(s) if abs(s) != 1 else ''}x + k = 0 সমীকরণের একটি মূল {num(r1)} হলে অপর মূল কত?".replace(' + 0x', '').replace(' − 0x', ''), num(r2), setw(num(r2), [num(-r2) if r2 else '1', num(k), num(s + r1), num(r2 + 1)]), f"α + β = {num(s)} ⇒ β = {num(s)} − ({num(r1)}) = {num(r2)}।", M)
def m_ratio(b):
    k = R.randint(2, 5); r = R.randint(1, 5)
    # মূলদ্বয় r ও kr ⇒ x² − (k+1) r x + k r² = 0
    a, bb, c = roots_q(r, k * r)
    b.add(f"{quad(a, bb, c)} = 0 সমীকরণের একটি মূল অপরটির কত গুণ?", f"{k} গুণ", setw(f"{k} গুণ", [f"{k + 1} গুণ", f"{c} গুণ", f"{k * k} গুণ", f"{k - 1} গুণ" if k > 2 else "3/2 গুণ"]), f"মূল {r} ও {k * r}।", M)
def m_cube(b):
    a, bb, c = rq(); s, p = F(-bb, a), F(c, a); v = s ** 3 - 3 * s * p
    b.add(f"{quad(a, bb, c)} = 0-এর মূলদ্বয় α ও β হলে α³ + β³ = কত?", num(v), setw(num(v), [num(s ** 3 + 3 * s * p), num(s ** 3), num(s ** 3 - p), num(v + 1)]), f"(α + β)³ − 3αβ(α + β) = {num(v)}।", M)
def h_newroots(b):
    r1, r2 = R.sample([v for v in range(-6, 7) if v], 2); a, bb, c = roots_q(r1, r2)
    n1, n2 = r1 * r1, r2 * r2
    if n1 == n2: return
    A, B, C = roots_q(n1, n2); ok = f"{quad(A, B, C)} = 0"
    b.add(f"{quad(a, bb, c)} = 0-এর মূলদ্বয় α ও β হলে যে সমীকরণের মূলদ্বয় α² ও β², সেটি কোনটি?", ok, setw(ok, [f"{quad(1, -B, C)} = 0", f"{quad(1, B, -C)} = 0", f"{quad(1, -(n1 + n2) + 1, C)} = 0", f"{quad(1, B, C + 1)} = 0"]), f"α² + β² = {n1 + n2}, α²β² = {n1 * n2}।", H)
def h_shift(b):
    r1, r2 = R.sample([v for v in range(-6, 7) if v], 2); a, bb, c = roots_q(r1, r2); k = R.choice([1, 2, 3, -1, -2])
    A, B, C = roots_q(r1 + k, r2 + k); ok = f"{quad(A, B, C)} = 0"
    if B == 0 or C == 0: return
    W = roots_q(r1 - k, r2 - k)
    b.add(f"{quad(a, bb, c)} = 0-এর মূলদ্বয় α ও β হলে যে সমীকরণের মূলদ্বয় α {'+' if k > 0 else '−'} {abs(k)} ও β {'+' if k > 0 else '−'} {abs(k)}, সেটি কোনটি?", ok, setw(ok, [f"{quad(*W)} = 0", f"{quad(1, -B, C)} = 0", f"{quad(1, B, -C)} = 0", f"{quad(1, B + 1, C)} = 0"]), f"নতুন মূলের যোগফল {num(r1 + r2 + 2 * k)}, গুণফল {num((r1 + k) * (r2 + k))}।", H)
def h_recip_eq(b):
    r1, r2 = R.sample([v for v in range(-6, 7) if v and abs(v) != 1], 2); a, bb, c = roots_q(r1, r2)
    # 1/α, 1/β মূল ⇒ c x² + b x + a = 0
    ok = f"{quad(c, bb, a)} = 0"
    b.add(f"{quad(a, bb, c)} = 0-এর মূলদ্বয় α ও β হলে 1/α ও 1/β মূলবিশিষ্ট সমীকরণ কোনটি?", ok, setw(ok, [f"{quad(c, -bb, a)} = 0", f"{quad(a, bb, c)} = 0", f"{quad(c, bb, -a)} = 0", f"{quad(1, bb, c)} = 0"]), "x-এর স্থলে 1/x বসিয়ে সহগ উল্টে যায়।", H)
def h_diffk(b):
    d = R.randint(1, 8); s = R.randint(-9, 9)
    if (s + d) % 2: return
    r1, r2 = (s + d) // 2, (s - d) // 2; k = r1 * r2
    b.add(f"x² {'−' if s > 0 else '+'} {abs(s) if abs(s) != 1 else ''}x + k = 0 সমীকরণের মূলদ্বয়ের অন্তর {d} হলে k = কত?".replace(' + 0x', '').replace(' − 0x', ''), num(k), setw(num(k), [num(k + d), num(-k) if k else '1', num(F(s * s + d * d, 4)), num(k - 1)]), f"(α − β)² = (α + β)² − 4αβ ⇒ {d * d} = {s * s} − 4k ⇒ k = {num(k)}।", H)
p52 = run('5.2', R, fx52, [e_sum, e_prod, e_form], [m_sq, m_recip, m_diff2, m_kroot, m_ratio, m_cube], [h_newroots, h_shift, h_recip_eq, h_diffk])

# ---------------- 5.3 করণী সমীকরণ ----------------
fx53 = [
 ("করণী সমীকরণ সমাধানের পর মূল যাচাই করা হয় কেন?", "বর্গ করার ফলে অতিরিক্ত (অবাঞ্ছিত) মূল আসতে পারে", ["সমীকরণ জটিল হয় বলে", "মূল সবসময় ঋণাত্মক হয় বলে", "নিশ্চায়ক শূন্য হয় বলে"], "বর্গ করলে নতুন মূল যুক্ত হতে পারে।", E),
 ("যে সমীকরণে চলক বর্গমূল চিহ্নের ভিতরে থাকে তাকে কী বলে?", "করণী সমীকরণ", ["সূচক সমীকরণ", "রৈখিক সমীকরণ", "লগারিদমীয় সমীকরণ"], "করণী (মূলদ নয়) সমীকরণ।", E),
 ("√x = −3 সমীকরণের সমাধান কী?", "কোনো বাস্তব সমাধান নেই", ["x = 9", "x = −9", "x = 3"], "বর্গমূলের মুখ্য মান ঋণাত্মক নয়।", M),
]
def e_sqrt(b):
    a, k = R.randint(-9, 12), R.randint(1, 9)
    x = k * k - a
    b.add(f"√(x {'+' if a >= 0 else '−'} {abs(a)}) = {k} হলে x = কত?".replace('x + 0', 'x').replace('x − 0', 'x'), num(x), setw(num(x), [num(k - a), num(k * k + a), num(x + 1), num(2 * k - a)]), f"x {'+' if a >= 0 else '−'} {abs(a)} = {k * k} ⇒ x = {num(x)}।", E)
def e_sqrt2(b):
    p, q, k = R.randint(2, 6), R.randint(-9, 9), R.randint(1, 9)
    if (k * k - q) % p: return
    x = (k * k - q) // p
    b.add(f"√({p}x {'+' if q >= 0 else '−'} {abs(q)}) = {k} হলে x = কত?".replace(' + 0)', ')').replace(' − 0)', ')'), num(x), setw(num(x), [num(x + 1), num(F(k - q, p)) if F(k - q, p) != x else num(x - 1), num(k * k), num(x + 2)]), f"{p}x {'+' if q >= 0 else '−'} {abs(q)} = {k * k} ⇒ x = {num(x)}।", E)
def e_cbrt(b):
    a, k = R.randint(-9, 9), R.randint(-4, 5)
    x = k ** 3 - a
    b.add(f"∛(x {'+' if a >= 0 else '−'} {abs(a)}) = {num(k)} হলে x = কত?".replace('x + 0', 'x').replace('x − 0', 'x'), num(x), setw(num(x), [num(k * k - a), num(k ** 3 + a), num(x + 1), num(3 * k - a)]), f"x {'+' if a >= 0 else '−'} {abs(a)} = ({num(k)})³ = {num(k ** 3)}।", E)
def e_two(b):
    x = R.randint(0, 20); a = R.randint(1, 10)
    # √(x + a) = √(2x − k) etc: √(px + q) = √(rx + s)
    p, r = R.sample(range(1, 6), 2); q = R.randint(-10, 10); s = (p - r) * x + q
    b.add(f"√({lin and pfmt(lin([p], q), X)}) = √({pfmt(lin([r], s), X)}) হলে x = কত?", x, setw(x, [x + 1, abs(x - 1) if x != 1 else 3, x + 2, x * 2 if x else 5]), f"{p}x {'+' if q >= 0 else '−'} {abs(q)} = {r}x {'+' if s >= 0 else '−'} {abs(s)} ⇒ x = {x}।", E)
def m_ext(b):
    # √(x + a) = x − c  ⇒ x + a = (x − c)² ; একটি গ্রহণযোগ্য মূল
    x1 = R.randint(2, 12); c = R.randint(0, x1 - 1); a = (x1 - c) ** 2 - x1
    # অপর মূল: x² − (2c + 1)x + c² − a = 0 ⇒ x2 = 2c + 1 − x1
    x2 = 2 * c + 1 - x1
    if x2 - c >= 0 or x2 + a < 0: return
    b.add(f"√(x {'+' if a >= 0 else '−'} {abs(a)}) = x {'−' if c > 0 else '+'} {abs(c)} সমীকরণের সমাধান কোনটি?".replace('x + 0)', 'x)').replace('x − 0)', 'x)').replace(' = x + 0 ', ' = x ').replace(' = x − 0 ', ' = x '), f"x = {x1}", setw(f"x = {x1}", [f"x = {num(x2)}", f"x = {x1}, {num(x2)}", f"x = {x1 + 1}", "কোনো সমাধান নেই"]), f"বর্গ করে x = {x1} বা {num(x2)}; যাচাই করলে x = {num(x2)} গ্রহণযোগ্য নয়।", M)
def m_sum(b):
    # √(x + a) + √x = k  ⇒ √x = (k² − a)/(2k)
    t = R.randint(1, 6); k = R.randint(t + 1, t + 6); a = k * k - 2 * k * t
    if a <= 0: return
    x = t * t
    b.add(f"√(x + {a}) + √x = {k} হলে x = কত?", x, setw(x, [t, x + 1, a, (k - t) ** 2]), f"√(x + {a}) = {k} − √x; বর্গ করে √x = {t} ⇒ x = {x}।", M)
def m_diff(b):
    t = R.randint(1, 8); k = R.randint(1, 5); a = 2 * k * t + k * k
    x = t * t
    b.add(f"√(x + {a}) − √x = {k} হলে x = কত?", x, setw(x, [t, x + k, a, (t + k) ** 2]), f"√(x + {a}) = √x + {k}; বর্গ করে 2·{k}√x = {a - k * k} ⇒ √x = {t}।", M)
def m_quad_sub(b):
    # x + √x = k(k+1)  ⇒ √x = k
    k = R.randint(2, 9); v = k * (k + 1)
    b.add(f"x + √x = {v} হলে x = কত?", k * k, setw(k * k, [k, (k + 1) ** 2, v, k * k + 1]), f"√x = y ধরে y² + y − {v} = 0 ⇒ y = {k} ⇒ x = {k * k}।", M)
def m_sq_both(b):
    x = R.randint(1, 10); p = R.randint(1, 4)
    # √(x² + q) = x + p ⇒ q = 2px + p²
    q = 2 * p * x + p * p
    b.add(f"√(x² + {q}) = x + {p} হলে x = কত?", x, setw(x, [x + p, q, x - 1 if x > 1 else x + 2, p]), f"x² + {q} = x² + {2 * p}x + {p * p} ⇒ x = {x}।", M)
def h_nested(b):
    k = R.randint(2, 7)
    # √(x + √(x + ...))  — সরল: √(2x + 1) − √(x − 3) = 2 ধরণের সংখ্যাগত
    x = k * k + 3
    # √(x − 3) = k ; √(x − 3 + 2k + 1) = √((k+1)²) = k + 1
    b.add(f"√(x + {2 * k - 2}) − √(x − 3) = 1 সমীকরণের সমাধান কোনটি?", f"x = {x}", setw(f"x = {x}", [f"x = {k * k}", f"x = {x + 1}", f"x = {(k + 1) ** 2}", "কোনো সমাধান নেই"]), f"√(x − 3) = y ধরলে √(y² + {2 * k + 1}) = y + 1 ⇒ y = {k} ⇒ x = {x}।", H)
def h_sub(b):
    # √(x/(1−x)) + √((1−x)/x) = 13/6 ধরণের: t + 1/t = (p² + q²)/(pq)
    p, q = R.sample(range(1, 6), 2)
    if math.gcd(p, q) > 1: return
    s = F(p * p + q * q, p * q)
    # t = √(x/(1−x)) = p/q ⇒ x = p²/(p² + q²) অথবা q²/(p² + q²)
    x1, x2 = F(p * p, p * p + q * q), F(q * q, p * p + q * q)
    ok = f"x = {fr(min(x1, x2))}, {fr(max(x1, x2))}"
    b.add(f"√(x/(1 − x)) + √((1 − x)/x) = {fr(s)} হলে x = কত?", ok, setw(ok, [f"x = {fr(x1)}", f"x = {fr(F(p, p + q))}, {fr(F(q, p + q))}", f"x = {fr(F(p, q))}, {fr(F(q, p))}", f"x = {fr(x2)}"]), f"t = √(x/(1 − x)) ধরে t + 1/t = {fr(s)} ⇒ t = {p}/{q} বা {q}/{p}।", H)
def h_two_rad(b):
    t = R.randint(1, 6); u = R.randint(1, 6)
    # √(x + a) + √(x + b) = t + u, যেখানে x + a = t², x + b = u²
    x = R.randint(0, 9); a, bb = t * t - x, u * u - x
    if a == bb: return
    b.add(f"√(x {'+' if a >= 0 else '−'} {abs(a)}) + √(x {'+' if bb >= 0 else '−'} {abs(bb)}) = {t + u} হলে x = কত?".replace('x + 0)', 'x)').replace('x − 0)', 'x)'), x, setw(x, [x + 1, t * u, abs(a - bb), x + 3]), f"x = {x} বসালে √{t * t} + √{u * u} = {t + u}।", H)
p53 = run('5.3', R, fx53, [e_sqrt, e_sqrt2, e_cbrt, e_two], [m_ext, m_sum, m_diff, m_quad_sub, m_sq_both], [h_nested, h_sub, h_two_rad])

# ---------------- 5.4 সূচক সমীকরণ ----------------
fx54 = [
 ("aˣ = aʸ (a > 0, a ≠ 1) হলে কোনটি সত্য?", "x = y", ["x = −y", "x = 1/y", "xy = 1"], "ভিত্তি সমান হলে সূচক সমান।", E),
 ("a⁰ = কত? (a ≠ 0)", "1", ["0", "a", "অসংজ্ঞায়িত"], "শূন্য সূচকের নিয়ম।", E),
 ("aᵐ × aⁿ = কত?", "aᵐ⁺ⁿ", ["aᵐⁿ", "aᵐ⁻ⁿ", "2aᵐ⁺ⁿ"], "সূচকের গুণন নিয়ম।", E),
 ("a⁻ⁿ = কত?", "1/aⁿ", ["−aⁿ", "aⁿ", "−1/aⁿ"], "ঋণাত্মক সূচক।", E),
]
BASES = [(2, [4, 8, 16, 32, 64, 128]), (3, [9, 27, 81, 243]), (5, [25, 125, 625]), (7, [49, 343]), (10, [100, 1000])]
def e_exp(b):
    base, pw = R.choice(BASES); v = R.choice(pw); n = round(math.log(v, base))
    a = R.randint(-4, 4)
    x = n - a
    b.add(f"{base}^(x {'+' if a >= 0 else '−'} {abs(a)}) = {v} হলে x = কত?".replace('^(x + 0)', 'ˣ').replace('^(x − 0)', 'ˣ'), num(x), setw(num(x), [num(n), num(n + a), num(x + 1), num(x - 1)]), f"{v} = {base}{sup(n)} ⇒ x {'+' if a >= 0 else '−'} {abs(a)} = {n} ⇒ x = {num(x)}।", E)
def e_neg(b):
    base, pw = R.choice(BASES); v = R.choice(pw); n = round(math.log(v, base))
    b.add(f"{base}ˣ = 1/{v} হলে x = কত?", num(-n), setw(num(-n), [num(n), fr(F(1, n)), num(-n - 1), '0']), f"1/{v} = {base}{sup(-n)}।", E)
def e_zero(b):
    base = R.choice([2, 3, 5, 7, 10, 4, 6]); a = R.randint(-6, 6)
    b.add(f"{base}^(x {'+' if a >= 0 else '−'} {abs(a)}) = 1 হলে x = কত?", num(-a), setw(num(-a), [num(a) if a else '1', '1', '0' if a else '−1', num(-a + 1)]), f"1 = {base}⁰ ⇒ x {'+' if a >= 0 else '−'} {abs(a)} = 0।", E)
def e_mix(b):
    # 4ˣ = 8 ⇒ 2x = 3 ধরণের
    p, q = R.choice([(4, 8), (8, 4), (9, 27), (27, 9), (4, 32), (8, 16), (16, 8), (25, 125), (125, 25), (4, 64), (32, 4), (27, 81), (9, 243)])
    import math as m
    base = 2 if p in (4, 8, 16, 32, 64) else (3 if p in (9, 27, 81, 243) else 5)
    ep, eq = round(m.log(p, base)), round(m.log(q, base))
    x = F(eq, ep)
    b.add(f"{p}ˣ = {q} হলে x = কত?", fr(x), setw(fr(x), [fr(1 / x), fr(F(q, p)), fr(x + 1), str(eq)]), f"{base}{sup(ep)}ˣ = {base}{sup(eq)} ⇒ x = {fr(x)}।", E)
def m_sum2(b):
    # 2^(x+1) + 2^x = k ⇒ 3·2ˣ = k
    base = R.choice([2, 3]); n = R.randint(0, 5); k = (base + 1) * base ** n
    b.add(f"{base}^(x + 1) + {base}ˣ = {k} হলে x = কত?", n, setw(n, [n + 1, n - 1 if n else 2, k // base, base * n]), f"{base}ˣ({base} + 1) = {k} ⇒ {base}ˣ = {base ** n} ⇒ x = {n}।", M)
def m_quad_exp(b):
    base = R.choice([2, 3]); n1, n2 = R.sample(range(0, 5), 2)
    s, p = base ** n1 + base ** n2, base ** (n1 + n2)
    ok = Sx(n1, n2)
    b.add(f"{base * base}ˣ − {s}·{base}ˣ + {p} = 0 হলে x-এর মানসমূহ কোনটি?", ok, setw(ok, [Sx(base ** n1, base ** n2), Sx(n1 + 1, n2 + 1), Sx(-n1, -n2) if n1 or n2 else Sx(1, 2), Sx(n1, n2 + 2)]), f"y = {base}ˣ ধরে y² − {s}y + {p} = 0 ⇒ y = {base ** n1}, {base ** n2}।", M)
def m_same(b):
    # a^(px + q) = a^(rx + s)
    p, r = R.sample(range(1, 6), 2); x = R.randint(-5, 6); q = R.randint(-6, 6); s = (p - r) * x + q
    base = R.choice([2, 3, 5, 7])
    b.add(f"{base}^({pfmt(lin([p], q), X)}) = {base}^({pfmt(lin([r], s), X)}) হলে x = কত?", num(x), [num(w) for w in near(x)], f"{pfmt(lin([p], q), X)} = {pfmt(lin([r], s), X)} ⇒ x = {num(x)}।", M)
def m_root_exp(b):
    base = R.choice([2, 3]); k = R.randint(2, 4); n = R.randint(1, 6)
    # ᵏ√(baseˣ) = base^n ⇒ x = kn
    b.add(f"{k}-তম মূল {base}ˣ = {base ** n} অর্থাৎ ({base}ˣ)^(1/{k}) = {base ** n} হলে x = কত?", k * n, setw(k * n, [n, n + k, k * n + 1, base ** n]), f"x/{k} = {n} ⇒ x = {k * n}।", M)
def m_eqprod(b):
    base = R.choice([2, 3, 5]); a, c = R.randint(1, 4), R.randint(1, 4); n = R.randint(a + c, a + c + 6)
    x = n - a - c
    b.add(f"{base ** a}·{base}ˣ·{base ** c} = {base ** n} হলে x = কত?", x, setw(x, [n, x + 1, n - a, x * 2 if x else 3]), f"{base}^(x + {a + c}) = {base}{sup(n)} ⇒ x = {x}।", M)
def h_ratio(b):
    base = R.choice([2, 3]); n = R.randint(1, 5)
    # (base^(x+2) − base^(x+1)) / (base^(x+1) − base^x) = base
    v = (base ** (n + 2) - base ** (n + 1))
    b.add(f"{base}^(x + 2) − {base}^(x + 1) = {v} হলে x = কত?", n, setw(n, [n + 1, n - 1 if n > 1 else n + 2, v // base, n + 2]), f"{base}^(x + 1)({base} − 1) = {v} ⇒ {base}^(x + 1) = {v // (base - 1)} ⇒ x = {n}।", H)
def h_recipexp(b):
    base = R.choice([2, 3]); n = R.randint(1, 4); s = F(base ** n) + F(1, base ** n)
    ok = f"x = ±{n}"
    b.add(f"{base}ˣ + {base}⁻ˣ = {fr(s)} হলে x = কত?", ok, setw(ok, [f"x = {n}", f"x = ±{n + 1}", f"x = ±{base ** n}", "x = 0"]), f"y = {base}ˣ ধরে y + 1/y = {fr(s)} ⇒ y = {base ** n} বা 1/{base ** n}।", H)
def h_mixed(b):
    # 2^(2x+1) − 9·2ˣ + 4 = 0 ⇒ 2y² − 9y + 4 = 0 ⇒ y = 4, 1/2 ⇒ x = 2, −1
    k = R.randint(1, 4); m_ = -1
    y1, y2 = 2 ** k, F(1, 2)
    s = 2 * (y1 + y2); p = 2 * y1 * y2
    ok = Sx(k, -1)
    b.add(f"2^(2x + 1) − {fr(s)}·2ˣ + {fr(p)} = 0 হলে x-এর মানসমূহ কোনটি?", ok, setw(ok, [Sx(k, 1), Sx(2 ** k, F(1, 2)), Sx(-k, 1), Sx(k + 1, -1)]), f"y = 2ˣ ধরে 2y² − {fr(s)}y + {fr(p)} = 0 ⇒ y = {2 ** k}, 1/2।", H)
def h_frac_base(b):
    a, c = R.choice([(2, 3), (3, 2), (2, 5), (5, 2), (3, 4), (4, 3)]); n = R.randint(1, 4)
    x = -n
    b.add(f"({a}/{c})ˣ = {c ** n}/{a ** n} হলে x = কত?", num(x), setw(num(x), [num(n), fr(F(1, n)) if n > 1 else '0', num(x - 1), num(n + 1)]), f"{c ** n}/{a ** n} = ({a}/{c}){sup(-n)}।", H)
p54 = run('5.4', R, fx54, [e_exp, e_neg, e_zero, e_mix], [m_sum2, m_quad_exp, m_same, m_root_exp, m_eqprod], [h_ratio, h_recipexp, h_mixed, h_frac_base])

# ---------------- 5.5 দুই চলকের দ্বিঘাত সহসমীকরণ ----------------
def pair(x, y): return f"({num(x)}, {num(y)})"
def pairs(*ps): return ', '.join(pair(*p) for p in sorted(set(ps)))
fx55 = [
 ("x + y = a ও xy = b হলে x ও y কোন সমীকরণের মূল?", "t² − at + b = 0", ["t² + at + b = 0", "t² − bt + a = 0", "t² + at − b = 0"], "যোগফল ও গুণফল থেকে দ্বিঘাত সমীকরণ।", E),
 ("(x + y)² − (x − y)² = কত?", "4xy", ["2xy", "x² − y²", "0"], "অভেদ।", E),
 ("(x + y)² + (x − y)² = কত?", "2(x² + y²)", ["4xy", "x² + y²", "2xy"], "অভেদ।", E),
]
def e_check(b):
    x, y = R.randint(-6, 8), R.randint(-6, 8); s, p = x + y, x * y
    ok = pair(x, y)
    b.add(f"x + y = {num(s)} এবং xy = {num(p)} হলে নিচের কোন জোড়টি সমাধান?", ok, setw(ok, [pair(x + 1, y - 1), pair(-x, -y), pair(x, -y) if y else pair(x, 2), pair(x + 2, y)]), f"{num(x)} + ({num(y)}) = {num(s)}, {num(x)} × ({num(y)}) = {num(p)}।", E)
def e_sq(b):
    s, p = R.randint(-9, 12), R.randint(-10, 20)
    v = s * s - 2 * p
    b.add(f"x + y = {num(s)} এবং xy = {num(p)} হলে x² + y² = কত?", num(v), setw(num(v), [num(s * s + 2 * p), num(s * s - p), num(s * s), num(v + 1)]), f"(x + y)² − 2xy = {num(v)}।", E)
def e_diff(b):
    s, p = R.randint(1, 12), R.randint(-10, 30)
    v = s * s - 4 * p
    if v < 0: return
    b.add(f"x + y = {s} এবং xy = {num(p)} হলে (x − y)² = কত?", num(v), setw(num(v), [num(s * s + 4 * p), num(s * s - 2 * p), num(v + 4), num(s * s)]), f"(x + y)² − 4xy = {num(v)}।", E)
def e_lin(b):
    x, y = R.randint(1, 9), R.randint(1, 9)
    b.add(f"x + y = {x + y} এবং x − y = {num(x - y)} হলে xy = কত?", x * y, setw(x * y, [x * y + 1, x + y, abs(x - y) * (x + y), x * x]), f"x = {x}, y = {y}; xy = {x * y}।", E)
def m_solve(b):
    x, y = R.sample(range(1, 10), 2); s, p = x + y, x * y
    ok = pairs((x, y), (y, x))
    b.add(f"x + y = {s}, xy = {p} সমীকরণজোটের সমাধান কোনটি?", ok, setw(ok, [pair(x, y), pairs((-x, -y), (-y, -x)), pairs((x, -y), (-y, x)), pairs((x + 1, y - 1), (y - 1, x + 1))]), f"t² − {s}t + {p} = 0 ⇒ t = {x}, {y}।", M)
def m_solve2(b):
    x, y = R.sample(range(1, 10), 2)
    if x < y: x, y = y, x
    d, p = x - y, x * y
    ok = pairs((x, y), (-y, -x))
    b.add(f"x − y = {d}, xy = {p} সমীকরণজোটের সমাধান কোনটি?", ok, setw(ok, [pair(x, y), pairs((y, x), (-x, -y)), pairs((x, -y), (-x, y)), pairs((x + 1, y + 1), (-y, -x))]), f"y = x − {d} বসিয়ে x² − {d}x − {p} = 0 ⇒ x = {x} বা {-y}।", M)
def m_sqsum(b):
    x, y = R.sample(range(1, 10), 2); q = x * x + y * y; s = x + y
    b.add(f"x² + y² = {q} এবং x + y = {s} হলে xy = কত?", x * y, setw(x * y, [q - s * s, (s * s + q) // 2, x * y + 1, s * s - q]), f"2xy = (x + y)² − (x² + y²) = {s * s} − {q} ⇒ xy = {x * y}।", M)
def m_diffsq(b):
    x, y = R.sample(range(1, 12), 2)
    if x < y: x, y = y, x
    b.add(f"x² − y² = {x * x - y * y} এবং x − y = {x - y} হলে x + y = কত?", x + y, setw(x + y, [x - y, x * y, x + y + 1, (x * x - y * y) // 2 if (x * x - y * y) % 2 == 0 else x + y + 2]), f"x + y = {x * x - y * y}/{x - y} = {x + y}।", M)
def m_cube(b):
    s, p = R.randint(1, 7), R.randint(-6, 10)
    v = s ** 3 - 3 * s * p
    b.add(f"x + y = {s} এবং xy = {num(p)} হলে x³ + y³ = কত?", num(v), setw(num(v), [num(s ** 3 + 3 * s * p), num(s ** 3), num(s ** 3 - p), num(v + 1)]), f"(x + y)³ − 3xy(x + y) = {num(v)}।", M)
def m_line_circle(b):
    x, y = R.choice([(3, 4), (4, 3), (5, 12), (12, 5), (6, 8), (8, 6), (0, 5), (5, 0), (1, 7), (7, 1)])
    r2 = x * x + y * y; s = x + y
    other = (y, x)
    ok = pairs((x, y), other) if (x, y) != other else pair(x, y)
    b.add(f"x² + y² = {r2} এবং x + y = {s} হলে (x, y) = কত?", ok, setw(ok, [pair(x, y), pairs((-x, -y), (-y, -x)), pairs((x, -y), (-y, x)), pairs((x + 1, y - 1), (y - 1, x + 1))]), f"xy = ({s}² − {r2})/2 = {x * y}; t² − {s}t + {x * y} = 0।", M)
def h_hom(b):
    # x² + xy = a, y² + xy = c  ⇒ (x + y)² = a + c
    x, y = R.randint(1, 8), R.randint(1, 8); a, c = x * (x + y), y * (x + y)
    ok = pairs((x, y), (-x, -y))
    b.add(f"x² + xy = {a} এবং y² + xy = {c} হলে (x, y) = কত?", ok, setw(ok, [pair(x, y), pairs((y, x), (-y, -x)), pairs((x, -y), (-x, y)), pairs((x + 1, y), (-x - 1, -y))]), f"যোগ করে (x + y)² = {a + c} ⇒ x + y = ±{x + y}; x = {a}/(x + y)।", H)
def h_ratio(b):
    k = R.randint(2, 4); y = R.randint(1, 6); x = k * y
    q = x * x + y * y
    ok = pairs((x, y), (-x, -y))
    b.add(f"x = {k}y এবং x² + y² = {q} হলে (x, y) = কত?", ok, setw(ok, [pair(x, y), pairs((y, x), (-y, -x)), pairs((x, -y), (-x, y)), pairs((k, 1), (-k, -1)) if y != 1 else pairs((2 * x, 2 * y), (-2 * x, -2 * y))]), f"{k * k + 1}y² = {q} ⇒ y = ±{y}।", H)
def h_rec(b):
    x, y = R.sample(range(2, 9), 2)
    s = F(1, x) + F(1, y); p = F(1, x * y)
    b.add(f"1/x + 1/y = {fr(s)} এবং xy = {x * y} হলে x + y = কত?", x + y, setw(x + y, [abs(x - y), x * y, fr(s * x * y + 1), x + y + 1]), f"(x + y)/xy = {fr(s)} ⇒ x + y = {fr(s)} × {x * y} = {x + y}।", H)
def h_quart(b):
    s, p = R.randint(2, 7), R.randint(1, 10)
    a2 = s * s - 2 * p; v = a2 * a2 - 2 * p * p
    b.add(f"x + y = {s} এবং xy = {p} হলে x⁴ + y⁴ = কত?", v, setw(v, [a2 * a2, a2 * a2 + 2 * p * p, s ** 4, v - 1]), f"x² + y² = {a2}; x⁴ + y⁴ = {a2}² − 2·{p}² = {v}।", H)
p55 = run('5.5', R, fx55, [e_check, e_sq, e_diff, e_lin], [m_solve, m_solve2, m_sqsum, m_diffsq, m_cube, m_line_circle], [h_hom, h_ratio, h_rec, h_quart])

# ---------------- 5.6 সূচক ও লগারিদমীয় সহসমীকরণ ----------------
fx56 = [
 ("logₐ(MN) = কত?", "logₐM + logₐN", ["logₐM × logₐN", "logₐM − logₐN", "M logₐN"], "লগারিদমের গুণফল নিয়ম।", E),
 ("logₐ(M/N) = কত?", "logₐM − logₐN", ["logₐM/logₐN", "logₐM + logₐN", "logₐ(M − N)"], "ভাগফল নিয়ম।", E),
 ("logₐ(Mʳ) = কত?", "r logₐM", ["(logₐM)ʳ", "logₐM + r", "logₐ r·M"], "ঘাত নিয়ম।", E),
 ("logₐa = কত?", "1", ["0", "a", "অসংজ্ঞায়িত"], "a¹ = a।", E),
 ("logₐ1 = কত?", "0", ["1", "a", "অসংজ্ঞায়িত"], "a⁰ = 1।", E),
]
def e_logv(b):
    base = R.choice([2, 3, 5, 10]); n = R.randint(-2, 5); v = F(base) ** n
    b.add(f"log_{base}({fr(v)}) = কত?", num(n), setw(num(n), [num(-n) if n else '1', fr(v), num(n + 1), num(n - 1)]), f"{base}{sup(n)} = {fr(v)}।", E)
def e_logx(b):
    base = R.choice([2, 3, 4, 5, 10]); n = R.randint(1, 4)
    b.add(f"log_{base} x = {n} হলে x = কত?", base ** n, setw(base ** n, [base * n, n ** base, base ** (n + 1), base ** n + 1]), f"x = {base}{sup(n)} = {base ** n}।", E)
def e_expsys(b):
    x, y = R.randint(-3, 6), R.randint(-3, 6); base = R.choice([2, 3, 5])
    b.add(f"{base}ˣ·{base}ʸ = {base}{sup(x + y)} এবং {base}ˣ ÷ {base}ʸ = {base}{sup(x - y)} হলে x = কত?", num(x), setw(num(x), [num(y), num(x + y), num(x - y), num(x + 1)]), f"x + y = {x + y}, x − y = {x - y} ⇒ x = {num(x)}।", E)
def e_logsum(b):
    a, c = R.choice([(2, 5), (4, 25), (20, 5), (50, 2), (25, 40), (8, 125), (200, 5)]); v = round(math.log10(a * c))
    b.add(f"log {a} + log {c} = কত? (ভিত্তি 10)", v, setw(v, [a + c, v + 1, round(math.log10(a + c), 2), v - 1]), f"log({a} × {c}) = log {a * c} = {v}।", E)
def m_logsys(b):
    x, y = R.randint(1, 4), R.randint(1, 4); base = R.choice([2, 3, 10])
    # log x + log y = log(base^(x+y))... সরল: log_b X + log_b Y = s, log_b X − log_b Y = d ⇒ X = b^x, Y = b^y
    X_, Y_ = base ** x, base ** y
    b.add(f"log_{base} X + log_{base} Y = {x + y} এবং log_{base} X − log_{base} Y = {num(x - y)} হলে X = কত?", X_, setw(X_, [Y_, x, base ** (x + y), X_ * base]), f"log_{base} X = {x} ⇒ X = {X_}।", M)
def m_expsys2(b):
    x, y = R.randint(0, 4), R.randint(0, 4)
    # 2ˣ + 3ʸ = A, 2ˣ − 3ʸ = B
    A, B = 2 ** x + 3 ** y, 2 ** x - 3 ** y
    ok = pair(x, y)
    b.add(f"2ˣ + 3ʸ = {A} এবং 2ˣ − 3ʸ = {num(B)} হলে (x, y) = কত?", ok, setw(ok, [pair(y, x), pair(2 ** x, 3 ** y), pair(x + 1, y), pair(x, y + 1)]), f"2ˣ = {2 ** x}, 3ʸ = {3 ** y}।", M)
def m_eqlog(b):
    x = R.randint(2, 12); a = R.randint(1, 8)
    # log(x + a) + log(x − ?)...  log_b(x + a) = log_b(2x − c) ⇒ x = a + c
    c = x - a
    if 2 * x - c <= 0: return
    b.add(f"log(x + {a}) = log(2x {'−' if c > 0 else '+'} {abs(c)}) হলে x = কত?".replace(' − 0)', ')').replace(' + 0)', ')'), x, setw(x, [a, x + 1, a + 2 * c if a + 2 * c != x else x + 3, 2 * x]), f"x + {a} = 2x {'−' if c > 0 else '+'} {abs(c)} ⇒ x = {x}।", M)
def m_logprod(b):
    base = R.choice([2, 3]); r1 = R.randint(1, 5); k = R.randint(1, 4)
    # log_b x + log_b(x + d) = k ⇒ x(x + d) = b^k
    v = base ** k; cand = [(d, x) for x in range(1, 40) for d in range(1, 30) if x * (x + d) == v]
    if not cand: return
    d, x = R.choice(cand)
    b.add(f"log_{base} x + log_{base}(x + {d}) = {k} হলে x = কত?", x, setw(x, [-(x + d), x + d, v, x + 1]), f"x(x + {d}) = {v} ⇒ x = {x} (ঋণাত্মক মূল বাদ)।", M)
def m_changebase(b):
    a, c = R.choice([(2, 8), (4, 64), (3, 81), (9, 27), (8, 32), (27, 9), (16, 8), (25, 125), (4, 8), (32, 2)])
    v = F(round(math.log(c, 2 if a in (2, 4, 8, 16, 32) else (3 if a in (3, 9, 27, 81) else 5))), round(math.log(a, 2 if a in (2, 4, 8, 16, 32) else (3 if a in (3, 9, 27, 81) else 5))))
    b.add(f"log_{a} {c} = কত?", fr(v), setw(fr(v), [fr(1 / v), fr(F(c, a)), fr(v + 1), str(c // a if c % a == 0 else c - a)]), f"ভিত্তি পরিবর্তন করে = {fr(v)}।", M)
def h_sys_log(b):
    x, y = R.randint(1, 3), R.randint(1, 3)
    X_, Y_ = 10 ** x, 10 ** y
    # log x + log y = x + y; xy = 10^(x+y); x/y = 10^(x−y)
    ok = pair(X_, Y_)
    b.add(f"log x + log y = {x + y} এবং log x − log y = {num(x - y)} হলে (x, y) = কত? (ভিত্তি 10)", ok, setw(ok, [pair(x, y), pair(Y_, X_), pair(10 * x, 10 * y), pair(X_ * 10, Y_)]), f"log x = {x}, log y = {y}।", H)
def h_mixed(b):
    x, y = R.randint(1, 4), R.randint(1, 4)
    # 2ˣ·3ʸ = A এবং 3ˣ·2ʸ = B
    A, B = 2 ** x * 3 ** y, 3 ** x * 2 ** y
    if A == B: return
    ok = pair(x, y)
    b.add(f"2ˣ·3ʸ = {A} এবং 3ˣ·2ʸ = {B} হলে (x, y) = কত?", ok, setw(ok, [pair(y, x), pair(x + 1, y), pair(x, y + 1), pair(x + 1, y + 1)]), f"গুণ করে 6^(x + y) = {A * B} ⇒ x + y = {x + y}; ভাগ করে (2/3)^(x − y) = {fr(F(A, B))} ⇒ x − y = {num(x - y)}।", H)
def h_logsq(b):
    base = R.choice([2, 3]); n1, n2 = R.sample(range(-2, 4), 2)
    s, p = n1 + n2, n1 * n2
    ok = Sx(F(base) ** n1, F(base) ** n2)
    b.add(f"(log_{base} x)² {'−' if s > 0 else '+'} {abs(s)}·log_{base} x {'+' if p >= 0 else '−'} {abs(p)} = 0 হলে x-এর মানসমূহ কোনটি?".replace(' + 0·log', '').replace(' − 0·log', '').replace(f' + 0 = 0', ' = 0').replace(f' − 0 = 0', ' = 0').replace('0·log_2 x', '').replace('0·log_3 x', ''), ok, setw(ok, [Sx(n1, n2), Sx(F(base) ** -n1, F(base) ** -n2), Sx(F(base) ** (n1 + 1), F(base) ** n2), Sx(base * n1, base * n2)]), f"log_{base} x = {num(n1)} বা {num(n2)}।", H)
p56 = run('5.6', R, fx56, [e_logv, e_logx, e_expsys, e_logsum], [m_logsys, m_expsys2, m_eqlog, m_logprod, m_changebase], [h_sys_log, h_mixed, h_logsq])

# ---------------- 5.7 সমীকরণের বাস্তব প্রয়োগ ----------------
fx57 = [
 ("কোনো সংখ্যা ও তার বর্গের যোগফল 0 হলে সংখ্যাটি কত হতে পারে?", "0 অথবা −1", ["1 অথবা −1", "শুধু 0", "শুধু 1"], "x² + x = 0 ⇒ x(x + 1) = 0।", E),
 ("বাস্তব সমস্যার সমীকরণ থেকে পাওয়া ঋণাত্মক দৈর্ঘ্য বা বয়সের মান কী করা হয়?", "বাদ দেওয়া হয়", ["গ্রহণ করা হয়", "পরম মান নেওয়া হয়", "দ্বিগুণ করা হয়"], "দৈর্ঘ্য বা বয়স ঋণাত্মক হতে পারে না।", E),
]
def e_rect(b):
    w, d = R.randint(2, 15), R.randint(1, 10); A = w * (w + d)
    b.add(f"একটি আয়তক্ষেত্রের দৈর্ঘ্য প্রস্থ অপেক্ষা {d} মিটার বেশি এবং ক্ষেত্রফল {A} বর্গমিটার। প্রস্থ কত মিটার?", w, setw(w, [w + d, A // 4, w + 1, d]), f"x(x + {d}) = {A} ⇒ x = {w}।", E)
def e_cons(b):
    n = R.randint(2, 20)
    b.add(f"দুটি ক্রমিক স্বাভাবিক সংখ্যার গুণফল {n * (n + 1)}। ছোট সংখ্যাটি কত?", n, setw(n, [n + 1, n - 1, n * 2, (n * (n + 1)) // 2]), f"x(x + 1) = {n * (n + 1)} ⇒ x = {n}।", E)
def e_sqnum(b):
    n = R.randint(2, 20); k = R.randint(1, 20)
    b.add(f"কোনো ধনাত্মক সংখ্যার বর্গ থেকে {k} বিয়োগ করলে {n * n - k} হয়। সংখ্যাটি কত?", n, setw(n, [n + 1, n * n, n - 1, k]), f"x² = {n * n} ⇒ x = {n}।", E)
def e_sumsq(b):
    a = R.randint(1, 15)
    b.add(f"দুটি ক্রমিক স্বাভাবিক সংখ্যার বর্গের যোগফল {a * a + (a + 1) ** 2}। বড় সংখ্যাটি কত?", a + 1, setw(a + 1, [a, a + 2, a * a, 2 * a + 1]), f"x² + (x + 1)² = {a * a + (a + 1) ** 2} ⇒ x = {a}; বড় সংখ্যা {a + 1}।", E)
def m_recip(b):
    p, q = R.sample(range(1, 8), 2)
    if math.gcd(p, q) > 1: return
    s = F(p, q) + F(q, p)
    b.add(f"একটি ধনাত্মক ভগ্নাংশ ও তার অন্যোন্যকের যোগফল {fr(s)}। ভগ্নাংশটি কত হতে পারে?", fr(F(min(p, q), max(p, q))), setw(fr(F(min(p, q), max(p, q))), [fr(F(min(p, q), max(p, q)) + 1), fr(s / 2), fr(F(min(p, q) + 1, max(p, q))), fr(F(1, p * q))]), f"x + 1/x = {fr(s)} ⇒ x = {p}/{q} বা {q}/{p}।", M)
def m_speed(b):
    v = R.randint(10, 60); d = R.choice([60, 90, 120, 150, 180, 240, 300]); k = R.randint(5, 15)
    t1 = F(d, v); t2 = F(d, v + k)
    diff = t1 - t2
    if diff.denominator > 4: return
    b.add(f"একটি গাড়ি {d} কিমি পথ অতিক্রম করে। গতিবেগ ঘণ্টায় {k} কিমি বেশি হলে {fr(diff)} ঘণ্টা কম লাগত। গাড়িটির গতিবেগ ঘণ্টায় কত কিমি?", v, setw(v, [v + k, v - k if v > k else v + 2 * k, d // k if d // k != v else v + 5, v + 1]), f"{d}/x − {d}/(x + {k}) = {fr(diff)} ⇒ x = {v}।", M)
def m_perim(b):
    w, l = R.sample(range(3, 25), 2); P = 2 * (w + l); A = w * l
    b.add(f"একটি আয়তক্ষেত্রের পরিসীমা {P} মিটার ও ক্ষেত্রফল {A} বর্গমিটার। বড় বাহুর দৈর্ঘ্য কত মিটার?", max(w, l), setw(max(w, l), [min(w, l), P // 4, max(w, l) + 1, A // 4 if A // 4 != max(w, l) else A // 2]), f"x + y = {w + l}, xy = {A} ⇒ {max(w, l)}, {min(w, l)}।", M)
def m_age(b):
    s = R.randint(4, 15); k = R.randint(2, 6)
    f = s * s + k   # বাবার বয়স = পুত্রের বয়সের বর্গ + k
    if f > 70 or f < 2 * s: return
    b.add(f"পিতার বয়স পুত্রের বয়সের বর্গ অপেক্ষা {k} বছর বেশি। তাদের বয়সের সমষ্টি {f + s} বছর হলে পুত্রের বয়স কত বছর?", s, setw(s, [s + 1, f, (f + s) // 2, s - 1]), f"x² + {k} + x = {f + s} ⇒ x = {s}।", M)
def m_digits(b):
    t, u = R.randint(1, 9), R.randint(0, 9)
    n = 10 * t + u; p = t * u
    if not p: return
    b.add(f"দুই অঙ্কবিশিষ্ট একটি সংখ্যার অঙ্কদ্বয়ের গুণফল {p} এবং দশক স্থানীয় অঙ্ক এককের অঙ্কের চেয়ে {t - u} {'বেশি' if t > u else 'কম'}। সংখ্যাটি কত?".replace(' 0 বেশি', ' সমান').replace(f' {t - u} কম', f' {u - t} কম'), n, setw(n, [10 * u + t, n + 1, n + 10, t + u]), f"অঙ্কদ্বয় {t} ও {u} ⇒ {n}।", M)
def m_path(b):
    L, W, w = R.randint(10, 40), R.randint(8, 30), R.randint(1, 4)
    A = (L + 2 * w) * (W + 2 * w) - L * W
    b.add(f"{L} মি × {W} মি আয়তাকার বাগানের চারদিকে সমান চওড়া একটি রাস্তার ক্ষেত্রফল {A} বর্গমিটার। রাস্তাটি কত মিটার চওড়া?", w, setw(w, [w + 1, w * 2, A // (L + W), w + 2]), f"(L + 2x)(W + 2x) − LW = {A} ⇒ x = {w}।", M)
def h_work(b):
    a = R.randint(4, 20); d = R.randint(2, 10); bb = a + d
    t = F(a * bb, a + bb)
    if t.denominator > 1: return
    b.add(f"A একা একটি কাজ B অপেক্ষা {d} দিন কম সময়ে শেষ করে। দুজনে একত্রে কাজটি {fr(t)} দিনে শেষ করে। A একা কত দিনে কাজটি শেষ করবে?", a, setw(a, [bb, a + 1, int(t) * 2, a - 1]), f"1/x + 1/(x + {d}) = 1/{fr(t)} ⇒ x = {a}।", H)
def h_boat(b):
    u, c = R.randint(8, 20), R.randint(1, 6); d = R.choice([24, 30, 36, 40, 48, 60, 72, 80, 90, 96])
    T = F(d, u + c) + F(d, u - c)
    if T.denominator > 2: return
    b.add(f"একটি নৌকা স্রোতের অনুকূলে {d} কিমি গিয়ে আবার ফিরে আসতে মোট {fr(T)} ঘণ্টা লাগে। স্রোতের বেগ ঘণ্টায় {c} কিমি হলে স্থির পানিতে নৌকার বেগ কত?", u, setw(u, [u + c, u - c, d // 4 if d // 4 != u else u + 3, u + 1]), f"{d}/(x + {c}) + {d}/(x − {c}) = {fr(T)} ⇒ x = {u}।", H)
def h_price(b):
    n, p = R.randint(5, 30), R.randint(5, 40)
    total = n * p; k = R.randint(1, 5)
    # দাম k টাকা কম হলে আরও m টি বেশি: total/(p − k) − n = m
    if p <= k or total % (p - k): return
    m_ = total // (p - k) - n
    b.add(f"{total} টাকায় কিছু কলম কেনা হলো। প্রতিটির দাম {k} টাকা কম হলে আরও {m_}টি কলম বেশি পাওয়া যেত। প্রতিটি কলমের দাম কত টাকা?", p, setw(p, [p - k, n, p + k, total // (n + m_) if total // (n + m_) != p - k else p + 1]), f"{total}/(x − {k}) − {total}/x = {m_} ⇒ x = {p}।", H)
def h_tri(b):
    a, c = R.choice([(3, 4), (5, 12), (6, 8), (8, 15), (7, 24), (9, 12), (20, 21), (12, 16), (9, 40)])
    h = math.isqrt(a * a + c * c)
    b.add(f"একটি সমকোণী ত্রিভুজের অতিভুজ {h} সেমি এবং অপর দুই বাহুর অন্তর {c - a} সেমি। ক্ষুদ্রতম বাহু কত সেমি?", a, setw(a, [c, h - c if h - c != a else a + 1, a + c - h, c - a]), f"x² + (x + {c - a})² = {h}² ⇒ x = {a}।", H)
p57 = run('5.7', R, fx57, [e_rect, e_cons, e_sqnum, e_sumsq], [m_recip, m_speed, m_perim, m_age, m_digits, m_path], [h_work, h_boat, h_price, h_tri])
save('h5', p51 + p52 + p53 + p54 + p55 + p56 + p57)

# ---------------- 6.1 রৈখিক অসমতা ----------------
fx61 = [
 ("অসমতার উভয় পক্ষকে একই ঋণাত্মক সংখ্যা দিয়ে গুণ করলে কী হয়?", "অসমতার চিহ্ন উল্টে যায়", ["চিহ্ন একই থাকে", "সমীকরণ হয়ে যায়", "অসমতা মিথ্যা হয়"], "যেমন 2 < 3 ⇒ −2 > −3।", E),
 ("অসমতার উভয় পক্ষে একই সংখ্যা যোগ করলে কী হয়?", "চিহ্ন অপরিবর্তিত থাকে", ["চিহ্ন উল্টে যায়", "সমীকরণ হয়", "কিছুই বলা যায় না"], "যোগ-বিয়োগে চিহ্ন বদলায় না।", E),
 ("a > b এবং b > c হলে কোনটি সত্য?", "a > c", ["a < c", "a = c", "কিছুই বলা যায় না"], "সংক্রমণশীলতা।", E),
 ("x ≥ 3 অসমতার সমাধান সেটকে ব্যবধিতে লিখলে কোনটি?", "[3, ∞)", ["(3, ∞)", "(−∞, 3]", "[3, ∞]"], "3 অন্তর্ভুক্ত, তাই বন্ধনী [।", E),
]
def iv(lo=None, hi=None, lc=False, hc=False):
    L = ('[' if lc else '(') + (num(lo) if lo is not None else '−∞'); Hh = (num(hi) if hi is not None else '∞') + (']' if hc else ')')
    return L + ', ' + Hh
def e_lin(b):
    a = R.choice([2, 3, 4, 5, 6]); x = R.randint(-6, 8); c = R.randint(-9, 9); op = R.choice(['<', '>', '≤', '≥'])
    rhs = a * x + c
    ok = f"x {op} {num(x)}"
    flip = {'<': '>', '>': '<', '≤': '≥', '≥': '≤'}[op]
    b.add(f"{pfmt(lin([a], c), X)} {op} {num(rhs)} অসমতার সমাধান কোনটি?", ok, setw(ok, [f"x {flip} {num(x)}", f"x {op} {num(x + 1)}", f"x {op} {num(rhs)}", f"x {flip} {num(-x)}" if x else f"x {flip} 1"]), f"{a}x {op} {num(rhs - c)} ⇒ x {op} {num(x)}।", E)
def e_neg(b):
    a = R.choice([2, 3, 4, 5]); x = R.randint(-6, 8); c = R.randint(-9, 9); op = R.choice(['<', '>', '≤', '≥'])
    rhs = -a * x + c; flip = {'<': '>', '>': '<', '≤': '≥', '≥': '≤'}[op]
    ok = f"x {flip} {num(x)}"
    b.add(f"{pfmt(lin([-a], c), X)} {op} {num(rhs)} অসমতার সমাধান কোনটি?", ok, setw(ok, [f"x {op} {num(x)}", f"x {flip} {num(-x)}" if x else f"x {flip} 2", f"x {op} {num(-x)}" if x else f"x {op} 1", f"x {flip} {num(x + 1)}"]), f"−{a}x {op} {num(rhs - c)}; −{a} দিয়ে ভাগ করলে চিহ্ন উল্টে x {flip} {num(x)}।", E)
def e_int(b):
    a = R.choice([2, 3, 4]); x = R.randint(1, 10); c = R.randint(-5, 5)
    rhs = a * x + c
    # ax + c < rhs ⇒ x < x ; বৃহত্তম পূর্ণসংখ্যা x − 1
    b.add(f"{pfmt(lin([a], c), X)} < {num(rhs)} হলে x-এর বৃহত্তম পূর্ণসাংখ্যিক মান কত?", x - 1, setw(x - 1, [x, x + 1, x - 2, rhs]), f"x < {x} ⇒ বৃহত্তম পূর্ণসংখ্যা {x - 1}।", E)
def e_interval(b):
    lo, hi = sorted(R.sample(range(-8, 10), 2)); lc, hc = R.choice([True, False]), R.choice([True, False])
    ok = iv(lo, hi, lc, hc)
    b.add(f"{num(lo)} {'≤' if lc else '<'} x {'≤' if hc else '<'} {num(hi)}-কে ব্যবধিতে প্রকাশ করলে কোনটি?", ok, setw(ok, [iv(lo, hi, not lc, hc), iv(lo, hi, lc, not hc), iv(lo, hi, not lc, not hc), iv(hi, lo, lc, hc)]), "সমান চিহ্ন থাকলে [ ], না থাকলে ( )।", E)
def m_double(b):
    a = R.choice([2, 3, 4, 5]); c = R.randint(-6, 6); lo, hi = sorted(R.sample(range(-5, 8), 2))
    L, Hh = a * lo + c, a * hi + c
    ok = f"{num(lo)} < x < {num(hi)}"
    b.add(f"{num(L)} < {pfmt(lin([a], c), X)} < {num(Hh)} অসমতার সমাধান কোনটি?", ok, setw(ok, [f"{num(lo)} ≤ x ≤ {num(hi)}", f"{num(L)} < x < {num(Hh)}", f"{num(lo + 1)} < x < {num(hi + 1)}", f"x < {num(lo)} অথবা x > {num(hi)}"]), f"{c} বিয়োগ ও {a} দিয়ে ভাগ করে।", M)
def m_count(b):
    a = R.choice([2, 3]); c = R.randint(-4, 4); lo, hi = sorted(R.sample(range(-5, 9), 2))
    L, Hh = a * lo + c, a * hi + c
    n = hi - lo + 1
    b.add(f"{num(L)} ≤ {pfmt(lin([a], c), X)} ≤ {num(Hh)} অসমতার কয়টি পূর্ণসাংখ্যিক সমাধান আছে?", n, setw(n, [n - 1, n + 1, n - 2 if n > 2 else n + 2, Hh - L]), f"{num(lo)} ≤ x ≤ {num(hi)} ⇒ {n}টি।", M)
def m_frac(b):
    p, q = R.choice([(2, 3), (3, 4), (2, 5), (3, 5), (4, 3)]); x = R.randint(-3, 6) * p * q // math.gcd(p, q)
    lhs = F(x, p) - F(x, q)
    if lhs == 0: return
    ok = f"x > {num(x)}" if (F(1, p) - F(1, q)) > 0 else f"x < {num(x)}"
    b.add(f"x/{p} − x/{q} > {num(lhs)} অসমতার সমাধান কোনটি?", ok, setw(ok, [f"x < {num(x)}" if ok.startswith('x >') else f"x > {num(x)}", f"x > {num(lhs)}", f"x > {num(-x)}" if x else "x > 1", f"x < {num(lhs)}"]), f"x({fr(F(1, p) - F(1, q))}) > {num(lhs)}।", M)
def m_word(b):
    price, budget = R.randint(5, 40), R.randint(100, 900); fixed = R.randint(10, 80)
    n = (budget - fixed) // price
    if n < 2: return
    b.add(f"একজন শিক্ষার্থীর কাছে {budget} টাকা আছে। {fixed} টাকার একটি খাতা কেনার পর প্রতিটি {price} টাকা দামের সর্বোচ্চ কয়টি কলম কিনতে পারবে?", n, setw(n, [n + 1, n - 1, budget // price, (budget + fixed) // price]), f"{fixed} + {price}x ≤ {budget} ⇒ x ≤ {fr(F(budget - fixed, price))}।", M)
def m_both(b):
    a, c = R.randint(2, 5), R.randint(1, 3)
    if a == c: return
    x = R.randint(-5, 7); p = R.randint(-6, 6); q = (a - c) * x + p
    op = '<'
    ok = f"x < {num(x)}" if a > c else f"x > {num(x)}"
    b.add(f"{pfmt(lin([a], p), X)} < {pfmt(lin([c], q), X)} অসমতার সমাধান কোনটি?", ok, setw(ok, [f"x > {num(x)}" if a > c else f"x < {num(x)}", f"x < {num(x + 1)}", f"x < {num(q - p)}", f"x > {num(-x)}" if x else "x > 2"]), f"({a} − {c})x < {num(q - p)}।", M)
def h_age(b):
    s = R.randint(8, 20); k = R.randint(2, 5); t = R.randint(5, 15)
    b.add(f"রনির বয়স {s} বছর এবং বাবার বয়স {k * s + t} বছর। কমপক্ষে কত বছর পর বাবার বয়স রনির বয়সের {k} গুণের চেয়ে কম হবে?", "কখনো না", setw("কখনো না", [f"{t} বছর", f"{t // (k - 1) + 1} বছর", f"{s} বছর", f"{t + 1} বছর"]), f"{k * s + t} + x < {k}({s} + x) ⇒ {t} < {k - 1}x; ... আসলে x > {fr(F(t, k - 1))} বছর পর।", H) if False else None
    x0 = F(t, k - 1); n = math.floor(x0) + 1
    b.add(f"রনির বয়স {s} বছর এবং বাবার বয়স {k * s + t} বছর। ন্যূনতম কত পূর্ণ বছর পর বাবার বয়স রনির বয়সের {k} গুণের চেয়ে কম হবে?", f"{n} বছর", setw(f"{n} বছর", [f"{n - 1} বছর" if n > 1 else f"{n + 2} বছর", f"{n + 1} বছর", f"{t} বছর" if t != n else f"{t + 3} বছর", f"{s} বছর"]), f"{k * s + t} + x < {k}({s} + x) ⇒ x > {fr(x0)} ⇒ ন্যূনতম {n}।", H)
def h_frac2(b):
    a = R.randint(1, 6); c = R.randint(1, 6)
    # (x − a)/(x + c) < 0 ⇒ −c < x < a
    ok = f"{num(-c)} < x < {num(a)}"
    b.add(f"(x − {a})/(x + {c}) < 0 অসমতার সমাধান কোনটি?", ok, setw(ok, [f"x < {num(-c)} অথবা x > {num(a)}", f"{num(-c)} ≤ x ≤ {num(a)}", f"{num(-a)} < x < {num(c)}", f"x > {num(a)}"]), "লব ও হর বিপরীত চিহ্নের হতে হবে।", H)
def h_consec(b):
    s = R.randint(20, 120); k = R.choice([2, 3])
    # k টি ক্রমিক বিজোড়... সরল: ক্রমিক তিনটি স্বাভাবিক সংখ্যার যোগফল s-এর কম হলে বৃহত্তম ক্ষুদ্রতম সংখ্যা
    n = (s - (k * (k - 1)) // 2 - 1) // k
    if n < 1: return
    b.add(f"{k}টি ক্রমিক স্বাভাবিক সংখ্যার যোগফল {s}-এর চেয়ে কম। ক্ষুদ্রতম সংখ্যাটির সর্বোচ্চ মান কত?", n, setw(n, [n + 1, n - 1, s // k, n + 2]), f"{k}x + {k * (k - 1) // 2} < {s} ⇒ x < {fr(F(s - k * (k - 1) // 2, k))}।", H)
def h_mean(b):
    marks = [R.randint(40, 90) for _ in range(3)]; target = R.randint(60, 85)
    need = 4 * target - sum(marks)
    if need > 100 or need < 0: return
    b.add(f"তিনটি পরীক্ষায় প্রাপ্ত নম্বর {marks[0]}, {marks[1]}, {marks[2]}। চার পরীক্ষার গড় কমপক্ষে {target} হতে চতুর্থ পরীক্ষায় ন্যূনতম কত নম্বর লাগবে?", need, setw(need, [need + 1, need - 1, target, 3 * target - sum(marks) if 3 * target - sum(marks) > 0 else need + 4]), f"({sum(marks)} + x)/4 ≥ {target} ⇒ x ≥ {need}।", H)
p61 = run('6.1', R, fx61, [e_lin, e_neg, e_int, e_interval], [m_double, m_count, m_frac, m_word, m_both], [h_age, h_frac2, h_consec, h_mean])

# ---------------- 6.2 দ্বিঘাত ও পরমমান অসমতা ----------------
fx62 = [
 ("|x| < a (a > 0) অসমতার সমাধান কোনটি?", "−a < x < a", ["x < −a অথবা x > a", "x < a", "x > −a"], "পরমমানের সংজ্ঞা।", E),
 ("|x| > a (a > 0) অসমতার সমাধান কোনটি?", "x < −a অথবা x > a", ["−a < x < a", "x > a", "x < a"], "পরমমানের সংজ্ঞা।", E),
 ("|x| < 0 অসমতার সমাধান সেট কোনটি?", "∅", ["{0}", "R", "(0, ∞)"], "পরমমান কখনো ঋণাত্মক নয়।", M),
 ("|x| ≥ 0 অসমতার সমাধান সেট কোনটি?", "R", ["∅", "{0}", "[0, ∞)"], "সব বাস্তব সংখ্যার জন্য সত্য।", M),
 ("(x − a)(x − b) < 0 (a < b) হলে সমাধান কোনটি?", "a < x < b", ["x < a অথবা x > b", "x > b", "x < a"], "উৎপাদক দুটি বিপরীত চিহ্নের।", E),
]
def e_abs(b):
    a, k = R.randint(-6, 8), R.randint(1, 9)
    ok = f"{num(a - k)} < x < {num(a + k)}"
    b.add(f"|x {'−' if a >= 0 else '+'} {abs(a)}| < {k} অসমতার সমাধান কোনটি?".replace('|x − 0|', '|x|'), ok, setw(ok, [f"x < {num(a - k)} অথবা x > {num(a + k)}", f"{num(-a - k)} < x < {num(-a + k)}", f"{num(a - k)} ≤ x ≤ {num(a + k)}", f"{num(-k)} < x < {num(k)}" if a else f"{num(-k - 1)} < x < {num(k + 1)}"]), f"−{k} < x {'−' if a >= 0 else '+'} {abs(a)} < {k}।", E)
def e_abs_gt(b):
    a, k = R.randint(-6, 8), R.randint(1, 9)
    ok = f"x < {num(a - k)} অথবা x > {num(a + k)}"
    b.add(f"|x {'−' if a >= 0 else '+'} {abs(a)}| > {k} অসমতার সমাধান কোনটি?".replace('|x − 0|', '|x|'), ok, setw(ok, [f"{num(a - k)} < x < {num(a + k)}", f"x < {num(-a - k)} অথবা x > {num(-a + k)}", f"x > {num(a + k)}", f"x ≤ {num(a - k)} অথবা x ≥ {num(a + k)}"]), "দূরত্ব k-এর বেশি।", E)
def e_quad(b):
    r1, r2 = sorted(R.sample(range(-7, 9), 2)); a, bb, c = roots_q(r1, r2)
    ok = f"{num(r1)} < x < {num(r2)}"
    b.add(f"{quad(a, bb, c)} < 0 অসমতার সমাধান কোনটি?", ok, setw(ok, [f"x < {num(r1)} অথবা x > {num(r2)}", f"{num(-r2)} < x < {num(-r1)}", f"{num(r1)} ≤ x ≤ {num(r2)}", f"x > {num(r2)}"]), f"(x − ({num(r1)}))(x − ({num(r2)})) < 0।", E)
def e_quad_gt(b):
    r1, r2 = sorted(R.sample(range(-7, 9), 2)); a, bb, c = roots_q(r1, r2)
    ok = f"x < {num(r1)} অথবা x > {num(r2)}"
    b.add(f"{quad(a, bb, c)} > 0 অসমতার সমাধান কোনটি?", ok, setw(ok, [f"{num(r1)} < x < {num(r2)}", f"x < {num(-r2)} অথবা x > {num(-r1)}", f"x > {num(r2)}", f"x ≤ {num(r1)} অথবা x ≥ {num(r2)}"]), "উভয় উৎপাদক একই চিহ্নের।", E)
def m_abs_lin(b):
    p = R.choice([2, 3, 4]); q = R.randint(-6, 6); k = R.randint(1, 9)
    lo, hi = F(-k - q, p), F(k - q, p)
    ok = f"{num(lo)} ≤ x ≤ {num(hi)}"
    b.add(f"|{pfmt(lin([p], q), X)}| ≤ {k} অসমতার সমাধান কোনটি?", ok, setw(ok, [f"x ≤ {num(lo)} অথবা x ≥ {num(hi)}", f"{num(-k - q)} ≤ x ≤ {num(k - q)}", f"{num(F(-k + q, p))} ≤ x ≤ {num(F(k + q, p))}", f"{num(lo)} < x < {num(hi)}"]), f"−{k} ≤ {pfmt(lin([p], q), X)} ≤ {k}।", M)
def m_count_abs(b):
    a, k = R.randint(-5, 6), R.randint(1, 8)
    n = 2 * k - 1
    b.add(f"|x {'−' if a >= 0 else '+'} {abs(a)}| < {k} অসমতার কয়টি পূর্ণসাংখ্যিক সমাধান আছে?".replace('|x − 0|', '|x|'), n, setw(n, [2 * k + 1, 2 * k, k, n - 1]), f"{num(a - k)} < x < {num(a + k)} ⇒ {n}টি।", M)
def m_quad_le(b):
    r1, r2 = sorted(R.sample(range(-6, 8), 2)); a, bb, c = roots_q(r1, r2)
    n = r2 - r1 + 1
    b.add(f"{quad(a, bb, c)} ≤ 0 অসমতার কয়টি পূর্ণসাংখ্যিক সমাধান আছে?", n, setw(n, [n - 1, n + 1, n - 2 if n > 2 else n + 2, r2 - r1 - 1 if r2 - r1 - 1 not in (n - 1,) else n + 3]), f"{num(r1)} ≤ x ≤ {num(r2)} ⇒ {n}টি।", M)
def m_sq(b):
    k = R.randint(1, 12)
    ok = f"−{k} < x < {k}"
    b.add(f"x² < {k * k} অসমতার সমাধান কোনটি?", ok, setw(ok, [f"x < {k}", f"x < −{k} অথবা x > {k}", f"0 < x < {k}", f"−{k * k} < x < {k * k}"]), f"|x| < {k}।", M)
def m_neg_lead(b):
    r1, r2 = sorted(R.sample(range(-6, 8), 2)); a, bb, c = roots_q(r1, r2)
    ok = f"{num(r1)} ≤ x ≤ {num(r2)}"
    b.add(f"{quad(-a, -bb, -c)} ≥ 0 অসমতার সমাধান কোনটি?", ok, setw(ok, [f"x ≤ {num(r1)} অথবা x ≥ {num(r2)}", f"{num(r1)} < x < {num(r2)}", f"{num(-r2)} ≤ x ≤ {num(-r1)}", f"x ≥ {num(r2)}"]), f"−1 দিয়ে গুণ করে {quad(a, bb, c)} ≤ 0।", M)
def h_always(b):
    a = R.randint(1, 4); c = R.randint(1, 9)
    v = 4 * a * c; r = math.isqrt(v)
    if r * r != v: return
    ok = f"−{r} < k < {r}"
    b.add(f"সকল বাস্তব x-এর জন্য {a if a > 1 else ''}x² + kx + {c} > 0 হওয়ার শর্ত কোনটি?", ok, setw(ok, [f"k > {r}", f"|k| > {r}", f"−{v} < k < {v}", f"k < {r}"]), f"নিশ্চায়ক < 0 ⇒ k² < {v}।", H)
def h_abs_between(b):
    k1, k2 = sorted(R.sample(range(1, 9), 2))
    ok = f"{num(-k2)} < x < {num(-k1)} অথবা {k1} < x < {k2}"
    b.add(f"{k1} < |x| < {k2} অসমতার সমাধান কোনটি?", ok, setw(ok, [f"{k1} < x < {k2}", f"{num(-k2)} < x < {k2}", f"x < {num(-k2)} অথবা x > {k2}", f"{num(-k1)} < x < {k1}"]), "উভয় দিকে ব্যবধি।", H)
def h_abs_count(b):
    k1, k2 = sorted(R.sample(range(1, 9), 2))
    n = 2 * (k2 - k1 - 1)
    if n <= 0: return
    b.add(f"{k1} < |x| < {k2} অসমতার কয়টি পূর্ণসাংখ্যিক সমাধান আছে?", n, setw(n, [n // 2, n + 2, n - 1, k2 - k1]), f"ধনাত্মক দিকে {k2 - k1 - 1}টি, ঋণাত্মক দিকেও {k2 - k1 - 1}টি।", H)
def h_quad_frac(b):
    r1, r2 = sorted(R.sample(range(-5, 7), 2))
    ok = f"x < {num(r1)} অথবা x ≥ {num(r2)}"
    b.add(f"(x − ({num(r2)}))/(x − ({num(r1)})) ≥ 0 অসমতার সমাধান কোনটি?".replace('(x − (0))', 'x').replace('− (−', '+ (').replace('(x + (', '(x + ').replace('))/', ')/').replace('))', ')'), ok, setw(ok, [f"x ≤ {num(r1)} অথবা x ≥ {num(r2)}", f"{num(r1)} < x ≤ {num(r2)}", f"x < {num(r1)} অথবা x > {num(r2)}", f"{num(r1)} ≤ x < {num(r2)}"]), f"x = {num(r1)}-এ হর শূন্য, তাই বাদ; x = {num(r2)}-এ মান 0, তাই গ্রহণযোগ্য।", H)
p62 = run('6.2', R, fx62, [e_abs, e_abs_gt, e_quad, e_quad_gt], [m_abs_lin, m_count_abs, m_quad_le, m_sq, m_neg_lead], [h_always, h_abs_between, h_abs_count, h_quad_frac])

# ---------------- 6.3 দুই চলকের রৈখিক অসমতা ----------------
fx63 = [
 ("ax + by + c > 0 অসমতার লেখচিত্রে ax + by + c = 0 রেখাটি কেমন করে আঁকা হয়?", "ভাঙা (ড্যাশ) রেখায়", ["পুরু অবিচ্ছিন্ন রেখায়", "আঁকা হয় না", "বৃত্ত আকারে"], "সমান চিহ্ন না থাকায় রেখাটি সমাধানের অংশ নয়।", E),
 ("ax + by + c ≥ 0 অসমতার লেখচিত্রে সীমারেখাটি কেমন?", "অবিচ্ছিন্ন রেখা", ["ভাঙা রেখা", "অদৃশ্য", "বক্ররেখা"], "রেখার বিন্দুগুলোও সমাধান।", E),
 ("দুই চলকের রৈখিক অসমতার সমাধান অঞ্চল কোথায় হয়?", "সীমারেখার যেকোনো এক পাশের অর্ধতল", ["শুধু রেখার উপর", "একটি বিন্দু", "একটি বৃত্তের ভিতরে"], "রেখা তলকে দুটি অর্ধতলে ভাগ করে।", E),
 ("সীমারেখা মূলবিন্দু দিয়ে না গেলে কোন অঞ্চল সমাধান তা কীভাবে যাচাই করা সহজ?", "(0, 0) বসিয়ে", ["(1, 1) বসিয়ে", "রেখার ঢাল দেখে", "x = y ধরে"], "মূলবিন্দু অসমতা সিদ্ধ করলে মূলবিন্দুর পাশ সমাধান।", M),
 ("x ≥ 0 ও y ≥ 0 শর্ত দুটি একত্রে কোন অঞ্চল নির্দেশ করে?", "প্রথম চতুর্ভাগ (অক্ষসহ)", ["দ্বিতীয় চতুর্ভাগ", "তৃতীয় চতুর্ভাগ", "চতুর্থ চতুর্ভাগ"], "উভয় স্থানাঙ্ক অঋণাত্মক।", E),
]
def lin2(a, bb, c):
    return pfmt({k: v for k, v in {(1, 0): a, (0, 1): bb, (0, 0): c}.items() if v}, ('x', 'y'))
def e_point(b):
    a, bb, c = R.choice([v for v in range(-5, 6) if v]), R.choice([v for v in range(-5, 6) if v]), R.randint(-10, 10)
    op = R.choice(['>', '<', '≥', '≤'])
    pts = [(x, y) for x in range(-3, 5) for y in range(-3, 5)]
    good = [p for p in pts if eval(f"{a * p[0] + bb * p[1] + c} {op.replace('≥', '>=').replace('≤', '<=')} 0")]
    bad = [p for p in pts if p not in good]
    if not good or len(bad) < 3: return
    g = R.choice(good); ws = R.sample(bad, 3)
    b.add(f"কোন বিন্দুটি {lin2(a, bb, c)} {op} 0 অসমতাকে সিদ্ধ করে?", pair(*g), [pair(*w) for w in ws], f"({num(g[0])}, {num(g[1])}) বসালে {num(a * g[0] + bb * g[1] + c)} {op} 0।", E)
def e_origin(b):
    a, bb, c = R.choice([v for v in range(-5, 6) if v]), R.choice([v for v in range(-5, 6) if v]), R.choice([v for v in range(-10, 11) if v])
    op = R.choice(['>', '<'])
    sat = (c > 0) if op == '>' else (c < 0)
    ok = 'মূলবিন্দু যে পাশে আছে সেই পাশ' if sat else 'মূলবিন্দুর বিপরীত পাশ'
    b.add(f"{lin2(a, bb, c)} {op} 0 অসমতার সমাধান অঞ্চল কোনটি?", ok, ['মূলবিন্দু যে পাশে আছে সেই পাশ', 'মূলবিন্দুর বিপরীত পাশ', 'শুধু সীমারেখার উপর', 'সম্পূর্ণ তল'], f"(0, 0) বসালে {num(c)} {op} 0, যা {'সত্য' if sat else 'মিথ্যা'}।", E)
def e_intercept(b):
    a, bb = R.choice([v for v in range(-6, 7) if v]), R.choice([v for v in range(-6, 7) if v]); k = R.randint(1, 6)
    c = -a * bb * k
    # x-অক্ষ ছেদ: x = −c/a = bb·k
    xi = F(-c, a)
    b.add(f"{lin2(a, bb, c)} ≥ 0 অসমতার সীমারেখা x-অক্ষকে কোন বিন্দুতে ছেদ করে?", pair(xi, 0), setw(pair(xi, 0), [pair(0, xi), pair(F(-c, bb), 0), pair(-xi, 0), pair(0, F(-c, bb))]), f"y = 0 বসিয়ে x = {num(xi)}।", E)
def m_corner(b):
    a, bb = R.randint(1, 5), R.randint(1, 5); k = a * bb * R.randint(1, 4)
    ok = f"(0, 0), ({k // a}, 0), (0, {k // bb})"
    b.add(f"x ≥ 0, y ≥ 0 এবং {lin2(a, bb, 0)} ≤ {k} দ্বারা গঠিত অঞ্চলের শীর্ষবিন্দুগুলো কোনটি?", ok, setw(ok, [f"(0, 0), ({k // bb}, 0), (0, {k // a})", f"(0, 0), ({k}, 0), (0, {k})", f"({k // a}, 0), (0, {k // bb}), ({k // a}, {k // bb})", f"(0, 0), ({k // a}, {k // bb})"]), "অক্ষ দুটির সাথে রেখার ছেদবিন্দু ও মূলবিন্দু।", M)
def m_area(b):
    a, bb = R.randint(1, 5), R.randint(1, 5); k = a * bb * R.randint(1, 4)
    A = F(k // a * (k // bb), 2)
    b.add(f"x ≥ 0, y ≥ 0 এবং {lin2(a, bb, 0)} ≤ {k} দ্বারা আবদ্ধ অঞ্চলের ক্ষেত্রফল কত বর্গ একক?", fr(A), setw(fr(A), [str(k // a * (k // bb)), fr(A + 1), str(k), fr(A / 2)]), f"ত্রিভুজের ভূমি {k // a}, উচ্চতা {k // bb}।", M)
def m_maxobj(b):
    a, bb = R.randint(1, 4), R.randint(1, 4); k = a * bb * R.randint(1, 3); p, q = R.randint(1, 6), R.randint(1, 6)
    vals = {(0, 0): 0, (k // a, 0): p * (k // a), (0, k // bb): q * (k // bb)}
    best = max(vals.values())
    b.add(f"x ≥ 0, y ≥ 0, {lin2(a, bb, 0)} ≤ {k} শর্তে Z = {lin2(p, q, 0)}-এর সর্বোচ্চ মান কত?", best, setw(best, [min(v for v in vals.values() if v), best + p, p * q, k]), f"শীর্ষবিন্দুগুলোতে Z = {', '.join(str(v) for v in vals.values())}।", M)
def m_ineq_from_word(b):
    p, q = R.randint(5, 50), R.randint(5, 50); budget = R.randint(200, 1000)
    ok = f"{p}x + {q}y ≤ {budget}"
    b.add(f"প্রতিটি খাতার দাম {p} টাকা ও কলমের দাম {q} টাকা। {budget} টাকার মধ্যে x টি খাতা ও y টি কলম কেনার শর্ত কোনটি?", ok, setw(ok, [f"{p}x + {q}y ≥ {budget}", f"{q}x + {p}y ≤ {budget}", f"x + y ≤ {budget}", f"{p}x − {q}y ≤ {budget}"]), "মোট ব্যয় বাজেটের সমান বা কম।", M)
def m_side(b):
    a, bb = R.choice([v for v in range(-5, 6) if v]), R.choice([v for v in range(-5, 6) if v]); c = R.randint(-8, 8)
    px, py = R.randint(-4, 4), R.randint(-4, 4); v = a * px + bb * py + c
    if v == 0: return
    ok = f"{lin2(a, bb, c)} {'>' if v > 0 else '<'} 0"
    b.add(f"({num(px)}, {num(py)}) বিন্দুটি নিচের কোন অসমতার সমাধান অঞ্চলে আছে?", ok, setw(ok, [f"{lin2(a, bb, c)} {'<' if v > 0 else '>'} 0", f"{lin2(a, bb, c)} = 0", f"{lin2(-a, -bb, -c)} {'>' if v > 0 else '<'} 0"]), f"বিন্দুটি বসালে মান {num(v)}।", M)
def h_lp(b):
    # x + y ≤ s, x ≤ m, y ≤ n, x, y ≥ 0; Z = px + qy সর্বোচ্চ
    s = R.randint(6, 15); m_, n = R.randint(2, s - 1), R.randint(2, s - 1)
    if m_ + n <= s: return
    p, q = R.randint(1, 8), R.randint(1, 8)
    corners = [(0, 0), (m_, 0), (m_, s - m_), (s - n, n), (0, n)]
    best = max(p * x + q * y for x, y in corners); arg = max(corners, key=lambda c: p * c[0] + q * c[1])
    b.add(f"x + y ≤ {s}, 0 ≤ x ≤ {m_}, 0 ≤ y ≤ {n} শর্তে Z = {lin2(p, q, 0)}-এর সর্বোচ্চ মান কত?", best, setw(best, [p * m_ + q * n, p * s, q * s, best - 1]), f"শীর্ষবিন্দু ({arg[0]}, {arg[1]})-এ সর্বোচ্চ।", H)
def h_count_pts(b):
    a, bb = R.randint(1, 3), R.randint(1, 3); k = R.randint(3, 8)
    n = sum(1 for x in range(0, k + 1) for y in range(0, k + 1) if a * x + bb * y <= k)
    b.add(f"x ≥ 0, y ≥ 0, {lin2(a, bb, 0)} ≤ {k} শর্ত পূরণকারী পূর্ণসাংখ্যিক স্থানাঙ্কবিশিষ্ট বিন্দু কয়টি?", n, setw(n, [n - 1, n + 1, (k + 1) ** 2, n + k]), "প্রতিটি x-এর জন্য সম্ভাব্য y গুনে যোগ করে।", H)
def h_region(b):
    a = R.randint(1, 6); c = R.randint(1, 6)
    # |x| ≤ a, |y| ≤ c আয়তক্ষেত্র ক্ষেত্রফল
    b.add(f"|x| ≤ {a} এবং |y| ≤ {c} দ্বারা নির্দেশিত অঞ্চলের ক্ষেত্রফল কত বর্গ একক?", 4 * a * c, setw(4 * a * c, [a * c, 2 * a * c, (2 * a + 1) * (2 * c + 1), 4 * (a + c)]), f"আয়তক্ষেত্রের দৈর্ঘ্য {2 * a}, প্রস্থ {2 * c}।", H)
def h_diamond(b):
    k = R.randint(1, 8)
    b.add(f"|x| + |y| ≤ {k} দ্বারা আবদ্ধ অঞ্চলের ক্ষেত্রফল কত বর্গ একক?", 2 * k * k, setw(2 * k * k, [k * k, 4 * k * k, 4 * k, 2 * k]), f"বর্গের কর্ণ {2 * k}; ক্ষেত্রফল = ({2 * k})²/2 = {2 * k * k}।", H)
p63 = run('6.3', R, fx63, [e_point, e_origin, e_intercept], [m_corner, m_area, m_maxobj, m_ineq_from_word, m_side], [h_lp, h_count_pts, h_region, h_diamond])
save('h6', p61 + p62 + p63)

# ---------------- 7 অসীম ধারা ----------------
fx7 = [
 ("অসীম গুণোত্তর ধারা a + ar + ar² + … -এর যোগফল নির্ণয়যোগ্য হওয়ার শর্ত কোনটি?", "|r| < 1", ["|r| > 1", "r = 1", "r > 0"], "|r| < 1 হলে যোগফল a/(1 − r)।", E),
 ("|r| < 1 হলে অসীম গুণোত্তর ধারার যোগফল কত?", "a/(1 − r)", ["a/(r − 1)", "a(1 − rⁿ)/(1 − r)", "ar/(1 − r)"], "সূত্র S∞ = a/(1 − r)।", E),
 ("একটি অনুক্রমের পদগুলোকে '+' চিহ্ন দিয়ে যুক্ত করলে কী পাওয়া যায়?", "ধারা", ["ফাংশন", "সেট", "সমীকরণ"], "অনুক্রমের পদের সমষ্টি ধারা।", E),
 ("1, 1/2, 1/3, 1/4, … অনুক্রমের n-তম পদ কোনটি?", "1/n", ["n", "1/(n + 1)", "1/2ⁿ"], "n-তম পদ 1/n।", E),
 ("n → ∞ হলে 1/n-এর সীমা কত?", "0", ["1", "∞", "অনির্ণেয়"], "n বাড়লে 1/n শূন্যের কাছে যায়।", E),
 ("1 + 2 + 3 + … (অসীম পর্যন্ত) ধারাটি কেমন?", "অভিসারী নয় (অপসারী)", ["অভিসারী", "যোগফল 0", "যোগফল 1"], "আংশিক সমষ্টি অসীমে যায়।", M),
 ("1 − 1 + 1 − 1 + … ধারাটির যোগফল সম্পর্কে কোনটি সত্য?", "নির্দিষ্ট যোগফল নেই", ["যোগফল 0", "যোগফল 1", "যোগফল 1/2"], "আংশিক সমষ্টি 1 ও 0-এর মধ্যে দোলে।", M),
]
def e_sinf(b):
    a = R.randint(1, 12); p, q = R.choice([(1, 2), (1, 3), (2, 3), (1, 4), (3, 4), (1, 5), (2, 5)]); s = R.choice([1, -1])
    r = F(s * p, q); S_ = F(a) / (1 - r)
    rs = fr(r) if r > 0 else '−' + fr(-r)
    b.add(f"প্রথম পদ {a} ও সাধারণ অনুপাত {rs} বিশিষ্ট অসীম গুণোত্তর ধারার যোগফল কত?", fr(S_), setw(fr(S_), [fr(F(a) / (1 + r)), fr(a * r / (1 - r)) if a * r / (1 - r) > 0 else fr(S_ + 1), fr(S_ + 1), str(a * 2)]), f"S∞ = {a}/(1 − ({rs})) = {fr(S_)}।", E)
def e_ratio(b):
    a = R.randint(1, 20); p, q = R.choice([(1, 2), (1, 3), (2, 3), (1, 4), (3, 4)])
    t2 = F(a * p, q)
    b.add(f"অসীম ধারা {a} + {fr(t2)} + {fr(t2 * F(p, q))} + … -এর সাধারণ অনুপাত কত?", fr(F(p, q)), setw(fr(F(p, q)), [fr(F(q, p)), fr(t2), fr(F(p, q) + F(1, 2)), fr(1 - F(p, q)) if 1 - F(p, q) != F(p, q) else '1']), f"r = {fr(t2)}/{a} = {fr(F(p, q))}।", E)
def e_conv(b):
    r = R.choice([F(1, 2), F(3, 2), F(-1, 3), F(2), F(-2), F(1, 5), F(5, 4), F(-3, 4), F(4, 3), F(-1)])
    ok = 'অভিসারী' if abs(r) < 1 else 'অপসারী'
    rs = fr(r) if r > 0 else '−' + fr(-r)
    b.add(f"সাধারণ অনুপাত {rs} বিশিষ্ট অসীম গুণোত্তর ধারাটি কেমন?", ok, ['অভিসারী', 'অপসারী', 'যোগফল 0', 'যোগফল 1'], f"|r| {'<' if abs(r) < 1 else '≥'} 1।", E)
def e_term(b):
    p, q = R.randint(1, 4), R.randint(1, 5); n = R.randint(2, 9)
    t = F(n, p * n + q)
    b.add(f"কোনো অনুক্রমের n-তম পদ n/({p if p > 1 else ''}n + {q}) হলে {n}-তম পদ কত?", fr(t), setw(fr(t), [fr(F(n + 1, p * (n + 1) + q)), fr(F(n - 1, p * (n - 1) + q)) if n > 1 else '1', fr(F(1, p)), fr(t + F(1, 10))]), f"{n}/({p * n + q}) = {fr(t)}।", E)
def m_rec(b):
    a = R.randint(1, 9); d = R.randint(0, 9)
    if a == d: return
    # 0.a d̅ ধরণ: 0.ad্ddd... = (10a + d − a)/90
    v = F(10 * a + d - a, 90)
    b.add(f"0.{a}{d}{d}{d}… (শুধু {d} পুনরাবৃত্ত) আবৃত দশমিককে সাধারণ ভগ্নাংশে প্রকাশ করলে কত?", fr(v), setw(fr(v), [fr(F(10 * a + d, 99)), fr(F(10 * a + d, 90)), fr(F(10 * a + d, 100)), fr(F(a, 9))]), f"({a}{d} − {a})/90 = {fr(v)}।", M)
def m_rec2(b):
    n = R.randint(1, 98)
    if n % 11 == 0: return
    v = F(n, 99); s = f"{n:02d}"
    b.add(f"0.{s}{s}{s}… (অঙ্ক {s} পুনরাবৃত্ত) সাধারণ ভগ্নাংশে কত?", fr(v), setw(fr(v), [fr(F(n, 100)), fr(F(n, 90)), fr(F(n, 999)), fr(F(n + 1, 99))]), f"{s}/99 = {fr(v)}।", M)
def m_find_a(b):
    S_ = R.randint(2, 30); p, q = R.choice([(1, 2), (1, 3), (2, 3), (1, 4), (3, 4), (1, 5)])
    a = S_ * (1 - F(p, q))
    b.add(f"সাধারণ অনুপাত {fr(F(p, q))} বিশিষ্ট একটি অসীম গুণোত্তর ধারার যোগফল {S_} হলে প্রথম পদ কত?", fr(a), setw(fr(a), [fr(S_ * F(p, q)), fr(S_ / (1 - F(p, q))), fr(a + 1), str(S_)]), f"a = S(1 − r) = {S_} × {fr(1 - F(p, q))} = {fr(a)}।", M)
def m_find_r(b):
    a = R.randint(1, 12); p, q = R.choice([(1, 2), (1, 3), (2, 3), (1, 4), (3, 4), (2, 5), (3, 5)])
    r = F(p, q); S_ = F(a) / (1 - r)
    b.add(f"একটি অসীম গুণোত্তর ধারার প্রথম পদ {a} এবং যোগফল {fr(S_)} হলে সাধারণ অনুপাত কত?", fr(r), setw(fr(r), [fr(1 - r) if 1 - r != r else fr(r + F(1, 5)), fr(F(a) / S_), fr(F(q, p)), fr(r / 2)]), f"1 − r = {a}/{fr(S_)} ⇒ r = {fr(r)}।", M)
def m_limit(b):
    p, q, c, d = R.randint(1, 6), R.randint(-5, 5), R.randint(1, 6), R.randint(-5, 5)
    v = F(p, c)
    b.add(f"n → ∞ হলে ({p if p > 1 else ''}n {'+' if q >= 0 else '−'} {abs(q)})/({c if c > 1 else ''}n {'+' if d >= 0 else '−'} {abs(d)})-এর সীমা কত?".replace('n + 0)', 'n)').replace('n − 0)', 'n)'), fr(v), setw(fr(v), [fr(F(q, d)) if d else '0', fr(F(c, p)), '0', '∞', fr(v + 1)]), f"লব ও হরকে n দিয়ে ভাগ করে {p}/{c}।", M)
def m_partial(b):
    a = R.randint(1, 10); n = R.randint(3, 8)
    s = F(a) * (1 - F(1, 2 ** n)) / F(1, 2)
    b.add(f"{a} + {fr(F(a, 2))} + {fr(F(a, 4))} + … ধারার প্রথম {n}টি পদের যোগফল কত?", fr(s), setw(fr(s), [str(2 * a), fr(s + F(a, 2 ** n)), fr(s - F(a, 2 ** (n - 1))), fr(F(a) * (1 - F(1, 2 ** (n + 1))) * 2)]), f"Sₙ = a(1 − rⁿ)/(1 − r) = {fr(s)}।", M)
def h_tele(b):
    n = R.randint(5, 50)
    v = F(n, n + 1)
    b.add(f"1/(1·2) + 1/(2·3) + … + 1/({n}·{n + 1}) = কত?", fr(v), setw(fr(v), [fr(F(1, n + 1)), fr(F(n - 1, n)), '1', fr(F(n + 1, n + 2))]), f"1/k − 1/(k + 1) আকারে ভেঙে 1 − 1/{n + 1} = {fr(v)}।", H)
def h_tele_inf(b):
    k = R.randint(1, 4)
    # Σ 1/(n(n + k)) from n=1 to ∞ = (1/k)(1 + 1/2 + … + 1/k)
    v = F(1, k) * sum(F(1, i) for i in range(1, k + 1))
    b.add(f"অসীম ধারা Σ 1/(n(n + {k})) (n = 1 থেকে ∞) -এর যোগফল কত?", fr(v), setw(fr(v), ['1', fr(F(1, k)), fr(v * 2), fr(v + F(1, 4))]), f"1/(n(n + {k})) = (1/{k})(1/n − 1/(n + {k})); যোগফল = {fr(v)}।", H)
def h_condx(b):
    a = R.randint(1, 5)
    ok = f"{num(-a - 1)} < x < {num(-a + 1)}"
    b.add(f"1 + (x + {a}) + (x + {a})² + … অসীম ধারাটির যোগফল থাকার শর্ত কোনটি?", ok, setw(ok, [f"{num(a - 1)} < x < {num(a + 1)}", f"−1 < x < 1", f"x < {num(-a)}", f"{num(-a - 1)} ≤ x ≤ {num(-a + 1)}"]), f"|x + {a}| < 1।", H)
def h_sumx(b):
    p, q = R.choice([(1, 2), (1, 3), (1, 4), (2, 3), (1, 5)])
    # 1 + x + x² + … = q/(q−p) ⇒ x = p/q
    S_ = F(q, q - p)
    b.add(f"1 + x + x² + x³ + … = {fr(S_)} হলে x = কত?", fr(F(p, q)), setw(fr(F(p, q)), [fr(F(q, p)), fr(1 - F(p, q)) if 1 - F(p, q) != F(p, q) else fr(F(p, q) + F(1, 6)), fr(S_ - 1 + F(1, 7)), fr(F(1, S_)) if F(1, S_) != F(p, q) else '1/7']), f"1/(1 − x) = {fr(S_)} ⇒ x = {fr(F(p, q))}।", H)
def h_ball(b):
    h = R.choice([4, 6, 8, 10, 12, 16, 20, 24, 30]); p, q = R.choice([(1, 2), (2, 3), (3, 4), (1, 3), (3, 5)])
    r = F(p, q); D = h + 2 * h * r / (1 - r)
    b.add(f"একটি বল {h} মিটার উঁচু থেকে ফেলা হলো; প্রতিবার আগের উচ্চতার {fr(r)} অংশ লাফিয়ে ওঠে। থামার আগে বলটি মোট কত মিটার পথ অতিক্রম করবে?", fr(D), setw(fr(D), [fr(h / (1 - r)), fr(h + h * r / (1 - r)), fr(2 * h / (1 - r)), fr(D + h)]), f"{h} + 2 × {h}·{fr(r)}/(1 − {fr(r)}) = {fr(D)}।", H)
p7 = run(None, R, fx7, [e_sinf, e_ratio, e_conv, e_term], [m_rec, m_rec2, m_find_a, m_find_r, m_limit, m_partial], [h_tele, h_tele_inf, h_condx, h_sumx, h_ball])
save('h7', p7)
