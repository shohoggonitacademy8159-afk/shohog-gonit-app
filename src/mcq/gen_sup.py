#!/usr/bin/env python3
"""বর্ধিত প্রশ্ন (MCQ_EXT): মূল জেনারেটরের টেমপ্লেটে যেসব অংশে নতুন প্রশ্ন কম পড়েছে, সেগুলো পূরণের অতিরিক্ত টেমপ্লেট।
আউটপুট: ext/S_<course>_<ch>.json (প্রতিটি প্রশ্নে ex ট্যাগ; অধ্যায়ভিত্তিক হলে ex নেই)।
প্রয়োজন: --need ফাইল (ext/need.json) = {"course|ch|ex": {"সহজ": n, ...}}"""
import os, sys, json, math, random, pathlib
from fractions import Fraction as F
os.environ['MCQ_EXT'] = '1'
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
import mcqlib
from mcqlib import Bank, E, M, H, fr, num, surd, sup, pfmt

R = random.Random(2026110299)
D = pathlib.Path(__file__).resolve().parent
NEED = json.loads((D / 'ext/need.json').read_text(encoding='utf-8'))

def W(c, pool):
    out = []
    for w in pool:
        w = str(w)
        if w != str(c) and w not in out: out.append(w)
    return out
def nz(a, b): return R.choice([v for v in range(a, b + 1) if v])
def sq(v):
    v = F(v)
    if v.denominator == 1:
        r = math.isqrt(v.numerator); return str(r) if r * r == v.numerator else surd(v.numerator)
    n, d = v.numerator, v.denominator; rn, rd = math.isqrt(n), math.isqrt(d)
    if rn * rn == n and rd * rd == d: return fr(F(rn, rd))
    if rd * rd == d: return f"{sq(n)}/{rd}"
    return f"{sq(n * d)}/{d}"
def co(c, s):
    c = F(c)
    if c == 1: return s
    if c == -1: return '−' + s
    return (f"({num(c)})" if c.denominator > 1 else num(c)) + s
def piF(v):
    v = F(v)
    if v == 0: return '0'
    sg = '−' if v < 0 else ''; v = abs(v)
    if v == 1: return sg + 'π'
    if v.denominator == 1: return f"{sg}{v.numerator}π"
    return f"{sg}{v.numerator if v.numerator != 1 else ''}π/{v.denominator}"
X = ('x',)
def px(d): return pfmt({(k,): v for k, v in d.items() if v}, X) if any(d.values()) else '0'
TRI = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29), (9, 40, 41), (12, 35, 37), (11, 60, 61), (28, 45, 53), (33, 56, 65), (16, 63, 65), (48, 55, 73), (13, 84, 85), (36, 77, 85), (39, 80, 89), (65, 72, 97)]
def tri():
    p, q, r = R.choice(TRI)
    return (p, q, r) if R.random() < .5 else (q, p, r)
def dg(v): return f"{num(v)}°"

OUT = {}
def part(course, ch, ex, fixed, eg, mg, hg):
    key = f"{course}|{ch}|{ex or '-'}"
    need = NEED.get(key)
    if not need: return
    b = Bank(ex, R)
    for q, c, w, e, lv in fixed:
        if b.count(lv) < need.get(lv, 0): b.add(q, c, w, e, lv)
    for lv, gs in ((E, eg), (M, mg), (H, hg)):
        n = need.get(lv, 0); tries = 0; miss = {}
        while b.count(lv) < n:
            tries += 1
            if tries > 120000: print('STILL SHORT', key, lv, b.count(lv), '/', n); break
            alive = [g for g in gs if miss.get(g.__name__, 0) < 400] or gs
            g = R.choice(alive); before = b.count(lv)
            g(b, lv)
            if b.count(lv) == before: miss[g.__name__] = miss.get(g.__name__, 0) + 1
            else: miss[g.__name__] = 0
    items = []
    for lv in (E, M, H): items += [x for x in b.items if x['lv'] == lv][:need.get(lv, 0)]
    if ex is None:
        for x in items: x.pop('ex', None)
    OUT.setdefault((course, ch), []).extend(items)
    print(key, {lv: sum(1 for x in items if x['lv'] == lv) for lv in (E, M, H)})

# ---------------------------------------------------------------- c10 অধ্যায় 1: বাস্তব সংখ্যা
PR = [p for p in range(2, 200) if all(p % d for d in range(2, int(p ** .5) + 1))]
def a1_class(b, lv):
    n = R.randint(2, 400); r = math.isqrt(n)
    t = R.choice(['root', 'frac', 'dec'])
    if t == 'root': q, ok = f"√{n}", ('মূলদ' if r * r == n else 'অমূলদ')
    elif t == 'frac': p, d = R.randint(1, 99), R.randint(2, 99); q, ok = f"{p}/{d}", 'মূলদ'
    else: q, ok = f"{R.randint(0, 99)}.{R.randint(1, 999)}", 'মূলদ'
    b.add(f"{q} কোন ধরনের সংখ্যা?", ok, ['মূলদ', 'অমূলদ', 'জটিল', 'কাল্পনিক'], "p/q আকারে লেখা গেলে মূলদ।", lv)
def a1_term(b, lv):
    p, d = R.randint(1, 60), R.randint(2, 160)
    if math.gcd(p, d) != 1: return
    dd = d
    for f in (2, 5):
        while dd % f == 0: dd //= f
    ok = 'সসীম দশমিক' if dd == 1 else 'আবৃত্ত দশমিক'
    b.add(f"{p}/{d} ভগ্নাংশটিকে দশমিকে প্রকাশ করলে কেমন হবে?", ok, ['সসীম দশমিক', 'আবৃত্ত দশমিক', 'অসীম অনাবৃত্ত দশমিক', 'পূর্ণসংখ্যা'], "হরে 2 ও 5 ছাড়া মৌলিক উৎপাদক থাকলে আবৃত্ত।", lv)
def a1_rec2(b, lv):
    ab = R.randint(1, 98)
    if ab % 11 == 0: return
    s = f"{ab:02d}"; v = F(ab, 99)
    b.add(f"0.{s}{s}{s}… (আবৃত্ত) কে সাধারণ ভগ্নাংশে প্রকাশ করলে কত?", fr(v), W(fr(v), [fr(F(ab, 100)), fr(F(ab, 90)), fr(F(ab, 999)), fr(F(ab + 1, 99))]), f"{s}/99।", lv)
def a1_surdadd(b, lv):
    n = R.choice([2, 3, 5, 6, 7, 10, 11, 13]); a, c = R.randint(1, 15), R.randint(1, 15); op = R.choice(['+', '−'])
    v = a + c if op == '+' else a - c
    ok = '0' if v == 0 else co(v, f"√{n}")
    b.add(f"{a}√{n} {op} {c}√{n} = কত?", ok, W(ok, [co(a * c, f"√{n}"), f"{a + c}√{2 * n}", co(abs(v) + 1, f"√{n}"), co(-v, f"√{n}") if v else '1']), "", lv)
def a1_mixed(b, lv):
    a = R.randint(1, 9); bc = R.randint(1, 98)
    if bc % 11 == 0: return
    s = f"{bc:02d}"; v = F(a * 100 + bc - a, 990)
    b.add(f"0.{a}{s}{s}{s}… (শুধু {s} আবৃত্ত) কে সাধারণ ভগ্নাংশে প্রকাশ করলে কত?", fr(v), W(fr(v), [fr(F(a * 100 + bc, 990)), fr(F(a * 100 + bc - a, 999)), fr(F(a * 100 + bc, 1000)), fr(v + F(1, 990))]), f"({a}{s} − {a})/990।", lv)
def a1_conj(b, lv):
    a, n = R.randint(1, 15), R.randint(2, 60)
    if math.isqrt(n) ** 2 == n: return
    v = a * a - n
    b.add(f"({a} + √{n})({a} − √{n}) = কত?", num(v), W(num(v), [num(a * a + n), num(a - n), num(2 * a), num(v + 1)]), "(a + b)(a − b) = a² − b²।", lv)
def a1_sqsum(b, lv):
    p, q = R.sample([2, 3, 5, 6, 7, 10, 11, 13, 14, 15], 2)
    ok = f"{p + q} + 2√{p * q}" if math.isqrt(p * q) ** 2 != p * q else str(p + q + 2 * math.isqrt(p * q))
    b.add(f"(√{p} + √{q})² = কত?", ok, W(ok, [str(p + q), f"{p + q} − 2√{p * q}", f"{p * q} + 2√{p + q}", f"{p + q} + √{p * q}"]), "", lv)
def a1_period(b, lv):
    p = R.choice([3, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101])
    k, x = 1, 10 % p
    while x != 1: x = x * 10 % p; k += 1
    a = R.randint(1, p - 1)
    b.add(f"{a}/{p} কে দশমিকে প্রকাশ করলে আবৃত্ত অংশে কয়টি অঙ্ক থাকবে?", k, W(k, [k + 1, k - 1 if k > 1 else k + 2, p - 1 if p - 1 != k else k + 3, 2 * k]), "10ᵏ ≡ 1 (mod p)-এর ক্ষুদ্রতম k।", lv)
def a1_primes(b, lv):
    a = R.randint(1, 150); c = a + R.randint(10, 40)
    n = sum(1 for p in PR if a < p < c)
    b.add(f"{a} ও {c}-এর মাঝে কয়টি মৌলিক সংখ্যা আছে?", n, W(n, [n + 1, n - 1 if n else 2, n + 2, n + 3]), "", lv)
def a1_rat(b, lv):
    a, c = R.sample(range(2, 40), 2)
    if math.isqrt(a) ** 2 == a or math.isqrt(c) ** 2 == c: return
    a, c = max(a, c), min(a, c)
    ok = f"(√{a} + √{c})/{a - c}".replace('/1', '') if a - c != 1 else f"√{a} + √{c}"
    b.add(f"1/(√{a} − √{c})-এর হরকে মূলদ করলে কোনটি পাওয়া যায়?", ok, W(ok, [f"(√{a} − √{c})/{a - c}", f"(√{a} + √{c})/{a + c}", f"√{a} − √{c}", f"(√{a} + √{c})/{a * c}"]), "লব ও হরকে (√a + √b) দিয়ে গুণ।", lv)
