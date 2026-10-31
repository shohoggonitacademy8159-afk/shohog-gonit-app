#!/usr/bin/env python3
"""অধ্যায় 13 সসীম ধারা: 13.1 সমান্তর ধারা · 13.2 গুণোত্তর ধারা"""
import random, pathlib, sys, math
from fractions import Fraction as F
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from mcqlib import run, save, E, M, H, fr, near, num

R = random.Random(2026103113)
def ser(t, k=4):
    out = num(t[0])
    for x in t[1:k]: out += (' − ' + num(-F(x))) if F(x) < 0 else (' + ' + num(x))
    return out + ' + …'
def seq(t, k=4): return ', '.join(num(x) for x in t[:k]) + ', …'
fx131 = [
 ("সমান্তর ধারার n-তম পদ কত? (প্রথম পদ a, সাধারণ অন্তর d)", "a + (n − 1)d", ["a + nd", "a(n − 1)d", "a + (n + 1)d"], "সূত্র।", E),
 ("সমান্তর ধারার প্রথম n পদের সমষ্টি কত?", "(n/2){2a + (n − 1)d}", ["n{2a + (n − 1)d}", "(n/2){a + (n − 1)d}", "na + d"], "সূত্র।", E),
 ("প্রথম n টি স্বাভাবিক সংখ্যার সমষ্টি কত?", "n(n + 1)/2", ["n(n − 1)/2", "n²", "n(n + 1)"], "সূত্র।", E),
 ("প্রথম n টি স্বাভাবিক সংখ্যার বর্গের সমষ্টি কত?", "n(n + 1)(2n + 1)/6", ["n(n + 1)/2", "{n(n + 1)/2}²", "n²(n + 1)/2"], "সূত্র।", E),
 ("প্রথম n টি স্বাভাবিক সংখ্যার ঘনের সমষ্টি কত?", "{n(n + 1)/2}²", ["n(n + 1)(2n + 1)/6", "n³", "n(n + 1)/2"], "সূত্র।", E),
 ("প্রথম পদ a ও শেষ পদ l হলে সমান্তর ধারার n পদের সমষ্টি কত?", "(n/2)(a + l)", ["n(a + l)", "(a + l)/2", "n(a − l)/2"], "সূত্র।", M),
 ("প্রথম n টি বিজোড় সংখ্যার সমষ্টি কত?", "n²", ["n(n + 1)", "2n", "n(n + 1)/2"], "1 + 3 + … + (2n − 1) = n²।", M),
]
def e_d(b):
    a_, d = R.randint(-10, 20), R.choice([v for v in range(-7, 9) if v])
    t = [a_ + i * d for i in range(4)]
    b.add(f"{ser(t)} ধারাটির সাধারণ অন্তর কত?", num(d), [num(-d), num(d + 1), num(t[1])] if t[1] not in (d, -d, d + 1) else [num(-d), num(d + 1), num(d + 2)], f"{num(t[1])} − ({num(t[0])}) = {num(d)}।", E)
def e_nth(b):
    a_, d, n = R.randint(-5, 15), R.choice([v for v in range(-5, 8) if v]), R.randint(5, 30)
    t = [a_ + i * d for i in range(4)]; v = a_ + (n - 1) * d
    b.add(f"{ser(t)} ধারাটির {n}-তম পদ কত?", num(v), [num(a_ + n * d), num(v + 1), num(a_ + (n - 2) * d)], f"a + (n − 1)d = {num(a_)} + {n - 1}×({num(d)}) = {num(v)}।", E)
