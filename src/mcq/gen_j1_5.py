#!/usr/bin/env python3
"""দ্বাদশ শ্রেণি উচ্চতর গণিত ২য় পত্র (h12)। প্রতি অনুশীলনী 200 (অধ্যায় 2 ও 4: 300), হার 30/50/20।
1.A বাস্তব সংখ্যা ও পরমমান · 1.B অসমতা · 2 যোগাশ্রয়ী প্রোগ্রাম · 3.A জটিল সংখ্যার মৌলিক ধারণা · 3.B পোলার রূপ, এককের ঘনমূল ও বর্গমূল
4 বহুপদী ও বহুপদী সমীকরণ · 5.A ধনাত্মক পূর্ণসাংখ্যিক সূচকের দ্বিপদী · 5.B যেকোনো মূলদ সূচকের দ্বিপদী
6.A পরাবৃত্ত · 6.B উপবৃত্ত · 6.C অধিবৃত্ত · 7.A বিপরীত ত্রিকোণমিতিক ফাংশন · 7.B ত্রিকোণমিতিক সমীকরণ
8.A বলের লব্ধি · 8.B সমবিন্দু বলের ভারসাম্য (লামি) · 8.C সমান্তরাল বল ও মোমেন্ট
9.A সরলরৈখিক গতি · 9.B উল্লম্ব গতি ও পড়ন্ত বস্তু · 9.C প্রক্ষেপক · 9.D গতির অন্যান্য সমস্যা (আপেক্ষিক বেগ, নদী পারাপার)
10.A বিস্তার পরিমাপ · 10.B সম্ভাবনা"""
import random, pathlib, sys, math
from fractions import Fraction as F
from itertools import combinations
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from mcqlib import run, save, E, M, H, fr, near, num, pfmt, surd, sup

R = random.Random(2026110201)
def W(c, pool):
    out = []
    for w in pool:
        w = str(w)
        if w != str(c) and w not in out: out.append(w)
    return out
def nz(a, b): return R.choice([v for v in range(a, b + 1) if v])
X = ('x',)
def px(d): return pfmt({(k,): v for k, v in d.items() if v}, X) if any(d.values()) else '0'
def co(c, s):
    c = F(c)
    if c == 1: return s
    if c == -1: return '−' + s
    return num(c) + s
def sqf(v):
    r = math.isqrt(v); return str(r) if r * r == v else surd(v)
def piF(v):
    v = F(v)
    if v == 0: return '0'
    sg = '−' if v < 0 else ''; v = abs(v)
    if v == 1: return sg + 'π'
    if v.denominator == 1: return f"{sg}{v.numerator}π"
    return f"{sg}{v.numerator if v.numerator != 1 else ''}π/{v.denominator}"
def iv(lo, hi, lc=False, hc=False):
    return ('[' if lc else '(') + (num(lo) if lo is not None else '−∞') + ', ' + (num(hi) if hi is not None else '∞') + (']' if hc else ')')
G = 10   # অভিকর্ষজ ত্বরণ (সহজ হিসাবের জন্য কিছু প্রশ্নে 9.8)

# ================= 1.A বাস্তব সংখ্যা ও পরমমান =================
fx1a = [
 ("|a| = কত, যদি a < 0 হয়?", "−a", ["a", "0", "a²"], "পরমমানের সংজ্ঞা।", E),
 ("|ab| = কত?", "|a||b|", ["|a| + |b|", "ab", "|a| − |b|"], "", E),
 ("ত্রিভুজ অসমতা অনুযায়ী |a + b| ≤ কত?", "|a| + |b|", ["|a| − |b|", "|a||b|", "a + b"], "", E),
 ("√2 কোন ধরনের সংখ্যা?", "অমূলদ", ["মূলদ", "পূর্ণসংখ্যা", "জটিল"], "", E),
 ("দুটি মূলদ সংখ্যার মাঝে কতগুলো মূলদ সংখ্যা আছে?", "অসংখ্য", ["একটি", "দুটি", "নেই"], "ঘনত্ব ধর্ম।", E),
 ("|x| < a (a > 0) হলে কোনটি সত্য?", "−a < x < a", ["x < −a", "x > a", "x < a মাত্র"], "", E),
 ("|x − a| < δ-এর জ্যামিতিক অর্থ কী?", "x, a থেকে δ-এর কম দূরত্বে", ["x, a-এর সমান", "x > a + δ", "x < a − δ"], "", M),
 ("√(x²) = কত?", "|x|", ["x", "−x", "x²"], "", M),
 ("কোনটি পূর্ণ সংখ্যা (integer) নয়?", "1/2", ["0", "−5", "7"], "", E),
 ("বাস্তব সংখ্যার সেট কোন প্রক্রিয়ায় আবদ্ধ নয়?", "শূন্য দিয়ে ভাগ", ["যোগ", "গুণ", "বিয়োগ"], "", M),
]
def e_abs(b):
    a, c = R.randint(-30, 30), R.randint(-30, 30)
    v = abs(a) - abs(c) if R.random() < .5 else abs(a - c)
    q = f"|{num(a)}| − |{num(c)}|" if v == abs(a) - abs(c) else f"|{num(a)} − ({num(c)})|"
    b.add(f"{q} = কত?", num(v), W(num(v), [num(a - c), num(abs(a) + abs(c)), num(-v) if v else '1', num(v + 2)]), "পরমমানের সংজ্ঞা।", E)
def e_eq(b):
    a, k = R.randint(-15, 15), R.randint(1, 20)
    ok = f"{{{num(a - k)}, {num(a + k)}}}"
    b.add(f"|x {'−' if a >= 0 else '+'} {abs(a)}| = {k} সমীকরণের সমাধান সেট কোনটি?".replace('|x − 0|', '|x|'), ok, W(ok, [f"{{{num(-a - k)}, {num(-a + k)}}}", f"{{{num(a + k)}}}", f"{{{num(a - k)}, {num(a + k + 1)}}}"]), "x − a = ±k।", E)
def e_lin(b):
    p, q, k = R.randint(2, 7), R.randint(-12, 12), R.randint(1, 20)
    x1, x2 = F(k - q, p), F(-k - q, p)
    ok = f"{{{num(min(x1, x2))}, {num(max(x1, x2))}}}"
    b.add(f"|{px({1: p, 0: q})}| = {k} হলে x-এর মানসমূহ কোনটি?", ok, W(ok, [f"{{{num(F(k + q, p))}, {num(F(-k + q, p))}}}", f"{{{num(max(x1, x2))}}}", f"{{{num(k - q)}, {num(-k - q)}}}"]), f"{px({1: p, 0: q})} = ±{k}।", E)
def m_lt(b):
    p, q, k = R.randint(1, 6), R.randint(-12, 12), R.randint(1, 20)
    lo, hi = F(-k - q, p), F(k - q, p)
    ok = f"{num(lo)} < x < {num(hi)}"
    b.add(f"|{px({1: p, 0: q})}| < {k} অসমতার সমাধান কোনটি?", ok, W(ok, [f"x < {num(lo)} অথবা x > {num(hi)}", f"{num(lo)} ≤ x ≤ {num(hi)}", f"{num(F(-k + q, p))} < x < {num(F(k + q, p))}"]), f"−{k} < {px({1: p, 0: q})} < {k}।", M)
def m_gt(b):
    p, q, k = R.randint(1, 6), R.randint(-12, 12), R.randint(1, 20)
    lo, hi = F(-k - q, p), F(k - q, p)
    ok = f"x ≤ {num(lo)} অথবা x ≥ {num(hi)}"
    b.add(f"|{px({1: p, 0: q})}| ≥ {k} অসমতার সমাধান কোনটি?", ok, W(ok, [f"{num(lo)} ≤ x ≤ {num(hi)}", f"x < {num(lo)} অথবা x > {num(hi)}", f"x ≥ {num(hi)}"]), "পরমমানের বাইরে।", M)
def m_interval(b):
    lo, hi = sorted(R.sample(range(-20, 21), 2))
    c, r = F(lo + hi, 2), F(hi - lo, 2)
    ok = f"|x {'−' if c >= 0 else '+'} {num(abs(c))}| < {num(r)}".replace('|x − 0|', '|x|')
    b.add(f"{num(lo)} < x < {num(hi)}-কে পরমমানের মাধ্যমে প্রকাশ করলে কোনটি?", ok, W(ok, [f"|x {'+' if c >= 0 else '−'} {num(abs(c))}| < {num(r)}".replace('|x + 0|', '|x|'), f"|x {'−' if c >= 0 else '+'} {num(abs(c))}| > {num(r)}".replace('|x − 0|', '|x|'), f"|x| < {hi}"]), f"মধ্যবিন্দু {num(c)}, অর্ধ-দৈর্ঘ্য {num(r)}।", M)
def m_count(b):
    a, k = R.randint(-10, 10), R.randint(1, 15)
    n = 2 * k + 1
    b.add(f"|x {'−' if a >= 0 else '+'} {abs(a)}| ≤ {k} অসমতার কয়টি পূর্ণসাংখ্যিক সমাধান আছে?".replace('|x − 0|', '|x|'), n, W(n, [2 * k, 2 * k - 1, k, n + 2]), f"{num(a - k)} ≤ x ≤ {num(a + k)}।", M)
def m_dist(b):
    a, c = R.sample(range(-25, 26), 2)
    b.add(f"সংখ্যারেখায় {num(a)} ও {num(c)}-এর দূরত্ব কত?", abs(a - c), W(abs(a - c), [abs(a + c), abs(a) + abs(c), abs(a - c) + 1, max(abs(a), abs(c))]), "|a − b|।", M)