def a1_sumrec(b, lv):
    x, y = R.randint(1, 8), R.randint(1, 8)
    v = F(x + y, 9)
    b.add(f"0.{x}{x}{x}… + 0.{y}{y}{y}… = কত?", fr(v), W(fr(v), [fr(F(x + y, 10)), fr(F(x + y, 99)), fr(v + F(1, 9)), f"0.{x + y}"]), "a/9 + b/9।", lv)
def a1_between(b, lv):
    n = R.randint(2, 99)
    if math.isqrt(n) ** 2 == n: return
    r = math.isqrt(n)
    ok = f"{r} ও {r + 1}"
    b.add(f"√{n} কোন দুটি ক্রমিক পূর্ণসংখ্যার মাঝে অবস্থিত?", ok, W(ok, [f"{r - 1} ও {r}", f"{r + 1} ও {r + 2}", f"{n // 2} ও {n // 2 + 1}", f"{r} ও {r + 2}"]), f"{r}² = {r * r} < {n} < {(r + 1) ** 2}।", lv)
part('c10', '1', None, [], [a1_class, a1_term, a1_rec2, a1_surdadd, a1_between], [a1_mixed, a1_conj, a1_sqsum, a1_period, a1_primes, a1_rat], [a1_sumrec, a1_period, a1_rat])

# ---------------------------------------------------------------- c10 অধ্যায় 10: দূরত্ব ও উচ্চতা
def h10_ht(b, lv):
    d = R.randint(5, 300); a = R.choice([30, 45, 60]); t = R.choice(['টাওয়ার', 'গাছ', 'খুঁটি', 'দালান', 'মিনার'])
    ok = {30: f"{fr(F(d, 3))}√3" if d % 3 else f"{d // 3}√3", 45: str(d), 60: f"{d}√3"}[a] + ' মিটার'
    if a == 30 and d % 3: ok = f"{d}/√3 মিটার"
    b.add(f"একটি {t}ের পাদদেশ থেকে {d} মিটার দূরের একটি বিন্দুতে এর শীর্ষের উন্নতি কোণ {a}°। {t}টির উচ্চতা কত?", ok, W(ok, [f"{d}√3 মিটার", f"{d}/√3 মিটার", f"{d} মিটার", f"{2 * d} মিটার", f"{d}√2 মিটার"]), "উচ্চতা = দূরত্ব × tan θ।", lv)
