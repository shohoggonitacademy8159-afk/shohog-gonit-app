#!/usr/bin/env python3
"""অধ্যায় 12 দুই চলকবিশিষ্ট সরল সহসমীকরণ:
12.1 সমঞ্জসতা ও পরস্পর নির্ভরতা · 12.2 প্রতিস্থাপন/অপনয়ন/আড়গুণন পদ্ধতিতে সমাধান · 12.3 লেখচিত্রের সাহায্যে সমাধান · 12.4 বাস্তব সমস্যা"""
import random, pathlib, sys, math
from fractions import Fraction as F
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from mcqlib import run, save, E, M, H, fr, near, num, pfmt, lin

R = random.Random(2026103112)
XY = ('x', 'y')
def eq(a, b_, c):
    """ax + by = c"""
    return f"{pfmt(lin([a, b_]), XY)} = {num(c)}"
def P(x, y): return f"({num(x)}, {num(y)})"
def nz(lo=-6, hi=6): return R.choice([v for v in range(lo, hi + 1) if v])
fx121 = [
 ("যে সহসমীকরণ জোটের সমাধান আছে, তাকে কী বলে?", "সমঞ্জস", ["অসমঞ্জস", "অনির্ভরশীল নয়", "অসংজ্ঞায়িত"], "সমাধান থাকলে সমঞ্জস।", E),
 ("যে সহসমীকরণ জোটের কোনো সমাধান নেই, তাকে কী বলে?", "অসমঞ্জস", ["সমঞ্জস", "পরস্পর নির্ভরশীল", "অনন্য সমাধানযোগ্য"], "সমাধান না থাকলে অসমঞ্জস।", E),
 ("a₁x + b₁y = c₁ ও a₂x + b₂y = c₂ সমঞ্জস ও পরস্পর অনির্ভরশীল হওয়ার শর্ত কী?", "a₁/a₂ ≠ b₁/b₂", ["a₁/a₂ = b₁/b₂ ≠ c₁/c₂", "a₁/a₂ = b₁/b₂ = c₁/c₂", "c₁ = c₂"], "একটিমাত্র সমাধান।", E),
 ("a₁/a₂ = b₁/b₂ ≠ c₁/c₂ হলে সমীকরণ জোট কেমন?", "অসমঞ্জস", ["সমঞ্জস ও অনির্ভরশীল", "পরস্পর নির্ভরশীল", "একটি সমাধান আছে"], "রেখা দুটি সমান্তরাল।", E),
 ("a₁/a₂ = b₁/b₂ = c₁/c₂ হলে সমীকরণ জোটের কয়টি সমাধান?", "অসংখ্য", ["একটি", "কোনোটি না", "দুটি"], "রেখা দুটি সমপাতিত।", E),
 ("দুটি সরলরেখা পরস্পর সমান্তরাল হলে সংশ্লিষ্ট সমীকরণ জোট কেমন?", "অসমঞ্জস", ["সমঞ্জস", "নির্ভরশীল", "অনন্য সমাধানযোগ্য"], "ছেদবিন্দু নেই।", M),
 ("দুটি সরলরেখা একটি বিন্দুতে ছেদ করলে সমীকরণ জোটের সমাধান কয়টি?", "একটি", ["দুটি", "অসংখ্য", "কোনোটি না"], "ছেদবিন্দুই সমাধান।", M),
]
def kind(a1, b1, c1, a2, b2, c2):
    if a1 * b2 != a2 * b1: return 'অনন্য'
    if a1 * c2 == a2 * c1 and b1 * c2 == b2 * c1: return 'নির্ভর'
    return 'অসমঞ্জস'
