#!/usr/bin/env python3
"""অধ্যায় 5 এক চলকবিশিষ্ট সমীকরণ: 5.1 সরল সমীকরণ ও বাস্তব সমস্যা · 5.2 দ্বিঘাত সমীকরণ"""
import random, pathlib, sys, math
from fractions import Fraction as F
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from mcqlib import run, save, E, M, H, fr, near, num, sg, pfmt, pmul, lin

R = random.Random(2026103105)
X = ('x',)
def lx(a, c): return pfmt(lin([a], c), X)
fx51 = [
 ("যে সমীকরণে চলকের সর্বোচ্চ ঘাত 1, তাকে কী বলে?", "সরল বা একঘাত সমীকরণ", ["দ্বিঘাত সমীকরণ", "অভেদ", "ত্রিঘাত সমীকরণ"], "চলকের ঘাত 1।", E),
 ("চলকের সকল মানের জন্য যে সমতা সত্য, তাকে কী বলে?", "অভেদ", ["সমীকরণ", "অসমতা", "সূত্র নয়"], "যেমন (x + 1)² = x² + 2x + 1।", E),
 ("নিচের কোনটি অভেদ?", "(a + b)² = a² + 2ab + b²", ["2x + 3 = 7", "x² = 4", "x + 1 = 0"], "সব মানের জন্য সত্য।", E),
 ("একটি সরল সমীকরণের কয়টি মূল থাকে?", "1টি", ["2টি", "3টি", "অসংখ্য"], "একঘাত সমীকরণের একটি মূল।", E),
 ("সমীকরণের উভয় পক্ষে একই সংখ্যা যোগ করলে সমাধানের কী হয়?", "অপরিবর্তিত থাকে", ["দ্বিগুণ হয়", "শূন্য হয়", "বদলে যায়"], "সমীকরণের স্বতঃসিদ্ধ।", E),
]
def e_lin(b):
    a_, x = R.randint(2, 9), R.randint(-9, 12); c_ = R.choice([v for v in range(-15, 16) if v])
    rhs = a_ * x + c_
    b.add(f"{lx(a_, c_)} = {num(rhs)} হলে x = কত?", num(x), [num(w) for w in near(x)], f"{a_}x = {num(rhs)} {'−' if c_ > 0 else '+'} {abs(c_)} = {num(a_ * x)} ⇒ x = {num(x)}।", E)
def e_lin2(b):
    a_, b_ = R.sample(range(2, 10), 2); x = R.randint(-6, 9); c_ = R.randint(-9, 9); d_ = (a_ - b_) * x + c_
    b.add(f"{lx(a_, c_)} = {lx(b_, d_)} হলে x = কত?", num(x), [num(w) for w in near(x)], f"({a_} − {b_})x = {num(d_)} − ({num(c_)}) ⇒ x = {num(x)}।", E)
def e_word(b):
    k, s = R.choice([2, 3, 4, 5]), R.randint(2, 20)
    tot = s * (k + 1)
    b.add(f"একটি সংখ্যা ও তার {k} গুণের যোগফল {tot}। সংখ্যাটি কত?", s, near(s), f"x + {k}x = {tot} ⇒ x = {s}।", E)
def e_sub(b):
    a_, x = R.randint(2, 6), R.randint(1, 9)
    b.add(f"x = {x} হলে {a_}x − {a_} = কত?", a_ * x - a_, near(a_ * x - a_), f"{a_} × {x} − {a_} = {a_ * x - a_}।", E)
