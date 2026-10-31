#!/usr/bin/env python3
"""দশম শ্রেণি সাধারণ গণিত, অধ্যায় 3 (বীজগাণিতিক রাশি): অনুশীলনী 3.1–3.5, প্রতিটিতে 30 সহজ + 50 মধ্যম + 20 কঠিন।
3.1 বর্গের সূত্র · 3.2 ঘনের সূত্র · 3.3 উৎপাদক ও ভাগশেষ উপপাদ্য · 3.4 বাস্তব সমস্যা · 3.5 সরল ও চক্রবৃদ্ধি মুনাফা
সব হিসাব কোডে; সংখ্যা ইংরেজি অঙ্কে। আউটপুট: src/mcq/ch3.json"""
import json, random, pathlib, math, sys
from fractions import Fraction as F
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from mcqlib import Bank, E, M, H, fr, dec, near, pmul, padd, pscale, ppow, lin, pfmt

R = random.Random(2026103103)
XY, AB = ('x', 'y'), ('a', 'b')
def sgn(n): return '+' if n >= 0 else '−'
def lterm(a, b, v=AB):
    """ax + by আকারের লেখা"""
    return pfmt(lin([a, b]), v)

# ====================== 3.1 বর্গের সূত্র ======================
b = Bank('3.1', R)
for q, c, w, e in [
 ("(a + b)² = কত?", "a² + 2ab + b²", ["a² + b²", "a² − 2ab + b²", "a² + ab + b²"], "বর্গের প্রথম সূত্র।"),
 ("(a − b)² = কত?", "a² − 2ab + b²", ["a² + 2ab + b²", "a² − b²", "a² − ab + b²"], "বর্গের দ্বিতীয় সূত্র।"),
 ("a² − b² = কত?", "(a + b)(a − b)", ["(a − b)²", "(a + b)²", "a² + b² − 2ab"], "দুটি বর্গের অন্তর।"),
 ("(a + b)² − (a − b)² = কত?", "4ab", ["2ab", "2(a² + b²)", "0"], "দুটি সূত্র বিয়োগ করলে 4ab থাকে।"),
 ("(a + b)² + (a − b)² = কত?", "2(a² + b²)", ["4ab", "a² + b²", "2ab"], "দুটি সূত্র যোগ করলে 2a² + 2b²।"),
 ("a² + b² = (a + b)² − কত?", "2ab", ["ab", "4ab", "a² b²"], "(a + b)² = a² + b² + 2ab।"),
 ("a² + b² = (a − b)² + কত?", "2ab", ["4ab", "ab", "−2ab"], "(a − b)² = a² + b² − 2ab।"),
 ("ab = কত?", "((a + b)/2)² − ((a − b)/2)²", ["(a + b)² − (a − b)²", "((a − b)/2)² − ((a + b)/2)²", "(a + b)² − 2ab"], "চার দিয়ে ভাগ করা (a + b)² − (a − b)²।"),
 ("(a + b + c)² = কত?", "a² + b² + c² + 2ab + 2bc + 2ca", ["a² + b² + c²", "a² + b² + c² + ab + bc + ca", "a² + b² + c² − 2ab − 2bc − 2ca"], "তিন পদের বর্গ সূত্র।"),
 ("(a − b)² = (a + b)² − কত?", "4ab", ["2ab", "ab", "2(a² + b²)"], "(a + b)² − (a − b)² = 4ab।"),
]: b.add(q, c, w, e, E)

def e1_expand():
    k = R.choice([v for v in range(-9, 10) if v]); p = ppow(lin([1], k), 2)
    b.add(f"(x {sgn(k)} {abs(k)})² = কত?", pfmt(p, ('x',)), [f"x² + {k*k}", pfmt(padd(p, {(1,): -2 * 2 * k}) or {(2,): 1}, ('x',)), pfmt(padd(p, {(1,): -k}), ('x',))], f"x² {sgn(2*k)} 2×{abs(k)}x + {k*k}।", E)
def e1_sum_prod():
    m, n = R.randint(3, 12), R.randint(1, 20)
    v = m * m - 2 * n
    b.add(f"a + b = {m} এবং ab = {n} হলে a² + b² = কত?", v, [m * m + 2 * n, m * m - n, m * m - 4 * n], f"a² + b² = (a + b)² − 2ab = {m*m} − {2*n} = {v}।", E)
def e1_diff_prod():
    m, n = R.randint(1, 10), R.randint(1, 20)
    v = m * m + 2 * n
    b.add(f"a − b = {m} এবং ab = {n} হলে a² + b² = কত?", v, [m * m - 2 * n, m * m + n, m * m + 4 * n], f"a² + b² = (a − b)² + 2ab = {m*m} + {2*n} = {v}।", E)
def e1_numsq():
    base, d = R.choice([(100, R.choice([1, 2, 3, 4, 5, 6, 7, 8])), (100, -R.choice([1, 2, 3, 4])), (50, R.choice([1, 2, 3])), (1000, R.choice([1, 2]))])
    n = base + d; v = n * n
    b.add(f"সূত্রের সাহায্যে {n}² = কত?", v, [base * base + d * d, v + 2 * base, v - 2 * abs(d) * 10], f"({base} {sgn(d)} {abs(d)})² = {base*base} {sgn(d)} {2*base*abs(d)} + {d*d} = {v}।", E)
b.fill(E, 30, [e1_expand, e1_sum_prod, e1_diff_prod, e1_numsq])

def m1_expand2():
    p, q = R.choice([1, 2, 3, 4, 5]), R.choice([1, 2, 3, 4, 5, -1, -2, -3, -4])
    sq = ppow(lin([p, q]), 2)
    wrong1 = padd(pmul(lin([p, 0]), lin([p, 0])), pmul(lin([0, q]), lin([0, q])))
    wrong2 = padd(sq, {(1, 1): -4 * p * q})
    wrong3 = padd(sq, {(1, 1): -p * q})
    b.add(f"({lterm(p, q, XY)})² = কত?", pfmt(sq, XY), [pfmt(wrong1, XY), pfmt(wrong2, XY), pfmt(wrong3, XY)], f"(a + b)² সূত্রে a = {fr(p)}x, b = {fr(q)}y বসিয়ে।", M)
def m1_ab_from():
    s_, d_ = R.randint(4, 15), R.randint(1, 10)
    if (s_ - d_) % 2: return
    ab = F(s_ * s_ - d_ * d_, 4); a2b2 = F(s_ * s_ + d_ * d_, 2)
    if R.random() < .5:
        b.add(f"a + b = {s_} এবং a − b = {d_} হলে ab = কত?", fr(ab), [fr(ab * 2), fr(F(s_ * s_ - d_ * d_)), fr(ab + 1)], f"ab = ((a + b)² − (a − b)²)/4 = ({s_*s_} − {d_*d_})/4 = {fr(ab)}।", M)
    else:
        b.add(f"a + b = {s_} এবং a − b = {d_} হলে a² + b² = কত?", fr(a2b2), [fr(a2b2 * 2), fr(F(s_ * s_ - d_ * d_, 2)), fr(a2b2 + 1)], f"a² + b² = ((a + b)² + (a − b)²)/2 = ({s_*s_} + {d_*d_})/2 = {fr(a2b2)}।", M)
def m1_recip():
    m = R.randint(2, 9)
    if R.random() < .5:
        b.add(f"x + 1/x = {m} হলে x² + 1/x² = কত?", m * m - 2, [m * m + 2, m * m, m * m - 1], f"x² + 1/x² = (x + 1/x)² − 2 = {m*m} − 2 = {m*m-2}।", M)
    else:
        b.add(f"x − 1/x = {m} হলে x² + 1/x² = কত?", m * m + 2, [m * m - 2, m * m, m * m + 1], f"x² + 1/x² = (x − 1/x)² + 2 = {m*m} + 2 = {m*m+2}।", M)
def m1_three():
    s_, t = R.randint(4, 15), R.randint(2, 30)
    v = s_ * s_ - 2 * t
    b.add(f"a + b + c = {s_} এবং ab + bc + ca = {t} হলে a² + b² + c² = কত?", v, [s_ * s_ + 2 * t, s_ * s_ - t, v - 2], f"a² + b² + c² = (a + b + c)² − 2(ab + bc + ca) = {s_*s_} − {2*t} = {v}।", M)
def m1_value():
    a_, b_ = R.randint(-6, 9), R.randint(-6, 9)
    v = (a_ + b_) ** 2
    b.add(f"a = {a_}, b = {b_} হলে a² + 2ab + b² = কত?", v, [a_ * a_ + b_ * b_, (a_ - b_) ** 2 if (a_ - b_) ** 2 != v else v + 2, v + 1], f"a² + 2ab + b² = (a + b)² = ({a_ + b_})² = {v}।", M)
def m1_xpxq():
    p_, q_ = R.choice([v for v in range(-7, 9) if v]), R.choice([v for v in range(-7, 9) if v])
    if p_ == q_: return
    prod = pmul(lin([1], p_), lin([1], q_))
    b.add(f"(x {sgn(p_)} {abs(p_)})(x {sgn(q_)} {abs(q_)}) = কত?", pfmt(prod, ('x',)), [pfmt(padd({(2,): 1}, {(0,): p_ * q_}), ('x',)), pfmt(padd({(2,): 1}, {(1,): p_ * q_}, {(0,): p_ + q_}), ('x',)), pfmt(padd({(2,): 1}, {(1,): -(p_ + q_)}, {(0,): p_ * q_}), ('x',))],
          f"(x + a)(x + b) = x² + (a + b)x + ab; এখানে a + b = {p_ + q_}, ab = {p_ * q_}।", M)