LBL = {'অনন্য': 'সমঞ্জস ও পরস্পর অনির্ভরশীল', 'নির্ভর': 'সমঞ্জস ও পরস্পর নির্ভরশীল', 'অসমঞ্জস': 'অসমঞ্জস'}
def gen_pair(k):
    a1, b1, c1 = nz(), nz(), nz(-12, 12)
    if k == 'অনন্য':
        a2, b2, c2 = nz(), nz(), nz(-12, 12)
    else:
        m = R.choice([2, 3, -2, 4, -1])
        a2, b2 = a1 * m, b1 * m
        c2 = c1 * m if k == 'নির্ভর' else c1 * m + R.choice([1, 2, -3, 5])
    return a1, b1, c1, a2, b2, c2
def e_kind(b):
    k = R.choice(list(LBL)); t = gen_pair(k)
    if kind(*t) != k: return
    b.add(f"{eq(*t[:3])} এবং {eq(*t[3:])} সমীকরণ জোটটি কেমন?", LBL[k], [v for v in LBL.values() if v != LBL[k]] + ['সমাধান দুটি'], f"a₁/a₂, b₁/b₂, c₁/c₂ তুলনা করে।", E)
def m_count(b):
    k = R.choice(list(LBL)); t = gen_pair(k)
    if kind(*t) != k: return
    ans = {'অনন্য': 'একটি', 'নির্ভর': 'অসংখ্য', 'অসমঞ্জস': 'কোনো সমাধান নেই'}[k]
    b.add(f"{eq(*t[:3])} এবং {eq(*t[3:])} সমীকরণ জোটের কয়টি সমাধান আছে?", ans, [v for v in ['একটি', 'অসংখ্য', 'কোনো সমাধান নেই', 'দুটি'] if v != ans], "অনুপাত তুলনা করে।", M)
def m_k_par(b):
    a1, b1 = nz(), nz(); m = R.choice([2, 3, -2, 4]); c1 = nz(-10, 10)
    k = b1 * m
    b.add(f"{eq(a1, b1, c1)} এবং {a1 * m}x + ky = {num(c1 * m + R.choice([1, 2, 3]))} সমীকরণ জোট অসমঞ্জস হলে k = কত?", num(k), [num(-k), num(k + 1), num(b1)] if b1 != k and -k != k else [num(k + 2), num(k + 1), num(k - 1)], f"a₁/a₂ = b₁/b₂ ⇒ k = {num(k)}।", M)
def m_slope(b):
    k = R.choice(list(LBL)); t = gen_pair(k)
    if kind(*t) != k: return
    ans = {'অনন্য': 'একটি বিন্দুতে ছেদ করে', 'নির্ভর': 'সমপাতিত (একই রেখা)', 'অসমঞ্জস': 'সমান্তরাল'}[k]
    b.add(f"{eq(*t[:3])} এবং {eq(*t[3:])} সমীকরণদ্বয়ের লেখচিত্র কেমন হবে?", ans, [v for v in ['একটি বিন্দুতে ছেদ করে', 'সমপাতিত (একই রেখা)', 'সমান্তরাল', 'দুটি বিন্দুতে ছেদ করে'] if v != ans], "সহগের অনুপাত তুলনা।", M)
def h_k_dep(b):
    a1, b1, c1 = nz(), nz(), nz(-10, 10); m = R.choice([2, 3, -2, 4, 5])
    k = c1 * m
    b.add(f"{eq(a1, b1, c1)} এবং {pfmt(lin([a1 * m, b1 * m]), XY)} = k সমীকরণ জোট পরস্পর নির্ভরশীল হলে k = কত?", num(k), [num(c1), num(k + m), num(-k)] if c1 != k else [num(k + m), num(-k), num(k + 1)], f"c₁/c₂ = a₁/a₂ ⇒ k = {num(k)}।", H)
def h_k_unique(b):
    a1, b1 = nz(), nz(); m = R.choice([2, 3, -2, 4])
    k = b1 * m
    b.add(f"{eq(a1, b1, 5)} এবং {a1 * m}x + ky = 7 সমীকরণ জোটের একটি মাত্র সমাধান থাকলে k এর মান কোনটি হতে পারে না?", num(k), [num(k + 1), num(k - 1), num(k + 2)], f"k = {num(k)} হলে a₁/a₂ = b₁/b₂ হয়।", H)
