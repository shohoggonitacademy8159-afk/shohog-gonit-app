#!/usr/bin/env python3
"""অধ্যায় 11 বীজগাণিতিক অনুপাত ও সমানুপাত: 11.1 অনুপাত ও সমানুপাত · 11.2 ক্রমিক অনুপাত, যোজন-বিয়োজন ও সমানুপাতিক ভাগ"""
import random, pathlib, sys, math
from fractions import Fraction as F
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from mcqlib import run, save, E, M, H, fr, near, num

R = random.Random(2026103111)
def rt(a, b):
    g = math.gcd(a, b); return f"{a // g} : {b // g}"
fx111 = [
 ("a : b = c : d হলে নিচের কোনটি সত্য?", "ad = bc", ["ab = cd", "ac = bd", "a + d = b + c"], "প্রান্তীয় পদের গুণফল = মধ্যপদের গুণফল।", E),
 ("a : b অনুপাতে a-কে কী বলে?", "পূর্বপদ", ["উত্তরপদ", "মধ্যপদ", "প্রান্তপদ"], "প্রথম রাশি পূর্বপদ।", E),
 ("a : b অনুপাতের ব্যস্ত অনুপাত কোনটি?", "b : a", ["a : b", "a² : b²", "1 : ab"], "পদ উল্টে দিলে।", E),
 ("অনুপাতের দুই পদকে একই অশূন্য সংখ্যা দিয়ে গুণ করলে অনুপাতের কী হয়?", "অপরিবর্তিত থাকে", ["দ্বিগুণ হয়", "উল্টে যায়", "শূন্য হয়"], "অনুপাতের মৌলিক ধর্ম।", E),
 ("অনুপাতের একক সম্পর্কে কোনটি সত্য?", "অনুপাতের কোনো একক নেই", ["একক মিটার", "একক টাকা", "একক পূর্বপদের একক"], "একই জাতীয় রাশির তুলনা।", E),
 ("a : b = c : d হলে a : c = b : d — এটি কোন রূপান্তর?", "একান্তরকরণ", ["ব্যস্তকরণ", "যোজন", "বিয়োজন"], "মধ্যপদ স্থান বিনিময়।", M),
 ("a : b = c : d হলে (a + b) : b = (c + d) : d — এটি কোন রূপান্তর?", "যোজন", ["বিয়োজন", "ব্যস্তকরণ", "একান্তরকরণ"], "উভয় পক্ষে 1 যোগ।", M),
 ("a : b = c : d হলে (a − b) : b = (c − d) : d — এটি কোন রূপান্তর?", "বিয়োজন", ["যোজন", "একান্তরকরণ", "ব্যস্তকরণ"], "উভয় পক্ষ থেকে 1 বিয়োগ।", M),
 ("a/b = c/d হলে (a + b)/(a − b) = কত?", "(c + d)/(c − d)", ["(c − d)/(c + d)", "(a + c)/(b + d)", "cd/ab"], "যোজন-বিয়োজন।", H),
]
def e_simp(b):
    g = R.randint(2, 12); a_, b_ = R.sample(range(1, 15), 2)
    if math.gcd(a_, b_) != 1: return
    b.add(f"{a_ * g} : {b_ * g} অনুপাতের সরল রূপ কোনটি?", f"{a_} : {b_}", [f"{b_} : {a_}", f"{a_ + 1} : {b_}", f"{a_ * 2} : {b_}"], f"উভয় পদকে {g} দিয়ে ভাগ।", E)
def e_fourth(b):
    a_, b_, k = R.randint(2, 9), R.randint(2, 9), R.randint(2, 6)
    c_ = a_ * k; d_ = b_ * k
    b.add(f"{a_} : {b_} = {c_} : x হলে x = কত?", d_, near(d_) if d_ > 3 else [d_ + 1, d_ + 2, d_ + 3], f"x = {b_} × {c_} / {a_} = {d_}।", E)
