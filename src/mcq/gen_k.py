#!/usr/bin/env python3
"""৮ম শ্রেণি সাধারণ গণিত (c8)। অধ্যায় 1, 3, 7, 9, 11: 300টি (অধ্যায়ভিত্তিক); বাকি প্রতিটি অনুশীলনী 250টি। হার: সহজ 50%, মধ্যম 40%, কঠিন 10%।
2.1 সরল মুনাফা · 2.2 চক্রবৃদ্ধি মুনাফা · 4.1 বর্গের সূত্র · 4.2 ঘনের সূত্র · 4.3 উৎপাদকে বিশ্লেষণ · 4.4 গ.সা.গু. ও ল.সা.গু.
5.1 লঘিষ্ঠকরণ ও সাধারণ হর · 5.2 যোগ, বিয়োগ, গুণ ও ভাগ · 6.1 সমাধান পদ্ধতি · 6.2 বাস্তব সমস্যা · 8.1 চতুর্ভুজের ধর্ম ও কোণ · 8.2 চতুর্ভুজক্ষেত্রের ক্ষেত্রফল
10.1 বৃত্তের অংশ, জ্যা ও কোণ · 10.2 পরিধি ও ক্ষেত্রফল"""
import random, pathlib, sys, math
from fractions import Fraction as F
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from mcqlib import Bank, save, E, M, H, fr, num, pfmt, surd, sup

R = random.Random(2026110208)
def W(c, pool):
    out = []
    for w in pool:
        w = str(w)
        if w != str(c) and w not in out: out.append(w)
    return out
def nz(a, b): return R.choice([v for v in range(a, b + 1) if v])
def co(c, s):
    c = F(c)
    if c == 1: return s
    if c == -1: return '−' + s
    return num(c) + s
XY = ('x', 'y'); AB = ('a', 'b')
def p2(d, v=XY): return pfmt({k: c for k, c in d.items() if c}, v) if any(d.values()) else '0'
def px(d): return pfmt({(k,): c for k, c in d.items() if c}, ('x',)) if any(d.values()) else '0'
def tk(v): return f"{v:,} টাকা".replace(',', ',')
def sq(v):
    r = math.isqrt(v); return str(r) if r * r == v else surd(v)