I121 = run('12.1', R, fx121, [e_kind], [m_count, m_k_par, m_slope], [h_k_dep, h_k_unique], caps=(30, 20, 12))

fx122 = [
 ("সহসমীকরণ সমাধানের প্রতিস্থাপন পদ্ধতিতে প্রথমে কী করা হয়?", "একটি সমীকরণ থেকে একটি চলকের মান অপর চলকের মাধ্যমে বের করা", ["দুই সমীকরণ যোগ করা", "লেখচিত্র আঁকা", "দুই সমীকরণ গুণ করা"], "তারপর অপর সমীকরণে বসানো।", E),
 ("অপনয়ন পদ্ধতিতে কী করা হয়?", "একটি চলকের সহগ সমান করে চলকটি অপসারণ করা", ["উভয় চলক অপসারণ", "সমীকরণ বর্গ করা", "লেখচিত্র আঁকা"], "যোগ বা বিয়োগ করে।", E),
 ("a₁x + b₁y + c₁ = 0, a₂x + b₂y + c₂ = 0 হলে আড়গুণন সূত্রে x/(b₁c₂ − b₂c₁) = ? ", "y/(c₁a₂ − c₂a₁) = 1/(a₁b₂ − a₂b₁)", ["y/(a₁b₂ − a₂b₁) = 1/(c₁a₂ − c₂a₁)", "y/(b₁c₂ − b₂c₁)", "1/(a₁ + b₁)"], "আড়গুণন সূত্র।", M),
]
def sol(x, y):
    a1, b1, a2, b2 = nz(-5, 5), nz(-5, 5), nz(-5, 5), nz(-5, 5)
    if a1 * b2 == a2 * b1: return None
    return (a1, b1, a1 * x + b1 * y), (a2, b2, a2 * x + b2 * y)
def e_simple(b):
    x, y = R.randint(-5, 9), R.randint(-5, 9)
    b.add(f"x + y = {num(x + y)} এবং x − y = {num(x - y)} হলে (x, y) = কত?", P(x, y), [P(y, x) if x != y else P(x + 1, y), P(x + 1, y - 1), P(-x, y) if x else P(x, -y if y else 2)], f"যোগ করে 2x = {num(2 * x)} ⇒ x = {num(x)}, y = {num(y)}।", E)
def e_sub(b):
    x, y = R.randint(-5, 9), R.randint(-5, 9); k = R.randint(2, 5)
    b.add(f"y = {k}x এবং x + y = {num(x + k * x)} হলে x = কত?", num(x), [num(w) for w in near(x)], f"x + {k}x = {num((k + 1) * x)} ⇒ x = {num(x)}।", E) if x else None
def e_check(b):
    x, y = R.randint(-4, 6), R.randint(-4, 6)
    s = sol(x, y)
    if not s: return
    (a1, b1, c1), (a2, b2, c2) = s
    b.add(f"নিচের কোনটি {eq(a1, b1, c1)} ও {eq(a2, b2, c2)} সহসমীকরণের সমাধান?", P(x, y), [P(y, x) if x != y else P(x + 2, y), P(x + 1, y), P(x, y + 1)], "দুটি সমীকরণেই বসিয়ে যাচাই।", E)
def m_solve(b):
    x, y = R.randint(-6, 8), R.randint(-6, 8)
    s = sol(x, y)
    if not s: return
    (a1, b1, c1), (a2, b2, c2) = s
    b.add(f"{eq(a1, b1, c1)} এবং {eq(a2, b2, c2)} হলে (x, y) = কত?", P(x, y), [P(y, x) if x != y else P(x - 1, y), P(-x, -y) if (x, y) != (0, 0) else P(1, 1), P(x + 1, y - 1)], f"অপনয়ন পদ্ধতিতে x = {num(x)}, y = {num(y)}।", M)