def m1_diffsq_num():
    a_, d = R.choice([51, 52, 63, 75, 87, 99, 101, 105]), R.choice([1, 2, 3, 5])
    a2, b2 = a_ + d, a_ - d
    v = a2 * a2 - b2 * b2
    b.add(f"{a2}² − {b2}² = কত?", v, [v // 2, (a2 - b2) ** 2, v + 2 * d], f"a² − b² = (a + b)(a − b) = {a2 + b2} × {a2 - b2} = {v}।", M)
def m1_perfect():
    k = R.randint(2, 9)
    b.add(f"x² + {2*k}x + কত যোগ করলে পূর্ণবর্গ হবে?", k * k, [2 * k, k, 4 * k], f"x² + {2*k}x + {k*k} = (x + {k})²।", M)
def m1_ab_sq():
    m, n = R.randint(3, 12), R.randint(1, 20)
    v = m * m - 4 * n
    b.add(f"a + b = {m} এবং ab = {n} হলে (a − b)² = কত?", v, [m * m - 2 * n, m * m + 4 * n, m * m - n], f"(a − b)² = (a + b)² − 4ab = {m*m} − {4*n} = {v}।", M)
b.fill(M, 50, [m1_expand2, m1_ab_from, m1_recip, m1_three, m1_value, m1_xpxq, m1_diffsq_num, m1_perfect, m1_ab_sq])

def h1_x4():
    m = R.randint(2, 6); s2 = m * m - 2; v = s2 * s2 - 2
    b.add(f"x + 1/x = {m} হলে x⁴ + 1/x⁴ = কত?", v, [s2 * s2, s2 * s2 + 2, m ** 4 - 2], f"x² + 1/x² = {m*m} − 2 = {s2}; x⁴ + 1/x⁴ = {s2}² − 2 = {v}।", H)
def h1_surd():
    p_, q_ = R.choice([(2, 3), (3, 8), (4, 15), (5, 24), (6, 35)])
    if R.random() < .5:
        b.add(f"x = {p_} + √{q_} হলে x + 1/x = কত?", 2 * p_, [2 * p_ + 1, p_, 2 * p_ - 2], f"1/x = {p_} − √{q_} (কারণ {p_}² − {q_} = 1); যোগফল {2*p_}।", H)
    else:
        v = 4 * p_ * p_ - 2
        b.add(f"x = {p_} + √{q_} হলে x² + 1/x² = কত?", v, [v + 4, 4 * p_ * p_, v - 2], f"x + 1/x = {2*p_}; x² + 1/x² = {2*p_}² − 2 = {v}।", H)
def h1_a4b4():
    m, n = R.randint(3, 8), R.randint(1, 6)
    s2 = m * m - 2 * n; v = s2 * s2 - 2 * n * n
    b.add(f"a + b = {m} এবং ab = {n} হলে a⁴ + b⁴ = কত?", v, [s2 * s2, s2 * s2 + 2 * n * n, v - 2 * n], f"a² + b² = {s2}; a⁴ + b⁴ = (a² + b²)² − 2(ab)² = {s2*s2} − {2*n*n} = {v}।", H)
def h1_three_back():
    s_, q_ = R.randint(5, 12), R.randint(20, 80)
    if (s_ * s_ - q_) % 2 or s_ * s_ <= q_: return
    v = (s_ * s_ - q_) // 2
    b.add(f"a + b + c = {s_} এবং a² + b² + c² = {q_} হলে ab + bc + ca = কত?", v, [s_ * s_ - q_, v + 1, (s_ * s_ + q_) // 2], f"ab + bc + ca = ((a + b + c)² − (a² + b² + c²))/2 = ({s_*s_} − {q_})/2 = {v}।", H)
def h1_ab_from_sum():
    a_, b_ = R.randint(2, 9), R.randint(1, 8)
    s_, sq = a_ + b_, a_ * a_ + b_ * b_
    v = F(s_ * s_ - sq, 2)
    b.add(f"a + b = {s_} এবং a² + b² = {sq} হলে ab = কত?", fr(v), [fr(v * 2), fr(v + 1), fr(F(s_ * s_ + sq, 2))], f"2ab = (a + b)² − (a² + b²) = {s_*s_} − {sq}; ab = {fr(v)}।", H)
b.fill(H, 20, [h1_x4, h1_surd, h1_a4b4, h1_three_back, h1_ab_from_sum], cap=5)
B31 = b.final()

# ====================== 3.2 ঘনের সূত্র ======================
b = Bank('3.2', R)
for q, c, w, e in [
 ("(a + b)³ = কত?", "a³ + 3a²b + 3ab² + b³", ["a³ + b³", "a³ + 3ab + b³", "a³ − 3a²b + 3ab² − b³"], "ঘনের প্রথম সূত্র।"),
 ("(a − b)³ = কত?", "a³ − 3a²b + 3ab² − b³", ["a³ − b³", "a³ + 3a²b + 3ab² + b³", "a³ − 3ab − b³"], "ঘনের দ্বিতীয় সূত্র।"),
 ("a³ + b³ = কত?", "(a + b)(a² − ab + b²)", ["(a + b)(a² + ab + b²)", "(a − b)(a² + ab + b²)", "(a + b)³"], "দুটি ঘনের যোগফল।"),
 ("a³ − b³ = কত?", "(a − b)(a² + ab + b²)", ["(a − b)(a² − ab + b²)", "(a + b)(a² − ab + b²)", "(a − b)³"], "দুটি ঘনের অন্তর।"),
 ("a³ + b³ = (a + b)³ − কত?", "3ab(a + b)", ["3ab", "ab(a + b)", "3a²b²"], "(a + b)³ = a³ + b³ + 3ab(a + b)।"),
 ("a³ − b³ = (a − b)³ + কত?", "3ab(a − b)", ["3ab(a + b)", "3ab", "ab(a − b)"], "(a − b)³ = a³ − b³ − 3ab(a − b)।"),
 ("a + b + c = 0 হলে a³ + b³ + c³ = কত?", "3abc", ["0", "abc", "a + b + c"], "a³ + b³ + c³ − 3abc = (a + b + c)(…) = 0।"),
 ("(a + b)³ − (a − b)³ = কত?", "6a²b + 2b³", ["2a³ + 6ab²", "6ab²", "2b³"], "দুটি সূত্র বিয়োগ করে।"),
 ("(a + b)³ + (a − b)³ = কত?", "2a³ + 6ab²", ["6a²b + 2b³", "2a³", "2a³ + 2b³"], "দুটি সূত্র যোগ করে।"),
]: b.add(q, c, w, e, E)
def e2_expand():
    k = R.choice([v for v in range(-6, 7) if v]); p = ppow(lin([1], k), 3)
    b.add(f"(x {sgn(k)} {abs(k)})³ = কত?", pfmt(p, ('x',)), [pfmt({(3,): 1, (0,): k ** 3}, ('x',)), pfmt(padd(p, {(2,): -2 * 3 * k}), ('x',)), pfmt(padd(p, {(1,): -2 * 3 * k * k}), ('x',))], f"(a + b)³ সূত্রে a = x, b = {k}।", E)
def e2_sum():
    m, n = R.randint(2, 8), R.randint(1, 12)
    v = m ** 3 - 3 * n * m
    b.add(f"a + b = {m} এবং ab = {n} হলে a³ + b³ = কত?", v, [m ** 3 + 3 * n * m, m ** 3 - n * m, m ** 3 - 3 * n], f"a³ + b³ = (a + b)³ − 3ab(a + b) = {m**3} − {3*n*m} = {v}।", E)
def e2_numcube():
    base, d = R.choice([(10, 1), (10, 2), (10, -1), (20, 1), (100, 1), (100, -1), (10, 3), (20, -1)])
    n = base + d; v = n ** 3
    b.add(f"সূত্রের সাহায্যে {n}³ = কত?", v, [base ** 3 + d ** 3, v + 3 * base * d * d, v - base * base], f"({base} {sgn(d)} {abs(d)})³ সূত্রে বিস্তার করে {v}।", E)
def e2_value():
    a_, b_ = R.randint(1, 6), R.randint(1, 6)
    v = a_ ** 3 + b_ ** 3
    b.add(f"a = {a_}, b = {b_} হলে a³ + b³ = কত?", v, [(a_ + b_) ** 3, v + 1, abs(a_ ** 3 - b_ ** 3) if abs(a_ ** 3 - b_ ** 3) != v else v + 2], f"{a_}³ + {b_}³ = {a_**3} + {b_**3} = {v}।", E)
b.fill(E, 30, [e2_expand, e2_sum, e2_numcube, e2_value])
def m2_diff():
    m, n = R.randint(1, 8), R.randint(1, 12)
    v = m ** 3 + 3 * n * m
    b.add(f"a − b = {m} এবং ab = {n} হলে a³ − b³ = কত?", v, [m ** 3 - 3 * n * m, m ** 3 + n * m, m ** 3 + 3 * n], f"a³ − b³ = (a − b)³ + 3ab(a − b) = {m**3} + {3*n*m} = {v}।", M)
def m2_recip():
    m = R.randint(2, 7)
    if R.random() < .5:
        v = m ** 3 - 3 * m
        b.add(f"x + 1/x = {m} হলে x³ + 1/x³ = কত?", v, [m ** 3 + 3 * m, m ** 3, m ** 3 - m], f"x³ + 1/x³ = (x + 1/x)³ − 3(x + 1/x) = {m**3} − {3*m} = {v}।", M)
    else:
        v = m ** 3 + 3 * m
        b.add(f"x − 1/x = {m} হলে x³ − 1/x³ = কত?", v, [m ** 3 - 3 * m, m ** 3, m ** 3 + m], f"x³ − 1/x³ = (x − 1/x)³ + 3(x − 1/x) = {m**3} + {3*m} = {v}।", M)
def m2_expand2():
    p, q = R.choice([1, 2, 3]), R.choice([1, 2, 3, -1, -2])
    cube = ppow(lin([p, q]), 3)
    b.add(f"({lterm(p, q, XY)})³ = কত?", pfmt(cube, XY), [pfmt(padd(pmul(lin([p, 0]), ppow(lin([p, 0]), 2)), ppow(lin([0, q]), 3)), XY), pfmt(padd(cube, {(2, 1): -2 * 3 * p * p * q}), XY), pfmt(padd(cube, {(1, 2): -2 * 3 * p * q * q}), XY)], f"(a + b)³ সূত্রে a = {p}x, b = {q}y।", M)
def m2_coef():
    p, q = R.choice([1, 2, 3, 4]), R.choice([1, 2, 3, -1, -2])
    c = 3 * p * p * q
    b.add(f"({lterm(p, q, XY)})³ এর বিস্তৃতিতে x²y এর সহগ কত?", c, [p * p * q, 3 * p * q * q, c + 3], f"3 × ({p})² × ({q}) = {c}।", M)
def m2_zero_sum():
    a_, b_ = R.randint(1, 7), R.randint(1, 7); c_ = -(a_ + b_)
    v = 3 * a_ * b_ * c_
    b.add(f"a = {a_}, b = {b_}, c = {c_} হলে a³ + b³ + c³ = কত?", v, [0, a_ * b_ * c_, -v], f"a + b + c = 0, তাই a³ + b³ + c³ = 3abc = {v}।", M)
def m2_factor_val():
    a_, b_ = R.randint(2, 9), R.randint(1, 8)
    if a_ == b_: return
    v = (a_ + b_) * (a_ * a_ - a_ * b_ + b_ * b_)
    b.add(f"(a + b)(a² − ab + b²) এর মান কত, যখন a = {a_}, b = {b_}?", v, [(a_ + b_) ** 3, v - 2 * a_ * b_ * (a_ + b_), abs(a_ ** 3 - b_ ** 3)], f"রাশিটি a³ + b³ = {a_**3} + {b_**3} = {v}।", M)
def m2_simplify():
    k = R.randint(2, 6)
    v = 6 * k * k + 2  # (k+1)^3 - (k-1)^3
    b.add(f"({k} + 1)³ − ({k} − 1)³ = কত?", v, [2, 6 * k * k, v + 6], f"(a + b)³ − (a − b)³ = 6a²b + 2b³; a = {k}, b = 1 ⇒ {v}।", M)
def m2_a3_from():
    a_, b_ = R.randint(2, 7), R.randint(1, 6)
    s_, p_ = a_ + b_, a_ * b_
    v = s_ ** 3 - 3 * p_ * s_
    v = s_ * s_ - 3 * p_
    b.add(f"a + b = {s_} এবং ab = {p_} হলে a² − ab + b² = কত?", v, [s_ * s_ - p_, s_ * s_ - 2 * p_, s_ * s_ + 3 * p_], f"a² − ab + b² = (a + b)² − 3ab = {s_*s_} − {3*p_} = {v}।", M)
def m2_cube_root():
    k = R.randint(2, 6)
    p = ppow(lin([1], k), 3)
    b.add(f"{pfmt(p, ('x',))} কোন রাশির ঘন?", f"x + {k}", [f"x − {k}", f"x + {k*k}", f"x + {3*k}"], f"(x + {k})³ = {pfmt(p, ('x',))}।", M)
b.fill(M, 50, [m2_diff, m2_recip, m2_expand2, m2_coef, m2_zero_sum, m2_factor_val, m2_simplify, m2_a3_from, m2_cube_root])
def h2_x6():
    m = R.randint(2, 5); t = m ** 3 - 3 * m; v = t * t - 2
    b.add(f"x + 1/x = {m} হলে x⁶ + 1/x⁶ = কত?", v, [t * t, t * t + 2, m ** 6 - 2], f"x³ + 1/x³ = {t}; x⁶ + 1/x⁶ = {t}² − 2 = {v}।", H)
def h2_surd():
    p_, q_ = R.choice([(2, 3), (3, 8), (4, 15), (5, 24)])
    s_ = 2 * p_; v = s_ ** 3 - 3 * s_
    b.add(f"x = {p_} + √{q_} হলে x³ + 1/x³ = কত?", v, [s_ ** 3, s_ ** 3 + 3 * s_, v - 2], f"x + 1/x = {s_}; x³ + 1/x³ = {s_}³ − 3×{s_} = {v}।", H)
def h2_ab_back():
    a_, b_ = R.randint(2, 8), R.randint(1, 7)
    s_, cu = a_ + b_, a_ ** 3 + b_ ** 3
    v = F(s_ ** 3 - cu, 3 * s_)
    b.add(f"a + b = {s_} এবং a³ + b³ = {cu} হলে ab = কত?", fr(v), [fr(v + 1), fr(F(s_ ** 3 - cu, s_)), fr(F(s_ ** 3 + cu, 3 * s_))], f"3ab(a + b) = (a + b)³ − (a³ + b³) = {s_**3 - cu}; ab = {fr(v)}।", H)
def h2_ratio():
    b.add("a + b + c = 0 হলে a²/bc + b²/ca + c²/ab = কত?", 3, [0, 1, "abc"], "রাশি = (a³ + b³ + c³)/abc = 3abc/abc = 3।", H)
    k = R.randint(2, 9)
    b.add(f"a + b + c = 0 এবং abc = {k} হলে a³ + b³ + c³ = কত?", 3 * k, [0, k, 9 * k], f"a³ + b³ + c³ = 3abc = {3*k}।", H)
def h2_diff_back():
    a_, b_ = R.randint(3, 9), R.randint(1, 6)
    if a_ <= b_: return
    d_, cu = a_ - b_, a_ ** 3 - b_ ** 3
    v = F(cu - d_ ** 3, 3 * d_)
    b.add(f"a − b = {d_} এবং a³ − b³ = {cu} হলে ab = কত?", fr(v), [fr(v + 1), fr(F(cu + d_ ** 3, 3 * d_)), fr(F(cu - d_ ** 3, d_))], f"3ab(a − b) = (a³ − b³) − (a − b)³ = {cu - d_**3}; ab = {fr(v)}।", H)
b.fill(H, 20, [h2_x6, h2_surd, h2_ab_back, h2_ratio, h2_diff_back], cap=6)
B32 = b.final()

# ================ 3.3/3.4/3.5 টেমপ্লেট (ব্যাংক নিচে সাজানো) ================
def fac(r):  # (x − r)
    return f"(x {sgn(-r)} {abs(r)})" if r else "x"
FIX33 = [
 ("P(x)-কে (x − a) দ্বারা ভাগ করলে ভাগশেষ কত হয়?", "P(a)", ["P(−a)", "P(0)", "a"], "ভাগশেষ উপপাদ্য।"),
 ("P(a) = 0 হলে নিচের কোনটি P(x)-এর একটি উৎপাদক?", "x − a", ["x + a", "a", "x"], "উৎপাদক উপপাদ্য।"),
 ("P(x)-কে (x + a) দ্বারা ভাগ করলে ভাগশেষ কত?", "P(−a)", ["P(a)", "P(0)", "−a"], "x + a = x − (−a)।"),
 ("P(x)-কে (ax − b) দ্বারা ভাগ করলে ভাগশেষ কত?", "P(b/a)", ["P(a/b)", "P(−b/a)", "P(b)"], "ax − b = 0 ⇒ x = b/a।"),
 ("x⁴ + x² + 1 এর উৎপাদক কোনটি?", "(x² + x + 1)(x² − x + 1)", ["(x² + 1)²", "(x² + x − 1)(x² − x − 1)", "(x² + 1)(x² − 1)"], "(x² + 1)² − x² আকারে লিখে।"),
 ("a⁴ + 4 এর উৎপাদক কোনটি?", "(a² + 2a + 2)(a² − 2a + 2)", ["(a² + 2)²", "(a² + 2)(a² − 2)", "(a + 2)(a³ + 2)"], "(a² + 2)² − (2a)² আকারে লিখে।"),
]
def e3_diffsq():
    k = R.randint(1, 12)
    b.add(f"x² − {k*k} এর উৎপাদক কোনটি?", f"(x + {k})(x − {k})", [f"(x − {k})²", f"(x + {k})²", f"(x − {k*k})(x + 1)"], "a² − b² = (a + b)(a − b)।", E)
def e3_monic():
    r1, r2 = R.sample([v for v in range(-7, 8) if v], 2)
    if r1 == -r2: return
    p = pmul(lin([1], -r1), lin([1], -r2))
    b.add(f"{pfmt(p, ('x',))} এর উৎপাদক কোনটি?", f"{fac(r1)}{fac(r2)}", [f"{fac(-r1)}{fac(-r2)}", f"{fac(r1)}{fac(-r2)}" if r1 != -r2 else f"{fac(r1 + 1)}{fac(r2)}", f"{fac(r1 * r2)}(x − 1)" if r1 * r2 != 1 else f"{fac(r1 + 2)}{fac(r2)}"], f"গুণফল {r1 * r2} ও যোগফল {r1 + r2} এমন দুটি সংখ্যা {r1}, {r2}।", E)
def e3_common():
    a_, k = R.randint(2, 6), R.randint(2, 9)
    b.add(f"{a_}x² + {a_*k}x এর উৎপাদক কোনটি?", f"{a_}x(x + {k})", [f"{a_}(x² + {k})", f"x({a_}x + {k})", f"{a_}x(x + {a_*k})"], f"সাধারণ উৎপাদক {a_}x বের করে।", E)
def e3_rem_simple():
    a_, c_ = R.choice([-4, -3, -2, -1, 1, 2, 3, 4, 5]), R.choice([v for v in range(-8, 9) if v])
    v = a_ * a_ + c_
    b.add(f"x² {sgn(c_)} {abs(c_)} কে (x {sgn(-a_)} {abs(a_)}) দ্বারা ভাগ করলে ভাগশেষ কত?", v, near(v), f"ভাগশেষ = P({a_}) = {a_*a_} {sgn(c_)} {abs(c_)} = {v}।", E)
def m3_split():
    p_, q_, r_, s_ = R.choice([2, 3, 4, 5]), R.choice([v for v in range(-5, 6) if v]), 1, R.choice([v for v in range(-5, 6) if v])
    if math.gcd(p_, abs(q_)) != 1: return
    poly = pmul(lin([p_], q_), lin([1], s_))
    ans = f"({pfmt(lin([p_], q_), ('x',))})({pfmt(lin([1], s_), ('x',))})"
    w1 = f"({pfmt(lin([p_], -q_), ('x',))})({pfmt(lin([1], -s_), ('x',))})"
    w2 = f"({pfmt(lin([p_], s_), ('x',))})({pfmt(lin([1], q_), ('x',))})" if s_ != q_ else f"({pfmt(lin([p_], q_ + 1), ('x',))})({pfmt(lin([1], s_), ('x',))})"
    w3 = f"({pfmt(lin([p_], -q_), ('x',))})({pfmt(lin([1], s_), ('x',))})"
    b.add(f"{pfmt(poly, ('x',))} এর উৎপাদক কোনটি?", ans, [w1, w2, w3], "মধ্যপদ বিভাজন করে।", M)
def m3_cubes():
    k = R.randint(1, 5); kx = 'x' if k == 1 else f'{k}x'
    if R.random() < .5:
        b.add(f"x³ + {k**3} এর উৎপাদক কোনটি?", f"(x + {k})(x² − {kx} + {k*k})", [f"(x + {k})(x² + {kx} + {k*k})", f"(x − {k})(x² + {kx} + {k*k})", f"(x + {k})³"], "a³ + b³ = (a + b)(a² − ab + b²)।", M)
    else:
        b.add(f"x³ − {k**3} এর উৎপাদক কোনটি?", f"(x − {k})(x² + {kx} + {k*k})", [f"(x − {k})(x² − {kx} + {k*k})", f"(x + {k})(x² − {kx} + {k*k})", f"(x − {k})³"], "a³ − b³ = (a − b)(a² + ab + b²)।", M)
def m3_rem_cubic():
    co = [R.randint(-3, 3) for _ in range(3)]; a_ = R.choice([-2, -1, 1, 2, 3])
    P = lambda x: x ** 3 + co[0] * x * x + co[1] * x + co[2]
    poly = pfmt({(3,): 1, (2,): co[0], (1,): co[1], (0,): co[2]} if True else {}, ('x',))
    poly = pfmt({k: v for k, v in {(3,): 1, (2,): co[0], (1,): co[1], (0,): co[2]}.items() if v}, ('x',))
    v = P(a_)
    b.add(f"{poly} কে (x {sgn(-a_)} {abs(a_)}) দ্বারা ভাগ করলে ভাগশেষ কত?", v, [P(-a_) if P(-a_) != v else v + 2, v + 1, v - 1], f"ভাগশেষ = P({a_}) = {v}।", M)
def m3_find_k():
    a_, c_ = R.choice([-3, -2, -1, 1, 2, 3]), R.choice([v for v in range(-8, 9) if v])
    # x² + kx + c ; P(a)=0 ⇒ k = −(a² + c)/a
    k = F(-(a_ * a_ + c_), a_)
    if k.denominator != 1: return
    b.add(f"(x {sgn(-a_)} {abs(a_)}) রাশিটি x² + kx {sgn(c_)} {abs(c_)} এর উৎপাদক হলে k = কত?", fr(k), [fr(-k) if k else '1', fr(k + 1), fr(k - 2)], f"P({a_}) = 0 ⇒ {a_*a_} + ({a_})k {sgn(c_)} {abs(c_)} = 0 ⇒ k = {fr(k)}।", M)
def m3_group():
    a_, b_ = R.randint(2, 7), R.randint(2, 7)
    if a_ == b_: return
    b.add(f"x² + {a_}x + {b_}x + {a_*b_} এর উৎপাদক কোনটি?", f"(x + {a_})(x + {b_})", [f"(x + {a_})(x − {b_})", f"(x − {a_})(x − {b_})", f"(x + {a_*b_})(x + 1)"], "জোড়ায় জোড়ায় সাজিয়ে সাধারণ উৎপাদক বের করে।", M)
def m3_sq_trinom():
    k = R.randint(2, 9); s_ = R.choice([1, -1])
    p = ppow(lin([1], s_ * k), 2)
    b.add(f"{pfmt(p, ('x',))} এর উৎপাদক কোনটি?", f"(x {sgn(s_*k)} {k})²", [f"(x {sgn(-s_*k)} {k})²", f"(x + {k})(x − {k})", f"(x {sgn(s_*k)} {k*k})(x {sgn(s_)} 1)"], "পূর্ণবর্গ রাশি।", M)
def m3_four():
    a_, c_ = R.randint(1, 5), R.randint(1, 5)
    b.add(f"a² − b² − {2*c_}b − {c_*c_} এর উৎপাদক কোনটি?", f"(a + b + {c_})(a − b − {c_})", [f"(a + b − {c_})(a − b + {c_})", f"(a − b − {c_})²", f"(a + b + {c_})²"], f"a² − (b + {c_})² আকারে লিখে।", M)
def m3_is_factor():
    r1, r2 = R.sample([v for v in range(-5, 6) if v], 2)
    p = pmul(lin([1], -r1), lin([1], -r2))
    wrong = [f"x {sgn(r1)} {abs(r1)}" if r1 != -r2 else f"x {sgn(-r1-1)} {abs(r1+1)}", f"x {sgn(-r1*r2)} {abs(r1*r2)}" if r1 * r2 not in (r1, r2) else "x + 10", f"x {sgn(-(r1+r2))} {abs(r1+r2)}" if r1 + r2 not in (r1, r2, 0) else "x − 11"]
    b.add(f"নিচের কোনটি {pfmt(p, ('x',))} এর একটি উৎপাদক?", f"x {sgn(-r1)} {abs(r1)}", wrong, f"P({r1}) = 0, তাই (x {sgn(-r1)} {abs(r1)}) উৎপাদক।", M)
def h3_cubic():
    rs = R.sample([v for v in range(-4, 5) if v], 3)
    p = pmul(pmul(lin([1], -rs[0]), lin([1], -rs[1])), lin([1], -rs[2]))
    ans = ''.join(fac(r) for r in sorted(rs))
    b.add(f"{pfmt(p, ('x',))} এর উৎপাদক কোনটি?", ans, [''.join(fac(-r) for r in sorted(rs)), ''.join(fac(r) for r in sorted([rs[0], rs[1], -rs[2]])), ''.join(fac(r) for r in sorted([-rs[0], rs[1], rs[2]]))], f"P({rs[0]}) = 0 থেকে শুরু করে ভাগশেষ উপপাদ্যের সাহায্যে।", H)
def h3_cubic_k():
    a_ = R.choice([-2, -1, 1, 2]); c1, c2 = R.randint(-4, 4), R.randint(-4, 4)
    # x³ + c1 x² + c2 x + k ; P(a)=0 ⇒ k = −(a³ + c1 a² + c2 a)
    k = -(a_ ** 3 + c1 * a_ * a_ + c2 * a_)
    head = pfmt({kk: vv for kk, vv in {(3,): 1, (2,): c1, (1,): c2}.items() if vv}, ('x',))
    b.add(f"(x {sgn(-a_)} {abs(a_)}) রাশিটি {head} + k এর উৎপাদক হলে k = কত?", k, near(k), f"P({a_}) = 0 ⇒ k = {k}।", H)
def h3_rem_linear():
    p_, q_ = R.choice([(2, 1), (3, 1), (2, 3), (3, 2)])
    co = [R.randint(-4, 5) for _ in range(3)]
    x0 = F(q_, p_); v = co[0] * x0 * x0 + co[1] * x0 + co[2]
    if co[0] == 0: return
    poly = pfmt({k: vv for k, vv in {(2,): co[0], (1,): co[1], (0,): co[2]}.items() if vv}, ('x',))
    b.add(f"{poly} কে ({p_}x − {q_}) দ্বারা ভাগ করলে ভাগশেষ কত?", fr(v), [fr(co[0] * x0 ** -2 + co[1] / x0 + co[2]) if x0 else '0', fr(v + 1), fr(co[0] * q_ * q_ + co[1] * q_ + co[2])], f"x = {fr(x0)} বসিয়ে ভাগশেষ {fr(v)}।", H)
def h3_complex():
    k = R.randint(1, 4)
    b.add(f"x² − y² + {2*k}y − {k*k} এর উৎপাদক কোনটি?", f"(x + y − {k})(x − y + {k})", [f"(x + y + {k})(x − y − {k})", f"(x − y + {k})²", f"(x + y − {k})²"], f"x² − (y − {k})² আকারে লিখে।", H)
def h3_sum_cubes_poly():
    k = R.randint(2, 4)
    b.add(f"8x³ + {k**3} এর উৎপাদক কোনটি?", f"(2x + {k})(4x² − {2*k}x + {k*k})", [f"(2x + {k})(4x² + {2*k}x + {k*k})", f"(2x − {k})(4x² + {2*k}x + {k*k})", f"(8x + {k})(x² − {k}x + {k*k})"], f"(2x)³ + {k}³ = (2x + {k})((2x)² − 2x·{k} + {k}²)।", H)

# ---- বাস্তব সমস্যা ----
FIX34 = [
 ("কেউ একটি কাজ n দিনে করলে 1 দিনে কাজের কত অংশ করে?", "1/n", ["n", "n − 1", "1 − n"], "সম্পূর্ণ কাজকে 1 ধরে।"),
 ("দূরত্ব, বেগ ও সময়ের সম্পর্ক কোনটি?", "দূরত্ব = বেগ × সময়", ["বেগ = দূরত্ব × সময়", "সময় = বেগ × দূরত্ব", "দূরত্ব = বেগ ÷ সময়"], "d = vt।"),
 ("স্রোতের অনুকূলে নৌকার কার্যকর বেগ কত?", "নৌকার বেগ + স্রোতের বেগ", ["নৌকার বেগ − স্রোতের বেগ", "স্রোতের বেগ", "নৌকার বেগ × স্রোতের বেগ"], "স্রোত নৌকাকে সাহায্য করে।"),
 ("স্রোতের প্রতিকূলে নৌকার কার্যকর বেগ কত?", "নৌকার বেগ − স্রোতের বেগ", ["নৌকার বেগ + স্রোতের বেগ", "স্রোতের বেগ − নৌকার বেগ", "নৌকার বেগ"], "স্রোত নৌকাকে বাধা দেয়।"),
 ("লাভ = কত?", "বিক্রয়মূল্য − ক্রয়মূল্য", ["ক্রয়মূল্য − বিক্রয়মূল্য", "বিক্রয়মূল্য + ক্রয়মূল্য", "বিক্রয়মূল্য × ক্রয়মূল্য"], "বিক্রয়মূল্য বেশি হলে লাভ।"),
 ("লাভের হার সাধারণত কিসের উপর হিসাব করা হয়?", "ক্রয়মূল্যের উপর", ["বিক্রয়মূল্যের উপর", "লাভের উপর", "মোট টাকার উপর"], "লাভ% = লাভ/ক্রয়মূল্য × 100।"),
]
def e4_dist():
    v, t = R.randint(20, 80), R.randint(2, 6)
    b.add(f"ঘণ্টায় {v} কিমি বেগে {t} ঘণ্টায় কত কিমি পথ যাওয়া যাবে?", v * t, [v + t, v * t + v, v * (t - 1)], f"দূরত্ব = {v} × {t} = {v*t} কিমি।", E)
def e4_time():
    v, t = R.randint(20, 60), R.randint(2, 6); d = v * t
    b.add(f"ঘণ্টায় {v} কিমি বেগে {d} কিমি যেতে কত ঘণ্টা লাগবে?", t, near(t), f"সময় = {d} ÷ {v} = {t} ঘণ্টা।", E)
def e4_pct():
    p, n = R.choice([5, 10, 12, 15, 20, 25, 40]), R.choice([200, 300, 400, 500, 600, 800, 1200])
    v = p * n // 100
    b.add(f"{n} এর {p}% = কত?", v, [v * 2, p * n // 10 if p * n // 10 != v else v + 10, v + p], f"{n} × {p}/100 = {v}।", E)
def e4_profit():
    c, s = R.choice([200, 400, 500, 800, 1000]), R.choice([5, 10, 20, 25])
    sp = c + c * s // 100
    b.add(f"একটি জিনিস {c} টাকায় কিনে {sp} টাকায় বিক্রি করলে লাভের হার কত?", f"{s}%", [f"{s + 5}%", f"{(sp - c) * 100 // sp}%" if (sp - c) * 100 // sp != s else f"{s - 2}%", f"{sp - c}%"], f"লাভ {sp - c} টাকা; লাভের হার = {sp - c}/{c} × 100 = {s}%।", E)
def e4_oneday():
    n = R.randint(4, 20)
    b.add(f"রহিম একটি কাজ {n} দিনে করতে পারে। {n//2 if n%2==0 else 2} দিনে সে কাজের কত অংশ করবে?", dec(F(n // 2 if n % 2 == 0 else 2, n)), [dec(F(1, n)), dec(F(n // 2 if n % 2 == 0 else 2, n) + F(1, n)), dec(1 - F(n // 2 if n % 2 == 0 else 2, n)) if 1 - F(n // 2 if n % 2 == 0 else 2, n) != F(n // 2 if n % 2 == 0 else 2, n) else dec(F(1, 3))], "প্রতিদিন 1/n অংশ।", E)
WORK = [(12, 24, 8), (10, 15, 6), (20, 30, 12), (6, 12, 4), (12, 36, 9), (18, 36, 12), (15, 30, 10), (4, 12, 3), (30, 60, 20), (10, 40, 8), (6, 3, 2), (20, 5, 4), (24, 8, 6)]
def m4_together():
    a_, b_, t = R.choice(WORK)
    b.add(f"ক একটি কাজ {a_} দিনে এবং খ {b_} দিনে করতে পারে। দুজনে একসাথে কাজটি কত দিনে করবে?", t, [(a_ + b_) // 2, a_ + b_, t + 2], f"1 দিনে 1/{a_} + 1/{b_} = 1/{t} অংশ; তাই {t} দিন।", M)
def m4_pipe():
    a_, b_ = R.choice([(4, 6), (3, 6), (6, 12), (5, 10), (4, 12), (8, 12), (10, 15)])
    t = F(a_ * b_, b_ - a_)
    b.add(f"একটি নল একটি খালি চৌবাচ্চা {a_} ঘণ্টায় পূর্ণ করে, আরেকটি নল পূর্ণ চৌবাচ্চা {b_} ঘণ্টায় খালি করে। দুটি নল একসাথে খুললে চৌবাচ্চা কত ঘণ্টায় পূর্ণ হবে?", dec(t), [dec(F(a_ * b_, a_ + b_)), b_ - a_, dec(t + 2)], f"1 ঘণ্টায় 1/{a_} − 1/{b_} = 1/{dec(t)}; তাই {dec(t)} ঘণ্টা।", M)
def m4_boat():
    v, s = R.randint(8, 20), R.randint(1, 5)
    if R.random() < .5:
        b.add(f"স্থির পানিতে নৌকার বেগ ঘণ্টায় {v} কিমি এবং স্রোতের বেগ ঘণ্টায় {s} কিমি। স্রোতের প্রতিকূলে নৌকার বেগ কত?", f"{v - s} কিমি/ঘণ্টা", [f"{v + s} কিমি/ঘণ্টা", f"{v} কিমি/ঘণ্টা", f"{s} কিমি/ঘণ্টা"], f"{v} − {s} = {v - s}।", M)
    else:
        d = (v + s) * R.randint(2, 4)
        b.add(f"স্থির পানিতে নৌকার বেগ ঘণ্টায় {v} কিমি এবং স্রোতের বেগ ঘণ্টায় {s} কিমি। স্রোতের অনুকূলে {d} কিমি যেতে কত ঘণ্টা লাগবে?", d // (v + s), [dec(F(d, v - s)), dec(F(d, v)), d // (v + s) + 1], f"অনুকূলে বেগ {v + s}; সময় {d} ÷ {v + s} = {d // (v + s)} ঘণ্টা।", M)
def m4_train():
    L, v = R.choice([100, 150, 200, 250, 300]), R.choice([36, 54, 72, 90])
    ms = F(v * 1000, 3600); t = F(L) / ms
    b.add(f"{L} মিটার লম্বা একটি ট্রেন ঘণ্টায় {v} কিমি বেগে চলে। একটি খুঁটি অতিক্রম করতে কত সেকেন্ড লাগবে?", dec(t), [dec(t * 2), dec(F(L, v)), dec(t + 5)], f"{v} কিমি/ঘণ্টা = {dec(ms)} মি/সে; সময় {L} ÷ {dec(ms)} = {dec(t)} সেকেন্ড।", M)
def m4_cost():
    c, s = R.choice([400, 500, 600, 800, 1000, 1200]), R.choice([10, 20, 25])
    sp = c + c * s // 100
    b.add(f"একটি জিনিস {sp} টাকায় বিক্রি করলে {s}% লাভ হয়। জিনিসটির ক্রয়মূল্য কত টাকা?", c, [sp - sp * s // 100, sp - s, c + 50], f"ক্রয়মূল্য = {sp} × 100/{100 + s} = {c} টাকা।", M)
def m4_loss():
    c, s = R.choice([400, 500, 600, 800, 1000]), R.choice([5, 10, 20])
    sp = c - c * s // 100
    b.add(f"{c} টাকার একটি জিনিস {s}% ক্ষতিতে বিক্রি করলে বিক্রয়মূল্য কত টাকা?", sp, [c + c * s // 100, c - s, sp - 20], f"{c} − {c}×{s}/100 = {sp} টাকা।", M)
def m4_finish():
    a_, b_, t = R.choice([(12, 24, 8), (10, 15, 6), (20, 30, 12), (15, 30, 10), (18, 36, 12)])
    k = R.randint(1, a_ // 3)
    rem = 1 - F(k, a_); days = rem * b_
    b.add(f"ক একটি কাজ {a_} দিনে, খ {b_} দিনে করতে পারে। ক {k} দিন কাজ করে চলে গেলে বাকি কাজ খ কত দিনে শেষ করবে?", dec(days), [dec(days + 1), b_ - k, dec(F(b_ * k, a_))], f"ক করেছে {dec(F(k, a_))} অংশ; বাকি {dec(rem)} অংশ খ করবে {dec(rem)} × {b_} = {dec(days)} দিনে।", M)
def m4_pctchange():
    old, p = R.choice([200, 400, 500, 800]), R.choice([10, 20, 25])
    new = old + old * p // 100
    b.add(f"কোনো জিনিসের দাম {old} টাকা থেকে বেড়ে {new} টাকা হলে দাম শতকরা কত বৃদ্ধি পেল?", f"{p}%", [f"{(new - old) * 100 // new}%" if (new - old) * 100 // new != p else f"{p + 5}%", f"{new - old}%", f"{p * 2}%"], f"বৃদ্ধি {new - old}; হার {new - old}/{old} × 100 = {p}%।", M)
def m4_speed_avg():
    v1, v2 = R.choice([(30, 60), (40, 60), (20, 30), (60, 90), (12, 24)])
    avg = F(2 * v1 * v2, v1 + v2)
    b.add(f"একজন লোক একটি পথ ঘণ্টায় {v1} কিমি বেগে যায় এবং ঘণ্টায় {v2} কিমি বেগে ফিরে আসে। গড় বেগ কত কিমি/ঘণ্টা?", dec(avg), [dec(F(v1 + v2, 2)), dec(avg + 2), dec(F(v1 * v2, v1 + v2))], f"গড় বেগ = 2×{v1}×{v2}/({v1}+{v2}) = {dec(avg)}।", M)
def h4_three():
    a_, b_, c_ = R.choice([(10, 15, 30), (12, 24, 8), (6, 12, 12), (20, 30, 60), (4, 6, 12), (12, 18, 36)])
    t = 1 / (F(1, a_) + F(1, b_) + F(1, c_))
    b.add(f"ক, খ ও গ একটি কাজ যথাক্রমে {a_}, {b_} ও {c_} দিনে করতে পারে। তিনজন একসাথে কাজটি কত দিনে করবে?", dec(t), [dec(F(a_ + b_ + c_, 3)), dec(t + 1), dec(1 / (F(1, a_) + F(1, b_)))], f"1 দিনে 1/{a_} + 1/{b_} + 1/{c_} = 1/{dec(t)}।", H)
def h4_trains():
    l1, l2 = R.choice([(100, 150), (120, 180), (200, 100), (150, 150)])
    v1, v2 = R.choice([(36, 54), (54, 72), (36, 36), (72, 18)])
    rel = F((v1 + v2) * 1000, 3600); t = F(l1 + l2) / rel
    b.add(f"{l1} মি ও {l2} মি লম্বা দুটি ট্রেন বিপরীত দিক থেকে ঘণ্টায় {v1} কিমি ও {v2} কিমি বেগে আসছে। পরস্পরকে অতিক্রম করতে কত সেকেন্ড লাগবে?", dec(t), [dec(F(l1 + l2) / F(abs(v1 - v2) * 1000, 3600)) if v1 != v2 else dec(t * 2), dec(t + 3), dec(F(l1) / rel)], f"আপেক্ষিক বেগ {v1 + v2} কিমি/ঘণ্টা = {dec(rel)} মি/সে; সময় {l1 + l2} ÷ {dec(rel)} = {dec(t)} সেকেন্ড।", H)
def h4_eff():
    a_ = R.choice([12, 18, 24, 30, 36]); k = R.choice([2, 3])
    b_ = a_ * k; t = 1 / (F(1, a_) + F(1, b_))
    b.add(f"ক, খ-এর চেয়ে {k} গুণ দক্ষ। ক একা একটি কাজ {a_} দিনে করে। দুজনে একসাথে কত দিনে করবে?", dec(t), [dec(F(a_, k)), dec(t + 2), dec(F(a_ * k, k + 1) + 1)], f"খ লাগবে {b_} দিন; একসাথে 1/{a_} + 1/{b_} ⇒ {dec(t)} দিন।", H)
def h4_profit_two():
    c = R.choice([1000, 1200, 1500, 2000]); p1, p2 = R.choice([(10, 10), (20, 20), (25, 20), (10, 20)])
    sp1 = c - c * p1 // 100; sp2 = c + c * p2 // 100
    b.add(f"একটি জিনিস {sp1} টাকায় বিক্রি করলে {p1}% ক্ষতি হয়। {p2}% লাভ করতে হলে বিক্রয়মূল্য কত হবে?", sp2, [sp1 + sp1 * p2 // 100, sp2 + 50, c + p2], f"ক্রয়মূল্য = {sp1} × 100/{100 - p1} = {c}; {p2}% লাভে {sp2} টাকা।", H)
def h4_upstream():
    v, s = R.randint(6, 15), R.randint(1, 4)
    down, up = v + s, v - s; t = R.randint(2, 4); d = down * up * t
    b.add(f"একটি নৌকা স্রোতের অনুকূলে {d} কিমি {d // down} ঘণ্টায় এবং প্রতিকূলে একই পথ {d // up} ঘণ্টায় যায়। স্রোতের বেগ কত কিমি/ঘণ্টা?", s, [v, down, up if up != s else s + 1], f"অনুকূলে বেগ {down}, প্রতিকূলে {up}; স্রোতের বেগ = ({down} − {up})/2 = {s}।", H)

# ---- মুনাফা ----
FIX35 = [
 ("সরল মুনাফা নির্ণয়ের সূত্র কোনটি? (P = আসল, r = শতকরা হার, n = বছর)", "I = Pnr/100", ["I = P(1 + r)ⁿ", "I = P + nr", "I = Pn/r"], "সরল মুনাফা = আসল × সময় × হার / 100।"),
 ("মুনাফা-আসল (সবৃদ্ধি মূলধন) = কত?", "আসল + মুনাফা", ["আসল − মুনাফা", "আসল × মুনাফা", "মুনাফা − আসল"], "A = P + I।"),
 ("চক্রবৃদ্ধি মূলধনের সূত্র কোনটি?", "C = P(1 + r/100)ⁿ", ["C = P(1 + nr/100)", "C = Pnr/100", "C = P(1 − r/100)ⁿ"], "প্রতি বছরের মুনাফা আসলের সাথে যোগ হয়।"),
 ("চক্রবৃদ্ধি মুনাফা = কত?", "চক্রবৃদ্ধি মূলধন − আসল", ["আসল − চক্রবৃদ্ধি মূলধন", "চক্রবৃদ্ধি মূলধন + আসল", "আসল × হার"], "C − P।"),
 ("প্রথম বছর শেষে সরল ও চক্রবৃদ্ধি মুনাফার মধ্যে সম্পর্ক কী?", "উভয়ই সমান", ["সরল মুনাফা বেশি", "চক্রবৃদ্ধি মুনাফা বেশি", "চক্রবৃদ্ধি মুনাফা দ্বিগুণ"], "প্রথম বছরে মুনাফার উপর মুনাফা হয় না।"),
]
def e5_si():
    P, r, n = R.choice([1000, 2000, 5000, 1500, 3000, 4000]), R.choice([5, 6, 8, 10, 12]), R.randint(1, 5)
    I = P * r * n // 100
    b.add(f"{P} টাকার {r}% হারে {n} বছরের সরল মুনাফা কত টাকা?", I, [P * r // 100, I + P, I * 2], f"I = {P} × {n} × {r}/100 = {I} টাকা।", E)
def e5_amount():
    P, r, n = R.choice([1000, 2000, 5000, 1500]), R.choice([5, 8, 10]), R.randint(2, 4)
    A = P + P * r * n // 100
    b.add(f"{P} টাকার {r}% হারে {n} বছরের সরল মুনাফা-আসল কত টাকা?", A, [P * r * n // 100, A + P * r // 100, P + P * r // 100], f"I = {P * r * n // 100}; মুনাফা-আসল = {P} + {P * r * n // 100} = {A}।", E)
def e5_rate():
    P, r, n = R.choice([1000, 2000, 5000, 4000]), R.choice([5, 6, 8, 10]), R.randint(2, 5)
    I = P * r * n // 100
    b.add(f"{P} টাকা {n} বছরে {I} টাকা সরল মুনাফা দিলে মুনাফার হার কত?", f"{r}%", [f"{r * n}%", f"{r + 2}%", f"{r // 2 if r % 2 == 0 else r + 1}%"], f"r = 100 × {I}/({P} × {n}) = {r}%।", E)
def e5_ci1():
    P, r = R.choice([1000, 2000, 5000, 10000]), R.choice([5, 10, 20])
    C = P * (100 + r) // 100
    b.add(f"{P} টাকার {r}% হারে 1 বছরের চক্রবৃদ্ধি মূলধন কত টাকা?", C, [P * r // 100, C + P * r // 100, P + r], f"{P} × (1 + {r}/100) = {C}।", E)
def m5_ci2():
    P, r = R.choice([1000, 2000, 5000, 10000, 8000]), R.choice([5, 10, 20])
    C = F(P) * F(100 + r, 100) ** 2
    b.add(f"{P} টাকার {r}% হারে 2 বছরের চক্রবৃদ্ধি মূলধন কত টাকা?", dec(C), [dec(P + P * r * 2 // 100), dec(C + P * r // 100), dec(C - P)], f"C = {P}(1 + {r}/100)² = {dec(C)} টাকা।", M)
def m5_ciint():
    P, r = R.choice([1000, 2000, 5000, 10000]), R.choice([5, 10, 20])
    CI = F(P) * F(100 + r, 100) ** 2 - P
    b.add(f"{P} টাকার {r}% হারে 2 বছরের চক্রবৃদ্ধি মুনাফা কত টাকা?", dec(CI), [dec(P * r * 2 // 100), dec(CI + P), dec(CI + P * r // 100)], f"C = {dec(CI + P)}; চক্রবৃদ্ধি মুনাফা = {dec(CI + P)} − {P} = {dec(CI)}।", M)
def m5_diff():
    P, r = R.choice([1000, 2000, 5000, 10000, 4000]), R.choice([5, 10, 20])
    d = F(P) * F(r, 100) ** 2
    b.add(f"{P} টাকার {r}% হারে 2 বছরের চক্রবৃদ্ধি মুনাফা ও সরল মুনাফার পার্থক্য কত টাকা?", dec(d), [dec(d * 2), dec(F(P * r, 100)), dec(d + 10)], f"পার্থক্য = P(r/100)² = {P} × ({r}/100)² = {dec(d)}।", M)
def m5_time():
    P, r, n = R.choice([1000, 2000, 5000, 4000]), R.choice([5, 8, 10, 12]), R.randint(2, 6)
    I = P * r * n // 100
    b.add(f"কত বছরে {P} টাকার {r}% হারে সরল মুনাফা {I} টাকা হবে?", n, near(n), f"n = 100 × {I}/({P} × {r}) = {n} বছর।", M)
def m5_principal():
    P, r, n = R.choice([1000, 2000, 2500, 4000, 5000]), R.choice([5, 8, 10]), R.randint(2, 5)
    I = P * r * n // 100
    b.add(f"কত টাকা {r}% হারে {n} বছরে {I} টাকা সরল মুনাফা দেবে?", P, [I * r, P + I, P - I], f"P = 100 × {I}/({r} × {n}) = {P} টাকা।", M)
def m5_pop():
    P, r = R.choice([10000, 20000, 50000, 80000]), R.choice([2, 5, 10])
    v = F(P) * F(100 + r, 100) ** 2
    b.add(f"একটি শহরের জনসংখ্যা {P}। প্রতি বছর {r}% হারে বাড়লে 2 বছর পর জনসংখ্যা কত হবে?", dec(v), [dec(P + P * r * 2 // 100), dec(v + 100), dec(F(P) * F(100 + r, 100))], f"{P}(1 + {r}/100)² = {dec(v)}।", M)
def m5_depr():
    P, r = R.choice([10000, 20000, 50000, 40000]), R.choice([10, 20])
    v = F(P) * F(100 - r, 100) ** 2
    b.add(f"একটি যন্ত্রের দাম {P} টাকা। প্রতি বছর {r}% হারে মূল্য কমলে 2 বছর পর দাম কত টাকা?", dec(v), [dec(P - P * r * 2 // 100), dec(F(P) * F(100 + r, 100) ** 2), dec(F(P) * F(100 - r, 100))], f"{P}(1 − {r}/100)² = {dec(v)} টাকা।", M)
def m5_double():
    r = R.choice([4, 5, 8, 10, 12.5, 20])
    n = F(100) / F(r)
    b.add(f"সরল মুনাফার হার বার্ষিক {r}% হলে কত বছরে আসল দ্বিগুণ হবে?", dec(n), [dec(n * 2), dec(n / 2), dec(n + 2)], f"দ্বিগুণ হলে মুনাফা = আসল; n = 100/{r} = {dec(n)} বছর।", M)
def h5_ci3():
    P, r = R.choice([1000, 8000, 10000, 2000]), R.choice([5, 10, 20])
    C = F(P) * F(100 + r, 100) ** 3
    b.add(f"{P} টাকার {r}% হারে 3 বছরের চক্রবৃদ্ধি মূলধন কত টাকা?", dec(C), [dec(P + P * r * 3 // 100), dec(F(P) * F(100 + r, 100) ** 2), dec(C + P * r // 100)], f"C = {P}(1 + {r}/100)³ = {dec(C)}।", H)
def h5_rate_back():
    P, r = R.choice([1000, 2000, 5000, 10000]), R.choice([5, 10, 20])
    C = F(P) * F(100 + r, 100) ** 2
    b.add(f"কোনো আসল {P} টাকা চক্রবৃদ্ধি হারে 2 বছরে {dec(C)} টাকা হলে মুনাফার হার কত?", f"{r}%", [f"{r * 2}%", f"{r + 2}%", f"{r + 5}%"], f"(1 + r/100)² = {dec(C)}/{P} = {dec(C / P)} ⇒ 1 + r/100 = {dec(F(100 + r, 100))} ⇒ r = {r}%।", H)
def h5_principal_diff():
    P, r = R.choice([1000, 2000, 5000, 8000, 10000]), R.choice([5, 10, 20])
    d = F(P) * F(r, 100) ** 2
    b.add(f"{r}% হারে 2 বছরের চক্রবৃদ্ধি ও সরল মুনাফার পার্থক্য {dec(d)} টাকা হলে আসল কত টাকা?", P, [dec(d * 100 / r), P * 2, dec(P + d)], f"P = পার্থক্য ÷ (r/100)² = {dec(d)} ÷ ({r}/100)² = {P}।", H)
def h5_si_ci_rate():
    P, n = R.choice([1000, 2000, 4000, 5000]), R.choice([2, 3, 4])
    r = R.choice([5, 10]); I = P * r * n // 100
    C = F(P) * F(100 + r, 100) ** 2
    b.add(f"কোনো আসল {n} বছরে {r}% সরল মুনাফায় {P + I} টাকা হয়। একই আসলে একই হারে 2 বছরের চক্রবৃদ্ধি মূলধন কত?", dec(C), [dec(P + P * r * 2 // 100), dec(P + I), dec(C + 10)], f"আসল = {P + I} × 100/(100 + {r * n}) = {P}; C = {P}(1 + {r}/100)² = {dec(C)}।", H)
def h5_two_rates():
    P = R.choice([10000, 20000, 5000]); r1, r2 = R.choice([(5, 10), (10, 20), (10, 5), (20, 10)])
    v = F(P) * F(100 + r1, 100) * F(100 + r2, 100)
    b.add(f"{P} টাকা প্রথম বছর {r1}% এবং দ্বিতীয় বছর {r2}% চক্রবৃদ্ধি হারে রাখলে 2 বছর পর কত টাকা হবে?", dec(v), [dec(P + P * (r1 + r2) // 100), dec(F(P) * F(100 + max(r1, r2), 100) ** 2), dec(v + 100)], f"{P} × {dec(F(100 + r1, 100))} × {dec(F(100 + r2, 100))} = {dec(v)}।", H)


# ---- 3.3 উৎপাদক: নতুন টেমপ্লেট ----
def e3_diffsq2():
    a_, k = R.randint(2, 7), R.randint(1, 9)
    if math.gcd(a_, k) != 1: return
    b.add(f"{a_*a_}x² − {k*k} এর উৎপাদক কোনটি?", f"({a_}x + {k})({a_}x − {k})", [f"({a_}x − {k})²", f"({a_*a_}x + {k})({a_*a_}x − {k})" if a_ > 1 else f"({a_}x + {k})²", f"({a_}x + {k})²"], f"({a_}x)² − {k}² = ({a_}x + {k})({a_}x − {k})।", E)
def e3_common_bin():
    p_, k = R.randint(2, 9), R.randint(1, 9)
    b.add(f"{p_}(x + {k}) + y(x + {k}) এর উৎপাদক কোনটি?", f"(x + {k})({p_} + y)", [f"(x + {k})({p_}y)", f"({p_}x + {k})(1 + y)", f"(x + {k} + y)({p_} + 1)"], f"সাধারণ উৎপাদক (x + {k}) বের করে।", E)
def e3_sq_easy():
    k = R.randint(2, 9)
    p_ = ppow(lin([1], k), 2)
    b.add(f"{pfmt(p_, ('x',))} এর উৎপাদক কোনটি?", f"(x + {k})²", [f"(x − {k})²", f"(x + {k})(x − {k})", f"(x + {k*k})(x + 1)"], f"a² + 2ab + b² = (a + b)²; এখানে b = {k}।", E)
def m3_x4():
    k = R.randint(1, 4)
    b.add(f"x⁴ − {k**4} এর উৎপাদক কোনটি?", f"(x² + {k*k})(x + {k})(x − {k})", [f"(x² − {k*k})²", f"(x² + {k*k})²", f"(x + {k})²(x − {k})²"], f"(x²)² − ({k*k})² = (x² + {k*k})(x² − {k*k})।", M)
def h3_split2():
    p_, r_ = R.choice([2, 3]), R.choice([2, 3, 4])
    q_, s_ = R.choice([v for v in range(-5, 6) if v]), R.choice([v for v in range(-5, 6) if v])
    if math.gcd(p_, abs(q_)) != 1 or math.gcd(r_, abs(s_)) != 1 or F(-q_, p_) == F(-s_, r_) or p_ == r_: return
    poly = pmul(lin([p_], q_), lin([r_], s_)); X = ('x',)
    f1, f2 = pfmt(lin([p_], q_), X), pfmt(lin([r_], s_), X)
    b.add(f"{pfmt(poly, X)} এর উৎপাদক কোনটি?", f"({f1})({f2})", [f"({pfmt(lin([p_], -q_), X)})({pfmt(lin([r_], -s_), X)})", f"({pfmt(lin([p_], s_), X)})({pfmt(lin([r_], q_), X)})", f"({pfmt(lin([p_], -q_), X)})({f2})"], "মধ্যপদ বিভাজন: ac এর দুটি উৎপাদক যাদের যোগফল b।", H)
def h3_x4k():
    k = R.randint(2, 4)
    b.add(f"x⁴ + {k*k}x² + {k**4} এর উৎপাদক কোনটি?", f"(x² + {'' if k == 1 else k}x + {k*k})(x² − {'' if k == 1 else k}x + {k*k})", [f"(x² + {k*k})²", f"(x² + {k*k})(x² − {k*k})", f"(x² + {2*k}x + {k*k})(x² − {2*k}x + {k*k})"], f"(x² + {k*k})² − ({'' if k == 1 else k}x)² আকারে লিখে।", H)
def h3_x4_4():
    k = R.randint(1, 3); k2, k4 = 2 * k * k, 4 * k ** 4
    kx = 'x' if 2 * k == 1 else f'{2*k}x'
    b.add(f"x⁴ + {k4} এর উৎপাদক কোনটি?", f"(x² + {kx} + {k2})(x² − {kx} + {k2})", [f"(x² + {k2})²", f"(x² + {k2})(x² − {k2})", f"(x² + {k2}x + {2*k})(x² − {k2}x + {2*k})"], f"(x² + {k2})² − ({kx})² আকারে লিখে।", H)
def h3_cube_diff2():
    k = R.randint(2, 4)
    b.add(f"27x³ − {k**3} এর উৎপাদক কোনটি?", f"(3x − {k})(9x² + {3*k}x + {k*k})", [f"(3x − {k})(9x² − {3*k}x + {k*k})", f"(3x + {k})(9x² − {3*k}x + {k*k})", f"(27x − {k})(x² + {k}x + {k*k})"], f"(3x)³ − {k}³ = (3x − {k})((3x)² + 3x·{k} + {k}²)।", H)
# ---- 3.4 ভাগশেষ উপপাদ্য: নতুন টেমপ্লেট ----
def e4r_lin():
    a_, c_, r_ = R.randint(2, 7), R.choice([v for v in range(-8, 9) if v]), R.choice([v for v in range(-4, 5) if v])
    v = a_ * r_ + c_
    b.add(f"{a_}x {sgn(c_)} {abs(c_)} কে (x {sgn(-r_)} {abs(r_)}) দ্বারা ভাগ করলে ভাগশেষ কত?", v, [a_ * -r_ + c_ if a_ * -r_ + c_ != v else v + 2, v + 1, c_ if c_ != v else v - 1], f"ভাগশেষ = P({r_}) = {a_}×({r_}) {sgn(c_)} {abs(c_)} = {v}।", E)
def e4r_const():
    co = [R.randint(-5, 5) for _ in range(3)]; c_ = R.choice([v for v in range(-9, 10) if v])
    poly = pfmt({k: v for k, v in {(3,): 1, (2,): co[0], (1,): co[1], (0,): c_}.items() if v}, ('x',))
    b.add(f"{poly} কে x দ্বারা ভাগ করলে ভাগশেষ কত?", c_, [-c_, 1 + co[0] + co[1] + c_ if 1 + co[0] + co[1] + c_ not in (c_, -c_) else c_ + 3, 0 if c_ else 1], f"ভাগশেষ = P(0) = ধ্রুবপদ = {c_}।", E)
def e4r_val():
    a_ = R.choice([-2, -1, 1, 2, 3]); co = [R.randint(-5, 5), R.randint(-6, 6)]
    v = a_ * a_ + co[0] * a_ + co[1]
    poly = pfmt({k: vv for k, vv in {(2,): 1, (1,): co[0], (0,): co[1]}.items() if vv}, ('x',))
    b.add(f"P(x) = {poly} হলে P({a_}) = কত?", v, near(v), f"x = {a_} বসিয়ে {v}।", E)
def m4r_xn():
    n, k = R.choice([3, 5, 7]), R.randint(1, 4)
    b.add(f"x{'³⁵⁷'[[3,5,7].index(n)]} − {k**n} এর একটি উৎপাদক কোনটি?", f"x − {k}", [f"x + {k}", f"x − {k**n}", f"x + {k**n}"], f"P({k}) = {k}^{n} − {k**n} = 0।", M)
def m4r_k_rem():
    a_, c_, r_ = R.choice([-2, -1, 1, 2, 3]), R.choice([v for v in range(-8, 9) if v]), R.randint(-5, 9)
    k = F(r_ - a_ * a_ - c_, a_)
    if k.denominator != 1: return
    b.add(f"x² + kx {sgn(c_)} {abs(c_)} কে (x {sgn(-a_)} {abs(a_)}) দ্বারা ভাগ করলে ভাগশেষ {r_} হলে k = কত?", fr(k), [fr(-k) if k else '2', fr(k + 1), fr(k - 1)], f"P({a_}) = {r_} ⇒ {a_*a_} + ({a_})k {sgn(c_)} {abs(c_)} = {r_} ⇒ k = {fr(k)}।", M)
def h4r_two_k():
    # x³ + px² + qx + 6 এর উৎপাদক (x − 1) ও (x − 2) হলে p, q
    r1, r2 = R.sample([-3, -2, -1, 1, 2, 3], 2); r3 = R.choice([v for v in [-3, -2, -1, 1, 2, 3] if v not in (r1, r2)])
    poly = pmul(pmul(lin([1], -r1), lin([1], -r2)), lin([1], -r3))
    pq, qq = poly.get((2,), 0), poly.get((1,), 0); c_ = poly.get((0,), 0)
    if not c_: return
    b.add(f"(x {sgn(-r1)} {abs(r1)}) ও (x {sgn(-r2)} {abs(r2)}) উভয়ই x³ + px² + qx {sgn(c_)} {abs(c_)} এর উৎপাদক হলে p + q = কত?", pq + qq, near(pq + qq), f"P({r1}) = 0 ও P({r2}) = 0 থেকে p = {pq}, q = {qq}; p + q = {pq + qq}।", H)

# ======================= ব্যাংক সাজানো =======================
# 3.3 উৎপাদকে বিশ্লেষণ
b = Bank('3.3', R)
for q, c, w, e in FIX33[4:]: b.add(q, c, w, e, H)
b.fill(E, 30, [e3_diffsq, e3_monic, e3_common, e3_diffsq2, e3_common_bin, e3_sq_easy])
b.fill(M, 50, [m3_split, m3_cubes, m3_group, m3_sq_trinom, m3_four, m3_x4])
b.fill(H, 20, [h3_complex, h3_sum_cubes_poly, h3_split2, h3_x4k, h3_x4_4, h3_cube_diff2], cap=4)
B33 = b.final()
# 3.4 ভাগশেষ উপপাদ্য, k-এর মান, ত্রিঘাত রাশির উৎপাদক
b = Bank('3.4', R)
for q, c, w, e in FIX33[:4]: b.add(q, c, w, e, E)
b.fill(E, 30, [e3_rem_simple, e4r_lin, e4r_const, e4r_val])
b.fill(M, 50, [m3_rem_cubic, m3_find_k, m3_is_factor, m4r_xn, m4r_k_rem], cap=10)
b.fill(H, 20, [h3_cubic, h3_cubic_k, h3_rem_linear, h4r_two_k], cap=5)
B34 = b.final()
# 3.5 বাস্তব সমস্যা ও মুনাফা
b = Bank('3.5', R)
for q, c, w, e in FIX34[:3] + FIX35[:3]: b.add(q, c, w, e, E)
b.fill(E, 30, [e4_dist, e4_time, e4_pct, e4_profit, e4_oneday, e5_si, e5_amount, e5_rate, e5_ci1], cap=3)
b.fill(M, 50, [m4_together, m4_pipe, m4_boat, m4_train, m4_cost, m4_loss, m4_finish, m4_pctchange, m4_speed_avg,
               m5_ci2, m5_ciint, m5_diff, m5_time, m5_principal, m5_pop, m5_depr, m5_double], cap=3)
b.fill(H, 20, [h4_three, h4_trains, h4_eff, h4_profit_two, h4_upstream, h5_ci3, h5_rate_back, h5_principal_diff, h5_si_ci_rate, h5_two_rates], cap=2)
B35 = b.final()

items = B31 + B32 + B33 + B34 + B35
for i, x in enumerate(items): x['n'] = i + 1
root = pathlib.Path(__file__).resolve().parents[2]
(root / 'src/mcq/ch3.json').write_text(json.dumps(items, ensure_ascii=False, indent=1), encoding='utf-8')
from collections import Counter
print('ch3:', len(items), Counter((x['ex'], x['lv']) for x in items))