def h_two(b):
    a, c = sorted(R.sample(range(-10, 11), 2))
    # |x − a| + |x − c| এর ন্যূনতম মান = c − a
    b.add(f"|x {'−' if a >= 0 else '+'} {abs(a)}| + |x {'−' if c >= 0 else '+'} {abs(c)}|-এর ক্ষুদ্রতম মান কত?".replace('|x − 0|', '|x|').replace('|x + 0|', '|x|'), c - a, W(c - a, [abs(a) + abs(c), 0, c + a if c + a > 0 else c - a + 1, c - a + 2]), f"{num(a)} ≤ x ≤ {num(c)} হলে মান {c - a}।", H)
def h_eq2(b):
    a, c = R.randint(1, 9), R.randint(1, 9)
    # |x − a| = |x + c| ⇒ x = (a − c)/2
    v = F(a - c, 2)
    b.add(f"|x − {a}| = |x + {c}| হলে x = কত?", num(v), W(num(v), [num(F(a + c, 2)), num(-v) if v else '1', num(a - c), num(v + 1)]), "বর্গ করে সমাধান।", H)
def h_frac(b):
    k = R.randint(1, 9)
    ok = f"x < −{k} অথবা x > {k}"
    b.add(f"1/|x| < 1/{k} (x ≠ 0) অসমতার সমাধান কোনটি?", ok, W(ok, [f"−{k} < x < {k}", f"x > {k}", f"0 < x < {k}"]), f"|x| > {k}।", H)
def h_sq(b):
    a, k = R.randint(-8, 8), R.randint(1, 10)
    n = 2 * k - 1
    b.add(f"(x {'−' if a >= 0 else '+'} {abs(a)})² < {k * k} অসমতার পূর্ণসাংখ্যিক সমাধান কয়টি?".replace('(x − 0)', 'x'), n, W(n, [2 * k + 1, 2 * k, k, n - 2 if n > 2 else n + 4]), f"|x − ({num(a)})| < {k}।", H)
p1a = run('1.A', R, fx1a, [e_abs, e_eq, e_lin], [m_lt, m_gt, m_interval, m_count, m_dist], [h_two, h_eq2, h_frac, h_sq], caps=(40, 40, 20), mult=2)

# ================= 1.B অসমতা =================
fx1b = [
 ("a > b ও c < 0 হলে কোনটি সত্য?", "ac < bc", ["ac > bc", "ac = bc", "a + c < b"], "ঋণাত্মক দিয়ে গুণে চিহ্ন উল্টে যায়।", E),
 ("a, b ধনাত্মক হলে কোনটি সত্য (AM-GM)?", "(a + b)/2 ≥ √(ab)", ["(a + b)/2 ≤ √(ab)", "a + b ≤ 2ab", "ab ≥ a + b"], "", M),
 ("x² + 1 > 0 অসমতার সমাধান সেট কোনটি?", "R", ["∅", "(0, ∞)", "(−1, 1)"], "", E),
 ("x² < 0 অসমতার সমাধান সেট কোনটি?", "∅", ["R", "{0}", "(−∞, 0)"], "", E),
 ("0 < a < b হলে 1/a ও 1/b-এর সম্পর্ক কোনটি?", "1/a > 1/b", ["1/a < 1/b", "1/a = 1/b", "নির্ণয় সম্ভব নয়"], "", M),
]
def e_lin(b):
    a = R.choice([2, 3, 4, 5, 6, -2, -3, -4]); x = R.randint(-10, 12); c = R.randint(-15, 15); op = R.choice(['<', '>', '≤', '≥'])
    rhs = a * x + c; fl = {'<': '>', '>': '<', '≤': '≥', '≥': '≤'}
    res = op if a > 0 else fl[op]
    ok = f"x {res} {num(x)}"
    b.add(f"{px({1: a, 0: c})} {op} {num(rhs)} অসমতার সমাধান কোনটি?", ok, W(ok, [f"x {fl[res]} {num(x)}", f"x {res} {num(-x)}" if x else f"x {res} 1", f"x {res} {num(rhs)}"]), f"{num(a)}x {op} {num(rhs - c)}।", E)
def e_quad(b):
    r1, r2 = sorted(R.sample(range(-12, 13), 2)); s, p = r1 + r2, r1 * r2
    op = R.choice(['<', '>'])
    ok = f"{num(r1)} < x < {num(r2)}" if op == '<' else f"x < {num(r1)} অথবা x > {num(r2)}"
    alt = f"x < {num(r1)} অথবা x > {num(r2)}" if op == '<' else f"{num(r1)} < x < {num(r2)}"
    b.add(f"{px({2: 1, 1: -s, 0: p})} {op} 0 অসমতার সমাধান কোনটি?", ok, W(ok, [alt, f"{num(-r2)} < x < {num(-r1)}", f"x > {num(r2)}"]), f"(x − ({num(r1)}))(x − ({num(r2)})) {op} 0।", E)
def e_interval(b):
    lo, hi = sorted(R.sample(range(-15, 16), 2)); lc, hc = R.choice([True, False]), R.choice([True, False])
    ok = iv(lo, hi, lc, hc)
    b.add(f"{num(lo)} {'≤' if lc else '<'} x {'≤' if hc else '<'} {num(hi)}-কে ব্যবধিতে লিখলে কোনটি?", ok, W(ok, [iv(lo, hi, not lc, hc), iv(lo, hi, lc, not hc), iv(lo, hi, not lc, not hc)]), "", E)
def m_frac(b):
    a, c = R.sample(range(-9, 10), 2)
    lo, hi = sorted([a, -c])
    # (x − a)/(x + c) < 0
    ok = f"{num(lo)} < x < {num(hi)}"
    b.add(f"(x {'−' if a >= 0 else '+'} {abs(a)})/(x {'+' if c >= 0 else '−'} {abs(c)}) < 0 অসমতার সমাধান কোনটি?".replace('(x − 0)', 'x').replace('(x + 0)', 'x'), ok, W(ok, [f"x < {num(lo)} অথবা x > {num(hi)}", f"{num(lo)} ≤ x ≤ {num(hi)}", f"{num(-hi)} < x < {num(-lo)}"]), "লব ও হর বিপরীত চিহ্নের।", M)
def m_double(b):
    a = R.choice([2, 3, 4, 5]); c = R.randint(-8, 8); lo, hi = sorted(R.sample(range(-10, 12), 2))
    ok = f"{num(lo)} ≤ x ≤ {num(hi)}"
    b.add(f"{num(a * lo + c)} ≤ {px({1: a, 0: c})} ≤ {num(a * hi + c)} অসমতার সমাধান কোনটি?", ok, W(ok, [f"{num(lo)} < x < {num(hi)}", f"{num(a * lo + c)} ≤ x ≤ {num(a * hi + c)}", f"{num(lo + 1)} ≤ x ≤ {num(hi + 1)}"]), "", M)
def m_qcount(b):
    r1, r2 = sorted(R.sample(range(-10, 11), 2)); s, p = r1 + r2, r1 * r2
    n = r2 - r1 + 1
    b.add(f"{px({2: 1, 1: -s, 0: p})} ≤ 0 অসমতার কয়টি পূর্ণসাংখ্যিক সমাধান আছে?", n, W(n, [n - 1, n + 1, r2 - r1 - 1 if r2 - r1 - 1 not in (n - 1,) else n + 2, n + 3]), "", M)
def m_neg(b):
    r1, r2 = sorted(R.sample(range(-10, 11), 2)); s, p = r1 + r2, r1 * r2
    ok = f"{num(r1)} ≤ x ≤ {num(r2)}"
    b.add(f"{px({2: -1, 1: s, 0: -p})} ≥ 0 অসমতার সমাধান কোনটি?", ok, W(ok, [f"x ≤ {num(r1)} অথবা x ≥ {num(r2)}", f"{num(r1)} < x < {num(r2)}", f"{num(-r2)} ≤ x ≤ {num(-r1)}"]), "−1 দিয়ে গুণ করে।", M)
def h_always(b):
    a, c = R.randint(1, 5), R.randint(1, 20)
    v = 4 * a * c; r = math.isqrt(v)
    ok = f"−{r} < k < {r}" if r * r == v else f"−{surd(v)} < k < {surd(v)}"
    b.add(f"সকল বাস্তব x-এর জন্য {co(a, 'x²')} + kx + {c} > 0 হলে k-এর সীমা কোনটি?", ok, W(ok, [f"k > {r}" if r * r == v else "k > 0", f"|k| > {r}" if r * r == v else "k < 0", f"−{v} < k < {v}"]), "নিশ্চায়ক < 0।", H)
def h_amgm(b):
    k = R.randint(1, 30)
    b.add(f"x > 0 হলে x + {k * k}/x-এর ক্ষুদ্রতম মান কত?", 2 * k, W(2 * k, [k, k * k, 2 * k * k, k + 1]), f"AM ≥ GM: x + {k * k}/x ≥ 2√{k * k} = {2 * k}।", H)