def m_xonly(b):
    x, y = R.randint(-6, 8), R.randint(-6, 8)
    s = sol(x, y)
    if not s: return
    (a1, b1, c1), (a2, b2, c2) = s
    want = R.choice('xy'); v = x if want == 'x' else y
    b.add(f"{eq(a1, b1, c1)} এবং {eq(a2, b2, c2)} হলে {want} = কত?", num(v), [num(w) for w in near(v)], f"সমাধান x = {num(x)}, y = {num(y)}।", M)
def m_sum(b):
    x, y = R.randint(-5, 8), R.randint(-5, 8)
    s = sol(x, y)
    if not s: return
    (a1, b1, c1), (a2, b2, c2) = s
    b.add(f"{eq(a1, b1, c1)} এবং {eq(a2, b2, c2)} হলে x + y = কত?", num(x + y), [num(x - y) if x - y != x + y else num(x + y + 2), num(x + y + 1), num(x * y) if x * y not in (x + y, x - y, x + y + 1) else num(x + y - 1)], f"x = {num(x)}, y = {num(y)}।", M)
def h_frac(b):
    x, y = R.choice([1, 2, 3, 4, 5, 6]), R.choice([1, 2, 3, 4, 5, 6])
    a1, b1, a2, b2 = R.randint(1, 4), R.randint(1, 4), R.randint(1, 4), R.randint(1, 4)
    if a1 * b2 == a2 * b1: return
    c1 = F(a1, x) + F(b1, y); c2 = F(a2, x) - F(b2, y)
    b.add(f"{a1}/x + {b1}/y = {fr(c1)} এবং {a2}/x − {b2}/y = {fr(c2)} হলে (x, y) = কত?", P(x, y), [P(y, x) if x != y else P(x + 1, y), P(fr(F(1, x)), fr(F(1, y))) if x * y != 1 else P(2, 2), P(x + 1, y + 1)], f"1/x = u, 1/y = v ধরে u = {fr(F(1, x))}, v = {fr(F(1, y))}।", H)
def h_frac2(b):
    x, y = R.randint(1, 9), R.randint(1, 9); p, q = R.choice([(2, 3), (3, 2), (2, 5), (4, 3), (3, 4)])
    s1 = F(x, p) + F(y, q); s2 = x - y
    b.add(f"x/{p} + y/{q} = {fr(s1)} এবং x − y = {num(s2)} হলে (x, y) = কত?", P(x, y), [P(y, x) if x != y else P(x + 1, y + 1), P(x + 1, y + 1) if x != y else P(x + 2, y + 2), P(x * 2, y * 2)], f"প্রথম সমীকরণকে {p * q // math.gcd(p, q)} দিয়ে গুণ করে সমাধান।", H)
def h_param(b):
    x, y = R.randint(1, 6), R.randint(1, 6); a_ = R.randint(2, 5)
    # ax + by = c with unknown a? 'x = .., y = .. সমাধান হলে k'
    k = R.randint(2, 6); c = k * x + a_ * y
    b.add(f"(x, y) = {P(x, y)} সমীকরণ kx + {a_}y = {c} এর সমাধান হলে k = কত?", k, near(k), f"{x}k + {a_ * y} = {c} ⇒ k = {k}।", H)
I122 = run('12.2', R, fx122, [e_simple, e_sub, e_check], [m_solve, m_xonly, m_sum], [h_frac, h_frac2, h_param], caps=(10, 17, 7))