def e_mean(b):
    a_, k = R.randint(1, 9), R.randint(2, 5)
    c_ = a_ * k * k; m = a_ * k
    b.add(f"{a_} ও {c_} এর মধ্যসমানুপাতী কত?", m, [F(a_ + c_, 2) if F(a_ + c_, 2) != m else m + 1, m + 1, a_ * c_], f"√({a_} × {c_}) = {m}।", E)
def e_third(b):
    a_, k = R.randint(1, 8), R.randint(2, 4)
    b_ = a_ * k; c_ = b_ * k
    b.add(f"{a_} ও {b_} এর তৃতীয় সমানুপাতী কত?", c_, [c_ + a_, b_ * 2 if b_ * 2 != c_ else c_ + 2, a_ * b_ if a_ * b_ != c_ else c_ - 1], f"{a_} : {b_} = {b_} : x ⇒ x = {b_}²/{a_} = {c_}।", E)
def m_div(b):
    a_, b_ = R.sample(range(1, 10), 2); k = R.randint(5, 50)
    tot = (a_ + b_) * k
    b.add(f"{tot} টাকা {a_} : {b_} অনুপাতে ভাগ করলে বড় অংশ কত টাকা?", max(a_, b_) * k, [min(a_, b_) * k, tot // 2 if tot % 2 == 0 and tot // 2 != max(a_, b_) * k else max(a_, b_) * k + k, max(a_, b_) * k + 10], f"প্রতি অংশ {k}; বড় অংশ {max(a_, b_) * k}।", M)
def m_xy(b):
    a_, b_ = R.sample(range(1, 10), 2)
    if math.gcd(a_, b_) != 1: return
    p, q = R.randint(1, 6), R.randint(1, 6)
    # (px + qy):(px − qy) form... simpler: x:y = a:b ⇒ (x + y):(x − y)
    if a_ <= b_: return
    s, d = a_ + b_, a_ - b_
    g = math.gcd(s, abs(d))
    b.add(f"x : y = {a_} : {b_} হলে (x + y) : (x − y) = কত?", f"{s // g} : {num(d // g)}", [f"{num(d // g)} : {s // g}", f"{a_} : {b_}", f"{s} : {a_ * b_}"], f"x = {a_}k, y = {b_}k বসিয়ে।", M)
def m_age(b):
    a_, b_ = R.sample(range(2, 9), 2); k = R.randint(2, 8)
    if math.gcd(a_, b_) != 1: return
    s = (a_ + b_) * k
    b.add(f"দুই ভাইয়ের বয়সের অনুপাত {a_} : {b_} এবং বয়সের সমষ্টি {s} বছর। ছোট ভাইয়ের বয়স কত বছর?", min(a_, b_) * k, [max(a_, b_) * k, min(a_, b_) * k + k, s // 2 if s // 2 not in (min(a_, b_) * k, max(a_, b_) * k) else s], f"প্রতি অংশ {k}।", M)
def m_change(b):
    a_, b_ = R.sample(range(2, 9), 2); k = R.randint(1, 5)
    if math.gcd(a_, b_) != 1: return
    # একটি অনুপাতের প্রতিটি পদে k যোগ করলে নতুন অনুপাত
    b.add(f"{a_} : {b_} অনুপাতের প্রতিটি পদের সাথে {k} যোগ করলে নতুন অনুপাত কত?", rt(a_ + k, b_ + k), [rt(a_, b_), rt(a_ * k, b_ * k) if rt(a_ * k, b_ * k) != rt(a_ + k, b_ + k) else rt(a_ + 2 * k, b_ + k), rt(b_ + k, a_ + k)], f"{a_ + k} : {b_ + k} = {rt(a_ + k, b_ + k)}।", M)
def m_sqrt(b):
    a_, b_ = R.sample(range(1, 8), 2)
    b.add(f"{a_ * a_} : {b_ * b_} অনুপাতের বর্গমূলীয় অনুপাত কোনটি?", rt(a_, b_), [rt(a_ * a_, b_ * b_), rt(b_, a_), rt(a_ * a_ * a_, b_ ** 3)], f"√{a_ * a_} : √{b_ * b_} = {rt(a_, b_)}।", M)
def m_pct(b):
    a_, p = R.choice([100, 200, 300, 400, 500, 800]), R.choice([10, 20, 25, 50])
    nb = a_ + a_ * p // 100
    b.add(f"কোনো রাশি {a_} থেকে {p}% বাড়লে পুরাতন ও নতুন রাশির অনুপাত কত?", rt(a_, nb), [rt(nb, a_), rt(100, p), rt(a_, a_ - a_ * p // 100)], f"নতুন রাশি {nb}; {rt(a_, nb)}।", M)
def h_comp(b):
    a_, b_, c_, d_ = [R.randint(1, 7) for _ in range(4)]
    n, d = a_ * c_, b_ * d_
    b.add(f"{a_} : {b_} এবং {c_} : {d_} অনুপাতের মিশ্র (যৌগিক) অনুপাত কত?", rt(n, d), [rt(a_ + c_, b_ + d_) if rt(a_ + c_, b_ + d_) != rt(n, d) else rt(n + 1, d), rt(d, n) if rt(d, n) != rt(n, d) else rt(n, d + 1), rt(a_ * d_, b_ * c_) if rt(a_ * d_, b_ * c_) != rt(n, d) else rt(n + 2, d)], f"পূর্বপদ গুণ ও উত্তরপদ গুণ: {n} : {d}।", H)
def h_eq(b):
    a_, b_ = R.sample(range(1, 9), 2); k = R.randint(1, 6)
    # (x + k) : (x − k) = a : b ⇒ b(x + k) = a(x − k) ⇒ x = k(a + b)/(a − b)
    if a_ <= b_: a_, b_ = b_, a_
    x = F(k * (a_ + b_), a_ - b_)
    if x.denominator != 1: return
    b.add(f"(x + {k}) : (x − {k}) = {a_} : {b_} হলে x = কত?", fr(x), [fr(x + 1), fr(x - 1), fr(-x)], f"যোজন-বিয়োজন: x/{k} = ({a_} + {b_})/({a_} − {b_}) ⇒ x = {fr(x)}।", H)
def h_ratio_eq(b):
    a_, b_ = R.sample(range(1, 9), 2); p, q = R.randint(1, 5), R.randint(1, 5)
    # (px + qy) : (px − qy) with x:y=a:b
    num_, den = p * a_ + q * b_, p * a_ - q * b_
    if den <= 0: return
    g = math.gcd(num_, abs(den)); n, d = num_ // g, den // g
    if d < 0: n, d = -n, -d
    b.add(f"x : y = {a_} : {b_} হলে ({p}x + {q}y) : ({p}x − {q}y) = কত?", f"{num(n)} : {d}", [f"{d} : {num(n)}", f"{a_} : {b_}", f"{num(n + 1)} : {d}"], f"x = {a_}k, y = {b_}k বসিয়ে {num_} : {den}।", H)
I111 = run('11.1', R, fx111, [e_simp, e_fourth, e_mean, e_third], [m_div, m_xy, m_age, m_change, m_sqrt, m_pct], [h_comp, h_eq, h_ratio_eq], caps=(8, 9, 8))

fx112 = [
 ("a : b = b : c হলে a, b, c কে কী বলে?", "ক্রমিক সমানুপাতী", ["ব্যস্ত সমানুপাতী", "সমান", "মিশ্র অনুপাত"], "সংজ্ঞা।", E),
 ("a, b, c ক্রমিক সমানুপাতী হলে নিচের কোনটি সত্য?", "b² = ac", ["a² = bc", "c² = ab", "b = a + c"], "a/b = b/c।", E),
 ("x/a = y/b = z/c হলে প্রতিটি অনুপাত কিসের সমান?", "(x + y + z)/(a + b + c)", ["xyz/abc", "x/(a + b + c)", "(x + y + z)/abc"], "সমানুপাতের ধর্ম।", M),
 ("a : b = 2 : 3 এবং b : c = 3 : 4 হলে a : c = কত?", "1 : 2", ["3 : 4", "2 : 3", "3 : 2"], "a : b : c = 2 : 3 : 4।", M),
]
def e_abc(b):
    a_, b1, b2, c_ = R.randint(1, 7), R.randint(1, 7), R.randint(1, 7), R.randint(1, 7)
    A, B, C = a_ * b2, b1 * b2, b1 * c_
    g = math.gcd(math.gcd(A, B), C); A, B, C = A // g, B // g, C // g
    b.add(f"a : b = {a_} : {b1} এবং b : c = {b2} : {c_} হলে a : b : c = কত?", f"{A} : {B} : {C}", [f"{a_} : {b1} : {c_}", f"{C} : {B} : {A}" if (C, A) != (A, C) else f"{A + 1} : {B} : {C}", f"{a_ * b1} : {b1 * b2} : {b2 * c_}" if (a_ * b1, b1 * b2, b2 * c_) != (A, B, C) else f"{A} : {B + 1} : {C}"], "b-এর মান সমান করে।", E)
def e_mid(b):
    a_, k = R.randint(1, 6), R.randint(2, 4)
    b.add(f"{a_}, x, {a_ * k * k} ক্রমিক সমানুপাতী হলে x = কত? (x > 0)", a_ * k, [a_ * k * k // 2 if a_ * k * k % 2 == 0 and a_ * k * k // 2 != a_ * k else a_ * k + 2, a_ * k + 1, a_ * k * k], f"x² = {a_} × {a_ * k * k} ⇒ x = {a_ * k}।", E)
def e_div3(b):
    r = R.choice([(1, 2, 3), (2, 3, 4), (3, 4, 5), (1, 3, 5), (2, 5, 8), (1, 1, 2), (4, 5, 6), (3, 5, 7)]); k = R.randint(5, 40)
    tot = sum(r) * k
    b.add(f"{tot} টাকা {r[0]} : {r[1]} : {r[2]} অনুপাতে ভাগ করলে ক্ষুদ্রতম অংশ কত?", min(r) * k, [max(r) * k, tot // 3 if tot % 3 == 0 and tot // 3 != min(r) * k else min(r) * k + k, min(r) * k + 5], f"প্রতি অংশ {k}।", E)
def m_find(b):
    a_, b_, c_ = R.randint(1, 6), R.randint(1, 6), R.randint(1, 6); k = R.randint(2, 6)
    x, y, z = a_ * k, b_ * k, c_ * k
    b.add(f"x : y : z = {a_} : {b_} : {c_} এবং x + y + z = {x + y + z} হলে y = কত?", y, [x if x != y else y + k, z if z not in (y, x) else y + 2 * k, y + 1], f"প্রতি অংশ {k}; y = {b_} × {k} = {y}।", M)
def m_partner(b):
    c1, c2 = R.choice([(2000, 3000), (5000, 3000), (4000, 6000), (3000, 7000), (1500, 2500), (6000, 9000)])
    profit = R.choice([1000, 2000, 2500, 5000, 4000])
    g = math.gcd(c1, c2); s1, s2 = c1 // g, c2 // g
    if profit % (s1 + s2): return
    v = profit * s1 // (s1 + s2)
    b.add(f"ক {c1} টাকা ও খ {c2} টাকা দিয়ে ব্যবসা শুরু করে {profit} টাকা লাভ করল। মূলধনের অনুপাতে ক কত টাকা পাবে?", v, [profit - v, profit // 2 if profit // 2 != v else v + 100, v + 100], f"অনুপাত {s1} : {s2}; ক পাবে {profit} × {s1}/{s1 + s2} = {v}।", M)
def m_cont(b):
    a_, r = R.randint(1, 5), R.randint(2, 4)
    t = [a_, a_ * r, a_ * r * r, a_ * r ** 3]
    b.add(f"{t[0]}, {t[1]}, {t[2]}, x ক্রমিক সমানুপাতী হলে x = কত?", t[3], [t[2] + t[1], t[3] + r, t[2] * 2 if t[2] * 2 != t[3] else t[3] + 1], f"সাধারণ অনুপাত 1 : {r}; x = {t[3]}।", M)
def m_inverse(b):
    w, d = R.choice([(10, 12), (12, 15), (8, 18), (15, 20), (6, 20), (20, 9), (24, 10)])
    w2 = R.choice([v for v in (4, 5, 6, 8, 10, 12, 15, 16, 20, 24, 30, 40) if (w * d) % v == 0 and v != w])
    v = w * d // w2
    b.add(f"{w} জন লোক একটি কাজ {d} দিনে করে। {w2} জন লোক কাজটি কত দিনে করবে?", v, [d * w2 // w if d * w2 % w == 0 and d * w2 // w != v else v + 2, v + 1, v - 1], f"ব্যস্ত সমানুপাত: {w} × {d} = {w2} × x ⇒ x = {v}।", M)
def m_cons(b):
    k = R.randint(2, 9); a_, b_, c_ = R.randint(1, 9), R.randint(1, 9), R.randint(1, 9)
    x, y, z = a_ * k, b_ * k, c_ * k
    b.add(f"x/{a_} = y/{b_} = z/{c_} এবং x + y + z = {x + y + z} হলে প্রতিটি অনুপাতের মান কত?", k, [k + 1, x + y + z, (a_ + b_ + c_)], f"(x + y + z)/({a_} + {b_} + {c_}) = {x + y + z}/{a_ + b_ + c_} = {k}।", M) if k not in (x + y + z, a_ + b_ + c_) else None
def h_split(b):
    r = R.choice([(F(1, 2), F(1, 3), F(1, 4)), (F(1, 2), F(1, 3), F(1, 6)), (F(1, 3), F(1, 4), F(1, 6)), (F(1, 2), F(1, 4), F(1, 8))])
    l = math.lcm(*[x.denominator for x in r]); w = [int(x * l) for x in r]
    k = R.randint(5, 30); tot = sum(w) * k
    b.add(f"{tot} টাকা তিনজনের মধ্যে {fr(r[0])} : {fr(r[1])} : {fr(r[2])} অনুপাতে ভাগ করলে প্রথমজন কত পাবে?", w[0] * k, [w[2] * k, tot // 3 if tot % 3 == 0 and tot // 3 != w[0] * k else w[0] * k + k, w[1] * k], f"অনুপাত {w[0]} : {w[1]} : {w[2]}; প্রথমজন {w[0] * k}।", H)
def h_mix(b):
    a_, b_ = R.choice([(3, 2), (5, 3), (4, 1), (7, 3), (2, 1)]); k = R.randint(2, 8); add = R.randint(2, 10)
    m, w = a_ * k, b_ * k
    g = math.gcd(m, w + add)
    b.add(f"একটি মিশ্রণে দুধ ও পানির অনুপাত {a_} : {b_}। মিশ্রণের পরিমাণ {m + w} লিটার। আরও {add} লিটার পানি মেশালে নতুন অনুপাত কত?", rt(m, w + add), [rt(a_, b_ + add), rt(m + add, w), rt(m, w)], f"দুধ {m}, পানি {w + add} লিটার।", H)
def h_abc_val(b):
    a_, b_, c_ = R.sample(range(1, 7), 3)
    # a/b = b/c? use x:y:z with expression
    p = R.randint(1, 4)
    n = a_ + b_ + c_; d = a_ * p
    g = math.gcd(n, d)
    b.add(f"a : b : c = {a_} : {b_} : {c_} হলে (a + b + c) : {p}a = কত?", rt(n, d), [rt(d, n), rt(n, a_), rt(n + 1, d)] if rt(n, a_) != rt(n, d) else [rt(d, n), rt(n + 1, d), rt(n, d + 1)], f"a = {a_}k, … বসিয়ে {n}k : {d}k।", H)
I112 = run('11.2', R, fx112, [e_abc, e_mid, e_div3], [m_find, m_partner, m_cont, m_inverse, m_cons], [h_split, h_mix, h_abc_val], caps=(10, 10, 8))
save(11, I111 + I112)