def h10_ladder(b, lv):
    L = R.randint(2, 60) * 2; a = R.choice([30, 60, 45])
    t = R.choice(['উচ্চতা', 'দূরত্ব'])
    hv = {30: str(L // 2), 60: f"{L // 2}√3", 45: f"{L // 2}√2"}[a]
    dv = {30: f"{L // 2}√3", 60: str(L // 2), 45: f"{L // 2}√2"}[a]
    ok = (hv if t == 'উচ্চতা' else dv) + ' মিটার'
    b.add(f"{L} মিটার লম্বা একটি মই দেয়ালে হেলান দিয়ে মাটির সাথে {a}° কোণ উৎপন্ন করে। মইয়ের পাদদেশ থেকে দেয়ালের {('যে উচ্চতায় মইটি পৌঁছায় তা' if t == 'উচ্চতা' else 'দূরত্ব')} কত?", ok, W(ok, [hv + ' মিটার', dv + ' মিটার', f"{L} মিটার", f"{L}√3 মিটার"]), "sin ও cos ব্যবহার।", lv)
def h10_shadow(b, lv):
    hgt = R.randint(2, 80); a = R.choice([30, 45, 60])
    ok = {30: f"{hgt}√3", 45: str(hgt), 60: f"{hgt}/√3"}[a] + ' মিটার'
    b.add(f"সূর্যের উন্নতি কোণ {a}° হলে {hgt} মিটার উঁচু একটি খুঁটির ছায়ার দৈর্ঘ্য কত?", ok, W(ok, [f"{hgt}√3 মিটার", f"{hgt} মিটার", f"{hgt}/√3 মিটার", f"{2 * hgt} মিটার"]), "ছায়া = উচ্চতা/tan θ।", lv)
part('c10', '10', None, [], [h10_ht, h10_shadow], [h10_ht, h10_ladder, h10_shadow], [h10_ladder])

# ---------------------------------------------------------------- c10 14.3 প্রতিসমতা
SHAPES = [('বর্গ', 4, 4), ('আয়ত', 2, 2), ('রম্বস', 2, 2), ('সামান্তরিক', 0, 2), ('সমবাহু ত্রিভুজ', 3, 3), ('সমদ্বিবাহু ত্রিভুজ', 1, 1), ('বিষমবাহু ত্রিভুজ', 0, 1), ('ঘুড়ি', 1, 1), ('অর্ধবৃত্ত', 1, 1), ('সমদ্বিবাহু ট্রাপিজিয়াম', 1, 1)]
NG = {3: 'ত্রিভুজ', 4: 'চতুর্ভুজ', 5: 'পঞ্চভুজ', 6: 'ষড়ভুজ', 7: 'সপ্তভুজ', 8: 'অষ্টভুজ', 9: 'নবভুজ', 10: 'দশভুজ', 12: 'দ্বাদশভুজ'}
def ngon(n): return f"সুষম {NG[n]}" if n in NG else f"{n} বাহুবিশিষ্ট সুষম বহুভুজ"
def s14_lines(b, lv):
    n = R.randint(3, 40)
    b.add(f"{ngon(n)}-এর প্রতিসাম্য রেখা কয়টি?", n, W(n, [n - 1, n + 1, 2 * n, n // 2]), "সুষম n-ভুজের n টি প্রতিসাম্য রেখা।", lv)
def s14_order(b, lv):
    n = R.randint(3, 40)
    b.add(f"{ngon(n)}-এর ঘূর্ণন প্রতিসাম্যের মাত্রা কত?", n, W(n, [n - 1, n + 1, 2 * n, 1]), "", lv)
def s14_angle(b, lv):
    n = R.choice([d for d in range(3, 73) if 360 % d == 0])
    v = 360 // n
    b.add(f"{ngon(n)}-কে ক্ষুদ্রতম কত ডিগ্রি ঘোরালে আগের অবস্থানের মতো দেখায়?", f"{v}°", W(f"{v}°", [f"{2 * v}°", f"{180 // n if 180 % n == 0 else v + 10}°", f"{360 - v}°", f"{v + 5}°"]), "360°/n।", lv)
def s14_shape(b, lv):
    s, l, o = R.choice(SHAPES); t = R.choice(['রেখা', 'মাত্রা'])
    v = l if t == 'রেখা' else o
    q = f"একটি {s}-এর প্রতিসাম্য রেখা কয়টি?" if t == 'রেখা' else f"একটি {s}-এর ঘূর্ণন প্রতিসাম্যের মাত্রা কত?"
    b.add(q, v, W(v, [0, 1, 2, 3, 4, 6]), "", lv)
def s14_fromang(b, lv):
    n = R.choice([d for d in range(3, 73) if 360 % d == 0]); v = 360 // n
    b.add(f"একটি সুষম বহুভুজের ক্ষুদ্রতম ঘূর্ণন কোণ {v}° হলে এর বাহু কয়টি?", n, W(n, [n + 1, n - 1, 2 * n, v]), "n = 360°/θ।", lv)
def s14_sum(b, lv):
    n1, n2 = R.sample(range(3, 21), 2)
    v = n1 + n2
    b.add(f"{ngon(n1)} ও {ngon(n2)}-এর মোট প্রতিসাম্য রেখা কয়টি?", v, W(v, [v + 1, v - 1, n1 * n2, v + 2]), "", lv)
def s14_mix(b, lv):
    n = R.randint(3, 30)
    b.add(f"{ngon(n)}-এর প্রতিসাম্য রেখার সংখ্যা ও ঘূর্ণন প্রতিসাম্যের মাত্রার যোগফল কত?", 2 * n, W(2 * n, [n, 2 * n + 1, n + 1, 2 * n - 2]), "", lv)
part('c10', '14', '14.3', [], [s14_lines, s14_order, s14_shape], [s14_angle, s14_fromang, s14_sum, s14_shape], [s14_mix, s14_sum])

# ---------------------------------------------------------------- c10 16.3 বৃত্ত সংক্রান্ত পরিমাপ
def c16_arc(b, lv):
    r = R.randint(2, 50); th = R.choice([30, 45, 60, 90, 120, 135, 150, 180, 210, 240, 270, 300])
    v = F(th, 180) * r
    ok = f"{fr(v)}π সেমি".replace('1π', 'π') if v != 1 else 'π সেমি'
    b.add(f"{r} সেমি ব্যাসার্ধের বৃত্তে {th}° কেন্দ্রস্থ কোণ উৎপন্নকারী বৃত্তচাপের দৈর্ঘ্য কত?", ok, W(ok, [f"{fr(v * 2)}π সেমি", f"{fr(v / 2)}π সেমি", f"{fr(F(th, 360) * r * r)}π সেমি", f"{fr(v + 1)}π সেমি"]), "s = (θ/180°)πr।", lv)
def c16_sector(b, lv):
    r = R.randint(2, 40); th = R.choice([30, 45, 60, 90, 120, 150, 180, 240, 270])
    v = F(th, 360) * r * r
    ok = f"{fr(v)}π বর্গ সেমি"
    b.add(f"{r} সেমি ব্যাসার্ধের বৃত্তের {th}° কোণের বৃত্তকলার ক্ষেত্রফল কত?", ok, W(ok, [f"{fr(v * 2)}π বর্গ সেমি", f"{fr(F(th, 180) * r)}π বর্গ সেমি", f"{fr(v / 2)}π বর্গ সেমি", f"{fr(v + 1)}π বর্গ সেমি"]), "(θ/360°)πr²।", lv)
part('c10', '16', '16.3', [], [c16_arc], [c16_arc, c16_sector], [c16_sector])

# ---------------------------------------------------------------- c10 2.2 অন্বয় ও ফাংশন
def f22_val(b, lv):
    a, c, k = nz(-9, 9), R.randint(-15, 15), R.randint(-12, 12)
    v = a * k + c
    b.add(f"f(x) = {px({1: a, 0: c})} হলে f({num(k)}) = কত?", num(v), W(num(v), [num(a * k - c), num(a + k + c), num(-v) if v else '1', num(v + a)]), "", lv)
def f22_dom(b, lv):
    xs = R.sample(range(-9, 10), R.randint(3, 5)); pairs = [(x, R.randint(-9, 9)) for x in xs]
    t = R.choice(['ডোমেন', 'রেঞ্জ'])
    vals = sorted(set(p[0] if t == 'ডোমেন' else p[1] for p in pairs)); oth = sorted(set(p[1] if t == 'ডোমেন' else p[0] for p in pairs))
    S = lambda v: '{' + ', '.join(num(x) for x in v) + '}'
    if vals == oth: return
    b.add(f"S = {{{', '.join(f'({num(a)}, {num(c)})' for a, c in pairs)}}} অন্বয়ের {t} কোনটি?", S(vals), W(S(vals), [S(oth), S(vals[:-1]) if len(vals) > 1 else '∅', S(sorted(set(vals + oth)))]), "", lv)
def f22_q(b, lv):
    a, c, d = R.choice([1, 2, 3]), R.randint(-6, 6), R.randint(-6, 6); k = R.randint(-6, 6)
    v = a * k * k + c * k + d
    b.add(f"f(x) = {px({2: a, 1: c, 0: d})} হলে f({num(k)}) = কত?", num(v), W(num(v), [num(a * k * k - c * k + d), num(v + 1), num(a * k + c * k + d), num(-v) if v else '2']), "", lv)
part('c10', '2', '2.2', [], [f22_val, f22_dom, f22_q], [f22_q], [f22_q])

# ---------------------------------------------------------------- c10 4.1, 4.2
def e41h(b, lv):
    base = R.choice([2, 3, 5, 7]); m = R.randint(2, 9); k = R.randint(1, 5)
    # base^(x+k) = base^m ⇒ x = m − k ; লিখি সংখ্যায়
    v = base ** m
    b.add(f"{base}^(x + {k}) = {v} হলে x = কত?", m - k, W(m - k, [m + k, m, m - k + 1, k]), f"{v} = {base}{sup(m)}।", lv)
def e41h2(b, lv):
    a = R.choice([2, 3, 4, 5]); p, q = R.randint(2, 6), R.randint(1, 5)
    v = F(a ** (p + q) , a ** p) if True else 0
    b.add(f"({a}{sup(p)} × {a}{sup(q)}) ÷ {a}{sup(p + q - 1)} = কত?", a, W(a, [a * a, 1, a ** (p + q), a + 1]), "সূচকের নিয়ম।", lv)
part('c10', '4', '4.1', [], [], [], [e41h, e41h2])
def l42e(b, lv):
    base = R.choice([2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]); k = R.randint(-4, 6)
    v = F(base) ** k
    arg = fr(v)
    b.add(f"log_{base} ({arg}) = কত?", num(k), W(num(k), [num(k + 1), num(-k) if k else '1', num(k - 1), str(base)]), f"{base}^{num(k)} = {arg}।", lv)
def l42root(b, lv):
    base = R.choice([2, 3, 5, 7]); k = R.randint(1, 8)
    v = base ** k
    b.add(f"log_√{base} ({v}) = কত?", 2 * k, W(2 * k, [k, k // 2 if k > 1 else 3, 2 * k + 1, base]), f"(√{base})^{2 * k} = {v}।", lv)
part('c10', '4', '4.2', [], [l42e, l42root], [], [])

# ---------------------------------------------------------------- c10 8.1 জ্যা, 8.5 সম্পাদ্য
def ch81_len(b, lv):
    p, q, r = tri(); k = R.randint(1, 4)
    b.add(f"{r * k} সেমি ব্যাসার্ধের বৃত্তের কেন্দ্র থেকে একটি জ্যা-এর লম্ব দূরত্ব {p * k} সেমি হলে জ্যাটির দৈর্ঘ্য কত?", f"{2 * q * k} সেমি", W(f"{2 * q * k} সেমি", [f"{q * k} সেমি", f"{2 * p * k} সেমি", f"{2 * r * k} সেমি", f"{(q + 1) * k * 2} সেমি"]), "জ্যা = 2√(r² − d²)।", lv)
def ch81_dist(b, lv):
    p, q, r = tri(); k = R.randint(1, 4)
    b.add(f"{r * k} সেমি ব্যাসার্ধের বৃত্তে {2 * q * k} সেমি দৈর্ঘ্যের জ্যা-এর কেন্দ্র থেকে দূরত্ব কত?", f"{p * k} সেমি", W(f"{p * k} সেমি", [f"{q * k} সেমি", f"{2 * p * k} সেমি", f"{r * k - q * k if r > q else p * k + 1} সেমি", f"{(p + 1) * k} সেমি"]), "d = √(r² − (জ্যা/2)²)।", lv)
def ch81_rad(b, lv):
    p, q, r = tri(); k = R.randint(1, 4)
    b.add(f"একটি বৃত্তের {2 * q * k} সেমি দৈর্ঘ্যের জ্যা কেন্দ্র থেকে {p * k} সেমি দূরে অবস্থিত। বৃত্তের ব্যাসার্ধ কত?", f"{r * k} সেমি", W(f"{r * k} সেমি", [f"{(p + q) * k} সেমি", f"{2 * r * k} সেমি", f"{q * k} সেমি", f"{(r + 1) * k} সেমি"]), "r² = d² + (জ্যা/2)²।", lv)
def ch81_dia(b, lv):
    r = R.randint(2, 60)
    b.add(f"{r} সেমি ব্যাসার্ধের বৃত্তের বৃহত্তম জ্যা-এর দৈর্ঘ্য কত?", f"{2 * r} সেমি", W(f"{2 * r} সেমি", [f"{r} সেমি", f"{r * r} সেমি", f"{3 * r} সেমি"]), "ব্যাস বৃহত্তম জ্যা।", lv)
def ch81_two(b, lv):
    (p1, q1, r1) = R.choice(TRI)
    alts = [t for t in TRI if t[2] == r1 and t != (p1, q1, r1)]
    k = R.randint(1, 3)
    # একই বৃত্তে দুটি সমান্তরাল জ্যা: কেন্দ্র থেকে দূরত্ব p1, q1 (দৈর্ঘ্য 2q1, 2p1)
    side = R.choice(['একই', 'বিপরীত'])
    v = abs(q1 - p1) * k if side == 'একই' else (p1 + q1) * k
    b.add(f"{r1 * k} সেমি ব্যাসার্ধের বৃত্তে {2 * q1 * k} সেমি ও {2 * p1 * k} সেমি দৈর্ঘ্যের দুটি সমান্তরাল জ্যা কেন্দ্রের {side} পাশে আছে। জ্যাদ্বয়ের দূরত্ব কত?", f"{v} সেমি", W(f"{v} সেমি", [f"{(p1 + q1) * k if side == 'একই' else abs(q1 - p1) * k} সেমি", f"{r1 * k} সেমি", f"{v + k} সেমি"]), "কেন্দ্র থেকে দূরত্ব দুটির যোগ/বিয়োগ।", lv)
part('c10', '8', '8.1', [], [ch81_len, ch81_dist, ch81_dia], [ch81_len, ch81_dist, ch81_rad, ch81_two], [ch81_two])
def c85_circ(b, lv):
    p, q, r = tri(); k = R.randint(1, 5)
    t = R.choice(['পরি', 'অন্ত'])
    v = F(r * k, 2) if t == 'পরি' else F((p + q - r) * k, 2)
    b.add(f"একটি সমকোণী ত্রিভুজের বাহুগুলো {p * k}, {q * k} ও {r * k} সেমি। এর {t}বৃত্তের ব্যাসার্ধ কত?", f"{fr(v)} সেমি", W(f"{fr(v)} সেমি", [f"{fr(F(r * k, 2) if t == 'অন্ত' else F((p + q - r) * k, 2))} সেমি", f"{r * k} সেমি", f"{fr(v + 1)} সেমি", f"{fr(F(p * q * k, p + q + r))} সেমি" if t == 'পরি' else f"{fr(v * 2)} সেমি"]), "পরিব্যাসার্ধ = অতিভুজ/2, অন্তর্ব্যাসার্ধ = (a + b − c)/2।", lv)
def c85_tan(b, lv):
    p, q, r = tri(); k = R.randint(1, 5)
    b.add(f"{p * k} সেমি ব্যাসার্ধের বৃত্তের কেন্দ্র থেকে {r * k} সেমি দূরের একটি বিন্দু থেকে অঙ্কিত স্পর্শকের দৈর্ঘ্য কত?", f"{q * k} সেমি", W(f"{q * k} সেমি", [f"{(r - p) * k} সেমি", f"{(r + p) * k} সেমি", f"{r * k} সেমি", f"{(q + 1) * k} সেমি"]), "√(d² − r²)।", lv)
def c85_eq(b, lv):
    a = R.randint(1, 30) * 3; t = R.choice(['পরি', 'অন্ত'])
    ok = (f"{a // 3}√3" if t == 'পরি' else f"{fr(F(a, 6))}√3") + ' সেমি'
    b.add(f"{a} সেমি বাহুবিশিষ্ট সমবাহু ত্রিভুজের {t}বৃত্তের ব্যাসার্ধ কত?", ok, W(ok, [f"{a // 3}√3 সেমি", f"{fr(F(a, 6))}√3 সেমি", f"{a}√3 সেমি", f"{fr(F(a, 2))} সেমি"]), "R = a/√3, r = a/(2√3)।", lv)
def c85_common(b, lv):
    r1, r2 = R.randint(1, 15), R.randint(1, 15)
    case = R.choice(['far', 'ext', 'cut', 'int', 'in'])
    if r1 == r2 and case in ('int', 'in'): return
    d = {'far': r1 + r2 + R.randint(1, 10), 'ext': r1 + r2, 'cut': abs(r1 - r2) + R.randint(1, max(1, r1 + r2 - abs(r1 - r2) - 1)), 'int': abs(r1 - r2), 'in': R.randint(0, max(0, abs(r1 - r2) - 1))}[case]
    if case == 'cut' and not (abs(r1 - r2) < d < r1 + r2): return
    if case == 'in' and (d >= abs(r1 - r2) or abs(r1 - r2) == 0): return
    n = {'far': 4, 'ext': 3, 'cut': 2, 'int': 1, 'in': 0}[case]
    b.add(f"দুটি বৃত্তের ব্যাসার্ধ {r1} সেমি ও {r2} সেমি এবং কেন্দ্রদ্বয়ের দূরত্ব {d} সেমি। এদের সাধারণ স্পর্শক কয়টি?", n, W(n, [0, 1, 2, 3, 4]), "দূরত্ব ও ব্যাসার্ধের তুলনা।", lv)
def c85_pt(b, lv):
    r = R.randint(2, 30); d = R.randint(1, 60); n = 2 if d > r else (1 if d == r else 0)
    b.add(f"{r} সেমি ব্যাসার্ধের বৃত্তের কেন্দ্র থেকে {d} সেমি দূরের বিন্দু থেকে বৃত্তে কয়টি স্পর্শক আঁকা যায়?", n, W(n, [0, 1, 2, 3]), "", lv)
part('c10', '8', '8.5', [], [c85_pt, c85_tan, c85_circ], [c85_circ, c85_tan, c85_eq, c85_common], [c85_common, c85_eq])

# ---------------------------------------------------------------- c10 9.1, 9.2
def t91h(b, lv):
    p, q, r = tri()
    f, g = R.choice([('sec θ + tan θ', F(r + p, q)), ('sec θ − tan θ', F(r - p, q)), ('cosec θ + cot θ', F(r + q, p)), ('cosec θ − cot θ', F(r - q, p)), ('sin θ + cos θ', F(p + q, r)), ('tan θ + cot θ', F(p * p + q * q, p * q))])
    b.add(f"sin θ = {fr(F(p, r))} (θ সূক্ষ্মকোণ) হলে {f} = কত?", fr(g), W(fr(g), [fr(1 / g), fr(g + 1), fr(F(p, q)), fr(F(r, p))]), f"cos θ = {fr(F(q, r))}, tan θ = {fr(F(p, q))}।", lv)
part('c10', '9', '9.1', [], [], [], [t91h])
SV = {0: (F(0), F(1)), 30: (F(1, 2), None), 45: (None, None), 60: (None, F(1, 2)), 90: (F(1), F(0))}
SQ = {'sin': {0: F(0), 30: F(1, 4), 45: F(1, 2), 60: F(3, 4), 90: F(1)}, 'cos': {0: F(1), 30: F(3, 4), 45: F(1, 2), 60: F(1, 4), 90: F(0)}, 'tan': {0: F(0), 30: F(1, 3), 45: F(1), 60: F(3)}}
def t92h(b, lv):
    terms = []; v = F(0)
    for _ in range(3):
        f = R.choice(['sin', 'cos', 'tan']); a = R.choice(list(SQ[f])); c = R.randint(1, 4)
        terms.append(f"{c if c > 1 else ''}{f}²{a}°"); v += c * SQ[f][a]
    b.add(f"{' + '.join(terms)} = কত?", fr(v), W(fr(v), [fr(v + 1), fr(v - F(1, 2)), fr(v * 2), fr(v + F(1, 4))]), "বর্গের মান বসিয়ে।", lv)
part('c10', '9', '9.2', [], [], [], [t92h])

# ---------------------------------------------------------------- ত্রিকোণমিতিক সমীকরণ (ডিগ্রিতে) — c10h 8.3
SD = {'sin': {'1/2': [30, 150], '1/√2': [45, 135], '√3/2': [60, 120], '1': [90], '0': [0, 180, 360], '−1/2': [210, 330], '−√3/2': [240, 300], '−1': [270]},
      'cos': {'1/2': [60, 300], '1/√2': [45, 315], '√3/2': [30, 330], '1': [0, 360], '0': [90, 270], '−1/2': [120, 240], '−√3/2': [150, 210], '−1': [180]},
      'tan': {'1': [45, 225], '√3': [60, 240], '1/√3': [30, 210], '0': [0, 180, 360], '−1': [135, 315], '−√3': [120, 300]}}
def tq_sol(b, lv):
    f = R.choice(list(SD)); v = R.choice(list(SD[f])); sols = SD[f][v]
    ok = ', '.join(f"{s}°" for s in sols)
    other = R.choice([x for x in SD[f] if x != v])
    b.add(f"0° ≤ θ ≤ 360° হলে {f} θ = {v} সমীকরণের সমাধান কোনটি?", ok, W(ok, [', '.join(f"{s}°" for s in SD[f][other]), f"{sols[0]}°", ', '.join(f"{(s + 90) % 360}°" for s in sols), ', '.join(f"{360 - s if s else 180}°" for s in sols[:1]) + (', 180°' if len(sols) == 1 else '')]), "", lv)
def tq_acute(b, lv):
    f = R.choice(['sin', 'cos', 'tan']); v = R.choice([x for x in SD[f] if not x.startswith('−') and SD[f][x][0] not in (0, 360) and SD[f][x][0] < 90])
    a = SD[f][v][0]; k = R.randint(2, 9)
    num_ = {'1/2': (k, 2 * k, f"{2 * k} {f} θ = {k}"), '1': (k, k, f"{k} {f} θ = {k}"), '√3': (k, k, f"{k} {f} θ = {k}√3"), '1/√3': (k, k, f"{k}√3 {f} θ = {k}"), '1/√2': (k, k, f"{k}√2 {f} θ = {k}"), '√3/2': (k, k, f"{2 * k} {f} θ = {k}√3")}
    if v not in num_: return
    q = num_[v][2]
    b.add(f"{q} হলে সূক্ষ্মকোণ θ = কত?", f"{a}°", W(f"{a}°", ['30°', '45°', '60°', '90°', '0°']), "", lv)
def tq_sq(b, lv):
    f = R.choice(['sin', 'cos', 'tan'])
    v, ans = R.choice({'sin': [('1/4', '30°'), ('1/2', '45°'), ('3/4', '60°')], 'cos': [('1/4', '60°'), ('1/2', '45°'), ('3/4', '30°')], 'tan': [('1/3', '30°'), ('1', '45°'), ('3', '60°')]}[f])
    k = R.randint(1, 6)
    q = f"{k if k > 1 else ''}{f}²θ = {fr(F(v) * k) if '/' in v or v.isdigit() else v}"
    b.add(f"{q} হলে সূক্ষ্মকোণ θ = কত?", ans, W(ans, ['30°', '45°', '60°', '90°']), "", lv)
def tq_cnt(b, lv):
    f = R.choice(list(SD)); v = R.choice(list(SD[f])); n = len(SD[f][v])
    b.add(f"0° ≤ θ ≤ 360° ব্যবধিতে {f} θ = {v} সমীকরণের কয়টি সমাধান আছে?", n, W(n, [1, 2, 3, 4]), "", lv)
def tq_quad(b, lv):
    c = R.choice([('2sin²θ − sin θ = 0', '0°, 30°, 150°, 180°, 360°'), ('2cos²θ − cos θ = 0', '60°, 90°, 270°, 300°'), ('tan²θ − tan θ = 0', '0°, 45°, 180°, 225°, 360°'), ('2sin²θ = sin θ', '0°, 30°, 150°, 180°, 360°'), ('sin θ cos θ = 0', '0°, 90°, 180°, 270°, 360°'), ('2cos²θ = 1', '45°, 135°, 225°, 315°'), ('4sin²θ = 3', '60°, 120°, 240°, 300°'), ('tan²θ = 3', '60°, 120°, 240°, 300°'), ('3tan²θ = 1', '30°, 150°, 210°, 330°'), ('4cos²θ = 1', '60°, 120°, 240°, 300°'), ('2sin²θ = 1', '45°, 135°, 225°, 315°'), ('cos²θ = 1', '0°, 180°, 360°')])
    pool = ['0°, 30°, 150°, 180°, 360°', '60°, 90°, 270°, 300°', '0°, 45°, 180°, 225°, 360°', '0°, 90°, 180°, 270°, 360°', '45°, 135°, 225°, 315°', '60°, 120°, 240°, 300°', '30°, 150°, 210°, 330°', '0°, 180°, 360°']
    b.add(f"0° ≤ θ ≤ 360° হলে {c[0]} সমীকরণের সমাধান কোনটি?", c[1], W(c[1], R.sample(pool, 5)), "উৎপাদকে বিশ্লেষণ।", lv)
part('c10h', '8', '8.3', [], [tq_sol, tq_acute, tq_cnt, tq_sq], [tq_sol, tq_acute, tq_sq, tq_quad, tq_cnt], [tq_quad])

# ---------------------------------------------------------------- c10h 9.1 মূলদ সূচক (কঠিন)
def r91h(b, lv):
    base, m = R.choice([(2, 'x'), (3, 'x'), (4, 'x'), (8, 'x'), (9, 'x'), (16, 'x'), (25, 'x'), (27, 'x'), (32, 'x'), (64, 'x'), (81, 'x'), (125, 'x')])
    roots = {2: 2, 3: 3, 4: 2, 8: 2, 9: 3, 16: 2, 25: 5, 27: 3, 32: 2, 64: 2, 81: 3, 125: 5}
    p0 = roots[base]; e = round(math.log(base, p0))
    nn = R.choice([d for d in (1, 2, 3, 4, 5, 6) if e % d == 0 or True])
    pp = R.randint(-4, 4)
    if pp == 0: return
    ex = F(pp, nn)
    if (e * ex).denominator != 1: return
    v = F(p0) ** int(e * ex)
    b.add(f"({base})^({num(ex)}) = কত?", fr(v), W(fr(v), [fr(1 / v), fr(v * p0), fr(F(base) * ex) if F(base) * ex != v else fr(v + 1), fr(-v)]), f"{base} = {p0}{sup(e)}।", lv)
part('c10h', '9', '9.1', [], [], [], [r91h])

# ---------------------------------------------------------------- h11 5.A বিন্যাস
def p5_npr(b, lv):
    n = R.randint(3, 20); r = R.randint(1, min(4, n))
    v = math.perm(n, r)
    b.add(f"{n}P{r}-এর মান কত?", v, W(v, [math.comb(n, r), math.perm(n, r - 1) if r > 1 else n + 1, v * 2, n ** r]), "n!/(n − r)!।", lv)
def p5_line(b, lv):
    n = R.randint(3, 9); t = R.choice(['বই', 'ছাত্র', 'চেয়ার', 'পতাকা', 'খেলনা'])
    v = math.factorial(n)
    b.add(f"{n}টি ভিন্ন {t} একটি সারিতে কত প্রকারে সাজানো যায়?", v, W(v, [math.factorial(n - 1), n * n, 2 ** n, v // 2]), "n!।", lv)
def p5_digits(b, lv):
    n = R.randint(4, 9); r = R.randint(2, min(4, n))
    v = math.perm(n, r)
    b.add(f"{n}টি ভিন্ন অশূন্য অঙ্ক থেকে (পুনরাবৃত্তি ছাড়া) {r} অঙ্কের কতগুলো সংখ্যা গঠন করা যায়?", v, W(v, [math.comb(n, r), n ** r, math.perm(n, r - 1), v + n]), "ⁿPᵣ।", lv)
WORDS = ['BANANA', 'APPLE', 'COMMITTEE', 'MATHEMATICS', 'STATISTICS', 'PEPPER', 'LETTER', 'BALLOON', 'SUCCESS', 'ENGINEERING', 'MISSISSIPPI', 'ASSASSINATION', 'DHAKA', 'BANGLADESH', 'CALCULUS', 'ALGEBRA', 'GEOMETRY', 'PARALLEL', 'TOMATO', 'COFFEE', 'CHITTAGONG', 'RAJSHAHI', 'SYLHET', 'KHULNA', 'BARISAL', 'RANGPUR', 'NARAYANGANJ', 'MYMENSINGH', 'COMILLA', 'EXAMINATION', 'PERMUTATION', 'COMBINATION', 'PROBABILITY', 'TRIANGLE', 'DIFFERENTIATION', 'INTEGRATION']
def p5_word(b, lv):
    w = R.choice(WORDS); from collections import Counter
    c = Counter(w); v = math.factorial(len(w))
    for k in c.values(): v //= math.factorial(k)
    b.add(f"'{w}' শব্দটির সবগুলো অক্ষর একত্রে নিয়ে কত প্রকারে সাজানো যায়?", v, W(v, [math.factorial(len(w)), v * 2, v // 2 if v > 2 else v + 3, math.factorial(len(set(w)))]), "পুনরাবৃত্ত অক্ষরের ফ্যাক্টোরিয়াল দিয়ে ভাগ।", lv)
def p5_circ(b, lv):
    n = R.randint(3, 10); t = R.choice(['ব্যক্তি', 'অতিথি', 'শিক্ষার্থী'])
    v = math.factorial(n - 1)
    b.add(f"{n} জন {t}কে একটি গোল টেবিলের চারপাশে কত প্রকারে বসানো যায়?", v, W(v, [math.factorial(n), v // 2 if v > 1 else 2, n * n, v * 2]), "(n − 1)!।", lv)
def p5_vowel(b, lv):
    w = R.choice(['EQUATION', 'ORANGE', 'DAUGHTER', 'FAILURE', 'EDUCATION', 'MONDAY', 'SUNDAY', 'TRIANGLE', 'NUMBER', 'PENCIL', 'MOTHER', 'FATHER', 'GARDEN', 'FRIEND', 'SCHOOL', 'COUNTRY', 'PLANET'])
    if len(set(w)) != len(w): return
    vw = [ch for ch in w if ch in 'AEIOU']; n = len(w); k = len(vw)
    v = math.factorial(n - k + 1) * math.factorial(k)
    b.add(f"'{w}' শব্দটির অক্ষরগুলোকে কত প্রকারে সাজানো যায় যাতে স্বরবর্ণগুলো সর্বদা একত্রে থাকে?", v, W(v, [math.factorial(n), math.factorial(n - k + 1), math.factorial(n) - v, v * 2]), f"স্বরবর্ণ {k}টিকে একটি একক ধরে।", lv)
part('h11', '5', '5.A', [], [p5_npr, p5_line, p5_digits, p5_circ], [], [p5_word, p5_vowel])

# ---------------------------------------------------------------- h11 6.A কোণ পরিমাপ
def a6_rad(b, lv):
    d = R.choice([x for x in range(5, 721, 5)])
    v = F(d, 180)
    b.add(f"{d}° = কত রেডিয়ান?", piF(v), W(piF(v), [piF(v * 2), piF(v / 2), piF(F(180, d)) if d != 180 else 'π/2', piF(v + F(1, 6))]), "×π/180।", lv)
part('h11', '6', '6.A', [], [a6_rad], [], [])

# ---------------------------------------------------------------- h11 7.B–7.G
def frs(x): return fr(x)
def c7b_tan(b, lv):
    a, c = F(R.randint(1, 9), R.randint(1, 9)), F(R.randint(1, 9), R.randint(1, 9))
    if a * c == 1: return
    v = (a + c) / (1 - a * c)
    b.add(f"tan A = {fr(a)} ও tan B = {fr(c)} হলে tan(A + B) = কত?", fr(v), W(fr(v), [fr(a + c), fr((a - c) / (1 + a * c)), fr((a + c) / (1 + a * c)), fr(-v)]), "(tan A + tan B)/(1 − tan A tan B)।", lv)
part('h11', '7', '7.B', [], [], [], [c7b_tan])
def c7c(b, lv):
    p, q, r = tri(); f = R.choice(['sin 2A', 'cos 2A', 'tan 2A', 'sin 3A', 'cos 3A'])
    s, c = F(p, r), F(q, r)
    v = {'sin 2A': 2 * s * c, 'cos 2A': c * c - s * s, 'tan 2A': (2 * s / c) / (1 - (s / c) ** 2) if s != c else None, 'sin 3A': 3 * s - 4 * s ** 3, 'cos 3A': 4 * c ** 3 - 3 * c}[f]
    if v is None: return
    given = R.choice([('sin A', s), ('cos A', c), ('tan A', s / c)])
    b.add(f"A সূক্ষ্মকোণ ও {given[0]} = {fr(given[1])} হলে {f} = কত?", fr(v), W(fr(v), [fr(-v), fr(2 * s), fr(c * c + s * s - 2 * s * s * 0 + s), fr(v + F(1, r))]), f"sin A = {fr(s)}, cos A = {fr(c)}।", lv)
part('h11', '7', '7.C', [], [c7c], [c7c], [c7c])
def c7d(b, lv):
    p, q, r = tri(); c = F(q, r); s = F(p, r)
    f = R.choice(['sin²(A/2)', 'cos²(A/2)', 'tan(A/2)', 'tan²(A/2)'])
    v = {'sin²(A/2)': (1 - c) / 2, 'cos²(A/2)': (1 + c) / 2, 'tan(A/2)': s / (1 + c), 'tan²(A/2)': (1 - c) / (1 + c)}[f]
    b.add(f"A সূক্ষ্মকোণ ও cos A = {fr(c)} হলে {f} = কত?", fr(v), W(fr(v), [fr((1 + c) / 2 if f != 'cos²(A/2)' else (1 - c) / 2), fr(s / (1 - c)) if c != 1 else '1', fr(v * 2) if v * 2 != v else '1', fr(c / 2)]), "অর্ধকোণের সূত্র।", lv)
part('h11', '7', '7.D', [], [c7d], [c7d], [])
def c7f(b, lv):
    while True:
        a, c, d = R.randint(2, 15), R.randint(2, 15), R.randint(2, 15)
        if a + c > d and a + d > c and c + d > a: break
    v = F(a * a + c * c - d * d, 2 * a * c)
    b.add(f"ABC ত্রিভুজে a = {a}, b = {c}, c = {d} হলে cos C = কত?", fr(v), W(fr(v), [fr(F(a * a + d * d - c * c, 2 * a * d)), fr(F(c * c + d * d - a * a, 2 * c * d)), fr(-v) if v else '1/2', fr(F(a * a + c * c + d * d, 2 * a * c))]), "cos C = (a² + b² − c²)/2ab।", lv)
def c7f_area(b, lv):
    a, c = R.randint(2, 20), R.randint(2, 20); ang = R.choice([30, 150, 90])
    v = F(a * c, 4) if ang != 90 else F(a * c, 2)
    b.add(f"ABC ত্রিভুজে a = {a}, b = {c} ও C = {ang}° হলে ক্ষেত্রফল কত বর্গ একক?", fr(v), W(fr(v), [fr(v * 2), fr(F(a * c, 4) if ang == 90 else F(a * c, 2)), fr(a * c), fr(v + 1)]), "½ab sin C।", lv)
part('h11', '7', '7.F', [], [], [], [c7f, c7f_area])
GA = {'sin': {'1/2': F(1, 6), '1/√2': F(1, 4), '√3/2': F(1, 3)}, 'cos': {'1/2': F(1, 3), '1/√2': F(1, 4), '√3/2': F(1, 6)}, 'tan': {'1/√3': F(1, 6), '1': F(1, 4), '√3': F(1, 3)}}
def g7(b, lv):
    f = R.choice(list(GA)); s, a = R.choice(list(GA[f].items())); k = R.choice([1, 2, 3, 4, 5]); neg = R.random() < .4
    th = 'x' if k == 1 else f"{k}x"
    if f == 'sin':
        al = -a if neg else a; ok = f"{th} = nπ + (−1)ⁿ{('(' + piF(al) + ')') if neg else piF(al)}"; ws = [f"{th} = 2nπ ± {piF(a)}", f"{th} = nπ + {piF(a)}", f"{th} = nπ + (−1)ⁿ{piF(F(1, 2) - a)}"]
    elif f == 'cos':
        al = 1 - a if neg else a; ok = f"{th} = 2nπ ± {piF(al)}"; ws = [f"{th} = nπ + (−1)ⁿ{piF(al)}", f"{th} = nπ ± {piF(al)}", f"{th} = 2nπ ± {piF(F(1, 2) - al) if al != F(1, 4) else 'π/3'}"]
    else:
        ok = f"{th} = nπ {'−' if neg else '+'} {piF(a)}"; ws = [f"{th} = 2nπ + {piF(a)}", f"{th} = nπ {'+' if neg else '−'} {piF(a)}", f"{th} = nπ + {piF(F(1, 2) - a)}"]
    b.add(f"{f} {th} = {'−' if neg else ''}{s} হলে x-এর সাধারণ মান কী?", ok, W(ok, ws), "", lv)
def g7_two(b, lv):
    k1, k2 = R.sample(range(1, 8), 2)
    f = R.choice(['sin', 'cos', 'tan'])
    t1 = 'x' if k1 == 1 else f"{k1}x"; t2 = 'x' if k2 == 1 else f"{k2}x"
    def ov(nm, d): return nm if d == 1 else f"{nm}/{d}"
    if f == 'tan': ok = f"x = {ov('nπ', abs(k1 - k2))}"
    elif f == 'cos': ok = f"x = {ov('2nπ', k1 + k2)} অথবা x = {ov('2nπ', abs(k1 - k2))}"
    else: ok = f"x = {ov('2nπ', abs(k1 - k2))} অথবা x = {ov('(2n + 1)π', k1 + k2)}"
    b.add(f"{f} {t1} = {f} {t2} সমীকরণের সাধারণ সমাধান কোনটি?", ok, W(ok, [f"x = nπ/{k1 + k2}", f"x = 2nπ/{k1 * k2}", f"x = nπ/{abs(k1 - k2) + 1}", f"x = (2n + 1)π/{abs(k1 - k2) + k1 + k2}"]), "সমান অনুপাতের সাধারণ সমাধান।", lv)
part('h11', '7', '7.G', [], [g7], [g7, g7_two], [g7_two])

# ---------------------------------------------------------------- h11 9.F, 9.G, 9.H, 9.I
def d9f(b, lv):
    a = nz(-9, 9); c = R.randint(-9, 9)
    t = R.choice(['exp', 'ln', 'asin', 'atan', 'pow', 'log10', 'expx2'])
    ax = co(a, 'x'); inner = px({1: a, 0: c})
    if t == 'exp': q, ok = f"e^({ax})", f"{co(a, '')}e^({ax})".replace('()', '')
    elif t == 'ln': q, ok = f"ln({inner})", f"{num(a)}/({inner})"
    elif t == 'asin':
        a = abs(a); q, ok = f"sin⁻¹({co(a, 'x')})", f"{a}/√(1 − {a * a}x²)".replace('− 1x²', '− x²')
    elif t == 'atan':
        a = abs(a); q, ok = f"tan⁻¹({co(a, 'x')})", f"{a}/(1 + {a * a}x²)".replace('+ 1x²', '+ x²')
    elif t == 'pow':
        k = R.randint(2, 15); q, ok = f"{k}ˣ", f"{k}ˣ ln {k}"
    elif t == 'log10':
        k = R.randint(2, 15); q, ok = f"log_{k} x", f"1/(x ln {k})"
    else:
        q, ok = f"e^(x² {'+' if c >= 0 else '−'} {abs(c)})".replace(' + 0', '').replace(' − 0', ''), f"2x e^(x² {'+' if c >= 0 else '−'} {abs(c)})".replace(' + 0', '').replace(' − 0', '')
    if ok.startswith('1e'): ok = ok[1:]
    if ok.startswith('−1e'): ok = '−' + ok[2:]
    b.add(f"d/dx [{q}] = কত?", ok, W(ok, [q, ok.replace('/', '·') if '/' in ok else ok + ' + 1', '1/' + q if t != 'pow' else f"x·{q}", f"−{ok}" if not ok.startswith('−') else ok[1:]]), "আদর্শ সূত্র ও শৃঙ্খল নিয়ম।", lv)
part('h11', '9', '9.F', [], [d9f], [d9f], [])
def d9g(b, lv):
    t = R.choice(['circ', 'param', 'xy'])
    if t == 'circ':
        p, q, r = tri(); x, y = p, q
        v = F(-x, y)
        b.add(f"x² + y² = {r * r} বক্ররেখার ({x}, {y}) বিন্দুতে dy/dx = কত?", fr(v), W(fr(v), [fr(-v), fr(F(y, x)), fr(F(-y, x)), '0']), "dy/dx = −x/y।", lv)
    elif t == 'param':
        a, tv = R.randint(1, 9), nz(-6, 6)
        v = F(1, tv)
        b.add(f"x = {a}t², y = {2 * a}t হলে t = {num(tv)} বিন্দুতে dy/dx = কত?", fr(v), W(fr(v), [fr(F(tv)), fr(2 * v), fr(-v), fr(F(a, tv))]), "dy/dx = 1/t।", lv)
    else:
        k = nz(-12, 12); x = nz(-6, 6); y = F(k, x)
        v = -y / x
        b.add(f"xy = {num(k)} হলে x = {num(x)} বিন্দুতে dy/dx = কত?", fr(v), W(fr(v), [fr(-v), fr(y), fr(F(x, k)) if k else '1', fr(v * 2)]), "y + x dy/dx = 0।", lv)
part('h11', '9', '9.G', [], [], [], [d9g])
def d9h(b, lv):
    t = R.choice(['pow', 'exp', 'sin', 'cos'])
    a = R.randint(2, 9); n = R.randint(3, 9)
    if t == 'pow': q, ok, w = f"x{sup(n)}", f"{n * (n - 1)}x{sup(n - 2)}".replace('x¹', 'x'), [f"{n}x{sup(n - 1)}", f"{n * (n - 1)}x{sup(n - 1)}", f"{n * n}x{sup(n - 2)}".replace('x¹', 'x')]
    elif t == 'exp': q, ok, w = f"e^({a}x)", f"{a * a}e^({a}x)", [f"{a}e^({a}x)", f"{2 * a}e^({a}x)", f"e^({a}x)"]
    elif t == 'sin': q, ok, w = f"sin {a}x", f"−{a * a} sin {a}x", [f"{a * a} sin {a}x", f"−{a} cos {a}x", f"{a} cos {a}x"]
    else: q, ok, w = f"cos {a}x", f"−{a * a} cos {a}x", [f"{a * a} cos {a}x", f"−{a} sin {a}x", f"{a * a} sin {a}x"]
    b.add(f"y = {q} হলে d²y/dx² = কত?", ok, W(ok, w), "দুবার অন্তরীকরণ।", lv)
def d9h2(b, lv):
    a = R.randint(2, 12); n = R.randint(2, 9); t = R.choice(['cpow', 'ln', 'third', 'expb'])
    if t == 'cpow': q, ok, w = f"{a}x{sup(n)}", f"{a * n * (n - 1)}x{sup(n - 2)}".replace('x¹', 'x').replace('x⁰', ''), [f"{a * n}x{sup(n - 1)}", f"{a * n * n}x{sup(n - 2)}".replace('x¹', 'x').replace('x⁰', ''), f"{n * (n - 1)}x{sup(n - 2)}".replace('x¹', 'x').replace('x⁰', '')]
    elif t == 'ln': q, ok, w = f"ln({a}x)", "−1/x²", ["1/x²", f"−{a}/x²", "1/x"]
    elif t == 'expb':
        c = nz(-9, 9); q, ok, w = f"e^({a}x {'+' if c > 0 else '−'} {abs(c)})", f"{a * a}e^({a}x {'+' if c > 0 else '−'} {abs(c)})", [f"{a}e^({a}x {'+' if c > 0 else '−'} {abs(c)})", f"{2 * a}e^({a}x {'+' if c > 0 else '−'} {abs(c)})", f"e^({a}x {'+' if c > 0 else '−'} {abs(c)})"]
    else:
        n = R.randint(3, 9); q = f"x{sup(n)}"; ok = f"{n * (n - 1) * (n - 2)}x{sup(n - 3)}".replace('x¹', 'x').replace('x⁰', ''); w = [f"{n * (n - 1)}x{sup(n - 2)}", f"{n ** 3}x{sup(n - 3)}".replace('x¹', 'x').replace('x⁰', ''), f"{n * (n - 1) * (n - 2)}x{sup(n - 2)}"]
        b.add(f"y = {q} হলে d³y/dx³ = কত?", ok, W(ok, w), "তিনবার অন্তরীকরণ।", lv); return
    b.add(f"y = {q} হলে d²y/dx² = কত?", ok, W(ok, w), "দুবার অন্তরীকরণ।", lv)
part('h11', '9', '9.H', [], [d9h, d9h2], [], [])
def d9i(b, lv):
    t = R.choice(['slope', 'ext', 'vel'])
    if t == 'slope':
        a, c, d = nz(-5, 5), R.randint(-9, 9), R.randint(-9, 9); x = R.randint(-5, 5)
        v = 2 * a * x + c
        b.add(f"y = {px({2: a, 1: c, 0: d})} বক্ররেখার x = {num(x)} বিন্দুতে স্পর্শকের ঢাল কত?", num(v), W(num(v), [num(a * x * x + c * x + d), num(v + c), num(-v) if v else '1', num(2 * a + c)]), "dy/dx-এর মান।", lv)
    elif t == 'ext':
        a = nz(-6, 6); h = R.randint(-8, 8); k = R.randint(-20, 20)
        c, d = -2 * a * h, a * h * h + k
        kind = 'ক্ষুদ্রতম' if a > 0 else 'বৃহত্তম'
        b.add(f"f(x) = {px({2: a, 1: c, 0: d})}-এর {kind} মান কত?", num(k), W(num(k), [num(d), num(h), num(-k) if k else '1', num(k + a)]), f"f′(x) = 0 ⇒ x = {num(h)}।", lv)
    else:
        a, c, d = R.randint(1, 6), R.randint(-10, 10), R.randint(1, 20); tt = R.randint(1, 8)
        v = 3 * a * tt * tt + c
        b.add(f"কোনো কণার সরণ s = {px({3: a, 1: c, 0: d}).replace('x', 't')} মিটার হলে t = {tt} সেকেন্ডে বেগ কত?", f"{num(v)} m/s", W(f"{num(v)} m/s", [f"{num(a * tt ** 3 + c * tt + d)} m/s", f"{num(6 * a * tt)} m/s", f"{num(v + c)} m/s"]), "v = ds/dt।", lv)
part('h11', '9', '9.I', [], [], [d9i], [])

# ---------------------------------------------------------------- h11 10.A, 10.C–10.G
def xp(c, k):
    t = '' if k == 0 else ('x' if k == 1 else f"x{sup(k)}")
    if not t: return num(c)
    return co(c, t)
def i10a(b, lv):
    n = R.randint(1, 9); m = R.randint(1, 12); a = m * (n + 1)
    ok = f"{xp(m, n + 1)} + c"
    b.add(f"∫ {xp(a, n)} dx = কত?", ok, W(ok, [f"{xp(a * n, n - 1)} + c", f"{xp(a, n + 1)} + c", f"{xp(m, n)} + c", f"{xp(a * (n + 1), n + 1)} + c"]), "xⁿ⁺¹/(n + 1)।", lv)
part('h11', '10', '10.A', [], [], [i10a], [])
def i10c(b, lv):
    a = R.randint(2, 12); t = R.choice(['sin', 'cos', 'sec²', 'cosec²', 'sec tan'])
    ok, w = {'sin': (f"−(1/{a}) cos {a}x + c", [f"(1/{a}) cos {a}x + c", f"−{a} cos {a}x + c", f"(1/{a}) sin {a}x + c"]),
             'cos': (f"(1/{a}) sin {a}x + c", [f"−(1/{a}) sin {a}x + c", f"{a} sin {a}x + c", f"(1/{a}) cos {a}x + c"]),
             'sec²': (f"(1/{a}) tan {a}x + c", [f"{a} tan {a}x + c", f"−(1/{a}) tan {a}x + c", f"(1/{a}) sec {a}x + c"]),
             'cosec²': (f"−(1/{a}) cot {a}x + c", [f"(1/{a}) cot {a}x + c", f"−{a} cot {a}x + c", f"(1/{a}) cosec {a}x + c"]),
             'sec tan': (f"(1/{a}) sec {a}x + c", [f"{a} sec {a}x + c", f"(1/{a}) tan {a}x + c", f"−(1/{a}) sec {a}x + c"])}[t]
    integrand = {'sin': f"sin {a}x", 'cos': f"cos {a}x", 'sec²': f"sec²{a}x", 'cosec²': f"cosec²{a}x", 'sec tan': f"sec {a}x tan {a}x"}[t]
    b.add(f"∫ {integrand} dx = কত?", ok, W(ok, w), "", lv)
def i10c2(b, lv):
    a = R.randint(1, 12); t = R.choice(['sin²', 'cos²'])
    s = '−' if t == 'sin²' else '+'
    ok = f"x/2 {s} sin {2 * a}x/{4 * a} + c"
    b.add(f"∫ {t}{'x' if a == 1 else f'{a}x'} dx = কত?".replace('sin²1x', 'sin²x'), ok, W(ok, [f"x/2 {'+' if s == '−' else '−'} sin {2 * a}x/{4 * a} + c", f"x/2 {s} sin {2 * a}x/{2 * a} + c", f"x {s} sin {2 * a}x/{4 * a} + c"]), "দ্বিগুণ কোণের সূত্রে রূপান্তর।", lv)
part('h11', '10', '10.C', [], [i10c], [i10c, i10c2], [])
def i10d(b, lv):
    a = R.randint(2, 12); t = R.choice(['exp', 'cos', 'sin', 'ln'])
    if t == 'exp': q, ok, w = f"x e^({a}x)", f"e^({a}x)(x/{a} − 1/{a * a}) + c", [f"e^({a}x)(x/{a} + 1/{a * a}) + c", f"x e^({a}x)/{a} + c", f"e^({a}x)(x − 1) + c"]
    elif t == 'cos': q, ok, w = f"x cos {a}x", f"(x/{a}) sin {a}x + (1/{a * a}) cos {a}x + c", [f"(x/{a}) sin {a}x − (1/{a * a}) cos {a}x + c", f"x sin {a}x + cos {a}x + c", f"−(x/{a}) sin {a}x + c"]
    elif t == 'sin': q, ok, w = f"x sin {a}x", f"−(x/{a}) cos {a}x + (1/{a * a}) sin {a}x + c", [f"(x/{a}) cos {a}x + (1/{a * a}) sin {a}x + c", f"−x cos {a}x + sin {a}x + c", f"(x/{a}) sin {a}x + c"]
    else:
        n = R.randint(1, 6); q = f"x{sup(n)} ln x".replace('x¹', 'x'); ok = f"x{sup(n + 1)} ln x/{n + 1} − x{sup(n + 1)}/{(n + 1) ** 2} + c"; w = [f"x{sup(n + 1)} ln x/{n + 1} + x{sup(n + 1)}/{(n + 1) ** 2} + c", f"x{sup(n + 1)} ln x − x{sup(n + 1)} + c", f"x{sup(n)}/{n} + c"]
    for i in range(3): w[i] = w[i].replace('/1 ', ' ').replace('/1)', ')')
    ok = ok.replace('/1 ', ' ').replace('/1)', ')')
    b.add(f"∫ {q} dx = কত?", ok, W(ok, w), "অংশায়ন: ∫u dv = uv − ∫v du।", lv)
part('h11', '10', '10.D', [], [i10d], [], [])
def i10e(b, lv):
    a = R.randint(2, 15); t = R.choice(['atan', 'asin', 'ln', 'diff', 'lin'])
    A2 = a * a
    if t == 'atan': q, ok, w = f"1/(x² + {A2})", f"(1/{a}) tan⁻¹(x/{a}) + c", [f"tan⁻¹(x/{a}) + c", f"(1/{a}) sin⁻¹(x/{a}) + c", f"(1/{2 * a}) ln|x² + {A2}| + c"]
    elif t == 'asin': q, ok, w = f"1/√({A2} − x²)", f"sin⁻¹(x/{a}) + c", [f"(1/{a}) sin⁻¹(x/{a}) + c", f"cos⁻¹(x/{a}) + c", f"(1/{a}) tan⁻¹(x/{a}) + c"]
    elif t == 'diff': q, ok, w = f"1/(x² − {A2})", f"(1/{2 * a}) ln|(x − {a})/(x + {a})| + c", [f"(1/{2 * a}) ln|(x + {a})/(x − {a})| + c", f"(1/{a}) ln|(x − {a})/(x + {a})| + c", f"(1/{a}) tan⁻¹(x/{a}) + c"]
    elif t == 'ln':
        p, c = R.randint(1, 9), R.randint(-9, 9); q = f"1/({px({1: p, 0: c})})"; ok = f"(1/{p}) ln|{px({1: p, 0: c})}| + c"; w = [f"{p} ln|{px({1: p, 0: c})}| + c", f"ln|{px({1: p, 0: c})}| + c", f"−1/({px({1: p, 0: c})})² + c"]
    else:
        p, c = R.randint(1, 9), R.randint(1, 9); q = f"{p}/(x + {c})"; ok = f"{p} ln|x + {c}| + c"; w = [f"ln|x + {c}| + c", f"{p}(x + {c}) + c", f"−{p}/(x + {c})² + c"]
    ok = ok.replace('(1/1) ', '').replace('1/1 ', ''); w = [x.replace('(1/1) ', '') for x in w]
    b.add(f"∫ {q} dx = কত?".replace('x/1)', 'x)'), ok.replace('x/1)', 'x)'), W(ok.replace('x/1)', 'x)'), [x.replace('x/1)', 'x)') for x in w]), "বিশেষ সূত্র।", lv)
def i10e_pf(b, lv):
    a, c = R.sample(range(-8, 9), 2)
    # 1/((x − a)(x − c)) = (1/(a − c))[1/(x − a) − 1/(x − c)]
    k = F(1, a - c)
    def lx(v): return f"x {'−' if v >= 0 else '+'} {abs(v)}".replace(' − 0', '').replace(' + 0', '')
    K = lambda v: '' if v == 1 else ('−' if v == -1 else f"({num(v)}) ")
    ok = f"{K(k)}ln|({lx(a)})/({lx(c)})| + c"
    b.add(f"∫ dx/(({lx(a)})({lx(c)})) = কত?", ok, W(ok, [f"{K(-k)}ln|({lx(a)})/({lx(c)})| + c", f"ln|({lx(a)})({lx(c)})| + c", f"{K(k)}ln|({lx(a)})({lx(c)})| + c", f"{K(2 * k)}ln|({lx(a)})/({lx(c)})| + c"]), "আংশিক ভগ্নাংশ।", lv)
part('h11', '10', '10.E', [], [i10e], [i10e, i10e_pf], [i10e_pf])
def i10f(b, lv):
    t = R.choice(['lin', 'sq', 'cub', 'trig'])
    if t == 'lin':
        p, q = nz(-9, 9), R.randint(-9, 9); lo, hi = sorted(R.sample(range(-5, 8), 2))
        v = F(p, 2) * (hi * hi - lo * lo) + q * (hi - lo); integ = px({1: p, 0: q})
    elif t == 'sq':
        p = R.randint(1, 9); lo, hi = sorted(R.sample(range(-4, 7), 2)); v = F(p, 3) * (hi ** 3 - lo ** 3); integ = co(p, 'x²')
    elif t == 'cub':
        p = R.randint(1, 8); lo, hi = 0, R.randint(1, 5); v = F(p, 4) * hi ** 4; integ = co(p, 'x³')
    else:
        p = R.randint(1, 9); lo, hi = 0, None
        f, up, v = R.choice([('sin x', 'π/2', F(p)), ('cos x', 'π/2', F(p)), ('sin x', 'π', F(2 * p)), ('cos x', 'π', F(0)), ('sec²x', 'π/4', F(p))])
        b.add(f"∫₀^{up} {co(p, f)} dx = কত?", num(v), W(num(v), [num(v + p), num(-v) if v else str(p), num(v * 2) if v else str(2 * p), '1' if v != 1 else '2']), "", lv); return
    b.add(f"∫ ({integ}) dx-এর মান {num(lo)} থেকে {num(hi)} সীমায় কত?", num(v), W(num(v), [num(-v) if v else '1', num(v + 1), num(v * 2) if v else '2', num(v - F(1, 2))]), "F(b) − F(a)।", lv)
part('h11', '10', '10.F', [], [], [i10f], [])
def i10g(b, lv):
    t = R.choice(['x2', 'lin', 'cube', 'between'])
    if t == 'x2':
        k = R.randint(1, 12); p = R.randint(1, 6); v = F(p * k ** 3, 3)
        q = f"y = {co(p, 'x²')}, x-অক্ষ এবং x = 0 ও x = {k} রেখা দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল কত বর্গ একক?"
    elif t == 'lin':
        m, k = R.randint(1, 9), R.randint(1, 15); v = F(m * k * k, 2)
        q = f"y = {co(m, 'x')}, x-অক্ষ ও x = {k} রেখা দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল কত বর্গ একক?"
    elif t == 'cube':
        k = R.randint(1, 6); v = F(k ** 4, 4)
        q = f"y = x³, x-অক্ষ এবং x = 0 ও x = {k} দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল কত বর্গ একক?"
    else:
        m = R.randint(1, 9); v = F(m ** 3, 6)
        q = f"y = x² ও y = {co(m, 'x')} দ্বারা আবদ্ধ ক্ষেত্রের ক্ষেত্রফল কত বর্গ একক?"
    b.add(q, fr(v), W(fr(v), [fr(v * 2), fr(v / 2), fr(v + 1), fr(v * 3)]), "নির্দিষ্ট যোগজ।", lv)
part('h11', '10', '10.G', [], [i10g], [i10g], [])

# ---------------------------------------------------------------- h12 3.B, 5.A, 5.B, 7.B, 9.B
def c3b(b, lv):
    r = R.randint(1, 9); n = R.randint(2, 9); th = R.choice([F(1, 6), F(1, 4), F(1, 3), F(1, 2), F(1, 12)])
    ok = f"{r ** n}(cos {piF(n * th)} − i sin {piF(n * th)})"
    b.add(f"[{r}(cos {piF(th)} − i sin {piF(th)})]{sup(n)} = কত?".replace('[1(', '[(').replace(')]', ')]'), ok, W(ok, [f"{r ** n}(cos {piF(n * th)} + i sin {piF(n * th)})", f"{r * n}(cos {piF(n * th)} − i sin {piF(n * th)})", f"{r ** n}(cos {piF(th)} − i sin {piF(th)})"]), "দ্য মোয়াভর।", lv)
def c3b_mod(b, lv):
    p, q, r = tri(); n = R.randint(2, 8)
    b.add(f"|({p} + {q}i){sup(n)}| = কত?", r ** n, W(r ** n, [r * n, (p + q) ** n, r ** (n + 1)]), "|zⁿ| = |z|ⁿ।", lv)
part('h12', '3', '3.B', [], [], [c3b, c3b_mod], [])
def b5a(b, lv):
    n = R.randint(4, 15); r = R.randint(1, n - 1); a, c = R.choice([(1, 2), (2, 1), (1, 3), (3, 1), (2, 3), (1, -2), (2, -1), (1, -3)])
    v = math.comb(n, r) * a ** (n - r) * c ** r
    b.add(f"({a if a > 1 else ''}{'' if a > 1 else ''}{'1' if a == 1 else ''} {'+' if c > 0 else '−'} {co(abs(c), 'x')}){sup(n)}-এর বিস্তৃতিতে x{sup(r)}-এর সহগ কত?".replace('x¹', 'x'), num(v), W(num(v), [num(math.comb(n, r)), num(-v), num(math.comb(n, r) * c ** r), num(v * 2)]), f"{n}C{r}·{a}^{n - r}·({num(c)})^{r}।", lv)
part('h12', '5', '5.A', [], [], [b5a], [])
def b5b(b, lv):
    k = R.choice([2, 3, 4, 5, 6, F(1, 2), F(1, 3), -2, -3]); r = R.randint(2, 7)
    v = F(k) ** r
    b.add(f"1/(1 − {co(k, 'x')})-এর বিস্তৃতিতে x{sup(r)}-এর সহগ কত?".replace('− −', '+ ').replace('− (−', '+ ('), fr(v), W(fr(v), [fr(-v), fr(F(k) * r), fr(F(k) ** (r - 1)), fr(v * (r + 1))]), "(1 − kx)⁻¹ = Σkʳxʳ।", lv)
part('h12', '5', '5.B', [], [b5b], [], [])
part('h12', '7', '7.B', [], [g7], [g7, g7_two], [])
def v9b(b, lv):
    g = R.choice([10, F(98, 10)]); k = R.randint(1, 20)
    u = g * k; t = R.choice(['tmax', 'v', 'hmax'])
    def d(x): s = f"{float(x):.2f}".rstrip('0').rstrip('.'); return s
    if t == 'tmax': q, ok, w = f"{d(u)} m/s বেগে খাড়া উপরে নিক্ষিপ্ত বস্তু কত সময়ে সর্বোচ্চ উচ্চতায় পৌঁছায়? (g = {d(g)} m/s²)", f"{k} s", [f"{2 * k} s", f"{k + 1} s", f"{d(u)} s"]
    elif t == 'v':
        tt = R.randint(1, max(1, k - 1)) if k > 1 else 1; v = u - g * tt
        q, ok, w = f"{d(u)} m/s বেগে খাড়া উপরে নিক্ষিপ্ত বস্তুর {tt} সেকেন্ড পর বেগ কত? (g = {d(g)} m/s²)", f"{d(v)} m/s", [f"{d(u + g * tt)} m/s", f"{d(g * tt)} m/s", f"{d(v + g)} m/s"]
    else: q, ok, w = f"{d(u)} m/s বেগে খাড়া উপরে নিক্ষিপ্ত বস্তুর সর্বোচ্চ উচ্চতা কত? (g = {d(g)} m/s²)", f"{d(g * k * k / 2)} m", [f"{d(g * k * k)} m", f"{d(g * k * k / 4)} m", f"{d(u * k)} m"]
    b.add(q, ok, W(ok, w), "", lv)
part('h12', '9', '9.B', [], [v9b], [v9b], [])

# ---------------------------------------------------------------- অতিরিক্ত পূরণ
def s55(b, lv):
    x, y = R.randint(1, 12), R.randint(1, 12)
    if x == y: return
    s_, p_ = x + y, x * y
    ok = f"({x}, {y}) অথবা ({y}, {x})"
    b.add(f"x + y = {s_} ও xy = {p_} হলে (x, y) = কত?", ok, W(ok, [f"({x}, {-y}) অথবা ({-y}, {x})", f"({x + 1}, {y - 1}) অথবা ({y - 1}, {x + 1})", f"({s_}, {p_})"]), "t² − (x + y)t + xy = 0।", lv)
part('c10h', '5', '5.5', [], [], [s55], [])
ANGV = {'sin': {0: '0', 30: '1/2', 45: '1/√2', 60: '√3/2', 90: '1'}, 'cos': {0: '1', 30: '√3/2', 45: '1/√2', 60: '1/2', 90: '0'}, 'tan': {0: '0', 30: '1/√3', 45: '1', 60: '√3'}}
def a7(b, lv):
    f = R.choice(['sin', 'cos', 'tan']); k = R.randint(1, 8); base = R.choice([30, 45, 60])
    ang = k * 90 + R.choice([1, -1]) * base
    if ang <= 0: return
    q = ang % 360; ref = q % 180; ref = ref if ref <= 90 else 180 - ref
    sv = {'sin': 1 if q < 180 else -1, 'cos': 1 if (q < 90 or q > 270) else -1, 'tan': 1 if (q % 180) < 90 else -1}[f]
    v = ANGV[f][ref]; ok = v if sv > 0 else '−' + v
    b.add(f"{f} {ang}° = কত?", ok, W(ok, [v if sv < 0 else '−' + v] + [x for x in ANGV[f].values() if x not in (v, '0')] + ['0']), "সংযুক্ত কোণের সূত্র।", lv)
part('h11', '7', '7.A', [], [a7], [], [])
def e6b(b, lv):
    a, c = R.randint(2, 30), R.randint(1, 29)
    if c >= a: return
    ok = f"{a * c}π"
    b.add(f"x²/{a * a} + y²/{c * c} = 1 উপবৃত্তের ক্ষেত্রফল কত বর্গ একক?", ok, W(ok, [f"{a * a}π", f"{2 * a * c}π", f"{(a + c)}π", f"{c * c}π"]), "πab।", lv)
part('h12', '6', '6.B', [], [], [e6b], [])

for (course, ch), items in OUT.items():
    (D / f"ext/S{os.environ.get('SUPTAG', '')}_{course}_{ch}.json").write_text(json.dumps(items, ensure_ascii=False, indent=1), encoding='utf-8')
print('done', sum(len(v) for v in OUT.values()))