fx123 = [
 ("দুই চলকবিশিষ্ট সরল সমীকরণের লেখচিত্র কেমন?", "সরলরেখা", ["বৃত্ত", "পরাবৃত্ত", "বক্ররেখা"], "একঘাত সমীকরণ।", E),
 ("লেখচিত্রে দুটি সরলরেখার ছেদবিন্দু কী নির্দেশ করে?", "সহসমীকরণের সমাধান", ["কোনো সমাধান নেই", "x-অক্ষ", "মূলবিন্দু"], "উভয় রেখায় থাকা বিন্দু।", E),
 ("x-অক্ষের সমীকরণ কোনটি?", "y = 0", ["x = 0", "y = x", "x + y = 0"], "x-অক্ষের সব বিন্দুতে y = 0।", E),
 ("y-অক্ষের সমীকরণ কোনটি?", "x = 0", ["y = 0", "y = x", "x = y = 0"], "y-অক্ষের সব বিন্দুতে x = 0।", E),
 ("মূলবিন্দুর স্থানাঙ্ক কত?", "(0, 0)", ["(1, 1)", "(0, 1)", "(1, 0)"], "দুই অক্ষের ছেদবিন্দু।", E),
 ("y = mx সরলরেখা কোন বিন্দু দিয়ে যায়?", "মূলবিন্দু (0, 0)", ["(1, 0)", "(0, 1)", "(m, 0)"], "x = 0 হলে y = 0।", M),
 ("x = a সরলরেখা কোন অক্ষের সমান্তরাল?", "y-অক্ষ", ["x-অক্ষ", "y = x রেখা", "কোনোটির নয়"], "x স্থির থাকে।", M),
]
def e_onl(b):
    a1, b1 = nz(-4, 4), nz(-4, 4); x, y = R.randint(-4, 5), R.randint(-4, 5); c = a1 * x + b1 * y
    w = []
    for dx, dy in [(1, 0), (0, 1), (1, 1), (-1, 0), (2, 1), (0, -2)]:
        if a1 * (x + dx) + b1 * (y + dy) != c: w.append(P(x + dx, y + dy))
    b.add(f"নিচের কোন বিন্দুটি {eq(a1, b1, c)} রেখার উপর অবস্থিত?", P(x, y), w[:3], f"বসালে {a1}×{num(x)} + {b1}×{num(y)} = {num(c)}।", E)
def e_xint(b):
    a1, b1 = nz(-5, 5), nz(-5, 5); x0 = R.randint(-6, 6)
    c = a1 * x0
    b.add(f"{eq(a1, b1, c)} রেখাটি x-অক্ষকে কোন বিন্দুতে ছেদ করে?", P(x0, 0), [P(0, x0) if x0 else P(1, 0), P(fr(F(c, b1)), 0) if F(c, b1) != x0 else P(x0 + 1, 0), P(x0, 1)], f"y = 0 বসিয়ে x = {num(x0)}।", E)
def m_yint(b):
    a1, b1 = nz(-5, 5), nz(-5, 5); y0 = R.randint(-6, 6)
    c = b1 * y0
    b.add(f"{eq(a1, b1, c)} রেখাটি y-অক্ষকে কোন বিন্দুতে ছেদ করে?", P(0, y0), [P(y0, 0) if y0 else P(0, 1), P(0, fr(F(c, a1))) if F(c, a1) != y0 else P(0, y0 + 1), P(1, y0)], f"x = 0 বসিয়ে y = {num(y0)}।", M)
def m_meet(b):
    x, y = R.randint(-5, 6), R.randint(-5, 6)
    s = sol(x, y)
    if not s: return
    (a1, b1, c1), (a2, b2, c2) = s
    b.add(f"{eq(a1, b1, c1)} ও {eq(a2, b2, c2)} রেখাদ্বয়ের লেখচিত্রের ছেদবিন্দু কোনটি?", P(x, y), [P(y, x) if x != y else P(x, y + 2), P(x + 1, y), P(-x, y) if x else P(x, y - 1)], f"সমাধান করে ({num(x)}, {num(y)})।", M)
