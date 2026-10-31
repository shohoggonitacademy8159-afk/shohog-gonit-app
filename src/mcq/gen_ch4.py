#!/usr/bin/env python3
"""অধ্যায় 4 সূচক ও লগারিদম: 4.1 সূচক · 4.2 লগারিদম · 4.3 বৈজ্ঞানিক রূপ ও সাধারণ লগারিদম"""
import random, pathlib, sys, math
from fractions import Fraction as F
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from mcqlib import run, save, E, M, H, fr, near, num, sup

R = random.Random(2026103104)
# ------------- 4.1 সূচক -------------
fx41 = [
 ("a ≠ 0 হলে a⁰ = কত?", "1", ["0", "a", "অসংজ্ঞায়িত"], "শূন্য সূচকের নিয়ম।", E),
 ("aᵐ × aⁿ = কত?", "aᵐ⁺ⁿ", ["aᵐⁿ", "aᵐ⁻ⁿ", "2aᵐ⁺ⁿ"], "একই ভিত্তির গুণে সূচক যোগ হয়।", E),
 ("aᵐ ÷ aⁿ = কত?", "aᵐ⁻ⁿ", ["aᵐ⁺ⁿ", "aᵐ/ⁿ", "aⁿ⁻ᵐ"], "একই ভিত্তির ভাগে সূচক বিয়োগ হয়।", E),
 ("(aᵐ)ⁿ = কত?", "aᵐⁿ", ["aᵐ⁺ⁿ", "aᵐ⁻ⁿ", "aᵐ"], "ঘাতের ঘাতে সূচক গুণ হয়।", E),
 ("a⁻ⁿ = কত?", "1/aⁿ", ["−aⁿ", "aⁿ", "−1/aⁿ"], "ঋণাত্মক সূচক মানে বিপরীত।", E),
 ("(ab)ⁿ = কত?", "aⁿbⁿ", ["abⁿ", "aⁿb", "(a + b)ⁿ"], "গুণফলের ঘাত।", E),
 ("a^(1/n) কে কীভাবে লেখা যায়?", "ⁿ√a", ["a/n", "1/aⁿ", "√(an)"], "ভগ্নাংশ সূচক মানে মূল।", E),
 ("(a/b)ⁿ = কত?", "aⁿ/bⁿ", ["a/bⁿ", "aⁿ/b", "(a − b)ⁿ"], "ভাগফলের ঘাত।", E),
 ("aˣ = aʸ (a > 0, a ≠ 1) হলে নিচের কোনটি সত্য?", "x = y", ["x > y", "x = −y", "xy = 1"], "একই ভিত্তি হলে সূচক সমান।", M),
 ("(aᵖ/aᑫ)ᵖ⁺ᑫ × (aᑫ/aʳ)ᑫ⁺ʳ × (aʳ/aᵖ)ʳ⁺ᵖ = কত?", "1", ["0", "a", "aᵖᑫʳ"], "সূচকের যোগফল p² − q² + q² − r² + r² − p² = 0।", H),
]
def e_pow(b):
    a_, n = R.choice([(2, R.randint(3, 10)), (3, R.randint(2, 6)), (5, R.randint(2, 4)), (4, R.randint(2, 5)), (10, R.randint(2, 6)), (7, 2), (6, 3)])
    v = a_ ** n; b.add(f"{a_}{sup(n)} = কত?", v, [a_ * n, v // a_, v * a_], f"{a_} কে {n} বার গুণ করে {v}।", E)
def e_neg(b):
    a_, n = R.choice([(2, R.randint(1, 6)), (3, R.randint(1, 4)), (5, R.randint(1, 3)), (10, R.randint(1, 4)), (4, 2)])
    v = F(1, a_ ** n); b.add(f"{a_}{sup(-n)} = কত?", fr(v), [num(-a_ ** n), num(-a_ * n), fr(F(1, a_ * n)) if a_ * n != a_ ** n else fr(F(1, a_ ** n + 1))], f"{a_}{sup(-n)} = 1/{a_}{sup(n)} = {fr(v)}।", E)
def e_root(b):
    r, n = R.choice([(2, 2), (3, 2), (4, 2), (5, 2), (2, 3), (3, 3), (4, 3), (5, 3), (2, 4), (3, 4), (2, 5), (10, 3), (6, 2), (7, 2)])
    v = r ** n; nm = {2: '1/2', 3: '1/3', 4: '1/4', 5: '1/5'}[n]
    b.add(f"{v}^({nm}) = কত?", r, [v // n if v // n != r else r + 2, r * r if r * r != v else r + 1, F(v, 2) if F(v, 2) != r else r + 3], f"{v} = {r}{sup(n)}, তাই {n}-তম মূল {r}।", E)
def e_exp(b):
    m, n = R.randint(2, 9), R.randint(2, 9); op = R.choice('×÷^')
    if op == '×': c, ws, e = m + n, [m * n, abs(m - n) if m != n else m + n + 1, m + n + 1], "সূচক যোগ"
    elif op == '÷': c, ws, e = m - n, [m + n, F(m, n), n - m if n != m else 1], "সূচক বিয়োগ"
    else: c, ws, e = m * n, [m + n, m ** n, m * n + 1], "সূচক গুণ"
    q = {'×': f"x{sup(m)} × x{sup(n)} = xᵏ হলে k = কত?", '÷': f"x{sup(m)} ÷ x{sup(n)} = xᵏ হলে k = কত?", '^': f"(x{sup(m)}){sup(n)} = xᵏ হলে k = কত?"}[op]
    b.add(q, num(c), [num(w) for w in ws], f"{e}: k = {num(c)}।", E)
def e_zero(b):
    a_ = R.choice([2, 3, 5, 7, 10, 25, 100, 999]); k = R.randint(2, 9)
    b.add(f"{k} × {a_}⁰ = কত?", k, [0, k * a_, a_], f"{a_}⁰ = 1, তাই {k} × 1 = {k}।", E)
def m_frac(b):
    r, n, m = R.choice([(2, 3, 2), (3, 3, 2), (2, 4, 3), (2, 5, 2), (3, 2, 3), (4, 2, 3), (2, 2, 5), (5, 2, 3), (2, 3, 4), (3, 4, 3), (10, 3, 2), (2, 6, 5)])
    base = r ** n; v = r ** m
    b.add(f"{base}^({m}/{n}) = কত?", v, [r ** (m + 1), base * m // n if base * m % n == 0 and base * m // n != v else v + 2, r * m if r * m != v else v - 1], f"{base} = {r}{sup(n)}; ({r}{sup(n)})^({m}/{n}) = {r}{sup(m)} = {v}।", M)
def m_neg_frac(b):
    r, n = R.choice([(2, 2), (3, 2), (2, 3), (3, 3), (5, 2), (2, 4), (4, 2), (10, 2)])
    base = r ** n; v = F(1, r)
    b.add(f"{base}^(−1/{n}) = কত?", fr(v), [num(-r), r, fr(F(1, base))], f"{base}^(1/{n}) = {r}; ঋণাত্মক সূচকে বিপরীত = 1/{r}।", M)
def m_solve(b):
    a_, x = R.choice([2, 3, 5, 4, 7]), R.randint(1, 6)
    k = R.choice([0, 1, 2, -1]); v = a_ ** (x + k)
    if x + k < 1: return
    lhs = f"{a_}ˣ" if k == 0 else f"{a_}^(x {'+' if k > 0 else '−'} {abs(k)})"
    b.add(f"{lhs} = {v} হলে x = কত?", x, near(x), f"{v} = {a_}{sup(x + k)}; সূচক তুলনা করে x = {x}।", M)
def m_ratio(b):
    a_, k = R.choice([2, 3, 5, 4]), R.choice([1, 2])
    s = R.choice([1, -1]); v = a_ ** k + s
    b.add(f"({a_}ⁿ⁺{sup(k)} {'+' if s > 0 else '−'} {a_}ⁿ) ÷ {a_}ⁿ = কত?", v, [a_ ** k, a_ ** k - s, a_ * k], f"{a_}ⁿ সাধারণ নিয়ে {a_}{sup(k)} {'+' if s > 0 else '−'} 1 = {v}।", M)
def m_simplify(b):
    a_, p, q = R.choice([2, 3, 5]), R.randint(2, 6), R.randint(1, 5)
    v = a_ ** (p - q) if p >= q else F(1, a_ ** (q - p))
    b.add(f"({a_}{sup(p)} × {a_}{sup(q)}) ÷ {a_}{sup(2*q)} = কত?", fr(v), [fr(a_ ** (p + q)), fr(v * a_), fr(v / a_)], f"সূচক: {p} + {q} − {2*q} = {p - q}; মান {fr(v)}।", M)
def m_root_pow(b):
    a_, n = R.choice([2, 3, 5]), R.choice([2, 3])
    k = R.randint(2, 4); v = a_ ** k
    b.add(f"{'√' if n == 2 else '∛'}({a_}{sup(n*k)}) = কত?", v, [a_ ** (n * k), a_ ** (k + 1), a_ * k if a_ * k != v else v + 1], f"({a_}{sup(n*k)})^(1/{n}) = {a_}{sup(k)} = {v}।", M)
def m_sq_eq(b):
    x = R.randint(2, 6); a_ = R.choice([2, 3])
    b.add(f"{a_ * a_}ˣ = {a_}^(x + {x}) হলে x = কত?", x, near(x), f"{a_*a_}ˣ = {a_}^(2x); 2x = x + {x} ⇒ x = {x}।", M)
def h_frac_eq(b):
    a_, p, q = R.choice([(2, 2, 3), (2, 3, 2), (3, 2, 3), (2, 2, 5), (2, 4, 3), (3, 3, 2), (5, 2, 3), (2, 3, 4)])
    # (a^p)^x = a^q ⇒ x = q/p
    b.add(f"{a_ ** p}ˣ = {a_ ** q} হলে x = কত?", fr(F(q, p)), [fr(F(p, q)), fr(F(a_ ** q, a_ ** p)) if F(a_ ** q, a_ ** p) != F(q, p) else '2', q - p if q - p and F(q - p) != F(q, p) else q + p], f"{a_}^({p}x) = {a_}{sup(q)} ⇒ x = {fr(F(q, p))}।", H)
def h_sum_eq(b):
    a_, x = R.choice([2, 3]), R.randint(2, 6)
    v = a_ ** x + a_ ** (x + 1)
    b.add(f"{a_}ˣ + {a_}ˣ⁺¹ = {v} হলে x = কত?", x, near(x), f"{a_}ˣ(1 + {a_}) = {v} ⇒ {a_}ˣ = {v // (1 + a_)} ⇒ x = {x}।", H)
def h_value(b):
    a_, k = R.choice([2, 3, 4, 5]), R.randint(1, 3)
    x = R.choice([2, 3, 4])
    num_ = F(a_ ** (x + k)) ; den = F(a_ ** (x - 1))
    v = num_ / den
    b.add(f"x = {x} হলে {a_}^(x + {k}) ÷ {a_}^(x − 1) = কত?", fr(v), [fr(v * a_), fr(v / a_), fr(F(a_ ** k))], f"সূচক: (x + {k}) − (x − 1) = {k + 1}; মান {a_}{sup(k + 1)} = {fr(v)}।", H)
def h_mix(b):
    r = R.choice([2, 3]); m, n = R.choice([(2, 3), (3, 2), (4, 3), (2, 5)])
    base = r ** (n * 2); v = r ** (2 * m)
    b.add(f"({base}^({m}/{n}))^(1/2) × {r}^({m}) = কত?", r ** (2 * m) * r ** m // r ** m if False else r ** (m + m), [r ** (2 * m + 1), r ** m, r ** (3 * m)], f"({r}^({2*n}))^({m}/{n}) = {r}^({2*m}); তার বর্গমূল {r}{sup(m)}; গুণফল {r}{sup(2*m)}।", H)
I41 = run('4.1', R, fx41, [e_pow, e_neg, e_root, e_exp, e_zero], [m_frac, m_neg_frac, m_solve, m_ratio, m_simplify, m_root_pow, m_sq_eq], [h_frac_eq, h_sum_eq, h_value, h_mix], caps=(7, 9, 7))

# ------------- 4.2 লগারিদম -------------
fx42 = [
 ("a > 0, a ≠ 1 হলে logₐ1 = কত?", "0", ["1", "a", "অসংজ্ঞায়িত"], "a⁰ = 1।", E),
 ("logₐa = কত?", "1", ["0", "a", "−1"], "a¹ = a।", E),
 ("logₐ(MN) = কত?", "logₐM + logₐN", ["logₐM × logₐN", "logₐM − logₐN", "M logₐN"], "গুণফলের লগ।", E),
 ("logₐ(M/N) = কত?", "logₐM − logₐN", ["logₐM ÷ logₐN", "logₐM + logₐN", "logₐ(M − N)"], "ভাগফলের লগ।", E),
 ("logₐ(Mʳ) = কত?", "r logₐM", ["(logₐM)ʳ", "logₐM + r", "logₐ(rM)"], "ঘাতের লগ।", E),
 ("logₐb × logᵦa = কত? (এখানে logᵦ মানে b ভিত্তিক লগ)", "1", ["0", "ab", "a/b"], "ভিত্তি পরিবর্তনের সূত্র।", M),
 ("a^(logₐx) = কত?", "x", ["a", "logₐx", "aˣ"], "লগারিদমের সংজ্ঞা।", M),
 ("aˣ = N হলে নিচের কোনটি সত্য?", "x = logₐN", ["N = logₐx", "a = logₓN", "x = log_N a"], "সংজ্ঞা অনুযায়ী।", E),
 ("শূন্য বা ঋণাত্মক সংখ্যার লগারিদম সম্পর্কে কোনটি সত্য?", "সংজ্ঞায়িত নয়", ["0", "1", "ঋণাত্মক"], "a > 0 হলে aˣ সর্বদা ধনাত্মক।", E),
 ("সাধারণ লগারিদমের ভিত্তি কত?", "10", ["e", "2", "1"], "সাধারণ লগ = log₁₀।", E),
]
SUB = str.maketrans('0123456789', '₀₁₂₃₄₅₆₇₈₉')
def lg(b_): return 'log' + str(b_).translate(SUB)
def e_logp(b):
    a_, k = R.choice([(2, R.randint(2, 8)), (3, R.randint(2, 5)), (5, R.randint(2, 4)), (10, R.randint(2, 5)), (4, R.randint(2, 4)), (7, 2), (6, 2)])
    b.add(f"{lg(a_)}{a_ ** k} = কত?", k, [a_ ** k // a_, k + 1, k - 1 if k > 2 else a_], f"{a_ ** k} = {a_}{sup(k)}, তাই লগ = {k}।", E)
def e_logfrac(b):
    a_, k = R.choice([(2, R.randint(1, 6)), (3, R.randint(1, 4)), (5, R.randint(1, 3)), (10, R.randint(1, 4))])
    b.add(f"{lg(a_)}(1/{a_ ** k}) = কত?", num(-k), [k, fr(F(1, k)) if k > 1 else '0', num(-k - 1)], f"1/{a_ ** k} = {a_}{sup(-k)}।", E)
def e_def(b):
    a_, x = R.choice([2, 3, 5, 10, 4]), R.randint(2, 4)
    b.add(f"{lg(a_)}x = {x} হলে x = কত?", a_ ** x, [a_ * x, x ** a_ if x ** a_ != a_ ** x else a_ ** x + 1, a_ ** (x - 1)], f"x = {a_}{sup(x)} = {a_ ** x}।", E)
def m_sqrt_base(b):
    a_, k = R.choice([2, 3, 5]), R.randint(1, 4)
    v = 2 * k
    b.add(f"log_√{a_} ({a_ ** k}) = কত?", v, [k, F(k, 2) if k % 2 == 0 else k + 1, 2 * k + 2], f"{a_ ** k} = (√{a_}){sup(2*k)}।", M)
def m_findbase(b):
    a_, k = R.choice([(2, R.randint(3, 6)), (3, R.randint(2, 4)), (5, R.randint(2, 3)), (4, 3), (6, 2), (7, 2), (9, 2), (10, 3)])
    b.add(f"logₓ{a_ ** k} = {k} হলে x = কত?", a_, [a_ + 1, a_ ** k // k if a_ ** k % k == 0 and a_ ** k // k != a_ else a_ * 2, k], f"x{sup(k)} = {a_ ** k} ⇒ x = {a_}।", M)
def m_sum(b):
    a_ = R.choice([2, 3, 5]); p, q = R.randint(1, 4), R.randint(1, 4); s = R.choice([1, -1])
    v = p + s * q
    b.add(f"{lg(a_)}{a_ ** p} {'+' if s > 0 else '−'} {lg(a_)}{a_ ** q} = কত?", num(v), [num(p * q), num(v + 1), num(p - s * q) if p - s * q != v else num(v - 1)], f"{p} {'+' if s > 0 else '−'} {q} = {num(v)}।", M)
def m_log10(b):
    pairs = [("log 2 + log 5", 1), ("log 20 + log 5", 2), ("log 50 + log 2", 2), ("log 4 + log 25", 2), ("log 8 + log 125", 3), ("log 200 − log 2", 2), ("log 500 − log 5", 2), ("log 40 + log 25", 3), ("log 0.1", -1), ("log 0.01", -2), ("log 1000", 3), ("log 2 + log 50", 2), ("log 250 + log 4", 3), ("log 5000 − log 5", 3)]
    q, v = R.choice(pairs)
    b.add(f"{q} = কত? (ভিত্তি 10)", num(v), [num(v + 1), num(v - 1), num(-v) if v else '10'], "সূত্র logM + logN = log(MN) ব্যবহার করে।", M)
def m_pow(b):
    a_, k, r = R.choice([2, 3, 5]), R.randint(1, 3), R.randint(2, 4)
    v = k * r
    b.add(f"{lg(a_)}({a_ ** k}{sup(r)}) = কত?", v, [k + r, k ** r if k ** r != v else v + 1, r], f"r logₐM = {r} × {k} = {v}।", M)
def m_given(b):
    L2, L3 = F('0.3010'), F('0.4771')
    opts = [("log 4", 2 * L2), ("log 8", 3 * L2), ("log 6", L2 + L3), ("log 9", 2 * L3), ("log 12", 2 * L2 + L3), ("log 18", L2 + 2 * L3), ("log 5", 1 - L2), ("log 1.5", L3 - L2), ("log 16", 4 * L2), ("log 27", 3 * L3), ("log 24", 3 * L2 + L3), ("log 25", 2 - 2 * L2)]
    q, v = R.choice(opts)
    f4 = lambda x: f"{float(x):.4f}"
    b.add(f"log 2 = 0.3010 ও log 3 = 0.4771 হলে {q} = কত?", f4(v), [f4(v + L2), f4(v - F('0.1')), f4(v + F('0.0791'))], f"উৎপাদকে ভেঙে লগ যোগ/বিয়োগ করে {f4(v)}।", M)
def h_nested(b):
    a_, k, m = R.choice([2, 3]), R.randint(2, 4), R.randint(2, 3)
    # log_{a^m} a^{k}  = k/m
    b.add(f"{lg(a_ ** m)}{a_ ** k} = কত?", fr(F(k, m)), [fr(F(m, k)), k * m, k - m if k != m and F(k - m) != F(k, m) else k + m], f"{a_ ** k} = ({a_ ** m})^({fr(F(k, m))})।", H)
def h_frac_base(b):
    a_, k = R.choice([2, 3, 5]), R.randint(2, 4)
    b.add(f"log_(1/{a_}) {a_ ** k} = কত?", num(-k), [k, fr(F(1, k)), num(-k + 1)], f"{a_ ** k} = (1/{a_})^({num(-k)})।", H)
def h_eq(b):
    a_, x = R.choice([2, 3]), R.randint(2, 5)
    # log_a(x+c) = k
    c = R.randint(1, 9); k_ = None
    for kk in range(1, 8):
        if a_ ** kk - c > 0 and a_ ** kk - c == x: k_ = kk
    if k_ is None:
        k_ = R.randint(2, 4); x = a_ ** k_ - c
        if x <= 0: return
    b.add(f"{lg(a_)}(x + {c}) = {k_} হলে x = কত?", x, near(x), f"x + {c} = {a_}{sup(k_)} = {a_ ** k_} ⇒ x = {x}।", H)
def h_chain(b):
    a_, b_, c_ = R.choice([(2, 4, 16), (3, 9, 81), (2, 8, 64), (5, 25, 625), (2, 16, 256), (3, 27, 729)])
    v = math.log(c_, a_)
    v = round(v)
    b.add(f"{lg(a_)}{b_} × {lg(b_)}{c_} = কত?", v, [v + 1, v - 1, v * 2], f"logₐb × log_b c = logₐc = {lg(a_)}{c_} = {v}।", H)
def h_sqrt(b):
    a_ = R.choice([2, 3, 5]); k = R.randint(2, 5)
    # log_a (a^k √a) = k + 1/2
    v = F(2 * k + 1, 2)
    b.add(f"{lg(a_)}({a_ ** k}√{a_}) = কত?", fr(v), [k, fr(v + 1), fr(F(k, 2))], f"{a_ ** k}√{a_} = {a_}^({fr(v)})।", H)
I42 = run('4.2', R, fx42, [e_logp, e_logfrac, e_def], [m_sqrt_base, m_findbase, m_sum, m_log10, m_pow, m_given], [h_nested, h_frac_base, h_eq, h_chain, h_sqrt], caps=(9, 9, 6))

# ------------- 4.3 বৈজ্ঞানিক রূপ ও সাধারণ লগারিদম -------------
fx43 = [
 ("কোনো সংখ্যার বৈজ্ঞানিক রূপ a × 10ⁿ হলে a-এর মান কোন সীমায় থাকে?", "1 ≤ a < 10", ["0 < a < 1", "1 < a ≤ 10", "10 ≤ a < 100"], "বৈজ্ঞানিক রূপের শর্ত।", E),
 ("সাধারণ লগারিদমের দুটি অংশ কী কী?", "পূর্ণক ও অংশক", ["ভিত্তি ও সূচক", "লব ও হর", "মূল ও ঘাত"], "পূর্ণক (characteristic) ও অংশক (mantissa)।", E),
 ("3.47, 34.7 ও 347 এর লগারিদমের কোন অংশ একই?", "অংশক", ["পূর্ণক", "দুটিই", "কোনোটিই নয়"], "অঙ্কগুলো একই হলে অংশক একই থাকে।", M),
 ("অংশক সর্বদা কেমন হয়?", "ধনাত্মক (0 ≤ অংশক < 1)", ["ঋণাত্মক", "পূর্ণসংখ্যা", "1 এর বেশি"], "অংশক দশমিক ভগ্নাংশ।", M),
 ("1 এর চেয়ে ছোট ধনাত্মক সংখ্যার লগারিদমের পূর্ণক কেমন হয়?", "ঋণাত্মক", ["ধনাত্মক", "শূন্য", "1"], "যেমন log 0.5 = −1 + 0.6990।", E),
]
def sci(n10, e):
    """(a, n): a × 10ⁿ লেখা"""
    return f"{n10} × 10{sup(e)}"
def e_sci(b):
    d = R.choice(['2.5', '3.47', '5.6', '7.02', '1.23', '9.8', '4.05', '6.3', '8.1', '2.04'])
    e = R.choice([2, 3, 4, 5, 6, -1, -2, -3, -4])
    val = F(d) * F(10) ** e
    s = f"{float(val):f}".rstrip('0').rstrip('.') if e < 0 else str(int(val))
    b.add(f"{s} এর বৈজ্ঞানিক রূপ কোনটি?", sci(d, e), [sci(d, e + 1), sci(d, -e), sci(str(F(d) * 10).replace('.0', '') if True else d, e - 1) if False else f"{fr(F(d) * 10) if (F(d) * 10).denominator == 1 else float(F(d) * 10)} × 10{sup(e - 1)}"], f"দশমিক বিন্দু সরিয়ে 1 ≤ a < 10 করে {sci(d, e)}।", E)
def e_char(b):
    e = R.randint(-4, 5); d = R.choice(['3.47', '5.6', '2.08', '7.13', '1.9', '8.4', '4.56'])
    val = F(d) * F(10) ** e
    s = f"{float(val):f}".rstrip('0').rstrip('.') if e < 0 else str(int(val)) if val.denominator == 1 else str(float(val))
    b.add(f"log {s} এর পূর্ণক কত?", num(e), [num(e + 1), num(e - 1), num(-e) if e else '1'], f"{s} = {sci(d, e)}, তাই পূর্ণক {num(e)}।", E)
def e_log10(b):
    e = R.randint(-5, 6)
    s = str(10 ** e) if e >= 0 else f"{float(F(1, 10 ** -e)):f}".rstrip('0')
    b.add(f"log {s} = কত?", num(e), [num(e + 1), num(-e) if e else '10', num(e - 1)], f"{s} = 10{sup(e)}।", E)
def m_digits(b):
    c = R.randint(0, 6)
    b.add(f"কোনো সংখ্যার লগারিদমের পূর্ণক {c} হলে সংখ্যাটির পূর্ণ অংশে কয়টি অঙ্ক আছে?", c + 1, [c, c + 2, 2 * c if 2 * c not in (c, c + 1, c + 2) else c + 3], f"পূর্ণক n হলে অঙ্ক সংখ্যা n + 1 = {c + 1}।", M)
def m_scimul(b):
    a1, a2 = R.choice([(2, 3), (2, 4), (1.5, 4), (2.5, 2), (3, 3), (1.2, 5), (4, 2), (1.1, 6)]); e1, e2 = R.randint(-4, 6), R.randint(-4, 6)
    p = F(str(a1)) * F(str(a2)); e = e1 + e2
    if p >= 10: p /= 10; e += 1
    ps = fr(p) if p.denominator == 1 else str(float(p))
    b.add(f"({a1} × 10{sup(e1)}) × ({a2} × 10{sup(e2)}) = কত?", sci(ps, e), [sci(ps, e1 * e2), sci(ps, e + 1), sci(ps, e - 1)], f"অংশ গুণ ও সূচক যোগ করে {sci(ps, e)}।", M)
def m_scidiv(b):
    a1, a2 = R.choice([(6, 3), (8, 2), (9, 3), (8, 4), (6, 2), (4.8, 1.2), (7.5, 2.5)]); e1, e2 = R.randint(-3, 7), R.randint(-3, 5)
    p = F(str(a1)) / F(str(a2)); e = e1 - e2
    ps = fr(p) if p.denominator == 1 else str(float(p))
    b.add(f"({a1} × 10{sup(e1)}) ÷ ({a2} × 10{sup(e2)}) = কত?", sci(ps, e), [sci(ps, e1 + e2) if e1 + e2 != e else sci(ps, e + 2), sci(ps, e + 1), sci(ps, e - 1)], f"অংশ ভাগ ও সূচক বিয়োগ করে {sci(ps, e)}।", M)
def m_charfrom(b):
    # দশমিকের পর শূন্যের সংখ্যা থেকে পূর্ণক
    z = R.randint(0, 4); d = R.choice(['35', '702', '48', '9', '123'])
    s = '0.' + '0' * z + d
    b.add(f"log {s} এর পূর্ণক কত?", num(-(z + 1)), [num(-z) if z else '0', num(z + 1), num(-(z + 2))], f"দশমিকের পর প্রথম অশূন্য অঙ্কের আগে {z}টি শূন্য, তাই পূর্ণক −{z + 1}।", M)
def m_given2(b):
    L2 = F('0.3010')
    e = R.choice([-3, -2, -1, 1, 2, 3, 4])
    v = L2 + e
    s = (str(2 * 10 ** e) if e >= 0 else f"{float(F(2, 10 ** -e)):f}".rstrip('0'))
    f4 = lambda x: f"{float(x):.4f}"
    b.add(f"log 2 = 0.3010 হলে log {s} = কত?", f4(v), [f4(v + 1), f4(v - 1), f4(-v)], f"{s} = 2 × 10{sup(e)}; লগ = 0.3010 {'+' if e >= 0 else '−'} {abs(e)} = {f4(v)}।", M)
def h_digits_pow(b):
    base, L = R.choice([(2, F('0.3010')), (3, F('0.4771'))]); n = R.randint(10, 60)
    d = math.floor(n * L) + 1
    if d != len(str(base ** n)): return
    b.add(f"log {base} = {float(L):.4f} হলে {base}{sup(n)} সংখ্যাটিতে কয়টি অঙ্ক আছে?", d, [d - 1, d + 1, n], f"log {base}{sup(n)} = {n} × {float(L):.4f} = {float(n * L):.4f}; পূর্ণক {d - 1}, অঙ্ক {d}।", H)
def h_mantissa(b):
    L = R.choice([('2', F('0.3010')), ('3', F('0.4771')), ('5', F('0.6990')), ('7', F('0.8451'))])
    e = R.randint(-4, -1)
    s = f"{float(F(int(L[0]), 10 ** -e)):f}".rstrip('0')
    v = L[1] + e
    f4 = lambda x: f"{float(x):.4f}"
    b.add(f"log {L[0]} = {float(L[1]):.4f} হলে log {s} = কত?", f4(v), [f4(L[1] - e), f4(-L[1] + e), f4(v + 1)], f"{s} = {L[0]} × 10{sup(e)}; লগ = {num(e)} + {float(L[1]):.4f} = {f4(v)}।", H)
def h_antilog(b):
    e = R.randint(-3, 4); L = R.choice([('2', '0.3010'), ('3', '0.4771'), ('5', '0.6990')])
    val = F(int(L[0])) * F(10) ** e
    s = str(int(val)) if val.denominator == 1 else f"{float(val):f}".rstrip('0')
    other = lambda k: (str(int(F(int(L[0])) * F(10) ** k)) if k >= 0 else f"{float(F(int(L[0])) * F(10) ** k):f}".rstrip('0'))
    b.add(f"log x = {num(e)} + {L[1]} হলে x = কত? (log {L[0]} = {L[1]})", s, [other(e + 1), other(e - 1), other(-e) if e else other(2)], f"x = {L[0]} × 10{sup(e)} = {s}।", H)
I43 = run('4.3', R, fx43, [e_sci, e_char, e_log10], [m_digits, m_scimul, m_scidiv, m_charfrom, m_given2], [h_digits_pow, h_mantissa, h_antilog], caps=(10, 11, 8))
save(4, I41 + I42 + I43)
