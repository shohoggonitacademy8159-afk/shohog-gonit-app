#!/usr/bin/env python3
"""৬ষ্ঠ শ্রেণি গণিত (c6)। অধ্যায় 5, 7, 8: 300টি (অধ্যায়ভিত্তিক); বাকি প্রতিটি অনুশীলনী 100টি। হার: সহজ 50%, মধ্যম 40%, কঠিন 10%।
1.1 অঙ্কপাতন ও গণনা রীতি · 1.2 মৌলিক সংখ্যা ও বিভাজ্যতা · 1.3 গ.সা.গু. ও ল.সা.গু. · 1.4 ভগ্নাংশের তুলনা, যোগ ও বিয়োগ
1.5 ভগ্নাংশের গুণ, ভাগ ও সরলীকরণ · 1.6 দশমিক ভগ্নাংশ · 2.1 অনুপাত · 2.2 অনুপাত ও শতকরা · 2.3 ঐকিক নিয়ম
3.1 পূর্ণসংখ্যা ও ক্রম · 3.2 পূর্ণসংখ্যার যোগ · 3.3 পূর্ণসংখ্যার বিয়োগ · 4.1 প্রতীক, চলক, সহগ ও পদ · 4.2 সূচক · 4.3 সদৃশ পদ, যোগ ও বিয়োগ
5 সরল সমীকরণ · 6.1 রেখা, কোণ ও সমান্তরাল রেখা · 6.2 ত্রিভুজ ও চতুর্ভুজ · 7 ব্যবহারিক জ্যামিতি · 8 তথ্য ও উপাত্ত"""
import random, pathlib, sys, math
from fractions import Fraction as F
from itertools import permutations
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from mcqlib import Bank, save, E, M, H, fr, num, pfmt, sup, dec

R = random.Random(2026110206)
def W(c, pool):
    out = []
    for w in pool:
        w = str(w)
        if w != str(c) and w not in out: out.append(w)
    return out
def nz(a, b): return R.choice([v for v in range(a, b + 1) if v])

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

def grp(n, sizes):
    s = str(n); out = []
    i = 0
    while s:
        k = sizes[min(i, len(sizes) - 1)]; out.insert(0, s[-k:]); s = s[:-k]; i += 1
    return ','.join(out)
IND = lambda n: grp(n, [3, 2])
INT = lambda n: grp(n, [3, 3])
PL_BN = ['একক', 'দশক', 'শতক', 'হাজার', 'অযুত', 'লক্ষ', 'নিযুত', 'কোটি', 'দশ কোটি']
PL_IN = ['একক', 'দশক', 'শতক', 'হাজার', 'দশ হাজার', 'শত হাজার', 'মিলিয়ন', 'দশ মিলিয়ন', 'শত মিলিয়ন']
def rnum(dig):
    return R.randint(10 ** (dig - 1), 10 ** dig - 1)
PR = [p for p in range(2, 600) if all(p % d for d in range(2, int(p ** .5) + 1))]
def isp(n): return n in PR
def comp_odd(lo, hi):
    return [n for n in range(lo, hi) if n > 3 and not isp(n)]
def pf(n):
    out, d = [], 2
    while n > 1:
        while n % d == 0: out.append(d); n //= d
        d += 1
    return out
def nfac(n): return sum(1 for d in range(1, n + 1) if n % d == 0)
def lcm(a, b): return a * b // math.gcd(a, b)
def tk(v): return f"{v} টাকা"
def D(x):
    x = F(x); d = x.denominator; k = 0
    while d % 2 == 0: d //= 2
    while d % 5 == 0: d //= 5
    if d != 1: return fr(x)
    neg = x < 0; x = abs(x); p = 0
    while (x * 10 ** p).denominator != 1: p += 1
    n = str((x * 10 ** p).numerator).rjust(p + 1, '0')
    out = n if p == 0 else n[:-p] + '.' + n[-p:]
    return ('−' if neg else '') + out

# ===================================================== 1.1 অঙ্কপাতন ও গণনা রীতি
fx11 = [
 ("দেশীয় গণনা রীতিতে কোটির ঘরের পরের (বামের) ঘরটি কী?", "দশ কোটি", ["নিযুত", "অযুত", "শত কোটি"], "", E),
 ("আন্তর্জাতিক রীতিতে 1 মিলিয়ন = দেশীয় রীতিতে কত?", "10 লক্ষ", ["1 লক্ষ", "1 কোটি", "100 লক্ষ"], "", E),
 ("1 কোটি = আন্তর্জাতিক রীতিতে কত?", "10 মিলিয়ন", ["1 মিলিয়ন", "100 মিলিয়ন", "1 বিলিয়ন"], "", E),
 ("দেশীয় রীতিতে কমা বসানো হয় ডান দিক থেকে কীভাবে?", "প্রথমে তিন অঙ্ক পরে, তারপর দুই অঙ্ক পরপর", ["সবসময় তিন অঙ্ক পরপর", "সবসময় দুই অঙ্ক পরপর", "প্রথমে দুই অঙ্ক পরে, তারপর তিন অঙ্ক পরপর"], "", E),
 ("আন্তর্জাতিক রীতিতে কমা বসানো হয় কীভাবে?", "ডান দিক থেকে তিন অঙ্ক পরপর", ["ডান দিক থেকে দুই অঙ্ক পরপর", "বাম দিক থেকে দুই অঙ্ক পরপর", "প্রথমে তিন, পরে দুই অঙ্ক পরপর"], "", E),
 ("1 বিলিয়ন = দেশীয় রীতিতে কত?", "100 কোটি", ["10 কোটি", "1000 কোটি", "10 লক্ষ"], "", M),
]
def a11_name(b, lv):
    dig = R.randint(6, 9); n = rnum(dig); s = str(n); k = R.randrange(dig); d = s[dig - 1 - k]
    if s.count(d) != 1: return
    ind = R.random() < .6
    PL = PL_BN if ind else PL_IN
    b.add(f"{(IND if ind else INT)(n)} সংখ্যাটিতে {d} অঙ্কটি {'দেশীয়' if ind else 'আন্তর্জাতিক'} রীতিতে কোন স্থানে আছে?", PL[k], W(PL[k], [PL[k + 1] if k + 1 < len(PL) else PL[k - 2], PL[k - 1] if k else PL[k + 2], PL[(k + 3) % len(PL)], PL[(k + 4) % len(PL)]]), "ডান দিক থেকে স্থান গণনা।", lv)
def a11_val(b, lv):
    dig = R.randint(5, 9); n = rnum(dig); s = str(n); k = R.randrange(dig); d = int(s[dig - 1 - k])
    if d == 0 or s.count(str(d)) != 1: return
    v = d * 10 ** k
    b.add(f"{IND(n)} সংখ্যায় {d} এর স্থানীয় মান কত?", IND(v), W(IND(v), [IND(d * 10 ** (k + 1)), IND(d * 10 ** max(k - 1, 0)) if k else str(d * 100), str(d) if k else IND(d * 1000), IND(d * 10 ** (k + 2))]), "অঙ্ক × স্থানের মান।", lv)
def a11_ind(b, lv):
    n = rnum(R.randint(7, 9)); c = IND(n)
    b.add(f"দেশীয় রীতিতে {n} সংখ্যাটিতে কমা বসালে কোনটি হবে?", c, W(c, [INT(n), grp(n, [2]), grp(n, [3, 3, 2]), grp(n, [2, 3])]), "ডান দিক থেকে প্রথমে 3 অঙ্ক, পরে 2 অঙ্ক পরপর।", lv)
def a11_int(b, lv):
    n = rnum(R.randint(7, 9)); c = INT(n)
    b.add(f"আন্তর্জাতিক রীতিতে {n} সংখ্যাটিতে কমা বসালে কোনটি হবে?", c, W(c, [IND(n), grp(n, [2]), grp(n, [3, 3, 2]), grp(n, [2, 3])]), "ডান দিক থেকে 3 অঙ্ক পরপর।", lv)
def a11_ext(b, lv):
    d = R.randint(2, 10); big = R.random() < .5
    v = 10 ** d - 1 if big else 10 ** (d - 1)
    b.add(f"{d} অঙ্কের {'বৃহত্তম' if big else 'ক্ষুদ্রতম'} সংখ্যা কোনটি?", IND(v), W(IND(v), [IND(10 ** d) if big else IND(10 ** d - 1), IND(10 ** (d - 1) - 1) if big else IND(10 ** (d - 2) if d > 2 else 1), IND(10 ** (d - 1)) if big else IND(10 ** d), IND(v + 1) if not big else IND(10 ** (d + 1) - 1)]), "", lv)
def a11_conv(b, lv):
    t = R.randrange(4); x = R.randint(2, 99)
    q, c, w = [
        (f"{x} মিলিয়ন = কত লক্ষ?", 10 * x, [x, 100 * x, F(x, 10)]),
        (f"{x} কোটি = কত মিলিয়ন?", 10 * x, [x, 100 * x, F(x, 10)]),
        (f"{x} বিলিয়ন = কত কোটি?", 100 * x, [10 * x, 1000 * x, x]),
        (f"{x} লক্ষ = কত হাজার?", 100 * x, [10 * x, 1000 * x, x]),
    ][t]
    b.add(q, f"{fr(c)}", W(fr(c), [fr(v) for v in w] + [fr(c + 10)]), "", lv)
def digs(k, zero=True):
    return R.sample(range(0 if zero else 1, 10), k)
def a11_form(b, lv):
    ds = digs(R.randint(4, 6)); big = R.random() < .5
    s = sorted(ds, reverse=big)
    if not big and s[0] == 0: s[0], s[1] = s[1], s[0]
    v = int(''.join(map(str, s)))
    alt = int(''.join(map(str, sorted(ds)))) if sorted(ds)[0] else int(''.join(map(str, sorted(ds)[1:]))); rev = int(''.join(map(str, sorted(ds, reverse=not big))).lstrip('0') or 0)
    b.add(f"{', '.join(map(str, ds))} অঙ্কগুলো প্রত্যেকটি একবার ব্যবহার করে গঠিত {'বৃহত্তম' if big else 'ক্ষুদ্রতম'} সংখ্যা কোনটি?", IND(v), W(IND(v), [IND(alt), IND(rev), IND(v + 9), IND(int(str(v)[:-2] + str(v)[-1] + str(v)[-2]))]), "বৃহত্তমে বড় অঙ্ক বামে; ক্ষুদ্রতমে 0 প্রথমে বসে না।", lv)
def a11_two(b, lv):
    d = R.randint(1, 9); i, j = sorted(R.sample(range(0, 7), 2), reverse=True)
    s = [str(R.choice([x for x in range(10) if x != d])) for _ in range(7)]
    s[6 - i] = str(d); s[6 - j] = str(d)
    if s[0] == '0': s[0] = str(R.choice([x for x in range(1, 10) if x != d]))
    n = int(''.join(s)); v = d * (10 ** i - 10 ** j)
    b.add(f"{IND(n)} সংখ্যায় দুটি {d} এর স্থানীয় মানের পার্থক্য কত?", IND(v), W(IND(v), [IND(d * (10 ** i + 10 ** j)), IND(d * 10 ** i), IND(v * 10), "0"]), "বড় স্থানীয় মান − ছোট স্থানীয় মান।", lv)
def a11_face(b, lv):
    n = rnum(7); s = str(n); k = R.randrange(1, 7); d = int(s[6 - k])
    if d == 0 or s.count(str(d)) != 1: return
    v = d * 10 ** k - d
    b.add(f"{IND(n)} সংখ্যায় {d} এর স্থানীয় মান ও প্রকৃত মানের পার্থক্য কত?", IND(v), W(IND(v), [IND(d * 10 ** k), IND(d * 10 ** k + d), str(d), IND(v + 1)]), "স্থানীয় মান − প্রকৃত (নিজস্ব) মান।", lv)
def a11_even(b, lv):
    ds = digs(R.randint(4, 5)); big = R.random() < .5; odd = R.random() < .5
    ok = [int(''.join(map(str, p))) for p in permutations(ds) if p[0] != 0 and p[-1] % 2 == (1 if odd else 0)]
    if len(ok) < 2: return
    v = max(ok) if big else min(ok)
    all_ = [int(''.join(map(str, p))) for p in permutations(ds) if p[0] != 0]
    b.add(f"{', '.join(map(str, ds))} অঙ্কগুলো একবার করে ব্যবহার করে গঠিত {'বৃহত্তম' if big else 'ক্ষুদ্রতম'} {'বিজোড়' if odd else 'জোড়'} সংখ্যা কোনটি?", IND(v), W(IND(v), [IND(max(all_) if big else min(all_)), IND(sorted(ok)[-2] if big else sorted(ok)[1]), IND(min(ok) if big else max(ok)), IND(v + 2)]), "শেষ অঙ্ক জোড়/বিজোড় রেখে বাকিগুলো সাজাও।", lv)
def a11_sum(b, lv):
    ds = digs(4); all_ = [int(''.join(map(str, p))) for p in permutations(ds) if p[0] != 0]
    hi, lo = max(all_), min(all_); dif = R.random() < .5
    v = hi - lo if dif else hi + lo
    b.add(f"{', '.join(map(str, ds))} অঙ্কগুলো একবার করে ব্যবহার করে গঠিত বৃহত্তম ও ক্ষুদ্রতম সংখ্যার {'পার্থক্য' if dif else 'যোগফল'} কত?", IND(v), W(IND(v), [IND(hi + lo if dif else hi - lo), IND(v + 9), IND(v - 90), IND(hi)]), "", lv)
def a11_nd(b, lv):
    d = R.randint(3, 9); v = (10 ** d - 1) - 10 ** (d - 1)
    s = R.random() < .5
    if s: v = (10 ** d - 1) + 10 ** (d - 1)
    b.add(f"{d} অঙ্কের বৃহত্তম ও ক্ষুদ্রতম সংখ্যার {'যোগফল' if s else 'পার্থক্য'} কত?", IND(v), W(IND(v), [IND((10 ** d - 1) - 10 ** (d - 1) if s else (10 ** d - 1) + 10 ** (d - 1)), IND(v + 1), IND(v - 1), IND(10 ** d)]), "", lv)
P11 = part('1.1', 100, fx11, [a11_name, a11_val, a11_ind, a11_int, a11_ext], [a11_conv, a11_form, a11_two, a11_face, a11_val], [a11_even, a11_sum, a11_nd])

# ===================================================== 1.2 মৌলিক সংখ্যা ও বিভাজ্যতা
fx12 = [
 ("ক্ষুদ্রতম মৌলিক সংখ্যা কোনটি?", "2", ["1", "3", "0"], "", E),
 ("একমাত্র জোড় মৌলিক সংখ্যা কোনটি?", "2", ["4", "0", "6"], "", E),
 ("1 সংখ্যাটি কী?", "মৌলিকও নয়, যৌগিকও নয়", ["মৌলিক", "যৌগিক", "জোড় মৌলিক"], "", E),
 ("যে দুটি সংখ্যার 1 ছাড়া কোনো সাধারণ গুণনীয়ক নেই, তাদের কী বলে?", "সহমৌলিক", ["যৌগিক", "মৌলিক জোড়", "গুণিতক"], "", E),
 ("কোনো সংখ্যার অঙ্কগুলোর যোগফল 9 দ্বারা বিভাজ্য হলে সংখ্যাটি কোন সংখ্যা দ্বারা অবশ্যই বিভাজ্য?", "9", ["2", "5", "4"], "", E),
 ("কোনো সংখ্যার শেষ দুই অঙ্কের সংখ্যা 4 দ্বারা বিভাজ্য হলে সংখ্যাটি কোন সংখ্যা দ্বারা বিভাজ্য?", "4", ["3", "8", "9"], "", M),
 ("1 থেকে 100 পর্যন্ত মৌলিক সংখ্যা কয়টি?", "25", ["24", "26", "20"], "", M),
]
def b12_prime(b, lv):
    p = R.choice([x for x in PR if x < 200]); w = R.sample([x for x in comp_odd(9, 200) if x % 2], 3)
    b.add("নিচের কোনটি মৌলিক সংখ্যা?", p, W(p, w), f"{p} এর 1 ও {p} ছাড়া কোনো গুণনীয়ক নেই।", lv)
def b12_comp(b, lv):
    c = R.choice([x for x in comp_odd(9, 200) if x % 2]); w = R.sample([x for x in PR if 10 < x < 200], 3)
    b.add("নিচের কোনটি যৌগিক সংখ্যা?", c, W(c, w), f"{c} = {' × '.join(map(str, pf(c)))}।", lv)
