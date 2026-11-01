#!/usr/bin/env python3
"""একাদশ শ্রেণি উচ্চতর গণিত ১ম পত্র (h11) অধ্যায় 6–10।
6.A কোণ পরিমাপ · 6.B ত্রিকোণমিতিক অনুপাত ও অভেদ · 6.C বিভিন্ন চতুর্ভাগে অনুপাতের মান
7.A সংযুক্ত কোণ · 7.B যৌগিক কোণ · 7.C গুণিতক কোণ · 7.D উপগুণিতক কোণ · 7.E রূপান্তর সূত্র · 7.F ত্রিভুজের ত্রিকোণমিতি · 7.G ত্রিকোণমিতিক সমীকরণ
8 ফাংশন ও লেখচিত্র · 9.A সীমা · 9.B মূল নিয়মে অন্তরীকরণ · 9.C আদর্শ সূত্র · 9.D গুণ ও ভাগের অন্তরজ · 9.E সংযোজিত ফাংশন
9.F বিপরীত ত্রিকোণমিতিক, সূচক ও লগারিদমীয় · 9.G অস্পষ্ট ও পরামিতিক · 9.H পর্যায়ক্রমিক অন্তরজ · 9.I অন্তরজের প্রয়োগ
10.A মৌলিক যোগজ · 10.B প্রতিস্থাপন · 10.C ত্রিকোণমিতিক যোগজ · 10.D অংশায়ন · 10.E বিশেষ সূত্র ও আংশিক ভগ্নাংশ · 10.F নির্দিষ্ট যোগজ · 10.G ক্ষেত্রফল"""
import random, pathlib, sys, math
from fractions import Fraction as F
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from mcqlib import run, save, E, M, H, fr, near, num, pfmt, surd, sup

R = random.Random(2026110112)
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
    """সহগ + পদ: co(3,'x') = '3x', co(1,'x') = 'x', co(-1,'x') = '−x'"""
    c = F(c)
    if c == 1: return s
    if c == -1: return '−' + s
    return num(c) + s
def piF(v):
    v = F(v)
    if v == 1: return 'π'
    if v.denominator == 1: return f"{v.numerator}π"
    return f"{v.numerator if v.numerator != 1 else ''}π/{v.denominator}"
def rad(deg):
    v = F(deg, 180)
    if v == 0: return '0'
    n, d = abs(v.numerator), v.denominator; sgn = '−' if v < 0 else ''
    return sgn + ('π' if n == 1 else f'{n}π') + ('' if d == 1 else f'/{d}')
_T = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29), (9, 40, 41), (12, 35, 37), (11, 60, 61), (28, 45, 53), (33, 56, 65), (16, 63, 65), (48, 55, 73), (13, 84, 85), (36, 77, 85), (39, 80, 89), (65, 72, 97)]
TRIP = _T + [(b_, a_, c_) for a_, b_, c_ in _T]
# সাধারণ কোণের মান (চিহ্নসহ)
import math as _m
VAL = {}
for d in range(0, 361, 15):
    VAL[d] = (_m.sin(_m.radians(d)), _m.cos(_m.radians(d)))
SURDS = {0: '0', 1: '1', -1: '−1', .5: '1/2', -.5: '−1/2', 3 ** .5 / 2: '√3/2', -(3 ** .5) / 2: '−√3/2', 2 ** -.5: '1/√2', -(2 ** -.5): '−1/√2',
         3 ** .5: '√3', -(3 ** .5): '−√3', 3 ** -.5: '1/√3', -(3 ** -.5): '−1/√3', 2: '2', -2: '−2', 2 / 3 ** .5: '2/√3', -2 / 3 ** .5: '−2/√3', 2 ** .5: '√2', -(2 ** .5): '−√2'}
def sv(x):
    for k, v in SURDS.items():
        if abs(x - k) < 1e-9: return v
    return None
TV = ['0', '1', '−1', '1/2', '−1/2', '√3/2', '−√3/2', '1/√2', '−1/√2', '√3', '−√3', '1/√3', '−1/√3', 'অসংজ্ঞায়িত']
def tval(fn, d):
    s, c = VAL[d % 360]
    if fn == 'sin': return sv(s)
    if fn == 'cos': return sv(c)
    if fn == 'tan': return 'অসংজ্ঞায়িত' if abs(c) < 1e-9 else sv(s / c)
    if fn == 'cot': return 'অসংজ্ঞায়িত' if abs(s) < 1e-9 else sv(c / s)
    if fn == 'sec': return 'অসংজ্ঞায়িত' if abs(c) < 1e-9 else sv(1 / c)
    if fn == 'cosec': return 'অসংজ্ঞায়িত' if abs(s) < 1e-9 else sv(1 / s)
NICE = [d for d in range(0, 361, 15) if d % 30 == 0 or d % 45 == 0]