def e_sumN(b):
    n = R.randint(5, 100)
    b.add(f"1 + 2 + 3 + … + {n} = কত?", n * (n + 1) // 2, [n * (n - 1) // 2, n * n, n * (n + 1)], f"{n}×{n + 1}/2 = {n * (n + 1) // 2}।", E)
def m_sum(b):
    a_, d, n = R.randint(-5, 15), R.choice([v for v in range(-4, 7) if v]), R.randint(5, 25)
    t = [a_ + i * d for i in range(4)]; S = n * (2 * a_ + (n - 1) * d) // 2
    if n * (2 * a_ + (n - 1) * d) % 2: return
    b.add(f"{ser(t)} ধারাটির প্রথম {n}টি পদের সমষ্টি কত?", num(S), [num(n * (2 * a_ + n * d) // 2) if n * (2 * a_ + n * d) % 2 == 0 else num(S + d), num(S + a_) if a_ else num(S + 1), num(n * (a_ + (n - 1) * d))], f"(n/2){{2a + (n − 1)d}} = {num(S)}।", M)
def m_which(b):
    a_, d, n = R.randint(1, 15), R.randint(2, 7), R.randint(8, 40)
    t = [a_ + i * d for i in range(4)]; v = a_ + (n - 1) * d
    b.add(f"{ser(t)} ধারাটির কততম পদ {v}?", n, [n - 1, n + 1, v // d if v // d not in (n, n - 1, n + 1) else n + 2], f"{a_} + (n − 1)×{d} = {v} ⇒ n = {n}।", M)
def m_count(b):
    a_, d, n = R.randint(1, 15), R.randint(2, 7), R.randint(8, 40)
    l = a_ + (n - 1) * d
    b.add(f"{a_}, {a_ + d}, {a_ + 2 * d}, …, {l} ধারায় কতটি পদ আছে?", n, [n - 1, n + 1, (l - a_) // d + 2], f"n = ({l} − {a_})/{d} + 1 = {n}।", M)
def m_sq(b):
    n = R.randint(4, 20)
    v = n * (n + 1) * (2 * n + 1) // 6
    b.add(f"1² + 2² + 3² + … + {n}² = কত?", v, [(n * (n + 1) // 2) ** 2, n * (n + 1) // 2, v + n], f"n(n + 1)(2n + 1)/6 = {v}।", M)
def m_cube(b):
    n = R.randint(3, 15)
    v = (n * (n + 1) // 2) ** 2
    b.add(f"1³ + 2³ + 3³ + … + {n}³ = কত?", v, [n * (n + 1) * (2 * n + 1) // 6, n * (n + 1) // 2, v - n], f"{{n(n + 1)/2}}² = {v}।", M)
def m_odd(b):
    n = R.randint(5, 50)
    b.add(f"1 + 3 + 5 + … + {2 * n - 1} = কত?", n * n, [n * (n + 1), (2 * n - 1) * n, n * n + 1], f"পদসংখ্যা {n}; সমষ্টি {n}² = {n * n}।", M)
def h_mn(b):
    a_, d = R.randint(-5, 10), R.choice([v for v in range(-4, 6) if v]); p, q = sorted(R.sample(range(2, 20), 2))
    tp, tq = a_ + (p - 1) * d, a_ + (q - 1) * d
    b.add(f"একটি সমান্তর ধারার {p}-তম পদ {num(tp)} এবং {q}-তম পদ {num(tq)}। প্রথম পদ কত?", num(a_), [num(d), num(a_ + d), num(tp - p * d)] if d not in (a_, a_ + d) and tp - p * d not in (a_, d, a_ + d) else [num(a_ + 2 * d), num(a_ + d), num(a_ - d)], f"d = ({num(tq)} − {num(tp)})/({q} − {p}) = {num(d)}; a = {num(a_)}।", H)
def h_sumn(b):
    a_, d = R.randint(1, 8), R.randint(1, 5); n = R.randint(4, 20)
    S = n * (2 * a_ + (n - 1) * d) // 2
    if n * (2 * a_ + (n - 1) * d) % 2: return
    b.add(f"{a_} + {a_ + d} + {a_ + 2 * d} + … ধারাটির প্রথম কতটি পদের সমষ্টি {S}?", n, [n + 1, n - 1, n + 2], f"(n/2){{{2 * a_} + (n − 1){d}}} = {S} ⇒ n = {n}।", H)
def h_sumlast(b):
    a_, d, n = R.randint(1, 10), R.randint(2, 5), R.randint(6, 25)
    l = a_ + (n - 1) * d; S = n * (a_ + l)
    if S % 2: return
    b.add(f"একটি সমান্তর ধারার প্রথম পদ {a_}, শেষ পদ {l} এবং পদসংখ্যা {n} হলে সমষ্টি কত?", S // 2, [S, (a_ + l) // 2 if (a_ + l) % 2 == 0 and (a_ + l) // 2 != S // 2 else S // 2 + 1, S // 2 + n], f"(n/2)(a + l) = {S // 2}।", H)
def h_even(b):
    n = R.randint(5, 50)
    b.add(f"2 + 4 + 6 + … + {2 * n} = কত?", n * (n + 1), [n * n, 2 * n * (2 * n + 1) // 2, n * (n + 1) // 2], f"2(1 + 2 + … + {n}) = {n * (n + 1)}।", H)
I131 = run('13.1', R, fx131, [e_d, e_nth, e_sumN], [m_sum, m_which, m_count, m_sq, m_cube, m_odd], [h_mn, h_sumn, h_sumlast, h_even], caps=(10, 9, 6))

fx132 = [
 ("গুণোত্তর ধারার n-তম পদ কত? (প্রথম পদ a, সাধারণ অনুপাত r)", "arⁿ⁻¹", ["arⁿ", "a + (n − 1)r", "arⁿ⁺¹"], "সূত্র।", E),
 ("r > 1 হলে গুণোত্তর ধারার প্রথম n পদের সমষ্টি কত?", "a(rⁿ − 1)/(r − 1)", ["a(rⁿ + 1)/(r + 1)", "n(a + l)/2", "arⁿ/(r − 1)"], "সূত্র।", E),
 ("r = 1 হলে গুণোত্তর ধারার প্রথম n পদের সমষ্টি কত?", "na", ["a", "0", "aⁿ"], "সব পদ a।", M),
 ("গুণোত্তর ধারার যেকোনো পদ ও তার পূর্ববর্তী পদের অনুপাতকে কী বলে?", "সাধারণ অনুপাত", ["সাধারণ অন্তর", "প্রথম পদ", "সমষ্টি"], "সংজ্ঞা।", E),
]
def e_r(b):
    a_, r = R.choice([1, 2, 3, 4, 5, -2, 6]), R.choice([2, 3, -2, 4, 5, -3, F(1, 2), F(1, 3)])
    t = [a_ * F(r) ** i for i in range(4)]
    b.add(f"{ser(t)} ধারাটির সাধারণ অনুপাত কত?", num(r), [num(1 / F(r)), num(F(r) + 1), num(-F(r))], f"{num(t[1])} ÷ {num(t[0])} = {num(r)}।", E)
def e_nth(b):
    a_, r, n = R.choice([1, 2, 3, 5]), R.choice([2, 3, -2]), R.randint(5, 9)
    t = [a_ * r ** i for i in range(4)]; v = a_ * r ** (n - 1)
    b.add(f"{ser(t)} ধারাটির {n}-তম পদ কত?", num(v), [num(a_ * r ** n), num(a_ * r ** (n - 2)), num(-v)], f"arⁿ⁻¹ = {a_}×({num(r)})^{n - 1} = {num(v)}।", E)
def e_next(b):
    a_, r = R.choice([1, 2, 3, 4, 5, 7]), R.choice([2, 3, 4, 5, -2, -3])
    t = [a_ * r ** i for i in range(5)]
    b.add(f"{seq(t)} অনুক্রমের পরবর্তী পদ কত?" if False else f"{', '.join(num(x) for x in t[:4])}, x গুণোত্তর অনুক্রম হলে x = কত?", num(t[4]), [num(t[3] + (t[3] - t[2])), num(t[3] * 2) if r != 2 else num(t[3] * 3), num(-t[4])], f"সাধারণ অনুপাত {num(r)}; x = {num(t[4])}।", E)
def m_sum(b):
    a_, r, n = R.choice([1, 2, 3, 5]), R.choice([2, 3, -2]), R.randint(4, 8)
    S = a_ * (r ** n - 1) // (r - 1)
    t = [a_ * r ** i for i in range(4)]
    b.add(f"{ser(t)} ধারাটির প্রথম {n}টি পদের সমষ্টি কত?", num(S), [num(a_ * (r ** (n + 1) - 1) // (r - 1)), num(a_ * r ** (n - 1)), num(S + a_)], f"a(rⁿ − 1)/(r − 1) = {num(S)}।", M)
def m_which(b):
    a_, r, n = R.choice([1, 2, 3, 5]), R.choice([2, 3]), R.randint(5, 11)
    t = [a_ * r ** i for i in range(4)]; v = a_ * r ** (n - 1)
    b.add(f"{ser(t)} ধারাটির কততম পদ {v}?", n, [n - 1, n + 1, n + 2], f"{a_}×{r}^(n − 1) = {v} ⇒ n = {n}।", M)
def m_frac(b):
    a_, r, n = R.choice([1, 2, 4, 8, 16, 64]), R.choice([F(1, 2), F(1, 3), F(1, 4)]), R.randint(5, 7)
    t = [a_ * r ** i for i in range(4)]; v = a_ * r ** (n - 1)
    b.add(f"{ser(t)} ধারাটির {n}-তম পদ কত?", fr(v), [fr(a_ * r ** n), fr(a_ * r ** (n - 2)), fr(v * 2) if v * 2 != a_ * r ** (n - 2) else fr(v * 3)], f"arⁿ⁻¹ = {fr(v)}।", M)
def m_geomean(b):
    a_, k = R.randint(1, 8), R.randint(2, 5)
    b.add(f"{a_} ও {a_ * k * k} এর মধ্যে একটি গুণোত্তর মধ্যক বসালে সেটি কত? (ধনাত্মক)", a_ * k, [a_ * (1 + k * k) // 2 if a_ * (1 + k * k) % 2 == 0 and a_ * (1 + k * k) // 2 != a_ * k else a_ * k + 1, a_ * k * k // 2 if a_ * k * k % 2 == 0 and a_ * k * k // 2 != a_ * k else a_ * k + 2, a_ * k * k], f"√({a_} × {a_ * k * k}) = {a_ * k}।", M)
def h_find(b):
    a_, r = R.choice([1, 2, 3, 4, 5]), R.choice([2, 3, -2, -3]); p, q = R.choice([(2, 4), (3, 5), (2, 5), (1, 4), (3, 6)])
    tp, tq = a_ * r ** (p - 1), a_ * r ** (q - 1)
    b.add(f"একটি গুণোত্তর ধারার {p}-তম পদ {num(tp)} এবং {q}-তম পদ {num(tq)}। প্রথম পদ কত?", num(a_), [num(r), num(-a_), num(tp)] if r not in (a_, -a_) and tp not in (a_, -a_, r) else [num(a_ + 1), num(-a_), num(a_ * 2)], f"r^{q - p} = {num(F(tq, tp))} ⇒ r = {num(r)} ; a = {num(a_)}।", H)
def h_sum_n(b):
    a_, r = R.choice([1, 2, 3]), R.choice([2, 3]); n = R.randint(3, 8)
    S = a_ * (r ** n - 1) // (r - 1)
    b.add(f"{a_} + {a_ * r} + {a_ * r * r} + … ধারাটির প্রথম কতটি পদের সমষ্টি {S}?", n, [n + 1, n - 1, n + 2], f"{a_}({r}ⁿ − 1)/({r} − 1) = {S} ⇒ n = {n}।", H)
def h_log(b):
    a_, n = R.choice([2, 3, 5]), R.randint(3, 8)
    # log a + log a² + ... + log aⁿ = (n(n+1)/2) log a
    b.add(f"log {a_} + log {a_}² + log {a_}³ + … + log {a_}^{n} = কত?" if False else f"log {a_} + log {a_ * a_} + log {a_ ** 3} + … ধারাটির প্রথম {n}টি পদের সমষ্টি কত?", f"{n * (n + 1) // 2} log {a_}", [f"{n} log {a_}", f"{n * n} log {a_}", f"{n * (n - 1) // 2} log {a_}"], f"(1 + 2 + … + {n}) log {a_} = {n * (n + 1) // 2} log {a_}।", H)
def h_frac_sum(b):
    n = R.randint(3, 8); r = R.choice([2, 3])
    S = sum(F(1, r ** i) for i in range(n))
    b.add(f"1 + 1/{r} + 1/{r * r} + … ধারাটির প্রথম {n}টি পদের সমষ্টি কত?", fr(S), [fr(S + F(1, r ** n)), fr(S - F(1, r ** (n - 1))), fr(F(r, r - 1))], f"(1 − (1/{r})^{n})/(1 − 1/{r}) = {fr(S)}।", H)
I132 = run('13.2', R, fx132, [e_r, e_nth, e_next], [m_sum, m_which, m_frac, m_geomean], [h_find, h_sum_n, h_log, h_frac_sum], caps=(10, 13, 6))
save(13, I131 + I132)