def b12_div(b, lv):
    k = R.choice([2, 3, 4, 5, 6, 8, 9, 10])
    c = k * R.randint(100 // k + 1, 99999 // k)
    w = []
    while len(w) < 3:
        x = R.randint(100, 99999)
        if x % k and x not in w: w.append(x)
    b.add(f"নিচের কোন সংখ্যাটি {k} দ্বারা বিভাজ্য?", c, W(c, w), "", lv)
def b12_cop(b, lv):
    while True:
        a, c = R.randint(4, 60), R.randint(4, 60)
        if a != c and math.gcd(a, c) == 1: break
    w = []
    while len(w) < 3:
        x, y = R.randint(4, 60), R.randint(4, 60)
        if x != y and math.gcd(x, y) > 1 and f"{x}, {y}" not in w: w.append(f"{x}, {y}")
    b.add("নিচের কোন জোড়াটি সহমৌলিক?", f"{a}, {c}", W(f"{a}, {c}", w), "সাধারণ গুণনীয়ক শুধু 1।", lv)
def b12_count(b, lv):
    a = R.randint(1, 80); h = a + R.randint(15, 40)
    v = sum(1 for p in PR if a < p < h)
    b.add(f"{a} ও {h} এর মধ্যে মৌলিক সংখ্যা কয়টি?", v, W(v, [v + 1, v - 1, v + 2, v - 2]), "", lv)
def b12_miss(b, lv):
    k = R.choice([3, 9]); ln = R.randint(3, 5); pos = R.randrange(1, ln)
    ds = [R.randint(1, 9)] + [R.randint(0, 9) for _ in range(ln - 1)]
    s0 = sum(d for i, d in enumerate(ds) if i != pos)
    v = (-s0) % k
    pat = ''.join('*' if i == pos else str(d) for i, d in enumerate(ds))
    b.add(f"{pat} সংখ্যাটি {k} দ্বারা বিভাজ্য হলে * এর স্থানে ক্ষুদ্রতম অঙ্ক কত?", v, W(v, [(v + 1) % 10, (v + 2) % 10, (v + k - 1) % 10 if k == 9 else (v + 4) % 10, 9 - v if 9 - v != v else 8]), "অঙ্কগুলোর যোগফল যেন বিভাজ্য হয়।", lv)
def b12_fact(b, lv):
    n = R.randint(12, 400); f = pf(n)
    if len(f) < 3: return
    c = ' × '.join(map(str, f))
    w1 = f[:]; w1[-1] = w1[-1] + 2 if w1[-1] + 2 in PR else w1[-1] + 1
    w2 = f[:-1] + [f[-1] * 2]
    w3 = f + [2]
    b.add(f"{n} কে মৌলিক উৎপাদকে প্রকাশ করলে কোনটি হবে?", c, W(c, [' × '.join(map(str, w1)), ' × '.join(map(str, w2)), ' × '.join(map(str, w3)), ' × '.join(map(str, f[1:]))]), "", lv)
def b12_pset(b, lv):
    n = R.randint(20, 500); s = sorted(set(pf(n)))
    if len(s) < 2: return
    c = ', '.join(map(str, s))
    nxt = [p for p in PR if p not in s][:3]
    b.add(f"{n} এর মৌলিক গুণনীয়কগুলো কী কী?", c, W(c, [', '.join(map(str, sorted(s + [nxt[0]]))), ', '.join(map(str, s[1:] + [nxt[1]])), ', '.join(map(str, sorted(s[:-1] + [nxt[2]]))), ', '.join(map(str, s[:-1]))]), "", lv)
def b12_nf(b, lv):
    n = R.randint(12, 200); v = nfac(n)
    b.add(f"{n} এর গুণনীয়ক কয়টি?", v, W(v, [v + 1, v - 1, v + 2, len(pf(n))]), "সব গুণনীয়ক গুনে দেখো।", lv)
def b12_psum(b, lv):
    a = R.randint(1, 60); h = a + R.randint(10, 25)
    s = [p for p in PR if a < p < h]
    if len(s) < 2: return
    v = sum(s)
    b.add(f"{a} ও {h} এর মধ্যবর্তী মৌলিক সংখ্যাগুলোর যোগফল কত?", v, W(v, [v + s[0], v - s[-1], v + 2, v - 2]), f"মৌলিক সংখ্যাগুলো: {', '.join(map(str, s))}।", lv)
P12 = part('1.2', 100, fx12, [b12_prime, b12_comp, b12_div, b12_cop], [b12_count, b12_miss, b12_fact, b12_pset, b12_div], [b12_nf, b12_psum, b12_miss])

# ===================================================== 1.3 গ.সা.গু. ও ল.সা.গু.
fx13 = [
 ("দুটি সংখ্যার গুণফল সমান কোনটি?", "তাদের গ.সা.গু. × ল.সা.গু.", ["গ.সা.গু. + ল.সা.গু.", "ল.সা.গু. ÷ গ.সা.গু.", "গ.সা.গু.²"], "", E),
 ("দুটি সহমৌলিক সংখ্যার গ.সা.গু. কত?", "1", ["0", "সংখ্যা দুটির গুণফল", "বড় সংখ্যাটি"], "", E),
 ("দুটি সহমৌলিক সংখ্যার ল.সা.গু. কত?", "সংখ্যা দুটির গুণফল", ["1", "সংখ্যা দুটির যোগফল", "ছোট সংখ্যাটি"], "", M),
]
def c13_h(b, lv):
    g = R.randint(2, 15); a, c = g * R.randint(2, 9), g * R.randint(2, 9)
    if a == c: return
    v = math.gcd(a, c)
    b.add(f"{a} ও {c} এর গ.সা.গু. কত?", v, W(v, [lcm(a, c), v * 2, max(1, v // 2), g + 1]), "", lv)
def c13_l(b, lv):
    a, c = R.randint(4, 40), R.randint(4, 40)
    if a == c: return
    v = lcm(a, c)
    b.add(f"{a} ও {c} এর ল.সা.গু. কত?", v, W(v, [a * c if a * c != v else v * 2, math.gcd(a, c), v + a, v // 2 if v % 2 == 0 else v + c]), "", lv)
def c13_h3(b, lv):
    g = R.randint(2, 12); xs = [g * R.randint(2, 12) for _ in range(3)]
    if len(set(xs)) < 3: return
    v = math.gcd(math.gcd(xs[0], xs[1]), xs[2])
    b.add(f"{', '.join(map(str, xs))} এর গ.সা.গু. কত?", v, W(v, [v * 2, v * 3, max(1, v // 2), min(xs)]), "", lv)
def c13_l3(b, lv):
    xs = R.sample(range(2, 25), 3)
    v = lcm(lcm(xs[0], xs[1]), xs[2])
    b.add(f"{', '.join(map(str, xs))} এর ল.সা.গু. কত?", v, W(v, [xs[0] * xs[1] * xs[2] if xs[0] * xs[1] * xs[2] != v else v * 2, v * 2, v // 2 if v % 2 == 0 else v + 1, max(xs) * 2]), "", lv)
def c13_prod(b, lv):
    g = R.randint(2, 12); x, y = R.sample(range(1, 12), 2)
    if math.gcd(x, y) != 1: return
    a, c = g * x, g * y; L = g * x * y
    b.add(f"দুটি সংখ্যার গ.সা.গু. {g} ও ল.সা.গু. {L}। একটি সংখ্যা {a} হলে অপরটি কত?", c, W(c, [L // g, a, g * L // max(1, a) + g, c + g]), "অপর সংখ্যা = গ.সা.গু. × ল.সা.গু. ÷ প্রদত্ত সংখ্যা।", lv)
def c13_rem(b, lv):
    g = R.randint(5, 30); r1 = R.randint(1, g - 1); r2 = R.randint(1, g - 1)
    a, c = g * R.randint(3, 15) + r1, g * R.randint(3, 15) + r2
    if math.gcd(a - r1, c - r2) != g or a == c: return
    b.add(f"কোন বৃহত্তম সংখ্যা দিয়ে {a} ও {c} কে ভাগ করলে যথাক্রমে {r1} ও {r2} অবশিষ্ট থাকে?", g, W(g, [math.gcd(a, c), g * 2, g + r1, max(1, g - 1)]), f"{a - r1} ও {c - r2} এর গ.সা.গু.।", lv)
def c13_small(b, lv):
    xs = R.sample(range(3, 20), 3); r = R.randint(1, min(xs) - 1)
    L = lcm(lcm(xs[0], xs[1]), xs[2]); v = L + r
    b.add(f"কোন ক্ষুদ্রতম সংখ্যাকে {', '.join(map(str, xs))} দ্বারা ভাগ করলে প্রতিক্ষেত্রে {r} অবশিষ্ট থাকে?", v, W(v, [L, L - r, L * 2 + r, v + 1]), "ল.সা.গু. + অবশিষ্ট।", lv)
def c13_bell(b, lv):
    xs = R.sample(range(4, 30), 3); L = lcm(lcm(xs[0], xs[1]), xs[2])
    if L > 600: return
    b.add(f"তিনটি ঘণ্টা যথাক্রমে {xs[0]}, {xs[1]} ও {xs[2]} মিনিট পরপর বাজে। একসাথে বাজার পর আবার কত মিনিট পর একসাথে বাজবে?", L, W(L, [sum(xs), L * 2, xs[0] * xs[1], L // 2 if L % 2 == 0 else L + 1]), "ল.সা.গু. নির্ণয় করো।", lv)
def c13_4d(b, lv):
    xs = R.sample(range(4, 25), 3); L = lcm(lcm(xs[0], xs[1]), xs[2])
    if L > 999: return
    v = ((1000 + L - 1) // L) * L
    b.add(f"চার অঙ্কের কোন ক্ষুদ্রতম সংখ্যা {', '.join(map(str, xs))} দ্বারা নিঃশেষে বিভাজ্য?", v, W(v, [v - L if v - L >= 1000 else v + L, 1000, L, v + L]), "", lv)
P13 = part('1.3', 100, fx13, [c13_h, c13_l], [c13_h3, c13_l3, c13_prod], [c13_rem, c13_small, c13_bell, c13_4d])

# ===================================================== 1.4 ভগ্নাংশের তুলনা, যোগ ও বিয়োগ
fx14 = [
 ("যে ভগ্নাংশের লব হরের চেয়ে ছোট তাকে কী বলে?", "প্রকৃত ভগ্নাংশ", ["অপ্রকৃত ভগ্নাংশ", "মিশ্র ভগ্নাংশ", "দশমিক ভগ্নাংশ"], "", E),
 ("যে ভগ্নাংশের লব হরের সমান বা বড় তাকে কী বলে?", "অপ্রকৃত ভগ্নাংশ", ["প্রকৃত ভগ্নাংশ", "লঘিষ্ঠ ভগ্নাংশ", "সমহর ভগ্নাংশ"], "", E),
 ("ভগ্নাংশের লব ও হরকে একই অশূন্য সংখ্যা দিয়ে গুণ করলে মানের কী পরিবর্তন হয়?", "কোনো পরিবর্তন হয় না", ["দ্বিগুণ হয়", "অর্ধেক হয়", "শূন্য হয়"], "", E),
]
def frac(lo=2, hi=15):
    d = R.randint(lo, hi); n = R.randint(1, d - 1); return F(n, d)
def d14_low(b, lv):
    x = frac(3, 15); k = R.randint(2, 9)
    if x.denominator * k > 120: return
    b.add(f"{x.numerator * k}/{x.denominator * k} কে লঘিষ্ঠ আকারে প্রকাশ করলে কোনটি হবে?", fr(x), W(fr(x), [f"{x.numerator * k // math.gcd(k, 2) if k % 2 == 0 else x.numerator + 1}/{x.denominator * k // 2 if k % 2 == 0 else x.denominator + 1}", f"{x.denominator}/{x.numerator}", f"{x.numerator + 1}/{x.denominator}", f"{x.numerator}/{x.denominator + 1}"]), "লব ও হরকে গ.সা.গু. দিয়ে ভাগ।", lv)
def d14_eq(b, lv):
    x = frac(3, 12); k = R.randint(2, 8)
    c = f"{x.numerator * k}/{x.denominator * k}"
    b.add(f"নিচের কোনটি {fr(x)} এর সমতুল ভগ্নাংশ?", c, W(c, [f"{x.numerator * k}/{x.denominator * k + 1}", f"{x.numerator + k}/{x.denominator + k}", f"{x.denominator * k}/{x.numerator * k}", f"{x.numerator * k + 1}/{x.denominator * k}"]), "লব ও হরকে একই সংখ্যা দিয়ে গুণ।", lv)
def d14_mix(b, lv):
    w, x = R.randint(1, 9), frac(2, 12)
    v = w + x
    b.add(f"{w} {fr(x)} মিশ্র ভগ্নাংশকে অপ্রকৃত ভগ্নাংশে লিখলে কোনটি হবে?", fr(v), W(fr(v), [f"{w * x.numerator + x.denominator}/{x.denominator}", f"{w + x.numerator}/{x.denominator}", f"{w * x.denominator}/{x.denominator}", f"{v.numerator}/{v.denominator + 1}"]), "পূর্ণ সংখ্যা × হর + লব।", lv)
def d14_big(b, lv):
    xs = set()
    while len(xs) < 4: xs.add(frac(2, 12))
    xs = list(xs); big = R.random() < .5
    c = max(xs) if big else min(xs)
    b.add(f"নিচের কোন ভগ্নাংশটি {'বৃহত্তম' if big else 'ক্ষুদ্রতম'}?", fr(c), W(fr(c), [fr(v) for v in xs]), "সমহর করে তুলনা।", lv)
def d14_add(b, lv):
    x, y = frac(2, 12), frac(2, 12)
    if x.denominator == y.denominator: return
    sub = R.random() < .45
    if sub and x < y: x, y = y, x
    v = x - y if sub else x + y
    if v == 0: return
    wrong = F(x.numerator - y.numerator if sub else x.numerator + y.numerator, x.denominator + y.denominator)
    b.add(f"{fr(x)} {'−' if sub else '+'} {fr(y)} = কত?", fr(v), W(fr(v), [fr(wrong) if wrong > 0 else '0', fr(x + y if sub else abs(x - y)), fr(v + F(1, x.denominator * y.denominator)), fr(v * 2)]), "হরের ল.সা.গু. নিয়ে সমহর করো।", lv)
def d14_ord(b, lv):
    xs = set()
    while len(xs) < 3: xs.add(frac(2, 12))
    s = sorted(xs); c = ' < '.join(map(fr, s))
    w = [' < '.join(map(fr, p)) for p in permutations(s) if list(p) != s]
    R.shuffle(w)
    b.add(f"{', '.join(fr(v) for v in R.sample(s, 3))} ভগ্নাংশগুলোকে মানের ঊর্ধ্বক্রমে সাজালে কোনটি হবে?", c, W(c, w), "সমহর করে লবের তুলনা।", lv)
def d14_mix2(b, lv):
    a, c = R.randint(1, 6), R.randint(1, 6); x, y = frac(2, 9), frac(2, 9)
    v = a + x + c + y
    w = int(v); r = v - w
    ans = f"{w} {fr(r)}" if r else str(w)
    b.add(f"{a} {fr(x)} + {c} {fr(y)} = কত?", ans, W(ans, [f"{w + 1} {fr(r)}" if r else str(w + 1), f"{a + c} {fr(F(x.numerator + y.numerator, x.denominator + y.denominator))}", f"{w - 1} {fr(r)}" if r else str(w - 1), f"{w} {fr(r + F(1, 12)) if r + F(1, 12) < 1 else '1/12'}"]), "পূর্ণ অংশ ও ভগ্নাংশ আলাদা যোগ।", lv)
def d14_rest(b, lv):
    x = frac(3, 8); y = frac(2, 6)
    left = (1 - x) * (1 - y)
    tot = R.choice([x.denominator * y.denominator * k for k in range(5, 40)])
    v = left * tot
    if v.denominator != 1: return
    b.add(f"একজন তার {tot} টাকার {fr(x)} অংশ খরচ করল এবং অবশিষ্ট টাকার {fr(y)} অংশ দান করল। তার কাছে কত টাকা রইল?", f"{v} টাকা", W(f"{v} টাকা", [f"{(1 - x - y) * tot} টাকা" if (1 - x - y) * tot > 0 and ((1 - x - y) * tot).denominator == 1 else f"{v + 10} টাকা", f"{(1 - x) * tot} টাকা", f"{tot - v} টাকা", f"{v * 2} টাকা"]), "প্রথমে বাকি অংশ, তারপর তার অংশ।", lv)
def d14_need(b, lv):
    x, y = frac(2, 10), frac(2, 10)
    if x >= y: x, y = y, x
    if x == y: return
    v = y - x
    b.add(f"{fr(x)} এর সাথে কত যোগ করলে যোগফল {fr(y)} হবে?", fr(v), W(fr(v), [fr(x + y), fr(F(abs(y.numerator - x.numerator), abs(y.denominator - x.denominator) or 1)), fr(v + F(1, 2 * y.denominator)), fr(y)]), "বড় ভগ্নাংশ − ছোট ভগ্নাংশ।", lv)
P14 = part('1.4', 100, fx14, [d14_low, d14_eq, d14_mix, d14_big], [d14_add, d14_ord, d14_mix2], [d14_rest, d14_need])

# ===================================================== 1.5 ভগ্নাংশের গুণ, ভাগ ও সরলীকরণ
fx15 = [
 ("কোনো ভগ্নাংশ দিয়ে ভাগ করা মানে কী দিয়ে গুণ করা?", "ভগ্নাংশটির বিপরীত (উল্টানো) ভগ্নাংশ", ["ভগ্নাংশটি নিজেই", "লব", "হর"], "", E),
 ("ভগ্নাংশের গ.সা.গু. = ?", "লবগুলোর গ.সা.গু. ÷ হরগুলোর ল.সা.গু.", ["লবগুলোর ল.সা.গু. ÷ হরগুলোর গ.সা.গু.", "লবগুলোর গ.সা.গু. ÷ হরগুলোর গ.সা.গু.", "হরগুলোর গ.সা.গু. ÷ লবগুলোর ল.সা.গু."], "", M),
 ("ভগ্নাংশের ল.সা.গু. = ?", "লবগুলোর ল.সা.গু. ÷ হরগুলোর গ.সা.গু.", ["লবগুলোর গ.সা.গু. ÷ হরগুলোর ল.সা.গু.", "লবগুলোর ল.সা.গু. ÷ হরগুলোর ল.সা.গু.", "হরগুলোর ল.সা.গু. ÷ লবগুলোর গ.সা.গু."], "", M),
]
def e15_mul(b, lv):
    x, y = frac(2, 12), frac(2, 12); v = x * y
    b.add(f"{fr(x)} × {fr(y)} = কত?", fr(v), W(fr(v), [fr(x / y), fr(x + y), fr(F(x.numerator * y.denominator, x.denominator * y.numerator)) if x != y else fr(v * 2), fr(v * 2)]), "লব × লব, হর × হর।", lv)
def e15_div(b, lv):
    x, y = frac(2, 12), frac(2, 12); v = x / y
    b.add(f"{fr(x)} ÷ {fr(y)} = কত?", fr(v), W(fr(v), [fr(x * y), fr(y / x), fr(v + 1), fr(F(x.numerator, y.numerator) if y.numerator else 1)]), "ভাজকের বিপরীত ভগ্নাংশ দিয়ে গুণ।", lv)
def e15_of(b, lv):
    x = frac(2, 12); n = x.denominator * R.randint(2, 30); v = x * n
    b.add(f"{n} এর {fr(x)} অংশ কত?", fr(v), W(fr(v), [fr(n / x) if (n / x).denominator == 1 else fr(v + 1), fr(v + x.numerator), fr(v - 1), fr(n - v)]), "", lv)
def e15_rec(b, lv):
    w = R.randint(1, 8); x = frac(2, 12); v = w + x
    b.add(f"{w} {fr(x)} এর বিপরীত ভগ্নাংশ কোনটি?", fr(1 / v), W(fr(1 / v), [fr(v), f"{x.denominator}/{x.numerator}", fr(1 / (w + 1 - x)), f"1/{w}"]), "প্রথমে অপ্রকৃত ভগ্নাংশ, পরে লব-হর উল্টাও।", lv)
def e15_hcf(b, lv):
    xs = []
    while len(xs) < 2:
        x = frac(2, 15)
        if x not in xs: xs.append(x)
    n = [x.numerator for x in xs]; d = [x.denominator for x in xs]
    h = F(math.gcd(*n), lcm(*d)); l = F(lcm(*n), math.gcd(*d))
    isl = R.random() < .5; c = l if isl else h
    b.add(f"{fr(xs[0])} ও {fr(xs[1])} এর {'ল.সা.গু.' if isl else 'গ.সা.গু.'} কত?", fr(c), W(fr(c), [fr(h if isl else l), fr(F(lcm(*n), lcm(*d))), fr(F(math.gcd(*n), math.gcd(*d))), fr(c * 2)]), "", lv)
def e15_simp(b, lv):
    x, y, z = frac(2, 8), frac(2, 8), frac(2, 8)
    v = x + y * z; wv = (x + y) * z
    b.add(f"{fr(x)} + {fr(y)} × {fr(z)} = কত?", fr(v), W(fr(v), [fr(wv), fr(x * y + z), fr(x + y + z), fr(v + F(1, 4))]), "আগে গুণ, পরে যোগ।", lv)
def e15_simp2(b, lv):
    x, y, z = frac(2, 8), frac(2, 8), frac(2, 8)
    v = (x + y) / z; wv = x + y / z
    b.add(f"({fr(x)} + {fr(y)}) ÷ {fr(z)} = কত?", fr(v), W(fr(v), [fr(wv), fr((x + y) * z), fr(v + 1), fr(z / (x + y))]), "আগে বন্ধনী, পরে ভাগ।", lv)
def e15_bamboo(b, lv):
    x, y = frac(4, 10), frac(4, 10)
    if x + y >= 1: return
    L = 1 - x - y
    tot = R.randint(4, 40) * lcm(x.denominator, y.denominator)
    rest = L * tot
    if rest.denominator != 1: return
    b.add(f"একটি খুঁটির {fr(x)} অংশ মাটিতে, {fr(y)} অংশ পানিতে এবং বাকি {rest} মিটার পানির উপরে আছে। খুঁটির দৈর্ঘ্য কত মিটার?", tot, W(tot, [tot + int(rest), int(rest / (1 - x)) if (rest / (1 - x)).denominator == 1 else tot * 2, tot - 2, tot + 4]), "বাকি অংশ = 1 − (দুই অংশের যোগফল)।", lv)
P15 = part('1.5', 100, fx15, [e15_mul, e15_div, e15_of, e15_rec], [e15_hcf, e15_simp, e15_of], [e15_simp2, e15_bamboo])

# ===================================================== 1.6 দশমিক ভগ্নাংশ
fx16 = [
 ("0.5 কে সাধারণ ভগ্নাংশে লিখলে কোনটি?", "1/2", ["1/5", "5/100", "2/5"], "", E),
 ("কোনো দশমিক সংখ্যাকে 10 দিয়ে গুণ করলে দশমিক বিন্দু কোন দিকে কত ঘর সরে?", "ডানে এক ঘর", ["বামে এক ঘর", "ডানে দুই ঘর", "সরে না"], "", E),
 ("কোনো দশমিক সংখ্যাকে 100 দিয়ে ভাগ করলে দশমিক বিন্দু কোন দিকে সরে?", "বামে দুই ঘর", ["ডানে দুই ঘর", "বামে এক ঘর", "ডানে এক ঘর"], "", E),
]
def rd(lo, hi, p): return F(R.randint(lo, hi), 10 ** p)
def f16_add(b, lv):
    x, y = rd(1, 9999, R.randint(1, 3)), rd(1, 9999, R.randint(1, 3)); sub = R.random() < .4
    if sub and x < y: x, y = y, x
    v = x - y if sub else x + y
    if v == 0: return
    b.add(f"{D(x)} {'−' if sub else '+'} {D(y)} = কত?", D(v), W(D(v), [D(v * 10), D(v / 10), D(x + y if sub else abs(x - y)), D(v + F(1, 10))]), "দশমিক বিন্দু বরাবর সাজিয়ে।", lv)
def f16_10(b, lv):
    x = rd(1, 99999, R.randint(1, 4)); k = R.choice([10, 100, 1000]); mul = R.random() < .5
    v = x * k if mul else x / k
    b.add(f"{D(x)} {'×' if mul else '÷'} {k} = কত?", D(v), W(D(v), [D(x / k if mul else x * k), D(v * 10), D(v / 10), D(x)]), "", lv)
def f16_fr(b, lv):
    x = F(R.choice([1, 3, 7, 9, 11, 13, 17, 19, 21, 23, 27]), R.choice([2, 4, 5, 8, 20, 25, 40, 50])) if R.random() < .7 else rd(1, 999, 3)
    if x.denominator == 1: return
    tofr = R.random() < .5
    if tofr: b.add(f"{D(x)} কে লঘিষ্ঠ আকারে সাধারণ ভগ্নাংশে প্রকাশ করলে কোনটি হবে?", fr(x), W(fr(x), [fr(x * 2), fr(x / 2), fr(x + F(1, x.denominator)), f"{x.numerator}/{x.denominator * 10}"]), "", lv)
    else: b.add(f"{fr(x)} কে দশমিক ভগ্নাংশে প্রকাশ করলে কোনটি হবে?", D(x), W(D(x), [D(x * 10), D(x / 10), D(x + F(1, 100)), D(F(x.numerator, 10))]), "", lv)
def f16_mul(b, lv):
    x, y = rd(1, 99, R.randint(1, 2)), rd(1, 99, R.randint(1, 2)); v = x * y
    b.add(f"{D(x)} × {D(y)} = কত?", D(v), W(D(v), [D(v * 10), D(v / 10), D(v * 100), D(x + y)]), "দশমিকের ঘর গুনে বসাও।", lv)
def f16_div(b, lv):
    y = rd(1, 99, R.randint(1, 2)); q = rd(1, 99, R.randint(0, 2)); x = y * q
    b.add(f"{D(x)} ÷ {D(y)} = কত?", D(q), W(D(q), [D(q * 10), D(q / 10), D(q * 100), D(q + 1)]), "ভাজককে পূর্ণসংখ্যা বানিয়ে ভাগ।", lv)
def f16_hl(b, lv):
    g = rd(1, 9, R.randint(1, 2)); a, c = R.sample(range(2, 12), 2)
    if math.gcd(a, c) != 1: return
    x, y = g * a, g * c; isl = R.random() < .5; v = g * a * c if isl else g
    b.add(f"{D(x)} ও {D(y)} এর {'ল.সা.গু.' if isl else 'গ.সা.গু.'} কত?", D(v), W(D(v), [D(g if isl else g * a * c), D(v * 10), D(v / 10), D(x * y)]), "দশমিকের ঘর সমান করে পূর্ণসংখ্যার মতো নির্ণয়।", lv)
def f16_word(b, lv):
    p = rd(105, 999, 1); k = rd(5, 95, 1)
    v = p * k
    if v.denominator > 100: return
    b.add(f"1 কেজি চালের দাম {D(p)} টাকা হলে {D(k)} কেজি চালের দাম কত টাকা?", f"{D(v)} টাকা", W(f"{D(v)} টাকা", [f"{D(v * 10)} টাকা", f"{D(v / 10)} টাকা", f"{D(p + k)} টাকা", f"{D(v + 1)} টাকা"]), "দাম × পরিমাণ।", lv)
def f16_rope(b, lv):
    L = rd(100, 999, 1); n = R.randint(2, 4); ps = [rd(5, 99, 2) for _ in range(n)]
    v = L - sum(ps)
    if v <= 0: return
    b.add(f"{D(L)} মিটার লম্বা একটি দড়ি থেকে {', '.join(D(x) for x in ps)} মিটার করে {n}টি টুকরা কেটে নেওয়া হলো। বাকি দড়ির দৈর্ঘ্য কত মিটার?", D(v), W(D(v), [D(sum(ps)), D(v + 1), D(v - F(1, 10)), D(v * 10)]), "", lv)
P16 = part('1.6', 100, fx16, [f16_add, f16_10, f16_fr], [f16_mul, f16_div, f16_hl], [f16_word, f16_rope])
save('m1', P11 + P12 + P13 + P14 + P15 + P16)

# ===================================================== 2.1 অনুপাত
fx21 = [
 ("অনুপাতের কোনো একক থাকে কি?", "না, অনুপাত এককবিহীন", ["হ্যাঁ, মিটার", "হ্যাঁ, টাকা", "হ্যাঁ, পূর্ববর্তী রাশির একক"], "", E),
 ("অনুপাতের প্রথম রাশিকে কী বলে?", "পূর্ব রাশি", ["উত্তর রাশি", "মধ্য রাশি", "সমানুপাতী"], "", E),
 ("অনুপাতের দ্বিতীয় রাশিকে কী বলে?", "উত্তর রাশি", ["পূর্ব রাশি", "লব", "সহগ"], "", E),
]
def g21_low(b, lv):
    a, c = R.randint(1, 15), R.randint(1, 15)
    if math.gcd(a, c) != 1 or a == c: return
    k = R.randint(2, 12)
    b.add(f"{a * k} : {c * k} এর লঘিষ্ঠ রূপ কোনটি?", f"{a} : {c}", W(f"{a} : {c}", [f"{c} : {a}", f"{a * 2} : {c * 2}" if k % 2 else f"{a + 1} : {c}", f"{a} : {c + 1}", f"{a * k} : {c}"]), "উভয় পদকে গ.সা.গু. দিয়ে ভাগ।", lv)
def g21_unit(b, lv):
    t = R.randrange(3)
    if t == 0: x, y = R.randint(1, 9), R.randint(5, 95); u = (f"{x} টাকা ও {y} পয়সা", 100 * x, y)
    elif t == 1: x, y = R.randint(1, 9), R.randint(5, 95); u = (f"{x} মিটার ও {y} সেন্টিমিটার", 100 * x, y)
    else: x, y = R.randint(1, 5), R.randint(5, 55); u = (f"{x} ঘণ্টা ও {y} মিনিট", 60 * x, y)
    s, a, c = u; g = math.gcd(a, c)
    ans = f"{a // g} : {c // g}"
    b.add(f"{s} এর অনুপাত কত?", ans, W(ans, [f"{x} : {y}", f"{c // g} : {a // g}", f"{a // g} : {c // g + 1}", f"{x * 10} : {y}"]), "একই এককে এনে অনুপাত।", lv)
def g21_div(b, lv):
    p, q = R.randint(1, 9), R.randint(1, 9)
    if math.gcd(p, q) != 1 or p == q: return
    N = (p + q) * R.randint(5, 100)
    v = N * p // (p + q)
    b.add(f"{N} টাকা {p} : {q} অনুপাতে ভাগ করলে প্রথম অংশ কত টাকা?", f"{v} টাকা", W(f"{v} টাকা", [f"{N - v} টাকা", f"{N // p if N % p == 0 else v + p} টাকা", f"{v + (p + q)} টাকা", f"{N // 2} টাকা" if N // 2 != v else f"{v - 1} টাকা"]), "মোট × প্রথম পদ ÷ পদের যোগফল।", lv)
def g21_inv(b, lv):
    a, c = R.randint(1, 15), R.randint(1, 15)
    if math.gcd(a, c) != 1 or a == c: return
    b.add(f"{a} : {c} এর ব্যস্ত অনুপাত কোনটি?", f"{c} : {a}", W(f"{c} : {a}", [f"{a} : {c}", f"{a * a} : {c * c}", f"{a + c} : {c}", f"1 : {a * c}"]), "পদ দুটি স্থান বদল।", lv)
def g21_comp(b, lv):
    a, c, d, e = [R.randint(1, 9) for _ in range(4)]
    x, y = a * d, c * e; g = math.gcd(x, y); ans = f"{x // g} : {y // g}"
    b.add(f"{a} : {c} ও {d} : {e} এর মিশ্র অনুপাত কোনটি?", ans, W(ans, [f"{a + d} : {c + e}", f"{y // g} : {x // g}", f"{a * e} : {c * d}", f"{x // g + 1} : {y // g}"]), "পূর্ব রাশিগুলোর গুণফল : উত্তর রাশিগুলোর গুণফল।", lv)
def g21_x(b, lv):
    a, c = R.randint(1, 12), R.randint(1, 12); k = R.randint(2, 12)
    if a == c: return
    b.add(f"{a} : {c} = {a * k} : x হলে x এর মান কত?", c * k, W(c * k, [a * k, c + k, c * k + c, a * c]), "", lv)
def g21_abc(b, lv):
    p, q, r, s = [R.randint(1, 9) for _ in range(4)]
    A, B, C = p * r, q * r, q * s; g = math.gcd(math.gcd(A, B), C)
    ans = f"{A // g} : {B // g} : {C // g}"
    b.add(f"A : B = {p} : {q} এবং B : C = {r} : {s} হলে A : B : C কত?", ans, W(ans, [f"{p} : {q * r} : {s}", f"{p} : {q} : {s}", f"{A // g} : {C // g} : {B // g}" if B != C else f"{A // g + 1} : {B // g} : {C // g}", f"{p * s} : {q * r} : {q * s}"]), "B এর মান সমান করে নাও।", lv)
def g21_age(b, lv):
    p, q = R.randint(1, 6), R.randint(2, 9); n = R.randint(2, 15)
    if p >= q or math.gcd(p, q) != 1: return
    k = R.randint(2, 8); a1, a2 = p * k, q * k
    r1, r2 = a1 + n, a2 + n; g = math.gcd(r1, r2)
    b.add(f"দুই ভাইয়ের বর্তমান বয়সের অনুপাত {p} : {q}। {n} বছর পর তাদের বয়সের অনুপাত হবে {r1 // g} : {r2 // g}। বড় ভাইয়ের বর্তমান বয়স কত বছর?", a2, W(a2, [a1, a2 + n, r2 // g, a2 - p]), "বয়স pk ও qk ধরে সমীকরণ।", lv)
def g21_three(b, lv):
    p, q, r = R.sample(range(1, 10), 3); N = (p + q + r) * R.randint(10, 80)
    who = R.randrange(3); v = N * [p, q, r][who] // (p + q + r)
    b.add(f"{N} টাকা তিনজনের মধ্যে {p} : {q} : {r} অনুপাতে ভাগ করলে {['প্রথম', 'দ্বিতীয়', 'তৃতীয়'][who]} জন কত টাকা পাবে?", f"{v} টাকা", W(f"{v} টাকা", [f"{N * x // (p + q + r)} টাকা" for x in (p, q, r)] + [f"{N // 3} টাকা", f"{v + p + q + r} টাকা"]), "", lv)
P21 = part('2.1', 100, fx21, [g21_low, g21_unit, g21_inv, g21_x], [g21_div, g21_comp, g21_x, g21_unit], [g21_abc, g21_age, g21_three])

# ===================================================== 2.2 অনুপাত ও শতকরা
fx22 = [
 ("শতকরা কথাটির অর্থ কী?", "প্রতি একশতে", ["প্রতি দশে", "প্রতি হাজারে", "প্রতি একে"], "", E),
 ("শতকরা কোন হরবিশিষ্ট ভগ্নাংশ?", "100", ["10", "1000", "1"], "", E),
]
def h22_pf(b, lv):
    p = R.choice([x for x in range(1, 100) if 100 % math.gcd(x, 100) == 0 and x % 5 == 0 or x in (12, 15, 24, 36, 48, 64, 75, 4, 8, 16, 28, 32)])
    v = F(p, 100)
    b.add(f"{p}% কে লঘিষ্ঠ আকারে সাধারণ ভগ্নাংশে লিখলে কোনটি হবে?", fr(v), W(fr(v), [f"{p}/10", fr(F(p, 1000)), fr(v * 2), fr(v + F(1, v.denominator))]), "শতকরা ÷ 100।", lv)
def h22_fp(b, lv):
    x = F(R.randint(1, 19), R.choice([2, 4, 5, 10, 20, 25, 50]))
    if x >= 1 or x.denominator == 1: return
    v = x * 100
    b.add(f"{fr(x)} কে শতকরায় প্রকাশ করলে কত?", f"{D(v)}%", W(f"{D(v)}%", [f"{D(v / 10)}%", f"{D(v * 10)}%", f"{x.numerator}%", f"{D(v + 5)}%"]), "ভগ্নাংশ × 100%।", lv)
def h22_of(b, lv):
    p = R.choice([5, 10, 12, 15, 20, 25, 30, 40, 50, 60, 75, 8, 4, 35, 45]); N = R.randint(2, 99) * 20
    v = F(p * N, 100)
    if v.denominator != 1: return
    b.add(f"{N} এর {p}% কত?", int(v), W(int(v), [int(v) * 10, N - int(v), int(v) + p, N // p if N % p == 0 and N // p != v else int(v) + 1]), "", lv)
def h22_ratio(b, lv):
    a, c = R.randint(1, 9), R.randint(1, 9)
    v = F(100 * a, c)
    if v.denominator not in (1, 2, 4, 5): return
    b.add(f"{a} : {c} অনুপাতকে শতকরায় প্রকাশ করলে কত?", f"{D(v)}%", W(f"{D(v)}%", [f"{D(F(100 * c, a))}%", f"{D(F(100 * a, a + c))}%", f"{a * 10}%", f"{D(v + 10)}%"]), "পূর্ব রাশি ÷ উত্তর রাশি × 100%।", lv)
def h22_what(b, lv):
    p = R.choice([5, 10, 15, 20, 25, 30, 40, 50, 60, 75, 80, 12, 35]); N = R.randint(2, 50) * 20
    a = p * N // 100
    if a * 100 != p * N: return
    b.add(f"{N} এর কত শতাংশ {a}?", f"{p}%", W(f"{p}%", [f"{p + 5}%", f"{p * 2}%", f"{100 - p}%", f"{a}%"]), f"{a} ÷ {N} × 100%।", lv)
def h22_inc(b, lv):
    p = R.choice([5, 10, 15, 20, 25, 30, 40, 50]); N = R.randint(2, 60) * 20; up = R.random() < .5
    v = N * (100 + (p if up else -p)) // 100
    b.add(f"{N} কে {p}% {'বৃদ্ধি' if up else 'হ্রাস'} করলে কত হবে?", v, W(v, [N * (100 - p if up else 100 + p) // 100, N * p // 100, v + p, N + p if up else N - p]), "", lv)
def h22_part(b, lv):
    a, c = R.randint(1, 9), R.randint(1, 9)
    v = F(100 * a, a + c)
    if v.denominator not in (1, 2, 4, 5) or a == c: return
    b.add(f"একটি শ্রেণিতে ছাত্র ও ছাত্রীর অনুপাত {a} : {c}। মোট শিক্ষার্থীর কত শতাংশ ছাত্র?", f"{D(v)}%", W(f"{D(v)}%", [f"{D(100 - v)}%", f"{D(F(100 * a, c))}%", f"{a * 10}%", f"{D(v + 5)}%"]), "ছাত্র ÷ মোট × 100%।", lv)
def h22_orig(b, lv):
    p = R.choice([5, 10, 20, 25, 40, 50]); N = R.randint(2, 50) * 20; up = R.random() < .5
    V = N * (100 + (p if up else -p)) // 100
    b.add(f"কোনো সংখ্যা {p}% {'বৃদ্ধি' if up else 'হ্রাস'} পেয়ে {V} হলো। সংখ্যাটি কত?", N, W(N, [V * (100 - p if up else 100 + p) // 100, V - p if up else V + p, N + 10, N - 10]), f"সংখ্যা × {100 + p if up else 100 - p}/100 = {V}।", lv)
def h22_marks(b, lv):
    T = R.choice([50, 75, 80, 100, 150, 200]); p = R.choice([40, 50, 60, 70, 80, 90, 45, 65, 85])
    m = T * p // 100
    if m * 100 != T * p: return
    tot = R.choice([2, 3]) * T
    b.add(f"রাফি {T} নম্বরের পরীক্ষায় {m} নম্বর পেল। সে শতকরা কত নম্বর পেল?", f"{p}%", W(f"{p}%", [f"{m}%", f"{p + 5}%", f"{100 - p}%", f"{p - 10}%"]), "", lv)
P22 = part('2.2', 100, fx22, [h22_pf, h22_fp, h22_of, h22_ratio], [h22_what, h22_inc, h22_part, h22_marks], [h22_orig, h22_part])

# ===================================================== 2.3 ঐকিক নিয়ম
fx23 = [
 ("ঐকিক নিয়মে প্রথমে কোনটি নির্ণয় করা হয়?", "এককের মান", ["মোট মান", "শতকরা মান", "অনুপাত"], "", E),
 ("লোকসংখ্যা বাড়লে একটি কাজ শেষ করতে প্রয়োজনীয় সময় কী হয়?", "কমে", ["বাড়ে", "একই থাকে", "দ্বিগুণ হয়"], "", E),
]
ITEMS = [('কলম', 'টি'), ('খাতা', 'টি'), ('ডিম', 'টি'), ('কমলা', 'টি'), ('বই', 'টি'), ('পেনসিল', 'টি')]
def u23_cost(b, lv):
    it, s = R.choice(ITEMS); u = R.randint(3, 60); n, m = R.sample(range(2, 30), 2)
    b.add(f"{n}{s} {it}ের দাম {u * n} টাকা হলে {m}{s} {it}ের দাম কত টাকা?", f"{u * m} টাকা", W(f"{u * m} টাকা", [f"{u * n * m} টাকা", f"{u * (m + 1)} টাকা", f"{u * m + n} টাকা", f"{u} টাকা"]), f"1{s}র দাম {u} টাকা।", lv)
def u23_kg(b, lv):
    u = R.randint(20, 150); n, m = R.sample(range(2, 25), 2)
    b.add(f"{n} কেজি চিনির দাম {u * n} টাকা হলে {u * m} টাকায় কত কেজি চিনি পাওয়া যাবে?", f"{m} কেজি", W(f"{m} কেজি", [f"{m + 1} কেজি", f"{n} কেজি", f"{m * 2} কেজি", f"{max(1, m - 1)} কেজি"]), "", lv)
def u23_work(b, lv):
    n = R.randint(2, 30); d = R.randint(2, 40); W0 = n * d
    m = R.choice([x for x in range(2, 60) if W0 % x == 0 and x != n] or [n * 2])
    b.add(f"{n} জন লোক একটি কাজ {d} দিনে করতে পারে। {m} জন লোক কাজটি কত দিনে করতে পারবে?", f"{W0 // m} দিনে", W(f"{W0 // m} দিনে", [f"{d * m // n if d * m % n == 0 else d + 1} দিনে", f"{W0} দিনে", f"{W0 // m + 1} দিনে", f"{d} দিনে"]), "লোক বাড়লে দিন কমে (ব্যস্ত সম্পর্ক)।", lv)
def u23_car(b, lv):
    k = R.randint(8, 20); l, m = R.sample(range(2, 40), 2)
    b.add(f"একটি গাড়ি {l} লিটার তেলে {k * l} কিমি যায়। {k * m} কিমি যেতে কত লিটার তেল লাগবে?", f"{m} লিটার", W(f"{m} লিটার", [f"{l} লিটার", f"{m + 2} লিটার", f"{k} লিটার", f"{m * 2} লিটার"]), "", lv)
def u23_food(b, lv):
    n = R.randint(10, 80); d = R.randint(10, 60); k = R.randint(2, d - 2); x = R.randint(2, 40)
    rem = n * (d - k)
    if rem % (n + x): return
    v = rem // (n + x)
    b.add(f"একটি হোস্টেলে {n} জনের {d} দিনের খাবার আছে। {k} দিন পর আরও {x} জন যোগ দিল। বাকি খাবারে আর কত দিন চলবে?", f"{v} দিন", W(f"{v} দিন", [f"{d - k} দিন", f"{n * d // (n + x)} দিন" if n * d % (n + x) == 0 and n * d // (n + x) != v else f"{v + 2} দিন", f"{v + 1} দিন", f"{max(1, v - 1)} দিন"]), "বাকি খাবার = লোক × বাকি দিন।", lv)
def u23_hours(b, lv):
    n, d, h = R.randint(4, 20), R.randint(4, 20), R.randint(4, 10)
    W0 = n * d * h; m, h2 = R.randint(2, 30), R.randint(4, 10)
    if W0 % (m * h2) or (m, h2) == (n, h): return
    v = W0 // (m * h2)
    b.add(f"{n} জন লোক দৈনিক {h} ঘণ্টা কাজ করে একটি কাজ {d} দিনে শেষ করে। {m} জন লোক দৈনিক {h2} ঘণ্টা কাজ করে কাজটি কত দিনে শেষ করবে?", f"{v} দিনে", W(f"{v} দিনে", [f"{d} দিনে", f"{v + 1} দিনে", f"{W0 // m} দিনে", f"{max(1, v - 2)} দিনে"]), "মোট কাজ = লোক × দিন × ঘণ্টা।", lv)
P23 = part('2.3', 100, fx23, [u23_cost, u23_kg, u23_car], [u23_work, u23_cost, u23_kg, u23_car], [u23_food, u23_hours, u23_work])
save('m2', P21 + P22 + P23)

# ===================================================== 3.1 পূর্ণসংখ্যা ও ক্রম
fx31 = [
 ("0 কোন ধরনের পূর্ণসংখ্যা?", "ধনাত্মকও নয়, ঋণাত্মকও নয়", ["ধনাত্মক", "ঋণাত্মক", "ভগ্নাংশ"], "", E),
 ("সংখ্যারেখায় 0 এর বাম দিকের সংখ্যাগুলো কেমন?", "ঋণাত্মক", ["ধনাত্মক", "শূন্য", "ভগ্নাংশ মাত্র"], "", E),
 ("বৃহত্তম ঋণাত্মক পূর্ণসংখ্যা কোনটি?", "−1", ["0", "1", "−100"], "", M),
 ("ক্ষুদ্রতম ধনাত্মক পূর্ণসংখ্যা কোনটি?", "1", ["0", "−1", "2"], "", E),
]
def i31_big(b, lv):
    xs = R.sample(range(-60, 60), 4); big = R.random() < .5; c = max(xs) if big else min(xs)
    b.add(f"{', '.join(num(x) for x in xs)} এর মধ্যে {'বৃহত্তম' if big else 'ক্ষুদ্রতম'} পূর্ণসংখ্যা কোনটি?", num(c), W(num(c), [num(x) for x in xs]), "সংখ্যারেখায় ডানের সংখ্যা বড়।", lv)
def i31_opp(b, lv):
    a = nz(-200, 200)
    b.add(f"{num(a)} এর বিপরীত সংখ্যা কোনটি?", num(-a), W(num(-a), [num(a), "0", num(-a + 1), num(a * 2)]), "যোগফল শূন্য হয়।", lv)
def i31_side(b, lv):
    a, c = R.sample(range(-50, 50), 2)
    ans = "ডান দিকে" if a > c else "বাম দিকে"
    b.add(f"সংখ্যারেখায় {num(a)} সংখ্যাটি {num(c)} এর কোন দিকে অবস্থিত?", ans, W(ans, ["বাম দিকে" if a > c else "ডান দিকে", "একই বিন্দুতে", "উপরের দিকে"]), "", lv)
def i31_temp(b, lv):
    t = R.randint(1, 30); c = R.random() < .5
    b.add(f"শূন্যের {t}° {'নিচের' if c else 'উপরের'} তাপমাত্রাকে পূর্ণসংখ্যায় কীভাবে লেখা হয়?", f"{num(-t if c else t)}°", W(f"{num(-t if c else t)}°", [f"{num(t if c else -t)}°", f"{num(-t - 1)}°", f"{num(t + 1)}°", "0°"]), "", lv)
def i31_ord(b, lv):
    xs = R.sample(range(-30, 30), 4); s = sorted(xs); c = ', '.join(num(x) for x in s)
    w = [', '.join(num(x) for x in sorted(xs, key=abs)), ', '.join(num(x) for x in sorted(xs, reverse=True)), ', '.join(num(x) for x in s[1:] + s[:1]), ', '.join(num(x) for x in sorted(xs, key=lambda v: -abs(v)))]
    b.add(f"{', '.join(num(x) for x in xs)} সংখ্যাগুলোকে ছোট থেকে বড় ক্রমে সাজালে কোনটি হবে?", c, W(c, w), "", lv)
def i31_cnt(b, lv):
    a = R.randint(-40, 0); c = R.randint(1, 40)
    v = c - a - 1
    b.add(f"{num(a)} ও {num(c)} এর মধ্যে কয়টি পূর্ণসংখ্যা আছে?", v, W(v, [v + 1, v + 2, c + a, v - 1]), "দুই প্রান্ত বাদ দিয়ে গুনো।", lv)
def i31_dist(b, lv):
    a = R.randint(-50, 10); c = R.randint(a + 1, 50)
    v = c - a
    b.add(f"সংখ্যারেখায় {num(a)} ও {num(c)} এর মধ্যবর্তী দূরত্ব কত একক?", v, W(v, [abs(c + a) if abs(c + a) != v else v + 2, v + 1, v - 1, c]), "বড় − ছোট।", lv)
def i31_sum(b, lv):
    a = R.randint(-20, -1); c = R.randint(1, 25)
    v = sum(range(a + 1, c))
    b.add(f"{num(a)} ও {num(c)} এর মধ্যবর্তী সকল পূর্ণসংখ্যার যোগফল কত?", num(v), W(num(v), [num(v + a), num(v + c), num(-v) if v else '1', num(v + 1)]), "বিপরীত সংখ্যাগুলো কেটে যায়।", lv)
P31 = part('3.1', 100, fx31, [i31_big, i31_opp, i31_side, i31_temp], [i31_ord, i31_cnt, i31_big], [i31_dist, i31_sum])

# ===================================================== 3.2 পূর্ণসংখ্যার যোগ
fx32 = [
 ("দুটি ঋণাত্মক পূর্ণসংখ্যার যোগফল সর্বদা কেমন?", "ঋণাত্মক", ["ধনাত্মক", "শূন্য", "ধনাত্মক বা শূন্য"], "", E),
 ("কোনো পূর্ণসংখ্যা ও তার বিপরীত সংখ্যার যোগফল কত?", "0", ["1", "সংখ্যাটির দ্বিগুণ", "−1"], "", E),
]
def j32_add(b, lv):
    a, c = nz(-99, 99), nz(-99, 99)
    if a > 0 and c > 0: c = -c
    v = a + c
    b.add(f"({num(a)}) + ({num(c)}) = কত?", num(v), W(num(v), [num(a - c), num(-v) if v else '1', num(abs(a) + abs(c)), num(v + 1)]), "চিহ্ন বিবেচনা করে যোগ।", lv)
def j32_three(b, lv):
    xs = [nz(-60, 60) for _ in range(R.randint(3, 4))]; v = sum(xs)
    b.add(f"{' + '.join(f'({num(x)})' for x in xs)} = কত?", num(v), W(num(v), [num(sum(abs(x) for x in xs)), num(-v) if v else '2', num(v + 2), num(v - xs[0] * 2)]), "", lv)
def j32_temp(b, lv):
    t = R.randint(-20, 10); r = R.randint(2, 30)
    v = t + r
    b.add(f"সকালের তাপমাত্রা {num(t)}° সেলসিয়াস ছিল। দুপুরে {r}° বাড়লে তাপমাত্রা কত হলো?", f"{num(v)}°", W(f"{num(v)}°", [f"{num(t - r)}°", f"{num(-v) if v else '1'}°", f"{num(r)}°", f"{num(v + 1)}°"]), "", lv)
def j32_lift(b, lv):
    f = R.randint(-4, 3); u = R.randint(2, 12)
    v = f + u
    lab = lambda x: f"ভূগর্ভস্থ {abs(x)} তলা" if x < 0 else ("নিচতলা (0)" if x == 0 else f"{x} তলা")
    b.add(f"একটি লিফট {lab(f)} থেকে {u} তলা উপরে উঠল। লিফটটি এখন কোথায়?", lab(v), W(lab(v), [lab(f - u), lab(v + 1), lab(u), lab(v - 1)]), "উপরে = ধনাত্মক, নিচে = ঋণাত্মক।", lv)
def j32_x(b, lv):
    a, c = nz(-50, 50), nz(-50, 50); v = c - a
    b.add(f"x + ({num(a)}) = {num(c)} হলে x = কত?", num(v), W(num(v), [num(c + a), num(a - c), num(v + 1), num(-c)]), "", lv)
def j32_range(b, lv):
    m, n = R.randint(1, 30), R.randint(1, 40)
    v = sum(range(-m, n + 1))
    b.add(f"{num(-m)} থেকে {n} পর্যন্ত সকল পূর্ণসংখ্যার যোগফল কত?", num(v), W(num(v), [num(-v) if v else '1', num(v + m), num(n * (n + 1) // 2), num(v - n)]), "বিপরীত জোড়াগুলো কেটে যায়।", lv)
P32 = part('3.2', 100, fx32, [j32_add, j32_temp, j32_lift], [j32_three, j32_temp, j32_lift, j32_add], [j32_x, j32_range])

# ===================================================== 3.3 পূর্ণসংখ্যার বিয়োগ
fx33 = [
 ("কোনো পূর্ণসংখ্যা বিয়োগ করা মানে কী যোগ করা?", "এর বিপরীত সংখ্যা", ["সংখ্যাটি নিজেই", "শূন্য", "1"], "", E),
 ("a − (−b) = ?", "a + b", ["a − b", "−a − b", "−a + b"], "", M),
]
def k33_sub(b, lv):
    a, c = nz(-99, 99), nz(-99, 99); v = a - c
    b.add(f"({num(a)}) − ({num(c)}) = কত?", num(v), W(num(v), [num(a + c), num(c - a), num(v + 1), num(abs(a) - abs(c))]), "বিয়োজ্যের বিপরীত সংখ্যা যোগ।", lv)
def k33_mix(b, lv):
    a, c, d = nz(-50, 50), nz(-50, 50), nz(-50, 50)
    if R.random() < .5: v = a - (c - d); s = f"({num(a)}) − [({num(c)}) − ({num(d)})]"; w = a - c - d
    else: v = a - c + d; s = f"({num(a)}) − ({num(c)}) + ({num(d)})"; w = a - c - d
    b.add(f"{s} = কত?", num(v), W(num(v), [num(w), num(a + c + d), num(-v) if v else '3', num(v + 2)]), "", lv)
def k33_temp(b, lv):
    a = R.randint(-30, 40); c = R.randint(-30, 40)
    if a == c: return
    v = abs(a - c)
    b.add(f"একটি শহরের দিনের তাপমাত্রা {num(max(a, c))}° এবং রাতের তাপমাত্রা {num(min(a, c))}°। তাপমাত্রার পার্থক্য কত ডিগ্রি?", f"{v}°", W(f"{v}°", [f"{abs(a + c)}°" if abs(a + c) != v else f"{v + 2}°", f"{v + 1}°", f"{max(a, c)}°", f"{max(1, v - 1)}°"]), "বড় − ছোট।", lv)
def k33_sea(b, lv):
    h = R.randint(100, 9000); d = R.randint(20, 900)
    v = h + d
    b.add(f"একটি বিমান সমুদ্রপৃষ্ঠ থেকে {h} মিটার উপরে এবং একটি ডুবোজাহাজ {d} মিটার নিচে আছে। তাদের উচ্চতার পার্থক্য কত মিটার?", f"{v} মিটার", W(f"{v} মিটার", [f"{h - d} মিটার", f"{v + 100} মিটার", f"{h} মিটার", f"{d} মিটার"]), f"{h} − (−{d}) = {v}।", lv)
def k33_find(b, lv):
    a, c = nz(-60, 60), nz(-60, 60); v = c + a
    b.add(f"কোন সংখ্যা থেকে {num(a)} বিয়োগ করলে {num(c)} হয়?", num(v), W(num(v), [num(c - a), num(a - c), num(v + 1), num(-v) if v else '2']), "", lv)
def k33_bank(b, lv):
    bal = R.randint(-500, 2000); out_ = R.randint(100, 2500)
    v = bal - out_
    b.add(f"একটি হিসাবে {num(bal)} টাকা ছিল (ঋণাত্মক মানে ধার)। সেখান থেকে {out_} টাকা তোলা হলে হিসাবে কত টাকা থাকল?", f"{num(v)} টাকা", W(f"{num(v)} টাকা", [f"{num(bal + out_)} টাকা", f"{num(-v) if v else 1} টাকা", f"{num(v + 100)} টাকা", f"{out_} টাকা"]), "", lv)
P33 = part('3.3', 100, fx33, [k33_sub, k33_temp], [k33_mix, k33_sea, k33_sub, k33_temp], [k33_find, k33_bank, k33_mix])
save('m3', P31 + P32 + P33)

# ===================================================== 4.1 প্রতীক, চলক, সহগ ও পদ
fx41 = [
 ("বীজগণিতে অজানা রাশি প্রকাশে যে অক্ষর ব্যবহার করা হয় তাকে কী বলে?", "চলক", ["ধ্রুবক", "সহগ", "সূচক"], "", E),
 ("যে রাশির মান নির্দিষ্ট, তাকে কী বলে?", "ধ্রুবক", ["চলক", "পদ", "রাশি"], "", E),
 ("বীজগণিতীয় রাশির যেসব অংশ + বা − চিহ্ন দ্বারা যুক্ত থাকে, তাদের কী বলে?", "পদ", ["সহগ", "সূচক", "চলক"], "", E),
]
def l41_coef(b, lv):
    c = nz(-15, 15); vs = R.choice(['x', 'y', 'a', 'xy', 'x²', 'a²b', 'xy²', 'ab'])
    t = f"{'' if c == 1 else ('−' if c == -1 else num(c))}{vs}"
    b.add(f"{t} পদের সাংখ্যিক সহগ কত?", num(c), W(num(c), [num(-c), vs, num(c + 1), "0"]), "", lv)
def l41_terms(b, lv):
    n = R.randint(2, 6); vs = ['x', 'y', 'a', 'b', 'x²', 'xy', 'z', 'ab']
    ts = [f"{R.randint(2, 9)}{v}" for v in R.sample(vs, n - 1)] + [str(R.randint(1, 20))]
    R.shuffle(ts); s = ts[0] + ''.join(R.choice([' + ', ' − ']) + t for t in ts[1:])
    b.add(f"{s} রাশিটিতে কয়টি পদ আছে?", n, W(n, [n + 1, n - 1, n + 2, 2 * n]), "", lv)
def l41_val(b, lv):
    a, c, x = nz(-9, 9), R.randint(-20, 20), nz(-6, 6)
    v = a * x + c
    b.add(f"x = {num(x)} হলে {pfmt({(1,): a, (0,): c} if c else {(1,): a}, ('x',))} এর মান কত?", num(v), W(num(v), [num(a + x + c), num(-v) if v else '1', num(a * x - c), num(v + a)]), "", lv)
def l41_word(b, lv):
    a, c = R.randint(2, 9), R.randint(1, 20); t = R.randrange(4)
    if t == 0: q, ans, w = f"x এর {a} গুণের সাথে {c} যোগ", f"{a}x + {c}", [f"{a}(x + {c})", f"x + {a * c}", f"{a}x − {c}", f"{c}x + {a}"]
    elif t == 1: q, ans, w = f"x থেকে {c} কম সংখ্যার {a} গুণ", f"{a}(x − {c})", [f"{a}x − {c}", f"{c} − {a}x", f"{a}(x + {c})", f"{c}(x − {a})"]
    elif t == 2: q, ans, w = f"x ও y এর যোগফলের {a} গুণ থেকে {c} বিয়োগ", f"{a}(x + y) − {c}", [f"{a}x + y − {c}", f"{c} − {a}(x + y)", f"{a}(x + y − {c})", f"{a}(x − y) − {c}"]
    else: q, ans, w = f"x এর বর্গের সাথে y এর {a} গুণ যোগ", f"x² + {a}y", [f"(x + {a}y)²", f"2x + {a}y", f"x² + y^{a}" if False else f"{a}x² + y", f"x² − {a}y"]
    b.add(f"'{q}' — বীজগণিতীয় রাশিতে কোনটি?", ans, W(ans, w), "", lv)
def l41_val2(b, lv):
    a, c, d = nz(-6, 6), nz(-6, 6), R.randint(-10, 10); x, y = nz(-5, 5), nz(-5, 5)
    v = a * x + c * y + d
    e = pfmt({(1, 0): a, (0, 1): c, (0, 0): d} if d else {(1, 0): a, (0, 1): c})
    b.add(f"x = {num(x)}, y = {num(y)} হলে {e} এর মান কত?", num(v), W(num(v), [num(a * y + c * x + d), num(-v) if v else '2', num(v + 2), num(a * x - c * y + d)]), "", lv)
def l41_sq(b, lv):
    a, c = nz(-4, 4), R.randint(-10, 10); x = nz(-5, 5)
    v = x * x + a * x + c
    e = pfmt({(2,): 1, (1,): a, (0,): c} if c else {(2,): 1, (1,): a}, ('x',))
    b.add(f"x = {num(x)} হলে {e} এর মান কত?", num(v), W(num(v), [num(2 * x + a * x + c), num(-x * x + a * x + c), num(v + 2 * a), num(v + 1)]), "", lv)
def l41_peri(b, lv):
    a, c = R.randint(2, 9), R.randint(1, 15)
    ans = f"{2 * a + 2}x + {2 * c}"
    b.add(f"একটি আয়তক্ষেত্রের দৈর্ঘ্য ({a}x + {c}) সেমি ও প্রস্থ x সেমি। পরিসীমা কত সেমি?", ans, W(ans, [f"{a + 1}x + {c}", f"{2 * a}x + {2 * c}", pfmt({(2,): a, (1,): c}, ("x",)), f"{2 * a + 1}x + {2 * c}"]), "2(দৈর্ঘ্য + প্রস্থ)।", lv)
P41 = part('4.1', 100, fx41, [l41_coef, l41_terms, l41_val], [l41_word, l41_val2, l41_val], [l41_sq, l41_peri])

# ===================================================== 4.2 সূচক
fx42 = [
 ("aⁿ রাশিতে a কে কী বলে?", "ভিত্তি", ["সূচক", "সহগ", "ঘাত"], "", E),
 ("aⁿ রাশিতে n কে কী বলে?", "সূচক বা ঘাত", ["ভিত্তি", "সহগ", "পদ"], "", E),
 ("a⁰ (a ≠ 0) এর মান কত?", "1", ["0", "a", "অসংজ্ঞায়িত"], "", M),
]
def m42_form(b, lv):
    a = R.choice(['2', '3', '5', '7', 'a', 'x', 'y', 'm']); n = R.randint(3, 8)
    s = ' × '.join([a] * n)
    b.add(f"{s} কে সূচকের সাহায্যে লিখলে কোনটি হবে?", f"{a}{sup(n)}", W(f"{a}{sup(n)}", [f"{n}{a}", f"{a}{sup(n - 1)}", f"{a}{sup(2 * n)}" if not a.isdigit() else f"{n}{sup(int(a))}", f"{a}{sup(n + 1)}"]), "", lv)
def m42_val(b, lv):
    a = R.randint(2, 9); n = R.randint(2, 5 if a < 5 else 3)
    v = a ** n
    b.add(f"{a}{sup(n)} এর মান কত?", v, W(v, [a * n, n ** a if n ** a != v else v + 1, a ** (n - 1), a ** (n + 1)]), "", lv)
def m42_base(b, lv):
    a = R.randint(2, 15); n = R.randint(2, 9); ask = R.random() < .5
    c = a if ask else n
    b.add(f"{a}{sup(n)} এ {'ভিত্তি' if ask else 'সূচক'} কত?", c, W(c, [n if ask else a, a * n, a ** 2 if a ** 2 != c else a + n, c + 1]), "", lv)
def m42_mul(b, lv):
    v = R.choice('xyabmp'); m, n = R.randint(2, 9), R.randint(2, 9); div = R.random() < .45
    if div and m <= n: m, n = n + 1, m
    r = m - n if div else m + n
    ans = f"{v}{sup(r)}" if r != 1 else v
    b.add(f"{v}{sup(m)} {'÷' if div else '×'} {v}{sup(n)} = কত?", ans, W(ans, [f"{v}{sup(m * n)}", (f"{v}{sup(m + n)}" if div else (f"{v}{sup(abs(m - n))}" if abs(m - n) > 1 else f"{v}{sup(m * n + 1)}")), f"{v}{sup(r + 1)}", f"{r}{v}"]), f"একই ভিত্তির ক্ষেত্রে সূচক {'বিয়োগ' if div else 'যোগ'} হয়।", lv)
def m42_num(b, lv):
    a = R.choice([2, 3, 5, 10]); m, n = R.randint(2, 4), R.randint(2, 4)
    v = a ** (m + n)
    if v > 100000: return
    b.add(f"{a}{sup(m)} × {a}{sup(n)} এর মান কত?", v, W(v, [a ** (m * n), a * (m + n), v * a, (a * a) ** (m + n) if (a * a) ** (m + n) != v else v + 1]), "", lv)
def m42_expr(b, lv):
    a, c = R.randint(2, 5), R.randint(2, 5); m, n = R.randint(2, 4), R.randint(2, 4); s = R.random() < .5
    v = a ** m + c ** n if s else a ** m - c ** n
    b.add(f"{a}{sup(m)} {'+' if s else '−'} {c}{sup(n)} এর মান কত?", num(v), W(num(v), [num(a * m + c * n if s else a * m - c * n), num(a ** m - c ** n if s else a ** m + c ** n), num(v + 1), num((a + c) ** max(m, n)) if s else num(v - 2)]), "", lv)
def m42_cmp(b, lv):
    a, n = R.sample(range(2, 7), 2)
    x, y = a ** n, n ** a
    if x == y: return
    ans = f"{a}{sup(n)}" if x > y else f"{n}{sup(a)}"
    b.add(f"{a}{sup(n)} ও {n}{sup(a)} এর মধ্যে কোনটি বড়?", ans, W(ans, [f"{n}{sup(a)}" if x > y else f"{a}{sup(n)}", "দুটি সমান", "তুলনা করা যায় না"]), f"{a}{sup(n)} = {x}, {n}{sup(a)} = {y}।", lv)
def m42_combo(b, lv):
    a = R.choice([2, 3, 5]); m, n, k = R.randint(2, 6), R.randint(2, 5), R.randint(2, 6)
    e = m + n - k
    if e < 0 or a ** e > 10000: return
    v = a ** e
    b.add(f"({a}{sup(m)} × {a}{sup(n)}) ÷ {a}{sup(k)} এর মান কত?", v, W(v, [a ** (m * n - k) if 0 <= m * n - k < 12 and a ** (m * n - k) != v else v * a, a ** (e + 1), a * e, a ** max(0, e - 1) if e else 2]), "", lv)
P42 = part('4.2', 100, fx42, [m42_form, m42_val, m42_base], [m42_mul, m42_num, m42_val], [m42_expr, m42_cmp, m42_combo])

# ===================================================== 4.3 সদৃশ পদ, যোগ ও বিয়োগ
fx43 = [
 ("যে পদগুলোর চলক ও চলকের সূচক একই, তাদের কী বলে?", "সদৃশ পদ", ["বিসদৃশ পদ", "ধ্রুবক পদ", "সহগ"], "", E),
 ("সদৃশ পদ যোগ করার সময় কী যোগ করা হয়?", "সাংখ্যিক সহগ", ["চলক", "সূচক", "চলক ও সূচক উভয়ই"], "", E),
]
MONO = [((1, 0), 'x'), ((0, 1), 'y'), ((2, 0), 'x²'), ((1, 1), 'xy'), ((2, 1), 'x²y'), ((1, 2), 'xy²')]
def n43_like(b, lv):
    e, s = R.choice(MONO); c, k = nz(-9, 9), nz(-12, 12)
    others = [t for _, t in MONO if t != s]
    fm = lambda c, t: f"{'' if c == 1 else ('−' if c == -1 else num(c))}{t}"
    b.add(f"নিচের কোনটি {fm(c, s)} এর সদৃশ পদ?", fm(k, s), W(fm(k, s), [fm(k, t) for t in R.sample(others, 3)]), "চলক ও সূচক হুবহু এক।", lv)
def n43_add(b, lv):
    e, s = R.choice(MONO); cs = [nz(-12, 12) for _ in range(R.randint(2, 3))]; v = sum(cs)
    if v == 0: return
    expr = pfmt({e: cs[0]}) + ''.join((' + ' if c > 0 else ' − ') + pfmt({e: abs(c)}) for c in cs[1:])
    b.add(f"{expr} = কত?", pfmt({e: v}), W(pfmt({e: v}), [pfmt({e: -v}), pfmt({e: sum(abs(c) for c in cs)}) if sum(abs(c) for c in cs) != v else pfmt({e: v + 1}), pfmt({(e[0] * 2, e[1] * 2): v}), pfmt({e: v + 2})]), "সহগগুলো যোগ।", lv)
def n43_two(b, lv):
    p = {(1, 0): nz(-9, 9), (0, 1): nz(-9, 9), (0, 0): nz(-15, 15)}
    q = {(1, 0): nz(-9, 9), (0, 1): nz(-9, 9), (0, 0): nz(-15, 15)}
    sub = R.random() < .5
    r = {k: p[k] - q[k] if sub else p[k] + q[k] for k in p}; r = {k: c for k, c in r.items() if c}
    if not r: return
    wr = {k: p[k] + q[k] if sub else p[k] - q[k] for k in p}; wr = {k: c for k, c in wr.items() if c}
    w2 = {k: (p[k] - q[k] if k != (0, 0) else p[k] + q[k]) if sub else (p[k] + q[k] if k != (0, 1) else p[k] - q[k]) for k in p}; w2 = {k: c for k, c in w2.items() if c}
    w3 = dict(r); w3[(0, 0)] = w3.get((0, 0), 0) + 2
    b.add(f"({pfmt(p)}) {'−' if sub else '+'} ({pfmt(q)}) = কত?", pfmt(r), W(pfmt(r), [pfmt(wr), pfmt(w2), pfmt({k: c for k, c in w3.items() if c}), pfmt({k: -c for k, c in r.items()})]), "সদৃশ পদ একত্র করো।", lv)
def n43_need(b, lv):
    A = {(1, 0): nz(-9, 9), (0, 1): nz(-9, 9), (0, 0): nz(-12, 12)}
    B = {(1, 0): nz(-9, 9), (0, 1): nz(-9, 9), (0, 0): nz(-12, 12)}
    r = {k: B[k] - A[k] for k in A}; r = {k: c for k, c in r.items() if c}
    if not r: return
    w = {k: B[k] + A[k] for k in A}; w = {k: c for k, c in w.items() if c}
    b.add(f"{pfmt(A)} এর সাথে কত যোগ করলে যোগফল {pfmt(B)} হবে?", pfmt(r), W(pfmt(r), [pfmt(w), pfmt({k: -c for k, c in r.items()}), pfmt({k: c + (1 if k == (0, 0) else 0) for k, c in r.items()}), pfmt(B)]), "দ্বিতীয় রাশি − প্রথম রাশি।", lv)
def n43_sumsub(b, lv):
    P = {(1, 0): nz(-6, 6), (0, 1): nz(-6, 6)}; Q = {(1, 0): nz(-6, 6), (0, 1): nz(-6, 6)}; C = {(1, 0): nz(-6, 6), (0, 1): nz(-6, 6)}
    r = {k: P[k] + Q[k] - C[k] for k in P}; r = {k: c for k, c in r.items() if c}
    if not r: return
    w = {k: P[k] + Q[k] + C[k] for k in P}; w = {k: c for k, c in w.items() if c}
    b.add(f"({pfmt(P)}) ও ({pfmt(Q)}) এর যোগফল থেকে ({pfmt(C)}) বিয়োগ করলে কত হয়?", pfmt(r), W(pfmt(r), [pfmt(w) if w else '0', pfmt({k: -c for k, c in r.items()}), pfmt({k: P[k] - Q[k] - C[k] for k in P if P[k] - Q[k] - C[k]}) or '1', pfmt({k: c * 2 for k, c in r.items()})]), "", lv)
P43 = part('4.3', 100, fx43, [n43_like, n43_add], [n43_two, n43_add], [n43_need, n43_sumsub])
save('m4', P41 + P42 + P43)

# ===================================================== অধ্যায় 5: সরল সমীকরণ
fx5 = [
 ("সমান চিহ্নযুক্ত বীজগণিতীয় খোলা বাক্যকে কী বলে?", "সমীকরণ", ["রাশি", "অসমতা", "সূত্র"], "", E),
 ("যে সমীকরণে চলকের সর্বোচ্চ ঘাত 1, তাকে কী বলে?", "সরল সমীকরণ", ["দ্বিঘাত সমীকরণ", "ত্রিঘাত সমীকরণ", "অভেদ"], "", E),
 ("সমীকরণের চলকের যে মান দ্বারা সমীকরণটি সিদ্ধ হয়, তাকে কী বলে?", "মূল বা সমাধান", ["সহগ", "সূচক", "পদ"], "", E),
 ("সমীকরণের উভয় পক্ষে একই সংখ্যা যোগ করলে কী হয়?", "সমীকরণ অপরিবর্তিত (সমান) থাকে", ["সমীকরণ মিথ্যা হয়", "মূল দ্বিগুণ হয়", "মূল শূন্য হয়"], "", E),
 ("পক্ষান্তর করলে কোনো পদের কী পরিবর্তন হয়?", "চিহ্ন বদলে যায়", ["সূচক বদলে যায়", "চলক বদলে যায়", "কিছুই বদলায় না"], "", M),
]
def o5_add(b, lv):
    x, a = nz(-30, 40), nz(-30, 30); c = x + a
    b.add(f"x {'+' if a > 0 else '−'} {abs(a)} = {num(c)} হলে x = কত?", num(x), W(num(x), [num(c + a), num(-x), num(x + 1), num(c)]), "পক্ষান্তর করো।", lv)
def o5_mul(b, lv):
    x, a = nz(-20, 30), nz(-12, 12)
    if a in (1, -1): return
    b.add(f"{num(a)}x = {num(a * x)} হলে x = কত?", num(x), W(num(x), [num(a * x - a), num(-x), num(a * x * a) if abs(a * x * a) < 999 else num(x + 2), num(x + 1)]), "উভয় পক্ষকে সহগ দিয়ে ভাগ।", lv)
def o5_div(b, lv):
    a = R.randint(2, 12); c = nz(-15, 20); x = a * c
    b.add(f"x/{a} = {num(c)} হলে x = কত?", num(x), W(num(x), [num(F(c, a)) if c % a == 0 else fr(F(c, a)), num(c + a), num(-x), num(x + a)]), "উভয় পক্ষকে গুণ।", lv)
def o5_chk(b, lv):
    a, c = R.randint(2, 9), R.randint(1, 20); x = R.randint(1, 15)
    d = a * x + c
    b.add(f"{a}x + {c} = {d} সমীকরণের মূল কোনটি?", x, W(x, [x + 1, x - 1 if x > 1 else x + 2, d // a if d // a != x else x + 3, d - c]), "", lv)
def o5_lin(b, lv):
    x, a, c = nz(-15, 20), nz(-9, 9), nz(-20, 20)
    if a in (1, -1): return
    d = a * x + c
    b.add(f"{pfmt({(1,): a, (0,): c}, ('x',))} = {num(d)} হলে x = কত?", num(x), W(num(x), [num(F(d + c, a)) if (d + c) % a == 0 else num(x + 2), num(-x), num(x + 1), num(d - c)]), "", lv)
def o5_both(b, lv):
    x = nz(-12, 15); a, c = R.sample([v for v in range(-9, 10) if v], 2); d = nz(-20, 20)
    e = a * x + d - c * x
    L = pfmt({(1,): a, (0,): d}, ('x',)); Rr = pfmt({(1,): c, (0,): e}, ('x',)) if e else pfmt({(1,): c}, ('x',))
    b.add(f"{L} = {Rr} হলে x = কত?", num(x), W(num(x), [num(-x), num(x + 1), num(x - 2), num(F(e + d, a + c)) if a + c and (e + d) % (a + c) == 0 and F(e + d, a + c) != x else num(x + 3)]), "চলকযুক্ত পদ এক পক্ষে আনো।", lv)
def o5_frac(b, lv):
    a = R.randint(2, 9); c = nz(-10, 10); x = a * nz(-8, 10); d = x // a + c
    b.add(f"x/{a} {'+' if c > 0 else '−'} {abs(c)} = {num(d)} হলে x = কত?", num(x), W(num(x), [num(d - c), num((d + c) * a), num(-x), num(x + a)]), "", lv)
def o5_br(b, lv):
    a = R.randint(2, 9); c = nz(-10, 10); x = nz(-10, 15)
    d = a * (x + c)
    b.add(f"{a}(x {'+' if c > 0 else '−'} {abs(c)}) = {num(d)} হলে x = কত?", num(x), W(num(x), [num(x + 2 * c), num(d - c), num(-x), num(x + 1)]), "", lv)
def o5_num(b, lv):
    a, c = R.randint(2, 9), R.randint(1, 40); x = R.randint(2, 50); add = R.random() < .5
    d = a * x + c if add else a * x - c
    b.add(f"কোনো সংখ্যার {a} গুণের সাথে {c} {'যোগ' if add else 'বিয়োগ'} করলে {d} হয়। সংখ্যাটি কত?", x, W(x, [x + 1, (d + c) // a if add and (d + c) % a == 0 and (d + c) // a != x else x - 1, d // a if d // a != x else x + 2, d - c]), "", lv)
def o5_cons(b, lv):
    n = R.choice([2, 3, 4]); x = R.randint(-10, 60); ev = R.random() < .4
    st = 2 if ev else 1
    if ev: x = x * 2
    s = sum(x + i * st for i in range(n))
    b.add(f"{n}টি ক্রমিক {'জোড় ' if ev else ''}পূর্ণসংখ্যার যোগফল {s}। ক্ষুদ্রতম সংখ্যাটি কত?", num(x), W(num(x), [num(x + st), num(x - st), num(s // n), num(x + n)]), f"x, x + {st}, … ধরে সমীকরণ।", lv)
def o5_age(b, lv):
    k = R.randint(2, 5); s = R.randint(4, 15); f = k * s; S = f + s
    b.add(f"পিতার বয়স পুত্রের বয়সের {k} গুণ। তাদের বয়সের যোগফল {S} বছর হলে পুত্রের বয়স কত বছর?", s, W(s, [f, S // 2, s + k, S // k]), f"পুত্র x হলে x + {k}x = {S}।", lv)
def o5_money(b, lv):
    a, c = R.randint(10, 200), R.randint(10, 200); diff = R.randint(5, 80)
    tot = a + a + diff
    b.add(f"রনি ও সুমির মোট {tot} টাকা আছে। সুমির টাকা রনির চেয়ে {diff} টাকা বেশি। রনির কত টাকা আছে?", f"{a} টাকা", W(f"{a} টাকা", [f"{a + diff} টাকা", f"{tot // 2} টাকা" if tot // 2 != a else f"{a + 1} টাকা", f"{tot - diff} টাকা", f"{a - diff if a > diff else a + 2 * diff} টাকা"]), "x + (x + বেশি) = মোট।", lv)
def o5_rect(b, lv):
    w = R.randint(3, 30); d = R.randint(2, 20); P = 2 * (w + w + d)
    b.add(f"একটি আয়তক্ষেত্রের দৈর্ঘ্য প্রস্থের চেয়ে {d} মিটার বেশি। পরিসীমা {P} মিটার হলে প্রস্থ কত মিটার?", w, W(w, [w + d, P // 4, w + 1, (P - d) // 2]), "2(x + x + বেশি) = পরিসীমা।", lv)
K5 = part(None, 300, fx5, [o5_add, o5_mul, o5_div, o5_chk, o5_lin], [o5_lin, o5_both, o5_frac, o5_br, o5_num, o5_chk], [o5_cons, o5_age, o5_money, o5_rect, o5_both])
save('m5', K5)

# ===================================================== 6.1 রেখা, কোণ ও সমান্তরাল রেখা
fx61 = [
 ("বিন্দুর কয়টি মাত্রা আছে?", "কোনো মাত্রা নেই", ["একটি", "দুইটি", "তিনটি"], "", E),
 ("রেখার কয়টি মাত্রা আছে?", "একটি (দৈর্ঘ্য)", ["কোনোটি নয়", "দুইটি", "তিনটি"], "", E),
 ("তলের কয়টি মাত্রা আছে?", "দুইটি", ["একটি", "তিনটি", "কোনোটি নয়"], "", E),
 ("ঘনবস্তুর কয়টি মাত্রা আছে?", "তিনটি", ["দুইটি", "একটি", "চারটি"], "", E),
 ("রেখাংশের কয়টি প্রান্তবিন্দু থাকে?", "দুইটি", ["একটি", "কোনোটি নয়", "তিনটি"], "", E),
 ("রশ্মির কয়টি প্রান্তবিন্দু থাকে?", "একটি", ["দুইটি", "কোনোটি নয়", "তিনটি"], "", E),
 ("দুটি সমান্তরাল সরলরেখা পরস্পরকে কতবার ছেদ করে?", "কখনো ছেদ করে না", ["একবার", "দুইবার", "অসংখ্যবার"], "", E),
 ("দুটি সরলরেখা পরস্পরকে ছেদ করলে বিপ্রতীপ কোণগুলো কেমন হয়?", "সমান", ["পূরক", "সম্পূরক সবসময়", "অসমান"], "", M),
]
def p61_comp(b, lv):
    a = R.randint(1, 89); sup_ = R.random() < .5
    if sup_: a = R.randint(1, 179)
    v = (180 if sup_ else 90) - a
    b.add(f"{a}° কোণের {'সম্পূরক' if sup_ else 'পূরক'} কোণ কত?", f"{v}°", W(f"{v}°", [f"{(90 if sup_ else 180) - a}°" if (90 if sup_ else 180) - a > 0 else f"{v + 10}°", f"{360 - a}°", f"{v + 1}°", f"{a}°"]), f"{'সম্পূরক: যোগফল 180°' if sup_ else 'পূরক: যোগফল 90°'}।", lv)
def p61_type(b, lv):
    a = R.choice([R.randint(1, 89), 90, R.randint(91, 179), 180, R.randint(181, 359)])
    t = 'সূক্ষ্মকোণ' if a < 90 else 'সমকোণ' if a == 90 else 'স্থূলকোণ' if a < 180 else 'সরলকোণ' if a == 180 else 'প্রবৃদ্ধ কোণ'
    b.add(f"{a}° কোণটি কোন ধরনের কোণ?", t, W(t, ['সূক্ষ্মকোণ', 'সমকোণ', 'স্থূলকোণ', 'সরলকোণ', 'প্রবৃদ্ধ কোণ']), "", lv)
def p61_line(b, lv):
    a = R.randint(10, 170); v = 180 - a
    b.add(f"একটি সরলরেখার উপর দুটি সন্নিহিত কোণের একটি {a}° হলে অপরটি কত?", f"{v}°", W(f"{v}°", [f"{abs(90 - a)}°" if abs(90 - a) != v else f"{v + 5}°", f"{a}°", f"{360 - a}°", f"{v + 10}°"]), "সরলরেখায় সন্নিহিত কোণের যোগফল 180°।", lv)
def p61_vert(b, lv):
    a = R.randint(10, 170)
    b.add(f"দুটি সরলরেখা ছেদ করে একটি কোণ {a}° উৎপন্ন করল। এর বিপ্রতীপ কোণ কত?", f"{a}°", W(f"{a}°", [f"{180 - a}°", f"{abs(90 - a)}°" if a != 90 else "0°", f"{360 - a}°", f"{a + 10}°"]), "বিপ্রতীপ কোণ পরস্পর সমান।", lv)
def p61_ratio(b, lv):
    p, q = R.randint(1, 9), R.randint(1, 9)
    if 180 % (p + q) or p == q: return
    k = 180 // (p + q); big = R.random() < .5
    v = max(p, q) * k if big else min(p, q) * k
    b.add(f"সরলরেখার উপর দুটি সন্নিহিত কোণের অনুপাত {p} : {q}। {'বড়' if big else 'ছোট'} কোণটি কত?", f"{v}°", W(f"{v}°", [f"{min(p, q) * k if big else max(p, q) * k}°", f"{90 // (p + q) * max(p, q) if 90 % (p + q) == 0 else v + 5}°", f"{v + k}°", f"{k}°"]), "", lv)
def p61_x(b, lv):
    a = R.randint(2, 6); c = R.randint(-20, 30); x = R.randint(5, 40)
    if not 0 < a * x + c < 180: return
    y = 180 - (a * x + c)
    b.add(f"সরলরেখার উপর দুটি সন্নিহিত কোণ ({a}x {'+' if c >= 0 else '−'} {abs(c)})° ও {y}° হলে x এর মান কত?", x, W(x, [x + 1, x - 2, (180 - y) // a if (180 - y) // a != x else x + 3, y // a]), "", lv)
def p61_point(b, lv):
    xs = [R.randint(30, 120) for _ in range(3)]; v = 360 - sum(xs)
    if v <= 0: return
    b.add(f"একটি বিন্দুতে চারটি কোণ উৎপন্ন হয়েছে। তিনটি কোণ {xs[0]}°, {xs[1]}° ও {xs[2]}° হলে চতুর্থ কোণ কত?", f"{v}°", W(f"{v}°", [f"{abs(180 - sum(xs))}°" if abs(180 - sum(xs)) != v else f"{v + 10}°", f"{v + 10}°", f"{sum(xs)}°", f"{max(1, v - 5)}°"]), "এক বিন্দুতে কোণগুলোর যোগফল 360°।", lv)
def p61_par(b, lv):
    a = R.randint(20, 160); t = R.randrange(3)
    nm, v = [('একান্তর', a), ('অনুরূপ', a), ('ছেদকের একই পাশের অন্তঃস্থ', 180 - a)][t]
    b.add(f"দুটি সমান্তরাল রেখাকে একটি ছেদক ছেদ করলে একটি কোণ {a}° হয়। এর {nm} কোণ কত?", f"{v}°", W(f"{v}°", [f"{180 - v}°" if 180 - v != v else f"{v + 10}°", f"{abs(90 - a)}°" if abs(90 - a) not in (v, 180 - v) else f"{v + 20}°", f"{360 - v}°", f"{v + 5}°"]), "", lv)
P61 = part('6.1', 100, fx61, [p61_comp, p61_type, p61_line, p61_vert], [p61_ratio, p61_x, p61_line, p61_comp], [p61_point, p61_par])

# ===================================================== 6.2 ত্রিভুজ ও চতুর্ভুজ
fx62 = [
 ("ত্রিভুজের তিন কোণের সমষ্টি কত?", "180°", ["90°", "360°", "270°"], "", E),
 ("চতুর্ভুজের চার কোণের সমষ্টি কত?", "360°", ["180°", "270°", "540°"], "", E),
 ("যে ত্রিভুজের তিনটি বাহুই সমান তাকে কী বলে?", "সমবাহু ত্রিভুজ", ["সমদ্বিবাহু ত্রিভুজ", "বিষমবাহু ত্রিভুজ", "সমকোণী ত্রিভুজ"], "", E),
 ("যে ত্রিভুজের দুটি বাহু সমান তাকে কী বলে?", "সমদ্বিবাহু ত্রিভুজ", ["সমবাহু ত্রিভুজ", "বিষমবাহু ত্রিভুজ", "স্থূলকোণী ত্রিভুজ"], "", E),
 ("সমবাহু ত্রিভুজের প্রতিটি কোণ কত?", "60°", ["90°", "45°", "120°"], "", E),
 ("যে চতুর্ভুজের বিপরীত বাহুগুলো সমান্তরাল তাকে কী বলে?", "সামান্তরিক", ["ট্রাপিজিয়াম", "ঘুড়ি", "অসমবাহু চতুর্ভুজ"], "", M),
 ("যে সামান্তরিকের সব বাহু সমান কিন্তু কোণ সমকোণ নয়, তাকে কী বলে?", "রম্বস", ["বর্গ", "আয়ত", "ট্রাপিজিয়াম"], "", M),
]
def q62_third(b, lv):
    a, c = R.randint(20, 100), R.randint(20, 100); v = 180 - a - c
    if v <= 0: return
    b.add(f"একটি ত্রিভুজের দুটি কোণ {a}° ও {c}° হলে তৃতীয় কোণ কত?", f"{v}°", W(f"{v}°", [f"{360 - a - c}°", f"{a + c}°", f"{v + 10}°", f"{abs(90 - a)}°" if abs(90 - a) != v else f"{v + 5}°"]), "", lv)
def q62_kind(b, lv):
    while True:
        a, c = R.randint(10, 130), R.randint(10, 130); d = 180 - a - c
        if d > 0: break
    m = max(a, c, d); t = 'সূক্ষ্মকোণী' if m < 90 else 'সমকোণী' if m == 90 else 'স্থূলকোণী'
    b.add(f"একটি ত্রিভুজের কোণগুলো {a}°, {c}° ও {d}° হলে ত্রিভুজটি কোন ধরনের?", f"{t} ত্রিভুজ", W(f"{t} ত্রিভুজ", ['সূক্ষ্মকোণী ত্রিভুজ', 'সমকোণী ত্রিভুজ', 'স্থূলকোণী ত্রিভুজ', 'সমবাহু ত্রিভুজ']), "বৃহত্তম কোণ দেখে।", lv)
def q62_side(b, lv):
    t = R.randrange(3); a = R.randint(3, 20)
    s = [(a, a, a), (a, a, R.choice([x for x in range(2, 2 * a) if x != a])), tuple(R.sample(range(3, 25), 3))][t]
    if t == 2 and (max(s) >= sum(s) - max(s)): return
    nm = ['সমবাহু', 'সমদ্বিবাহু', 'বিষমবাহু'][t]
    b.add(f"একটি ত্রিভুজের বাহুগুলো {s[0]}, {s[1]} ও {s[2]} সেমি হলে ত্রিভুজটি কোন ধরনের?", f"{nm} ত্রিভুজ", W(f"{nm} ত্রিভুজ", ['সমবাহু ত্রিভুজ', 'সমদ্বিবাহু ত্রিভুজ', 'বিষমবাহু ত্রিভুজ', 'সমকোণী ত্রিভুজ']), "", lv)
def q62_quad(b, lv):
    xs = [R.randint(50, 130) for _ in range(3)]; v = 360 - sum(xs)
    if not 20 < v < 180: return
    b.add(f"একটি চতুর্ভুজের তিনটি কোণ {xs[0]}°, {xs[1]}° ও {xs[2]}° হলে চতুর্থ কোণ কত?", f"{v}°", W(f"{v}°", [f"{abs(180 - sum(xs))}°" if abs(180 - sum(xs)) != v else f"{v + 10}°", f"{v + 10}°", f"{v - 5}°", f"{sum(xs) - 180}°" if sum(xs) - 180 not in (v,) and sum(xs) > 180 else f"{v + 20}°"]), "চতুর্ভুজের কোণগুলোর যোগফল 360°।", lv)
def q62_ratio(b, lv):
    p, q, r = R.sample(range(1, 10), 3)
    if 180 % (p + q + r): return
    k = 180 // (p + q + r); which = R.choice(['বৃহত্তম', 'ক্ষুদ্রতম'])
    v = (max if which == 'বৃহত্তম' else min)(p, q, r) * k
    b.add(f"একটি ত্রিভুজের কোণগুলোর অনুপাত {p} : {q} : {r} হলে {which} কোণটি কত?", f"{v}°", W(f"{v}°", [f"{x * k}°" for x in (p, q, r)] + [f"{v + k}°", f"{k}°"]), "", lv)
def q62_ext(b, lv):
    a, c = R.randint(20, 80), R.randint(20, 80)
    b.add(f"একটি ত্রিভুজের দুটি অন্তঃস্থ বিপরীত কোণ {a}° ও {c}° হলে বহিঃস্থ কোণটি কত?", f"{a + c}°", W(f"{a + c}°", [f"{180 - a - c}°", f"{180 - a}°", f"{a + c + 10}°", f"{abs(a - c)}°" if a != c else "90°"]), "বহিঃস্থ কোণ = অন্তঃস্থ বিপরীত কোণদ্বয়ের যোগফল।", lv)
def q62_peri(b, lv):
    t = R.randrange(3)
    if t == 0: a, c = R.randint(3, 30), R.randint(3, 30); v = 2 * (a + c); q = f"একটি আয়তক্ষেত্রের দৈর্ঘ্য {a} সেমি ও প্রস্থ {c} সেমি হলে পরিসীমা কত সেমি?"; w = [a * c, a + c, v + 2, 4 * a]
    elif t == 1: a = R.randint(3, 40); v = 4 * a; q = f"একটি বর্গের এক বাহু {a} সেমি হলে পরিসীমা কত সেমি?"; w = [a * a, 2 * a, v + 4, 3 * a]
    else: s = R.sample(range(3, 30), 3); v = sum(s); q = f"একটি ত্রিভুজের বাহুগুলো {s[0]}, {s[1]} ও {s[2]} সেমি হলে পরিসীমা কত সেমি?"; w = [v + 1, v - 2, s[0] * s[1], 2 * v]
    if v in w: return
    b.add(q, f"{v} সেমি", W(f"{v} সেমি", [f"{x} সেমি" for x in w]), "সব বাহুর যোগফল।", lv)
def q62_iso(b, lv):
    a = R.randint(10, 160)
    if (180 - a) % 2: return
    v = (180 - a) // 2
    b.add(f"একটি সমদ্বিবাহু ত্রিভুজের শীর্ষকোণ {a}° হলে ভূমিসংলগ্ন প্রতিটি কোণ কত?", f"{v}°", W(f"{v}°", [f"{180 - a}°", f"{a}°" if a != v else f"{v + 10}°", f"{90 - a // 2 + 5}°" if 90 - a // 2 + 5 != v else f"{v + 5}°", f"{v * 2 + 1}°"]), "ভূমিসংলগ্ন কোণ দুটি সমান।", lv)
def q62_qr(b, lv):
    xs = R.sample(range(1, 10), 4)
    if 360 % sum(xs): return
    k = 360 // sum(xs); v = max(xs) * k
    if v >= 180: return
    b.add(f"একটি চতুর্ভুজের কোণগুলোর অনুপাত {' : '.join(map(str, xs))} হলে বৃহত্তম কোণটি কত?", f"{v}°", W(f"{v}°", [f"{x * k}°" for x in xs] + [f"{v + k}°"]), "", lv)
def q62_rsq(b, lv):
    P = R.randint(4, 40) * 4; isq = R.random() < .5
    if isq: v = P // 4; q = f"একটি বর্গের পরিসীমা {P} সেমি হলে এক বাহুর দৈর্ঘ্য কত সেমি?"; w = [P // 2, v + 2, v * 2, P - 4]
    else:
        L = R.randint(5, 40); Wd = R.randint(2, L); P = 2 * (L + Wd); v = Wd
        q = f"একটি আয়তক্ষেত্রের পরিসীমা {P} সেমি ও দৈর্ঘ্য {L} সেমি হলে প্রস্থ কত সেমি?"; w = [P - L, P // 2, Wd + 2, L]
    if v in w: return
    b.add(q, f"{v} সেমি", W(f"{v} সেমি", [f"{x} সেমি" for x in w]), "", lv)
P62 = part('6.2', 100, fx62, [q62_third, q62_kind, q62_side, q62_quad, q62_peri], [q62_ratio, q62_ext, q62_peri, q62_quad], [q62_iso, q62_qr, q62_rsq])
save('m6', P61 + P62)

# ===================================================== অধ্যায় 7: ব্যবহারিক জ্যামিতি
fx7 = [
 ("জ্যামিতিক অঙ্কনে বৃত্তচাপ আঁকতে কোন যন্ত্র ব্যবহৃত হয়?", "কম্পাস", ["চাঁদা", "সেটস্কয়ার", "স্কেল"], "", E),
 ("কোণ পরিমাপ করতে কোন যন্ত্র ব্যবহৃত হয়?", "চাঁদা", ["কম্পাস", "স্কেল", "ডিভাইডার"], "", E),
 ("সরলরেখা আঁকতে ও দৈর্ঘ্য মাপতে কোন যন্ত্র ব্যবহৃত হয়?", "স্কেল (রুলার)", ["চাঁদা", "কম্পাস", "সেটস্কয়ার"], "", E),
 ("সমকোণ আঁকতে কোন যন্ত্রটি সবচেয়ে সহজে ব্যবহার করা যায়?", "সেটস্কয়ার", ["কম্পাস", "ডিভাইডার", "পেন্সিল"], "", E),
 ("শুধু কম্পাস ও রুলার দিয়ে প্রথমে কোন কোণটি সরাসরি আঁকা হয়?", "60°", ["50°", "70°", "40°"], "সমবাহু ত্রিভুজের কোণ।", E),
 ("60° কোণকে সমদ্বিখণ্ডিত করলে কোন কোণ পাওয়া যায়?", "30°", ["20°", "45°", "15°"], "", E),
 ("90° কোণকে সমদ্বিখণ্ডিত করলে কোন কোণ পাওয়া যায়?", "45°", ["30°", "60°", "22°"], "", E),
 ("কোনো রেখাংশের লম্বদ্বিখণ্ডক রেখাংশটির সাথে কত ডিগ্রি কোণ তৈরি করে?", "90°", ["45°", "60°", "180°"], "", E),
 ("কম্পাস ও রুলার দিয়ে 75° কোণ আঁকতে কোন দুটি কোণের মাঝের কোণ সমদ্বিখণ্ডিত করা হয়?", "60° ও 90°", ["45° ও 90°", "30° ও 60°", "90° ও 120°"], "", M),
 ("কম্পাস ও রুলার দিয়ে 105° কোণ আঁকতে কোন দুটি কোণের মাঝের কোণ সমদ্বিখণ্ডিত করা হয়?", "90° ও 120°", ["60° ও 90°", "120° ও 150°", "45° ও 60°"], "", M),
 ("কম্পাস ও রুলার দিয়ে 135° কোণ আঁকতে সাধারণত কী করা হয়?", "90° এর সাথে 45° যোগ করা হয়", ["60° এর সাথে 60° যোগ করা হয়", "120° কে সমদ্বিখণ্ডিত করা হয়", "180° থেকে 30° বাদ দেওয়া হয়"], "", M),
 ("রেখাংশ সমদ্বিখণ্ডিত করতে কম্পাসের ব্যাসার্ধ কেমন নিতে হয়?", "রেখাংশের অর্ধেকের চেয়ে বড়", ["রেখাংশের অর্ধেকের চেয়ে ছোট", "ঠিক রেখাংশের সমান হতে হবে", "শূন্য"], "", M),
]
def r7_bis(b, lv):
    a = R.randrange(10, 179, 2) if R.random() < .7 else R.randrange(11, 179, 2)
    v = F(a, 2)
    b.add(f"{a}° কোণকে সমদ্বিখণ্ডিত করলে প্রতিটি অংশ কত ডিগ্রি?", f"{D(v)}°", W(f"{D(v)}°", [f"{a}°", f"{D(F(a, 3))}°" if a % 3 == 0 else f"{D(v + 5)}°", f"{180 - a}°", f"{D(v + 10)}°"]), "কোণের অর্ধেক।", lv)
def r7_seg(b, lv):
    L = F(R.randint(20, 300), 10); n = R.choice([2, 2, 3, 4, 5]); v = L / n
    if v.denominator not in (1, 2, 4, 5, 10, 20): return
    b.add(f"{D(L)} সেমি দৈর্ঘ্যের একটি রেখাংশকে সমান {n} ভাগ করলে প্রতিটি ভাগের দৈর্ঘ্য কত সেমি?" if n > 2 else f"{D(L)} সেমি দৈর্ঘ্যের একটি রেখাংশকে সমদ্বিখণ্ডিত করলে প্রতিটি অংশের দৈর্ঘ্য কত সেমি?", D(v), W(D(v), [D(L), D(L / (n + 1)), D(L * n) if L * n < 100 else D(v + 1), D(v + F(1, 2))]), "", lv)
def r7_ok(b, lv):
    c = R.choice([15, 30, 45, 60, 75, 90, 105, 120, 135, 150, 165, 22.5, 67.5, 7.5])
    w = R.sample([x for x in [20, 25, 35, 40, 50, 55, 65, 70, 80, 85, 95, 100, 110, 115, 125, 130, 140, 145, 155, 160, 170, 10, 5] if x != c], 3)
    b.add("নিচের কোন কোণটি শুধু কম্পাস ও রুলার দিয়ে আঁকা যায়?", f"{D(F(c).limit_denominator(2))}°", W(f"{D(F(c).limit_denominator(2))}°", [f"{x}°" for x in w]), "60° থেকে সমদ্বিখণ্ডন ও যোগ-বিয়োগে পাওয়া কোণগুলো।", lv)
def r7_sup(b, lv):
    a = R.choice([30, 45, 60, 75, 90, 105, 120, 135, 150, 15, 165]); sup_ = R.random() < .6
    if not sup_ and a >= 90: a = R.choice([15, 30, 45, 60, 75])
    v = (180 if sup_ else 90) - a
    b.add(f"কম্পাস দিয়ে {a}° কোণ আঁকার পর সরলরেখার অপর পাশে যে {'সম্পূরক' if sup_ else 'পূরক'} কোণ পাওয়া যায় তা কত?" if sup_ else f"{a}° কোণের পূরক কোণ আঁকতে কত ডিগ্রি কোণ আঁকতে হবে?", f"{v}°", W(f"{v}°", [f"{(90 if sup_ else 180) - a}°" if (90 if sup_ else 180) - a > 0 else f"{v + 15}°", f"{a}°", f"{360 - a}°", f"{v + 15}°"]), "", lv)
def r7_combo(b, lv):
    a, c = R.sample([15, 30, 45, 60, 90, 120], 2); s = R.random() < .5
    v = a + c if s else abs(a - c)
    if v == 0 or v > 180: return
    b.add(f"{a}° ও {c}° কোণ পাশাপাশি {'যুক্ত করে' if s else 'একটি থেকে অপরটি বাদ দিয়ে'} আঁকলে কত ডিগ্রি কোণ পাওয়া যায়?", f"{v}°", W(f"{v}°", [f"{abs(a - c) if s else a + c}°", f"{v + 15}°", f"{max(a, c)}°", f"{180 - v}°" if 180 - v != v else f"{v + 30}°"]), "", lv)
def r7_bis2(b, lv):
    a = R.choice([60, 90, 120, 180, 150]); n = R.choice([2, 4])
    v = F(a, n)
    b.add(f"{a}° কোণকে সমদ্বিখণ্ডিত করে প্রাপ্ত প্রতিটি কোণকে আবার সমদ্বিখণ্ডিত করলে প্রতিটি কোণ কত?" if n == 4 else f"{a}° কোণের সমদ্বিখণ্ডক প্রতিটি অংশে কত ডিগ্রি কোণ তৈরি করে?", f"{D(v)}°", W(f"{D(v)}°", [f"{D(F(a, 2) if n == 4 else F(a, 4))}°", f"{D(F(a, 3))}°", f"{a}°", f"{D(v + 15)}°"]), "", lv)
def r7_tri(b, lv):
    s = sorted(R.sample(range(2, 20), 3)); ok = s[0] + s[1] > s[2]
    ans = "আঁকা যাবে" if ok else "আঁকা যাবে না"
    b.add(f"{s[0]} সেমি, {s[1]} সেমি ও {s[2]} সেমি বাহু দিয়ে ত্রিভুজ আঁকা যাবে কি?", ans, W(ans, ["আঁকা যাবে না" if ok else "আঁকা যাবে", "শুধু সমকোণী ত্রিভুজ আঁকা যাবে", "শুধু সমবাহু ত্রিভুজ আঁকা যাবে"]), "যেকোনো দুই বাহুর যোগফল তৃতীয় বাহু অপেক্ষা বড় হতে হয়।", lv)
def r7_third(b, lv):
    a, c = R.sample(range(3, 20), 2); lo, hi = abs(a - c), a + c
    v = R.randint(lo + 1, hi - 1)
    w = [lo, hi, hi + R.randint(1, 5)]
    b.add(f"একটি ত্রিভুজের দুটি বাহু {a} সেমি ও {c} সেমি। তৃতীয় বাহুর দৈর্ঘ্য নিচের কোনটি হতে পারে?", f"{v} সেমি", W(f"{v} সেমি", [f"{x} সেমি" for x in w]), f"{lo} < তৃতীয় বাহু < {hi}।", lv)
def r7_clock(b, lv):
    h = R.randint(1, 11); v = min(30 * h, 360 - 30 * h)
    b.add(f"ঘড়িতে ঠিক {h}টা বাজলে ঘণ্টা ও মিনিটের কাঁটার মধ্যবর্তী ক্ষুদ্রতর কোণ কত? (এই কোণটি কম্পাসেও আঁকা যায়)", f"{v}°", W(f"{v}°", [f"{360 - v}°" if 360 - v != v else "90°", f"{v + 30}°", f"{abs(v - 30)}°" if v != 30 else "60°", f"{h * 6}°"]), "প্রতি ঘণ্টার ঘর 30°।", lv)
K7 = part(None, 300, fx7, [r7_bis, r7_seg, r7_ok, r7_sup], [r7_combo, r7_bis2, r7_tri, r7_bis, r7_seg, r7_clock], [r7_third, r7_tri, r7_combo, r7_clock])
save('m7', K7)

# ===================================================== অধ্যায় 8: তথ্য ও উপাত্ত
fx8 = [
 ("সংখ্যাভিত্তিক তথ্যকে কী বলে?", "উপাত্ত", ["গড়", "মধ্যক", "লেখচিত্র"], "", E),
 ("মানের ক্রমানুসারে সাজানো উপাত্তকে কী বলে?", "বিন্যস্ত উপাত্ত", ["অবিন্যস্ত উপাত্ত", "গড়", "প্রচুরক"], "", E),
 ("উপাত্তে সবচেয়ে বেশিবার আসা মানকে কী বলে?", "প্রচুরক", ["মধ্যক", "গড়", "পরিসর"], "", E),
 ("উপাত্তগুলো মানের ক্রমে সাজালে মাঝের মানকে কী বলে?", "মধ্যক", ["প্রচুরক", "গড়", "সমষ্টি"], "", E),
 ("গড় নির্ণয়ের সূত্র কোনটি?", "উপাত্তগুলোর সমষ্টি ÷ উপাত্তের সংখ্যা", ["বৃহত্তম − ক্ষুদ্রতম", "মাঝের মান", "সবচেয়ে বেশিবার আসা মান"], "", E),
 ("ট্যালি চিহ্নে প্রতি পাঁচটি গণনার পঞ্চমটি কীভাবে দেওয়া হয়?", "আগের চারটি দাগ আড়াআড়ি কেটে", ["নতুন খাড়া দাগ দিয়ে", "বৃত্ত এঁকে", "তারকা দিয়ে"], "", E),
]
def s8_mean(b, lv):
    n = R.randint(3, 7)
    while True:
        xs = [R.randint(1, 60) for _ in range(n)]
        if sum(xs) % n == 0: break
    m = sum(xs) // n
    b.add(f"{', '.join(map(str, xs))} সংখ্যাগুলোর গড় কত?", m, W(m, [m + 1, m - 1, sorted(xs)[n // 2] if sorted(xs)[n // 2] != m else m + 2, sum(xs)]), "সমষ্টি ÷ সংখ্যা।", lv)
def s8_median(b, lv):
    n = R.choice([5, 7, 9, 6, 8]); xs = R.sample(range(1, 80), n); s = sorted(xs)
    med = F(s[n // 2]) if n % 2 else F(s[n // 2 - 1] + s[n // 2], 2)
    b.add(f"{', '.join(map(str, xs))} উপাত্তের মধ্যক কত?", D(med), W(D(med), [D(F(xs[n // 2])) if F(xs[n // 2]) != med else D(med + 1), D(F(sum(xs), n)), D(med + 1), D(F(s[0] + s[-1], 2))]), "মানের ক্রমে সাজিয়ে মাঝের মান।", lv)
def s8_mode(b, lv):
    base = R.sample(range(1, 60), 5); m = R.choice(base)
    xs = base + [m, m]; R.shuffle(xs)
    b.add(f"{', '.join(map(str, xs))} উপাত্তের প্রচুরক কত?", m, W(m, [x for x in base if x != m] + [max(xs)]), "সবচেয়ে বেশিবার আসা মান।", lv)
def s8_sort(b, lv):
    xs = R.sample(range(1, 99), 6); s = sorted(xs); c = ', '.join(map(str, s))
    w = [', '.join(map(str, sorted(xs, reverse=True))), ', '.join(map(str, s[:2] + [s[3], s[2]] + s[4:])), ', '.join(map(str, sorted(xs, key=lambda v: v % 10)))]
    b.add(f"{', '.join(map(str, xs))} উপাত্তকে মানের ঊর্ধ্বক্রমে সাজালে কোনটি হবে?", c, W(c, w + [', '.join(map(str, s[1:] + s[:1]))]), "", lv)
def s8_tally(b, lv):
    n = R.randint(6, 28); f, r = divmod(n, 5)
    s = '  '.join(['||||/'] * f + (['|' * r] if r else []))
    b.add(f"ট্যালি চিহ্ন  {s}  দ্বারা কোন সংখ্যা বোঝায়? (||||/ = আড়াআড়ি কাটা চারটি দাগ, অর্থাৎ 5)", n, W(n, [n + 1, n - 1, f + r, n + 5]), "প্রতিটি কাটা গুচ্ছ = 5।", lv)
def s8_freq(b, lv):
    vals = R.sample(range(1, 10), 3); xs = [R.choice(vals) for _ in range(R.randint(10, 16))]
    t = R.choice(vals); v = xs.count(t)
    if v == 0: return
    b.add(f"{', '.join(map(str, xs))} উপাত্তে {t} সংখ্যাটির গণসংখ্যা কত?", v, W(v, [v + 1, max(0, v - 1), len(xs), v + 2]), "কতবার এসেছে গুনে দেখো।", lv)
def s8_missing(b, lv):
    n = R.randint(4, 7); m = R.randint(10, 70)
    xs = [R.randint(1, 99) for _ in range(n - 1)]; last = m * n - sum(xs)
    if last <= 0 or last > 200: return
    b.add(f"{n}টি সংখ্যার গড় {m}। এর {n - 1}টি সংখ্যা {', '.join(map(str, xs))} হলে অপর সংখ্যাটি কত?", last, W(last, [last + 1, m, last - n, m * n]), "মোট = গড় × সংখ্যা।", lv)
def s8_total(b, lv):
    n = R.randint(5, 45); m = R.randint(20, 90)
    b.add(f"একটি শ্রেণির {n} জন শিক্ষার্থীর গড় নম্বর {m}। তাদের মোট নম্বর কত?", n * m, W(n * m, [n + m, n * m + n, n * m - m, m * 10]), "গড় × সংখ্যা।", lv)
def s8_bar(b, lv):
    days = ['শনি', 'রবি', 'সোম', 'মঙ্গল', 'বুধ']; xs = R.sample(range(10, 60), 5)
    ask = R.randrange(3)
    desc = ', '.join(f"{d}বার {x}" for d, x in zip(days, xs))
    if ask == 0: c = days[xs.index(max(xs))] + 'বার'; q = 'কোন দিন সবচেয়ে বেশি শিক্ষার্থী উপস্থিত ছিল?'; w = [d + 'বার' for d in days]
    elif ask == 1: c = str(sum(xs)); q = 'পাঁচ দিনে মোট কতজন উপস্থিত ছিল?'; w = [str(sum(xs) + 10), str(max(xs) * 5), str(sum(xs) - min(xs))]
    else: c = str(max(xs) - min(xs)); q = 'সর্বোচ্চ ও সর্বনিম্ন উপস্থিতির পার্থক্য কত?'; w = [str(max(xs)), str(max(xs) + min(xs)), str(max(xs) - min(xs) + 1)]
    b.add(f"একটি স্তম্ভলেখে পাঁচ দিনের উপস্থিতি দেখানো হয়েছে: {desc} জন। {q}", c, W(c, w), "", lv)
def s8_combined(b, lv):
    n1, n2 = R.randint(5, 30), R.randint(5, 30); m1, m2 = R.randint(20, 90), R.randint(20, 90)
    v = F(n1 * m1 + n2 * m2, n1 + n2)
    if v.denominator not in (1, 2, 4, 5, 10, 20, 25, 50): return
    b.add(f"{n1} জন শিক্ষার্থীর গড় নম্বর {m1} এবং অন্য {n2} জনের গড় নম্বর {m2} হলে সকলের গড় নম্বর কত?", D(v), W(D(v), [D(F(m1 + m2, 2)), D(v + 1), D(v - 1), D(v + 2)]), "মোট নম্বর ÷ মোট শিক্ষার্থী।", lv)
def s8_change(b, lv):
    n = R.randint(4, 10); m = R.randint(15, 60); x = R.randint(1, 99)
    tot = n * m + x
    if tot % (n + 1): return
    v = tot // (n + 1)
    b.add(f"{n}টি সংখ্যার গড় {m}। এদের সাথে {x} যোগ করলে নতুন গড় কত হবে?", v, W(v, [m, v + 1, (n * m + x) // n if (n * m + x) // n != v else v - 1, m + x]), "নতুন সমষ্টি ÷ নতুন সংখ্যা।", lv)
K8 = part(None, 300, fx8, [s8_mean, s8_median, s8_mode, s8_sort, s8_tally, s8_freq], [s8_mean, s8_median, s8_mode, s8_missing, s8_total, s8_bar, s8_freq], [s8_combined, s8_change, s8_missing, s8_bar])
save('m8', K8)