def h_abs_ineq(b):
    k1, k2 = sorted(R.sample(range(1, 15), 2))
    n = 2 * (k2 - k1 - 1)
    if n <= 0: return
    b.add(f"{k1} < |x| < {k2} অসমতার পূর্ণসাংখ্যিক সমাধান কয়টি?", n, W(n, [n // 2, n + 2, k2 - k1, n - 1]), "দুই দিকে সমান সংখ্যক।", H)
p1b = run('1.B', R, fx1b, [e_lin, e_quad, e_interval], [m_frac, m_double, m_qcount, m_neg], [h_always, h_amgm, h_abs_ineq], caps=(40, 40, 30), mult=2)
save('j1', p1a + p1b)

# ================= 2 যোগাশ্রয়ী প্রোগ্রাম =================
fx2 = [
 ("যোগাশ্রয়ী প্রোগ্রামে যে অপেক্ষককে সর্বোচ্চ বা সর্বনিম্ন করা হয় তাকে কী বলে?", "উদ্দেশ্য ফাংশন", ["শর্ত", "সম্ভাব্য অঞ্চল", "চলক"], "", E),
 ("যোগাশ্রয়ী প্রোগ্রামের শর্তগুলো পূরণকারী সকল বিন্দুর সেটকে কী বলে?", "সম্ভাব্য (feasible) অঞ্চল", ["অসম্ভব অঞ্চল", "উদ্দেশ্য ফাংশন", "চূড়ান্ত বিন্দু"], "", E),
 ("যোগাশ্রয়ী প্রোগ্রামের সর্বোচ্চ বা সর্বনিম্ন মান সাধারণত কোথায় পাওয়া যায়?", "সম্ভাব্য অঞ্চলের কৌণিক বিন্দুতে", ["অঞ্চলের কেন্দ্রে", "মূলবিন্দুতে সবসময়", "অঞ্চলের বাইরে"], "", E),
 ("x ≥ 0, y ≥ 0 শর্ত দুটিকে কী বলে?", "অঋণাত্মক শর্ত", ["উদ্দেশ্য ফাংশন", "সমতা শর্ত", "অপ্রয়োজনীয় শর্ত"], "", E),
 ("যোগাশ্রয়ী প্রোগ্রামে উদ্দেশ্য ফাংশন ও শর্তগুলো কেমন হয়?", "রৈখিক", ["দ্বিঘাত", "সূচকীয়", "ত্রিকোণমিতিক"], "", E),
 ("সম্ভাব্য অঞ্চল সীমাহীন হলে সর্বোচ্চ মান সম্পর্কে কী বলা যায়?", "সর্বোচ্চ মান নাও থাকতে পারে", ["সবসময় 0", "সবসময় আছে", "মূলবিন্দুতে"], "", M),
 ("লেখচিত্র পদ্ধতিতে কয়টি চলকের যোগাশ্রয়ী প্রোগ্রাম সহজে সমাধান করা যায়?", "দুটি", ["একটি", "তিনটি", "যেকোনো সংখ্যক"], "", E),
]
def lin2(a, c, k=0):
    return pfmt({kk: v for kk, v in {(1, 0): a, (0, 1): c, (0, 0): k}.items() if v}, ('x', 'y'))
def poly_corners(cons):
    """cons: [(a, b, c)] মানে ax + by ≤ c, সাথে x, y ≥ 0। কৌণিক বিন্দু।"""
    lines = cons + [(-1, 0, 0), (0, -1, 0)]
    pts = set()
    for (a1, b1, c1), (a2, b2, c2) in combinations(lines, 2):
        d = a1 * b2 - a2 * b1
        if d == 0: continue
        x, y = F(c1 * b2 - c2 * b1, d), F(a1 * c2 - a2 * c1, d)
        if all(a * x + b * y <= c for a, b, c in lines): pts.add((x, y))
    return sorted(pts)
def rand_lp(k=2):
    while True:
        cons = []
        for _ in range(k):
            a, c = R.randint(1, 6), R.randint(1, 6); m = R.randint(2, 8)
            cons.append((a, c, a * c * m // math.gcd(a, c)))
        pts = poly_corners(cons)
        if len(pts) >= 3 and all(p[0].denominator == 1 and p[1].denominator == 1 for p in pts): return cons, pts
def cons_txt(cons): return ', '.join(f"{lin2(a, c)} ≤ {k}" for a, c, k in cons) + ', x ≥ 0, y ≥ 0'
def P(x, y): return f"({num(x)}, {num(y)})"
def e_point(b):
    cons, pts = rand_lp(1); a, c, k = cons[0]
    x, y = R.randint(0, k // a + 2), R.randint(0, k // c + 2); inside = a * x + c * y <= k
    ok = 'হ্যাঁ' if inside else 'না'
    b.add(f"{P(x, y)} বিন্দুটি কি {cons_txt(cons)} শর্তগুলো সিদ্ধ করে?", ok, ['হ্যাঁ', 'না', 'শুধু প্রথম শর্ত', 'শুধু x ≥ 0'], f"{a}·{x} + {c}·{y} = {a * x + c * y} {'≤' if inside else '>'} {k}।", E)
def e_corner(b):
    a, c = R.randint(1, 8), R.randint(1, 8); k = a * c * R.randint(1, 6)
    ok = f"(0, 0), ({k // a}, 0), (0, {k // c})"
    b.add(f"{lin2(a, c)} ≤ {k}, x ≥ 0, y ≥ 0 অঞ্চলের কৌণিক বিন্দুগুলো কোনটি?", ok, W(ok, [f"(0, 0), ({k // c}, 0), (0, {k // a})", f"(0, 0), ({k}, 0), (0, {k})", f"({k // a}, 0), (0, {k // c}), ({k // a}, {k // c})"]), "অক্ষের সাথে ছেদবিন্দু।", E)
def e_obj(b):
    p, q, x, y = R.randint(1, 15), R.randint(1, 15), R.randint(0, 12), R.randint(0, 12)
    v = p * x + q * y
    b.add(f"Z = {lin2(p, q)} হলে {P(x, y)} বিন্দুতে Z-এর মান কত?", v, W(v, [p * y + q * x, v + p, p + q, v - q]), "", E)
def e_form(b):
    p, q, m = R.randint(5, 60), R.randint(5, 60), R.randint(100, 1500)
    ok = f"{p}x + {q}y ≤ {m}"
    b.add(f"একটি পণ্যের দাম {p} টাকা ও অন্যটির {q} টাকা। হাতে {m} টাকা থাকলে x ও y সংখ্যক কেনার শর্ত কোনটি?", ok, W(ok, [f"{p}x + {q}y ≥ {m}", f"{q}x + {p}y ≤ {m}", f"x + y ≤ {m}"]), "", E)
def m_max1(b):
    a, c = R.randint(1, 6), R.randint(1, 6); k = a * c * R.randint(1, 6); p, q = R.randint(1, 12), R.randint(1, 12)
    vals = [0, p * (k // a), q * (k // c)]; best = max(vals)
    b.add(f"{lin2(a, c)} ≤ {k}, x ≥ 0, y ≥ 0 শর্তে Z = {lin2(p, q)}-এর সর্বোচ্চ মান কত?", best, W(best, [min(v for v in vals if v), best + p, p * q, k]), f"কৌণিক বিন্দুতে মান {', '.join(map(str, vals))}।", M)
def m_max2(b):
    cons, pts = rand_lp(2); p, q = R.randint(1, 10), R.randint(1, 10)
    vals = [p * x + q * y for x, y in pts]; best = max(vals); arg = pts[vals.index(best)]
    others = sorted(set(vals) - {best}, reverse=True)
    b.add(f"{cons_txt(cons)} শর্তে Z = {lin2(p, q)}-এর সর্বোচ্চ মান কত?", num(best), W(num(best), [num(v) for v in others[:3]] + [num(best + p), num(best + q)]), f"কৌণিক বিন্দু {', '.join(P(*t) for t in pts)}; সর্বোচ্চ {P(*arg)}-এ।", M)
def m_min(b):
    cons, pts = rand_lp(2); p, q = R.randint(1, 10), R.randint(1, 10)
    pts2 = [t for t in pts if t != (0, 0)]
    vals = [p * x + q * y for x, y in pts2]; best = min(vals)
    b.add(f"{cons_txt(cons)} শর্তে মূলবিন্দু বাদে অন্যান্য কৌণিক বিন্দুতে Z = {lin2(p, q)}-এর সর্বনিম্ন মান কত?", num(best), W(num(best), [num(v) for v in sorted(set(vals) - {best})[:3]] + [num(best + 1), num(best + p)]), "কৌণিক বিন্দুতে মান তুলনা।", M)
def m_cornercount(b):
    cons, pts = rand_lp(2)
    b.add(f"{cons_txt(cons)} দ্বারা নির্ধারিত সম্ভাব্য অঞ্চলের কৌণিক বিন্দু কয়টি?", len(pts), W(len(pts), [len(pts) + 1, len(pts) - 1, 3, 5, 6]), f"{', '.join(P(*t) for t in pts)}।", M)
def m_inter(b):
    a1, c1, a2, c2 = R.randint(1, 5), R.randint(1, 5), R.randint(1, 5), R.randint(1, 5)
    if a1 * c2 == a2 * c1: return
    x, y = R.randint(1, 10), R.randint(1, 10)
    k1, k2 = a1 * x + c1 * y, a2 * x + c2 * y
    b.add(f"{lin2(a1, c1)} = {k1} ও {lin2(a2, c2)} = {k2} রেখাদ্বয়ের ছেদবিন্দু কোনটি?", P(x, y), W(P(x, y), [P(y, x), P(x + 1, y), P(x, y - 1)]), "", M)
def h_word(b):
    # দুই পণ্য: শ্রম ও কাঁচামাল সীমা
    a1, c1, a2, c2 = R.randint(1, 4), R.randint(1, 4), R.randint(1, 4), R.randint(1, 4)
    if a1 * c2 == a2 * c1: return
    x0, y0 = R.randint(2, 12), R.randint(2, 12); L, Mt = a1 * x0 + c1 * y0, a2 * x0 + c2 * y0
    p, q = R.randint(10, 60), R.randint(10, 60)
    cons = [(a1, c1, L), (a2, c2, Mt)]; pts = poly_corners(cons)
    if not all(t[0].denominator == 1 and t[1].denominator == 1 for t in pts): return
    vals = [p * x + q * y for x, y in pts]; best = max(vals)
    b.add(f"একটি কারখানা A ও B পণ্য তৈরি করে। প্রতি একক A-তে {a1} ঘণ্টা শ্রম ও {a2} কেজি কাঁচামাল, B-তে {c1} ঘণ্টা শ্রম ও {c2} কেজি কাঁচামাল লাগে। মোট শ্রম {L} ঘণ্টা ও কাঁচামাল {Mt} কেজি। প্রতি একক A-তে {p} টাকা ও B-তে {q} টাকা লাভ হলে সর্বোচ্চ লাভ কত টাকা?", num(best), W(num(best), [num(v) for v in sorted(set(vals) - {best}, reverse=True)[:3]] + [num(best + p)]), f"কৌণিক বিন্দু {', '.join(P(*t) for t in pts)}।", H)
def h_diet(b):
    a1, c1, a2, c2 = R.randint(1, 5), R.randint(1, 5), R.randint(1, 5), R.randint(1, 5)
    if a1 * c2 == a2 * c1: return
    x0, y0 = R.randint(1, 8), R.randint(1, 8); m1, m2 = a1 * x0 + c1 * y0, a2 * x0 + c2 * y0
    p, q = R.randint(2, 20), R.randint(2, 20)
    # ≥ শর্ত: কৌণিক বিন্দু: ছেদ, x-অক্ষে max(m1/a1, m2/a2), y-অক্ষে max(m1/c1, m2/c2)
    xa = max(F(m1, a1), F(m2, a2)); yb = max(F(m1, c1), F(m2, c2))
    pts = [(F(x0), F(y0)), (xa, F(0)), (F(0), yb)]
    vals = [p * x + q * y for x, y in pts]; best = min(vals)
    if best.denominator > 1: return
    b.add(f"{lin2(a1, c1)} ≥ {m1}, {lin2(a2, c2)} ≥ {m2}, x ≥ 0, y ≥ 0 শর্তে Z = {lin2(p, q)}-এর সর্বনিম্ন মান কত?", num(best), W(num(best), [num(v) for v in sorted(set(vals) - {best})[:2]] + [num(best + p), num(best + 1)]), f"কৌণিক বিন্দু {', '.join(P(*t) for t in pts)}।", H)
def h_region(b):
    a, c = R.randint(1, 6), R.randint(1, 6); k = a * c * R.randint(1, 5)
    A = F(k // a * (k // c), 2)
    b.add(f"{lin2(a, c)} ≤ {k}, x ≥ 0, y ≥ 0 সম্ভাব্য অঞ্চলের ক্ষেত্রফল কত বর্গ একক?", fr(A), W(fr(A), [str(k // a * (k // c)), fr(A + 1), str(k)]), "ত্রিভুজের ক্ষেত্রফল।", H)
p2 = run(None, R, fx2, [e_point, e_corner, e_obj, e_form], [m_max1, m_max2, m_min, m_cornercount, m_inter], [h_word, h_diet, h_region], caps=(40, 60, 30), mult=3)
save('j2', p2)

# ================= 3 জটিল সংখ্যা =================
def C(a, b):
    a, b = F(a), F(b)
    if b == 0: return num(a)
    bs = 'i' if abs(b) == 1 else (f"({num(abs(b))})i" if b.denominator > 1 else f"{num(abs(b))}i")
    if a == 0: return ('−' if b < 0 else '') + bs
    return f"{num(a)} {'−' if b < 0 else '+'} {bs}"
fx3a = [
 ("i² = কত?", "−1", ["1", "i", "−i"], "", E), ("i³ = কত?", "−i", ["i", "1", "−1"], "", E), ("i⁴ = কত?", "1", ["−1", "i", "−i"], "", E),
 ("z = a + ib-এর অনুবন্ধী কোনটি?", "a − ib", ["−a + ib", "b + ia", "−a − ib"], "", E), ("|z|² = কত?", "z·z̄", ["z + z̄", "z²", "z/z̄"], "", M),
 ("z + z̄ = কত? (z = a + ib)", "2a", ["2ib", "0", "a² + b²"], "", E), ("z − z̄ = কত? (z = a + ib)", "2ib", ["2a", "0", "a − b"], "", E),
 ("দুটি জটিল সংখ্যা সমান হওয়ার শর্ত কোনটি?", "বাস্তব অংশ ও কাল্পনিক অংশ পৃথকভাবে সমান", ["মডুলাস সমান", "আর্গুমেন্ট সমান", "যোগফল শূন্য"], "", M),
]
def rc(): return (R.randint(-9, 9), R.randint(-9, 9))
def e_ipow(b):
    n = R.randint(5, 200); v = ['1', 'i', '−1', '−i'][n % 4]
    b.add(f"i{sup(n)} = কত?", v, W(v, ['1', 'i', '−1', '−i']), f"{n} ÷ 4-এর ভাগশেষ {n % 4}।", E)
def e_add(b):
    z, w = rc(), rc(); op = R.choice(['+', '−'])
    r = (z[0] + w[0], z[1] + w[1]) if op == '+' else (z[0] - w[0], z[1] - w[1])
    ok = C(*r)
    b.add(f"({C(*z)}) {op} ({C(*w)}) = কত?", ok, W(ok, [C(z[0] - w[0], z[1] - w[1]) if op == '+' else C(z[0] + w[0], z[1] + w[1]), C(r[1], r[0]), C(r[0] + 1, r[1]), C(r[0], -r[1])]), "বাস্তব ও কাল্পনিক অংশ আলাদা।", E)
def e_mod(b):
    a, c = R.choice([(3, 4), (5, 12), (6, 8), (8, 15), (1, 1), (1, 2), (2, 3), (7, 24), (9, 12), (12, 16), (20, 21), (1, 3)])
    a *= R.choice([1, -1]); c *= R.choice([1, -1])
    ok = sqf(a * a + c * c)
    b.add(f"|{C(a, c)}| = কত?", ok, W(ok, [str(abs(a) + abs(c)), str(a * a + c * c), sqf(abs(a * a - c * c)) if a * a != c * c else '0']), "√(a² + b²)।", E)
def e_conj(b):
    z = rc(); ok = C(z[0], -z[1])
    if z[1] == 0: return
    b.add(f"{C(*z)}-এর অনুবন্ধী জটিল সংখ্যা কোনটি?", ok, W(ok, [C(-z[0], z[1]), C(-z[0], -z[1]), C(z[1], z[0])]), "", E)
def m_mul(b):
    z, w = rc(), rc(); r = (z[0] * w[0] - z[1] * w[1], z[0] * w[1] + z[1] * w[0])
    ok = C(*r)
    b.add(f"({C(*z)})({C(*w)}) = কত?", ok, W(ok, [C(z[0] * w[0] + z[1] * w[1], r[1]), C(r[0], -r[1]), C(z[0] * w[0], z[1] * w[1])]), "i² = −1।", M)
def m_div(b):
    z, w = rc(), rc()
    d = w[0] ** 2 + w[1] ** 2
    if d == 0: return
    re, im = F(z[0] * w[0] + z[1] * w[1], d), F(z[1] * w[0] - z[0] * w[1], d)
    if re.denominator > 10 or im.denominator > 10: return
    ok = C(re, im)
    b.add(f"({C(*z)})/({C(*w)}) = কত?", ok, W(ok, [C(re, -im), C(im, re), C(-re, im)]), "হর ও লবকে হরের অনুবন্ধী দিয়ে গুণ।", M)
def m_sq(b):
    a, c = nz(-7, 7), nz(-7, 7); r = (a * a - c * c, 2 * a * c)
    ok = C(*r)
    b.add(f"({C(a, c)})² = কত?", ok, W(ok, [C(a * a + c * c, 2 * a * c), C(r[0], -r[1]), C(a * a, c * c)]), "(a + ib)² = a² − b² + 2abi।", M)
def m_eq(b):
    x, y = R.randint(-8, 8), R.randint(-8, 8); a, c = nz(-4, 4), nz(-4, 4)
    re, im = a * x + 1, c * y - 2
    b.add(f"({co(a, 'x')} + 1) + i({co(c, 'y')} − 2) = {C(re, im)} হলে (x, y) = কত?", P(x, y), W(P(x, y), [P(y, x), P(-x, y), P(x, -y) if y else P(x, 1)]), "অংশ মিলিয়ে।", M)
def m_arg(b):
    (a, c), ang = R.choice([((1, 1), 'π/4'), ((-1, 1), '3π/4'), ((-1, -1), '−3π/4'), ((1, -1), '−π/4'), ((0, 1), 'π/2'), ((0, -1), '−π/2'), ((-1, 0), 'π'), ((1, 0), '0')])
    k = R.randint(1, 9)
    b.add(f"{C(a * k, c * k)}-এর মুখ্য আর্গুমেন্ট কত?", ang, W(ang, ['π/4', '3π/4', '−3π/4', '−π/4', 'π/2', '−π/2', 'π', '0']), "চতুর্ভাগ অনুযায়ী।", M)
    s3 = R.choice([((1, 3), 'π/3'), ((-1, 3), '2π/3'), ((-1, -3), '−2π/3'), ((1, -3), '−π/3')])
    (p, q), ang2 = s3
    b.add(f"{num(p * k)} {'+' if q > 0 else '−'} {k if k > 1 else ''}√3i-এর মুখ্য আর্গুমেন্ট কত?", ang2, W(ang2, ['π/3', '2π/3', '−2π/3', '−π/3', 'π/6', '5π/6']), "tan θ = √3।", M)
def h_recip(b):
    a, c = R.choice([(3, 4), (5, 12), (6, 8), (8, 15), (1, 2), (2, 1), (1, 3), (12, 5), (4, 3)]); a *= R.choice([1, -1])
    d = a * a + c * c
    ok = C(F(a, d), F(-c, d))
    b.add(f"{C(a, c)}-এর গুণাত্মক বিপরীত কোনটি?", ok, W(ok, [C(F(a, d), F(c, d)), C(-a, -c), C(F(1, a), F(-1, c))]), f"z̄/|z|²।", H)
def h_sqrt(b):
    a, c = R.randint(1, 8), nz(-8, 8)
    z = (a * a - c * c, 2 * a * c)
    ok = f"±({C(a, c)})"
    b.add(f"{C(*z)}-এর বর্গমূল কোনটি?", ok, W(ok, [f"±({C(a, -c)})", f"±({C(c, a)})", f"±({C(a * a, c)})"]), f"(a + ib)² = {C(*z)} থেকে।", H)
def h_locus(b):
    a, c, r = R.randint(-5, 5), R.randint(-5, 5), R.randint(1, 8)
    ok = f"বৃত্ত: কেন্দ্র {P(a, c)}, ব্যাসার্ধ {r}"
    b.add(f"|z − ({C(a, c)})| = {r} দ্বারা কোন সঞ্চারপথ নির্দেশিত হয়?".replace('(0)', '0'), ok, W(ok, [f"বৃত্ত: কেন্দ্র {P(-a, -c)}, ব্যাসার্ধ {r}", f"বৃত্ত: কেন্দ্র {P(a, c)}, ব্যাসার্ধ {r * r}", f"সরলরেখা"]), "", H)
def h_mod_prod(b):
    z, w = R.choice([(3, 4), (5, 12), (6, 8), (1, 1)]), R.choice([(3, 4), (5, 12), (8, 15), (1, 2)])
    v = math.sqrt(z[0] ** 2 + z[1] ** 2) * math.sqrt(w[0] ** 2 + w[1] ** 2)
    n2 = (z[0] ** 2 + z[1] ** 2) * (w[0] ** 2 + w[1] ** 2)
    ok = sqf(n2)
    b.add(f"|({C(*z)})({C(*w)})| = কত?", ok, W(ok, [str(z[0] + z[1] + w[0] + w[1]), str(n2), sqf(n2 + 1)]), "|zw| = |z||w|।", H)
p3a = run('3.A', R, fx3a, [e_ipow, e_add, e_mod, e_conj], [m_mul, m_div, m_sq, m_eq, m_arg], [h_recip, h_sqrt, h_locus, h_mod_prod], caps=(40, 50, 30), mult=2)

fx3b = [
 ("এককের ঘনমূলগুলো কী কী?", "1, ω, ω²", ["1, −1, i", "1, i, −i", "1, 2, 3"], "", E), ("1 + ω + ω² = কত?", "0", ["1", "−1", "3"], "", E),
 ("ω³ = কত?", "1", ["ω", "0", "−1"], "", E), ("ω = কত?", "(−1 + √3i)/2", ["(1 + √3i)/2", "(−1 − i)/2", "√3/2"], "", M),
 ("দ্য মোয়াভরের উপপাদ্য অনুযায়ী (cos θ + i sin θ)ⁿ = কত?", "cos nθ + i sin nθ", ["n cos θ + i n sin θ", "cosⁿθ + i sinⁿθ", "cos θⁿ + i sin θⁿ"], "", E),
 ("z = r(cos θ + i sin θ) হলে r কী নির্দেশ করে?", "মডুলাস", ["আর্গুমেন্ট", "বাস্তব অংশ", "কাল্পনিক অংশ"], "", E),
 ("ω ও ω²-এর গুণফল কত?", "1", ["0", "−1", "ω"], "", E), ("ω + ω² = কত?", "−1", ["0", "1", "2"], "", E),
]
def e_wpow(b):
    n = R.randint(4, 300); v = ['1', 'ω', 'ω²'][n % 3]
    b.add(f"ω{sup(n)} = কত?", v, W(v, ['1', 'ω', 'ω²', '−1', '0']), f"{n} ÷ 3-এর ভাগশেষ {n % 3}।", E)
def e_wsum(b):
    m, n = R.randint(1, 60), R.randint(1, 60)
    s = (m % 3, n % 3)
    vals = {0: 1, 1: 'ω', 2: 'ω²'}
    a, c = s
    if a == c: v = '2' if a == 0 else ('2ω' if a == 1 else '2ω²')
    elif {a, c} == {1, 2}: v = '−1'
    elif {a, c} == {0, 1}: v = '−ω²'
    else: v = '−ω'
    b.add(f"ω{sup(m)} + ω{sup(n)} = কত?", v, W(v, ['−1', '2', '−ω', '−ω²', '0', '1']), "1 + ω + ω² = 0 ব্যবহার করে।", E)
def m_polar(b):
    r = R.randint(1, 12); th, cs = R.choice([('π/2', (0, 1)), ('π', (-1, 0)), ('3π/2', (0, -1)), ('0', (1, 0)), ('π/6', None), ('π/3', None), ('π/4', None)])
    c, s = cs if cs else (None, None)
    if c is None:
        ok = {'π/6': f"{r if r > 1 else ''}√3/2 + {fr(F(r, 2))}i", 'π/3': f"{fr(F(r, 2))} + {r if r > 1 else ''}√3i/2", 'π/4': f"{r}/√2 + {r}i/√2"}[th]
        ws = [f"{fr(F(r, 2))} + {r if r > 1 else ''}√3i/2", f"{r if r > 1 else ''}√3/2 + {fr(F(r, 2))}i", f"{r}/√2 + {r}i/√2", f"{r} + {r}i"]
    else:
        ok = C(r * c, r * s); ws = [C(r * s, r * c), C(-r * c, -r * s) if (c or s) else '1', C(r, r)]
    b.add(f"{r}(cos {th} + i sin {th})-কে a + ib আকারে লিখলে কোনটি?", ok, W(ok, ws), "", M)
def m_demoivre(b):
    n = R.randint(2, 12); th = R.choice([F(1, 6), F(1, 4), F(1, 3), F(1, 2), F(1, 12), F(1, 8)])
    v = n * th
    ok = f"cos {piF(v)} + i sin {piF(v)}"
    b.add(f"(cos {piF(th)} + i sin {piF(th)}){sup(n)} = কত?", ok, W(ok, [f"cos {piF(th)} + i sin {piF(v)}", f"{n} cos {piF(th)} + i {n} sin {piF(th)}", f"cos {piF(v + th)} + i sin {piF(v + th)}"]), "দ্য মোয়াভর।", M)
def m_dm_val(b):
    n = R.choice([3, 6, 9, 12, 4, 8, 2]); th = R.choice([F(1, 6), F(1, 4), F(1, 3), F(1, 2)])
    ang = (n * th) % 2
    tbl = {F(0): '1', F(1, 2): 'i', F(1): '−1', F(3, 2): '−i'}
    if ang not in tbl: return
    ok = tbl[ang]
    b.add(f"(cos {piF(th)} + i sin {piF(th)}){sup(n)} = কত?", ok, W(ok, ['1', 'i', '−1', '−i', '0']), f"cos {piF(n * th)} + i sin {piF(n * th)}।", M)
def m_wexpr(b):
    a, c = R.randint(1, 9), R.randint(1, 9)
    # (a + cω + aω²)… সহজ: (1 + ω − ω²)(1 − ω + ω²) = 4
    q, ok = R.choice([("(1 + ω − ω²)(1 − ω + ω²)", '4'), ("(1 − ω + ω²)³", '−8'), ("(1 + ω − ω²)³", '−8'), ("(1 − ω)(1 − ω²)", '3'), ("(1 + ω²)⁴", 'ω'), ("(1 + ω)³", '−1'), ("(2 + 5ω + 2ω²)⁶", '729'), ("(1 − ω + ω²)(1 + ω − ω²)", '4'), ("ω¹⁰⁰ + ω²⁰⁰ + 1", '0'), ("(1 + ω)(1 + ω²)", '1')])
    b.add(f"{q} = কত?", ok, W(ok, ['4', '−8', '3', 'ω', '−1', '729', '0', '1', '8']), "1 + ω + ω² = 0 ও ω³ = 1।", M)
def h_cube(b):
    k = R.randint(2, 12)
    ok = f"{k}, {k}ω, {k}ω²"
    b.add(f"x³ = {k ** 3} সমীকরণের মূলগুলো কোনটি?", ok, W(ok, [f"{k}, −{k}, {k}i", f"{k}, {k}, {k}", f"{k}, {k}i, −{k}i", f"−{k}, {k}ω, {k}ω²"]), "এককের ঘনমূল দিয়ে গুণ।", H)
def h_sqrtc(b):
    a, c = R.randint(1, 9), R.randint(1, 9)
    z = (a * a - c * c, 2 * a * c)
    ok = f"±({C(a, c)})"
    b.add(f"√({C(*z)}) = কত?", ok, W(ok, [f"±({C(a, -c)})", f"±({C(c, a)})", f"±{a}"]), "", H)
def h_polar_mod(b):
    r1, r2 = R.randint(1, 9), R.randint(1, 9); t1, t2 = R.choice([F(1, 6), F(1, 4), F(1, 3)]), R.choice([F(1, 6), F(1, 4), F(1, 3), F(1, 2)])
    ok = f"{r1 * r2}(cos {piF(t1 + t2)} + i sin {piF(t1 + t2)})"
    b.add(f"z₁ = {r1}(cos {piF(t1)} + i sin {piF(t1)}), z₂ = {r2}(cos {piF(t2)} + i sin {piF(t2)}) হলে z₁z₂ = কত?", ok, W(ok, [f"{r1 + r2}(cos {piF(t1 + t2)} + i sin {piF(t1 + t2)})", f"{r1 * r2}(cos {piF(t1 * t2)} + i sin {piF(t1 * t2)})", f"{r1 * r2}(cos {piF(abs(t1 - t2))} + i sin {piF(abs(t1 - t2))})"]), "মডুলাস গুণ, আর্গুমেন্ট যোগ।", H)
p3b = run('3.B', R, fx3b, [e_wpow, e_wsum], [m_polar, m_demoivre, m_dm_val, m_wexpr], [h_cube, h_sqrtc, h_polar_mod], caps=(40, 50, 30), mult=2)
save('j3', p3a + p3b)

# ================= 4 বহুপদী ও বহুপদী সমীকরণ =================
fx4 = [
 ("ax² + bx + c = 0-এর মূলদ্বয়ের যোগফল কত?", "−b/a", ["b/a", "c/a", "−c/a"], "", E), ("ax² + bx + c = 0-এর মূলদ্বয়ের গুণফল কত?", "c/a", ["−c/a", "b/a", "a/c"], "", E),
 ("ax³ + bx² + cx + d = 0-এর মূলত্রয়ের যোগফল কত?", "−b/a", ["b/a", "−d/a", "c/a"], "", E), ("ax³ + bx² + cx + d = 0-এর মূলত্রয়ের গুণফল কত?", "−d/a", ["d/a", "−b/a", "c/a"], "", E),
 ("ax³ + bx² + cx + d = 0 হলে αβ + βγ + γα = কত?", "c/a", ["−c/a", "b/a", "d/a"], "", M), ("n মাত্রার বহুপদী সমীকরণের কয়টি মূল থাকে?", "n টি", ["n − 1 টি", "n + 1 টি", "2n টি"], "", E),
 ("বাস্তব সহগযুক্ত সমীকরণের একটি মূল a + ib হলে অপর একটি মূল কী?", "a − ib", ["−a + ib", "b + ia", "−a − ib"], "জটিল মূল জোড়ায় আসে।", M),
 ("মূলদ সহগযুক্ত সমীকরণের একটি মূল 2 + √3 হলে অপর একটি মূল কী?", "2 − √3", ["−2 + √3", "√3 − 2", "2√3"], "", M),
 ("নিশ্চায়ক b² − 4ac < 0 হলে দ্বিঘাত সমীকরণের মূলদ্বয় কেমন?", "জটিল (অবাস্তব) ও অনুবন্ধী", ["বাস্তব ও সমান", "বাস্তব ও অসমান", "মূলদ"], "", E),
]
def quad(a, c, d): return px({2: a, 1: c, 0: d})
def e_sum(b):
    a, c, d = R.choice([1, 2, 3, 4, 5]), nz(-12, 12), nz(-12, 12)
    s = F(-c, a)
    b.add(f"{quad(a, c, d)} = 0 সমীকরণের মূলদ্বয়ের যোগফল কত?", num(s), W(num(s), [num(-s), num(F(d, a)), num(F(-d, a)), num(s + 1)]), "−b/a।", E)
def e_prod(b):
    a, c, d = R.choice([1, 2, 3, 4, 5]), nz(-12, 12), nz(-12, 12)
    p = F(d, a)
    b.add(f"{quad(a, c, d)} = 0 সমীকরণের মূলদ্বয়ের গুণফল কত?", num(p), W(num(p), [num(-p), num(F(-c, a)), num(F(c, a)), num(p + 1)]), "c/a।", E)
def e_cub(b):
    r = R.sample(range(-6, 7), 3); a = R.choice([1, 1, 2])
    s, q, p = sum(r), r[0] * r[1] + r[1] * r[2] + r[0] * r[2], r[0] * r[1] * r[2]
    cs = {3: a, 2: -a * s, 1: a * q, 0: -a * p}
    kind = R.choice(['যোগফল', 'গুণফল'])
    v = s if kind == 'যোগফল' else p
    b.add(f"{px(cs)} = 0 সমীকরণের মূলত্রয়ের {kind} কত?", num(v), W(num(v), [num(-v) if v else '1', num(q), num(v + 1), num(s if kind == 'গুণফল' else p) if (s if kind == 'গুণফল' else p) != v else num(v + 2)]), "মূল-সহগ সম্পর্ক।", E)
def e_form(b):
    r1, r2 = R.sample([v for v in range(-12, 13) if v], 2)
    ok = f"{quad(1, -(r1 + r2), r1 * r2)} = 0"
    b.add(f"যে দ্বিঘাত সমীকরণের মূলদ্বয় {num(r1)} ও {num(r2)}, সেটি কোনটি?", ok, W(ok, [f"{quad(1, r1 + r2, r1 * r2)} = 0", f"{quad(1, -(r1 + r2), -r1 * r2)} = 0", f"{quad(1, r1 + r2, -r1 * r2)} = 0"]), "", E)
def m_sq(b):
    a, c, d = R.choice([1, 2, 3]), nz(-10, 10), nz(-10, 10); s, p = F(-c, a), F(d, a); v = s * s - 2 * p
    b.add(f"{quad(a, c, d)} = 0-এর মূল α, β হলে α² + β² = কত?", num(v), W(num(v), [num(s * s + 2 * p), num(s * s - p), num(s * s), num(v + 1)]), "(α + β)² − 2αβ।", M)
def m_cube(b):
    a, c, d = R.choice([1, 2]), nz(-8, 8), nz(-8, 8); s, p = F(-c, a), F(d, a); v = s ** 3 - 3 * s * p
    b.add(f"{quad(a, c, d)} = 0-এর মূল α, β হলে α³ + β³ = কত?", num(v), W(num(v), [num(s ** 3 + 3 * s * p), num(s ** 3), num(v + 1), num(s ** 3 - p)]), "(α + β)³ − 3αβ(α + β)।", M)
def m_cub2(b):
    r = R.sample(range(-5, 6), 3); s, q, p = sum(r), r[0] * r[1] + r[1] * r[2] + r[0] * r[2], r[0] * r[1] * r[2]
    v = s * s - 2 * q
    b.add(f"{px({3: 1, 2: -s, 1: q, 0: -p})} = 0-এর মূল α, β, γ হলে α² + β² + γ² = কত?", v, W(v, [s * s + 2 * q, s * s, v + 2, q]), "(Σα)² − 2Σαβ।", M)
def m_nature(b):
    a, c, d = R.randint(1, 6), nz(-12, 12), nz(-12, 12); D = c * c - 4 * a * d
    ok = 'বাস্তব ও সমান' if D == 0 else ('জটিল ও অনুবন্ধী' if D < 0 else ('বাস্তব, অসমান ও মূলদ' if math.isqrt(D) ** 2 == D else 'বাস্তব, অসমান ও অমূলদ'))
    b.add(f"{quad(a, c, d)} = 0-এর মূলের প্রকৃতি কেমন?", ok, W(ok, ['বাস্তব ও সমান', 'জটিল ও অনুবন্ধী', 'বাস্তব, অসমান ও মূলদ', 'বাস্তব, অসমান ও অমূলদ']), f"D = {num(D)}।", M)
def m_k(b):
    a, c = R.randint(1, 5), R.randint(1, 9)
    v = 4 * a * c; r = math.isqrt(v)
    if r * r != v: return
    b.add(f"{co(a, 'x²')} + kx + {c} = 0-এর মূলদ্বয় সমান হলে k = কত?", f"±{r}", W(f"±{r}", [str(r), f"±{v}", f"±{r // 2 if r % 2 == 0 else r + 1}"]), "k² = 4ac।", M)
def m_other(b):
    a, c = R.randint(-6, 6), R.randint(1, 8)
    ok = C(a, -c)
    b.add(f"বাস্তব সহগযুক্ত একটি দ্বিঘাত সমীকরণের একটি মূল {C(a, c)} হলে সমীকরণটি কোনটি?", f"{quad(1, -2 * a, a * a + c * c)} = 0", W(f"{quad(1, -2 * a, a * a + c * c)} = 0", [f"{quad(1, 2 * a, a * a + c * c)} = 0", f"{quad(1, -2 * a, a * a - c * c)} = 0", f"{quad(1, -a, a * a + c * c)} = 0"]), f"অপর মূল {ok}।", M)
def h_newroots(b):
    r1, r2 = R.sample([v for v in range(-8, 9) if v], 2); a, c = 1, -(r1 + r2); d = r1 * r2
    t = R.choice(['sq', 'neg', 'twice'])
    n1, n2 = {'sq': (r1 * r1, r2 * r2), 'neg': (-r1, -r2), 'twice': (2 * r1, 2 * r2)}[t]
    if n1 == n2: return
    ok = f"{quad(1, -(n1 + n2), n1 * n2)} = 0"
    lab = {'sq': 'α² ও β²', 'neg': '−α ও −β', 'twice': '2α ও 2β'}[t]
    b.add(f"{quad(a, c, d)} = 0-এর মূল α, β হলে যে সমীকরণের মূল {lab}, সেটি কোনটি?", ok, W(ok, [f"{quad(1, n1 + n2, n1 * n2)} = 0", f"{quad(1, -(n1 + n2), -n1 * n2)} = 0", f"{quad(a, c, d)} = 0"]), "নতুন মূলের যোগফল ও গুণফল।", H)
def h_cubic_root(b):
    r = R.sample(range(-5, 6), 3); s, q, p = sum(r), r[0] * r[1] + r[1] * r[2] + r[0] * r[2], r[0] * r[1] * r[2]
    v = F(q, -p) if p else None
    if v is None: return
    b.add(f"{px({3: 1, 2: -s, 1: q, 0: -p})} = 0-এর মূল α, β, γ হলে 1/α + 1/β + 1/γ = কত?", num(v), W(num(v), [num(-v) if v else '1', num(F(s, p)), num(v + 1)]), "Σαβ/αβγ।", H)
def h_ap(b):
    m, d = R.randint(-4, 4), R.randint(1, 4)
    r = [m - d, m, m + d]; s, q, p = sum(r), r[0] * r[1] + r[1] * r[2] + r[0] * r[2], r[0] * r[1] * r[2]
    b.add(f"{px({3: 1, 2: -s, 1: q, 0: -p})} = 0-এর মূলগুলো সমান্তর প্রগমনে থাকলে মধ্যম মূলটি কত?", num(m), W(num(m), [num(s), num(m + d), num(-m) if m else '1']), "3β = Σα।", H)
def h_common(b):
    r = nz(-6, 6); s1, s2 = R.sample([v for v in range(-7, 8) if v != r], 2)
    b.add(f"{quad(1, -(r + s1), r * s1)} = 0 ও {quad(1, -(r + s2), r * s2)} = 0-এর সাধারণ মূল কত?", num(r), W(num(r), [num(s1), num(s2), num(-r)]), "", H)
p4 = run(None, R, fx4, [e_sum, e_prod, e_cub, e_form], [m_sq, m_cube, m_cub2, m_nature, m_k, m_other], [h_newroots, h_cubic_root, h_ap, h_common], caps=(60, 60, 40), mult=3)
save('j4', p4)

# ================= 5 দ্বিপদী =================
Cm = math.comb
fx5a = [
 ("(a + b)ⁿ-এর বিস্তৃতিতে পদসংখ্যা কত?", "n + 1", ["n", "n − 1", "2n"], "", E), ("(a + b)ⁿ-এ (r + 1)-তম পদ কোনটি?", "ⁿCᵣ aⁿ⁻ʳ bʳ", ["ⁿCᵣ₊₁ aⁿ⁻ʳ bʳ", "ⁿCᵣ aʳ bⁿ⁻ʳ⁺¹", "ⁿCᵣ₋₁ aⁿ bʳ"], "", E),
 ("ⁿC₀ + ⁿC₁ + … + ⁿCₙ = কত?", "2ⁿ", ["n²", "n!", "2n"], "", E), ("ⁿC₀ − ⁿC₁ + ⁿC₂ − … = কত?", "0", ["1", "2ⁿ", "−1"], "", M),
 ("n জোড় হলে (a + b)ⁿ-এর মধ্যপদ কোনটি?", "(n/2 + 1)-তম", ["(n/2)-তম", "(n + 1)-তম", "দুটি মধ্যপদ"], "", M),
]
def e_coef(b):
    n = R.randint(3, 12); r = R.randint(1, n - 1); a, c = R.choice([1, 2, 3]), R.choice([1, 2, 3, -1, -2])
    v = Cm(n, r) * a ** (n - r) * c ** r
    xs = f"x{sup(n - r)}".replace('x¹', 'x'); ys = f"y{sup(r)}".replace('y¹', 'y')
    b.add(f"({co(a, 'x')} {'+' if c > 0 else '−'} {co(abs(c), 'y')}){sup(n)}-এর বিস্তৃতিতে {xs}{ys}-এর সহগ কত?", num(v), W(num(v), [num(Cm(n, r)), num(-v), num(Cm(n, r) * a ** r * c ** (n - r)) if Cm(n, r) * a ** r * c ** (n - r) != v else num(v + 1), num(v * 2)]), f"{n}C{r} × {a}{sup(n - r)} × ({num(c)}){sup(r)}।", E)
def e_terms(b):
    n = R.randint(3, 40)
    b.add(f"(2x + 3y){sup(n)}-এর বিস্তৃতিতে পদসংখ্যা কত?", n + 1, W(n + 1, [n, n + 2, 2 * n]), "", E)
def e_sum(b):
    n = R.randint(2, 10); a, c = R.choice([(1, 1), (2, 1), (1, 2), (3, 1), (2, -1), (3, -2), (1, -2), (4, -1)])
    v = (a + c) ** n
    b.add(f"({co(a, 'x')} {'+' if c > 0 else '−'} {co(abs(c), 'y')}){sup(n)}-এর সহগগুলোর যোগফল কত?", num(v), W(num(v), [num(2 ** n), num((a - c) ** n), num(a ** n + c ** n), num(v + 1)]), "x = y = 1।", E)
def m_indep(b):
    n = 2 * R.randint(2, 6); k = R.randint(1, 4)
    v = Cm(n, n // 2) * k ** (n // 2)
    b.add(f"(x + {k}/x){sup(n)}-এর বিস্তৃতিতে x-বর্জিত পদ কত?", v, W(v, [Cm(n, n // 2), v * k, Cm(n, n // 2 - 1) * k ** (n // 2), v + 1]), "n − 2r = 0।", M)
def m_indep2(b):
    n = 3 * R.randint(1, 4); k = R.choice([1, 2, -1, -2, 3])
    r = 2 * n // 3; v = Cm(n, r) * k ** r
    b.add(f"(x² {'+' if k > 0 else '−'} {abs(k)}/x){sup(n)}-এর বিস্তৃতিতে x-বর্জিত পদ কত?", num(v), W(num(v), [num(Cm(n, r)), num(-v), num(Cm(n, n // 3) * k ** (n // 3)) if Cm(n, n // 3) * k ** (n // 3) != v else num(v + 3)]), "2(n − r) − r = 0।", M)
def m_middle(b):
    n = 2 * R.randint(2, 6); a, c = R.choice([(1, 2), (2, 1), (1, 3), (2, 3), (3, 1)])
    r = n // 2; v = Cm(n, r) * a ** (n - r) * c ** r
    b.add(f"({co(a, 'x')} + {co(c, 'y')}){sup(n)}-এর মধ্যপদের সহগ কত?", v, W(v, [Cm(n, r), v * 2, Cm(n, r - 1) * a ** (n - r + 1) * c ** (r - 1)]), "", M)
def m_xpow(b):
    n = R.randint(5, 10); k = R.choice([1, 2, 3]); r = R.randint(0, n); p = n - 2 * r
    if p == 0: return
    v = Cm(n, r) * k ** r
    b.add(f"(x + {k}/x){sup(n)}-এর বিস্তৃতিতে x{sup(p)}-এর সহগ কত?".replace('x¹', 'x'), v, W(v, [Cm(n, r), v * 2, Cm(n, r + 1) * k ** (r + 1) if r < n else v + 3]), f"n − 2r = {p}।", M)
def m_ratio(b):
    n = R.randint(5, 20); v = F(Cm(n, 2), Cm(n, 1))
    b.add(f"(1 + x)ⁿ-এর বিস্তৃতিতে x² ও x-এর সহগের অনুপাত {fr(v)} হলে n = কত?", n, W(n, [n + 1, n - 1, 2 * n]), "(n − 1)/2।", M)
def h_sum2(b):
    n = R.randint(2, 12)
    b.add(f"ⁿC₁ + 2·ⁿC₂ + 3·ⁿC₃ + … + n·ⁿCₙ (n = {n}) = কত?", n * 2 ** (n - 1), W(n * 2 ** (n - 1), [2 ** n, n * 2 ** n, (n + 1) * 2 ** (n - 1)]), "n·2ⁿ⁻¹।", H)
def h_greatest(b):
    n = R.randint(4, 14)
    v = max(Cm(n, r) for r in range(n + 1))
    b.add(f"(1 + x){sup(n)}-এর বিস্তৃতিতে বৃহত্তম দ্বিপদী সহগ কত?", v, W(v, [2 ** n, Cm(n, n // 2 - 1), v + 1]), "মধ্যপদ।", H)
def h_term_eq(b):
    n = R.randint(6, 20); r = R.randint(1, n // 2 - 1)
    b.add(f"(1 + x){sup(n)}-এ x{sup(r)} ও xᵏ-এর সহগ সমান (k ≠ {r}) হলে k = কত?".replace('x¹', 'x'), n - r, W(n - r, [n - r + 1, r + 1, n]), "ⁿCᵣ = ⁿCₙ₋ᵣ।", H)
def h_diff(b):
    n = R.randint(3, 9); p = R.randint(0, n - 1)
    if (n - p) % 2 == 0: return
    v = 2 * Cm(n, p)
    b.add(f"(x + 1){sup(n)} − (x − 1){sup(n)}-এর বিস্তৃতিতে x{sup(p)}-এর সহগ কত?".replace('x¹', 'x').replace('x⁰', 'ধ্রুবক পদ'), v, W(v, [Cm(n, p), 0, v + 2]), "", H)
p5a = run('5.A', R, fx5a, [e_coef, e_terms, e_sum], [m_indep, m_indep2, m_middle, m_xpow, m_ratio], [h_sum2, h_greatest, h_term_eq, h_diff], caps=(50, 40, 30), mult=2)

fx5b = [
 ("(1 + x)ⁿ-এর অসীম বিস্তৃতি (n মূলদ, পূর্ণসংখ্যা নয়) বৈধ হওয়ার শর্ত কোনটি?", "|x| < 1", ["|x| > 1", "x > 0", "x < 1"], "", E),
 ("(1 − x)⁻¹ = কত? (|x| < 1)", "1 + x + x² + x³ + …", ["1 − x + x² − …", "1 + 2x + 3x² + …", "1 − x"], "", E),
 ("(1 + x)⁻¹ = কত? (|x| < 1)", "1 − x + x² − x³ + …", ["1 + x + x² + …", "1 − 2x + 3x² − …", "1 + x"], "", E),
 ("(1 − x)⁻² = কত? (|x| < 1)", "1 + 2x + 3x² + 4x³ + …", ["1 + x + x² + …", "1 − 2x + 3x² − …", "1 + 2x + x²"], "", M),
 ("n ঋণাত্মক পূর্ণসংখ্যা হলে (1 + x)ⁿ-এর বিস্তৃতিতে পদসংখ্যা কত?", "অসীম", ["n + 1", "|n| + 1", "n"], "", E),
]
def gcoef(n, r):
    """(1 + x)ⁿ-এ xʳ-এর সহগ, n মূলদ"""
    v = F(1)
    for i in range(r): v *= (n - i)
    return v / math.factorial(r)
def e_first(b):
    n = R.choice([F(1, 2), F(-1, 2), F(1, 3), F(-1), F(-2), F(-3), F(2, 3), F(3, 2), F(-1, 3)]); k = R.choice([1, 2, 3, -1, -2])
    c1, c2 = gcoef(n, 1) * k, gcoef(n, 2) * k * k
    ok = f"1 {'+' if c1 > 0 else '−'} {co(abs(c1), 'x')} {'+' if c2 > 0 else '−'} {co(abs(c2), 'x²')}"
    w = f"1 {'−' if c1 > 0 else '+'} {co(abs(c1), 'x')} {'+' if c2 > 0 else '−'} {co(abs(c2), 'x²')}"
    b.add(f"(1 {'+' if k > 0 else '−'} {co(abs(k), 'x')})^({num(n)})-এর বিস্তৃতির প্রথম তিন পদ কোনটি?", ok, W(ok, [w, f"1 {'+' if c1 > 0 else '−'} {co(abs(c1), 'x')} {'−' if c2 > 0 else '+'} {co(abs(c2), 'x²')}", f"1 + {co(abs(k), 'x')} + {co(k * k, 'x²')}"]), "সাধারণ সূত্র।", E)
def e_coef(b):
    n = R.choice([-1, -2, -3]); r = R.randint(2, 6); k = R.choice([1, 2, -1])
    v = gcoef(F(n), r) * F(k) ** r
    b.add(f"(1 {'+' if k > 0 else '−'} {co(abs(k), 'x')})^({n})-এর বিস্তৃতিতে x{sup(r)}-এর সহগ কত?", num(v), W(num(v), [num(-v), num(v + 1), num(gcoef(F(n), r - 1) * F(k) ** (r - 1))]), "", E)
def m_approx(b):
    n, a = R.choice([(2, 4), (2, 9), (2, 16), (2, 25), (3, 8), (3, 27), (2, 49), (2, 100)]); d = R.choice([1, 2, -1])
    root = round(a ** (1 / n)); x = F(d, a)
    v = root * (1 + F(1, n) * x)
    s = f"{float(v):.4f}"
    b.add(f"দ্বিপদী বিস্তৃতির প্রথম দুই পদ নিয়ে {['', '', '√', '∛'][n]}{a + d}-এর আসন্ন মান কত?", s, W(s, [f"{float(root + F(d, n)):.4f}", f"{root}", f"{float(v) + 0.01:.4f}"]), f"{root}(1 + {d}/{a})^(1/{n}) ≈ {root}(1 + {d}/({n}·{a}))।", M)
def m_gen(b):
    k = R.randint(2, 6); r = R.randint(2, 6)
    v = (r + 1) * k ** r
    b.add(f"(1 − {k}x)⁻²-এর বিস্তৃতিতে x{sup(r)}-এর সহগ কত?", v, W(v, [r * k ** r, (r + 1) * k, v + k]), "(r + 1)kʳ।", M)
def m_cond(b):
    k = R.choice([2, 3, 4, 5, F(1, 2), F(1, 3)])
    ok = f"|x| < {fr(1 / F(k))}"
    b.add(f"(1 + {fr(k)}x)^(1/2)-এর অসীম বিস্তৃতি বৈধ হওয়ার শর্ত কোনটি?", ok, W(ok, [f"|x| < {fr(F(k))}", "|x| < 1", f"|x| > {fr(1 / F(k))}"]), f"|{fr(k)}x| < 1।", M)
def m_coef2(b):
    n = R.choice([F(1, 2), F(-1, 2), F(1, 3), F(-1, 3), F(2, 3), F(3, 2), F(-2), F(-3), F(-4), F(1, 4), F(-3, 2)]); k = R.choice([1, 2, 3, 4, -1, -2, -3, F(1, 2), F(-1, 2)])
    r = R.choice([2, 3])
    v = gcoef(n, r) * F(k) ** r
    b.add(f"(1 {'+' if k > 0 else '−'} {co(abs(k), 'x')})^({num(n)})-এর বিস্তৃতিতে x{sup(r)}-এর সহগ কত?", num(v), W(num(v), [num(-v), num(gcoef(n, r) * F(k)), num(gcoef(n, r)), num(v * 2)]), "n(n − 1)…/r! × kʳ।", M)
def m_power(b):
    a, n = R.choice([(1, 10), (2, 10), (3, 10), (1, 100), (2, 100), (5, 100), (4, 100)]), R.choice([2, 3, 5, 10, F(1, 2), F(-1)])
    d, base = a
    x = F(d, base); v = 1 + F(n) * x
    s = f"{float(v):.4f}"
    b.add(f"প্রথম দুই পদ নিয়ে (1 + {num(x)})^({num(n)})-এর আসন্ন মান কত?", s, W(s, [f"{float(1 + x):.4f}", f"{float(1 - F(n) * x):.4f}", f"{float(v) + 0.1:.4f}"]), "(1 + x)ⁿ ≈ 1 + nx।", M)
def m_term3(b):
    n = R.choice([-1, -2, -3, -4]); k = R.choice([2, 3, 4, 5, -2, -3])
    r = R.randint(1, 5)
    v = gcoef(F(n), r) * F(k) ** r
    b.add(f"1/(1 {'+' if k > 0 else '−'} {abs(k)}x){sup(-n) if n != -1 else ''}-এর বিস্তৃতিতে x{sup(r)}-এর সহগ কত?".replace('x¹', 'x'), num(v), W(num(v), [num(-v), num(v + 1), num(gcoef(F(n), r))]), "", M)
def h_rterm(b):
    n = R.choice([F(1, 2), F(-1, 2), F(1, 3), F(-1, 3), F(3, 2)]); r = R.randint(2, 4)
    v = gcoef(n, r)
    b.add(f"(1 + x)^({num(n)})-এর বিস্তৃতিতে x{sup(r)}-এর সহগ কত?", num(v), W(num(v), [num(-v), num(gcoef(n, r - 1)), num(v * 2)]), "n(n − 1)…(n − r + 1)/r!।", H)
def h_sumser(b):
    k = R.choice([2, 3, 4, 5]);
    b.add(f"1 + 2(1/{k}) + 3(1/{k})² + 4(1/{k})³ + … = কত?", fr(F(k * k, (k - 1) ** 2)), W(fr(F(k * k, (k - 1) ** 2)), [fr(F(k, k - 1)), fr(F(k * k, (k + 1) ** 2)), str(k)]), "(1 − x)⁻², x = 1/k।", H)
def h_ratio(b):
    k = R.choice([2, 3, 4])
    b.add(f"1 + x/{k} + x²/{k * k} + … (|x| < {k})-এর যোগফল কোনটি?", f"{k}/({k} − x)", W(f"{k}/({k} − x)", [f"{k}/({k} + x)", f"1/({k} − x)", f"({k} − x)/{k}"]), "(1 − x/k)⁻¹।", H)
def h_prodser(b):
    a, k, r = R.randint(1, 6), R.choice([1, 2, 3]), R.randint(2, 6)
    # (1 + a x)(1 − kx)⁻¹ : xʳ-এর সহগ = kʳ + a kʳ⁻¹
    v = k ** r + a * k ** (r - 1)
    b.add(f"(1 + {co(a, 'x')})/(1 − {co(k, 'x')})-এর বিস্তৃতিতে x{sup(r)}-এর সহগ কত?", v, W(v, [k ** r, a * k ** (r - 1), k ** r - a * k ** (r - 1), v + k]), "(1 + ax)(1 + kx + k²x² + …)।", H)
def h_sq3(b):
    k = R.choice([2, 3, 4, 5]); r = R.randint(2, 6)
    v = math.comb(r + 2, 2) * k ** r
    b.add(f"(1 − {k}x)⁻³-এর বিস্তৃতিতে x{sup(r)}-এর সহগ কত?", v, W(v, [(r + 1) * k ** r, math.comb(r + 2, 2), v + k, math.comb(r + 3, 3) * k ** r]), "(r + 1)(r + 2)/2 · kʳ।", H)
def h_3term(b):
    n = R.choice([F(1, 2), F(-1, 2), F(1, 3), F(-1), F(-2)]); k = R.choice([F(1, 10), F(1, 100), F(-1, 10), F(2, 100)])
    v = 1 + n * k + gcoef(n, 2) * k * k
    s = f"{float(v):.5f}"
    b.add(f"প্রথম তিন পদ নিয়ে (1 + ({num(k)}))^({num(n)})-এর আসন্ন মান কত?", s, W(s, [f"{float(1 + n * k):.5f}", f"{float(1 + n * k - gcoef(n, 2) * k * k):.5f}", f"{float(v) + 0.001:.5f}"]), "", H)
p5b = run('5.B', R, fx5b, [e_first, e_coef], [m_approx, m_gen, m_cond, m_coef2, m_power, m_term3], [h_rterm, h_sumser, h_ratio, h_prodser, h_sq3, h_3term], caps=(50, 50, 30), mult=2)
save('j5', p5a + p5b)