def m_frac(b):
    p, q = R.choice([(2, 3), (3, 4), (2, 5), (3, 5), (4, 5), (2, 4), (3, 6), (4, 6)])
    x = math.lcm(p, q) * R.randint(1, 4); s = F(x, p) + F(x, q)
    b.add(f"x/{p} + x/{q} = {fr(s)} হলে x = কত?", x, [x + math.lcm(p, q), x // 2 if x % 2 == 0 and x // 2 != x else x + 1, fr(s * p)] , f"উভয় পক্ষকে {math.lcm(p, q)} দিয়ে গুণ করে x = {x}।", M)
def m_brk(b):
    a_, b_, c_ = R.randint(2, 5), R.randint(1, 6), R.randint(2, 4); x = R.randint(-5, 9)
    rhs = a_ * (x + b_) - c_ * (x - 1)
    b.add(f"{a_}(x + {b_}) − {c_}(x − 1) = {num(rhs)} হলে x = কত?", num(x), [num(w) for w in near(x)], f"বন্ধনী খুলে ({a_} − {c_})x + {a_ * b_ + c_} = {num(rhs)} ⇒ x = {num(x)}।", M)
def m_age(b):
    y, k, t = R.randint(5, 15), R.choice([2, 3, 4]), R.randint(2, 10)
    f = k * y
    b.add(f"পিতার বয়স পুত্রের বয়সের {k} গুণ। তাদের বয়সের যোগফল {f + y} বছর হলে পুত্রের বয়স কত বছর?", y, [f, y + 2, (f + y) // 2], f"x + {k}x = {f + y} ⇒ x = {y}।", M)
def m_consec(b):
    n, k = R.randint(5, 40), R.choice([2, 3, 4])
    s = sum(n + i for i in range(k))
    b.add(f"{k}টি ক্রমিক স্বাভাবিক সংখ্যার যোগফল {s}। ক্ষুদ্রতম সংখ্যাটি কত?", n, [n + 1, n - 1, s // k], f"x + (x + 1) + … = {s} ⇒ x = {n}।", M)
def m_even(b):
    n = 2 * R.randint(3, 25); k = R.choice([2, 3])
    s = sum(n + 2 * i for i in range(k))
    b.add(f"{k}টি ক্রমিক জোড় সংখ্যার যোগফল {s}। বৃহত্তম সংখ্যাটি কত?", n + 2 * (k - 1), [n, n + 2 * k, n + 2 * (k - 1) - 1], f"ক্ষুদ্রতম {n}; বৃহত্তম {n + 2 * (k - 1)}।", M)
def m_digit(b):
    t, u = R.randint(1, 8), R.randint(1, 9)
    if t == u: return
    n = 10 * t + u
    b.add(f"দুই অঙ্কের একটি সংখ্যার অঙ্কদ্বয়ের যোগফল {t + u}। অঙ্ক স্থান বিনিময় করলে সংখ্যাটি {abs(9 * (u - t))} {'বৃদ্ধি' if u > t else 'হ্রাস'} পায়। সংখ্যাটি কত?", n, [10 * u + t, n + 9, n - 9 if n - 9 != 10 * u + t else n + 18], f"দশকের অঙ্ক {t}, এককের অঙ্ক {u} ⇒ {n}।", M)
def m_rect(b):
    w, d = R.randint(3, 20), R.randint(2, 10)
    P = 2 * (2 * w + d)
    b.add(f"একটি আয়তক্ষেত্রের দৈর্ঘ্য প্রস্থ অপেক্ষা {d} মিটার বেশি এবং পরিসীমা {P} মিটার। প্রস্থ কত মিটার?", w, [w + d, P // 4, w + 1], f"2(x + x + {d}) = {P} ⇒ x = {w}।", M)
def m_money(b):
    n5, n10 = R.randint(3, 20), R.randint(3, 20)
    tot = 5 * n5 + 10 * n10; cnt = n5 + n10
    b.add(f"কারো কাছে 5 টাকা ও 10 টাকার মোট {cnt}টি নোট আছে, যার মোট মূল্য {tot} টাকা। 10 টাকার নোট কয়টি?", n10, [n5 if n5 != n10 else n10 + 2, n10 + 1, n10 - 1], f"5(x') + 10x = {tot} ও মোট {cnt} ⇒ 10 টাকার নোট {n10}টি।", M)
def h_fracvar(b):
    a_, b_ = R.randint(1, 6), R.randint(1, 6); k = R.randint(2, 4)
    # (x + a)/(x − b) = k  ⇒ x + a = kx − kb ⇒ x = (a + kb)/(k − 1)
    x = F(a_ + k * b_, k - 1)
    if x.denominator != 1 or x == b_: return
    b.add(f"(x + {a_})/(x − {b_}) = {k} হলে x = কত?", fr(x), [fr(x + 1), fr(F(a_ - k * b_, k - 1)) if F(a_ - k * b_, k - 1) != x else fr(x + 2), fr(x - 1)], f"x + {a_} = {k}x − {k * b_} ⇒ x = {fr(x)}।", H)
def h_mix(b):
    a_, b_ = R.randint(2, 6), R.randint(2, 6); x = R.randint(2, 12)
    # (x − a)/b + (x + 1)/a ... keep integral
    l = a_ * b_; lhs = F(x - a_, b_) + F(x + b_, a_)
    b.add(f"(x − {a_})/{b_} + (x + {b_})/{a_} = {fr(lhs)} হলে x = কত?", x, near(x), f"উভয় পক্ষকে {l} দিয়ে গুণ করে সমাধান x = {x}।", H)
def h_ageplus(b):
    s, k, t = R.randint(5, 15), R.choice([3, 4]), R.randint(3, 10)
    f = k * s
    if (f + t) % (s + t) or (f + t) // (s + t) == k: return
    m = (f + t) // (s + t)
    b.add(f"পিতার বয়স পুত্রের বয়সের {k} গুণ। {t} বছর পর পিতার বয়স পুত্রের বয়সের {m} গুণ হবে। পুত্রের বর্তমান বয়স কত বছর?", s, [s + t, f, s + 2], f"{k}x + {t} = {m}(x + {t}) ⇒ x = {s}।", H)
def h_work(b):
    n, k = R.randint(10, 40), R.choice([2, 3])
    # একটি সংখ্যার 1/k অংশ থেকে ... 
    x = n * k * 2
    s = F(x, k) - F(x, 2 * k)
    b.add(f"কোনো সংখ্যার 1/{k} অংশ থেকে তার 1/{2 * k} অংশ বিয়োগ করলে {fr(s)} হয়। সংখ্যাটি কত?", x, [x // 2, x * 2, x + k], f"x/{k} − x/{2 * k} = x/{2 * k} = {fr(s)} ⇒ x = {x}।", H)
def h_pct(b):
    c, p = R.choice([200, 300, 400, 500, 600, 800]), R.choice([10, 20, 25, 30])
    x = c * 100 // (100 + p)
    if c * 100 % (100 + p): return
    b.add(f"কোনো সংখ্যার সাথে তার {p}% যোগ করলে {c} হয়। সংখ্যাটি কত?", x, [c - c * p // 100, x + 10, c * p // 100], f"x + {p}x/100 = {c} ⇒ x = {x}।", H)
I51 = run('5.1', R, fx51, [e_lin, e_lin2, e_word, e_sub], [m_frac, m_brk, m_age, m_consec, m_even, m_digit, m_rect, m_money], [h_fracvar, h_mix, h_ageplus, h_work, h_pct], caps=(8, 8, 6))

fx52 = [
 ("ax² + bx + c = 0 সমীকরণটি দ্বিঘাত হওয়ার শর্ত কী?", "a ≠ 0", ["b ≠ 0", "c ≠ 0", "a = 0"], "x² এর সহগ শূন্য হলে দ্বিঘাত থাকে না।", E),
 ("একটি দ্বিঘাত সমীকরণের সর্বাধিক কয়টি মূল থাকে?", "2টি", ["1টি", "3টি", "অসংখ্য"], "ঘাত 2।", E),
 ("ab = 0 হলে নিচের কোনটি সত্য?", "a = 0 অথবা b = 0", ["a = 0 এবং b = 0", "a = b", "a = 1"], "শূন্য গুণফল নিয়ম।", E),
 ("x² = 0 সমীকরণের মূল কয়টি ও কী?", "দুটি সমান মূল 0, 0", ["একটি মূল 1", "কোনো মূল নেই", "0 ও 1"], "x·x = 0।", M),
]
def S(rs):
    rs = sorted(set(rs))
    return '{' + ', '.join(num(r) for r in rs) + '}'
def e_sq(b):
    k = R.randint(1, 12)
    b.add(f"x² = {k * k} সমীকরণের সমাধান সেট কোনটি?", S([k, -k]), [S([k]), S([k * k]), S([k, k * k])], f"x = ±{k}।", E)
def e_fac(b):
    r1, r2 = R.sample([v for v in range(-8, 9) if v], 2)
    b.add(f"(x {sg(-r1)} {abs(r1)})(x {sg(-r2)} {abs(r2)}) = 0 সমীকরণের সমাধান সেট কোনটি?", S([r1, r2]), [S([-r1, -r2]), S([r1, -r2]) if r1 != r2 else S([0]), S([-r1, r2])], "প্রতিটি উৎপাদক শূন্য ধরে।", E)
def e_common(b):
    a_ = R.choice([v for v in range(-9, 10) if v not in (0,)])
    b.add(f"x² {sg(-a_)} {abs(a_)}x = 0 সমীকরণের সমাধান সেট কোনটি?", S([0, a_]), [S([a_]), S([0, -a_]), S([1, a_])], f"x(x {sg(-a_)} {abs(a_)}) = 0।", E)
def m_monic(b):
    r1, r2 = R.sample([v for v in range(-9, 10) if v], 2)
    p = pmul(lin([1], -r1), lin([1], -r2))
    b.add(f"{pfmt(p, X)} = 0 সমীকরণের সমাধান সেট কোনটি?", S([r1, r2]), [S([-r1, -r2]), S([r1, -r2]) if r1 != -r2 else S([r1 + 1, r2]), S([-r1, r2]) if r1 != -r2 else S([r1, r2 - 1])], "উৎপাদকে বিশ্লেষণ করে।", M)
def m_root_of(b):
    r1, r2 = R.sample([v for v in range(-7, 8) if v], 2)
    p = pmul(lin([1], -r1), lin([1], -r2))
    b.add(f"নিচের কোনটি {pfmt(p, X)} = 0 সমীকরণের একটি মূল?", num(r1), [num(-r1), num(r1 + r2) if r1 + r2 not in (r1, r2, -r1) else num(r1 * 10), num(r1 * r2) if r1 * r2 not in (r1, r2, -r1) else num(-r1 - 11)], f"x = {num(r1)} বসালে মান 0 হয়।", M)
def m_perfect(b):
    k = R.choice([v for v in range(-9, 10) if v])
    b.add(f"(x {sg(-k)} {abs(k)})² = 0 সমীকরণের মূল কোনটি?", num(k), [num(-k), num(k * k), '0'], f"x = {num(k)} (দুটি সমান মূল)।", M)
def m_word_prod(b):
    n = R.randint(3, 20)
    b.add(f"দুটি ক্রমিক স্বাভাবিক সংখ্যার গুণফল {n * (n + 1)}। ছোট সংখ্যাটি কত?", n, [n + 1, n - 1, n * 2], f"x(x + 1) = {n * (n + 1)} ⇒ x = {n}।", M)
def m_rect_area(b):
    w, d = R.randint(3, 15), R.randint(1, 8)
    A = w * (w + d)
    b.add(f"একটি আয়তক্ষেত্রের দৈর্ঘ্য প্রস্থ অপেক্ষা {d} মি বেশি এবং ক্ষেত্রফল {A} বর্গমিটার। প্রস্থ কত মিটার?", w, [w + d, w + 1, w - 1], f"x(x + {d}) = {A} ⇒ x = {w}।", M)
def m_sqshift(b):
    a_, k = R.randint(1, 6), R.randint(1, 6)
    b.add(f"(x − {a_})² = {k * k} হলে x-এর মান কোনটি?", S([a_ + k, a_ - k]), [S([a_ + k]), S([k - a_, -a_ - k]), S([a_, k])], f"x − {a_} = ±{k}।", M)
def m_sum_sq(b):
    n = R.randint(2, 15)
    b.add(f"কোনো স্বাভাবিক সংখ্যার বর্গ থেকে সংখ্যাটি বিয়োগ করলে {n * n - n} হয়। সংখ্যাটি কত?", n, [n + 1, n - 1, n * n - n], f"x² − x = {n * n - n} ⇒ x = {n}।", M)
def h_nonmonic(b):
    p_, q_ = R.choice([2, 3, 4, 5]), R.choice([v for v in range(-5, 6) if v]); s_ = R.choice([v for v in range(-5, 6) if v])
    if math.gcd(p_, abs(q_)) != 1: return
    poly = pmul(lin([p_], q_), lin([1], -s_)); r1 = F(-q_, p_)
    b.add(f"{pfmt(poly, X)} = 0 সমীকরণের সমাধান সেট কোনটি?", '{' + ', '.join(num(v) for v in sorted({r1, F(s_)})) + '}', ['{' + ', '.join(num(v) for v in sorted({-r1, F(-s_)})) + '}', '{' + ', '.join(num(v) for v in sorted({F(q_, p_), F(s_)})) + '}' if q_ != 0 else '{0}', '{' + ', '.join(num(v) for v in sorted({F(-p_, q_), F(s_)})) + '}'], "মধ্যপদ বিভাজন করে।", H)
def h_recip(b):
    k = R.randint(2, 6)
    # x + 1/x = k + 1/k
    b.add(f"x + 1/x = {fr(F(k * k + 1, k))} হলে x-এর মান কোনটি?", '{' + f"1/{k}, {k}" + '}', ['{' + f"{k}" + '}', '{' + f"−{k}, −1/{k}" + '}', '{' + f"{k}, {k * k + 1}" + '}'], f"x² − {fr(F(k * k + 1, k))}x + 1 = 0 ⇒ x = {k} বা 1/{k}।", H)
def h_radical(b):
    a_, k = R.randint(1, 9), R.randint(2, 7)
    x = k * k - a_
    b.add(f"√(x + {a_}) = {k} হলে x = কত?", num(x), [num(k * k + a_), num(k - a_), num(x + 1)], f"x + {a_} = {k * k} ⇒ x = {num(x)}।", H)
def h_digit2(b):
    t, u = R.randint(1, 9), R.randint(0, 9)
    n = 10 * t + u
    if t * u == 0 or n % (t * u): return
    k = n // (t * u)
    if t + u > 9 or k < 2: return
    b.add(f"দুই অঙ্কের একটি সংখ্যার দশকের অঙ্ক এককের অঙ্কের চেয়ে {t - u} {'বেশি' if t > u else 'কম'}" if t != u else f"দুই অঙ্কের একটি সংখ্যার অঙ্ক দুটি সমান", None, [], '', H) if False else None
    b.add(f"দুই অঙ্কের একটি সংখ্যা তার অঙ্কদ্বয়ের গুণফলের {k} গুণ এবং অঙ্কদ্বয়ের যোগফল {t + u}। নিচের কোনটি সংখ্যাটি হতে পারে?", n, [10 * u + t if 10 * u + t != n else n + 9, n + 1, n - 1], f"{n} = {k} × {t} × {u} এবং {t} + {u} = {t + u}।", H)
def h_age_sq(b):
    s = R.randint(4, 12); k = R.randint(2, 5)
    f = s * s + k
    b.add(f"পিতার বয়স পুত্রের বয়সের বর্গ অপেক্ষা {k} বছর বেশি এবং পিতার বয়স {f} বছর। পুত্রের বয়স কত বছর?", s, [s + 1, s - 1, f - k], f"x² + {k} = {f} ⇒ x = {s}।", H)
I52 = run('5.2', R, fx52, [e_sq, e_fac, e_common], [m_monic, m_root_of, m_perfect, m_word_prod, m_rect_area, m_sqshift, m_sum_sq], [h_nonmonic, h_recip, h_radical, h_digit2, h_age_sq], caps=(10, 9, 6))
save(5, I51 + I52)