# ---------------- 6.A কোণ পরিমাপ ----------------
fx6a = [
 ("π রেডিয়ান = কত ডিগ্রি?", "180°", ["90°", "360°", "57°"], "", E),
 ("1 রেডিয়ান প্রায় কত ডিগ্রি?", "57°17′45″", ["60°", "45°", "57°"], "180°/π ≈ 57°17′45″।", E),
 ("1° = কত মিনিট?", "60′", ["100′", "30′", "360′"], "ষাটমূলক পদ্ধতি।", E),
 ("শতমূলক পদ্ধতিতে এক সমকোণ = কত গ্রেড?", "100ᵍ", ["90ᵍ", "60ᵍ", "180ᵍ"], "শতমূলক পদ্ধতি।", E),
 ("D ডিগ্রি, G গ্রেড ও R রেডিয়ান হলে কোনটি সত্য?", "D/180 = G/200 = R/π", ["D/90 = G/100 = R/π", "D/180 = G/100 = R/π", "D = G = R"], "সম্পর্ক।", M),
 ("s = rθ সূত্রে θ কোন এককে প্রকাশিত?", "রেডিয়ান", ["ডিগ্রি", "গ্রেড", "মিনিট"], "বৃত্তীয় পরিমাপ।", E),
]
DG = [15, 18, 20, 30, 36, 40, 45, 54, 60, 72, 75, 90, 105, 120, 135, 144, 150, 210, 225, 240, 270, 300, 315, 330, 360, 450, 540, 720]
def e_d2r(b):
    d = R.choice(DG); ok = rad(d)
    b.add(f"{d}° = কত রেডিয়ান?", ok, W(ok, [rad(2 * d), rad(d + 30), rad(abs(180 - d)) if d != 180 else rad(90), rad(d // 2) if d % 2 == 0 else rad(d + 15)]), f"{d} × π/180।", E)
def e_r2d(b):
    d = R.choice(DG); ok = f"{d}°"
    b.add(f"{rad(d)} রেডিয়ান = কত ডিগ্রি?", ok, W(ok, [f"{2 * d}°", f"{d + 30}°", f"{d + 45}°", f"{abs(180 - d)}°" if d != 180 else '90°']), "× 180/π।", E)
def e_grade(b):
    d = R.choice([9, 18, 27, 36, 45, 54, 63, 72, 81, 90, 135, 180])
    g = F(d * 200, 180)
    b.add(f"{d}° = কত গ্রেড?", f"{fr(g)}ᵍ", W(f"{fr(g)}ᵍ", [f"{d}ᵍ", f"{fr(g * 2)}ᵍ", f"{fr(F(d * 180, 200))}ᵍ"]), "D/180 = G/200।", E)
def m_arc(b):
    r, th = R.randint(2, 20), R.choice([F(1, 2), F(1), F(3, 2), F(2), F(5, 2), F(1, 4), F(3, 4)])
    b.add(f"{r} সেমি ব্যাসার্ধের বৃত্তে {fr(th)} রেডিয়ান কোণের বিপরীত চাপের দৈর্ঘ্য কত সেমি?", fr(r * th), W(fr(r * th), [fr(F(r) / th), fr(r * th * 2), fr(r * th + 1)]), "s = rθ।", M)
def m_ang_arc(b):
    r, s = R.randint(2, 15), R.randint(1, 30)
    b.add(f"{r} মিটার ব্যাসার্ধের বৃত্তে {s} মিটার চাপ কেন্দ্রে কত রেডিয়ান কোণ উৎপন্ন করে?", fr(F(s, r)), W(fr(F(s, r)), [fr(F(r, s)), str(r * s), fr(F(s, r) + 1)]), "θ = s/r।", M)
def m_dms(b):
    d, m_ = R.randint(10, 80), R.choice([15, 30, 45, 12, 6, 36, 24, 48])
    v = F(d) + F(m_, 60)
    b.add(f"{d}°{m_}′ = কত ডিগ্রি (দশমিকে)?", f"{float(v):g}°", W(f"{float(v):g}°", [f"{d}.{m_}°", f"{float(F(d) + F(m_, 100)):g}°", f"{float(v) + 0.5:g}°"]), f"{m_}′ = {fr(F(m_, 60))}°।", M)
def m_wheel(b):
    r, n = R.choice([7, 14, 21, 35]), R.randint(2, 30)
    d = F(2 * 22 * r * n, 7)
    b.add(f"{r} সেমি ব্যাসার্ধের চাকা {n} বার ঘুরলে কত সেমি পথ যায়? (π = 22/7)", fr(d), W(fr(d), [fr(d / 2), fr(d * 2), fr(F(22 * r * r * n, 7))]), "2πr × n।", M)
def m_tri(b):
    a, c = R.sample([15, 30, 36, 45, 54, 60, 72, 75, 90], 2); rest = 180 - a - c
    if rest <= 0: return
    b.add(f"ত্রিভুজের দুটি কোণ {rad(a)} ও {rad(c)} রেডিয়ান হলে তৃতীয় কোণ কত রেডিয়ান?", rad(rest), W(rad(rest), [rad(a + c), rad(rest + 15), rad(360 - a - c)]), "π − (A + B)।", M)
def h_clock(b):
    h, m_ = R.randint(1, 12), R.choice([0, 10, 15, 20, 30, 40, 45, 50])
    ang = abs(F(60 * h - 11 * m_, 2)) % 360
    if ang > 180: ang = 360 - ang
    if ang.denominator != 1 or ang == 0: return
    ok = rad(int(ang))
    b.add(f"{h}টা {m_} মিনিটে ঘণ্টা ও মিনিটের কাঁটার মধ্যবর্তী কোণ কত রেডিয়ান?", ok, W(ok, [rad(360 - int(ang)), rad(int(ang) + 15), rad(int(ang) + 30), rad(abs(int(ang) - 30)) if int(ang) != 30 else rad(45)]), "|30h − 5.5m|।", H)
def h_earth(b):
    R_ = 6400; ang = R.choice([1, 2, 5, 10, 15, 30, 45])
    ok = piF(F(R_ * ang, 180))
    b.add(f"পৃথিবীর ব্যাসার্ধ 6400 কিমি হলে কেন্দ্রে {ang}° কোণ উৎপন্নকারী দুই স্থানের দূরত্ব কত কিমি?", ok, W(ok, [piF(F(R_ * ang, 90)), piF(R_ * ang), piF(F(R_, 180))]), "s = rθ।", H)
def h_poly(b):
    n = R.choice([5, 6, 8, 9, 10, 12, 15, 18, 20])
    ok = rad(F(180 * (n - 2), n))
    b.add(f"সুষম {n} বাহুবিশিষ্ট বহুভুজের প্রতিটি অন্তঃকোণ কত রেডিয়ান?", ok, W(ok, [rad(F(360, n)), rad(F(180, n)), rad(F(180 * (n - 1), n))]), "(n − 2)π/n।", H)
p6a = run('6.A', R, fx6a, [e_d2r, e_r2d, e_grade], [m_arc, m_ang_arc, m_dms, m_wheel, m_tri], [h_clock, h_earth, h_poly])

# ---------------- 6.B অনুপাত ও অভেদ ----------------
fx6b = [
 ("sin²θ + cos²θ = কত?", "1", ["0", "2", "sin 2θ"], "মৌলিক অভেদ।", E),
 ("sec²θ − tan²θ = কত?", "1", ["0", "−1", "2"], "অভেদ।", E),
 ("cosec²θ − cot²θ = কত?", "1", ["0", "−1", "2"], "অভেদ।", E),
 ("tan θ · cot θ = কত?", "1", ["0", "tan²θ", "−1"], "পরস্পর অন্যোন্যক।", E),
 ("(1 − sin²θ)sec²θ = কত?", "1", ["0", "tan²θ", "cos²θ"], "cos²θ · sec²θ।", M),
 ("√((1 − cos θ)/(1 + cos θ)) = কত? (θ সূক্ষ্মকোণ)", "cosec θ − cot θ", ["sec θ − tan θ", "cosec θ + cot θ", "tan θ"], "লব-হরকে (1 − cos θ) দিয়ে গুণ।", H),
]
def e_from_sin(b):
    o, a, h = R.choice(TRIP); fn = R.choice(['cos', 'tan', 'sec', 'cosec', 'cot'])
    v = {'cos': F(a, h), 'tan': F(o, a), 'sec': F(h, a), 'cosec': F(h, o), 'cot': F(a, o)}[fn]
    b.add(f"θ সূক্ষ্মকোণ এবং sin θ = {o}/{h} হলে {fn} θ = কত?", fr(v), W(fr(v), [fr(1 / v), fr(F(o, a)) if fn != 'tan' else fr(F(a, h)), fr(F(a, h)) if fn != 'cos' else fr(F(o, h)), fr(F(o, h))]), f"বিপরীত {o}, অতিভুজ {h}, সন্নিহিত {a}।", E)
def e_from_tan(b):
    o, a, h = R.choice(TRIP); fn = R.choice(['sin', 'cos', 'sec'])
    v = {'sin': F(o, h), 'cos': F(a, h), 'sec': F(h, a)}[fn]
    b.add(f"θ সূক্ষ্মকোণ এবং tan θ = {o}/{a} হলে {fn} θ = কত?", fr(v), W(fr(v), [fr(1 / v), fr(F(o, a)), fr(F(a, o)), fr(F(o + a, h))]), f"অতিভুজ {h}।", E)
def m_sum(b):
    o, a, h = R.choice(TRIP)
    v = F(o + a, h)
    b.add(f"θ সূক্ষ্মকোণ ও sec θ = {h}/{a} হলে sin θ + cos θ = কত?", fr(v), W(fr(v), [fr(F(o * a, h * h)), fr(F(h, o + a)), fr(F(abs(o - a), h)), fr(v + 1)]), f"sin θ = {o}/{h}, cos θ = {a}/{h}।", M)
def m_k(b):
    k = R.choice([F(5, 4), F(7, 5), F(4, 3), F(13, 12), F(17, 15), F(3, 2)])
    # sin θ + cos θ = k ⇒ sin θ cos θ = (k² − 1)/2
    v = (k * k - 1) / 2
    b.add(f"sin θ + cos θ = {fr(k)} হলে sin θ cos θ = কত?", fr(v), W(fr(v), [fr(k * k - 1), fr(k * k + 1), fr((k * k + 1) / 2)]), "বর্গ করে 1 + 2sin θ cos θ = k²।", M)
def m_tc(b):
    o, a, h = R.choice(TRIP)
    v = F(o, a) + F(a, o)
    b.add(f"tan θ = {o}/{a} হলে tan θ + cot θ = কত?", fr(v), W(fr(v), [fr(F(o, a) - F(a, o)), '1', fr(F(h * h, o * a) + 1)]), f"= sec θ cosec θ = {fr(v)}।", M)
def m_expr(b):
    o, a, h = R.choice(TRIP)
    s, c = F(o, h), F(a, h)
    v = (s + c) / (s - c) if s != c else None
    if v is None: return
    b.add(f"tan θ = {o}/{a} হলে (sin θ + cos θ)/(sin θ − cos θ) = কত?", num(v), W(num(v), [num(1 / v), num(-v), num(F(o + a, h))]), f"লব-হরকে cos θ দিয়ে ভাগ: (tan θ + 1)/(tan θ − 1)।", M)
def h_tsq(b):
    k = R.randint(2, 6)
    # tan θ + sec θ = k ⇒ sec θ − tan θ = 1/k ⇒ sec θ = (k + 1/k)/2
    v = (F(k) + F(1, k)) / 2
    b.add(f"tan θ + sec θ = {k} হলে sec θ = কত?", fr(v), W(fr(v), [fr((F(k) - F(1, k)) / 2), fr(F(1, k)), fr(F(k * k + 1, k))]), "sec θ − tan θ = 1/(sec θ + tan θ)।", H)
def h_tsq2(b):
    k = R.randint(2, 6)
    v = (F(k) - F(1, k)) / 2
    b.add(f"tan θ + sec θ = {k} হলে tan θ = কত?", fr(v), W(fr(v), [fr((F(k) + F(1, k)) / 2), fr(F(1, k)), fr(F(k * k - 1, k))]), "sec θ − tan θ = 1/k ব্যবহার করে।", H)
def h_expr2(b):
    o, a, h = R.choice(TRIP)
    v = F(h, a) ** 2 + F(h, o) ** 2
    b.add(f"tan θ = {o}/{a} হলে sec²θ + cosec²θ = কত?", fr(v), W(fr(v), ['1', fr(F(h, a) ** 2), fr(v + 1)]), "= sec²θ cosec²θ।", H)
p6b = run('6.B', R, fx6b, [e_from_sin, e_from_tan], [m_sum, m_k, m_tc, m_expr], [h_tsq, h_tsq2, h_expr2], caps=(16, 13, 8))

fx6c = [
 ("কোন চতুর্ভাগে শুধু tan ও cot ধনাত্মক?", "তৃতীয়", ["প্রথম", "দ্বিতীয়", "চতুর্থ"], "", E),
 ("কোন চতুর্ভাগে শুধু cos ও sec ধনাত্মক?", "চতুর্থ", ["প্রথম", "দ্বিতীয়", "তৃতীয়"], "", E),
 ("sin θ-এর সর্বোচ্চ মান কত?", "1", ["0", "∞", "2"], "−1 ≤ sin θ ≤ 1।", E),
 ("sec θ-এর মান কোন ব্যবধিতে থাকতে পারে না?", "(−1, 1)", ["[1, ∞)", "(−∞, −1]", "{1}"], "|sec θ| ≥ 1।", M),
]
def e_val(b):
    fn = R.choice(['sin', 'cos', 'tan']); d = R.choice(NICE); ok = tval(fn, d)
    if ok is None: return
    b.add(f"{fn} {d}° = কত?" if R.random() < .5 else f"{fn} {rad(d)} = কত?", ok, W(ok, R.sample([v for v in TV if v != ok], 6)), "চতুর্ভাগ অনুযায়ী চিহ্ন।", E)
def e_quad(b):
    d = R.choice([x for x in range(5, 360) if x % 90]); q = d // 90 + 1; nm = {1: 'প্রথম', 2: 'দ্বিতীয়', 3: 'তৃতীয়', 4: 'চতুর্থ'}
    b.add(f"{d}° কোণটি কোন চতুর্ভাগে?", nm[q], [nm[i] for i in (1, 2, 3, 4) if i != q], "", E)
def m_rec(b):
    fn = R.choice(['sec', 'cosec', 'cot']); d = R.choice([x for x in NICE if x % 90]); ok = tval(fn, d)
    if ok is None: return
    b.add(f"{fn} {d}° = কত?", ok, W(ok, R.sample(['2', '−2', '2/√3', '−2/√3', '√2', '−√2', '√3', '−√3', '1/√3', '−1/√3', '1', '−1'], 6)), "অন্যোন্যক অনুপাত।", M)
def m_expr(b):
    a, c = R.sample([30, 45, 60, 120, 135, 150, 210, 225, 240, 300, 315, 330], 2)
    v = VAL[a][0] ** 2 + VAL[c][1] ** 2; vv = F(v).limit_denominator(8)
    if abs(float(vv) - v) > 1e-9: return
    b.add(f"sin²{a}° + cos²{c}° = কত?", fr(vv), W(fr(vv), ['1', '1/2', '3/2', '1/4', '5/4', '3/4', '0']), "প্রতিটির মান বসিয়ে।", M)
def m_given(b):
    o, a, h = R.choice(TRIP); q = R.choice([2, 3, 4]); nm = {2: 'দ্বিতীয়', 3: 'তৃতীয়', 4: 'চতুর্থ'}
    ss, cs = {2: (1, -1), 3: (-1, -1), 4: (-1, 1)}[q]
    ok = f"{'−' if cs < 0 else ''}{a}/{h}"
    b.add(f"sin θ = {'−' if ss < 0 else ''}{o}/{h} এবং θ {nm[q]} চতুর্ভাগে হলে cos θ = কত?", ok, W(ok, [f"{'' if cs < 0 else '−'}{a}/{h}", f"{'−' if cs < 0 else ''}{o}/{h}", f"{'−' if cs < 0 else ''}{a}/{o}"]), "চতুর্ভাগে চিহ্ন।", M)
def h_tanq(b):
    o, a, h = R.choice(TRIP); q = R.choice([2, 3, 4]); nm = {2: 'দ্বিতীয়', 3: 'তৃতীয়', 4: 'চতুর্থ'}
    ss, cs = {2: (1, -1), 3: (-1, -1), 4: (-1, 1)}[q]
    v = F(ss * o + cs * a, h)
    b.add(f"tan θ = {'−' if ss * cs < 0 else ''}{o}/{a} এবং θ {nm[q]} চতুর্ভাগে হলে sin θ + cos θ = কত?", num(v), W(num(v), [num(-v), num(F(o + a, h)), num(F(ss * o - cs * a, h))]), "চতুর্ভাগ অনুযায়ী।", H)
def h_maxmin(b):
    a, c = R.choice([(3, 4), (5, 12), (6, 8), (8, 15), (1, 1), (1, 2)]); k = R.randint(-5, 5)
    r = math.isqrt(a * a + c * c); rs = str(r) if r * r == a * a + c * c else surd(a * a + c * c)
    ok = f"{num(k)} + {rs}".replace('0 + ', '') if True else ''
    v = f"{rs}" if k == 0 else f"{num(k)} + {rs}"
    b.add(f"{a if a > 1 else ''}sin θ + {c if c > 1 else ''}cos θ {'+' if k >= 0 else '−'} {abs(k)}-এর সর্বোচ্চ মান কত?".replace(' + 0-এর', '-এর').replace(' − 0-এর', '-এর'), v, W(v, [str(a + c + k), f"{num(k)} − {rs}" if k else f"−{rs}", str(max(a, c) + k)]), f"√({a}² + {c}²) = {rs}।", H)
p6c = run('6.C', R, fx6c, [e_val, e_quad], [m_rec, m_expr, m_given], [h_tanq, h_maxmin], caps=(20, 18, 12))
save('i6', p6a + p6b + p6c)

# ---------------- 7.A সংযুক্ত কোণ ----------------
F3 = {'sin': _m.sin, 'cos': _m.cos, 'tan': _m.tan, 'cot': lambda z: 1 / _m.tan(z)}
CO = {'sin': 'cos', 'cos': 'sin', 'tan': 'cot', 'cot': 'tan'}
fx7a = [
 ("sin(90° + θ) = কত?", "cos θ", ["−cos θ", "sin θ", "−sin θ"], "", E), ("cos(180° − θ) = কত?", "−cos θ", ["cos θ", "sin θ", "−sin θ"], "", E),
 ("tan(270° − θ) = কত?", "cot θ", ["−cot θ", "tan θ", "−tan θ"], "তৃতীয় চতুর্ভাগে tan ধনাত্মক।", M), ("cos(−θ) = কত?", "cos θ", ["−cos θ", "sin θ", "sec θ"], "", E),
]
def e_red(b):
    k = R.choice([90, 180, 270, 360]); fn = R.choice(['sin', 'cos', 'tan']); s = R.choice([1, -1]); t = 20
    d = k + s * t; v = F3[fn](_m.radians(d)); g = CO[fn] if k in (90, 270) else fn; base = F3[g](_m.radians(t))
    ok = ('' if v * base > 0 else '−') + f"{g} θ"
    b.add(f"{fn}({k}° {'+' if s > 0 else '−'} θ) = কত?", ok, W(ok, [('−' if v * base > 0 else '') + f"{g} θ", f"{CO[g]} θ", f"−{CO[g]} θ"]), "চতুর্ভাগ ও (বিজোড়/জোড়) গুণিতক।", E)
def e_val(b):
    fn = R.choice(['sin', 'cos', 'tan']); d = R.choice([120, 135, 150, 210, 225, 240, 300, 315, 330, 390, 405, 420, 480, 510, 570, 600, 690])
    ok = tval(fn, d % 360)
    b.add(f"{fn} {d}° = কত?", ok, W(ok, R.sample([v for v in TV if v != ok and v != 'অসংজ্ঞায়িত'], 5)), "সংযুক্ত কোণ ব্যবহার করে।", E)
def m_neg(b):
    fn = R.choice(['sin', 'cos', 'tan']); d = R.choice([30, 45, 60, 120, 135, 150, 210, 225, 300, 330, 390, 750]); ok = tval(fn, -d % 360)
    b.add(f"{fn}(−{d}°) = কত?", ok, W(ok, R.sample([v for v in TV if v != ok and v != 'অসংজ্ঞায়িত'], 5)), "", M)
def m_expr(b):
    A = R.choice([10, 20, 25, 35, 40, 50, 65, 70, 80])
    kinds = [(f"sin({90 + A}°) − cos({A}°)", '0'), (f"cos({180 - A}°) + cos({A}°)", '0'), (f"tan({180 + A}°) − tan({A}°)", '0'), (f"sin({180 - A}°)/sin({A}°)", '1'), (f"cos({360 - A}°)/cos({A}°)", '1'), (f"tan({90 - A}°)·tan({A}°)", '1'), (f"sin({180 + A}°)/sin({A}°)", '−1')]
    q, ok = R.choice(kinds)
    b.add(f"{q} = কত?", ok, W(ok, ['0', '1', '−1', '2']), "সংযুক্ত কোণের সূত্র।", M)
def m_sum(b):
    fn = R.choice(['sin', 'cos']); A = R.choice([10, 20, 30, 40])
    ok = '0' if fn == 'cos' else '0'
    angs = [A, 180 - A, 180 + A, 360 - A]
    b.add(f"{fn} {angs[0]}° + {fn} {angs[1]}° + {fn} {angs[2]}° + {fn} {angs[3]}° = কত?", '0', ['1', '2', f"4{fn} {A}°"], "জোড়ায় কাটাকাটি।", M)
def h_tri(b):
    fn, ok = R.choice([('sin(A + B)', 'sin C'), ('cos(A + B)', '−cos C'), ('tan(A + B)', '−tan C'), ('sin((A + B)/2)', 'cos(C/2)'), ('cos((A + B)/2)', 'sin(C/2)')])
    b.add(f"ABC ত্রিভুজে {fn} = কত?", ok, W(ok, ['sin C', '−sin C', 'cos C', '−cos C', 'cos(C/2)', 'sin(C/2)', '−tan C', 'tan C']), "A + B = π − C।", H)
def h_prod(b):
    n = R.choice([45, 89])
    b.add(f"tan 1° · tan 2° · tan 3° · … · tan {n}° = কত?", '1', ['0', '√3', 'অসংজ্ঞায়িত'], "tan θ · tan(90° − θ) = 1।", H)
    b.add("cos 1° · cos 2° · … · cos 179° = কত?", '0', ['1', '−1', '1/2'], "cos 90° = 0 গুণনীয়ক।", H)
    b.add("sin²5° + sin²10° + … + sin²85° (প্রতি পদে 5° বৃদ্ধি) = কত?", '17/2', ['9', '8', '17'], "sin²θ + sin²(90° − θ) = 1; 8 জোড়া + sin²45°।", H)
def h_combo(b):
    ds = [d for d in range(390, 1100, 15) if d % 30 == 0 or d % 45 == 0]
    d1, d2 = R.sample(ds, 2); f1, f2 = R.choice([('sin', 'cos'), ('cos', 'sin'), ('sin', 'sin'), ('cos', 'cos')])
    op = R.choice(['+', '−', '·'])
    v1 = VAL[d1 % 360][0 if f1 == 'sin' else 1]; v2 = VAL[d2 % 360][0 if f2 == 'sin' else 1]
    v = v1 + v2 if op == '+' else (v1 - v2 if op == '−' else v1 * v2)
    ok = sv(v) or (fr(F(v).limit_denominator(8)) if abs(float(F(v).limit_denominator(8)) - v) < 1e-9 else None)
    if ok is None:
        for k, t in [((3 ** .5 + 1) / 2, '(√3 + 1)/2'), ((3 ** .5 - 1) / 2, '(√3 − 1)/2'), ((1 - 3 ** .5) / 2, '(1 − √3)/2'), (-(3 ** .5 + 1) / 2, '−(√3 + 1)/2'), (3 ** .5 / 4, '√3/4'), (-(3 ** .5) / 4, '−√3/4'), (1 / 4, '1/4'), (-1 / 4, '−1/4'), (3 / 4, '3/4'), (-3 / 4, '−3/4'), (1 / (2 * 2 ** .5), '1/(2√2)'), (-1 / (2 * 2 ** .5), '−1/(2√2)'), (3 ** .5 / (2 * 2 ** .5), '√3/(2√2)'), (-(3 ** .5) / (2 * 2 ** .5), '−√3/(2√2)'), ((1 + 2 ** .5) / 2, '(1 + √2)/2'), ((2 ** .5 - 1) / 2, '(√2 − 1)/2'), ((1 - 2 ** .5) / 2, '(1 − √2)/2'), (1 / 2 ** .5 + 3 ** .5 / 2, '(√2 + √3)/2'), (1 / 2 ** .5 - 3 ** .5 / 2, '(√2 − √3)/2'), (3 ** .5 / 2 - 1 / 2 ** .5, '(√3 − √2)/2'), (-(1 / 2 ** .5 + 3 ** .5 / 2), '−(√2 + √3)/2'), (-(1 + 2 ** .5) / 2, '−(1 + √2)/2'), (2 ** .5, '√2'), (-(2 ** .5), '−√2'), (3 ** .5, '√3'), (-(3 ** .5), '−√3'), (1.5, '3/2'), (-1.5, '−3/2')]:
            if abs(v - k) < 1e-9: ok = t; break
    if ok is None: return
    pool = ['0', '1', '−1', '1/2', '−1/2', '√3/2', '−√3/2', '(√3 + 1)/2', '(√3 − 1)/2', '√3/4', '1/4', '3/4', '√2', '1/√2', '(1 + √2)/2', '3/2', '−3/4', '−1/4']
    b.add(f"{f1} {d1}° {op} {f2} {d2}° = কত?", ok, W(ok, R.sample([x for x in pool if x != ok], 6)), "প্রতিটি কোণকে সংযুক্ত কোণে ভেঙে মান বসিয়ে।", H)
p7a = run('7.A', R, fx7a, [e_red, e_val], [m_neg, m_expr, m_sum], [h_tri, h_prod, h_combo], caps=(20, 20, 16))

# ---------------- 7.B যৌগিক কোণ ----------------
fx7b = [
 ("sin(A + B) = কত?", "sin A cos B + cos A sin B", ["sin A cos B − cos A sin B", "cos A cos B − sin A sin B", "sin A sin B + cos A cos B"], "", E),
 ("cos(A − B) = কত?", "cos A cos B + sin A sin B", ["cos A cos B − sin A sin B", "sin A cos B − cos A sin B", "sin A sin B − cos A cos B"], "", E),
 ("tan(A + B) = কত?", "(tan A + tan B)/(1 − tan A tan B)", ["(tan A − tan B)/(1 + tan A tan B)", "(tan A + tan B)/(1 + tan A tan B)", "tan A + tan B"], "", E),
 ("sin 75° = কত?", "(√3 + 1)/(2√2)", ["(√3 − 1)/(2√2)", "√3/2", "1/√2"], "sin(45° + 30°)।", M),
 ("cos 15° = কত?", "(√3 + 1)/(2√2)", ["(√3 − 1)/(2√2)", "√3/2", "1/2"], "cos(45° − 30°)।", M),
 ("tan 15° = কত?", "2 − √3", ["2 + √3", "√3 − 1", "1/√3"], "tan(45° − 30°)।", M),
 ("tan 75° = কত?", "2 + √3", ["2 − √3", "√3 + 1", "√3"], "tan(45° + 30°)।", M),
 ("sin(A + B) sin(A − B) = কত?", "sin²A − sin²B", ["sin²A + sin²B", "cos²A − sin²B", "sin²B − sin²A"], "", H),
]
def e_tan_sum(b):
    p, q = F(R.randint(1, 5), R.choice([1, 2, 3])), F(R.randint(1, 5), R.choice([1, 2, 3, 4]))
    if p * q == 1: return
    v = (p + q) / (1 - p * q)
    b.add(f"tan A = {fr(p)} ও tan B = {fr(q)} হলে tan(A + B) = কত?", num(v), W(num(v), [num((p - q) / (1 + p * q)), num(p + q), num((p + q) / (1 + p * q))]), "(tan A + tan B)/(1 − tan A tan B)।", E)
def e_val(b):
    a, c, op = R.choice([(45, 30, '+'), (45, 30, '−'), (60, 45, '+'), (60, 45, '−'), (30, 60, '+'), (90, 30, '+'), (60, 30, '−')])
    d = a + c if op == '+' else a - c
    fn = R.choice(['sin', 'cos'])
    ok = {15: {'sin': '(√3 − 1)/(2√2)', 'cos': '(√3 + 1)/(2√2)'}, 75: {'sin': '(√3 + 1)/(2√2)', 'cos': '(√3 − 1)/(2√2)'}, 105: {'sin': '(√3 + 1)/(2√2)', 'cos': '(1 − √3)/(2√2)'}, 90: {'sin': '1', 'cos': '0'}, 120: {'sin': '√3/2', 'cos': '−1/2'}, 30: {'sin': '1/2', 'cos': '√3/2'}}[d][fn]
    b.add(f"{fn} {a}° cos {c}° {op} cos {a}° sin {c}° = কত?" if fn == 'sin' else f"cos {a}° cos {c}° {'−' if op == '+' else '+'} sin {a}° sin {c}° = কত?", ok, W(ok, ['(√3 + 1)/(2√2)', '(√3 − 1)/(2√2)', '1/2', '√3/2', '0', '1', '(1 − √3)/(2√2)', '−1/2']), f"{fn}({a}° {op} {c}°) = {fn} {d}°।", E)
def m_sin_sum(b):
    (o1, a1, h1), (o2, a2, h2) = R.sample(TRIP, 2)
    v = F(o1 * a2 + a1 * o2, h1 * h2)
    b.add(f"A ও B সূক্ষ্মকোণ, sin A = {o1}/{h1} ও sin B = {o2}/{h2} হলে sin(A + B) = কত?", fr(v), W(fr(v), [fr(F(o1 * a2 - a1 * o2, h1 * h2)) if o1 * a2 != a1 * o2 else '0', fr(F(a1 * a2 - o1 * o2, h1 * h2)) if a1 * a2 > o1 * o2 else fr(F(o1 * o2, h1 * h2)), fr(F(a1 * a2 + o1 * o2, h1 * h2))]), "sin A cos B + cos A sin B।", M)
def m_cos_sum(b):
    (o1, a1, h1), (o2, a2, h2) = R.sample(TRIP, 2)
    v = F(a1 * a2 - o1 * o2, h1 * h2)
    b.add(f"A ও B সূক্ষ্মকোণ, cos A = {a1}/{h1} ও cos B = {a2}/{h2} হলে cos(A + B) = কত?", num(v), W(num(v), [num(F(a1 * a2 + o1 * o2, h1 * h2)), num(F(o1 * a2 + a1 * o2, h1 * h2)), num(-v) if v else '1']), "cos A cos B − sin A sin B।", M)
def m_tan_find(b):
    t = F(R.randint(1, 4), R.randint(1, 4))
    # tan(A + B) = 1 (A + B = 45°), tan A = t ⇒ tan B = (1 − t)/(1 + t)
    v = (1 - t) / (1 + t)
    b.add(f"A + B = 45° এবং tan A = {fr(t)} হলে tan B = কত?", num(v), W(num(v), [num((1 + t) / (1 - t)) if t != 1 else '1', num(1 - t), num(-v) if v else '1']), "tan(A + B) = 1।", M)
def h_prod(b):
    k = R.choice([45, 225])
    b.add(f"A + B = {k}° হলে (1 + tan A)(1 + tan B) = কত?", '2', ['1', '0', '4'], "tan(A + B) = 1 থেকে tan A + tan B + tan A tan B = 1।", H)
    b.add(f"A + B = {k}° হলে (cot A − 1)(cot B − 1) = কত?", '2', ['1', '0', '−2'], "cot(A + B) = 1।", H)
def h_sq(b):
    a, c = R.sample([15, 20, 30, 40, 45, 50, 60], 2)
    b.add(f"sin²{a + c}° − sin²{abs(a - c) if a > c else c - a}° = কত? (sin(A + B)sin(A − B) ব্যবহার করে, A = {max(a, c)}°, B = {min(a, c)}°)", f"sin {2 * max(a, c)}° sin {2 * min(a, c)}°".replace('sin 90°', '1·').replace('1· sin', 'sin') if False else f"sin {2 * max(a, c)}° · sin {2 * min(a, c)}°", ['0', f"cos {2 * max(a, c)}° · cos {2 * min(a, c)}°", f"sin {a + c}°"], "sin²x − sin²y = sin(x + y) sin(x − y)।", H)
def h_tan3(b):
    b.add("A + B + C = π হলে tan A + tan B + tan C = কত?", "tan A · tan B · tan C", ["0", "1", "tan A tan B + tan B tan C + tan C tan A"], "tan(A + B) = −tan C থেকে।", H)
    b.add("A + B + C = π/2 হলে tan A tan B + tan B tan C + tan C tan A = কত?", "1", ["0", "tan A tan B tan C", "−1"], "cot(A + B) = tan C থেকে।", H)
p7b = run('7.B', R, fx7b, [e_tan_sum, e_val], [m_sin_sum, m_cos_sum, m_tan_find], [h_prod, h_sq, h_tan3], caps=(20, 20, 14))

# ---------------- 7.C গুণিতক কোণ ----------------
fx7c = [
 ("sin 2A = কত?", "2 sin A cos A", ["sin²A − cos²A", "2 sin A", "sin A cos A"], "", E), ("cos 2A = কত?", "cos²A − sin²A", ["2 sin A cos A", "sin²A − cos²A", "1 + 2sin²A"], "", E),
 ("tan 2A = কত?", "2 tan A/(1 − tan²A)", ["2 tan A/(1 + tan²A)", "tan²A − 1", "2 tan A"], "", E), ("sin 3A = কত?", "3 sin A − 4 sin³A", ["4 sin³A − 3 sin A", "3 sin A + 4 sin³A", "3 cos A − 4 cos³A"], "", M),
 ("cos 3A = কত?", "4 cos³A − 3 cos A", ["3 cos A − 4 cos³A", "4 sin³A − 3 sin A", "3 cos A + 4 cos³A"], "", M), ("1 − cos 2A = কত?", "2 sin²A", ["2 cos²A", "sin 2A", "cos²A"], "", M),
 ("sin 2A-কে tan A-এর মাধ্যমে প্রকাশ করলে কোনটি?", "2 tan A/(1 + tan²A)", ["2 tan A/(1 − tan²A)", "(1 − tan²A)/(1 + tan²A)", "tan A/(1 + tan²A)"], "", H),
]
def e_s2(b):
    o, a, h = R.choice(TRIP); v = F(2 * o * a, h * h)
    b.add(f"A সূক্ষ্মকোণ ও sin A = {o}/{h} হলে sin 2A = কত?", fr(v), W(fr(v), [fr(F(2 * o, h)), fr(F(a * a - o * o, h * h)) if a > o else fr(F(o * o - a * a, h * h)), fr(F(o * a, h * h))]), "2 sin A cos A।", E)
def e_c2(b):
    o, a, h = R.choice(TRIP); v = F(a * a - o * o, h * h)
    b.add(f"A সূক্ষ্মকোণ ও cos A = {a}/{h} হলে cos 2A = কত?", num(v), W(num(v), [num(-v), num(F(2 * o * a, h * h)), num(F(2 * a, h))]), "cos²A − sin²A।", E)
def m_t2(b):
    t = F(R.randint(1, 5), R.randint(1, 6))
    if t == 1: return
    v = 2 * t / (1 - t * t)
    b.add(f"tan A = {fr(t)} হলে tan 2A = কত?", num(v), W(num(v), [num(2 * t / (1 + t * t)), num(2 * t), num(-v)]), "2 tan A/(1 − tan²A)।", M)
def m_s3(b):
    s = F(R.randint(1, 4), R.randint(2, 5))
    if s >= 1: return
    v = 3 * s - 4 * s ** 3
    b.add(f"sin A = {fr(s)} হলে sin 3A = কত?", num(v), W(num(v), [num(4 * s ** 3 - 3 * s), num(3 * s), num(3 * s + 4 * s ** 3)]), "3 sin A − 4 sin³A।", M)
def m_c3(b):
    c = F(R.randint(1, 4), R.randint(2, 5))
    if c >= 1: return
    v = 4 * c ** 3 - 3 * c
    b.add(f"cos A = {fr(c)} হলে cos 3A = কত?", num(v), W(num(v), [num(3 * c - 4 * c ** 3), num(3 * c), num(4 * c ** 3 + 3 * c)]), "4 cos³A − 3 cos A।", M)
def m_val(b):
    q, ok = R.choice([("2 sin 15° cos 15°", '1/2'), ("cos²15° − sin²15°", '√3/2'), ("2 cos²22.5° − 1", '1/√2'), ("1 − 2 sin²15°", '√3/2'), ("2 tan 22.5°/(1 − tan²22.5°)", '1'), ("3 sin 10° − 4 sin³10°", '1/2'), ("4 cos³20° − 3 cos 20°", '1/2'), ("2 sin 22.5° cos 22.5°", '1/√2'), ("cos²75° − sin²75°", '−√3/2')])
    b.add(f"{q} = কত?", ok, W(ok, ['1/2', '√3/2', '1/√2', '1', '−√3/2', '0']), "গুণিতক কোণের সূত্র।", M)
def h_tan_via(b):
    t = F(R.randint(1, 4), R.randint(1, 5))
    v = (1 - t * t) / (1 + t * t)
    b.add(f"tan A = {fr(t)} হলে cos 2A = কত?", num(v), W(num(v), [num(2 * t / (1 + t * t)), num((1 + t * t) / (1 - t * t)) if t != 1 else '1', num(-v) if v else '1']), "(1 − tan²A)/(1 + tan²A)।", H)
def h_ident(b):
    q, ok = R.choice([("(sin 2A)/(1 + cos 2A)", 'tan A'), ("(1 − cos 2A)/sin 2A", 'tan A'), ("(1 + cos 2A)/sin 2A", 'cot A'), ("(1 − cos 2A)/(1 + cos 2A)", 'tan²A'), ("sin 2A/(1 − cos 2A)", 'cot A'), ("cos⁴A − sin⁴A", 'cos 2A'), ("(cos A + sin A)²", '1 + sin 2A')])
    b.add(f"{q} = কত?", ok, W(ok, ['tan A', 'cot A', 'tan²A', 'cos 2A', '1 + sin 2A', 'sin 2A']), "সূত্র প্রয়োগ।", H)
def h_sin18(b):
    b.add("sin 18° = কত?", "(√5 − 1)/4", ["(√5 + 1)/4", "√5/4", "1/4"], "sin 2θ = cos 3θ, θ = 18°।", H)
    b.add("cos 36° = কত?", "(√5 + 1)/4", ["(√5 − 1)/4", "√3/2", "1/2"], "cos 36° = 1 − 2sin²18°।", H)
p7c = run('7.C', R, fx7c, [e_s2, e_c2], [m_t2, m_s3, m_c3, m_val], [h_tan_via, h_ident, h_sin18], caps=(16, 13, 10))

# ---------------- 7.D উপগুণিতক কোণ ----------------
fx7d = [
 ("sin A = কত (A/2-এর মাধ্যমে)?", "2 sin(A/2) cos(A/2)", ["sin²(A/2) − cos²(A/2)", "2 sin(A/2)", "sin(A/2)cos(A/2)"], "", E),
 ("1 + cos A = কত?", "2 cos²(A/2)", ["2 sin²(A/2)", "sin A", "cos²(A/2)"], "", E), ("1 − cos A = কত?", "2 sin²(A/2)", ["2 cos²(A/2)", "sin A", "sin²(A/2)"], "", E),
 ("tan(A/2) = কত?", "sin A/(1 + cos A)", ["sin A/(1 − cos A)", "(1 + cos A)/sin A", "cos A/(1 + sin A)"], "", M),
 ("cos 22.5° = কত?", "√(2 + √2)/2", ["√(2 − √2)/2", "1/√2", "√3/2"], "cos²22.5° = (1 + cos 45°)/2।", M), ("sin 22.5° = কত?", "√(2 − √2)/2", ["√(2 + √2)/2", "1/√2", "1/2"], "", M),
 ("tan 22.5° = কত?", "√2 − 1", ["√2 + 1", "1/√2", "2 − √3"], "(1 − cos 45°)/sin 45°।", M),
]
def e_half(b):
    o, a, h = R.choice(TRIP)
    v = F(h - a, 2 * h)
    b.add(f"A সূক্ষ্মকোণ ও cos A = {a}/{h} হলে sin²(A/2) = কত?", fr(v), W(fr(v), [fr(F(h + a, 2 * h)), fr(F(h - a, h)), fr(F(a, 2 * h))]), "(1 − cos A)/2।", E)
def e_half_c(b):
    o, a, h = R.choice(TRIP)
    v = F(h + a, 2 * h)
    b.add(f"A সূক্ষ্মকোণ ও cos A = {a}/{h} হলে cos²(A/2) = কত?", fr(v), W(fr(v), [fr(F(h - a, 2 * h)), fr(F(h + a, h)), fr(F(a, 2 * h))]), "(1 + cos A)/2।", E)
def m_tanh(b):
    o, a, h = R.choice(TRIP)
    v = F(o, h + a)
    b.add(f"A সূক্ষ্মকোণ ও sin A = {o}/{h} হলে tan(A/2) = কত?", fr(v), W(fr(v), [fr(F(o, h - a)), fr(F(o, a)), fr(F(h - a, o)) if F(h - a, o) != v else fr(v * 2)]), "sin A/(1 + cos A)।", M)
def m_sqrt(b):
    o, a, h = R.choice(TRIP)
    v2 = F(h - a, 2 * h); r1, r2 = math.isqrt(v2.numerator), math.isqrt(v2.denominator)
    if r1 * r1 != v2.numerator or r2 * r2 != v2.denominator: return
    v = F(r1, r2)
    b.add(f"A সূক্ষ্মকোণ ও cos A = {a}/{h} হলে sin(A/2) = কত?", fr(v), W(fr(v), [fr(v2), fr(F(math.isqrt(h + a), math.isqrt(2 * h))) if math.isqrt(h + a) ** 2 == h + a and math.isqrt(2 * h) ** 2 == 2 * h else fr(v + F(1, 5)), fr(1 - v)]), "√((1 − cos A)/2)।", M)
def m_tan_from_t(b):
    t = F(R.randint(1, 3), R.randint(2, 5))
    if t >= 1: return
    v = 2 * t / (1 + t * t); w = (1 - t * t) / (1 + t * t)
    fn = R.choice(['sin', 'cos'])
    ans = v if fn == 'sin' else w
    b.add(f"tan(A/2) = {fr(t)} হলে {fn} A = কত?", fr(ans), W(fr(ans), [fr(w if fn == 'sin' else v), fr(2 * t / (1 - t * t)), fr(ans + F(1, 10))]), "2t/(1 + t²) ও (1 − t²)/(1 + t²)।", M)
def h_expr(b):
    q, ok = R.choice([("(1 − cos A)/sin A", 'tan(A/2)'), ("(1 + cos A)/sin A", 'cot(A/2)'), ("√((1 + cos A)/2) (A সূক্ষ্মকোণ)", 'cos(A/2)'), ("sin A/(1 − cos A)", 'cot(A/2)'), ("(1 + sin A − cos A)/(1 + sin A + cos A)", 'tan(A/2)')])
    b.add(f"{q} = কত?", ok, W(ok, ['tan(A/2)', 'cot(A/2)', 'cos(A/2)', 'sin(A/2)', 'tan A']), "উপগুণিতক কোণের সূত্র।", H)
def h_num(b):
    q, ok = R.choice([("2 cos²(π/8) − 1", '1/√2'), ("1 − 2 sin²(π/12)", '√3/2'), ("tan(π/8) + cot(π/8)", '2√2'), ("cot 22.5° − tan 22.5°", '2'), ("sin(π/8) cos(π/8)", '1/(2√2)')])
    b.add(f"{q} = কত?", ok, W(ok, ['1/√2', '√3/2', '2√2', '2', '1/(2√2)', '1']), "", H)
def h_q2(b):
    o, a, h = R.choice(TRIP)
    v = F(o, h - a)
    b.add(f"A দ্বিতীয় চতুর্ভাগের কোণ এবং sin A = {o}/{h} হলে tan(A/2) = কত?", fr(v), W(fr(v), [fr(F(o, h + a)), fr(F(h - a, o)), fr(F(o, a)), fr(v + 1)]), f"cos A = −{a}/{h}; tan(A/2) = sin A/(1 + cos A) = {o}/{h - a}।", H)
p7d = run('7.D', R, fx7d, [e_half, e_half_c], [m_tanh, m_sqrt, m_tan_from_t], [h_expr, h_num, h_q2], caps=(16, 18, 12))

# ---------------- 7.E রূপান্তর ----------------
fx7e = [
 ("sin C + sin D = কত?", "2 sin((C + D)/2) cos((C − D)/2)", ["2 cos((C + D)/2) sin((C − D)/2)", "2 cos((C + D)/2) cos((C − D)/2)", "2 sin((C + D)/2) sin((C − D)/2)"], "", E),
 ("cos C + cos D = কত?", "2 cos((C + D)/2) cos((C − D)/2)", ["2 sin((C + D)/2) sin((C − D)/2)", "2 sin((C + D)/2) cos((C − D)/2)", "−2 sin((C + D)/2) sin((C − D)/2)"], "", E),
 ("cos C − cos D = কত?", "−2 sin((C + D)/2) sin((C − D)/2)", ["2 sin((C + D)/2) sin((C − D)/2)", "2 cos((C + D)/2) cos((C − D)/2)", "2 cos((C + D)/2) sin((C − D)/2)"], "", M),
 ("2 sin A cos B = কত?", "sin(A + B) + sin(A − B)", ["cos(A + B) + cos(A − B)", "sin(A + B) − sin(A − B)", "cos(A − B) − cos(A + B)"], "", E),
 ("2 sin A sin B = কত?", "cos(A − B) − cos(A + B)", ["cos(A + B) − cos(A − B)", "sin(A + B) + sin(A − B)", "cos(A + B) + cos(A − B)"], "", M),
 ("2 cos A cos B = কত?", "cos(A + B) + cos(A − B)", ["cos(A − B) − cos(A + B)", "sin(A + B) + sin(A − B)", "sin(A + B) − sin(A − B)"], "", E),
]
def e_num(b):
    q, ok = R.choice([("sin 75° + sin 15°", '√3/√2'), ("sin 75° − sin 15°", '1/√2'), ("cos 75° + cos 15°", '√3/√2'), ("cos 15° − cos 75°", '1/√2'), ("sin 105° + sin 15°", '√3/√2'), ("cos 20° + cos 100° + cos 140°", '0'), ("sin 50° − sin 70° + sin 10°", '0'), ("2 sin 75° cos 15°", '1 + √3/2'), ("2 cos 75° cos 15°", '1/2'), ("2 sin 75° sin 15°", '1/2')])
    b.add(f"{q} = কত?", ok, W(ok, ['√3/√2', '1/√2', '0', '1/2', '√3/2', '1 + √3/2', '1']), "রূপান্তর সূত্র।", E)
def m_ratio(b):
    A, B = R.sample([10, 20, 30, 40, 50, 60, 70, 80], 2)
    if (A + B) % 2: return
    ok = f"tan {(A + B) // 2}°" if True else ''
    b.add(f"(sin {A}° + sin {B}°)/(cos {A}° + cos {B}°) = কত?", ok, W(ok, [f"cot {(A + B) // 2}°", f"tan {abs(A - B) // 2}°", f"tan {A + B}°"]), "tan((A + B)/2)।", M)
def m_prod(b):
    A, B = R.sample(range(10, 80, 5), 2)
    if A < B: A, B = B, A
    ok = f"sin {A + B}° + sin {A - B}°"
    b.add(f"2 sin {A}° cos {B}°-কে যোগফল আকারে লিখলে কোনটি?", ok, W(ok, [f"sin {A + B}° − sin {A - B}°", f"cos {A + B}° + cos {A - B}°", f"cos {A - B}° − cos {A + B}°"]), "2 sin A cos B সূত্র।", M)
def m_sum(b):
    A, B = R.sample(range(10, 80, 10), 2)
    if A < B: A, B = B, A
    ok = f"2 cos {(A + B) // 2}° cos {(A - B) // 2}°"
    if (A + B) % 2: return
    b.add(f"cos {A}° + cos {B}°-কে গুণফল আকারে লিখলে কোনটি?", ok, W(ok, [f"2 sin {(A + B) // 2}° sin {(A - B) // 2}°", f"2 sin {(A + B) // 2}° cos {(A - B) // 2}°", f"−2 sin {(A + B) // 2}° sin {(A - B) // 2}°"]), "cos C + cos D সূত্র।", M)
def h_tri(b):
    q, ok = R.choice([("ABC ত্রিভুজে sin A + sin B + sin C", "4 cos(A/2) cos(B/2) cos(C/2)"), ("ABC ত্রিভুজে cos A + cos B + cos C", "1 + 4 sin(A/2) sin(B/2) sin(C/2)"), ("ABC ত্রিভুজে sin 2A + sin 2B + sin 2C", "4 sin A sin B sin C"), ("ABC ত্রিভুজে cos 2A + cos 2B + cos 2C", "−1 − 4 cos A cos B cos C")])
    b.add(f"{q} = কত?", ok, W(ok, ["4 cos(A/2) cos(B/2) cos(C/2)", "1 + 4 sin(A/2) sin(B/2) sin(C/2)", "4 sin A sin B sin C", "−1 − 4 cos A cos B cos C", "0"]), "A + B + C = π।", H)
def h_num2(b):
    q, ok = R.choice([("cos 20° cos 40° cos 80°", '1/8'), ("sin 20° sin 40° sin 80°", '√3/8'), ("cos 10° cos 50° cos 70°", '√3/8'), ("sin 10° sin 50° sin 70°", '1/8'), ("tan 20° tan 40° tan 80°", '√3')])
    b.add(f"{q} = কত?", ok, W(ok, ['1/8', '√3/8', '√3', '1/4', '1/16']), "রূপান্তর ও 3θ সূত্র।", H)
def e_gen(b):
    A, B = R.sample(range(10, 85, 5), 2)
    if A < B: A, B = B, A
    t = R.choice(['cc', 'ss', 'sc'])
    if t == 'cc': q, ok, ws = f"2 cos {A}° cos {B}°", f"cos {A + B}° + cos {A - B}°", [f"cos {A - B}° − cos {A + B}°", f"sin {A + B}° + sin {A - B}°", f"cos {A + B}° − cos {A - B}°"]
    elif t == 'ss': q, ok, ws = f"2 sin {A}° sin {B}°", f"cos {A - B}° − cos {A + B}°", [f"cos {A + B}° + cos {A - B}°", f"cos {A + B}° − cos {A - B}°", f"sin {A + B}° − sin {A - B}°"]
    else: q, ok, ws = f"2 cos {A}° sin {B}°", f"sin {A + B}° − sin {A - B}°", [f"sin {A + B}° + sin {A - B}°", f"cos {A - B}° − cos {A + B}°", f"cos {A + B}° + cos {A - B}°"]
    b.add(f"{q}-কে যোগফল/অন্তর আকারে লিখলে কোনটি?", ok, ws, "গুণফল থেকে যোগফলের সূত্র।", E)
def h_gen(b):
    A, B = R.sample(range(10, 170, 10), 2)
    if A < B: A, B = B, A
    t = R.choice([0, 1])
    if t == 0: q, ok, ws = f"(sin {A}° + sin {B}°)/(sin {A}° − sin {B}°)", f"tan {(A + B) // 2}° cot {(A - B) // 2}°", [f"cot {(A + B) // 2}° tan {(A - B) // 2}°", f"tan {(A + B) // 2}° tan {(A - B) // 2}°", f"tan {A + B}°"]
    else: q, ok, ws = f"(cos {B}° − cos {A}°)/(sin {A}° − sin {B}°)", f"tan {(A + B) // 2}°", [f"cot {(A + B) // 2}°", f"tan {(A - B) // 2}°", f"−tan {(A + B) // 2}°"]
    b.add(f"{q} = কত?", ok, ws, "যোগফল-গুণফল রূপান্তর।", H)
p7e = run('7.E', R, fx7e, [e_num, e_gen], [m_ratio, m_prod, m_sum], [h_tri, h_num2, h_gen], caps=(30, 20, 14))

# ---------------- 7.F ত্রিভুজের ত্রিকোণমিতি ----------------
TRI = [(a, b_, c) for a in range(3, 16) for b_ in range(a, 16) for c in range(b_, 16) if a + b_ > c]
fx7f = [
 ("সাইন সূত্র অনুযায়ী a/sin A = কত?", "b/sin B = c/sin C = 2R", ["b/cos B", "2r", "c/tan C"], "R পরিব্যাসার্ধ।", E),
 ("কোসাইন সূত্র অনুযায়ী cos A = কত?", "(b² + c² − a²)/(2bc)", ["(a² + b² − c²)/(2ab)", "(b² + c² + a²)/(2bc)", "(a² − b² − c²)/(2bc)"], "", E),
 ("ত্রিভুজের ক্ষেত্রফল কোনটি?", "½ bc sin A", ["½ bc cos A", "bc sin A", "½ ab cos C"], "", E),
 ("ত্রিভুজে a cos B + b cos A = কত?", "c", ["a", "b", "a + b"], "অভিক্ষেপ সূত্র।", M),
]
def e_cos(b):
    a, c, d = R.choice(TRI); v = F(c * c + d * d - a * a, 2 * c * d)
    b.add(f"ABC ত্রিভুজে a = {a}, b = {c}, c = {d} হলে cos A = কত?", num(v), W(num(v), [num(F(a * a + c * c - d * d, 2 * a * c)), num(-v) if v else '1', num(F(c * c + d * d + a * a, 2 * c * d))]), "(b² + c² − a²)/(2bc)।", E)
def e_area(b):
    a, c = R.randint(2, 12), R.randint(2, 12); A, s = R.choice([(30, F(1, 2)), (90, F(1)), (150, F(1, 2))])
    v = F(a * c, 2) * s
    b.add(f"ABC ত্রিভুজে b = {a}, c = {c} এবং A = {A}° হলে ক্ষেত্রফল কত?", fr(v), W(fr(v), [fr(F(a * c, 2)), fr(v * 2), str(a * c)]), "½ bc sin A।", E)
def m_angle(b):
    tri, ang = R.choice([((3, 5, 7), '120°'), ((5, 7, 8), '60°'), ((3, 7, 8), '60°'), ((7, 8, 13), '120°'), ((5, 8, 7), '60°'), ((3, 4, 5), '90°'), ((1, 1, 1), '60°')])
    a, c, d = tri
    big = max(tri)
    b.add(f"ত্রিভুজের বাহুগুলো {a}, {c}, {d} হলে {'বৃহত্তম' if ang != '60°' or tri == (1, 1, 1) else 'মধ্যম বাহুর বিপরীত'} কোণ কত?".replace('মধ্যম বাহুর বিপরীত', f'{sorted(tri)[1] if ang == "60°" and tri != (1, 1, 1) else big} বাহুর বিপরীত'), ang, W(ang, ['30°', '45°', '60°', '90°', '120°', '150°']), "কোসাইন সূত্র।", M)
def m_sine(b):
    a, A, B = R.randint(2, 12), *R.choice([(30, 90), (90, 30), (30, 150), (45, 90), (90, 45), (30, 45), (45, 30), (60, 90)])
    sA, sB = math.sin(math.radians(A)), math.sin(math.radians(B))
    v = a * sB / sA
    s = {(30, 90): f"{2 * a}", (90, 30): fr(F(a, 2)), (30, 150): str(a), (45, 90): f"{a}√2" if a > 1 else '√2', (90, 45): f"{a}/√2", (30, 45): f"{a}√2" if a > 1 else '√2', (45, 30): f"{a}/√2", (60, 90): f"{2 * a}/√3"}[(A, B)]
    b.add(f"ABC ত্রিভুজে a = {a}, A = {A}° ও B = {B}° হলে b = কত?", s, W(s, [str(a), f"{2 * a}", fr(F(a, 2)), f"{a}√3", f"{a}/√2", f"{a}√2"]), "a/sin A = b/sin B।", M)
def m_R(b):
    a, A = R.randint(2, 12), R.choice([30, 90, 150])
    v = F(a, 2) / {30: F(1, 2), 90: F(1), 150: F(1, 2)}[A]
    b.add(f"ABC ত্রিভুজে a = {a} এবং A = {A}° হলে পরিব্যাসার্ধ R = কত?", fr(v), W(fr(v), [fr(v * 2), fr(v / 2), str(a * 2) if a * 2 != v else str(a + 1)]), "a/sin A = 2R।", M)
def h_side(b):
    c, d, A, ok = R.choice([(3, 5, 120, '7'), (5, 8, 60, '7'), (3, 8, 60, '7'), (7, 8, 120, '13'), (5, 3, 60, '√19'), (2, 3, 60, '√7'), (4, 6, 60, '2√7'), (1, 1, 120, '√3'), (2, 2, 90, '2√2')])
    b.add(f"ABC ত্রিভুজে b = {c}, c = {d} এবং A = {A}° হলে a = কত?", ok, W(ok, ['7', '13', '√19', '√7', '2√7', '√3', '2√2', '5']), "a² = b² + c² − 2bc cos A।", H)
def h_type(b):
    q, ok = R.choice([("a cos A = b cos B হলে ত্রিভুজটি", 'সমদ্বিবাহু অথবা সমকোণী'), ("sin²A + sin²B = sin²C হলে ত্রিভুজটি", 'সমকোণী'), ("a = 2b cos C হলে ত্রিভুজটি", 'সমদ্বিবাহু'), ("cos A = sin B/(2 sin C) হলে ত্রিভুজটি", 'সমদ্বিবাহু')])
    b.add(f"ABC ত্রিভুজে {q} কেমন?", ok, W(ok, ['সমবাহু', 'সমদ্বিবাহু', 'সমকোণী', 'সমদ্বিবাহু অথবা সমকোণী', 'স্থূলকোণী']), "সাইন/কোসাইন সূত্রে রূপান্তর।", H)
def h_heron(b):
    a, c, d = R.choice([(13, 14, 15), (5, 12, 13), (6, 8, 10), (9, 10, 17), (10, 13, 13), (7, 15, 20), (5, 5, 6), (5, 5, 8)])
    s = F(a + c + d, 2); A = math.isqrt(int(s * (s - a) * (s - c) * (s - d)))
    b.add(f"ত্রিভুজের বাহু {a}, {c}, {d} হলে ক্ষেত্রফল কত?", A, W(A, [A * 2, A + 2, int(s)]), "হেরনের সূত্র।", H)
p7f = run('7.F', R, fx7f, [e_cos, e_area], [m_angle, m_sine, m_R], [h_side, h_type, h_heron], caps=(16, 18, 12))

# ---------------- 7.G ত্রিকোণমিতিক সমীকরণ ----------------
def degset(ds): return '{' + ', '.join(rad(d) for d in sorted(ds)) + '}'
TG = {'sin': [('1/2', .5), ('√3/2', 3 ** .5 / 2), ('1/√2', 2 ** -.5), ('−1/2', -.5), ('−√3/2', -(3 ** .5) / 2), ('−1/√2', -(2 ** -.5)), ('1', 1), ('−1', -1), ('0', 0)],
      'cos': [('1/2', .5), ('√3/2', 3 ** .5 / 2), ('1/√2', 2 ** -.5), ('−1/2', -.5), ('−√3/2', -(3 ** .5) / 2), ('−1/√2', -(2 ** -.5)), ('1', 1), ('−1', -1), ('0', 0)],
      'tan': [('1', 1), ('√3', 3 ** .5), ('1/√3', 3 ** -.5), ('−1', -1), ('−√3', -(3 ** .5)), ('−1/√3', -(3 ** -.5)), ('0', 0)]}
def solve(fn, v, lo=0, hi=360):
    out = []
    for d in range(lo, hi, 15):
        if fn == 'tan' and d % 180 == 90: continue
        if abs(F3[fn](_m.radians(d)) - v) < 1e-9: out.append(d)
    return out
fx7g = [
 ("sin θ = 0-এর সাধারণ সমাধান কোনটি?", "θ = nπ", ["θ = (2n + 1)π/2", "θ = 2nπ", "θ = nπ/2"], "", E), ("cos θ = 0-এর সাধারণ সমাধান কোনটি?", "θ = (2n + 1)π/2", ["θ = nπ", "θ = 2nπ", "θ = nπ/4"], "", E),
 ("sin θ = sin α-এর সাধারণ সমাধান কোনটি?", "θ = nπ + (−1)ⁿα", ["θ = 2nπ ± α", "θ = nπ + α", "θ = nπ − α"], "", M), ("cos θ = cos α-এর সাধারণ সমাধান কোনটি?", "θ = 2nπ ± α", ["θ = nπ + (−1)ⁿα", "θ = nπ + α", "θ = 2nπ + α"], "", M),
 ("tan θ = tan α-এর সাধারণ সমাধান কোনটি?", "θ = nπ + α", ["θ = 2nπ ± α", "θ = nπ + (−1)ⁿα", "θ = 2nπ + α"], "", M),
]
def e_basic(b):
    fn = R.choice(['sin', 'cos', 'tan']); t, v = R.choice(TG[fn]); ds = solve(fn, v, 0, 91)
    if len(ds) != 1: return
    b.add(f"{fn} θ = {t} এবং 0 ≤ θ ≤ π/2 হলে θ = কত?", rad(ds[0]), W(rad(ds[0]), ['0', 'π/6', 'π/4', 'π/3', 'π/2']), "", E)
def m_full(b):
    fn = R.choice(['sin', 'cos', 'tan']); t, v = R.choice(TG[fn]); ds = solve(fn, v)
    if len(ds) != 2: return
    cands = [[ds[0], (180 - ds[0]) % 360], [ds[0], (ds[0] + 180) % 360], [ds[0]], [(ds[0] + 90) % 360, (ds[1] + 90) % 360], [(360 - ds[0]) % 360, (360 - ds[1]) % 360], [(ds[0] + 30) % 360, (ds[1] + 30) % 360]]
    b.add(f"{fn} θ = {t} (0 ≤ θ < 2π) সমীকরণের সমাধান সেট কোনটি?", degset(ds), W(degset(ds), [degset(set(c)) for c in cands if set(c) != set(ds)]), "যে দুই চতুর্ভাগে চিহ্ন মেলে।", M)
def m_gen(b):
    fn, t, v = R.choice([('sin', '1/2', 30), ('sin', '√3/2', 60), ('sin', '1/√2', 45), ('cos', '1/2', 60), ('cos', '√3/2', 30), ('cos', '1/√2', 45), ('tan', '1', 45), ('tan', '√3', 60), ('tan', '1/√3', 30)])
    a = rad(v); ok = {'sin': f"θ = nπ + (−1)ⁿ{a}", 'cos': f"θ = 2nπ ± {a}", 'tan': f"θ = nπ + {a}"}[fn]
    b.add(f"{fn} θ = {t}-এর সাধারণ সমাধান কোনটি? (n ∈ Z)", ok, W(ok, [f"θ = nπ + (−1)ⁿ{a}", f"θ = 2nπ ± {a}", f"θ = nπ + {a}", f"θ = 2nπ + {a}"]), "", M)
def m_count(b):
    fn = R.choice(['sin', 'cos']); t, v = R.choice(TG[fn][:6]); k = R.choice([1, 2])
    n = sum(1 for d in range(0, 360 * k, 15) if abs(F3[fn](_m.radians(d)) - v) < 1e-9)
    b.add(f"0 ≤ θ < {'2π' if k == 1 else '4π'} ব্যবধিতে {fn} θ = {t}-এর কয়টি সমাধান?", n, W(n, [n // 2, n + 1, n * 2]), "", M)
def h_quad(b):
    fn = R.choice(['sin', 'cos'])
    (v1, v2), eq = R.choice([((1, .5), '2{f}²θ − 3{f}θ + 1 = 0'), ((-1, .5), '2{f}²θ + {f}θ − 1 = 0'), ((1, -.5), '2{f}²θ − {f}θ − 1 = 0'), ((-1, -.5), '2{f}²θ + 3{f}θ + 1 = 0')])
    ds = sorted(set(solve(fn, v1) + solve(fn, v2))); alt = sorted(set(solve(fn, -v1) + solve(fn, -v2)))
    b.add(f"{eq.format(f=fn)} (0 ≤ θ < 2π) সমীকরণের সমাধান সেট কোনটি?", degset(ds), W(degset(ds), [degset(alt), degset(solve(fn, v2)), degset(solve(fn, v1))]), "দ্বিঘাত হিসেবে উৎপাদকে বিশ্লেষণ।", H)
def h_mix(b):
    q, ds = R.choice([("sin θ + cos θ = 1", [0, 90]), ("sin θ − cos θ = 0", [45, 225]), ("tan θ + cot θ = 2", [45, 225]), ("sin 2θ = cos θ", [30, 90, 150, 270]), ("cos 2θ = cos θ", [0, 120, 240]), ("√3 cos θ + sin θ = 2", [30])])
    alts = [[45, 135], [0, 180], [60, 300], [30, 150], [90, 270], [60, 120]]
    b.add(f"{q} (0 ≤ θ < 2π) সমীকরণের সমাধান কোনটি?", degset(ds), W(degset(ds), [degset(a) for a in alts if a != ds]), "রূপান্তর করে সমাধান।", H)
def e_deg(b):
    fn = R.choice(['sin', 'cos', 'tan']); t, v = R.choice(TG[fn]); ds = solve(fn, v, 0, 91)
    if len(ds) != 1: return
    b.add(f"{fn} θ = {t} এবং 0° ≤ θ ≤ 90° হলে θ = কত ডিগ্রি?", f"{ds[0]}°", W(f"{ds[0]}°", ['0°', '30°', '45°', '60°', '90°']), "", E)
def e_two(b):
    fn = R.choice(['sin', 'cos']); k = R.choice([2, 3]); t, v = R.choice([('1/2', .5), ('0', 0), ('1', 1)])
    ds = [d for d in range(0, 91, 5) if abs(F3[fn](_m.radians(k * d)) - v) < 1e-9]
    if len(ds) != 1: return
    b.add(f"{fn} {k}θ = {t} এবং 0° ≤ θ ≤ {90 // k}° হলে θ = কত?", f"{ds[0]}°", W(f"{ds[0]}°", ['0°', '10°', '15°', '20°', '30°', '45°']), "", E)
def h_sec(b):
    fn = R.choice(['sec', 'cosec']); t, v = R.choice([('2', .5), ('−2', -.5), ('√2', 2 ** -.5), ('−√2', -(2 ** -.5)), ('2/√3', 3 ** .5 / 2), ('−2/√3', -(3 ** .5) / 2)])
    base = 'cos' if fn == 'sec' else 'sin'; ds = solve(base, v)
    b.add(f"{fn} θ = {t} (0 ≤ θ < 2π) সমীকরণের সমাধান সেট কোনটি?", degset(ds), W(degset(ds), [degset(solve('sin' if base == 'cos' else 'cos', v)), degset([(d + 180) % 360 for d in ds]), degset(ds[:1])]), f"{base} θ = 1/{fn} θ।", H)
p7g = run('7.G', R, fx7g, [e_basic, e_deg, e_two], [m_full, m_gen, m_count], [h_quad, h_mix, h_sec], caps=(30, 18, 14))
save('i7', p7a + p7b + p7c + p7d + p7e + p7f + p7g)

# ---------------- 8 ফাংশন ও লেখচিত্র ----------------
fx8 = [
 ("f(−x) = f(x) হলে f কোন ধরনের ফাংশন?", "জোড় ফাংশন", ["বিজোড় ফাংশন", "এক-এক ফাংশন", "ধ্রুবক ফাংশন"], "y-অক্ষ সাপেক্ষে প্রতিসম।", E),
 ("f(−x) = −f(x) হলে f কোন ধরনের ফাংশন?", "বিজোড় ফাংশন", ["জোড় ফাংশন", "পর্যাবৃত্ত ফাংশন", "ধ্রুবক ফাংশন"], "মূলবিন্দু সাপেক্ষে প্রতিসম।", E),
 ("কোনটি জোড় ফাংশন?", "cos x", ["sin x", "tan x", "x³"], "cos(−x) = cos x।", E), ("কোনটি বিজোড় ফাংশন?", "sin x", ["cos x", "x²", "|x|"], "", E),
 ("y = f(x) + k-এর লেখচিত্র y = f(x)-কে কীভাবে সরিয়ে পাওয়া যায়?", "k একক উপরে (k > 0)", ["k একক ডানে", "k একক বামে", "k গুণ প্রসারিত"], "উল্লম্ব স্থানান্তর।", M),
 ("y = f(x − h)-এর লেখচিত্র y = f(x)-কে কীভাবে সরিয়ে পাওয়া যায়?", "h একক ডানে (h > 0)", ["h একক বামে", "h একক উপরে", "h একক নিচে"], "আনুভূমিক স্থানান্তর।", M),
 ("sin x ফাংশনের পর্যায় কত?", "2π", ["π", "π/2", "4π"], "", E), ("tan x ফাংশনের পর্যায় কত?", "π", ["2π", "π/2", "4π"], "", E),
 ("y = sin⁻¹x-এর ডোমেন কোনটি?", "[−1, 1]", ["R", "[0, π]", "(−1, 1)"], "", M), ("y = sin⁻¹x-এর রেঞ্জ কোনটি?", "[−π/2, π/2]", ["[0, π]", "R", "(−π/2, π/2)"], "মুখ্য মান।", M),
 ("y = cos⁻¹x-এর রেঞ্জ কোনটি?", "[0, π]", ["[−π/2, π/2]", "R", "[−1, 1]"], "", M), ("y = eˣ-এর রেঞ্জ কোনটি?", "(0, ∞)", ["R", "[0, ∞)", "(1, ∞)"], "", E),
 ("y = ln x-এর ডোমেন কোনটি?", "(0, ∞)", ["R", "[0, ∞)", "(1, ∞)"], "", E),
]
def e_val(b):
    a, c, k = nz(-4, 5), R.randint(-6, 6), R.randint(-3, 4)
    v = a * k * k + c
    b.add(f"f(x) = {px({2: a, 0: c})} হলে f({num(k)}) = কত?", num(v), [num(w) for w in near(v)], "", E)
def e_dom(b):
    a = R.randint(-6, 8); kind = R.choice(['sqrt', 'frac', 'log'])
    q = {'sqrt': f"√(x {'−' if a >= 0 else '+'} {abs(a)})", 'frac': f"1/(x {'−' if a >= 0 else '+'} {abs(a)})", 'log': f"ln(x {'−' if a >= 0 else '+'} {abs(a)})"}[kind].replace('(x − 0)', 'x').replace('(x + 0)', 'x')
    ok = {'sqrt': f"[{num(a)}, ∞)", 'frac': f"R − {{{num(a)}}}", 'log': f"({num(a)}, ∞)"}[kind]
    b.add(f"f(x) = {q} ফাংশনের ডোমেন কোনটি?", ok, W(ok, [f"[{num(a)}, ∞)", f"({num(a)}, ∞)", f"R − {{{num(a)}}}", f"(−∞, {num(a)}]", "R"]), "সংজ্ঞায়িত হওয়ার শর্ত।", E)
def m_inv(b):
    a, c = R.choice([2, 3, 4, 5]), nz(-7, 7)
    ok = f"(x {'−' if c > 0 else '+'} {abs(c)})/{a}"
    b.add(f"f(x) = {px({1: a, 0: c})} হলে f⁻¹(x) = কত?", ok, W(ok, [f"(x {'+' if c > 0 else '−'} {abs(c)})/{a}", px({1: a, 0: -c}), f"1/({px({1: a, 0: c})})"]), "y = f(x) থেকে x নির্ণয়।", M)
def m_comp(b):
    a, c, p, q = R.randint(1, 4), R.randint(-5, 5), R.randint(1, 4), R.randint(-5, 5); k = R.randint(-3, 4)
    g = p * k + q; v = a * g + c; w = p * (a * k + c) + q
    if v == w: return
    b.add(f"f(x) = {px({1: a, 0: c})}, g(x) = {px({1: p, 0: q})} হলে (f∘g)({num(k)}) = কত?", num(v), W(num(v), [num(w), num(v + 1), num(g)]), "", M)
def m_range(b):
    a, k = R.randint(1, 4), R.randint(-6, 6); kind = R.choice(['sq', 'abs', 'sin', 'cos'])
    q, ok = {'sq': (f"{co(a, 'x²')} {'+' if k >= 0 else '−'} {abs(k)}", f"[{num(k)}, ∞)"), 'abs': (f"{co(a, '|x|')} {'+' if k >= 0 else '−'} {abs(k)}", f"[{num(k)}, ∞)"), 'sin': (f"{co(a, 'sin x')} {'+' if k >= 0 else '−'} {abs(k)}", f"[{num(k - a)}, {num(k + a)}]"), 'cos': (f"{co(a, 'cos x')} {'+' if k >= 0 else '−'} {abs(k)}", f"[{num(k - a)}, {num(k + a)}]")}[kind]
    q = q.replace(' + 0', '').replace(' − 0', '')
    b.add(f"f(x) = {q} (x ∈ R) ফাংশনের রেঞ্জ কোনটি?", ok, W(ok, [f"[{num(k)}, ∞)", f"({num(k)}, ∞)", "R", f"[{num(k - a)}, {num(k + a)}]", f"[−{a}, {a}]"]), "", M)
def m_parity(b):
    q, ok = R.choice([("x³ + sin x", 'বিজোড়'), ("x² + cos x", 'জোড়'), ("x|x|", 'বিজোড়'), ("x⁴ − 3x²", 'জোড়'), ("x + x²", 'জোড়ও নয়, বিজোড়ও নয়'), ("eˣ + e⁻ˣ", 'জোড়'), ("eˣ − e⁻ˣ", 'বিজোড়'), ("x sin x", 'জোড়'), ("x cos x", 'বিজোড়'), ("eˣ", 'জোড়ও নয়, বিজোড়ও নয়'), ("ln((1 + x)/(1 − x))", 'বিজোড়')])
    b.add(f"f(x) = {q} ফাংশনটি কেমন?", ok, W(ok, ['জোড়', 'বিজোড়', 'জোড়ও নয়, বিজোড়ও নয়', 'ধ্রুবক']), "f(−x) পরীক্ষা করে।", M)
def h_period(b):
    k = R.randint(2, 6); fn = R.choice(['sin', 'cos', 'tan'])
    base = {'sin': 2, 'cos': 2, 'tan': 1}[fn]
    v = F(base, k)
    ok = (f"{v.numerator}π" if v.numerator > 1 else 'π') + (f"/{v.denominator}" if v.denominator > 1 else '')
    b.add(f"f(x) = {fn} {k}x ফাংশনের পর্যায় কত?", ok, W(ok, ['2π', 'π', f"{2 * k}π", f"π/{k}", f"2π/{k}", f"{k}π"]), "মূল পর্যায় ÷ k।", H)
def h_inv_frac(b):
    a, c = R.randint(1, 6), R.randint(1, 6); y = R.choice([v for v in range(-5, 8) if v != 1])
    x = F(a + c * y, y - 1)
    b.add(f"f(x) = (x + {a})/(x − {c}) হলে f⁻¹({num(y)}) = কত?", num(x), W(num(x), [num(x + 1), num(-x) if x else '1', num(F(a - c * y, y - 1))]), "f(x) = y সমাধান।", H)
def h_floor(b):
    v = F(R.randint(-50, 50), 10)
    import math as mm
    ok = str(mm.floor(v)).replace('-', '−')
    dv = f"{float(v):g}".replace('-', '−')
    b.add(f"[x] বৃহত্তম পূর্ণসংখ্যা ফাংশন হলে [{dv}] = কত?", ok, W(ok, [str(mm.ceil(v)).replace('-', '−'), str(mm.floor(v) - 1).replace('-', '−'), str(round(float(v))).replace('-', '−'), dv]), "x অপেক্ষা বড় নয় এমন বৃহত্তম পূর্ণসংখ্যা।", H)
p8 = run(None, R, fx8, [e_val, e_dom], [m_inv, m_comp, m_range, m_parity], [h_period, h_inv_frac, h_floor], caps=(20, 13, 8))
save('i8', p8)

# ---------------- 9 অন্তরীকরণ ----------------
fx9a = [
 ("lim(x→0) (sin x)/x = কত?", "1", ["0", "∞", "অনির্ণেয়"], "", E), ("lim(x→0) (eˣ − 1)/x = কত?", "1", ["0", "e", "∞"], "", E),
 ("lim(n→∞) (1 + 1/n)ⁿ = কত?", "e", ["1", "∞", "0"], "", E), ("lim(x→0) (1 + x)^(1/x) = কত?", "e", ["1", "0", "∞"], "", E),
 ("lim(x→0) ln(1 + x)/x = কত?", "1", ["0", "e", "∞"], "", M), ("lim(x→0) (tan x)/x = কত?", "1", ["0", "∞", "অনির্ণেয়"], "", E),
 ("lim(x→0) (1 − cos x)/x = কত?", "0", ["1", "1/2", "∞"], "", M), ("lim(x→0) (1 − cos x)/x² = কত?", "1/2", ["0", "1", "2"], "", H),
]
def e_poly(b):
    a, c, k = nz(-4, 5), R.randint(-6, 6), R.randint(-3, 4)
    v = a * k * k + c * k
    b.add(f"lim(x→{num(k)}) ({px({2: a, 1: c})}) = কত?", num(v), [num(w) for w in near(v)], "সরাসরি বসিয়ে।", E)
def e_fact(b):
    a = nz(-6, 6)
    b.add(f"lim(x→{num(a)}) (x² − {a * a})/(x {'−' if a > 0 else '+'} {abs(a)}) = কত?", num(2 * a), W(num(2 * a), [num(a), '0', num(a * a), num(-2 * a)]), "(x − a)(x + a)/(x − a)।", E)
def m_sinkx(b):
    p, q = R.randint(1, 9), R.randint(1, 9)
    b.add(f"lim(x→0) (sin {p if p > 1 else ''}x)/({q if q > 1 else ''}x) = কত?" if q > 1 else f"lim(x→0) (sin {p}x)/x = কত?", fr(F(p, q)), W(fr(F(p, q)), [fr(F(q, p)), '1', '0', str(p * q)]), "(sin px)/(px) × p/q।", M)
def m_inf(b):
    a, c, d, e = nz(1, 6), R.randint(-6, 6), nz(1, 6), R.randint(-6, 6)
    b.add(f"lim(x→∞) ({px({2: a, 1: c})})/({px({2: d, 0: e})}) = কত?", fr(F(a, d)), W(fr(F(a, d)), [fr(F(d, a)), '0', '∞', fr(F(c, d)) if c else '1']), "সর্বোচ্চ ঘাতের সহগের অনুপাত।", M)
def m_power(b):
    n, a = R.randint(2, 6), R.randint(1, 4)
    v = n * a ** (n - 1)
    b.add(f"lim(x→{a}) (x{sup(n)} − {a ** n})/(x − {a}) = কত?", v, W(v, [a ** n, n * a ** n, (n - 1) * a ** (n - 1), v + 1]), "naⁿ⁻¹।", M)
def m_ekx(b):
    k = R.randint(2, 7)
    b.add(f"lim(x→0) (e^({k}x) − 1)/x = কত?", k, W(k, [1, 0, f"e{sup(k)}", F(1, k)]), "", M)
def h_root(b):
    a = R.choice([1, 4, 9, 16, 25]); r = math.isqrt(a)
    b.add(f"lim(x→{a}) (√x − {r})/(x − {a}) = কত?", fr(F(1, 2 * r)), W(fr(F(1, 2 * r)), [fr(F(1, r)), str(2 * r), '0']), "লব-হরকে অনুবন্ধী দিয়ে গুণ।", H)
def h_mixed(b):
    p, q = R.randint(1, 6), R.randint(1, 6)
    b.add(f"lim(x→0) (sin {p}x)/(tan {q}x) = কত?".replace(" 1x", " x"), fr(F(p, q)), W(fr(F(p, q)), [fr(F(q, p)), '1', '0']), "", H)
    b.add(f"lim(x→0) (1 − cos {p}x)/x² = কত?", fr(F(p * p, 2)), W(fr(F(p * p, 2)), [str(p * p), fr(F(p, 2)), '0']), "2sin²(px/2)/x²।", H)
p9a = run('9.A', R, fx9a, [e_poly, e_fact], [m_sinkx, m_inf, m_power, m_ekx], [h_root, h_mixed], caps=(20, 13, 12))

fx9b = [
 ("মূল নিয়মে f′(x) = কত?", "lim(h→0) (f(x + h) − f(x))/h", ["lim(h→0) (f(x + h) + f(x))/h", "lim(h→0) f(x + h)/h", "lim(h→∞) (f(x + h) − f(x))/h"], "সংজ্ঞা।", E),
 ("ধ্রুবকের অন্তরজ কত?", "0", ["1", "ধ্রুবকটি নিজে", "অসংজ্ঞায়িত"], "", E),
 ("অন্তরজের জ্যামিতিক অর্থ কী?", "বক্ররেখার স্পর্শকের ঢাল", ["বক্ররেখার নিচের ক্ষেত্রফল", "বক্ররেখার দৈর্ঘ্য", "ছেদবিন্দু"], "", E),
 ("মূল নিয়মে d/dx(√x) = কত?", "1/(2√x)", ["2√x", "1/√x", "√x/2"], "", M), ("মূল নিয়মে d/dx(1/x) = কত?", "−1/x²", ["1/x²", "ln x", "−1/x"], "", M),
 ("মূল নিয়মে d/dx(sin x) নির্ণয়ে কোন সীমা ব্যবহৃত হয়?", "lim(h→0) (sin h)/h = 1", ["lim(h→0) cos h/h", "lim(h→∞) sin h", "lim(h→0) h"], "", M),
]
def e_fp(b):
    a, c = nz(-5, 6), R.randint(-6, 6); k = R.randint(-3, 4)
    v = 2 * a * k + c
    b.add(f"f(x) = {px({2: a, 1: c})} হলে মূল নিয়মে নির্ণীত f′({num(k)}) = কত?", num(v), [num(w) for w in near(v)], f"f′(x) = {px({1: 2 * a, 0: c})}।", E)
def e_lin(b):
    a, c = nz(-9, 9), R.randint(-9, 9)
    b.add(f"f(x) = {px({1: a, 0: c})} হলে f′(x) = কত?", num(a), W(num(a), [num(c) if c and c != a else '0', num(a + c), px({1: a})]), "", E)
def m_quot(b):
    a, c = nz(-5, 6), R.randint(-6, 6)
    ok = px({1: 2 * a, 0: c})
    b.add(f"f(x) = {px({2: a, 1: c})} হলে lim(h→0) (f(x + h) − f(x))/h = কত?", ok, W(ok, [px({1: a, 0: c}), px({2: a, 1: c}), px({1: 2 * a})]), "", M)
def m_cube(b):
    a, k = nz(-3, 4), R.randint(-3, 3)
    v = 3 * a * k * k
    b.add(f"f(x) = {px({3: a})} হলে মূল নিয়মে f′({num(k)}) = কত?", num(v), [num(w) for w in near(v)] if v else ['1', '−1', '3'], "3ax²।", M)
def m_slope(b):
    a, c, d = nz(-4, 4), R.randint(-5, 5), R.randint(-5, 5); k = R.randint(-3, 3)
    v = 2 * a * k + c
    b.add(f"y = {px({2: a, 1: c, 0: d})} বক্ররেখার x = {num(k)} বিন্দুতে স্পর্শকের ঢাল কত?", num(v), [num(w) for w in near(v)], "dy/dx-এর মান।", M)
def h_rate(b):
    a, k = R.randint(1, 5), R.randint(1, 5)
    # গড় পরিবর্তনের হার [k, k + 1] এ ax² : a(2k + 1)
    v = a * (2 * k + 1)
    b.add(f"f(x) = {co(a, 'x²')} ফাংশনের x = {k} থেকে x = {k + 1} পর্যন্ত গড় পরিবর্তনের হার কত?", v, W(v, [2 * a * k, a * (2 * k + 2), a * k * k]), f"(f({k + 1}) − f({k}))/1।", H)
def h_recip(b):
    a, k = R.randint(1, 6), R.randint(1, 5)
    v = F(-a, k * k)
    b.add(f"f(x) = {a}/x হলে মূল নিয়মে f′({k}) = কত?", num(v), W(num(v), [num(-v), num(F(a, k)), num(F(-a, k))]), "−a/x²।", H)
def h_sqrt(b):
    k = R.choice([1, 4, 9, 16, 25]); r = math.isqrt(k)
    b.add(f"f(x) = √x হলে মূল নিয়মে f′({k}) = কত?", fr(F(1, 2 * r)), W(fr(F(1, 2 * r)), [fr(F(1, r)), str(2 * r), fr(F(r, 2))]), "1/(2√x)।", H)
p9b = run('9.B', R, fx9b, [e_fp, e_lin], [m_quot, m_cube, m_slope], [h_rate, h_recip, h_sqrt], caps=(20, 18, 12))

fx9c = [
 ("d/dx(xⁿ) = কত?", "nxⁿ⁻¹", ["xⁿ⁻¹", "nxⁿ", "xⁿ⁺¹/(n + 1)"], "", E), ("d/dx(sin x) = কত?", "cos x", ["−cos x", "sin x", "−sin x"], "", E),
 ("d/dx(cos x) = কত?", "−sin x", ["sin x", "cos x", "−cos x"], "", E), ("d/dx(tan x) = কত?", "sec²x", ["sec x tan x", "−cosec²x", "cot x"], "", E),
 ("d/dx(eˣ) = কত?", "eˣ", ["xeˣ⁻¹", "eˣ ln x", "1"], "", E), ("d/dx(ln x) = কত?", "1/x", ["x", "ln x", "eˣ"], "", E),
 ("d/dx(aˣ) = কত?", "aˣ ln a", ["xaˣ⁻¹", "aˣ", "aˣ/ln a"], "", M), ("d/dx(sec x) = কত?", "sec x tan x", ["sec²x", "−cosec x cot x", "tan²x"], "", M),
 ("d/dx(cot x) = কত?", "−cosec²x", ["cosec²x", "sec²x", "−sec²x"], "", M), ("d/dx(cosec x) = কত?", "−cosec x cot x", ["cosec x cot x", "−cot²x", "sec x tan x"], "", M),
]
def e_pow(b):
    a, n = nz(-5, 6), R.randint(2, 7)
    ok = co(a * n, f"x{sup(n - 1)}".replace('x¹', 'x'))
    b.add(f"d/dx({co(a, f'x{sup(n)}')}) = কত?", ok, W(ok, [co(a, f"x{sup(n - 1)}".replace('x¹', 'x')), co(a * n, f"x{sup(n)}"), co(a * (n - 1), f"x{sup(n - 1)}".replace('x¹', 'x'))]), "nxⁿ⁻¹।", E)
def e_poly(b):
    c3, c2, c1 = R.randint(-4, 4), R.randint(-5, 5), R.randint(-6, 6); k = R.randint(-2, 3)
    if not c3 and not c2: return
    v = 3 * c3 * k * k + 2 * c2 * k + c1
    b.add(f"f(x) = {px({3: c3, 2: c2, 1: c1})} হলে f′({num(k)}) = কত?", num(v), [num(w) for w in near(v)], "", E)
def m_neg(b):
    a, n = R.randint(1, 6), R.randint(1, 4)
    ok = f"−{a * n}/x{sup(n + 1)}"
    b.add(f"d/dx({a}/x{sup(n)}) = কত?".replace('x¹', 'x'), ok, W(ok, [f"{a * n}/x{sup(n + 1)}", f"−{a}/x{sup(n + 1)}", f"−{a * n}/x{sup(n - 1)}".replace('x⁰', '1').replace('/1', '') if n > 1 else f"−{a * n}"]), "x⁻ⁿ-এর অন্তরজ।", M)
def m_trig(b):
    a, c = nz(-5, 5), nz(-5, 5)
    ok = f"{co(a, 'cos x')} {'−' if c > 0 else '+'} {co(abs(c), 'sin x')}"
    b.add(f"d/dx({co(a, 'sin x')} {'+' if c > 0 else '−'} {co(abs(c), 'cos x')}) = কত?", ok, W(ok, [f"{co(a, 'cos x')} {'+' if c > 0 else '−'} {co(abs(c), 'sin x')}", f"{co(-a, 'cos x')} {'−' if c > 0 else '+'} {co(abs(c), 'sin x')}", f"{co(a, 'sin x')} {'−' if c > 0 else '+'} {co(abs(c), 'cos x')}"]), "", M)
def m_val(b):
    q, ok = R.choice([("d/dx(sin x) এর x = π/3-এ মান", '1/2'), ("d/dx(cos x) এর x = π/6-এ মান", '−1/2'), ("d/dx(tan x) এর x = π/4-এ মান", '2'), ("d/dx(eˣ) এর x = 0-এ মান", '1'), ("d/dx(ln x) এর x = 2-এ মান", '1/2'), ("d/dx(sec x) এর x = π/4-এ মান", '√2'), ("d/dx(√x) এর x = 4-এ মান", '1/4')])
    b.add(f"{q} কত?", ok, W(ok, ['1/2', '−1/2', '2', '1', '√2', '1/4', '0']), "", M)
def h_sqrt(b):
    n, d = R.choice([(1, 2), (3, 2), (1, 3), (2, 3), (5, 2)]); k = R.choice([1, 4, 9, 16]) if d == 2 else R.choice([1, 8, 27])
    v = F(n, d) * F(k) ** F(n - d, d) if False else None
    r = round(k ** (1 / d))
    val = F(n, d) * F(r) ** (n - d)
    b.add(f"f(x) = x^({n}/{d}) হলে f′({k}) = কত?", fr(val), W(fr(val), [fr(F(n, d) * F(r) ** n), fr(val * 2), fr(F(n, d))]), "nxⁿ⁻¹।", H)
def h_combo(b):
    a, c = R.randint(1, 5), R.randint(1, 5)
    q, ok = R.choice([(f"{a}eˣ + {c} ln x, x = 1".replace('1eˣ', 'eˣ').replace(' 1 ln', ' ln'), str(a + c)), (f"{co(a, 'x²')} + {co(c, 'eˣ')}, x = 0", str(c)), (f"{co(a, 'sin x')} + {co(c, 'cos x')}, x = 0", str(a)), (f"{co(a, 'tan x')} − {co(c, 'x')}, x = 0", num(a - c))])
    b.add(f"f(x) = {q.split(',')[0]} হলে f′(x)-এর মান{q.split(',')[1].replace('x =', ' x =')}-এ কত?", ok, W(ok, [str(a), str(c), str(a + c), str(a * c), num(a - c)]), "", H)
p9c = run('9.C', R, fx9c, [e_pow, e_poly], [m_neg, m_trig, m_val], [h_sqrt, h_combo], caps=(20, 18, 14))

fx9d = [
 ("d/dx(uv) = কত?", "u dv/dx + v du/dx", ["u dv/dx − v du/dx", "du/dx · dv/dx", "(du/dx)/(dv/dx)"], "", E),
 ("d/dx(u/v) = কত?", "(v du/dx − u dv/dx)/v²", ["(u dv/dx − v du/dx)/v²", "(v du/dx + u dv/dx)/v²", "du/dv"], "", E),
 ("d/dx(x eˣ) = কত?", "eˣ(x + 1)", ["xeˣ", "eˣ", "eˣ(x − 1)"], "", E), ("d/dx(x sin x) = কত?", "sin x + x cos x", ["x cos x", "cos x", "sin x − x cos x"], "", E),
 ("d/dx(x ln x) = কত?", "ln x + 1", ["1/x", "ln x", "x/ln x"], "", M), ("d/dx(eˣ sin x) = কত?", "eˣ(sin x + cos x)", ["eˣ cos x", "eˣ(sin x − cos x)", "eˣ sin x"], "", M),
 ("d/dx(sin x/x) = কত?", "(x cos x − sin x)/x²", ["(sin x − x cos x)/x²", "cos x", "cos x/x"], "", M), ("d/dx(eˣ/x) = কত?", "eˣ(x − 1)/x²", ["eˣ(x + 1)/x²", "eˣ/x²", "eˣ"], "", M),
]
def e_prod(b):
    a, c, k = nz(-4, 5), nz(-5, 5), R.randint(-3, 3)
    # (x + a)(x + c) ⇒ 2x + a + c
    v = 2 * k + a + c
    b.add(f"f(x) = (x {'+' if a > 0 else '−'} {abs(a)})(x {'+' if c > 0 else '−'} {abs(c)}) হলে f′({num(k)}) = কত?", num(v), [num(w) for w in near(v)], "গুণের সূত্র।", E)
def m_quot(b):
    a, c, k = R.randint(1, 5), R.randint(1, 5), R.randint(0, 4)
    # (x + a)/(x + c) ⇒ (c − a)/(x + c)²
    if a == c: return
    v = F(c - a, (k + c) ** 2)
    b.add(f"f(x) = (x + {a})/(x + {c}) হলে f′({k}) = কত?", num(v), W(num(v), [num(-v), num(F(c - a, k + c)), num(F(a - c, (k + c) ** 2 + 1))]), "(v·1 − u·1)/v²।", M)
def m_xn_ex(b):
    n = R.randint(2, 4)
    ok = f"x{sup(n - 1)}eˣ(x + {n})".replace('x¹e', 'xe')
    b.add(f"d/dx(x{sup(n)}eˣ) = কত?", ok, W(ok, [f"{n}x{sup(n - 1)}eˣ".replace('x¹e', 'xe'), f"x{sup(n)}eˣ", f"x{sup(n - 1)}eˣ(x − {n})".replace('x¹e', 'xe')]), "", M)
def m_val(b):
    q, ok = R.choice([("x sin x, x = π/2", '1'), ("x cos x, x = 0", '1'), ("x eˣ, x = 0", '1'), ("x² ln x, x = 1", '1'), ("eˣ cos x, x = 0", '1'), ("x/eˣ, x = 0", '1'), ("x tan x, x = 0", '0'), ("sin x cos x, x = 0", '1'), ("x²eˣ, x = 1", '3e')])
    f_, x0 = q.split(', ')
    b.add(f"f(x) = {f_} হলে f′(x)-এর {x0} বিন্দুতে মান কত?", ok, W(ok, ['0', '1', '−1', 'e', '3e', '2']), "", M)
def h_quot2(b):
    a = R.randint(1, 5)
    q, ok = R.choice([(f"x²/(x + {a})", f"x(x + {2 * a})/(x + {a})²"), (f"(x² + {a})/x", f"(x² − {a})/x²"), (f"x/(x² + {a})", f"({a} − x²)/(x² + {a})²")])
    b.add(f"d/dx({q}) = কত?", ok, W(ok, [ok.replace('−', '+', 1) if '−' in ok else ok.replace('+', '−', 1), f"2x/(x + {a})", "1"]), "ভাগের সূত্র।", H)
def h_three(b):
    b.add("d/dx(x eˣ sin x) = কত?", "eˣ(sin x + x sin x + x cos x)", ["eˣ x cos x", "eˣ(sin x + x cos x)", "x eˣ cos x"], "তিন গুণফলের সূত্র।", H)
    b.add("d/dx((1 + x)/(1 − x)) = কত?", "2/(1 − x)²", ["−2/(1 − x)²", "1/(1 − x)²", "2/(1 + x)²"], "", H)
    b.add("d/dx((1 − cos x)/sin x) = কত?", "1/(1 + cos x)", ["1/(1 − cos x)", "sec²(x/2)", "−1/(1 + cos x)"], "রাশিটি tan(x/2)।", H)
    b.add("d/dx(eˣ/(1 + eˣ)) = কত?", "eˣ/(1 + eˣ)²", ["1/(1 + eˣ)", "eˣ/(1 + eˣ)", "−eˣ/(1 + eˣ)²"], "", H)
def h_qv(b):
    a, c, k = R.randint(1, 6), R.randint(1, 5), R.randint(0, 3)
    v = F(2 * k * (k + c) - (k * k + a), (k + c) ** 2)
    b.add(f"f(x) = (x² + {a})/(x + {c}) হলে f′({k}) = কত?", num(v), W(num(v), [num(F(2 * k, k + c)), num(-v) if v else '1', num(v + 1)]), "ভাগের সূত্র।", H)
p9d = run('9.D', R, fx9d, [e_prod], [m_quot, m_xn_ex, m_val], [h_quot2, h_three, h_qv], caps=(30, 18, 14))

fx9e = [
 ("y = f(u), u = g(x) হলে dy/dx = কত?", "(dy/du)(du/dx)", ["(dy/du)/(du/dx)", "dy/du + du/dx", "du/dy"], "শিকল নিয়ম।", E),
 ("d/dx(sin²x) = কত?", "sin 2x", ["2 sin x", "cos²x", "2 cos x"], "2 sin x cos x।", E), ("d/dx(e^(x²)) = কত?", "2x e^(x²)", ["e^(x²)", "x² e^(x²)", "2e^(x²)"], "", E),
 ("d/dx(ln sin x) = কত?", "cot x", ["tan x", "1/sin x", "cos x"], "", M), ("d/dx(ln cos x) = কত?", "−tan x", ["tan x", "cot x", "−cot x"], "", M),
 ("d/dx(√(sin x)) = কত?", "cos x/(2√(sin x))", ["1/(2√(sin x))", "√(cos x)", "cos x/√(sin x)"], "", M),
]
def e_lin_in(b):
    a, c = nz(-6, 6), R.randint(-5, 5); fn = R.choice(['sin', 'cos', 'e'])
    inner = px({1: a, 0: c})
    if fn == 'e': q, ok = f"e^({inner})", f"{co(a, '')}e^({inner})".replace('e^', 'e^') if a != 1 else f"e^({inner})"
    elif fn == 'sin': q, ok = f"sin({inner})", f"{co(a, f'cos({inner})')}"
    else: q, ok = f"cos({inner})", f"{co(-a, f'sin({inner})')}"
    if fn == 'e': ok = (f"{num(a)}" if a not in (1, -1) else ('' if a == 1 else '−')) + f"e^({inner})"
    w = [q, (f"{num(-a)}" if -a not in (1, -1) else ('' if -a == 1 else '−')) + f"e^({inner})" if fn == 'e' else co(-a, f"{'cos' if fn == 'sin' else 'sin'}({inner})"), co(a, f"{'sin' if fn == 'sin' else 'cos'}({inner})")]
    b.add(f"d/dx({q}) = কত?", ok, W(ok, w + [co(a * 2, f"cos({inner})")]), "শিকল নিয়ম।", E)
def e_pow(b):
    a, c, n = nz(-4, 5), nz(-6, 6), R.randint(2, 6)
    inner = px({1: a, 0: c})
    ok = f"{num(n * a)}({inner}){sup(n - 1)}".replace('¹', '') if n * a not in (1, -1) else f"({inner}){sup(n - 1)}"
    b.add(f"d/dx(({inner}){sup(n)}) = কত?", ok, W(ok, [f"{n}({inner}){sup(n - 1)}".replace('¹', ''), f"{num(n * a)}({inner}){sup(n)}", (f"{num(a)}({inner}){sup(n - 1)}".replace('¹', '') if a not in (1, -1) else f"{'−' if a < 0 else ''}({inner}){sup(n - 1)}".replace('¹', ''))]), "n(ax + b)ⁿ⁻¹ · a।", E)
def m_ln(b):
    a, c = nz(-6, 6), nz(-7, 7)
    inner = px({1: a, 0: c})
    ok = f"{num(a)}/({inner})"
    b.add(f"d/dx(ln({inner})) = কত?", ok, W(ok, [f"1/({inner})", f"{num(a)}·ln({inner})", f"{num(-a)}/({inner})"]), "a/(ax + b)।", M)
def m_val(b):
    k = R.randint(2, 5); fn = R.choice(['sin', 'cos'])
    q, ok = (f"sin {k}x", str(k)) if fn == 'sin' else (f"cos {k}x", '0')
    b.add(f"f(x) = {q} হলে f′(0) = কত?", ok, W(ok, [str(k), '0', '1', str(-k)]), "", M)
def m_sqrt(b):
    a, c = R.randint(1, 5), R.randint(1, 9)
    ok = f"{a}x/√({co(a, 'x²')} + {c})" if a > 1 else f"x/√(x² + {c})"
    b.add(f"d/dx(√({co(a, 'x²')} + {c})) = কত?", ok, W(ok, [f"1/(2√({co(a, 'x²')} + {c}))", f"{2 * a}x/√({co(a, 'x²')} + {c})", f"{a}x√({co(a, 'x²')} + {c})" if a > 1 else f"x√(x² + {c})"]), "", M)
def h_nested(b):
    q, ok = R.choice([("sin(ln x)", "cos(ln x)/x"), ("ln(ln x)", "1/(x ln x)"), ("e^(sin x)", "cos x · e^(sin x)"), ("sin(e^x)", "eˣ cos(eˣ)"), ("ln(sec x + tan x)", "sec x"), ("ln(x + √(x² + 1))", "1/√(x² + 1)"), ("cos³x", "−3cos²x sin x"), ("tan²x", "2 tan x sec²x")])
    b.add(f"d/dx({q}) = কত?", ok, W(ok, ["cos(ln x)/x", "1/(x ln x)", "cos x · e^(sin x)", "eˣ cos(eˣ)", "sec x", "1/√(x² + 1)", "−3cos²x sin x", "2 tan x sec²x"]), "শিকল নিয়ম।", H)
def h_cv(b):
    a, c, n, k = R.randint(1, 4), R.randint(-3, 3), R.randint(2, 4), R.randint(-1, 2)
    v = n * a * (a * k + c) ** (n - 1)
    b.add(f"f(x) = ({px({1: a, 0: c})}){sup(n)} হলে f′({num(k)}) = কত?", num(v), W(num(v), [num(n * (a * k + c) ** (n - 1)), num((a * k + c) ** n), num(v + a)]), "শিকল নিয়ম।", H)
def h_ev(b):
    a, c, k = R.randint(1, 4), R.randint(1, 5), R.randint(0, 2)
    v = F(2 * a * k, a * k * k + c)
    b.add(f"f(x) = ln({co(a, 'x²')} + {c}) হলে f′({k}) = কত?", num(v), W(num(v), [num(F(1, a * k * k + c)), num(F(2 * k, a * k * k + c)) if a > 1 else num(v + 1), num(2 * a * k)]), "2ax/(ax² + c)।", H)
p9e = run('9.E', R, fx9e, [e_lin_in, e_pow], [m_ln, m_val, m_sqrt], [h_nested, h_cv, h_ev], caps=(20, 18, 20))

fx9f = [
 ("d/dx(sin⁻¹x) = কত?", "1/√(1 − x²)", ["−1/√(1 − x²)", "1/(1 + x²)", "√(1 − x²)"], "", E), ("d/dx(cos⁻¹x) = কত?", "−1/√(1 − x²)", ["1/√(1 − x²)", "−1/(1 + x²)", "1/(1 + x²)"], "", E),
 ("d/dx(tan⁻¹x) = কত?", "1/(1 + x²)", ["−1/(1 + x²)", "1/√(1 − x²)", "sec²x"], "", E), ("d/dx(cot⁻¹x) = কত?", "−1/(1 + x²)", ["1/(1 + x²)", "−cosec²x", "−1/√(1 − x²)"], "", M),
 ("d/dx(sec⁻¹x) = কত?", "1/(x√(x² − 1))", ["−1/(x√(x² − 1))", "1/√(x² − 1)", "sec x tan x"], "", M), ("d/dx(log₁₀x) = কত?", "1/(x ln 10)", ["1/x", "ln 10/x", "10/x"], "", M),
 ("d/dx(xˣ) = কত?", "xˣ(1 + ln x)", ["x·xˣ⁻¹", "xˣ ln x", "xˣ"], "লগারিদমীয় অন্তরীকরণ।", H),
]
def e_val(b):
    q, ok = R.choice([("tan⁻¹x, x = 1", '1/2'), ("tan⁻¹x, x = 0", '1'), ("sin⁻¹x, x = 0", '1'), ("cos⁻¹x, x = 0", '−1'), ("sin⁻¹x, x = 1/2", '2/√3'), ("tan⁻¹x, x = √3", '1/4'), ("cot⁻¹x, x = 1", '−1/2')])
    f_, x0 = q.split(', ')
    b.add(f"f(x) = {f_} হলে f′(x)-এর {x0} বিন্দুতে মান কত?", ok, W(ok, ['1/2', '1', '−1', '2/√3', '1/4', '−1/2', '0']), "", E)
def e_ax(b):
    a = R.choice([2, 3, 5, 10]); k = R.randint(0, 3)
    ok = f"{a ** k} ln {a}" if a ** k != 1 else f"ln {a}"
    b.add(f"f(x) = {a}ˣ হলে f′({k}) = কত?", ok, W(ok, [str(a ** k), f"{k * a ** (k - 1) if k else 0}", f"{a ** k}/ln {a}"]), "aˣ ln a।", E)
def m_chain(b):
    a = R.randint(2, 6)
    q, ok = R.choice([(f"tan⁻¹({a}x)", f"{a}/(1 + {a * a}x²)"), (f"sin⁻¹({a}x)", f"{a}/√(1 − {a * a}x²)"), (f"tan⁻¹(x/{a})", f"{a}/({a * a} + x²)"), (f"sin⁻¹(x/{a})", f"1/√({a * a} − x²)")])
    b.add(f"d/dx({q}) = কত?", ok, W(ok, [f"1/(1 + {a * a}x²)", f"{a}/(1 − {a * a}x²)", f"1/({a * a} + x²)", f"{a}/√({a * a} − x²)"]), "শিকল নিয়ম।", M)
def m_ident(b):
    q, ok = R.choice([("sin⁻¹x + cos⁻¹x", '0'), ("tan⁻¹x + cot⁻¹x", '0'), ("tan⁻¹(2x/(1 − x²)), |x| < 1", '2/(1 + x²)'), ("sin⁻¹(2x/(1 + x²)), |x| < 1", '2/(1 + x²)'), ("cos⁻¹((1 − x²)/(1 + x²)), x > 0", '2/(1 + x²)'), ("tan⁻¹(√((1 − cos x)/(1 + cos x))), 0 < x < π", '1/2')])
    f_ = q.split(', ')[0]
    b.add(f"d/dx({f_}) = কত?" + (f" ({q.split(', ')[1]})" if ', ' in q else ''), ok, W(ok, ['0', '1', '2/(1 + x²)', '1/2', '1/(1 + x²)']), "সরল করে অন্তরীকরণ।", M)
def h_log(b):
    q, ok = R.choice([("x^(sin x)", "x^(sin x)(cos x ln x + sin x/x)"), ("(sin x)ˣ", "(sin x)ˣ(ln sin x + x cot x)"), ("x^(1/x)", "x^(1/x)(1 − ln x)/x²"), ("(ln x)ˣ", "(ln x)ˣ(ln ln x + 1/ln x)")])
    b.add(f"d/dx({q}) = কত?", ok, W(ok, ["x^(sin x)(cos x ln x + sin x/x)", "(sin x)ˣ(ln sin x + x cot x)", "x^(1/x)(1 − ln x)/x²", "(ln x)ˣ(ln ln x + 1/ln x)", "x^(sin x) cos x"]), "উভয় পক্ষের ln নিয়ে।", H)
def h_val(b):
    b.add("f(x) = xˣ হলে f′(1) = কত?", '1', ['0', 'e', '2'], "xˣ(1 + ln x), x = 1।", H)
    b.add("f(x) = xˣ হলে f′(e) = কত?", '2eᵉ', ['eᵉ', 'e', '2e'], "eᵉ(1 + 1)।", H)
    b.add("y = log_x 2 হলে dy/dx = কত?", "−ln 2/(x (ln x)²)", ["ln 2/x", "1/(x ln 2)", "−1/(x ln x)"], "y = ln 2/ln x।", H)
def e_loga(b):
    a, k = R.choice([2, 3, 5, 10]), R.randint(1, 6)
    ok = f"1/({k} ln {a})" if k > 1 else f"1/ln {a}"
    b.add(f"f(x) = log_{a} x হলে f′({k}) = কত?", ok, W(ok, [fr(F(1, k)), f"ln {a}/{k}", f"{k} ln {a}"]), "1/(x ln a)।", E)
def m_cv(b):
    t = R.choice([0, 1])
    if t == 0:
        a, k = R.randint(1, 5), R.randint(0, 3); v = F(a, 1 + a * a * k * k)
        b.add(f"f(x) = tan⁻¹({co(a, 'x')}) হলে f′({k}) = কত?", fr(v), W(fr(v), [fr(F(1, 1 + a * a * k * k)), fr(F(a, 1 + k * k)) if F(a, 1 + k * k) != v else fr(v + 1), fr(v * 2)]), "a/(1 + a²x²)।", M)
    else:
        a, k = R.choice([(5, 3), (5, 4), (13, 5), (13, 12), (10, 6), (10, 8), (17, 8), (17, 15), (25, 7), (25, 24), (15, 9), (15, 12), (20, 12), (20, 16)])
        r = math.isqrt(a * a - k * k)
        b.add(f"f(x) = sin⁻¹(x/{a}) হলে f′({k}) = কত?", fr(F(1, r)), W(fr(F(1, r)), [fr(F(1, a)), fr(F(a, r)), fr(F(1, k))]), "1/√(a² − x²)।", M)
def h_num(b):
    a, k = R.choice([2, 3, 5, 10]), R.randint(1, 4)
    t = R.choice([0, 1])
    if t == 0:
        v = F(2 * k, k * k + 1); lnf = lambda q: f"{q.numerator}/ln {a}" if q.denominator == 1 else f"{q.numerator}/({q.denominator} ln {a})"
        ok = lnf(v)
        b.add(f"f(x) = log_{a}(x² + 1) হলে f′({k}) = কত?", ok, W(ok, [f"({fr(v)}) ln {a}", fr(v), lnf(F(1, k * k + 1))]), "2x/((x² + 1) ln a)।", H)
    else:
        a = R.choice([2, 3, 5]); k = R.randint(1, 2); v = 2 * k * a ** (k * k)
        b.add(f"f(x) = {a}^(x²) হলে f′({k}) = কত?", f"{v} ln {a}", W(f"{v} ln {a}", [str(v), f"{a ** (k * k)} ln {a}", f"{v}/ln {a}"]), "2x·a^(x²)·ln a।", H)
p9f = run('9.F', R, fx9f, [e_val, e_ax, e_loga], [m_chain, m_ident, m_cv], [h_log, h_val, h_num], caps=(20, 25, 20))

fx9g = [
 ("x² + y² = a² হলে dy/dx = কত?", "−x/y", ["x/y", "−y/x", "y/x"], "", E), ("x = at², y = 2at হলে dy/dx = কত?", "1/t", ["t", "2t", "1/(2t)"], "(dy/dt)/(dx/dt)।", E),
 ("x = a cos t, y = a sin t হলে dy/dx = কত?", "−cot t", ["cot t", "tan t", "−tan t"], "", M), ("xy = c² হলে dy/dx = কত?", "−y/x", ["y/x", "−x/y", "x/y"], "", E),
 ("পরামিতিক আকারে dy/dx = কত?", "(dy/dt)/(dx/dt)", ["(dx/dt)/(dy/dt)", "dy/dt · dx/dt", "dy/dt + dx/dt"], "", E),
]
def e_circ(b):
    x, y = R.choice([(3, 4), (4, 3), (5, 12), (12, 5), (6, 8), (8, 6)]); x *= R.choice([1, -1]); y *= R.choice([1, -1])
    v = F(-x, y)
    b.add(f"x² + y² = {x * x + y * y} বক্ররেখার {P_(x, y)} বিন্দুতে dy/dx = কত?", num(v), W(num(v), [num(-v), num(F(y, x)), num(F(-y, x))]), "−x/y।", E)
def P_(x, y): return f"({num(x)}, {num(y)})"
def m_imp(b):
    a, c = R.randint(1, 4), R.randint(1, 4); x, y = R.randint(1, 4), R.randint(1, 4)
    # ax² + cy² = k ⇒ dy/dx = −ax/(cy)
    k = a * x * x + c * y * y; v = F(-a * x, c * y)
    b.add(f"{co(a, 'x²')} + {co(c, 'y²')} = {k} বক্ররেখার {P_(x, y)} বিন্দুতে dy/dx = কত?", num(v), W(num(v), [num(-v), num(F(-c * y, a * x)), num(F(-a, c))]), "অস্পষ্ট অন্তরীকরণ।", M)
def m_param(b):
    a, k = R.randint(1, 5), nz(-4, 4)
    b.add(f"x = {co(a, 't²')}, y = {co(2 * a, 't')} হলে t = {num(k)}-এ dy/dx = কত?", num(F(1, k)), W(num(F(1, k)), [num(k), num(2 * k), num(F(-1, k))]), "1/t।", M)
def m_xy(b):
    x, y = R.randint(1, 6), R.randint(1, 6)
    b.add(f"xy = {x * y} বক্ররেখার {P_(x, y)} বিন্দুতে dy/dx = কত?", num(F(-y, x)), W(num(F(-y, x)), [num(F(y, x)), num(F(-x, y)), num(F(x, y))]), "−y/x।", M)
def h_mix(b):
    x, y = R.randint(1, 4), R.randint(1, 4)
    # x² + xy + y² = k ⇒ dy/dx = −(2x + y)/(x + 2y)
    k = x * x + x * y + y * y; v = F(-(2 * x + y), x + 2 * y)
    b.add(f"x² + xy + y² = {k} বক্ররেখার {P_(x, y)} বিন্দুতে dy/dx = কত?", num(v), W(num(v), [num(-v), num(F(-(x + 2 * y), 2 * x + y)), num(F(-x, y))]), "−(2x + y)/(x + 2y)।", H)
def h_param2(b):
    q, ok = R.choice([("x = a(t + sin t), y = a(1 − cos t)", "tan(t/2)"), ("x = a(t − sin t), y = a(1 − cos t)", "cot(t/2)"), ("x = a cos³t, y = a sin³t", "−tan t"), ("x = eᵗ cos t, y = eᵗ sin t", "(sin t + cos t)/(cos t − sin t)"), ("x = ln t, y = t²", "2t²")])
    b.add(f"{q} হলে dy/dx = কত?", ok, W(ok, ["tan(t/2)", "cot(t/2)", "−tan t", "(sin t + cos t)/(cos t − sin t)", "2t²", "2t"]), "(dy/dt)/(dx/dt)।", H)
def e_par2(b):
    c, d, k = R.randint(1, 5), R.randint(1, 5), R.randint(-3, 3)
    v = F(2 * d * k, c)
    b.add(f"x = {co(c, 't')}, y = {co(d, 't²')} হলে t = {num(k)}-এ dy/dx = কত?", num(v), W(num(v), [num(F(c, 2 * d * k)) if k else '1', num(2 * d * k), num(v + 1)]), "(dy/dt)/(dx/dt) = 2dt/c।", E)
def h_cube(b):
    x, y = R.randint(1, 3), R.randint(1, 3)
    # x³ + y³ = k ⇒ dy/dx = −x²/y²
    k = x ** 3 + y ** 3; v = F(-x * x, y * y)
    b.add(f"x³ + y³ = {k} বক্ররেখার {P_(x, y)} বিন্দুতে dy/dx = কত?", num(v), W(num(v), [num(-v), num(F(-y * y, x * x)) if x != y else '1', num(F(-x, y)) if x != y else '−2']), "−x²/y²।", H)
p9g = run('9.G', R, fx9g, [e_circ, e_par2], [m_imp, m_param, m_xy], [h_mix, h_param2, h_cube], caps=(30, 18, 14))

fx9h = [
 ("y = eˣ হলে d²y/dx² = কত?", "eˣ", ["xeˣ", "0", "2eˣ"], "", E), ("y = sin x হলে d²y/dx² = কত?", "−sin x", ["sin x", "cos x", "−cos x"], "", E),
 ("y = cos x হলে d⁴y/dx⁴ = কত?", "cos x", ["−cos x", "sin x", "−sin x"], "চার বার অন্তরীকরণে ফেরত।", M), ("y = ln x হলে d²y/dx² = কত?", "−1/x²", ["1/x²", "1/x", "ln x"], "", M),
 ("y = A sin x + B cos x হলে কোনটি সত্য?", "y₂ + y = 0", ["y₂ − y = 0", "y₂ + y₁ = 0", "y₁ = y"], "", M), ("y = Aeˣ + Be⁻ˣ হলে কোনটি সত্য?", "y₂ = y", ["y₂ + y = 0", "y₁ = y", "y₂ = 0"], "", M),
]
def e_poly2(b):
    a, n = nz(-4, 5), R.randint(2, 6)
    ok = co(a * n * (n - 1), f"x{sup(n - 2)}".replace('x⁰', '').replace('x¹', 'x')) if n > 2 else num(a * n * (n - 1))
    b.add(f"y = {co(a, f'x{sup(n)}')} হলে d²y/dx² = কত?", ok, W(ok, [co(a * n, f"x{sup(n - 1)}".replace('x¹', 'x')), co(a * n * (n - 1), f"x{sup(n - 1)}".replace('x¹', 'x')), co(a * (n - 1), f"x{sup(n - 2)}".replace('x⁰', '').replace('x¹', 'x')) if n > 2 else num(a * (n - 1))]), "", E)
def m_sinkx(b):
    k = R.randint(2, 6); fn = R.choice(['sin', 'cos', 'e'])
    if fn == 'e': q, ok = f"e^({k}x)", f"{k * k}e^({k}x)"; ws = [f"{k}e^({k}x)", f"e^({k}x)", f"{2 * k}e^({k}x)"]
    else: q, ok = f"{fn} {k}x", f"−{k * k} {fn} {k}x"; ws = [f"{k * k} {fn} {k}x", f"−{k} {fn} {k}x", f"−{k * k} {'cos' if fn == 'sin' else 'sin'} {k}x"]
    b.add(f"y = {q} হলে d²y/dx² = কত?", ok, W(ok, ws), "", M)
def m_val(b):
    c3, c2, c1 = R.randint(-3, 3), R.randint(-4, 4), R.randint(-5, 5); k = R.randint(-2, 3)
    if not c3: return
    v = 6 * c3 * k + 2 * c2
    b.add(f"y = {px({3: c3, 2: c2, 1: c1})} হলে x = {num(k)}-এ d²y/dx² = কত?", num(v), [num(w) for w in near(v)], "", M)
def h_nth(b):
    k = R.randint(2, 4); n = R.randint(3, 6)
    b.add(f"y = e^({k}x) হলে n-তম অন্তরজ yₙ = কত?", f"{k}ⁿe^({k}x)", [f"n{k}e^({k}x)", f"{k}e^({k}x)", f"{k}ⁿ⁻¹e^({k}x)"], "", H)
    b.add(f"y = x{sup(n)} হলে {n}-তম অন্তরজ কত?", str(math.factorial(n)), W(str(math.factorial(n)), [str(n), '0', str(math.factorial(n - 1))]), "n!।", H)
    b.add(f"y = x{sup(n)} হলে {n + 1}-তম অন্তরজ কত?", '0', [str(math.factorial(n)), '1', str(n)], "", H)
def h_eq(b):
    q, ok = R.choice([("y = e^(ax) sin bx হলে y₂ − 2ay₁ + (a² + b²)y = ?", '0'), ("y = sin(m sin⁻¹x) হলে (1 − x²)y₂ − xy₁ + m²y = ?", '0'), ("y = tan⁻¹x হলে (1 + x²)y₂ + 2xy₁ = ?", '0'), ("y = x ln x হলে xy₂ = ?", '1')])
    b.add(q.replace('= ?', '= কত?'), ok, W(ok, ['0', '1', 'y', '−1']), "", H)
def h_v(b):
    a, c, k = R.randint(1, 4), R.randint(1, 5), R.randint(0, 3)
    v = F(-a * a, (a * k + c) ** 2)
    b.add(f"y = ln({px({1: a, 0: c})}) হলে x = {k}-এ d²y/dx² = কত?", num(v), W(num(v), [num(-v), num(F(a, a * k + c)), num(F(-a, (a * k + c) ** 2)) if a > 1 else num(v * 2)]), "y₂ = −a²/(ax + b)²।", H)
p9h = run('9.H', R, fx9h, [e_poly2], [m_sinkx, m_val], [h_nth, h_eq, h_v], caps=(30, 25, 20))

fx9i = [
 ("f′(x) > 0 হলে ফাংশনটি কেমন?", "ক্রমবর্ধমান", ["ক্রমহ্রাসমান", "ধ্রুবক", "পর্যাবৃত্ত"], "", E), ("f′(a) = 0 ও f″(a) < 0 হলে x = a-তে f-এর কী?", "সর্বোচ্চ মান", ["সর্বনিম্ন মান", "প্রবৃদ্ধি বিন্দু", "অসংজ্ঞায়িত"], "", E),
 ("f′(a) = 0 ও f″(a) > 0 হলে x = a-তে f-এর কী?", "সর্বনিম্ন মান", ["সর্বোচ্চ মান", "শূন্য", "অসীম"], "", E),
 ("বক্ররেখার কোনো বিন্দুতে স্পর্শক x-অক্ষের সমান্তরাল হওয়ার শর্ত কোনটি?", "dy/dx = 0", ["dx/dy = 0", "dy/dx = 1", "dy/dx অসংজ্ঞায়িত"], "", M),
]
def e_tan(b):
    a, c, d = nz(-3, 3), R.randint(-4, 4), R.randint(-5, 5); k = R.randint(-2, 2)
    y0 = a * k * k + c * k + d; m = 2 * a * k + c
    # y − y0 = m(x − k) ⇒ y = mx + (y0 − mk)
    cc = y0 - m * k
    ok = 'y = ' + (pfmt({(1,): m, (0,): cc}, X) if (m or cc) else '0') if (m or cc) else 'y = 0'
    b.add(f"y = {px({2: a, 1: c, 0: d})} বক্ররেখার x = {num(k)} বিন্দুতে স্পর্শকের সমীকরণ কোনটি?", ok, W(ok, ['y = ' + pfmt({(1,): m, (0,): cc + 1}, X) if (m or cc + 1) else 'y = 1', 'y = ' + pfmt({(1,): -m, (0,): cc}, X) if (m or cc) else 'y = 2', 'y = ' + pfmt({(1,): m + 1, (0,): cc}, X)]), f"ঢাল {num(m)}, বিন্দু ({num(k)}, {num(y0)})।", E)
def e_ext(b):
    a, h, k = nz(-4, 4), R.randint(-4, 5), R.randint(-6, 6)
    # y = a(x − h)² + k ⇒ চরম মান k at x = h
    c1, c0 = -2 * a * h, a * h * h + k
    kind = 'সর্বনিম্ন' if a > 0 else 'সর্বোচ্চ'
    b.add(f"f(x) = {px({2: a, 1: c1, 0: c0})} ফাংশনের {kind} মান কত?", num(k), W(num(k), [num(h), num(c0), num(k + a), num(-k) if k else '1']), f"f′(x) = 0 ⇒ x = {num(h)}।", E)
def m_crit(b):
    r1, r2 = sorted(R.sample(range(-4, 5), 2))
    # f′(x) = 3(x − r1)(x − r2) ⇒ f = x³ − 3/2(r1 + r2)x² + 3r1r2x
    s, p = r1 + r2, r1 * r2
    if s % 2: return
    f = {3: 1, 2: -3 * s // 2, 1: 3 * p}
    ok = f"x = {num(r1)} ও x = {num(r2)}"
    b.add(f"f(x) = {px(f)} ফাংশনের সন্ধি বিন্দু (f′(x) = 0) কোনগুলো?", ok, W(ok, [f"x = {num(-r1)} ও x = {num(-r2)}", f"x = {num(r1)} ও x = {num(s)}" if s != r2 else f"x = 0 ও x = {num(r2)}", f"x = {num(p)}" if p else "x = 1"]), "f′(x) = 3x² − …।", M)
def m_incr(b):
    a, c = nz(1, 4), R.randint(-8, 8)
    if c % (2 * a): return
    h = F(-c, 2 * a)
    ok = f"x > {num(h)}"
    b.add(f"f(x) = {px({2: a, 1: c})} ফাংশনটি কোন ব্যবধিতে ক্রমবর্ধমান?", ok, W(ok, [f"x < {num(h)}", f"x > {num(-h)}" if h else "x > 1", "সকল x"]), f"f′(x) = {px({1: 2 * a, 0: c})} > 0।", M)
def m_rate(b):
    r, dr = R.randint(1, 10), R.randint(1, 5)
    ok = f"{2 * r * dr}π"
    b.add(f"একটি বৃত্তের ব্যাসার্ধ {dr} সেমি/সেকেন্ড হারে বাড়ছে। ব্যাসার্ধ {r} সেমি হলে ক্ষেত্রফল বৃদ্ধির হার কত বর্গ সেমি/সেকেন্ড?", ok, W(ok, [f"{r * dr}π", f"{r * r * dr}π", f"{2 * r}π"]), "dA/dt = 2πr dr/dt।", M)
def h_max(b):
    P = 4 * R.randint(2, 15)
    b.add(f"পরিসীমা {P} মিটার এমন আয়তক্ষেত্রের সর্বোচ্চ ক্ষেত্রফল কত বর্গমিটার?", (P // 4) ** 2, W((P // 4) ** 2, [P, (P // 4) * (P // 4 + 1), P * P // 8, P // 2]), "বর্গ হলে সর্বোচ্চ।", H)
def h_sum(b):
    s = 2 * R.randint(3, 25)
    b.add(f"দুটি ধনাত্মক সংখ্যার যোগফল {s} হলে তাদের গুণফলের সর্বোচ্চ মান কত?", (s // 2) ** 2, W((s // 2) ** 2, [s, (s // 2) * (s // 2 - 1), s * s // 2]), "সংখ্যা দুটি সমান হলে।", H)
def h_normal(b):
    a, k = nz(-3, 3), R.randint(-2, 2)
    m = 2 * a * k
    if m == 0: return
    nm = F(-1, m)
    b.add(f"y = {co(a, 'x²')} বক্ররেখার x = {num(k)} বিন্দুতে অভিলম্বের ঢাল কত?", num(nm), W(num(nm), [num(m), num(-m), num(F(1, m))]), "−1/(dy/dx)।", H)
p9i = run('9.I', R, fx9i, [e_tan, e_ext], [m_crit, m_incr, m_rate], [h_max, h_sum, h_normal], caps=(20, 18, 10))
save('i9', p9a + p9b + p9c + p9d + p9e + p9f + p9g + p9h + p9i)

# ---------------- 10 যোগজীকরণ ----------------
fx10a = [
 ("∫xⁿ dx = কত? (n ≠ −1)", "xⁿ⁺¹/(n + 1) + c", ["nxⁿ⁻¹ + c", "xⁿ⁺¹ + c", "xⁿ/(n + 1) + c"], "", E), ("∫(1/x) dx = কত?", "ln|x| + c", ["−1/x² + c", "x + c", "1/x² + c"], "", E),
 ("∫eˣ dx = কত?", "eˣ + c", ["xeˣ + c", "eˣ⁺¹ + c", "ln x + c"], "", E), ("∫cos x dx = কত?", "sin x + c", ["−sin x + c", "cos x + c", "tan x + c"], "", E),
 ("∫sin x dx = কত?", "−cos x + c", ["cos x + c", "sin x + c", "−sin x + c"], "", E), ("∫sec²x dx = কত?", "tan x + c", ["sec x + c", "−cot x + c", "sec x tan x + c"], "", E),
 ("∫cosec²x dx = কত?", "−cot x + c", ["cot x + c", "tan x + c", "−tan x + c"], "", M), ("∫sec x tan x dx = কত?", "sec x + c", ["tan x + c", "sec²x + c", "ln sec x + c"], "", M),
 ("∫aˣ dx = কত?", "aˣ/ln a + c", ["aˣ ln a + c", "xaˣ⁻¹ + c", "aˣ⁺¹/(x + 1) + c"], "", M),
]
def frac_term(c, n):
    """c·x^n (c ভগ্নাংশ)"""
    c = F(c); body = f"x{sup(n)}".replace('x¹', 'x').replace('x⁰', '')
    if c.denominator == 1: return co(c, body)
    return f"{'−' if c < 0 else ''}{abs(c.numerator) if abs(c.numerator) > 1 else ''}{body}/{c.denominator}"
def e_pow(b):
    a, n = nz(-6, 6), R.randint(1, 6)
    ok = frac_term(F(a, n + 1), n + 1) + ' + c'
    b.add(f"∫{co(a, f'x{sup(n)}'.replace('x¹', 'x'))} dx = কত?", ok, W(ok, [frac_term(a * n, n - 1) + ' + c' if n > 1 else f"{num(a)} + c", frac_term(a, n + 1) + ' + c', frac_term(F(a, n), n + 1) + ' + c']), "xⁿ⁺¹/(n + 1)।", E)
def e_poly(b):
    a, c = nz(-4, 4), nz(-6, 6)
    ok = f"{frac_term(F(a, 3), 3)} {'+' if c > 0 else '−'} {frac_term(F(abs(c), 2), 2)} + c"
    b.add(f"∫({px({2: a, 1: c})}) dx = কত?", ok, W(ok, [f"{frac_term(2 * a, 1)} {'+' if c > 0 else '−'} {abs(c)} + c", f"{frac_term(a, 3)} {'+' if c > 0 else '−'} {frac_term(abs(c), 2)} + c", f"{frac_term(F(a, 3), 3)} {'−' if c > 0 else '+'} {frac_term(F(abs(c), 2), 2)} + c"]), "পদে পদে।", E)
def m_mix(b):
    a, c = R.randint(1, 5), R.randint(1, 5)
    q, ok = R.choice([(f"({a}eˣ + {c}/x)", f"{a}eˣ + {c} ln|x| + c"), (f"({a} cos x − {c} sin x)", f"{a} sin x + {c} cos x + c"), (f"({a} sec²x + {c})", f"{a} tan x + {c}x + c"), (f"({a}/x − {c}eˣ)", f"{a} ln|x| − {c}eˣ + c")])
    ok = ok.replace('1eˣ', 'eˣ').replace('1 sin', 'sin').replace('1 cos', 'cos').replace('1 tan', 'tan').replace('1 ln', 'ln').replace(' 1x', ' x')
    q = q.replace('(1eˣ', '(eˣ').replace(' 1/x', ' 1/x').replace('(1 cos', '(cos').replace(' 1 sin', ' sin').replace('(1 sec', '(sec').replace('− 1eˣ', '− eˣ')
    b.add(f"∫{q} dx = কত?", ok, W(ok, [ok.replace('+ c', '').replace(' + ', ' − ', 1) + ' + c' if ' + ' in ok.replace(' + c', '') else ok.replace(' − ', ' + ', 1), ok.replace('ln|x|', '1/x²') if 'ln' in ok else ok.replace('sin', 'cos', 1), f"{a}eˣ + c"]), "আদর্শ সূত্র।", M)
def m_sqrt(b):
    a = R.randint(1, 5)
    q, ok = R.choice([(f"{a}√x", f"{fr(F(2 * a, 3))}x^(3/2) + c"), (f"{a}/√x", f"{2 * a}√x + c"), (f"{a}/x²", f"−{a}/x + c"), (f"{a}/x³", f"−{fr(F(a, 2))}/x² + c")])
    q = q.replace('1√', '√')
    b.add(f"∫{q} dx = কত?", ok, W(ok, [f"{a}x^(3/2) + c", f"{a}√x + c", f"{a}/x + c", f"−{2 * a}/x³ + c"]), "xⁿ সূত্র।", M)
def h_split(b):
    q, ok = R.choice([("(x² + 1)/x", "x²/2 + ln|x| + c"), ("(x + 1)²", "(x + 1)³/3 + c"), ("(1 + x)/√x", "2√x + (2/3)x^(3/2) + c"), ("(eˣ + e⁻ˣ)", "eˣ − e⁻ˣ + c"), ("tan²x", "tan x − x + c"), ("(x³ − 1)/(x − 1)", "x³/3 + x²/2 + x + c")])
    b.add(f"∫{q} dx = কত?", ok, W(ok, ["x²/2 + ln|x| + c", "(x + 1)³/3 + c", "2√x + (2/3)x^(3/2) + c", "eˣ − e⁻ˣ + c", "tan x − x + c", "x³/3 + x²/2 + x + c", "eˣ + e⁻ˣ + c"]), "ভেঙে বা সরল করে।", H)
def h_gen(b):
    k = R.randint(2, 9); t = R.choice([0, 1, 2])
    if t == 0: q, ok, ws = f"(x² + {k})/x", f"x²/2 + {k} ln|x| + c", [f"x²/2 − {k} ln|x| + c", f"x + {k}/x² + c", f"x³/3 + {k} ln|x| + c"]
    elif t == 1: q, ok, ws = f"(eˣ + {k})eˣ", f"e^(2x)/2 + {k}eˣ + c", [f"e^(2x) + {k}eˣ + c", f"eˣ + {k}x + c", f"e^(2x)/2 + {k}x + c"]
    else: q, ok, ws = f"(x + {k})/√x", f"(2/3)x^(3/2) + {2 * k}√x + c", [f"(2/3)x^(3/2) + {k}√x + c", f"x^(3/2) + {2 * k}√x + c", f"(3/2)x^(2/3) + {2 * k}√x + c"]
    b.add(f"∫{q} dx = কত?", ok, ws, "ভেঙে পদে পদে যোগজ।", H)
p10a = run('10.A', R, fx10a, [e_pow, e_poly], [m_mix, m_sqrt], [h_split, h_gen], caps=(20, 25, 20))

fx10b = [
 ("∫f′(x)/f(x) dx = কত?", "ln|f(x)| + c", ["f(x) + c", "1/f(x) + c", "f′(x) + c"], "", E), ("∫2x/(x² + 1) dx = কত?", "ln(x² + 1) + c", ["2 ln x + c", "tan⁻¹x + c", "x² + c"], "", E),
 ("∫cos x/sin x dx = কত?", "ln|sin x| + c", ["ln|cos x| + c", "−ln|sin x| + c", "tan x + c"], "", M), ("∫eˣ/(1 + eˣ) dx = কত?", "ln(1 + eˣ) + c", ["eˣ + c", "1/(1 + eˣ) + c", "x + c"], "", M),
 ("∫2x e^(x²) dx = কত?", "e^(x²) + c", ["x²e^(x²) + c", "2e^(x²) + c", "e^(2x) + c"], "", M),
]
def e_lin(b):
    a, c, n = R.randint(2, 6), R.randint(-6, 6), R.randint(2, 5)
    inner = px({1: a, 0: c})
    ok = f"({inner}){sup(n + 1)}/{a * (n + 1)} + c"
    b.add(f"∫({inner}){sup(n)} dx = কত?", ok, W(ok, [f"({inner}){sup(n + 1)}/{n + 1} + c", f"{a * n}({inner}){sup(n - 1)} + c".replace('¹', ''), f"({inner}){sup(n + 1)}/{a} + c"]), "প্রতিস্থাপন u = ax + b।", E)
def e_exp(b):
    a, c = nz(-6, 6), R.randint(-5, 5); inner = px({1: a, 0: c})
    ok = f"e^({inner})/{a} + c" if a > 0 else f"−e^({inner})/{-a} + c"
    ok = ok.replace('/1 +', ' +')
    b.add(f"∫e^({inner}) dx = কত?", ok, W(ok, [f"e^({inner}) + c", f"{num(a)}e^({inner}) + c", f"e^({inner})/{abs(a) + 1} + c"]), "", E)
def m_ln(b):
    a, c = nz(-6, 6), nz(-7, 7); inner = px({1: a, 0: c})
    ok = f"(1/{a}) ln|{inner}| + c" if a > 0 else f"−(1/{-a}) ln|{inner}| + c"
    ok = ok.replace('(1/1) ', '')
    b.add(f"∫1/({inner}) dx = কত?", ok, W(ok, [f"ln|{inner}| + c", f"{num(a)} ln|{inner}| + c", f"−1/({inner})² + c"]), "", M)
def m_sub(b):
    n, a = R.randint(2, 5), R.randint(1, 9)
    ok = f"(x² + {a}){sup(n + 1)}/{n + 1} + c"
    b.add(f"∫2x(x² + {a}){sup(n)} dx = কত?", ok, W(ok, [f"(x² + {a}){sup(n + 1)}/{2 * (n + 1)} + c", f"2(x² + {a}){sup(n + 1)} + c", f"x²(x² + {a}){sup(n)} + c"]), "u = x² + a।", M)
def m_trig_sub(b):
    q, ok = R.choice([("sin x cos x", "sin²x/2 + c"), ("sin²x cos x", "sin³x/3 + c"), ("cos²x sin x", "−cos³x/3 + c"), ("sec²x tan x", "tan²x/2 + c"), ("(ln x)/x", "(ln x)²/2 + c"), ("1/(x ln x)", "ln|ln x| + c")])
    b.add(f"∫{q} dx = কত?", ok, W(ok, ["sin²x/2 + c", "sin³x/3 + c", "−cos³x/3 + c", "tan²x/2 + c", "(ln x)²/2 + c", "ln|ln x| + c", "cos²x/2 + c"]), "উপযুক্ত প্রতিস্থাপন।", M)
def h_sub(b):
    q, ok = R.choice([("x/√(x² + 1)", "√(x² + 1) + c"), ("e^(√x)/√x", "2e^(√x) + c"), ("sin(ln x)/x", "−cos(ln x) + c"), ("x e^(−x²)", "−e^(−x²)/2 + c"), ("eˣ sin(eˣ)", "−cos(eˣ) + c"), ("(1 + ln x)/x", "(1 + ln x)²/2 + c")])
    b.add(f"∫{q} dx = কত?", ok, W(ok, ["√(x² + 1) + c", "2e^(√x) + c", "−cos(ln x) + c", "−e^(−x²)/2 + c", "−cos(eˣ) + c", "(1 + ln x)²/2 + c", "e^(√x) + c"]), "প্রতিস্থাপন।", H)
def h_gen(b):
    k = R.randint(2, 9); t = R.choice([0, 1, 2, 3])
    if t == 0: q, ok, ws = f"x/(x² + {k})", f"½ ln(x² + {k}) + c", [f"ln(x² + {k}) + c", f"2 ln(x² + {k}) + c", f"(1/√{k}) tan⁻¹(x/√{k}) + c"]
    elif t == 1: q, ok, ws = f"x e^({k}x²)", f"e^({k}x²)/{2 * k} + c", [f"e^({k}x²)/{k} + c", f"{2 * k}e^({k}x²) + c", f"x²e^({k}x²)/2 + c"]
    elif t == 2: q, ok, ws = f"sin x/({k} + cos x)", f"−ln|{k} + cos x| + c", [f"ln|{k} + cos x| + c", f"−ln|{k} + sin x| + c", f"cos x/({k} + cos x) + c"]
    else: q, ok, ws = f"(2x + {k})/(x² + {k}x + 1)", f"ln|x² + {k}x + 1| + c", [f"2 ln|x² + {k}x + 1| + c", f"½ ln|x² + {k}x + 1| + c", f"(x² + {k}x)/(x² + {k}x + 1) + c"]
    b.add(f"∫{q} dx = কত?", ok, ws, "প্রতিস্থাপন।", H)
p10b = run('10.B', R, fx10b, [e_lin, e_exp], [m_ln, m_sub, m_trig_sub], [h_sub, h_gen], caps=(20, 18, 20))

fx10c = [
 ("∫tan x dx = কত?", "ln|sec x| + c", ["sec²x + c", "ln|cos x| + c", "−ln|sec x| + c"], "", E), ("∫cot x dx = কত?", "ln|sin x| + c", ["ln|cos x| + c", "−cosec²x + c", "−ln|sin x| + c"], "", E),
 ("∫sec x dx = কত?", "ln|sec x + tan x| + c", ["sec x tan x + c", "ln|sec x| + c", "tan x + c"], "", M), ("∫cosec x dx = কত?", "ln|cosec x − cot x| + c", ["−cosec x cot x + c", "ln|sin x| + c", "−cot x + c"], "", M),
 ("∫sin²x dx = কত?", "x/2 − (sin 2x)/4 + c", ["x/2 + (sin 2x)/4 + c", "sin³x/3 + c", "−cos²x + c"], "sin²x = (1 − cos 2x)/2।", M), ("∫cos²x dx = কত?", "x/2 + (sin 2x)/4 + c", ["x/2 − (sin 2x)/4 + c", "cos³x/3 + c", "sin²x + c"], "", M),
]
def e_kx(b):
    k = R.randint(2, 8); fn = R.choice(['sin', 'cos', 'sec²'])
    ok = {'sin': f"−(cos {k}x)/{k} + c", 'cos': f"(sin {k}x)/{k} + c", 'sec²': f"(tan {k}x)/{k} + c"}[fn]
    b.add(f"∫{fn} {k}x dx = কত?", ok, W(ok, [ok.replace(f"/{k}", f"·{k}").replace('(', '').replace(')', ''), {'sin': f"(cos {k}x)/{k} + c", 'cos': f"−(sin {k}x)/{k} + c", 'sec²': f"(sec {k}x)/{k} + c"}[fn], ok.replace(f"/{k}", '')]), "", E)
def m_prod(b):
    a, c = R.sample(range(1, 7), 2)
    if a < c: a, c = c, a
    ok = f"−(cos {a + c}x)/{2 * (a + c)} − (cos {a - c}x)/{2 * (a - c)} + c".replace(' 1x', ' x').replace('cos 1x', 'cos x')
    b.add(f"∫sin {a}x cos {c}x dx = কত?", ok, W(ok, [ok.replace('−', '+'), f"(sin {a}x sin {c}x)/{a * c} + c", f"−(cos {a + c}x)/{a + c} + c"]), "2 sin A cos B = sin(A + B) + sin(A − B)।", M)
def m_sq(b):
    k = R.randint(2, 6); fn = R.choice(['sin', 'cos'])
    ok = f"x/2 {'−' if fn == 'sin' else '+'} (sin {2 * k}x)/{4 * k} + c"
    b.add(f"∫{fn}²{k}x dx = কত?", ok, W(ok, [f"x/2 {'+' if fn == 'sin' else '−'} (sin {2 * k}x)/{4 * k} + c", f"x/2 {'−' if fn == 'sin' else '+'} (sin {2 * k}x)/{2 * k} + c", f"{fn}³{k}x/{3 * k} + c"]), "অর্ধকোণ সূত্র।", M)
def h_misc(b):
    q, ok = R.choice([("1/(1 + cos x)", "tan(x/2) + c"), ("1/(1 − cos x)", "−cot(x/2) + c"), ("√(1 + cos 2x)", "√2 sin x + c (cos x ≥ 0)"), ("sin³x", "−cos x + cos³x/3 + c"), ("cos³x", "sin x − sin³x/3 + c"), ("tan³x sec²x", "tan⁴x/4 + c"), ("1/(sin²x cos²x)", "tan x − cot x + c")])
    b.add(f"∫{q} dx = কত?", ok, W(ok, ["tan(x/2) + c", "−cot(x/2) + c", "√2 sin x + c (cos x ≥ 0)", "−cos x + cos³x/3 + c", "sin x − sin³x/3 + c", "tan⁴x/4 + c", "tan x − cot x + c"]), "", H)
def e_k2(b):
    k = R.randint(2, 8); t = R.choice(['tan', 'cot', 'cosec²'])
    ok = {'tan': f"(1/{k}) ln|sec {k}x| + c", 'cot': f"(1/{k}) ln|sin {k}x| + c", 'cosec²': f"−(cot {k}x)/{k} + c"}[t]
    ws = {'tan': [f"ln|sec {k}x| + c", f"{k} ln|sec {k}x| + c", f"(1/{k}) ln|cos {k}x| + c"], 'cot': [f"ln|sin {k}x| + c", f"(1/{k}) ln|cos {k}x| + c", f"−(1/{k}) ln|sin {k}x| + c"], 'cosec²': [f"(cot {k}x)/{k} + c", f"−cot {k}x + c", f"(tan {k}x)/{k} + c"]}[t]
    b.add(f"∫{t} {k}x dx = কত?", ok, ws, "", E)
def m_prod2(b):
    a, c = R.sample(range(1, 7), 2)
    if a < c: a, c = c, a
    sx = lambda k: 'sin x' if k == 1 else f"sin {k}x"
    t = R.choice(['cc', 'ss'])
    if t == 'cc': ok = f"{sx(a + c)}/{2 * (a + c)} + {sx(a - c)}/{2 * (a - c)} + c"; ws = [f"{sx(a + c)}/{2 * (a + c)} − {sx(a - c)}/{2 * (a - c)} + c", f"{sx(a + c)}/{a + c} + {sx(a - c)}/{a - c} + c", f"−{sx(a + c)}/{2 * (a + c)} + c"]
    else: ok = f"{sx(a - c)}/{2 * (a - c)} − {sx(a + c)}/{2 * (a + c)} + c"; ws = [f"{sx(a - c)}/{2 * (a - c)} + {sx(a + c)}/{2 * (a + c)} + c", f"{sx(a + c)}/{2 * (a + c)} − {sx(a - c)}/{2 * (a - c)} + c", f"−{sx(a - c)}/{a - c} + c"]
    q = f"cos {a}x cos {c}x" if t == 'cc' else f"sin {a}x sin {c}x"
    b.add(f"∫{q} dx = কত?".replace(' 1x', ' x'), ok, ws, "গুণফলকে যোগফলে রূপান্তর।", M)
def h_gen(b):
    k = R.randint(2, 9); t = R.choice([0, 1, 2])
    if t == 0: q, ok, ws = f"tan²{k}x", f"(tan {k}x)/{k} − x + c", [f"(tan {k}x)/{k} + x + c", f"tan {k}x − x + c", f"(sec²{k}x)/{k} + c"]
    elif t == 1: q, ok, ws = f"sin {k}x cos {k}x", f"−(cos {2 * k}x)/{4 * k} + c", [f"(cos {2 * k}x)/{4 * k} + c", f"−(cos {2 * k}x)/{2 * k} + c", f"(sin²{k}x)/{k} + c"]
    else: q, ok, ws = f"1/(1 + cos {k}x)", f"(1/{k}) tan({k}x/2) + c", [f"tan({k}x/2) + c", f"(2/{k}) tan({k}x/2) + c", f"−(1/{k}) cot({k}x/2) + c"]
    b.add(f"∫{q} dx = কত?", ok, ws, "ত্রিকোণমিতিক অভেদ ব্যবহার করে।", H)
p10c = run('10.C', R, fx10c, [e_kx, e_k2], [m_prod, m_sq, m_prod2], [h_misc, h_gen], caps=(30, 30, 25))

fx10d = [
 ("অংশায়ন সূত্র ∫u dv = কত?", "uv − ∫v du", ["uv + ∫v du", "u′v − ∫uv′", "∫u du ∫v dv"], "", E), ("∫x eˣ dx = কত?", "eˣ(x − 1) + c", ["eˣ(x + 1) + c", "x eˣ + c", "x²eˣ/2 + c"], "", E),
 ("∫ln x dx = কত?", "x ln x − x + c", ["1/x + c", "x ln x + c", "ln x/x + c"], "", E), ("∫x cos x dx = কত?", "x sin x + cos x + c", ["x sin x − cos x + c", "−x sin x + c", "x²sin x/2 + c"], "", M),
 ("∫x sin x dx = কত?", "−x cos x + sin x + c", ["x cos x − sin x + c", "x cos x + sin x + c", "−x cos x − sin x + c"], "", M), ("∫eˣ(f(x) + f′(x)) dx = কত?", "eˣf(x) + c", ["eˣf′(x) + c", "f(x) + c", "eˣ + f(x) + c"], "", M),
 ("ILATE নিয়মে কোনটির অগ্রাধিকার সবচেয়ে বেশি?", "বিপরীত ত্রিকোণমিতিক ফাংশন", ["সূচক ফাংশন", "ত্রিকোণমিতিক ফাংশন", "বীজগাণিতিক ফাংশন"], "I-L-A-T-E।", E),
]
def e_xekx(b):
    k = R.randint(2, 5)
    ok = f"e^({k}x)(x/{k} − 1/{k * k}) + c"
    b.add(f"∫x e^({k}x) dx = কত?", ok, W(ok, [f"e^({k}x)(x/{k} + 1/{k * k}) + c", f"x e^({k}x)/{k} + c", f"e^({k}x)(x − 1) + c"]), "অংশায়ন।", E)
def m_xn_ln(b):
    n = R.randint(1, 4)
    ok = f"x{sup(n + 1)} ln x/{n + 1} − x{sup(n + 1)}/{(n + 1) ** 2} + c"
    b.add(f"∫x{sup(n)} ln x dx = কত?".replace('x¹', 'x'), ok, W(ok, [f"x{sup(n + 1)} ln x/{n + 1} + x{sup(n + 1)}/{(n + 1) ** 2} + c", f"x{sup(n + 1)} ln x + c", f"x{sup(n - 1)}/{n} + c".replace('x⁰', '1')]), "u = ln x।", M)
def m_ex(b):
    q, ok = R.choice([("eˣ(sin x + cos x)", "eˣ sin x + c"), ("eˣ(1/x − 1/x²)", "eˣ/x + c"), ("eˣ(ln x + 1/x)", "eˣ ln x + c"), ("eˣ(tan x + sec²x)", "eˣ tan x + c"), ("eˣ(x + 1)", "x eˣ + c"), ("eˣ(cos x − sin x)", "eˣ cos x + c")])
    b.add(f"∫{q} dx = কত?", ok, W(ok, ["eˣ sin x + c", "eˣ/x + c", "eˣ ln x + c", "eˣ tan x + c", "x eˣ + c", "eˣ cos x + c"]), "∫eˣ(f + f′) = eˣf।", M)
def h_misc(b):
    q, ok = R.choice([("x² eˣ", "eˣ(x² − 2x + 2) + c"), ("tan⁻¹x", "x tan⁻¹x − ½ ln(1 + x²) + c"), ("sin⁻¹x", "x sin⁻¹x + √(1 − x²) + c"), ("x sec²x", "x tan x − ln|sec x| + c"), ("eˣ sin x", "eˣ(sin x − cos x)/2 + c"), ("(ln x)²", "x(ln x)² − 2x ln x + 2x + c")])
    b.add(f"∫{q} dx = কত?", ok, W(ok, ["eˣ(x² − 2x + 2) + c", "x tan⁻¹x − ½ ln(1 + x²) + c", "x sin⁻¹x + √(1 − x²) + c", "x tan x − ln|sec x| + c", "eˣ(sin x − cos x)/2 + c", "x(ln x)² − 2x ln x + 2x + c", "eˣ(x² + 2x + 2) + c"]), "অংশায়ন।", H)
def e_more(b):
    k = R.randint(2, 9); t = R.choice([0, 1, 2, 3])
    if t == 0: q, ok, ws = f"x sin {k}x", f"−(x cos {k}x)/{k} + (sin {k}x)/{k * k} + c", [f"(x cos {k}x)/{k} − (sin {k}x)/{k * k} + c", f"−x cos {k}x + sin {k}x + c", f"−(x cos {k}x)/{k} − (sin {k}x)/{k * k} + c"]
    elif t == 1: q, ok, ws = f"x cos {k}x", f"(x sin {k}x)/{k} + (cos {k}x)/{k * k} + c", [f"(x sin {k}x)/{k} − (cos {k}x)/{k * k} + c", f"x sin {k}x + cos {k}x + c", f"−(x sin {k}x)/{k} + c"]
    elif t == 2: q, ok, ws = f"{k}x eˣ", f"{k}eˣ(x − 1) + c", [f"{k}eˣ(x + 1) + c", f"{k}x eˣ + c", f"eˣ(x − {k}) + c"]
    else: q, ok, ws = f"{k} ln x", f"{k}(x ln x − x) + c", [f"{k}/x + c", f"{k}x ln x + c", f"{k}(x ln x + x) + c"]
    b.add(f"∫{q} dx = কত?", ok, ws, "অংশায়ন সূত্র।", E)
def m_lin(b):
    a, c = R.randint(1, 5), R.randint(-5, 5); t = R.choice([0, 1, 2]); L1 = px({1: a, 0: c}); L2 = px({1: a, 0: c - a}) if (a or c - a) else '0'; L3 = px({1: a, 0: c + a})
    if t == 0: q, ok, ws = f"({L1})eˣ", f"eˣ({L2}) + c", [f"eˣ({L3}) + c", f"eˣ({L1}) + c", f"{num(a)}eˣ + c"]
    elif t == 1: q, ok, ws = f"({L1}) sin x", f"−({L1}) cos x + {co(a, 'sin x')} + c", [f"({L1}) cos x − {co(a, 'sin x')} + c", f"−({L1}) cos x − {co(a, 'sin x')} + c", f"({L1}) sin x + c"]
    else: q, ok, ws = f"({L1}) cos x", f"({L1}) sin x + {co(a, 'cos x')} + c", [f"({L1}) sin x − {co(a, 'cos x')} + c", f"−({L1}) sin x + {co(a, 'cos x')} + c", f"({L1}) cos x + c"]
    b.add(f"∫{q} dx = কত?", ok, ws, "u = ax + b ধরে অংশায়ন।", M)
def h_gen(b):
    k = R.randint(2, 9); t = R.choice([0, 1, 2])
    q, ok = [(f"e^({k}x)({k} sin x + cos x)", f"e^({k}x) sin x + c"), (f"e^({k}x)({k}x + 1)", f"x e^({k}x) + c"), (f"e^({k}x)({k} ln x + 1/x)", f"e^({k}x) ln x + c")][t]
    b.add(f"∫{q} dx = কত?", ok, W(ok, [f"e^({k}x) sin x + c", f"x e^({k}x) + c", f"e^({k}x) ln x + c", f"e^({k}x) cos x + c", f"e^({k}x)/{k} + c"]), "∫e^(kx)(kf + f′) dx = e^(kx) f।", H)
p10d = run('10.D', R, fx10d, [e_xekx, e_more], [m_xn_ln, m_ex, m_lin], [h_misc, h_gen], caps=(30, 30, 25))

fx10e = [
 ("∫dx/(x² + a²) = কত?", "(1/a) tan⁻¹(x/a) + c", ["tan⁻¹(x/a) + c", "(1/2a) ln|(x − a)/(x + a)| + c", "sin⁻¹(x/a) + c"], "", E), ("∫dx/√(a² − x²) = কত?", "sin⁻¹(x/a) + c", ["(1/a) sin⁻¹(x/a) + c", "cos⁻¹(x/a) + c", "ln|x + √(a² − x²)| + c"], "", E),
 ("∫dx/(x² − a²) = কত?", "(1/2a) ln|(x − a)/(x + a)| + c", ["(1/2a) ln|(x + a)/(x − a)| + c", "(1/a) tan⁻¹(x/a) + c", "ln|x² − a²| + c"], "", M), ("∫dx/√(x² + a²) = কত?", "ln|x + √(x² + a²)| + c", ["sin⁻¹(x/a) + c", "tan⁻¹(x/a) + c", "√(x² + a²) + c"], "", M),
 ("∫dx/(1 + x²) = কত?", "tan⁻¹x + c", ["ln(1 + x²) + c", "sin⁻¹x + c", "1/(1 + x²) + c"], "", E),
]
def e_atan(b):
    a = R.randint(2, 9)
    ok = f"(1/{a}) tan⁻¹(x/{a}) + c"
    b.add(f"∫dx/(x² + {a * a}) = কত?", ok, W(ok, [f"tan⁻¹(x/{a}) + c", f"(1/{a}) tan⁻¹(x) + c", f"(1/{2 * a}) ln|(x − {a})/(x + {a})| + c"]), "", E)
def e_asin(b):
    a = R.randint(2, 9)
    ok = f"sin⁻¹(x/{a}) + c"
    b.add(f"∫dx/√({a * a} − x²) = কত?", ok, W(ok, [f"(1/{a}) sin⁻¹(x/{a}) + c", f"cos⁻¹(x/{a}) + c", f"(1/{a}) tan⁻¹(x/{a}) + c"]), "", E)
def m_pf(b):
    p, q = sorted(R.sample(range(-5, 6), 2))
    d = q - p
    ok = f"(1/{d}) ln|(x {'−' if q >= 0 else '+'} {abs(q)})/(x {'−' if p >= 0 else '+'} {abs(p)})| + c".replace('(x − 0)', 'x').replace('(x + 0)', 'x').replace('(1/1) ', '')
    w = f"(1/{d}) ln|(x {'−' if p >= 0 else '+'} {abs(p)})/(x {'−' if q >= 0 else '+'} {abs(q)})| + c".replace('(x − 0)', 'x').replace('(x + 0)', 'x').replace('(1/1) ', '')
    fa = lambda v: f"(x {'−' if v >= 0 else '+'} {abs(v)})".replace('(x − 0)', 'x').replace('(x + 0)', 'x')
    b.add(f"∫dx/({fa(p)}{fa(q)}) = কত?".replace('(x', 'x', 0), ok, W(ok, [w, f"ln|{fa(p)}{fa(q)}| + c", f"(1/{d}) tan⁻¹(x) + c"]), "আংশিক ভগ্নাংশ।", M)
def m_kx(b):
    a, k = R.randint(1, 5), R.randint(2, 4)
    ok = f"(1/{a * k}) tan⁻¹({k}x/{a}) + c".replace('/1)', ')')
    b.add(f"∫dx/({k * k}x² + {a * a}) = কত?", ok, W(ok, [f"(1/{a}) tan⁻¹({k}x/{a}) + c".replace('/1)', ')'), f"(1/{k}) tan⁻¹(x/{a}) + c", f"tan⁻¹({k}x) + c"]), "u = kx প্রতিস্থাপন।", M)
def h_complete(b):
    h, a = R.randint(1, 4), R.randint(1, 4)
    ok = f"(1/{a}) tan⁻¹((x + {h})/{a}) + c".replace('(1/1) ', '').replace('/1)', ')')
    b.add(f"∫dx/(x² + {2 * h}x + {h * h + a * a}) = কত?", ok, W(ok, [f"tan⁻¹(x + {h}) + c", f"(1/{a}) tan⁻¹((x − {h})/{a}) + c".replace('(1/1) ', '').replace('/1)', ')'), f"ln|x² + {2 * h}x + {h * h + a * a}| + c"]), "পূর্ণবর্গ করে।", H)
def h_frac(b):
    q, ok = R.choice([("x/(x + 1)", "x − ln|x + 1| + c"), ("(x + 2)/(x + 1)", "x + ln|x + 1| + c"), ("x²/(x² + 1)", "x − tan⁻¹x + c"), ("1/(x(x + 1))", "ln|x/(x + 1)| + c"), ("(2x + 3)/(x² + 3x + 2)", "ln|x² + 3x + 2| + c")])
    b.add(f"∫{q} dx = কত?", ok, W(ok, ["x − ln|x + 1| + c", "x + ln|x + 1| + c", "x − tan⁻¹x + c", "ln|x/(x + 1)| + c", "ln|x² + 3x + 2| + c", "tan⁻¹x + c"]), "", H)
def e_alog(b):
    a = R.randint(2, 9); t = R.choice([0, 1])
    if t == 0: q, ok, ws = f"dx/(x² − {a * a})", f"(1/{2 * a}) ln|(x − {a})/(x + {a})| + c", [f"(1/{2 * a}) ln|(x + {a})/(x − {a})| + c", f"(1/{a}) tan⁻¹(x/{a}) + c", f"ln|x² − {a * a}| + c"]
    else: q, ok, ws = f"dx/√(x² + {a * a})", f"ln|x + √(x² + {a * a})| + c", [f"sin⁻¹(x/{a}) + c", f"(1/{a}) tan⁻¹(x/{a}) + c", f"√(x² + {a * a}) + c"]
    b.add(f"∫{q} = কত?", ok, ws, "বিশেষ সূত্র।", E)
p10e = run('10.E', R, fx10e, [e_atan, e_asin, e_alog], [m_pf, m_kx], [h_complete, h_frac], caps=(20, 30, 20))

fx10f = [
 ("∫ₐᵇ f(x) dx = F(x)|ₐᵇ হলে মান কত?", "F(b) − F(a)", ["F(a) − F(b)", "F(a) + F(b)", "F(b)·F(a)"], "", E), ("∫ₐᵃ f(x) dx = কত?", "0", ["f(a)", "2f(a)", "a"], "", E),
 ("∫ₐᵇ f(x) dx = −∫ ? ", "∫ᵦᵃ f(x) dx", ["∫ₐᵇ f(−x) dx", "∫₀ᵇ f(x) dx", "0"], "সীমা বিনিময়ে চিহ্ন বদলায়।", M),
 ("f বিজোড় ফাংশন হলে ∫₋ₐᵃ f(x) dx = কত?", "0", ["2∫₀ᵃ f(x) dx", "f(a)", "1"], "", M), ("f জোড় ফাংশন হলে ∫₋ₐᵃ f(x) dx = কত?", "2∫₀ᵃ f(x) dx", ["0", "∫₀ᵃ f(x) dx", "f(a) − f(−a)"], "", M),
]
def e_poly(b):
    a, c = R.randint(-3, 3), R.randint(-4, 4); lo, hi = sorted(R.sample(range(0, 5), 2))
    v = F(a, 3) * (hi ** 3 - lo ** 3) + F(c, 2) * (hi * hi - lo * lo)
    if not a and not c: return
    b.add(f"∫[{lo}→{hi}] ({px({2: a, 1: c})}) dx = কত?", num(v), W(num(v), [num(v + 1), num(-v) if v else '1', num(F(a, 3) * hi ** 3 + F(c, 2) * hi * hi), num(v * 2)]), "F(b) − F(a)।", E)
def e_std(b):
    q, ok = R.choice([("∫[0→π/2] sin x dx", '1'), ("∫[0→π/2] cos x dx", '1'), ("∫[0→π] sin x dx", '2'), ("∫[0→1] eˣ dx", 'e − 1'), ("∫[1→e] (1/x) dx", '1'), ("∫[0→π/4] sec²x dx", '1'), ("∫[0→1] 1/(1 + x²) dx", 'π/4'), ("∫[0→1] 1/√(1 − x²) dx", 'π/2'), ("∫[0→2π] sin x dx", '0'), ("∫[−1→1] x³ dx", '0')])
    b.add(f"{q} = কত?", ok, W(ok, ['0', '1', '2', 'e − 1', 'π/4', 'π/2', 'e']), "", E)
def m_kx(b):
    k = R.randint(2, 5); n = R.randint(1, 4)
    v = F(k ** (n + 1), n + 1)
    b.add(f"∫[0→{k}] x{sup(n)} dx = কত?".replace('x¹', 'x'), fr(v), W(fr(v), [fr(F(k ** n, n)), str(k ** (n + 1)), fr(v + 1)]), "", M)
def m_sym(b):
    a = R.randint(1, 4); n = R.choice([1, 3, 5])
    q, ok = R.choice([(f"∫[−{a}→{a}] x{sup(n)} dx".replace('x¹', 'x'), '0'), (f"∫[−{a}→{a}] sin x dx", '0'), (f"∫[−π→π] x² sin x dx", '0'), (f"∫[−{a}→{a}] x² dx", fr(F(2 * a ** 3, 3)))])
    b.add(f"{q} = কত?", ok, W(ok, ['0', fr(F(2 * a ** 3, 3)), fr(F(a ** 3, 3)), str(2 * a)]), "জোড়/বিজোড় ফাংশন।", M)
def m_sub(b):
    a = R.randint(1, 4)
    q, ok = R.choice([("∫[0→1] 2x e^(x²) dx", 'e − 1'), ("∫[0→π/2] sin x cos x dx", '1/2'), ("∫[1→e] (ln x)/x dx", '1/2'), ("∫[0→1] x/(1 + x²) dx", '½ ln 2'), ("∫[0→π/2] sin²x dx", 'π/4'), ("∫[0→π/2] cos²x dx", 'π/4')])
    b.add(f"{q} = কত?", ok, W(ok, ['e − 1', '1/2', '½ ln 2', 'π/4', 'π/2', '1', 'ln 2']), "প্রতিস্থাপন।", M)
def h_prop(b):
    q, ok = R.choice([("∫[0→π/2] sin x/(sin x + cos x) dx", 'π/4'), ("∫[0→π/2] √(sin x)/(√(sin x) + √(cos x)) dx", 'π/4'), ("∫[0→1] x eˣ dx", '1'), ("∫[1→e] ln x dx", '1'), ("∫[0→π/2] x sin x dx", '1'), ("∫[0→a] f(x) dx = ∫[0→a] ? dx", 'f(a − x)')])
    b.add(f"{q} = কত?" if '?' not in q else q.replace('?', '…') + ' — ফাঁকা স্থানে কোনটি বসবে?', ok, W(ok, ['π/4', 'π/2', '1', '0', 'f(a − x)', 'f(x − a)', 'e']), "নির্দিষ্ট যোগজের ধর্ম।", H)
def m_e(b):
    t = R.choice([0, 1, 2]); k = R.randint(2, 9)
    if t == 0: q, ok, ws = f"∫[1→{k}] (1/x) dx", f"ln {k}", [f"1 − 1/{k}", f"{k} − 1", f"1/{k}"]
    elif t == 1: q, ok, ws = f"∫[0→π/{2 * k}] cos {k}x dx", f"1/{k}", ["1", f"{k}", f"π/{2 * k}"]
    else: q, ok, ws = f"∫[0→{k}] e^(x/{k}) dx", f"{k}(e − 1)", ["e − 1", f"e{sup(k)} − 1", f"(e − 1)/{k}"]
    b.add(f"{q} = কত?", ok, ws, "", M)
def h_abs(b):
    k = R.randint(2, 8); m = R.randint(1, k - 1)
    v = F(m * m + (k - m) ** 2, 2)
    b.add(f"∫[0→{k}] |x − {m}| dx = কত?", fr(v), W(fr(v), [fr(F(k * k, 2) - m * k), fr(F((k - m) ** 2, 2)), fr(v + 1), str(k - m)]), "দুই অংশে ভাগ করে।", H)
def h_pow(b):
    n = R.randint(1, 8)
    b.add(f"∫[0→π/2] sin{sup(n)}x/(sin{sup(n)}x + cos{sup(n)}x) dx = কত?".replace('sin¹', 'sin ').replace('cos¹', 'cos '), 'π/4', ['π/2', '1', '0'], "∫₀ᵃ f(x)dx = ∫₀ᵃ f(a − x)dx।", H)
p10f = run('10.F', R, fx10f, [e_poly, e_std], [m_kx, m_sym, m_sub, m_e], [h_prop, h_abs, h_pow], caps=(20, 18, 25))

fx10g = [
 ("y = f(x), x-অক্ষ এবং x = a, x = b দ্বারা আবদ্ধ ক্ষেত্রফল কোনটি (f ≥ 0)?", "∫ₐᵇ f(x) dx", ["∫ₐᵇ x f(x) dx", "f(b) − f(a)", "∫ₐᵇ f′(x) dx"], "", E),
 ("দুটি বক্ররেখা y = f(x) ও y = g(x) (f ≥ g) দ্বারা আবদ্ধ ক্ষেত্রফল কোনটি?", "∫ₐᵇ (f(x) − g(x)) dx", ["∫ₐᵇ (f(x) + g(x)) dx", "∫ₐᵇ f(x)g(x) dx", "∫ₐᵇ f(x) dx"], "", E),
 ("x² + y² = a² বৃত্তের ক্ষেত্রফল যোগজীকরণে কত পাওয়া যায়?", "πa²", ["2πa", "πa", "a²"], "4∫₀ᵃ √(a² − x²) dx।", M),
]
def e_par(b):
    a = R.randint(1, 6); k = R.randint(1, 3)
    v = F(k * a ** 3, 3)
    b.add(f"y = {co(k, 'x²')} বক্ররেখা, x-অক্ষ এবং x = 0 ও x = {a} দ্বারা আবদ্ধ ক্ষেত্রফল কত বর্গ একক?", fr(v), W(fr(v), [fr(F(k * a * a, 2)), str(k * a ** 3), fr(v + 1)]), "∫ x² dx।", E)
def e_line(b):
    m, a = R.randint(1, 5), R.randint(1, 6)
    v = F(m * a * a, 2)
    b.add(f"y = {co(m, 'x')} রেখা, x-অক্ষ এবং x = {a} দ্বারা আবদ্ধ ক্ষেত্রফল কত?", fr(v), W(fr(v), [str(m * a * a), fr(F(m * a, 2)), fr(v + 1)]), "ত্রিভুজের ক্ষেত্রফল।", E)
def m_between(b):
    k = R.randint(1, 4)
    # y = kx ও y = x²: ছেদ x = 0, k; ক্ষেত্রফল k³/6
    v = F(k ** 3, 6)
    b.add(f"y = x² ও y = {co(k, 'x')} দ্বারা আবদ্ধ ক্ষেত্রফল কত বর্গ একক?", fr(v), W(fr(v), [fr(F(k ** 3, 3)), fr(F(k ** 3, 2)), fr(F(k * k, 6))]), f"∫₀^{k} ({co(k, 'x')} − x²) dx।", M)
def m_sin(b):
    q, ok = R.choice([("y = sin x ও x-অক্ষ দ্বারা 0 থেকে π পর্যন্ত", '2'), ("y = cos x ও x-অক্ষ দ্বারা 0 থেকে π/2 পর্যন্ত", '1'), ("y = eˣ, x-অক্ষ, x = 0 ও x = 1 দ্বারা", 'e − 1'), ("y = 1/x, x-অক্ষ, x = 1 ও x = e দ্বারা", '1'), ("y = sin x ও x-অক্ষ দ্বারা 0 থেকে 2π পর্যন্ত", '4')])
    b.add(f"{q} আবদ্ধ ক্ষেত্রফল কত?", ok, W(ok, ['0', '1', '2', '4', 'e − 1', 'e']), "", M)
def m_circle(b):
    a = R.randint(1, 9)
    b.add(f"x² + y² = {a * a} বৃত্তের প্রথম চতুর্ভাগে অবস্থিত অংশের ক্ষেত্রফল কত?", piF(F(a * a, 4)), W(piF(F(a * a, 4)), [piF(a * a), piF(F(a * a, 2)), piF(F(a, 4))]), "πa²/4।", M)
def h_parab(b):
    a = R.randint(1, 5)
    v = F(8 * a * a, 3)
    b.add(f"y² = {4 * a}x অধিবৃত্ত ও x = {a} রেখা দ্বারা আবদ্ধ ক্ষেত্রফল কত?", fr(v), W(fr(v), [fr(F(4 * a * a, 3)), fr(F(16 * a * a, 3)), str(2 * a * a)]), f"2∫₀^{a} 2√({a}x) dx।", H)
def h_two_par(b):
    a = R.randint(1, 4)
    v = F(16 * a * a, 3)
    b.add(f"y² = {4 * a}x ও x² = {4 * a}y অধিবৃত্তদ্বয় দ্বারা আবদ্ধ ক্ষেত্রফল কত?", fr(v), W(fr(v), [fr(F(8 * a * a, 3)), fr(F(32 * a * a, 3)), str(4 * a * a)]), "16a²/3।", H)
def h_ellipse(b):
    a, c = R.sample(range(2, 8), 2)
    b.add(f"x²/{a * a} + y²/{c * c} = 1 উপবৃত্তের ক্ষেত্রফল কত?", f"{a * c}π", W(f"{a * c}π", [f"{a * a * c * c}π", f"{a + c}π", piF(F(a * c, 4))]), "πab।", H)
def m_area2(b):
    t = R.choice([0, 1, 2])
    if t == 0:
        k, a = R.randint(1, 3), R.randint(1, 4); v = F(k * a ** 4, 4)
        b.add(f"y = {co(k, 'x³')}, x-অক্ষ, x = 0 ও x = {a} দ্বারা আবদ্ধ ক্ষেত্রফল কত?", fr(v), W(fr(v), [fr(F(k * a ** 3, 3)), fr(v * 2), str(k * a ** 4)]), "∫ x³ dx।", M)
    elif t == 1:
        n = R.randint(1, 6); v = F(2 * n ** 3, 3)
        b.add(f"y = √x, x-অক্ষ, x = 0 ও x = {n * n} দ্বারা আবদ্ধ ক্ষেত্রফল কত?", fr(v), W(fr(v), [fr(F(n ** 3, 3)), fr(F(3 * n ** 3, 2)), str(n ** 3)]), "∫ √x dx = (2/3)x^(3/2)।", M)
    else:
        r = R.randint(1, 5); c = r * r; v = F(4 * r ** 3, 3)
        b.add(f"y = x² বক্ররেখা ও y = {c} রেখা দ্বারা আবদ্ধ ক্ষেত্রফল কত?", fr(v), W(fr(v), [fr(F(2 * r ** 3, 3)), fr(F(8 * r ** 3, 3)), str(2 * r ** 3)]), f"∫[−{r}→{r}] ({c} − x²) dx।", M)
def m_axes(b):
    m, c = R.randint(1, 5), R.randint(1, 10)
    v = F(c * c, 2 * m)
    b.add(f"y = {c} − {co(m, 'x')} রেখা ও অক্ষদ্বয় দ্বারা প্রথম চতুর্ভাগে আবদ্ধ ক্ষেত্রফল কত?", fr(v), W(fr(v), [fr(F(c * c, m)), fr(F(c, 2 * m)), fr(v + 1)]), f"∫[0→{fr(F(c, m))}] ({c} − {co(m, 'x')}) dx।", M)
p10g = run('10.G', R, fx10g, [e_par, e_line], [m_between, m_sin, m_circle, m_area2, m_axes], [h_parab, h_two_par, h_ellipse], caps=(20, 18, 10))
save('i10', p10a + p10b + p10c + p10d + p10e + p10f + p10g)