def m_axis_meet(b):
    a_ = nz(-8, 8); k = nz(-8, 8)
    if R.random() < .5:
        b.add(f"x = {num(a_)} এবং y = {num(k)} রেখাদ্বয় কোন বিন্দুতে ছেদ করে?", P(a_, k), [P(k, a_) if a_ != k else P(a_, -k), P(a_, 0), P(0, k)], "x ও y এর মান সরাসরি।", M)
    else:
        b.add(f"y = {pfmt(lin([a_], 0), ('x',))} এবং x = {num(k)} রেখাদ্বয় কোন বিন্দুতে ছেদ করে?", P(k, a_ * k), [P(a_ * k, k) if a_ * k != k else P(k, 0), P(k, a_), P(0, a_ * k) if k else P(1, a_)], f"x = {num(k)} বসিয়ে y = {num(a_ * k)}।", M)
def m_quad(b):
    x, y = nz(-6, 6), nz(-6, 6)
    q = {(True, True): 'প্রথম', (False, True): 'দ্বিতীয়', (False, False): 'তৃতীয়', (True, False): 'চতুর্থ'}[(x > 0, y > 0)]
    b.add(f"{P(x, y)} বিন্দুটি কোন চতুর্ভাগে অবস্থিত?", f"{q} চতুর্ভাগ", [f"{v} চতুর্ভাগ" for v in ['প্রথম', 'দ্বিতীয়', 'তৃতীয়', 'চতুর্থ'] if v != q], "x ও y এর চিহ্ন দেখে।", M)
def h_area(b):
    a_, b_ = R.randint(1, 8), R.randint(1, 8)
    c = a_ * b_ * R.choice([1, 2])
    xi, yi = F(c, a_), F(c, b_)
    A = xi * yi / 2
    b.add(f"{eq(a_, b_, c)} রেখা ও দুই অক্ষ দ্বারা গঠিত ত্রিভুজের ক্ষেত্রফল কত বর্গএকক?", fr(A), [fr(A * 2), fr(xi + yi), fr(A + 1)], f"ছেদক অংশ x = {fr(xi)}, y = {fr(yi)}; ক্ষেত্রফল ½ × {fr(xi)} × {fr(yi)} = {fr(A)}।", H)
def h_par(b):
    a_, b_ = nz(-5, 5), nz(-5, 5); c1, c2 = R.sample(range(-9, 10), 2)
    b.add(f"{eq(a_, b_, c1)} ও {eq(a_, b_, c2)} রেখাদ্বয়ের লেখচিত্র সম্পর্কে কোনটি সত্য?", "পরস্পর সমান্তরাল, ছেদবিন্দু নেই", ["একটি বিন্দুতে ছেদ করে", "সমপাতিত", "পরস্পর লম্ব"], "সহগ এক কিন্তু ধ্রুবক ভিন্ন।", H)
def h_tri(b):
    x, y = R.randint(1, 6), R.randint(1, 6)
    # x + y = s রেখা, x অক্ষ ও y অক্ষ... ছেদবিন্দু ও মূলবিন্দু
    s = x + y
    b.add(f"x = {x}, y = {y} ও x + y = {s + R.randint(1, 4)} … " if False else f"x + y = {s} ও x − y = {num(x - y)} রেখাদ্বয়ের ছেদবিন্দু থেকে x-অক্ষের দূরত্ব কত একক?", y, [x if x != y else y + 1, s, abs(x - y) if abs(x - y) not in (x, y, s) else y + 2], f"ছেদবিন্দু ({x}, {y}); x-অক্ষ থেকে দূরত্ব |y| = {y}।", H)
I123 = run('12.3', R, fx123, [e_onl, e_xint], [m_yint, m_meet, m_axis_meet, m_quad], [h_area, h_par, h_tri], caps=(15, 13, 8))