def part(ex, total, fixed, eg, mg, hg):
    need = {E: total // 2, M: total * 2 // 5, H: total // 10}
    b = Bank(ex, R)
    for q, c, w, e, lv in fixed: b.add(q, c, w, e, lv)
    for lv, gs in ((E, eg), (M, mg), (H, hg)):
        tries, miss = 0, {}
        while b.count(lv) < need[lv]:
            tries += 1
            assert tries < 200000, (ex, lv, b.count(lv), need[lv])
            alive = [g for g in gs if miss.get(g.__name__, 0) < 500] or gs
            g = R.choice(alive); before = b.count(lv); g(b, lv)
            miss[g.__name__] = 0 if b.count(lv) > before else miss.get(g.__name__, 0) + 1
    out = []
    for lv in (E, M, H): out += [x for x in b.items if x['lv'] == lv][:need[lv]]
    for x in out: assert len(set(x['o'])) == 4, x
    if ex is None:
        for x in out: x.pop('ex', None)
    return out

# ===================================================== অধ্যায় 1: প্যাটার্ন
fx1 = [
 ("1, 4, 9, 16, … প্যাটার্নটি কোন সংখ্যার?", "বর্গসংখ্যা", ["ঘনসংখ্যা", "মৌলিক সংখ্যা", "বিজোড় সংখ্যা"], "", E),
 ("1, 3, 6, 10, … প্যাটার্নটির সংখ্যাগুলোকে কী বলে?", "ত্রিভুজাকার সংখ্যা", ["বর্গসংখ্যা", "ঘনসংখ্যা", "ফিবোনাচ্চি সংখ্যা"], "", E),
 ("1, 1, 2, 3, 5, 8, … প্যাটার্নটির নাম কী?", "ফিবোনাচ্চি", ["ত্রিভুজাকার", "সমান্তর", "বর্গ"], "আগের দুটি পদের যোগফল।", E),
 ("প্রথম n টি বিজোড় সংখ্যার যোগফল কত?", "n²", ["n(n + 1)", "2n", "n(n + 1)/2"], "", M),
 ("প্রথম n টি স্বাভাবিক সংখ্যার যোগফল কত?", "n(n + 1)/2", ["n²", "n(n − 1)/2", "2n + 1"], "", M),
]
def p1_next(b, lv):
    a, d = R.randint(-20, 40), nz(-12, 15)
    t = [a + i * d for i in range(4)]
    b.add(f"{', '.join(num(x) for x in t)}, … প্যাটার্নের পরবর্তী পদ কত?", num(a + 4 * d), W(num(a + 4 * d), [num(a + 5 * d), num(a + 4 * d + 1), num(a + 3 * d + 2 * d - 1), num(a + 4 * d - d // 2 if d // 2 else a + 4 * d + 2)]), f"প্রতিবার {num(d)} যোগ।", lv)
def p1_geo(b, lv):
    a, r = R.randint(1, 9), R.choice([2, 3, 4, 5, -2, -3])
    t = [a * r ** i for i in range(4)]
    v = a * r ** 4
    b.add(f"{', '.join(num(x) for x in t)}, … প্যাটার্নের পরবর্তী পদ কত?", num(v), W(num(v), [num(v * r), num(t[3] + (t[3] - t[2])), num(-v), num(v + r)]), f"প্রতিবার {num(r)} দিয়ে গুণ।", lv)
def p1_sq(b, lv):
    n = R.randint(5, 40); t = R.choice(['বর্গ', 'ঘন', 'ত্রিভুজাকার'])
    v = {'বর্গ': n * n, 'ঘন': n ** 3, 'ত্রিভুজাকার': n * (n + 1) // 2}[t]
    b.add(f"{n}তম {t}সংখ্যা কত?" if t != 'ত্রিভুজাকার' else f"{n}তম ত্রিভুজাকার সংখ্যা কত?", v, W(v, [n * n if t != 'বর্গ' else n * (n + 1) // 2, n ** 3 if t != 'ঘন' else n * n * 3, v + n, 2 * n]), "", lv)
def p1_nth(b, lv):
    a, d, n = R.randint(-10, 30), nz(-9, 12), R.randint(5, 60)
    v = a + (n - 1) * d
    t = [a + i * d for i in range(3)]
    b.add(f"{', '.join(num(x) for x in t)}, … প্যাটার্নের {n}তম পদ কত?", num(v), W(num(v), [num(a + n * d), num(a + (n - 2) * d), num(n * d), num(v + 1)]), "a + (n − 1)d।", lv)
def p1_fib(b, lv):
    x, y = R.randint(1, 15), R.randint(1, 15)
    t = [x, y]
    for _ in range(4): t.append(t[-1] + t[-2])
    b.add(f"{', '.join(str(v) for v in t[:5])}, … (প্রতিটি পদ আগের দুটি পদের যোগফল) প্যাটার্নের পরবর্তী পদ কত?", t[5], W(t[5], [t[5] + 1, t[4] * 2, t[5] - t[1], t[4] + t[2]]), "", lv)
def p1_formula(b, lv):
    a, d = R.randint(-10, 30), nz(-9, 12)
    t = [a + i * d for i in range(4)]
    ok = px({1: d, 0: a - d}).replace('x', 'n')
    b.add(f"{', '.join(num(x) for x in t)}, … প্যাটার্নের n তম পদ কোনটি?", ok, W(ok, [px({1: d, 0: a}).replace('x', 'n'), px({1: a, 0: d}).replace('x', 'n'), px({1: d, 0: a + d}).replace('x', 'n'), px({1: -d, 0: a - d}).replace('x', 'n')]), "a + (n − 1)d।", lv)
def p1_which(b, lv):
    a, d = R.randint(-10, 30), R.randint(2, 12); n = R.randint(6, 80); v = a + (n - 1) * d
    t = [a + i * d for i in range(3)]
    b.add(f"{', '.join(num(x) for x in t)}, … প্যাটার্নের কততম পদ {num(v)}?", n, W(n, [n + 1, n - 1, n + 2, v // d]), "a + (n − 1)d = মান।", lv)
def p1_sumn(b, lv):
    n = R.randint(5, 200); t = R.choice(['স্বাভাবিক', 'বিজোড়', 'জোড়'])
    v = {'স্বাভাবিক': n * (n + 1) // 2, 'বিজোড়': n * n, 'জোড়': n * (n + 1)}[t]
    b.add(f"প্রথম {n} টি {t} সংখ্যার যোগফল কত?", v, W(v, [n * (n + 1) // 2 if t != 'স্বাভাবিক' else n * n, n * n if t != 'বিজোড়' else n * (n + 1), v + n, v - 1]), "", lv)
def p1_stick(b, lv):
    k, n = R.choice([(3, 'ত্রিভুজ'), (4, 'বর্গ'), (5, 'পঞ্চভুজ'), (6, 'ষড়ভুজ')]), R.randint(3, 50)
    s, shape = k
    v = (s - 1) * n + 1
    b.add(f"পাশাপাশি লাগানো {shape} তৈরিতে প্রথমটিতে {s}টি ও পরে প্রতিটিতে {s - 1}টি করে কাঠি লাগে। {n}টি {shape} তৈরিতে কয়টি কাঠি লাগবে?", v, W(v, [s * n, v + 1, (s - 1) * n, v - s]), f"{s - 1}n + 1।", lv)
def p1_apsum(b, lv):
    a, d, n = R.randint(1, 20), R.randint(1, 9), R.randint(5, 30)
    v = n * (2 * a + (n - 1) * d) // 2
    b.add(f"{a} + {a + d} + {a + 2 * d} + … ধারার প্রথম {n}টি পদের যোগফল কত?", v, W(v, [n * (a + (n - 1) * d), v + d, n * (2 * a + n * d) // 2, v - a]), "(n/2){2a + (n − 1)d}।", lv)
def p1_quad(b, lv):
    a, c, d = R.randint(1, 3), R.randint(-5, 5), R.randint(-5, 10)
    t = [a * n * n + c * n + d for n in range(1, 6)]
    v = a * 36 + c * 6 + d
    b.add(f"{', '.join(num(x) for x in t[:5])}, … প্যাটার্নের পরবর্তী পদ কত?", num(v), W(num(v), [num(2 * t[4] - t[3]), num(v + 2 * a), num(v - 1), num(t[4] + t[1])]), "দ্বিতীয় অন্তর ধ্রুবক।", lv)
def p1_dot(b, lv):
    n = R.randint(3, 30)
    v = 4 * n - 4
    b.add(f"একটি বর্গের প্রতি বাহুতে {n}টি করে বিন্দু (কোণাসহ) থাকলে বর্গের পরিসীমায় মোট কয়টি বিন্দু আছে?", v, W(v, [4 * n, 4 * n - 2, n * n, 4 * n + 4]), "কোণের বিন্দু দুবার গোনা যাবে না।", lv)
K1 = part(None, 300, fx1, [p1_next, p1_geo, p1_sq, p1_nth, p1_fib], [p1_formula, p1_which, p1_sumn, p1_stick, p1_nth, p1_quad], [p1_apsum, p1_quad, p1_dot])
save('k1', K1)

# ===================================================== অধ্যায় 2: মুনাফা
fx21 = [("সরল মুনাফার সূত্র কোনটি?", "I = Pnr", ["I = P(1 + r)ⁿ", "I = P + nr", "I = Pn/r"], "P আসল, n সময়, r হার (দশমিকে)।", E),
        ("মুনাফা-আসল (সবৃদ্ধিমূল) = কত?", "আসল + মুনাফা", ["আসল − মুনাফা", "আসল × মুনাফা", "মুনাফা ÷ আসল"], "", E)]
def i21(b, lv):
    P = R.randint(1, 200) * 500; r = R.randint(2, 15); n = R.randint(1, 8)
    I = P * r * n // 100
    if P * r * n % 100: return
    t = R.choice(['I', 'A'])
    v = I if t == 'I' else P + I
    b.add(f"{P:,} টাকার {r}% হার সরল মুনাফায় {n} বছরের {'মুনাফা' if t == 'I' else 'মুনাফা-আসল'} কত?", tk(v), W(tk(v), [tk(P + I if t == 'I' else I), tk(P * r // 100), tk(v + P // 100), tk(P * (r + 1) * n // 100)]), "I = Pnr/100।", lv)
def i21_rate(b, lv):
    P = R.randint(1, 100) * 1000; r = R.randint(2, 15); n = R.randint(1, 8); I = P * r * n // 100
    b.add(f"{P:,} টাকা {n} বছরে সরল মুনাফায় {I:,} টাকা মুনাফা দিলে মুনাফার হার কত?", f"{r}%", W(f"{r}%", [f"{r + 1}%", f"{r * n}%", f"{r - 1}%" if r > 2 else "20%", f"{r + 2}%"]), "r = I/(Pn) × 100।", lv)
def i21_time(b, lv):
    P = R.randint(1, 100) * 1000; r = R.randint(2, 15); n = R.randint(1, 10); I = P * r * n // 100
    b.add(f"{r}% হার সরল মুনাফায় কত বছরে {P:,} টাকার মুনাফা {I:,} টাকা হবে?", f"{n} বছর", W(f"{n} বছর", [f"{n + 1} বছর", f"{n + 2} বছর", f"{n - 1} বছর" if n > 1 else "12 বছর", f"{r} বছর" if r != n else "15 বছর"]), "n = I/(Pr) × 100।", lv)
def i21_P(b, lv):
    P = R.randint(1, 100) * 1000; r = R.randint(2, 15); n = R.randint(1, 8); I = P * r * n // 100
    b.add(f"কত টাকার {r}% হার সরল মুনাফায় {n} বছরের মুনাফা {I:,} টাকা?", tk(P), W(tk(P), [tk(P + I), tk(P * 2), tk(P // 2), tk(P + 1000)]), "P = I/(nr) × 100।", lv)
def i21_double(b, lv):
    r = R.choice([2, 4, 5, 8, 10, 12, 20, 25]); k = R.choice([2, 3, 4])
    n = F((k - 1) * 100, r)
    b.add(f"সরল মুনাফায় কোনো আসল {r}% হারে কত বছরে {k} গুণ হবে?", f"{num(n)} বছর", W(f"{num(n)} বছর", [f"{num(n * 2)} বছর", f"{num(F(k * 100, r))} বছর", f"{num(n + 5)} বছর", f"{num(n / 2)} বছর"]), "মুনাফা = (k − 1)P।", lv)
def i21_amt(b, lv):
    P = R.randint(1, 50) * 1000; r = R.randint(2, 12); n1, n2 = sorted(R.sample(range(1, 9), 2))
    A1, A2 = P + P * r * n1 // 100, P + P * r * n2 // 100
    b.add(f"কোনো আসল সরল মুনাফায় {n1} বছরে মুনাফা-আসলে {A1:,} টাকা এবং {n2} বছরে {A2:,} টাকা হলে আসল কত?", tk(P), W(tk(P), [tk(A1 - (A2 - A1)), tk(A2 - A1), tk(P + 500), tk(A1)]), "প্রতি বছরের মুনাফা = অন্তর ÷ বছরের অন্তর।", lv)
K21 = part('2.1', 250, fx21, [i21, i21_rate, i21_time, i21_P], [i21, i21_rate, i21_time, i21_P, i21_double], [i21_amt, i21_double])
fx22 = [("চক্রবৃদ্ধি মূলধনের সূত্র কোনটি?", "C = P(1 + r)ⁿ", ["C = P(1 + nr)", "C = Pnr", "C = P + rⁿ"], "", E)]
def i22(b, lv):
    P = R.randint(1, 100) * 100 * 4; r = R.choice([5, 10, 20, 4, 8, 2]); n = R.choice([1, 2, 2, 3])
    C = F(P) * (1 + F(r, 100)) ** n
    if C.denominator != 1: return
    t = R.choice(['C', 'I'])
    v = int(C) if t == 'C' else int(C) - P
    b.add(f"{P:,} টাকার {r}% হার চক্রবৃদ্ধি মুনাফায় {n} বছরের {'চক্রবৃদ্ধি মূলধন' if t == 'C' else 'চক্রবৃদ্ধি মুনাফা'} কত?", tk(v), W(tk(v), [tk(int(C) - P if t == 'C' else int(C)), tk(P + P * r * n // 100 if t == 'C' else P * r * n // 100), tk(v + P // 100), tk(v - r)]), "C = P(1 + r/100)ⁿ।", lv)
def i22_diff(b, lv):
    P = R.randint(1, 100) * 100; r = R.choice([5, 10, 20, 4, 2])
    d = F(P * r * r, 10000)
    if d.denominator != 1: return
    b.add(f"{P:,} টাকার {r}% হারে 2 বছরের চক্রবৃদ্ধি মুনাফা ও সরল মুনাফার পার্থক্য কত?", tk(int(d)), W(tk(int(d)), [tk(int(d) * 2), tk(P * r // 100), tk(int(d) + r), tk(int(d) // 2 if d > 1 else 3)]), "P(r/100)²।", lv)
def i22_pop(b, lv):
    p = R.randint(1, 90) * 10000; r = R.choice([2, 5, 10, 4]); n = R.choice([1, 2])
    v = F(p) * (1 + F(r, 100)) ** n
    if v.denominator != 1: return
    b.add(f"একটি শহরের বর্তমান জনসংখ্যা {p:,}। জনসংখ্যা বৃদ্ধির হার বার্ষিক {r}% হলে {n} বছর পর জনসংখ্যা কত হবে?", f"{int(v):,}", W(f"{int(v):,}", [f"{p + p * r * n // 100:,}" if n > 1 else f"{p + p * r // 50:,}", f"{p * r // 100:,}", f"{int(v) + 100:,}", f"{p:,}"]), "P(1 + r)ⁿ।", lv)
def i22_dep(b, lv):
    p = R.randint(1, 90) * 10000; r = R.choice([10, 5, 20]); n = R.choice([1, 2])
    v = F(p) * (1 - F(r, 100)) ** n
    if v.denominator != 1: return
    b.add(f"একটি যন্ত্রের মূল্য {p:,} টাকা। প্রতি বছর মূল্য {r}% হ্রাস পেলে {n} বছর পর মূল্য কত হবে?", tk(int(v)), W(tk(int(v)), [tk(p - p * r * n // 100) if n > 1 else tk(p - p * r // 50), tk(p * r // 100), tk(int(v) + 500), tk(int(F(p) * (1 + F(r, 100)) ** n))]), "P(1 − r)ⁿ।", lv)
K22 = part('2.2', 250, fx22, [i22, i22_pop, i22_dep], [i22, i22_diff, i22_pop, i22_dep], [i22_diff, i22_dep, i22])
save('k2', K21 + K22)

# ===================================================== অধ্যায় 3: পরিমাপ
fx3 = [("1 হেক্টর = কত বর্গমিটার?", "10000", ["1000", "100", "100000"], "", E), ("1 ঘনমিটার = কত লিটার?", "1000", ["100", "10", "10000"], "", E),
       ("1 লিটার = কত ঘন সেন্টিমিটার?", "1000", ["100", "10", "10000"], "", E), ("1 কুইন্টাল = কত কেজি?", "100", ["1000", "10", "50"], "", E),
       ("1 মেট্রিক টন = কত কেজি?", "1000", ["100", "10000", "500"], "", E)]
U = [('কিলোমিটার', 'মিটার', 1000), ('মিটার', 'সেন্টিমিটার', 100), ('সেন্টিমিটার', 'মিলিমিটার', 10), ('কিলোগ্রাম', 'গ্রাম', 1000), ('লিটার', 'মিলিলিটার', 1000), ('মেট্রিক টন', 'কিলোগ্রাম', 1000), ('বর্গমিটার', 'বর্গসেন্টিমিটার', 10000), ('হেক্টর', 'বর্গমিটার', 10000)]
def m3_conv(b, lv):
    a, c, k = R.choice(U); v = F(R.randint(1, 999), R.choice([1, 1, 10, 100]))
    if R.random() < .5:
        q, ans = f"{num(v)} {a} = কত {c}?", num(v * k)
        ws = [num(v * k * 10), num(v * k / 10), num(v * k + k)]
    else:
        q, ans = f"{num(v * k)} {c} = কত {a}?", num(v)
        ws = [num(v * 10), num(v / 10), num(v + 1)]
    b.add(q, ans, W(ans, ws), "", lv)
def m3_rect(b, lv):
    l, w = R.randint(2, 80), R.randint(2, 60); t = R.choice(['ক্ষেত্রফল', 'পরিসীমা'])
    v = l * w if t == 'ক্ষেত্রফল' else 2 * (l + w)
    b.add(f"একটি আয়তক্ষেত্রের দৈর্ঘ্য {l} মিটার ও প্রস্থ {w} মিটার হলে এর {t} কত?", f"{v} {'বর্গমিটার' if t == 'ক্ষেত্রফল' else 'মিটার'}", W(f"{v} {'বর্গমিটার' if t == 'ক্ষেত্রফল' else 'মিটার'}", [f"{2 * (l + w) if t == 'ক্ষেত্রফল' else l * w} {'বর্গমিটার' if t == 'ক্ষেত্রফল' else 'মিটার'}", f"{v + l} {'বর্গমিটার' if t == 'ক্ষেত্রফল' else 'মিটার'}", f"{l + w} {'বর্গমিটার' if t == 'ক্ষেত্রফল' else 'মিটার'}"]), "", lv)
def m3_sq(b, lv):
    a = R.randint(2, 99); t = R.choice(['ক্ষেত্রফল', 'পরিসীমা', 'কর্ণ'])
    if t == 'কর্ণ': ok, ws = f"{a}√2 সেমি", [f"{2 * a} সেমি", f"{a * a} সেমি", f"{a}√3 সেমি"]
    elif t == 'ক্ষেত্রফল': ok, ws = f"{a * a} বর্গসেমি", [f"{4 * a} বর্গসেমি", f"{2 * a} বর্গসেমি", f"{a * a + a} বর্গসেমি"]
    else: ok, ws = f"{4 * a} সেমি", [f"{a * a} সেমি", f"{2 * a} সেমি", f"{4 * a + 4} সেমি"]
    b.add(f"{a} সেমি বাহুবিশিষ্ট বর্গের {t} কত?", ok, W(ok, ws), "", lv)
def m3_vol(b, lv):
    l, w, h = R.randint(2, 30), R.randint(2, 25), R.randint(2, 20)
    v = l * w * h
    b.add(f"একটি আয়তাকার ঘনবস্তুর দৈর্ঘ্য {l} সেমি, প্রস্থ {w} সেমি ও উচ্চতা {h} সেমি হলে আয়তন কত?", f"{v} ঘনসেমি", W(f"{v} ঘনসেমি", [f"{2 * (l * w + w * h + h * l)} ঘনসেমি", f"{l + w + h} ঘনসেমি", f"{v + l * w} ঘনসেমি"]), "দৈর্ঘ্য × প্রস্থ × উচ্চতা।", lv)
def m3_cube(b, lv):
    a = R.randint(2, 30); t = R.choice(['আয়তন', 'সমগ্রতলের ক্ষেত্রফল'])
    v, u = (a ** 3, 'ঘনসেমি') if t == 'আয়তন' else (6 * a * a, 'বর্গসেমি')
    b.add(f"{a} সেমি ধারবিশিষ্ট ঘনকের {t} কত?", f"{v} {u}", W(f"{v} {u}", [f"{6 * a * a if t == 'আয়তন' else a ** 3} {u}", f"{4 * a * a} {u}", f"{v + a} {u}"]), "", lv)
def m3_tank(b, lv):
    l, w, h = R.randint(1, 6), R.randint(1, 5), R.randint(1, 4)
    v = l * w * h * 1000
    b.add(f"একটি চৌবাচ্চার দৈর্ঘ্য {l} মিটার, প্রস্থ {w} মিটার ও গভীরতা {h} মিটার। এতে কত লিটার পানি ধরবে?", f"{v:,} লিটার", W(f"{v:,} লিটার", [f"{v // 10:,} লিটার", f"{v * 10:,} লিটার", f"{l * w * h:,} লিটার"]), "1 ঘনমিটার = 1000 লিটার।", lv)
def m3_path(b, lv):
    l, w, p = R.randint(10, 80), R.randint(8, 60), R.randint(1, 5)
    v = (l + 2 * p) * (w + 2 * p) - l * w
    b.add(f"{l} মিটার দীর্ঘ ও {w} মিটার প্রস্থ একটি বাগানের বাইরে চারদিকে {p} মিটার চওড়া রাস্তা আছে। রাস্তার ক্ষেত্রফল কত?", f"{v} বর্গমিটার", W(f"{v} বর্গমিটার", [f"{2 * p * (l + w)} বর্গমিটার", f"{v + 4 * p * p} বর্গমিটার", f"{l * w - (l - 2 * p) * (w - 2 * p)} বর্গমিটার"]), "বাইরের ক্ষেত্রফল − ভেতরের ক্ষেত্রফল।", lv)
def m3_cost(b, lv):
    l, w, c = R.randint(3, 30), R.randint(3, 25), R.randint(2, 50) * 10
    v = l * w * c
    b.add(f"{l} মিটার দীর্ঘ ও {w} মিটার প্রস্থ একটি মেঝেতে প্রতি বর্গমিটার {c} টাকা দরে কার্পেট বিছাতে মোট খরচ কত?", tk(v), W(tk(v), [tk(2 * (l + w) * c), tk(v + c), tk(l * w)]), "", lv)
def m3_wall(b, lv):
    l, w, h = R.randint(3, 15), R.randint(3, 12), R.randint(2, 5)
    v = 2 * (l + w) * h
    b.add(f"একটি ঘরের দৈর্ঘ্য {l} মিটার, প্রস্থ {w} মিটার ও উচ্চতা {h} মিটার হলে চার দেয়ালের ক্ষেত্রফল কত?", f"{v} বর্গমিটার", W(f"{v} বর্গমিটার", [f"{l * w * h} বর্গমিটার", f"{v + l * w} বর্গমিটার", f"{(l + w) * h} বর্গমিটার"]), "2(দৈর্ঘ্য + প্রস্থ) × উচ্চতা।", lv)
def m3_findw(b, lv):
    l, w = R.randint(5, 80), R.randint(3, 60)
    b.add(f"একটি আয়তক্ষেত্রের ক্ষেত্রফল {l * w} বর্গমিটার ও দৈর্ঘ্য {l} মিটার হলে পরিসীমা কত?", f"{2 * (l + w)} মিটার", W(f"{2 * (l + w)} মিটার", [f"{w} মিটার", f"{l + w} মিটার", f"{2 * (l + w) + 2} মিটার"]), f"প্রস্থ = {w} মিটার।", lv)
K3 = part(None, 300, fx3, [m3_conv, m3_rect, m3_sq, m3_vol, m3_cube], [m3_vol, m3_cube, m3_tank, m3_path, m3_cost, m3_wall, m3_findw], [m3_path, m3_wall, m3_findw, m3_tank])
save('k3', K3)

# ===================================================== অধ্যায় 4: বীজগাণিতিক সূত্রাবলি
fx41 = [("(a + b)² = কত?", "a² + 2ab + b²", ["a² + b²", "a² − 2ab + b²", "a² + ab + b²"], "", E), ("(a − b)² = কত?", "a² − 2ab + b²", ["a² + 2ab + b²", "a² − b²", "a² + b²"], "", E),
        ("a² − b² = কত?", "(a + b)(a − b)", ["(a − b)²", "(a + b)²", "a(a − b)"], "", E), ("(a + b)² − (a − b)² = কত?", "4ab", ["2ab", "2(a² + b²)", "0"], "", E), ("(a + b)² + (a − b)² = কত?", "2(a² + b²)", ["4ab", "a² + b²", "2ab"], "", E)]
def f41_exp(b, lv):
    p, q = R.randint(1, 9), R.randint(1, 9); s = R.choice([1, -1])
    ok = p2({(2, 0): p * p, (1, 1): 2 * p * q * s, (0, 2): q * q})
    b.add(f"({co(p, 'x')} {'+' if s > 0 else '−'} {co(q, 'y')})² = কত?", ok, W(ok, [p2({(2, 0): p * p, (0, 2): q * q}), p2({(2, 0): p * p, (1, 1): -2 * p * q * s, (0, 2): q * q}), p2({(2, 0): p * p, (1, 1): p * q * s, (0, 2): q * q})]), "", lv)
def f41_num(b, lv):
    n = R.choice([R.randint(11, 99), R.randint(101, 999)]); k = R.choice([1, 2, 3, 5])
    b.add(f"সূত্রের সাহায্যে {n}² = কত?", n * n, W(n * n, [n * n + 1, n * n - 10, n * 2 * 10, (n + 1) * (n - 1)]), "(a ± b)² ব্যবহার করে।", lv)
def f41_ab(b, lv):
    a, c = R.sample(range(-12, 13), 2); s, p = a + c, a * c
    t = R.choice(['sum', 'diff'])
    if t == 'sum': q, v = f"a + b = {num(s)} এবং ab = {num(p)} হলে a² + b² = কত?", s * s - 2 * p
    else: q, v = f"a − b = {num(a - c)} এবং ab = {num(p)} হলে a² + b² = কত?", (a - c) ** 2 + 2 * p
    b.add(q, num(v), W(num(v), [num(v + 2 * p) if p else num(v + 2), num(v - 2 * p) if p else num(v - 2), num(v + 1), num(s * s)]), "", lv)
def f41_diff(b, lv):
    a, c = R.sample(range(11, 120), 2)
    v = a * a - c * c
    b.add(f"{a}² − {c}² = কত?", num(v), W(num(v), [num((a - c) ** 2), num(v + 1), num(a - c), num(-v)]), "(a + b)(a − b)।", lv)
def f41_prod(b, lv):
    n, k = R.randint(20, 200), R.randint(1, 9)
    v = (n + k) * (n - k)
    b.add(f"{n + k} × {n - k} = কত?", v, W(v, [n * n, v + k * k * 2, n * n + k * k, v - 1]), f"{n}² − {k}²।", lv)
def f41_4ab(b, lv):
    a, c = R.sample(range(-12, 13), 2)
    s, d = a + c, a - c
    b.add(f"a + b = {num(s)} এবং a − b = {num(d)} হলে ab = কত?", num(a * c), W(num(a * c), [num(s * d), num((s * s + d * d) // 2), num(a * c + 1), num(-a * c) if a * c else '1']), "4ab = (a + b)² − (a − b)²।", lv)
def f41_x1x(b, lv):
    k = R.randint(2, 15)
    t = R.choice(['p', 'm'])
    v = k * k - 2 if t == 'p' else k * k + 2
    b.add(f"x {'+' if t == 'p' else '−'} 1/x = {k} হলে x² + 1/x² = কত?", v, W(v, [k * k, k * k + 2 if t == 'p' else k * k - 2, 2 * k, v + 1]), "", lv)
K41 = part('4.1', 250, fx41, [f41_exp, f41_num, f41_diff, f41_prod], [f41_ab, f41_4ab, f41_x1x, f41_exp, f41_prod], [f41_ab, f41_x1x, f41_4ab])
fx42 = [("(a + b)³ = কত?", "a³ + 3a²b + 3ab² + b³", ["a³ + b³", "a³ + 3ab + b³", "a³ + 3a²b + b³"], "", E), ("a³ + b³ = কত?", "(a + b)(a² − ab + b²)", ["(a + b)(a² + ab + b²)", "(a + b)³", "(a − b)(a² + ab + b²)"], "", E),
        ("a³ − b³ = কত?", "(a − b)(a² + ab + b²)", ["(a − b)(a² − ab + b²)", "(a − b)³", "(a + b)(a² + ab + b²)"], "", E)]
def f42_exp(b, lv):
    p, q = R.randint(1, 5), R.randint(1, 5); s = R.choice([1, -1])
    ok = p2({(3, 0): p ** 3, (2, 1): 3 * p * p * q * s, (1, 2): 3 * p * q * q, (0, 3): q ** 3 * s})
    b.add(f"({co(p, 'x')} {'+' if s > 0 else '−'} {co(q, 'y')})³ = কত?", ok, W(ok, [p2({(3, 0): p ** 3, (0, 3): q ** 3 * s}), p2({(3, 0): p ** 3, (2, 1): 3 * p * p * q, (1, 2): 3 * p * q * q, (0, 3): q ** 3}) if s < 0 else p2({(3, 0): p ** 3, (2, 1): -3 * p * p * q, (1, 2): 3 * p * q * q, (0, 3): -q ** 3}), p2({(3, 0): p ** 3, (2, 1): p * p * q * s, (1, 2): p * q * q, (0, 3): q ** 3 * s})]), "", lv)
def f42_val(b, lv):
    a, c = R.sample(range(-8, 9), 2); s, p = a + c, a * c
    t = R.choice(['p', 'm'])
    if t == 'p': q, v = f"a + b = {num(s)} এবং ab = {num(p)} হলে a³ + b³ = কত?", s ** 3 - 3 * p * s
    else: q, v = f"a − b = {num(a - c)} এবং ab = {num(p)} হলে a³ − b³ = কত?", (a - c) ** 3 + 3 * p * (a - c)
    b.add(q, num(v), W(num(v), [num(s ** 3 if t == 'p' else (a - c) ** 3), num(v + 3 * p) if p else num(v + 3), num(-v) if v else '1', num(v + 1)]), "", lv)
def f42_cube(b, lv):
    n = R.randint(11, 60)
    b.add(f"সূত্রের সাহায্যে {n}³ = কত?", n ** 3, W(n ** 3, [n ** 3 + n, n * n * 3, n ** 3 - 10, (n + 1) ** 3]), "(a ± b)³।", lv)
def f42_x1x(b, lv):
    k = R.randint(2, 12); t = R.choice(['p', 'm'])
    v = k ** 3 - 3 * k if t == 'p' else k ** 3 + 3 * k
    b.add(f"x {'+' if t == 'p' else '−'} 1/x = {k} হলে x³ {'+' if t == 'p' else '−'} 1/x³ = কত?", v, W(v, [k ** 3, k ** 3 + 3 * k if t == 'p' else k ** 3 - 3 * k, 3 * k, v + 1]), "", lv)
def f42_sum(b, lv):
    a, c = R.randint(2, 30), R.randint(2, 30)
    v = a ** 3 + c ** 3
    b.add(f"({a} + {c})({a}² − {a}·{c} + {c}²) = কত?", v, W(v, [a ** 3 - c ** 3, (a + c) ** 3, v + 1, a * a + c * c]), "a³ + b³।", lv)
K42 = part('4.2', 250, fx42, [f42_exp, f42_cube, f42_sum], [f42_val, f42_x1x, f42_exp, f42_sum], [f42_val, f42_x1x])
fx43 = []
def f43_quad(b, lv):
    r1, r2 = R.sample([v for v in range(-12, 13) if v], 2)
    s, p = -(r1 + r2), r1 * r2
    def fac(r): return f"(x {'+' if r > 0 else '−'} {abs(r)})"
    ok = fac(r1) + fac(r2)
    b.add(f"{px({2: 1, 1: s, 0: p})}-এর উৎপাদক কোনটি?", ok, W(ok, [fac(-r1) + fac(-r2), fac(r1) + fac(-r2), fac(-r1) + fac(r2), fac(r1 + r2 if r1 + r2 else 1) + fac(1)]), "যোগফল ও গুণফল মিলিয়ে।", lv)
def f43_dsq(b, lv):
    p, q = R.randint(1, 12), R.randint(1, 12)
    ok = f"({co(p, 'x')} + {co(q, 'y')})({co(p, 'x')} − {co(q, 'y')})"
    b.add(f"{p2({(2, 0): p * p, (0, 2): -q * q})}-এর উৎপাদক কোনটি?", ok, W(ok, [f"({co(p, 'x')} − {co(q, 'y')})²", f"({co(p, 'x')} + {co(q, 'y')})²", f"({co(p * p, 'x')} + {co(q, 'y')})({co(p, 'x')} − {co(q, 'y')})"]), "a² − b²।", lv)
def f43_common(b, lv):
    a, c, k = R.randint(1, 9), R.randint(1, 9), R.randint(2, 9)
    if math.gcd(a, c) != 1: return
    ok = f"{k}x({co(a, 'x')} + {co(c, 'y')})"
    b.add(f"{p2({(2, 0): k * a, (1, 1): k * c})}-এর উৎপাদক কোনটি?", ok, W(ok, [f"{k}({co(a, 'x²')} + {co(c, 'xy')})" if True else '', f"x({co(k * a, 'x')} + {co(c, 'y')})", f"{k}x({co(a, 'x')} − {co(c, 'y')})"]), "সাধারণ উৎপাদক বের করে।", lv)
def f43_ax2(b, lv):
    a, c = R.choice([2, 3, 5]), R.choice([1, 2, 3])
    r = nz(-6, 6)
    # (a x + c)(x + r)
    s, p = a * r + c, c * r
    def f(x, y): return f"({co(x, 'x')} {'+' if y > 0 else '−'} {abs(y)})"
    ok = f(a, c) + f(1, r)
    b.add(f"{px({2: a, 1: s, 0: p})}-এর উৎপাদক কোনটি?", ok, W(ok, [f(a, -c) + f(1, -r), f(a, r) + f(1, c) if r != c else f(a, c + 1) + f(1, r), f(a, -c) + f(1, r), f(1, c) + f(a, r)]), "মধ্যপদ বিভক্তি।", lv)
def f43_cube(b, lv):
    p, q = R.randint(1, 6), R.randint(1, 6); s = R.choice([1, -1])
    if s > 0: ok = f"({co(p, 'x')} + {co(q, 'y')})({p2({(2, 0): p * p, (1, 1): -p * q, (0, 2): q * q})})"; w = f"({co(p, 'x')} + {co(q, 'y')})({p2({(2, 0): p * p, (1, 1): p * q, (0, 2): q * q})})"
    else: ok = f"({co(p, 'x')} − {co(q, 'y')})({p2({(2, 0): p * p, (1, 1): p * q, (0, 2): q * q})})"; w = f"({co(p, 'x')} − {co(q, 'y')})({p2({(2, 0): p * p, (1, 1): -p * q, (0, 2): q * q})})"
    b.add(f"{p2({(3, 0): p ** 3, (0, 3): s * q ** 3})}-এর উৎপাদক কোনটি?", ok, W(ok, [w, f"({co(p, 'x')} {'+' if s > 0 else '−'} {co(q, 'y')})³", f"({co(p, 'x')} {'−' if s > 0 else '+'} {co(q, 'y')})({p2({(2, 0): p * p, (0, 2): q * q})})"]), "a³ ± b³।", lv)
K43 = part('4.3', 250, fx43, [f43_quad, f43_dsq, f43_common], [f43_quad, f43_ax2, f43_dsq, f43_cube], [f43_ax2, f43_cube])
fx44 = []
def mono(c, a, b_):
    s = co(c, '') if c != 1 else ''
    s = (str(c) if c != 1 else '') + (('a' + (sup(a) if a > 1 else '')) if a else '') + (('b' + (sup(b_) if b_ > 1 else '')) if b_ else '')
    return s or '1'
def f44(b, lv):
    c1, c2 = R.randint(2, 60), R.randint(2, 60); a1, a2, b1, b2 = R.randint(0, 5), R.randint(0, 5), R.randint(0, 5), R.randint(0, 5)
    if (a1 + b1) == 0 or (a2 + b2) == 0: return
    t = R.choice(['গ.সা.গু.', 'ল.সা.গু.'])
    if t == 'গ.সা.গু.': ok = mono(math.gcd(c1, c2), min(a1, a2), min(b1, b2)); w = mono(c1 * c2 // math.gcd(c1, c2), max(a1, a2), max(b1, b2))
    else: ok = mono(c1 * c2 // math.gcd(c1, c2), max(a1, a2), max(b1, b2)); w = mono(math.gcd(c1, c2), min(a1, a2), min(b1, b2))
    b.add(f"{mono(c1, a1, b1)} ও {mono(c2, a2, b2)}-এর {t} কত?", ok, W(ok, [w, mono(c1 * c2, a1 + a2, b1 + b2), mono(math.gcd(c1, c2), max(a1, a2), max(b1, b2)) if t == 'গ.সা.গু.' else mono(c1 * c2 // math.gcd(c1, c2), min(a1, a2), min(b1, b2)), mono(c1 + c2, max(a1, a2), max(b1, b2))]), "সহগের গ.সা.গু./ল.সা.গু. ও চলকের ক্ষুদ্রতম/বৃহত্তম ঘাত।", lv)
def f44_poly(b, lv):
    r1, r2, r3 = R.sample([v for v in range(-9, 10) if v], 3)
    def fac(r): return f"(x {'+' if r > 0 else '−'} {abs(r)})"
    t = R.choice(['গ.সা.গু.', 'ল.সা.গু.'])
    e1, e2 = px({2: 1, 1: -(r1 + r2), 0: r1 * r2}), px({2: 1, 1: -(r1 + r3), 0: r1 * r3})
    ok = fac(-r1) if t == 'গ.সা.গু.' else fac(-r1) + fac(-r2) + fac(-r3)
    b.add(f"{e1} ও {e2}-এর {t} কত?", ok, W(ok, [fac(r1), fac(-r2), fac(-r1) + fac(-r2) + fac(-r3) if t == 'গ.সা.গু.' else fac(-r1), fac(-r2) + fac(-r3)]), "উৎপাদকে বিশ্লেষণ করে।", lv)
K44 = part('4.4', 250, fx44, [f44], [f44, f44_poly], [f44_poly])
save('k4', K41 + K42 + K43 + K44)

# ===================================================== অধ্যায় 5: বীজগাণিতিক ভগ্নাংশ
def lx(r): return f"x {'+' if r > 0 else '−'} {abs(r)}" if r else 'x'
def f51_red(b, lv):
    a = R.randint(1, 15); t = R.choice(['m', 'p', 'k'])
    if t == 'm': q, ok, w = f"(x² − {a * a})/(x − {a})", f"x + {a}", [f"x − {a}", f"x² + {a}", f"1/(x + {a})"]
    elif t == 'p': q, ok, w = f"(x² + {2 * a}x + {a * a})/(x + {a})", f"x + {a}", [f"x − {a}", f"(x + {a})²", f"x + {2 * a}"]
    else:
        k = R.randint(2, 12); q, ok, w = f"{k}x/({k}x² + {k * a}x)", f"1/(x + {a})", [f"x/(x + {a})", f"{k}/(x + {a})", f"1/(x + {k * a})"]
    b.add(f"{q}-কে লঘিষ্ঠ আকারে প্রকাশ করলে কোনটি?", ok, W(ok, w), "লব ও হরের সাধারণ উৎপাদক বাদ দিয়ে।", lv)
def f51_mono(b, lv):
    c1, c2 = R.randint(2, 40), R.randint(2, 40); p1, p2_, q1, q2 = R.randint(1, 6), R.randint(1, 6), R.randint(1, 6), R.randint(1, 6)
    g = math.gcd(c1, c2); n, d = c1 // g, c2 // g
    xn, yn = p1 - p2_, q1 - q2
    num_ = (str(n) if n > 1 else '') + (('x' + (sup(xn) if xn > 1 else '')) if xn > 0 else '') + (('y' + (sup(yn) if yn > 1 else '')) if yn > 0 else '')
    den = (str(d) if d > 1 else '') + (('x' + (sup(-xn) if -xn > 1 else '')) if xn < 0 else '') + (('y' + (sup(-yn) if -yn > 1 else '')) if yn < 0 else '')
    ok = (num_ or '1') + (f"/{den}" if den else '')
    def m(c, a, bb): return str(c) + ('x' + (sup(a) if a > 1 else '')) + ('y' + (sup(bb) if bb > 1 else ''))
    b.add(f"{m(c1, p1, q1)}/{m(c2, p2_, q2)}-কে লঘিষ্ঠ আকারে প্রকাশ করো।", ok, W(ok, [(den or '1') + (f"/{num_}" if num_ else ''), f"{c1}/{c2}", ok + 'x', (num_ or '1') + f"/{d * 2}"]), "", lv)
def f51_cd(b, lv):
    a, c = R.sample([v for v in range(-9, 10) if v], 2)
    ok = f"({lx(a)})({lx(c)})"
    b.add(f"1/({lx(a)}) ও 1/({lx(c)}) ভগ্নাংশদ্বয়ের সাধারণ হর কোনটি?", ok, W(ok, [f"{lx(a)} + {lx(c)}".replace('x + x', '2x'), f"({lx(-a)})({lx(-c)})", f"({lx(a)})²"]), "হরগুলোর ল.সা.গু.।", lv)
def f51_val(b, lv):
    a = R.randint(1, 9); x = R.choice([v for v in range(-9, 10) if v != a and v != -a])
    v = F(x * x - a * a, x - a)
    b.add(f"x = {num(x)} হলে (x² − {a * a})/(x − {a})-এর মান কত?", num(v), W(num(v), [num(x - a), num(v + 1), num(x * x - a * a), num(-v) if v else '1']), f"x + {a}।", lv)
K51 = part('5.1', 250, [], [f51_red, f51_mono, f51_cd, f51_val], [f51_red, f51_mono, f51_cd, f51_val], [f51_mono, f51_red])
def f52_add(b, lv):
    p, q, k = R.randint(1, 20), R.randint(1, 20), R.randint(2, 9); op = R.choice(['+', '−'])
    v = p + q if op == '+' else p - q
    ok = f"{num(v)}/{k}x" if v else '0'
    g = math.gcd(abs(v), k) if v else 1
    ok = (f"{num(v // g)}/{k // g}x" if k // g > 1 else f"{num(v // g)}/x") if v else '0'
    b.add(f"{p}/{k}x {op} {q}/{k}x = কত?", ok, W(ok, [f"{num(p + q if op == '−' else p - q)}/{k}x", f"{num(v)}/{2 * k}x" if v else '1/x', f"{p * q}/{k}x"]), "হর একই হলে লব যোগ/বিয়োগ।", lv)
def f52_two(b, lv):
    a = R.randint(1, 12); t = R.choice(['m', 'p'])
    if t == 'm': q, ok, w = f"1/(x − {a}) − 1/(x + {a})", f"{2 * a}/(x² − {a * a})", [f"2x/(x² − {a * a})", f"{2 * a}/(x² + {a * a})", "0"]
    else: q, ok, w = f"1/(x − {a}) + 1/(x + {a})", f"2x/(x² − {a * a})", [f"{2 * a}/(x² − {a * a})", f"2/(x² − {a * a})", f"2x/(x² + {a * a})"]
    b.add(f"{q} = কত?", ok, W(ok, w), "সাধারণ হর (x² − a²)।", lv)
def f52_mul(b, lv):
    a, c = R.randint(1, 12), R.randint(1, 12)
    q = f"(x² − {a * a})/(x + {c}) × (x + {c})/(x − {a})"
    ok = f"x + {a}"
    b.add(f"{q} = কত?", ok, W(ok, [f"x − {a}", f"x + {c}", f"(x + {a})/(x + {c})"]), "", lv)
def f52_div(b, lv):
    p, q, r, s = R.randint(2, 9), R.randint(2, 9), R.randint(2, 9), R.randint(2, 9)
    if F(p * s, q * r) == 1: return
    v = F(p * s, q * r)
    ok = f"{fr(v)}" if v.denominator == 1 else f"{v.numerator}/{v.denominator}"
    b.add(f"({p}x/{q}y) ÷ ({r}x/{s}y) = কত?", ok, W(ok, [fr(F(p * r, q * s)), fr(1 / v) if v != 1 else '2', f"{fr(v)}x", fr(v + 1)]), "ভাজকের বিপরীত দিয়ে গুণ।", lv)
def f52_val(b, lv):
    a = R.randint(1, 9); x = R.choice([v for v in range(-12, 13) if abs(v) != a])
    v = F(2 * a, x * x - a * a)
    b.add(f"x = {num(x)} হলে 1/(x − {a}) − 1/(x + {a})-এর মান কত?", fr(v).replace('-', '−'), W(fr(v).replace('-', '−'), [fr(-v).replace('-', '−'), fr(F(2 * x, x * x - a * a)).replace('-', '−'), fr(v * 2).replace('-', '−'), '0']), "", lv)
K52 = part('5.2', 250, [], [f52_add, f52_div, f52_mul], [f52_two, f52_div, f52_mul, f52_val, f52_add], [f52_val, f52_two])
save('k5', K51 + K52)

# ===================================================== অধ্যায় 6: সরল সহসমীকরণ
def lin(a, c): return p2({(1, 0): a, (0, 1): c})
def f61_solve(b, lv):
    x, y = R.randint(-9, 9), R.randint(-9, 9); a1, b1, a2, b2 = nz(-6, 6), nz(-6, 6), nz(-6, 6), nz(-6, 6)
    if a1 * b2 == a2 * b1: return
    ok = f"({num(x)}, {num(y)})"
    b.add(f"{lin(a1, b1)} = {num(a1 * x + b1 * y)}, {lin(a2, b2)} = {num(a2 * x + b2 * y)} সমীকরণজোটের সমাধান (x, y) কত?", ok, W(ok, [f"({num(y)}, {num(x)})", f"({num(-x)}, {num(y)})" if x else f"(1, {num(y)})", f"({num(x)}, {num(-y)})" if y else f"({num(x)}, 1)", f"({num(x + 1)}, {num(y)})"]), "অপনয়ন বা প্রতিস্থাপন পদ্ধতি।", lv)
def f61_simple(b, lv):
    x, y = R.randint(-15, 15), R.randint(-15, 15)
    ok = f"({num(x)}, {num(y)})"
    b.add(f"x + y = {num(x + y)} এবং x − y = {num(x - y)} হলে (x, y) = কত?", ok, W(ok, [f"({num(y)}, {num(x)})", f"({num(x + y)}, {num(x - y)})", f"({num(-x)}, {num(-y)})" if x or y else '(1, 1)', f"({num(x + 1)}, {num(y - 1)})"]), "যোগ ও বিয়োগ করে।", lv)
def f61_check(b, lv):
    x, y = R.randint(-9, 9), R.randint(-9, 9); a, c = nz(-6, 6), nz(-6, 6)
    k = a * x + c * y
    ok = f"({num(x)}, {num(y)})"
    b.add(f"নিচের কোন বিন্দুটি {lin(a, c)} = {num(k)} সমীকরণকে সিদ্ধ করে?", ok, W(ok, [f"({num(x + 1)}, {num(y)})", f"({num(x)}, {num(y + 1)})", f"({num(y)}, {num(x)})" if a * y + c * x != k else f"({num(x + 2)}, {num(y)})", f"({num(-x)}, {num(-y)})" if k != 0 and (x or y) else f"({num(x + 3)}, {num(y)})"]), "মান বসিয়ে যাচাই।", lv)
def f61_nature(b, lv):
    a, c = nz(-6, 6), nz(-6, 6); k = R.choice([2, 3, -2]); t = R.choice(['inf', 'none', 'one'])
    d1, d2 = R.randint(-9, 9), R.randint(-9, 9)
    if t == 'inf': e2, ok = f"{lin(k * a, k * c)} = {num(k * d1)}", 'অসংখ্য সমাধান'
    elif t == 'none':
        if k * d1 == d2: return
        e2, ok = f"{lin(k * a, k * c)} = {num(d2)}", 'কোনো সমাধান নেই'
    else:
        e, f_ = nz(-6, 6), nz(-6, 6)
        if a * f_ == c * e: return
        e2, ok = f"{lin(e, f_)} = {num(d2)}", 'একটিমাত্র সমাধান'
    b.add(f"{lin(a, c)} = {num(d1)} এবং {e2} সমীকরণজোটের সমাধান সম্পর্কে কোনটি সঠিক?", ok, ['অসংখ্য সমাধান', 'কোনো সমাধান নেই', 'একটিমাত্র সমাধান', 'দুটি সমাধান'], "সহগের অনুপাত তুলনা।", lv)
K61 = part('6.1', 250, [], [f61_simple, f61_check, f61_solve], [f61_solve, f61_simple, f61_nature, f61_check], [f61_solve, f61_nature])
def f62_num(b, lv):
    x, y = sorted(R.sample(range(1, 100), 2), reverse=True)
    ok = f"{x} ও {y}"
    b.add(f"দুটি সংখ্যার যোগফল {x + y} এবং বিয়োগফল {x - y}। সংখ্যা দুটি কত?", ok, W(ok, [f"{x + 1} ও {y - 1}", f"{x + y} ও {x - y}", f"{x} ও {y + 1}", f"{y} ও {y}"]), "", lv)
def f62_age(b, lv):
    f_, s = R.randint(30, 70), R.randint(3, 25); k = R.randint(2, 10)
    if f_ <= s: return
    ok = f"{f_} বছর ও {s} বছর"
    b.add(f"পিতা ও পুত্রের বর্তমান বয়সের সমষ্টি {f_ + s} বছর। {k} বছর পর তাদের বয়সের পার্থক্য হবে {f_ - s} বছর এবং {k} বছর আগে পিতার বয়স ছিল {f_ - k} বছর। তাদের বর্তমান বয়স কত?", ok, W(ok, [f"{f_ + k} বছর ও {s - k} বছর" if s > k else f"{f_ + 1} বছর ও {s - 1} বছর", f"{f_ - k} বছর ও {s + k} বছর", f"{s} বছর ও {f_} বছর"]), "", lv)
def f62_price(b, lv):
    p, q = R.randint(5, 60), R.randint(5, 60); a1, b1, a2, b2 = R.randint(1, 6), R.randint(1, 6), R.randint(1, 6), R.randint(1, 6)
    if a1 * b2 == a2 * b1: return
    it = R.choice([('কলম', 'খাতা'), ('আম', 'কলা'), ('চেয়ার', 'টেবিল'), ('বই', 'পেন্সিল')])
    ok = f"{p} টাকা ও {q} টাকা"
    b.add(f"{a1}টি {it[0]} ও {b1}টি {it[1]}-এর দাম {a1 * p + b1 * q} টাকা এবং {a2}টি {it[0]} ও {b2}টি {it[1]}-এর দাম {a2 * p + b2 * q} টাকা। প্রতিটি {it[0]} ও {it[1]}-এর দাম কত?", ok, W(ok, [f"{q} টাকা ও {p} টাকা", f"{p + 1} টাকা ও {q - 1} টাকা", f"{p} টাকা ও {q + 2} টাকা"]), "সহসমীকরণ গঠন করে।", lv)
def f62_frac(b, lv):
    n, d = R.randint(1, 20), R.randint(2, 25)
    if n >= d or math.gcd(n, d) != 1: return
    k = R.randint(1, 5)
    v1 = F(n + k, d + k)
    ok = f"{n}/{d}"
    b.add(f"একটি ভগ্নাংশের লব ও হরের যোগফল {n + d}। লব ও হর উভয়ের সাথে {k} যোগ করলে ভগ্নাংশটি {fr(v1)} হয়। ভগ্নাংশটি কত?", ok, W(ok, [f"{d}/{n}", f"{n + 1}/{d - 1}", f"{n + k}/{d + k}" if F(n + k, d + k) != F(n, d) else f"{n}/{d + 1}"]), "", lv)
def f62_digit(b, lv):
    t, u = R.randint(1, 9), R.randint(0, 9)
    if t == u or u == 0: return
    n = 10 * t + u; rv = 10 * u + t
    b.add(f"দুই অঙ্কবিশিষ্ট একটি সংখ্যার অঙ্কদ্বয়ের যোগফল {t + u}। অঙ্ক দুটি স্থান বিনিময় করলে সংখ্যাটি {abs(rv - n)} {'বৃদ্ধি' if rv > n else 'হ্রাস'} পায়। সংখ্যাটি কত?", n, W(n, [rv, n + 9, n - 9, 10 * (t + 1) + u - 1]), "10x + y।", lv)
K62 = part('6.2', 250, [], [f62_num, f62_price], [f62_price, f62_frac, f62_age, f62_num, f62_digit], [f62_digit, f62_frac, f62_age])
save('k6', K61 + K62)

# ===================================================== অধ্যায় 7: সেট
fx7 = [("যে সেটের কোনো উপাদান নেই তাকে কী বলে?", "ফাঁকা সেট", ["সার্বিক সেট", "উপসেট", "শক্তি সেট"], "", E), ("ফাঁকা সেটের প্রতীক কোনটি?", "∅", ["{0}", "0", "U"], "", E),
       ("A ⊆ B হলে A ∪ B = কত?", "B", ["A", "∅", "A ∩ B"], "", M), ("A ⊆ B হলে A ∩ B = কত?", "A", ["B", "∅", "A ∪ B"], "", M), ("A − A = কত?", "∅", ["A", "U", "{0}"], "", E)]
def S(xs): xs = sorted(set(xs)); return '∅' if not xs else '{' + ', '.join(str(x) for x in xs) + '}'
def s7_n(b, lv):
    n = R.randint(0, 9); t = R.choice(['উপসেট', 'প্রকৃত উপসেট'])
    v = 2 ** n if t == 'উপসেট' else 2 ** n - 1
    xs = R.sample(range(1, 30), n)
    b.add(f"A = {S(xs)} হলে A-এর {t}ের সংখ্যা কত?", v, W(v, [2 ** n - 1 if t == 'উপসেট' else 2 ** n, 2 * n, n, 2 ** (n + 1)]), "2ⁿ ও 2ⁿ − 1।", lv)
def s7_op(b, lv):
    A, B = set(R.sample(range(1, 16), R.randint(3, 6))), set(R.sample(range(1, 16), R.randint(3, 6)))
    op = R.choice(['∪', '∩', '−'])
    v = {'∪': A | B, '∩': A & B, '−': A - B}[op]
    alt = [A | B, A & B, A - B, B - A, A ^ B]
    b.add(f"A = {S(A)} ও B = {S(B)} হলে A {op} B = কত?", S(v), W(S(v), [S(x) for x in alt]), "", lv)
def s7_card(b, lv):
    a, c = R.randint(5, 60), R.randint(5, 60); i = R.randint(0, min(a, c))
    v = a + c - i
    b.add(f"n(A) = {a}, n(B) = {c} এবং n(A ∩ B) = {i} হলে n(A ∪ B) = কত?", v, W(v, [a + c, a + c - 2 * i, v + 1, abs(a - c)]), "n(A) + n(B) − n(A ∩ B)।", lv)
def s7_build(b, lv):
    k = R.randint(2, 9); lo, hi = R.randint(1, 10), R.randint(20, 60)
    xs = [x for x in range(lo, hi + 1) if x % k == 0]
    if len(xs) > 8 or len(xs) < 2: return
    b.add(f"{{x : x ∈ N, {lo} ≤ x ≤ {hi} এবং x, {k}-এর গুণিতক}}-কে তালিকা পদ্ধতিতে লিখলে কোনটি?", S(xs), W(S(xs), [S(xs[:-1]), S(xs + [xs[-1] + k]), S([x + 1 for x in xs]), S([x for x in range(lo, hi + 1) if x % (k + 1) == 0][:len(xs)])]), "", lv)
def s7_div(b, lv):
    n = R.randint(6, 60)
    xs = [d for d in range(1, n + 1) if n % d == 0]
    if len(xs) > 10: return
    b.add(f"{n}-এর গুণনীয়কগুলোর সেট কোনটি?", S(xs), W(S(xs), [S(xs[1:]), S(xs[:-1]), S([d for d in range(1, n + 1) if n % d == 0 and d % 2 == 0]) if len([d for d in xs if d % 2 == 0]) else S([n]), S(xs + [n * 2])]), "", lv)
def s7_word(b, lv):
    T = R.randint(30, 200); a = R.randint(10, T - 5); c = R.randint(10, T - 5); i = a + c - T + R.randint(0, 20)
    if i < 0 or i > min(a, c): return
    nn = T - (a + c - i)
    b.add(f"একটি ক্লাসের {T} জন শিক্ষার্থীর মধ্যে {a} জন ফুটবল ও {c} জন ক্রিকেট খেলে, {i} জন উভয়ই খেলে। কতজন কোনোটিই খেলে না?", nn, W(nn, [nn + i, T - a - c if T - a - c > 0 else nn + 2, nn + 1, i]), "T − n(A ∪ B)।", lv)
def s7_power(b, lv):
    xs = R.sample(['a', 'b', 'c', 'p', 'q', 'x', 'y', '1', '2', '3'], R.randint(1, 4))
    n = len(xs)
    b.add(f"A = {{{', '.join(xs)}}} হলে P(A)-এর উপাদান সংখ্যা কত?", 2 ** n, W(2 ** n, [n, 2 * n, 2 ** n - 1, n * n + 1]), "2ⁿ।", lv)
K7 = part(None, 300, fx7, [s7_n, s7_op, s7_card, s7_power, s7_div], [s7_op, s7_card, s7_build, s7_div, s7_n], [s7_word, s7_build])
save('k7', K7)

# ===================================================== অধ্যায় 8: চতুর্ভুজ
fx81 = [("চতুর্ভুজের চার কোণের সমষ্টি কত?", "360°", ["180°", "270°", "540°"], "", E), ("সামান্তরিকের বিপরীত কোণগুলো কেমন?", "সমান", ["সম্পূরক", "পূরক", "অসমান"], "", E),
        ("রম্বসের কর্ণদ্বয় পরস্পরকে কীভাবে ছেদ করে?", "সমকোণে সমদ্বিখণ্ডিত করে", ["সমান্তরালভাবে", "45° কোণে", "ছেদ করে না"], "", E),
        ("আয়তের কর্ণদ্বয় কেমন?", "সমান", ["অসমান", "লম্ব", "সমান্তরাল"], "", E), ("কোন চতুর্ভুজের এক জোড়া বিপরীত বাহু সমান্তরাল?", "ট্রাপিজিয়াম", ["রম্বস", "বর্গ", "ঘুড়ি"], "", E),
        ("বর্গের প্রতিটি কোণ কত?", "90°", ["60°", "120°", "45°"], "", E)]
def q81_missing(b, lv):
    a, c, d = R.randint(40, 140), R.randint(40, 140), R.randint(40, 140)
    v = 360 - a - c - d
    if v <= 10 or v >= 180: return
    b.add(f"একটি চতুর্ভুজের তিনটি কোণ {a}°, {c}° ও {d}° হলে চতুর্থ কোণ কত?", f"{v}°", W(f"{v}°", [f"{180 - (a + c + d) % 180}°", f"{v + 10}°", f"{v - 10}°", f"{360 - a - c}°"]), "360° − তিন কোণের সমষ্টি।", lv)
def q81_para(b, lv):
    a = R.randint(20, 160)
    if a == 90: return
    t = R.choice(['adj', 'opp'])
    v = 180 - a if t == 'adj' else a
    b.add(f"একটি সামান্তরিকের একটি কোণ {a}° হলে এর {'সন্নিহিত' if t == 'adj' else 'বিপরীত'} কোণ কত?", f"{v}°", W(f"{v}°", [f"{a if t == 'adj' else 180 - a}°", f"{360 - a}°", f"{90 - a % 90}°", f"{v + 5}°"]), "", lv)
def q81_ratio(b, lv):
    r = R.sample(range(1, 10), 4)
    s = sum(r)
    if 360 % s: return
    k = 360 // s; t = R.choice(['বৃহত্তম', 'ক্ষুদ্রতম'])
    v = max(r) * k if t == 'বৃহত্তম' else min(r) * k
    b.add(f"একটি চতুর্ভুজের কোণগুলোর অনুপাত {' : '.join(map(str, r))} হলে {t} কোণটি কত?", f"{v}°", W(f"{v}°", [f"{min(r) * k if t == 'বৃহত্তম' else max(r) * k}°", f"{v + k}°", f"{v * 2 if v * 2 < 360 else v - k}°", f"{k}°"]), "", lv)
def q81_rhombus(b, lv):
    p, q, r = R.choice([(3, 4, 5), (6, 8, 10), (5, 12, 13), (8, 15, 17), (9, 12, 15), (12, 16, 20), (7, 24, 25), (20, 21, 29), (15, 20, 25)])
    k = R.randint(1, 4)
    b.add(f"একটি রম্বসের কর্ণদ্বয় {2 * p * k} সেমি ও {2 * q * k} সেমি হলে এর প্রতিটি বাহুর দৈর্ঘ্য কত?", f"{r * k} সেমি", W(f"{r * k} সেমি", [f"{(p + q) * k} সেমি", f"{2 * r * k} সেমি", f"{(r + 1) * k} সেমি"]), "কর্ণদ্বয় পরস্পরকে লম্বভাবে সমদ্বিখণ্ডিত করে।", lv)
def q81_trap(b, lv):
    a = R.randint(30, 150)
    if a == 90: return
    b.add(f"ট্রাপিজিয়াম ABCD-তে AB ∥ DC এবং ∠A = {a}° হলে ∠D = কত?", f"{180 - a}°", W(f"{180 - a}°", [f"{a}°", f"{360 - a}°", f"{90 + a % 90}°"]), "সমান্তরাল রেখার একই পাশের অন্তঃকোণ সম্পূরক।", lv)
def q81_x(b, lv):
    k = R.randint(1, 5); c1, c2, c3, c4 = [R.randint(1, 4) for _ in range(4)]; d = R.randint(0, 30)
    s = c1 + c2 + c3 + c4
    x = F(360 - 4 * d, s)
    if x.denominator != 1 or x <= 0: return
    b.add(f"একটি চতুর্ভুজের কোণগুলো ({c1}x + {d})°, ({c2}x + {d})°, ({c3}x + {d})° ও ({c4}x + {d})° হলে x = কত?".replace('(1x', '(x').replace(' + 0)', ')'), num(x), W(num(x), [num(x + 1), num(F(360, s)), num(x - 2), num(x * 2)]), "কোণের সমষ্টি 360°।", lv)
K81 = part('8.1', 250, fx81, [q81_missing, q81_para, q81_trap], [q81_missing, q81_ratio, q81_rhombus, q81_para, q81_x], [q81_x, q81_ratio, q81_rhombus])
def q82(b, lv):
    t = R.choice(['para', 'trap', 'rhom', 'rect', 'sq'])
    if t == 'para':
        bs, h = R.randint(3, 60), R.randint(2, 40); v = bs * h; q = f"একটি সামান্তরিকের ভূমি {bs} সেমি ও উচ্চতা {h} সেমি হলে ক্ষেত্রফল কত?"; ws = [F(v, 2), 2 * (bs + h), v + bs]
    elif t == 'trap':
        a, c, h = R.randint(3, 40), R.randint(3, 40), R.randint(2, 30); v = F((a + c) * h, 2); q = f"একটি ট্রাপিজিয়ামের সমান্তরাল বাহুদ্বয় {a} সেমি ও {c} সেমি এবং এদের দূরত্ব {h} সেমি হলে ক্ষেত্রফল কত?"; ws = [(a + c) * h, a * c * h // 2 if a * c * h % 2 == 0 else a * c, v + h]
    elif t == 'rhom':
        d1, d2 = R.randint(2, 40), R.randint(2, 40); v = F(d1 * d2, 2); q = f"একটি রম্বসের কর্ণদ্বয় {d1} সেমি ও {d2} সেমি হলে ক্ষেত্রফল কত?"; ws = [d1 * d2, d1 + d2, v + 1]
    elif t == 'rect':
        l, w = R.randint(2, 50), R.randint(2, 40); v = l * w; q = f"একটি আয়তক্ষেত্রের দৈর্ঘ্য {l} সেমি ও প্রস্থ {w} সেমি হলে ক্ষেত্রফল কত?"; ws = [2 * (l + w), v + w, F(v, 2)]
    else:
        d = R.randint(2, 50); v = F(d * d, 2); q = f"একটি বর্গের কর্ণের দৈর্ঘ্য {d} সেমি হলে এর ক্ষেত্রফল কত?"; ws = [d * d, 4 * d, v + d]
    ok = f"{num(v)} বর্গসেমি"
    b.add(q, ok, W(ok, [f"{num(x)} বর্গসেমি" for x in ws]), "", lv)
def q82_find(b, lv):
    t = R.choice(['h', 'd2', 'trh'])
    if t == 'h':
        bs, h = R.randint(3, 50), R.randint(2, 40); q = f"একটি সামান্তরিকের ক্ষেত্রফল {bs * h} বর্গসেমি ও ভূমি {bs} সেমি হলে উচ্চতা কত?"; v = h; ws = [h * 2, bs, h + 1]
    elif t == 'd2':
        d1, d2 = R.randint(2, 40), R.randint(2, 40); q = f"একটি রম্বসের ক্ষেত্রফল {num(F(d1 * d2, 2))} বর্গসেমি ও একটি কর্ণ {d1} সেমি হলে অপর কর্ণ কত?"; v = d2; ws = [F(d2, 2), d2 * 2, d2 + 1]
    else:
        a, c, h = R.randint(3, 40), R.randint(3, 40), R.randint(2, 30); q = f"একটি ট্রাপিজিয়ামের ক্ষেত্রফল {num(F((a + c) * h, 2))} বর্গসেমি এবং সমান্তরাল বাহুদ্বয় {a} সেমি ও {c} সেমি হলে এদের মধ্যবর্তী দূরত্ব কত?"; v = h; ws = [h * 2, F(h, 2), h + 1]
    ok = f"{num(v)} সেমি"
    b.add(q, ok, W(ok, [f"{num(x)} সেমি" for x in ws]), "", lv)
def q82_ratio(b, lv):
    p, q = R.randint(1, 9), R.randint(1, 9); P = R.randint(2, 20) * 2
    s = P // 2
    if s % (p + q): return
    k = s // (p + q); v = p * k * q * k
    b.add(f"একটি আয়তক্ষেত্রের দৈর্ঘ্য ও প্রস্থের অনুপাত {p} : {q} এবং পরিসীমা {P} মিটার হলে ক্ষেত্রফল কত?", f"{v} বর্গমিটার", W(f"{v} বর্গমিটার", [f"{v * 2} বর্গমিটার", f"{p * q} বর্গমিটার", f"{v + k} বর্গমিটার"]), "", lv)
K82 = part('8.2', 250, [], [q82, q82_find], [q82, q82_find, q82_ratio], [q82_ratio, q82_find])
save('k8', K81 + K82)

# ===================================================== অধ্যায় 9: পিথাগোরাসের উপপাদ্য
fx9 = [("সমকোণী ত্রিভুজে অতিভুজের উপর অঙ্কিত বর্গক্ষেত্রের ক্ষেত্রফল অপর দুই বাহুর উপর অঙ্কিত বর্গক্ষেত্রের ক্ষেত্রফলের কী?", "সমষ্টির সমান", ["অন্তরের সমান", "গুণফলের সমান", "অর্ধেক"], "", E),
       ("সমকোণী ত্রিভুজের বৃহত্তম বাহুকে কী বলে?", "অতিভুজ", ["ভূমি", "লম্ব", "মধ্যমা"], "", E)]
TR = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29), (9, 40, 41), (12, 35, 37), (11, 60, 61), (28, 45, 53), (33, 56, 65), (16, 63, 65), (13, 84, 85)]
def t9_hyp(b, lv):
    p, q, r = R.choice(TR); k = R.randint(1, 6)
    b.add(f"একটি সমকোণী ত্রিভুজের সমকোণ সংলগ্ন বাহুদ্বয় {p * k} সেমি ও {q * k} সেমি হলে অতিভুজ কত?", f"{r * k} সেমি", W(f"{r * k} সেমি", [f"{(p + q) * k} সেমি", f"{(r + 1) * k} সেমি", f"{(q - p) * k} সেমি", f"{(r - 1) * k} সেমি"]), "c² = a² + b²।", lv)
def t9_side(b, lv):
    p, q, r = R.choice(TR); k = R.randint(1, 6)
    if R.random() < .5: p, q = q, p
    b.add(f"একটি সমকোণী ত্রিভুজের অতিভুজ {r * k} সেমি ও একটি বাহু {p * k} সেমি হলে অপর বাহু কত?", f"{q * k} সেমি", W(f"{q * k} সেমি", [f"{(r - p) * k} সেমি", f"{(r + p) * k} সেমি", f"{(q + 1) * k} সেমি", f"{(q - 1) * k} সেমি"]), "", lv)
def t9_check(b, lv):
    p, q, r = R.choice(TR); k = R.randint(1, 5)
    ok = f"{p * k}, {q * k}, {r * k}"
    b.add("নিচের কোন বাহুত্রয় দ্বারা সমকোণী ত্রিভুজ গঠিত হয়?", ok, W(ok, [f"{p * k}, {q * k}, {(r + 1) * k}", f"{p * k + 1}, {q * k}, {r * k}", f"{p * k}, {q * k + 1}, {r * k}", f"{p * k}, {p * k}, {r * k}"]), "a² + b² = c² যাচাই।", lv)
def t9_surd(b, lv):
    a, c = R.randint(1, 20), R.randint(1, 20)
    v = a * a + c * c
    ok = sq(v) + ' সেমি'
    b.add(f"একটি সমকোণী ত্রিভুজের সমকোণ সংলগ্ন বাহুদ্বয় {a} সেমি ও {c} সেমি হলে অতিভুজ কত?", ok, W(ok, [f"{a + c} সেমি", sq(abs(a * a - c * c)) + ' সেমি' if a != c else f"{2 * a} সেমি", sq(v + 1) + ' সেমি']), "", lv)
def t9_rect(b, lv):
    p, q, r = R.choice(TR); k = R.randint(1, 5)
    b.add(f"একটি আয়তক্ষেত্রের দৈর্ঘ্য {q * k} মিটার ও প্রস্থ {p * k} মিটার হলে এর কর্ণের দৈর্ঘ্য কত?", f"{r * k} মিটার", W(f"{r * k} মিটার", [f"{(p + q) * k} মিটার", f"{(r + 2) * k} মিটার", f"{2 * r * k} মিটার"]), "", lv)
def t9_ladder(b, lv):
    p, q, r = R.choice(TR); k = R.randint(1, 3)
    b.add(f"{r * k} মিটার লম্বা একটি মই দেয়ালে হেলান দিয়ে রাখা আছে। মইয়ের পাদদেশ দেয়াল থেকে {p * k} মিটার দূরে হলে মইটি দেয়ালের কত উচ্চতায় পৌঁছায়?", f"{q * k} মিটার", W(f"{q * k} মিটার", [f"{(r - p) * k} মিটার", f"{(r + p) * k} মিটার", f"{(q + 1) * k} মিটার"]), "", lv)
def t9_iso(b, lv):
    a = R.randint(1, 30)
    b.add(f"একটি সমদ্বিবাহু সমকোণী ত্রিভুজের সমান বাহুদ্বয়ের প্রতিটি {a} সেমি হলে অতিভুজ কত?", f"{a}√2 সেমি", W(f"{a}√2 সেমি", [f"{2 * a} সেমি", f"{a}√3 সেমি", f"{a * a} সেমি"]), "", lv)
def t9_eq(b, lv):
    a = R.randint(1, 30) * 2
    b.add(f"{a} সেমি বাহুবিশিষ্ট সমবাহু ত্রিভুজের উচ্চতা কত?", f"{a // 2}√3 সেমি", W(f"{a // 2}√3 সেমি", [f"{a}√3 সেমি", f"{a // 2} সেমি", f"{a // 2}√2 সেমি"]), "h = (√3/2)a।", lv)
K9 = part(None, 300, fx9, [t9_hyp, t9_side, t9_check, t9_rect], [t9_side, t9_surd, t9_ladder, t9_iso, t9_rect, t9_hyp], [t9_eq, t9_surd, t9_ladder])
save('k9', K9)

# ===================================================== অধ্যায় 10: বৃত্ত
fx101 = [("বৃত্তের বৃহত্তম জ্যা কোনটি?", "ব্যাস", ["ব্যাসার্ধ", "চাপ", "স্পর্শক"], "", E), ("অর্ধবৃত্তস্থ কোণ কত?", "90°", ["180°", "60°", "45°"], "", E),
         ("বৃত্তের কেন্দ্র থেকে জ্যা-এর উপর অঙ্কিত লম্ব জ্যাকে কী করে?", "সমদ্বিখণ্ডিত করে", ["সমত্রিখণ্ডিত করে", "দ্বিগুণ করে", "স্পর্শ করে"], "", E),
         ("একই চাপের উপর দণ্ডায়মান কেন্দ্রস্থ কোণ বৃত্তস্থ কোণের কত গুণ?", "দ্বিগুণ", ["সমান", "অর্ধেক", "তিনগুণ"], "", E), ("বৃত্তস্থ চতুর্ভুজের বিপরীত কোণদ্বয়ের সমষ্টি কত?", "180°", ["90°", "360°", "270°"], "", E)]
def c101_dia(b, lv):
    r = R.randint(1, 90); t = R.choice(['d', 'r'])
    if t == 'd': b.add(f"একটি বৃত্তের ব্যাসার্ধ {r} সেমি হলে ব্যাস কত?", f"{2 * r} সেমি", W(f"{2 * r} সেমি", [f"{r} সেমি", f"{r * r} সেমি", f"{3 * r} সেমি"]), "", lv)
    else: b.add(f"একটি বৃত্তের ব্যাস {2 * r} সেমি হলে ব্যাসার্ধ কত?", f"{r} সেমি", W(f"{r} সেমি", [f"{2 * r} সেমি", f"{4 * r} সেমি", f"{r + 1} সেমি"]), "", lv)
def c101_angle(b, lv):
    a = R.randint(10, 85); t = R.choice(['c2i', 'i2c'])
    if t == 'c2i': b.add(f"একই চাপের উপর দণ্ডায়মান কেন্দ্রস্থ কোণ {2 * a}° হলে বৃত্তস্থ কোণ কত?", f"{a}°", W(f"{a}°", [f"{2 * a}°", f"{4 * a}°", f"{180 - 2 * a}°"]), "", lv)
    else: b.add(f"একই চাপের উপর দণ্ডায়মান বৃত্তস্থ কোণ {a}° হলে কেন্দ্রস্থ কোণ কত?", f"{2 * a}°", W(f"{2 * a}°", [f"{a}°", f"{num(F(a, 2))}°", f"{180 - a}°"]), "", lv)
def c101_cyc(b, lv):
    a = R.randint(30, 150)
    b.add(f"বৃত্তস্থ চতুর্ভুজ ABCD-এর ∠A = {a}° হলে ∠C = কত?", f"{180 - a}°", W(f"{180 - a}°", [f"{a}°", f"{360 - a}°", f"{90 - a % 90 if a != 90 else 45}°"]), "বিপরীত কোণ সম্পূরক।", lv)
def c101_chord(b, lv):
    p, q, r = R.choice(TR); k = R.randint(1, 4)
    t = R.choice(['len', 'dist'])
    if t == 'len': b.add(f"{r * k} সেমি ব্যাসার্ধের বৃত্তের কেন্দ্র থেকে {p * k} সেমি দূরের জ্যা-এর দৈর্ঘ্য কত?", f"{2 * q * k} সেমি", W(f"{2 * q * k} সেমি", [f"{q * k} সেমি", f"{2 * p * k} সেমি", f"{2 * r * k} সেমি"]), "2√(r² − d²)।", lv)
    else: b.add(f"{r * k} সেমি ব্যাসার্ধের বৃত্তে {2 * q * k} সেমি দৈর্ঘ্যের জ্যা কেন্দ্র থেকে কত দূরে?", f"{p * k} সেমি", W(f"{p * k} সেমি", [f"{q * k} সেমি", f"{(r - q) * k} সেমি", f"{2 * p * k} সেমি"]), "", lv)
def c101_semi(b, lv):
    a = R.randint(10, 80)
    b.add(f"AB বৃত্তের ব্যাস এবং C বৃত্তের উপর একটি বিন্দু। ∠CAB = {a}° হলে ∠CBA = কত?", f"{90 - a}°", W(f"{90 - a}°", [f"{a}°", f"{180 - a}°", f"{90 + a}°"]), "∠ACB = 90°।", lv)
K101 = part('10.1', 250, fx101, [c101_dia, c101_angle, c101_cyc], [c101_chord, c101_semi, c101_angle, c101_cyc], [c101_chord, c101_semi])
def c102(b, lv):
    r = R.randint(1, 30) * 7; t = R.choice(['পরিধি', 'ক্ষেত্রফল'])
    v = 2 * 22 * r // 7 if t == 'পরিধি' else 22 * r * r // 7
    u = 'সেমি' if t == 'পরিধি' else 'বর্গসেমি'
    b.add(f"{r} সেমি ব্যাসার্ধের বৃত্তের {t} কত? (π = 22/7)", f"{v} {u}", W(f"{v} {u}", [f"{22 * r * r // 7 if t == 'পরিধি' else 2 * 22 * r // 7} {u}", f"{v // 2} {u}", f"{v * 2} {u}"]), "2πr ও πr²।", lv)
def c102_pi(b, lv):
    r = R.randint(1, 60); t = R.choice(['পরিধি', 'ক্ষেত্রফল'])
    ok = f"{2 * r}π সেমি" if t == 'পরিধি' else f"{r * r}π বর্গসেমি"
    b.add(f"{r} সেমি ব্যাসার্ধের বৃত্তের {t} কত (π-এর মাধ্যমে)?", ok, W(ok, [f"{r * r}π সেমি" if t == 'পরিধি' else f"{2 * r}π বর্গসেমি", f"{r}π {'সেমি' if t == 'পরিধি' else 'বর্গসেমি'}", f"{4 * r * r}π {'সেমি' if t == 'পরিধি' else 'বর্গসেমি'}"]), "", lv)
def c102_back(b, lv):
    r = R.randint(1, 20) * 7; t = R.choice(['c', 'a'])
    if t == 'c': q = f"একটি বৃত্তের পরিধি {2 * 22 * r // 7} সেমি হলে ব্যাসার্ধ কত? (π = 22/7)"
    else: q = f"একটি বৃত্তের ক্ষেত্রফল {22 * r * r // 7} বর্গসেমি হলে ব্যাসার্ধ কত? (π = 22/7)"
    b.add(q, f"{r} সেমি", W(f"{r} সেমি", [f"{2 * r} সেমি", f"{r // 7} সেমি", f"{r + 7} সেমি"]), "", lv)
def c102_semi(b, lv):
    r = R.randint(1, 20) * 7
    v = 22 * r // 7 + 2 * r
    b.add(f"{r} সেমি ব্যাসার্ধের অর্ধবৃত্তের পরিসীমা কত? (π = 22/7)", f"{v} সেমি", W(f"{v} সেমি", [f"{22 * r // 7} সেমি", f"{2 * 22 * r // 7} সেমি", f"{v + r} সেমি"]), "πr + 2r।", lv)
def c102_wheel(b, lv):
    r = R.randint(1, 10) * 7; n = R.randint(10, 500)
    v = 2 * 22 * r // 7 * n
    b.add(f"{r} সেমি ব্যাসার্ধের একটি চাকা {n} বার ঘুরলে কত দূরত্ব অতিক্রম করবে? (π = 22/7)", f"{v:,} সেমি", W(f"{v:,} সেমি", [f"{v // 2:,} সেমি", f"{22 * r * r // 7 * n:,} সেমি", f"{v + n:,} সেমি"]), "পরিধি × ঘূর্ণন সংখ্যা।", lv)
def c102_ring(b, lv):
    r1, r2 = sorted(R.sample(range(1, 30), 2))
    ok = f"{r2 * r2 - r1 * r1}π বর্গসেমি"
    b.add(f"একই কেন্দ্রবিশিষ্ট দুটি বৃত্তের ব্যাসার্ধ {r2} সেমি ও {r1} সেমি হলে বৃত্তদ্বয়ের মধ্যবর্তী অংশের ক্ষেত্রফল কত?", ok, W(ok, [f"{(r2 - r1) ** 2}π বর্গসেমি", f"{r2 * r2 + r1 * r1}π বর্গসেমি", f"{2 * (r2 - r1)}π বর্গসেমি"]), "π(R² − r²)।", lv)
K102 = part('10.2', 250, [], [c102, c102_pi, c102_back], [c102, c102_back, c102_semi, c102_wheel, c102_pi], [c102_ring, c102_wheel])
save('k10', K101 + K102)

# ===================================================== অধ্যায় 11: তথ্য ও উপাত্ত
fx11 = [("উপাত্তের মধ্যে যে মান সবচেয়ে বেশিবার আসে তাকে কী বলে?", "প্রচুরক", ["গড়", "মধ্যক", "পরিসর"], "", E), ("মানের ক্রমানুসারে সাজানো উপাত্তের মাঝের মানকে কী বলে?", "মধ্যক", ["প্রচুরক", "গড়", "পরিসর"], "", E),
        ("পরিসর = কত?", "বৃহত্তম মান − ক্ষুদ্রতম মান + 1", ["বৃহত্তম মান + ক্ষুদ্রতম মান", "গড় − মধ্যক", "বৃহত্তম মান × ক্ষুদ্রতম মান"], "শ্রেণিবিন্যাসের পাঠ্যবইয়ের সংজ্ঞা।", E)]
def d11_mean(b, lv):
    n = R.randint(4, 9)
    while True:
        xs = [R.randint(1, 99) for _ in range(n)]
        if sum(xs) % n == 0: break
    m = sum(xs) // n
    b.add(f"{', '.join(map(str, xs))} সংখ্যাগুলোর গাণিতিক গড় কত?", m, W(m, [m + 1, m - 1, sorted(xs)[n // 2] if sorted(xs)[n // 2] != m else m + 2, sum(xs)]), "সমষ্টি ÷ সংখ্যা।", lv)
def d11_median(b, lv):
    n = R.choice([5, 7, 9, 6, 8])
    xs = R.sample(range(1, 100), n); s = sorted(xs)
    med = F(s[n // 2]) if n % 2 else F(s[n // 2 - 1] + s[n // 2], 2)
    D = lambda v: (f"{float(v):.2f}".rstrip('0').rstrip('.'))
    b.add(f"{', '.join(map(str, xs))} উপাত্তের মধ্যক কত?", D(med), W(D(med), [D(F(xs[n // 2])) if F(xs[n // 2]) != med else D(med + 1), D(F(sum(xs), n)), D(med + 1), D(F(s[0] + s[-1], 2))]), "মানের ক্রমে সাজিয়ে মাঝের মান।", lv)
def d11_mode(b, lv):
    base = R.sample(range(1, 60), 5); m = R.choice(base)
    xs = base + [m, m]; R.shuffle(xs)
    others = [x for x in base if x != m]
    b.add(f"{', '.join(map(str, xs))} উপাত্তের প্রচুরক কত?", m, W(m, others + [max(xs)]), "সবচেয়ে বেশিবার আসা মান।", lv)
def d11_range(b, lv):
    xs = R.sample(range(1, 200), R.randint(5, 9))
    v = max(xs) - min(xs) + 1
    b.add(f"{', '.join(map(str, xs))} উপাত্তের পরিসর কত?", v, W(v, [v - 1, max(xs) + min(xs), v + 1, max(xs)]), "বৃহত্তম − ক্ষুদ্রতম + 1।", lv)
def d11_class(b, lv):
    lo, hi, h = R.randint(1, 50), R.randint(80, 200), R.choice([5, 10, 15, 20])
    rng = hi - lo + 1; n = math.ceil(rng / h)
    b.add(f"কোনো উপাত্তের ক্ষুদ্রতম মান {lo} ও বৃহত্তম মান {hi}। শ্রেণিব্যাপ্তি {h} হলে শ্রেণিসংখ্যা কত?", n, W(n, [n + 1, n - 1, rng // h if rng // h != n else n + 2, h]), "পরিসর ÷ শ্রেণিব্যাপ্তি (পূর্ণসংখ্যায় উন্নীত)।", lv)
def d11_mid(b, lv):
    lo = R.randint(0, 90); h = R.choice([5, 10, 4, 6, 8, 20])
    hi = lo + h - 1
    v = F(lo + hi, 2)
    b.add(f"{lo} – {hi} শ্রেণির মধ্যমান কত?", num(v), W(num(v), [num(F(lo + hi + 1, 2)), str(h), num(v + 1), str(hi)]), "(নিম্নসীমা + উচ্চসীমা)/2।", lv)
def d11_missing(b, lv):
    n = R.randint(4, 8); m = R.randint(10, 80)
    xs = [R.randint(1, 99) for _ in range(n - 1)]; last = m * n - sum(xs)
    if last <= 0 or last > 200: return
    b.add(f"{n}টি সংখ্যার গড় {m}। এর {n - 1}টি সংখ্যা {', '.join(map(str, xs))} হলে অপর সংখ্যাটি কত?", last, W(last, [last + 1, m, last - n, m * n]), "মোট = গড় × সংখ্যা।", lv)
def d11_combined(b, lv):
    n1, n2 = R.randint(5, 40), R.randint(5, 40); m1, m2 = R.randint(20, 90), R.randint(20, 90)
    v = F(n1 * m1 + n2 * m2, n1 + n2)
    if v.denominator not in (1, 2, 4, 5, 10, 20, 25, 50): return
    D = lambda x: (f"{float(x):.2f}".rstrip('0').rstrip('.'))
    b.add(f"{n1} জন শিক্ষার্থীর গড় নম্বর {m1} এবং {n2} জনের গড় নম্বর {m2} হলে সকলের গড় নম্বর কত?", D(v), W(D(v), [D(F(m1 + m2, 2)), D(v + 1), D(F(n1 * m2 + n2 * m1, n1 + n2)) if m1 != m2 and n1 != n2 else D(v + 2), D(v - 1)]), "মোট নম্বর ÷ মোট শিক্ষার্থী।", lv)
K11 = part(None, 300, fx11, [d11_mean, d11_median, d11_mode, d11_range, d11_mid], [d11_mean, d11_median, d11_class, d11_missing, d11_mid, d11_mode], [d11_missing, d11_combined, d11_class])
save('k11', K11)