fx124 = [
 ("দুটি সংখ্যার যোগফল s ও অন্তর d হলে বড় সংখ্যাটি কত?", "(s + d)/2", ["(s − d)/2", "s + d", "sd/2"], "x + y = s, x − y = d যোগ করে।", E),
 ("দুই অঙ্কের সংখ্যার দশকের অঙ্ক x ও এককের অঙ্ক y হলে সংখ্যাটি কত?", "10x + y", ["x + y", "10y + x", "xy"], "স্থানীয় মান।", E),
]
def e_sumdiff(b):
    x, y = R.randint(10, 60), R.randint(1, 40)
    if x <= y: return
    b.add(f"দুটি সংখ্যার যোগফল {x + y} এবং অন্তর {x - y}। বড় সংখ্যাটি কত?", x, [y, x + 1, (x + y) // 2 if (x + y) // 2 not in (x, y) else x - 1], f"({x + y} + {x - y})/2 = {x}।", E)
def e_small(b):
    x, y = R.randint(10, 60), R.randint(1, 40)
    if x <= y: return
    b.add(f"দুটি সংখ্যার যোগফল {x + y} এবং অন্তর {x - y}। ছোট সংখ্যাটি কত?", y, [x, y + 1, y - 1], f"({x + y} − {x - y})/2 = {y}।", E)
def e_pens(b):
    p, q = R.randint(5, 20), R.randint(10, 40); m, n = R.randint(1, 4), R.randint(1, 4)
    b.add(f"1টি কলম ও 1টি খাতার মোট দাম {p + q} টাকা। কলমের দাম খাতার চেয়ে {abs(q - p)} টাকা {'কম' if p < q else 'বেশি'} হলে কলমের দাম কত?", p, [q, p + 1, (p + q) // 2 if (p + q) // 2 not in (p, q) else p + 2], f"x + y = {p + q}, y − x = {q - p} ⇒ x = {p}।", E) if p != q else None
def m_digit(b):
    t, u = R.randint(1, 9), R.randint(0, 9)
    if t == u or u == 0: return
    n = 10 * t + u; r = 10 * u + t
    b.add(f"দুই অঙ্কের একটি সংখ্যার অঙ্কদ্বয়ের যোগফল {t + u}। অঙ্কদ্বয় স্থান বিনিময় করলে নতুন সংখ্যাটি মূল সংখ্যা থেকে {abs(r - n)} {'বেশি' if r > n else 'কম'} হয়। মূল সংখ্যাটি কত?", n, [r, n + 9, n - 9 if n - 9 != r else n + 18], f"10x + y ও 10y + x সমীকরণ থেকে {n}।", M)
def m_frac(b):
    p, q = R.randint(1, 9), R.randint(2, 12)
    if p >= q or math.gcd(p, q) != 1: return
    a_, c_ = R.randint(1, 4), R.randint(1, 4)
    f1 = F(p + a_, q + a_); f2 = F(p - c_, q - c_) if p - c_ > 0 else None
    if f2 is None or f2 <= 0: return
    b.add(f"একটি ভগ্নাংশের লব ও হরের সাথে {a_} যোগ করলে {fr(f1)} হয়, আর লব ও হর থেকে {c_} বিয়োগ করলে {fr(f2)} হয়। ভগ্নাংশটি কত?", f"{p}/{q}", [f"{q}/{p}", f"{p}/{q + 1}", f"{p + 1}/{q + 2}"], "দুটি সমীকরণ গঠন করে সমাধান।", M)
def m_age(b):
    f, s = R.randint(30, 50), R.randint(5, 15); t = R.randint(3, 10)
    b.add(f"পিতা ও পুত্রের বর্তমান বয়সের সমষ্টি {f + s} বছর। {t} বছর আগে পিতার বয়স পুত্রের বয়সের {fr(F(f - t, s - t))} গুণ ছিল। পুত্রের বর্তমান বয়স কত?", s, [f, s + t, s - 1], f"x + y = {f + s} এবং (x − {t}) = {fr(F(f - t, s - t))}(y − {t}) ⇒ পুত্র {s} বছর।", M) if s > t and F(f - t, s - t).denominator == 1 else None
def m_rect(b):
    l, w = R.randint(6, 30), R.randint(3, 20)
    if l <= w: return
    b.add(f"একটি আয়তক্ষেত্রের পরিসীমা {2 * (l + w)} মি এবং দৈর্ঘ্য প্রস্থ অপেক্ষা {l - w} মি বেশি। দৈর্ঘ্য কত মি?", l, [w, l + 1, l + w], f"2(x + y) = {2 * (l + w)}, x − y = {l - w} ⇒ x = {l}।", M)
def m_ticket(b):
    a_, c_ = R.choice([(50, 30), (100, 60), (40, 20), (80, 50)]); n1, n2 = R.randint(5, 30), R.randint(5, 30)
    b.add(f"একটি অনুষ্ঠানে বড়দের টিকিট {a_} টাকা ও ছোটদের {c_} টাকা। মোট {n1 + n2}টি টিকিট বিক্রি করে {a_ * n1 + c_ * n2} টাকা পাওয়া গেল। বড়দের টিকিট কয়টি?", n1, [n2 if n1 != n2 else n1 + 2, n1 + 1, n1 - 1], f"x + y = {n1 + n2}, {a_}x + {c_}y = {a_ * n1 + c_ * n2} ⇒ x = {n1}।", M)
def h_boat(b):
    v, s = R.randint(6, 15), R.randint(1, 5); t1, t2 = R.randint(2, 5), R.randint(2, 6)
    d1, d2 = (v + s) * t1, (v - s) * t2
    b.add(f"একটি নৌকা স্রোতের অনুকূলে {t1} ঘণ্টায় {d1} কিমি এবং প্রতিকূলে {t2} ঘণ্টায় {d2} কিমি যায়। স্থির পানিতে নৌকার বেগ কত কিমি/ঘণ্টা?", v, [s, v + s, v - s], f"x + y = {v + s}, x − y = {v - s} ⇒ x = {v}।", H)
def h_work(b):
    a_, b_ = R.choice([(10, 15), (12, 24), (20, 30), (6, 12), (15, 10), (18, 36)])
    t = F(a_ * b_, a_ + b_)
    b.add(f"ক ও খ একসাথে একটি কাজ {fr(t)} দিনে করে। ক একা {a_} দিনে করলে খ একা কত দিনে করবে?", b_, [a_, b_ + 2, a_ + b_], f"1/x = 1/{fr(t)} − 1/{a_} ⇒ x = {b_}।", H)
def h_mix(b):
    p1, p2 = R.choice([(60, 80), (40, 50), (100, 150), (30, 45)]); n1, n2 = R.randint(2, 10), R.randint(2, 10)
    tot = p1 * n1 + p2 * n2
    b.add(f"প্রতি কেজি {p1} টাকা ও {p2} টাকা দামের দুই ধরনের চাল মিশিয়ে {n1 + n2} কেজি মিশ্রণ তৈরি হলো, যার মোট দাম {tot} টাকা। {p2} টাকা দামের চাল কত কেজি?", n2, [n1 if n1 != n2 else n2 + 1, n2 + 1, n2 - 1] if n2 > 1 else [n1, n2 + 1, n2 + 2], f"x + y = {n1 + n2}, {p1}x + {p2}y = {tot} ⇒ y = {n2}।", H)
def h_coins(b):
    n5, n2 = R.randint(3, 20), R.randint(3, 20)
    b.add(f"কারো কাছে 5 টাকা ও 2 টাকার মোট {n5 + n2}টি মুদ্রা আছে, যার মূল্য {5 * n5 + 2 * n2} টাকা। 5 টাকার মুদ্রা কয়টি?", n5, [n2 if n2 != n5 else n5 + 2, n5 + 1, n5 - 1], f"x + y = {n5 + n2}, 5x + 2y = {5 * n5 + 2 * n2} ⇒ x = {n5}।", H)
I124 = run('12.4', R, fx124, [e_sumdiff, e_small, e_pens], [m_digit, m_frac, m_age, m_rect, m_ticket], [h_boat, h_work, h_mix, h_coins], caps=(10, 10, 6))
save(12, I121 + I122 + I123 + I124)
