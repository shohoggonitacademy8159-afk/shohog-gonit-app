#!/usr/bin/env python3
"""উচ্চতর গণিত (দশম, c10h) অধ্যায় 8–14:
8.1 রেডিয়ান ও বৃত্তীয় পরিমাপ · 8.2 সকল চতুর্ভাগে ত্রিকোণমিতিক অনুপাত · 8.3 ত্রিকোণমিতিক সমীকরণ
9.1 মূলদ সূচক · 9.2 লগারিদম ও সূচকীয়/লগারিদমীয় ফাংশন · 10.1 (1 + x)ⁿ-এর বিস্তৃতি · 10.2 (x + y)ⁿ ও সাধারণ পদ
11.1 দূরত্ব · 11.2 ক্ষেত্রফল · 11.3 ঢাল · 11.4 সরলরেখার সমীকরণ · 12 সমতলীয় ভেক্টর · 13 ঘন জ্যামিতি · 14 সম্ভাবনা"""
import random, pathlib, sys, math
from fractions import Fraction as F
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from mcqlib import run, save, E, M, H, fr, near, num, pfmt, lin, surd, sup

R = random.Random(2026110103)
X = ('x',)
def setw(c, pool):
    out = []
    for w in pool:
        w = str(w)
        if w != str(c) and w not in out: out.append(w)
    return out
def rad(deg):
    v = F(deg, 180)
    if v == 0: return '0'
    n, d = v.numerator, v.denominator
    s = '−' if n < 0 else ''; n = abs(n)
    top = 'π' if n == 1 else f'{n}π'
    return s + (top if d == 1 else f'{top}/{d}')

# ---------------- 8.1 রেডিয়ান ----------------
fx81 = [
 ("1 রেডিয়ান কোণ বলতে কী বোঝায়?", "বৃত্তের ব্যাসার্ধের সমান চাপ কেন্দ্রে যে কোণ উৎপন্ন করে", ["ব্যাসের সমান চাপ যে কোণ উৎপন্ন করে", "এক সমকোণের 1/90 অংশ", "পরিধির সমান চাপ যে কোণ উৎপন্ন করে"], "রেডিয়ানের সংজ্ঞা।", E),
 ("π রেডিয়ান = কত ডিগ্রি?", "180°", ["90°", "360°", "57°"], "π রেডিয়ান = 180°।", E),
 ("1 রেডিয়ান প্রায় কত ডিগ্রি?", "57.3°", ["60°", "45°", "180°"], "180°/π ≈ 57.3°।", E),
 ("ব্যাসার্ধ r ও কেন্দ্রস্থ কোণ θ (রেডিয়ানে) হলে বৃত্তচাপের দৈর্ঘ্য কত?", "rθ", ["r/θ", "θ/r", "πrθ/180"], "s = rθ।", E),
 ("রেডিয়ান কোণ কেমন রাশি?", "ধ্রুব কোণ (বৃত্তের আকারের উপর নির্ভর করে না)", ["বৃত্তের ব্যাসার্ধের উপর নির্ভরশীল", "সবসময় 1-এর বেশি", "শুধু সূক্ষ্মকোণের জন্য সংজ্ঞায়িত"], "অনুপাত হওয়ায় ধ্রুব।", M),
 ("1° = কত রেডিয়ান?", "π/180", ["180/π", "π/360", "1/π"], "180° = π রেডিয়ান।", E),
]
DEGS = [15, 18, 20, 30, 36, 40, 45, 60, 72, 75, 90, 105, 120, 135, 150, 180, 210, 225, 240, 270, 300, 315, 330, 360, 400, 450, 540, 720]
def e_d2r(b):
    d = R.choice(DEGS); ok = rad(d)
    b.add(f"{d}°-কে রেডিয়ানে প্রকাশ করলে কত?", ok, setw(ok, [rad(2 * d), rad(d // 2) if d % 2 == 0 else rad(d + 30), rad(180 - d) if d < 180 else rad(d - 90), rad(d + 45)]), f"{d}° × π/180 = {ok}।", E)
def e_r2d(b):
    d = R.choice(DEGS); ok = f"{d}°"
    b.add(f"{rad(d)} রেডিয়ান = কত ডিগ্রি?", ok, setw(ok, [f"{2 * d}°", f"{d // 2}°" if d % 2 == 0 else f"{d + 30}°", f"{d + 45}°", f"{abs(180 - d)}°" if d != 180 else "90°"]), f"{rad(d)} × 180/π = {d}°।", E)
def e_arc(b):
    r, th = R.randint(2, 20), R.choice([F(1, 2), F(1), F(3, 2), F(2), F(5, 2), F(3), F(1, 4), F(3, 4)])
    s = r * th
    b.add(f"{r} সেমি ব্যাসার্ধের বৃত্তে {fr(th)} রেডিয়ান কোণ উৎপন্নকারী চাপের দৈর্ঘ্য কত সেমি?", fr(s), setw(fr(s), [fr(F(r) / th), fr(th / r), fr(s * 2), fr(s + 1)]), f"s = rθ = {r} × {fr(th)} = {fr(s)}।", E)
def e_theta(b):
    r, s = R.randint(2, 15), R.randint(1, 30)
    th = F(s, r)
    b.add(f"{r} সেমি ব্যাসার্ধের বৃত্তে {s} সেমি দৈর্ঘ্যের চাপ কেন্দ্রে কত রেডিয়ান কোণ উৎপন্ন করে?", fr(th), setw(fr(th), [fr(F(r, s)), str(r * s), fr(th + 1), fr(th / 2)]), f"θ = s/r = {s}/{r} = {fr(th)}।", E)
def m_clock(b):
    h, m = R.randint(1, 12), R.choice([0, 10, 15, 20, 30, 40, 45, 50])
    ang = abs(F(60 * h - 11 * m, 2)) % 360
    if ang > 180: ang = 360 - ang
    if ang.denominator != 1: return
    ang = int(ang)
    ok = rad(ang) if ang else '0'
    if not ang: return
    b.add(f"ঘড়িতে যখন {h}টা বেজে {m} মিনিট, তখন ঘণ্টা ও মিনিটের কাঁটার মধ্যবর্তী কোণ রেডিয়ানে কত?".replace(' বেজে 0 মিনিট', 'টা') .replace('টাটা', 'টা'), ok, setw(ok, [rad(360 - ang), rad(ang + 15) if ang + 15 <= 360 else rad(ang - 15), rad(30 * h % 360) if 30 * h % 360 not in (0, ang) else rad(ang + 30), rad(abs(6 * m - 30 * h) % 360) if abs(6 * m - 30 * h) % 360 not in (0, ang) else rad(ang + 45)]), f"কোণ = |30h − 5.5m| = {ang}° = {ok}।", M)
def m_wheel(b):
    r = R.choice([7, 14, 21, 28, 35, 42]); n = R.randint(2, 50)
    d = F(2 * 22 * r * n, 7)
    b.add(f"{r} সেমি ব্যাসার্ধের একটি চাকা {n} বার ঘুরলে কত সেমি পথ অতিক্রম করবে? (π = 22/7)", fr(d), setw(fr(d), [fr(d / 2), fr(F(22 * r * r * n, 7)), fr(d + 2 * r), fr(d * 2)]), f"পরিধি = 2πr = {fr(F(44 * r, 7))}; {n} বারে {fr(d)}।", M)
def m_speed(b):
    r = R.choice([7, 14, 21, 35]); rpm = R.randint(10, 60)
    th = F(2 * rpm)   # π রেডিয়ান প্রতি মিনিট
    ok = f"{2 * rpm}π"
    b.add(f"একটি চাকা প্রতি মিনিটে {rpm} বার ঘোরে। এক মিনিটে চাকাটি কত রেডিয়ান কোণ উৎপন্ন করে?", ok, setw(ok, [f"{rpm}π", f"{4 * rpm}π", f"{rpm * 360}", f"{2 * rpm}"]), f"প্রতি ঘূর্ণনে 2π; {rpm} বারে {2 * rpm}π।", M)
def m_sector(b):
    r = R.randint(2, 14); d = R.choice([30, 45, 60, 90, 120, 135, 150])
    A = F(r * r, 2) * F(d, 180)
    ok = (f"{fr(A)}π" if A != 1 else 'π').replace('1π', 'π') if A.numerator != 1 or A.denominator != 1 else 'π'
    if A.numerator == 1 and A.denominator > 1: ok = f"π/{A.denominator}"
    elif A.denominator > 1: ok = f"{A.numerator}π/{A.denominator}"
    else: ok = f"{A.numerator}π" if A.numerator > 1 else 'π'
    alt = A * 2
    b.add(f"{r} সেমি ব্যাসার্ধের বৃত্তের {d}° কেন্দ্রস্থ কোণবিশিষ্ট বৃত্তকলার ক্ষেত্রফল কত বর্গ সেমি?", ok, setw(ok, [f"{alt.numerator}π/{alt.denominator}" if alt.denominator > 1 else f"{alt.numerator}π", f"{r * r}π", f"{fr(F(r * d, 180))}π", f"{fr(A)}"]), f"(1/2)r²θ = (1/2)·{r * r}·{rad(d)} = {ok}।", M)
def m_angle_tri(b):
    a, c = R.sample([15, 30, 36, 45, 54, 60, 72, 75, 90], 2)
    rest = 180 - a - c
    if rest <= 0: return
    ok = rad(rest)
    b.add(f"একটি ত্রিভুজের দুটি কোণ {rad(a)} ও {rad(c)} রেডিয়ান হলে তৃতীয় কোণ কত রেডিয়ান?", ok, setw(ok, [rad(rest + 15), rad(a + c), rad(360 - a - c), rad(abs(rest - 30)) if rest != 30 else rad(45)]), f"π − {rad(a)} − {rad(c)} = {ok}।", M)
def h_earth(b):
    R_ = R.choice([6400, 6370, 6000]); ang = R.choice([1, 2, 5, 10, 15, 30])
    d = F(R_ * ang, 180)
    ok = f"{fr(d)}π"
    b.add(f"পৃথিবীর ব্যাসার্ধ {R_} কিমি ধরে, পৃথিবীর কেন্দ্রে {ang}° কোণ উৎপন্নকারী দুটি স্থানের দূরত্ব (চাপের দৈর্ঘ্য) কত কিমি?", ok, setw(ok, [f"{fr(d * 2)}π", f"{R_ * ang}π", f"{fr(F(R_, 180))}π", f"{fr(d / 2)}π"]), f"s = rθ = {R_} × {rad(ang)} = {ok}।", H)
def h_minute(b):
    L = R.choice([7, 14, 21, 28, 35]); m = R.choice([10, 15, 20, 30, 40, 45])
    s = F(2 * 22 * L * m, 7 * 60)
    b.add(f"একটি ঘড়ির মিনিটের কাঁটার দৈর্ঘ্য {L} সেমি। {m} মিনিটে কাঁটার অগ্রভাগ কত সেমি পথ অতিক্রম করে? (π = 22/7)", fr(s), setw(fr(s), [fr(s * 2), fr(s / 2), fr(F(22 * L * m, 7 * 30)) if F(22 * L * m, 7 * 30) != s else fr(s + 1), fr(F(L * m, 60))]), f"{m} মিনিটে কোণ {rad(6 * m)}; চাপ = {L} × {rad(6 * m)} = {fr(s)}।", H)
def h_poly(b):
    n = R.choice([5, 6, 8, 9, 10, 12, 15, 18])
    ok = rad(F(180 * (n - 2), n))
    if '/' not in ok and 'π' not in ok: return
    b.add(f"সুষম {n} বাহুবিশিষ্ট বহুভুজের প্রতিটি অন্তঃকোণ কত রেডিয়ান?", ok, setw(ok, [rad(F(360, n)), rad(F(180 * (n - 1), n)), rad(F(180, n)), rad(F(180 * (n - 2), n) + 10)]), f"(n − 2)π/n = {ok}।", H)
def h_ratio(b):
    a, c = R.randint(1, 5), R.randint(1, 5)
    if a == c or math.gcd(a, c) > 1: return
    # ত্রিভুজের কোণগুলোর অনুপাত a : c : (a + c)  ⇒ বৃহত্তম কোণ = π/2
    ok = 'π/2'
    b.add(f"একটি ত্রিভুজের কোণত্রয়ের অনুপাত {a} : {c} : {a + c} হলে বৃহত্তম কোণটি কত রেডিয়ান?", ok, setw(ok, [rad(F(180 * a, 2 * (a + c))), rad(F(180 * c, 2 * (a + c))), 'π/3', '2π/3']), f"বৃহত্তম কোণ = π × {a + c}/{2 * (a + c)} = π/2।", H)
p81 = run('8.1', R, fx81, [e_d2r, e_r2d, e_arc, e_theta], [m_clock, m_wheel, m_speed, m_sector, m_angle_tri], [h_earth, h_minute, h_poly, h_ratio])

# ---------------- 8.2 সকল চতুর্ভাগে ত্রিকোণমিতিক অনুপাত ----------------
BASE = {0: ('0', '1', '0'), 30: ('1/2', '√3/2', '1/√3'), 45: ('1/√2', '1/√2', '1'), 60: ('√3/2', '1/2', '√3'), 90: ('1', '0', None)}
def tval(fn, deg):
    deg %= 360
    q = deg // 90; r = deg % 90
    if r == 0:
        k = deg
        table = {0: ('0', '1', '0'), 90: ('1', '0', None), 180: ('0', '−1', '0'), 270: ('−1', '0', None)}
        v = table[k][['sin', 'cos', 'tan'].index(fn)]
        return v if v is not None else 'অসংজ্ঞায়িত'
    ref = {0: r, 1: 90 - r, 2: r, 3: 90 - r}[q]
    ref = r if q in (0, 2) else 90 - r
    ref = deg if q == 0 else (180 - deg if q == 1 else (deg - 180 if q == 2 else 360 - deg))
    sgn = {'sin': [1, 1, -1, -1], 'cos': [1, -1, -1, 1], 'tan': [1, -1, 1, -1]}[fn][q]
    v = BASE[ref][['sin', 'cos', 'tan'].index(fn)]
    return v if sgn > 0 else '−' + v
ALL = [d for d in range(0, 361, 15) if d % 30 == 0 or d % 45 == 0]
VALS = ['0', '1', '−1', '1/2', '−1/2', '√3/2', '−√3/2', '1/√2', '−1/√2', '√3', '−√3', '1/√3', '−1/√3', 'অসংজ্ঞায়িত']
fx82 = [
 ("কোন চতুর্ভাগে sin, cos, tan সবগুলো ধনাত্মক?", "প্রথম", ["দ্বিতীয়", "তৃতীয়", "চতুর্থ"], "প্রথম চতুর্ভাগে সব ধনাত্মক।", E),
 ("দ্বিতীয় চতুর্ভাগে কোন অনুপাতটি ধনাত্মক?", "sin", ["cos", "tan", "cot"], "দ্বিতীয় চতুর্ভাগে শুধু sin ও cosec ধনাত্মক।", E),
 ("তৃতীয় চতুর্ভাগে কোন অনুপাতটি ধনাত্মক?", "tan", ["sin", "cos", "sec"], "তৃতীয় চতুর্ভাগে tan ও cot ধনাত্মক।", E),
 ("চতুর্থ চতুর্ভাগে কোন অনুপাতটি ধনাত্মক?", "cos", ["sin", "tan", "cot"], "চতুর্থ চতুর্ভাগে cos ও sec ধনাত্মক।", E),
 ("sin(−θ) = কত?", "−sin θ", ["sin θ", "cos θ", "−cos θ"], "sin বিজোড় ফাংশন।", E),
 ("cos(−θ) = কত?", "cos θ", ["−cos θ", "sin θ", "−sin θ"], "cos জোড় ফাংশন।", E),
 ("sin(π/2 + θ) = কত?", "cos θ", ["−cos θ", "sin θ", "−sin θ"], "দ্বিতীয় চতুর্ভাগে sin ধনাত্মক; sin → cos।", M),
 ("cos(π/2 + θ) = কত?", "−sin θ", ["sin θ", "cos θ", "−cos θ"], "দ্বিতীয় চতুর্ভাগে cos ঋণাত্মক।", M),
 ("sin(π − θ) = কত?", "sin θ", ["−sin θ", "cos θ", "−cos θ"], "দ্বিতীয় চতুর্ভাগে sin ধনাত্মক।", M),
 ("cos(π − θ) = কত?", "−cos θ", ["cos θ", "sin θ", "−sin θ"], "দ্বিতীয় চতুর্ভাগে cos ঋণাত্মক।", M),
 ("tan(π + θ) = কত?", "tan θ", ["−tan θ", "cot θ", "−cot θ"], "তৃতীয় চতুর্ভাগে tan ধনাত্মক।", M),
 ("sin(3π/2 − θ) = কত?", "−cos θ", ["cos θ", "sin θ", "−sin θ"], "তৃতীয় চতুর্ভাগে sin ঋণাত্মক; sin → cos।", M),
 ("sin²θ + cos²θ = কত?", "1", ["0", "2", "tan²θ"], "মৌলিক অভেদ।", E),
 ("sec²θ − tan²θ = কত?", "1", ["0", "−1", "cot²θ"], "অভেদ।", E),
]
def e_val(b):
    fn = R.choice(['sin', 'cos', 'tan']); d = R.choice(ALL)
    ok = tval(fn, d)
    if fn == 'tan' and d % 90 == 0 and d % 180: pass
    b.add(f"{fn} {rad(d)} = কত?" if R.random() < .5 else f"{fn} {d}° = কত?", ok, setw(ok, R.sample([v for v in VALS if v != ok], 6)), f"রেফারেন্স কোণ ও চতুর্ভাগ অনুযায়ী চিহ্ন নিয়ে {ok}।", E)
def e_quad(b):
    d = R.choice([x for x in range(5, 360) if x % 90])
    q = d // 90 + 1
    names = {1: 'প্রথম', 2: 'দ্বিতীয়', 3: 'তৃতীয়', 4: 'চতুর্থ'}
    b.add(f"{d}° কোণটি কোন চতুর্ভাগে অবস্থিত?", names[q], [names[i] for i in (1, 2, 3, 4) if i != q], f"{90 * (q - 1)}° < {d}° < {90 * q}°।", E)
def e_sign(b):
    d = R.choice([x for x in ALL if x % 90]); fn = R.choice(['sin', 'cos', 'tan'])
    v = tval(fn, d); ok = 'ঋণাত্মক' if v.startswith('−') else 'ধনাত্মক'
    b.add(f"{fn} {d}°-এর চিহ্ন কেমন?", ok, setw(ok, ['ধনাত্মক', 'ঋণাত্মক', 'শূন্য', 'অসংজ্ঞায়িত']), f"{d}° কোণ {d // 90 + 1} নম্বর চতুর্ভাগে।", E)
def m_find(b):
    trip = R.choice([(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29)])
    o, a, h = trip; q = R.choice([2, 3, 4])
    sgn_s, sgn_c = {2: (1, -1), 3: (-1, -1), 4: (-1, 1)}[q]
    names = {2: 'দ্বিতীয়', 3: 'তৃতীয়', 4: 'চতুর্থ'}
    given = f"sin θ = {'−' if sgn_s < 0 else ''}{o}/{h}"
    fn = R.choice(['cos', 'tan'])
    if fn == 'cos': ok = f"{'−' if sgn_c < 0 else ''}{a}/{h}"; alts = [f"{'' if sgn_c < 0 else '−'}{a}/{h}", f"{'−' if sgn_c < 0 else ''}{o}/{h}", f"{'−' if sgn_c < 0 else ''}{a}/{o}"]
    else:
        st = sgn_s * sgn_c; ok = f"{'−' if st < 0 else ''}{o}/{a}"; alts = [f"{'' if st < 0 else '−'}{o}/{a}", f"{'−' if st < 0 else ''}{a}/{o}", f"{'−' if st < 0 else ''}{o}/{h}"]
    b.add(f"{given} এবং θ {names[q]} চতুর্ভাগে হলে {fn} θ = কত?", ok, setw(ok, alts), f"cos θ = {'−' if sgn_c < 0 else ''}√(1 − {o * o}/{h * h}) = {'−' if sgn_c < 0 else ''}{a}/{h}।", M)
def m_reduce(b):
    k = R.choice([90, 180, 270, 360]); fn = R.choice(['sin', 'cos', 'tan']); s = R.choice([1, -1])
    # f(k ± θ) in terms of θ (θ সূক্ষ্মকোণ)
    test = 20; d = (k + s * test) % 360
    cofn = {'sin': 'cos', 'cos': 'sin', 'tan': 'cot'}[fn] if k in (90, 270) else fn
    # সংখ্যাগত চিহ্ন বের করতে sin/cos/tan-এর মান ব্যবহার
    import math as m
    val = {'sin': m.sin, 'cos': m.cos, 'tan': m.tan}[fn](m.radians(d))
    base = {'sin': m.sin, 'cos': m.cos, 'tan': m.tan, 'cot': lambda x: 1 / m.tan(x)}[cofn](m.radians(test))
    sg = '' if val * base > 0 else '−'
    ok = f"{sg}{cofn} θ"
    arg = f"{rad(k)} {'+' if s > 0 else '−'} θ"
    b.add(f"{fn}({arg}) = কত?", ok, setw(ok, [f"{'−' if not sg else ''}{cofn} θ", f"{sg}{fn if cofn != fn else {'sin': 'cos', 'cos': 'sin', 'tan': 'cot'}[fn]} θ", f"{'−' if not sg else ''}{fn if cofn != fn else {'sin': 'cos', 'cos': 'sin', 'tan': 'cot'}[fn]} θ"]), f"{rad(k)}-এর {'বিজোড়' if k in (90, 270) else 'জোড়'} গুণিতক; চতুর্ভাগ অনুযায়ী চিহ্ন।", M)
def m_neg(b):
    d = R.choice([30, 45, 60, 120, 135, 150, 210, 240, 300, 330]); fn = R.choice(['sin', 'cos', 'tan'])
    ok = tval(fn, -d % 360)
    b.add(f"{fn}(−{d}°) = কত?", ok, setw(ok, R.sample([v for v in VALS if v != ok and v != 'অসংজ্ঞায়িত'], 5)), f"−{d}° ও {(-d) % 360}° সহপ্রান্তিক।", M)
def m_big(b):
    d = R.choice([30, 45, 60, 90, 120, 135, 150, 180, 210, 240, 300, 330]); k = R.randint(1, 3); fn = R.choice(['sin', 'cos', 'tan'])
    ok = tval(fn, d)
    b.add(f"{fn} {d + 360 * k}° = কত?", ok, setw(ok, R.sample([v for v in VALS if v != ok], 5)), f"{d + 360 * k}° = {k} × 360° + {d}°।", M)
def m_expr(b):
    a, c = R.sample([30, 45, 60, 120, 135, 150, 210, 225, 240, 300, 315, 330], 2)
    def num_(fn, d):
        import math as m
        return {'sin': m.sin, 'cos': m.cos}[fn](m.radians(d))
    v = num_('sin', a) ** 2 + num_('cos', c) ** 2
    vv = F(v).limit_denominator(8)
    if abs(float(vv) - v) > 1e-9: return
    ok = fr(vv)
    b.add(f"sin²{a}° + cos²{c}° = কত?", ok, setw(ok, ['1', '0', '1/2', '3/2', '2', '1/4', '3/4', '5/4']), f"sin²{a}° = {fr(F(num_('sin', a) ** 2).limit_denominator(8))}, cos²{c}° = {fr(F(num_('cos', c) ** 2).limit_denominator(8))}।", M)
def h_tan_find(b):
    trip = R.choice([(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25)]); o, a, h = trip; q = R.choice([2, 3, 4])
    sgn_t = {2: -1, 3: 1, 4: -1}[q]; sgn_s, sgn_c = {2: (1, -1), 3: (-1, -1), 4: (-1, 1)}[q]
    names = {2: 'দ্বিতীয়', 3: 'তৃতীয়', 4: 'চতুর্থ'}
    v = F(sgn_s * o + sgn_c * a, h)
    b.add(f"tan θ = {'−' if sgn_t < 0 else ''}{o}/{a} এবং θ {names[q]} চতুর্ভাগে হলে sin θ + cos θ = কত?", num(v), setw(num(v), [num(F(o + a, h)), num(-v), num(F(sgn_s * o - sgn_c * a, h)), num(F(o - a, h)) if F(o - a, h) not in (v, -v) else num(v + 1)]), f"sin θ = {'−' if sgn_s < 0 else ''}{o}/{h}, cos θ = {'−' if sgn_c < 0 else ''}{a}/{h}।", H)
def h_sum(b):
    fn = R.choice(['sin', 'cos'])
    k = R.choice([4, 6])
    angs = [180 * i // k for i in range(1, 2 * k)]
    import math as m
    v = sum({'sin': m.sin, 'cos': m.cos}[fn](m.radians(x)) for x in angs)
    vv = F(v).limit_denominator(4)
    if abs(float(vv) - v) > 1e-9: return
    b.add(f"{fn} {rad(angs[0])} + {fn} {rad(angs[1])} + … + {fn} {rad(angs[-1])} = কত? (প্রতি পদে কোণ {rad(angs[0])} করে বৃদ্ধি)", fr(vv) if vv >= 0 else '−' + fr(-vv), setw(fr(vv) if vv >= 0 else '−' + fr(-vv), ['0', '1', '−1', '2', '1/2']), "সম্পূরক/সহপ্রান্তিক জোড়ায় মান কাটাকাটি যায়।", H)
def h_identity(b):
    a = R.choice([10, 20, 25, 35, 40, 50, 70, 80])
    ok = '1'
    b.add(f"sin²{a}° + sin²{90 - a}° = কত?", ok, ['0', '2', f"2sin²{a}°"], f"sin{90 - a}° = cos{a}°; তাই যোগফল 1।", H)
def h_complex(b):
    d = R.choice([120, 135, 150, 210, 225, 240, 300, 315, 330])
    import math as m
    v = m.sin(m.radians(d)) * m.cos(m.radians(d))
    vv = F(v).limit_denominator(8)
    if abs(float(vv) - v) > 1e-9: return
    s = fr(vv) if vv >= 0 else '−' + fr(-vv)
    b.add(f"sin {d}° · cos {d}° = কত?", s, setw(s, ['√3/4', '−√3/4', '1/2', '−1/2', '1/4', '−1/4']), f"sin {d}° = {tval('sin', d)}, cos {d}° = {tval('cos', d)}।", H)
def h_sqrt3(b):
    d = R.choice([120, 150, 210, 240, 300, 330])
    import math as m
    v = m.tan(m.radians(d)) ** 2 + 1
    vv = F(v).limit_denominator(4)
    b.add(f"tan² {d}° + 1 = কত?", fr(vv), setw(fr(vv), ['4/3', '4', '2', '1', '3']), f"1 + tan²θ = sec²θ; sec {d}° = {'±'}... ⇒ {fr(vv)}।", H)
p82 = run('8.2', R, fx82, [e_val, e_quad, e_sign], [m_find, m_reduce, m_neg, m_big, m_expr], [h_tan_find, h_sum, h_identity, h_complex, h_sqrt3])

# ---------------- 8.3 ত্রিকোণমিতিক সমীকরণ ----------------
def sols(fn, val_deg_check, lo=0, hi=360):
    return [d for d in range(lo, hi + 1) if val_deg_check(d)]
def degset(ds): return '{' + ', '.join(rad(d) for d in sorted(ds)) + '}'
fx83 = [
 ("sin θ = 0 সমীকরণের সাধারণ সমাধান কোনটি?", "θ = nπ", ["θ = (2n + 1)π/2", "θ = 2nπ", "θ = nπ/2"], "sin θ শূন্য হয় π-এর গুণিতকে।", E),
 ("cos θ = 0 সমীকরণের সাধারণ সমাধান কোনটি?", "θ = (2n + 1)π/2", ["θ = nπ", "θ = 2nπ", "θ = nπ/4"], "π/2-এর বিজোড় গুণিতকে।", E),
 ("tan θ = 0 সমীকরণের সাধারণ সমাধান কোনটি?", "θ = nπ", ["θ = (2n + 1)π/2", "θ = 2nπ", "θ = nπ/3"], "tan θ = sin θ/cos θ।", E),
 ("sin θ = 2 সমীকরণের বাস্তব সমাধান কয়টি?", "কোনো সমাধান নেই", ["1টি", "2টি", "অসংখ্য"], "−1 ≤ sin θ ≤ 1।", M),
]
import math as _m
def fval(fn, d):
    return {'sin': _m.sin, 'cos': _m.cos, 'tan': _m.tan}[fn](_m.radians(d))
TARGETS = {'sin': [('1/2', .5), ('√3/2', 3 ** .5 / 2), ('1/√2', 2 ** -.5), ('−1/2', -.5), ('−√3/2', -(3 ** .5) / 2), ('−1/√2', -(2 ** -.5)), ('1', 1), ('−1', -1), ('0', 0)],
           'cos': [('1/2', .5), ('√3/2', 3 ** .5 / 2), ('1/√2', 2 ** -.5), ('−1/2', -.5), ('−√3/2', -(3 ** .5) / 2), ('−1/√2', -(2 ** -.5)), ('1', 1), ('−1', -1), ('0', 0)],
           'tan': [('1', 1), ('√3', 3 ** .5), ('1/√3', 3 ** -.5), ('−1', -1), ('−√3', -(3 ** .5)), ('−1/√3', -(3 ** -.5)), ('0', 0)]}
CAND = [d for d in range(0, 361) if d % 15 == 0]
def solve(fn, v, lo=0, hi=360, strict_hi=False):
    out = []
    for d in CAND:
        if d < lo or d > hi or (strict_hi and d == hi): continue
        if fn == 'tan' and d % 180 == 90: continue
        if abs(fval(fn, d) - v) < 1e-9: out.append(d)
    return out
def e_basic(b):
    fn = R.choice(['sin', 'cos', 'tan']); t, v = R.choice(TARGETS[fn])
    ds = solve(fn, v, 0, 90)
    if len(ds) != 1: return
    ok = rad(ds[0])
    b.add(f"{fn} θ = {t} হলে θ = কত? (0 ≤ θ ≤ π/2)", ok, setw(ok, ['0', 'π/6', 'π/4', 'π/3', 'π/2']), f"{fn} {rad(ds[0])} = {t}।", E)
def e_deg(b):
    fn = R.choice(['sin', 'cos', 'tan']); t, v = R.choice(TARGETS[fn])
    ds = solve(fn, v, 0, 90)
    if len(ds) != 1: return
    ok = f"{ds[0]}°"
    b.add(f"{fn} θ = {t} এবং 0° ≤ θ ≤ 90° হলে θ = কত ডিগ্রি?", ok, setw(ok, ['0°', '30°', '45°', '60°', '90°']), f"{fn} {ds[0]}° = {t}।", E)
def m_full(b):
    fn = R.choice(['sin', 'cos', 'tan']); t, v = R.choice(TARGETS[fn])
    ds = solve(fn, v, 0, 360, strict_hi=True)
    if len(ds) != 2: return
    ok = degset(ds)
    cands = [[ds[0], (180 - ds[0]) % 360], [ds[0], (ds[0] + 180) % 360], [ds[0]], [(ds[0] + 90) % 360, (ds[1] + 90) % 360], [(360 - ds[0]) % 360, (360 - ds[1]) % 360], [(ds[0] + 30) % 360, (ds[1] + 30) % 360], [(ds[0] + 60) % 360, (ds[1] + 60) % 360]]
    alts = [degset(sorted(set(c))) for c in cands if set(c) != set(ds)]
    b.add(f"{fn} θ = {t} (0 ≤ θ < 2π) সমীকরণের সমাধান সেট কোনটি?", ok, setw(ok, alts), "রেফারেন্স কোণ নির্ণয় করে যে দুই চতুর্ভাগে চিহ্ন মেলে সেখানে।", M)
def m_count(b):
    fn = R.choice(['sin', 'cos']); t, v = R.choice(TARGETS[fn][:6]); k = R.choice([1, 2])
    hi = 360 * k
    n = sum(1 for d in range(0, hi) if (fn != 'tan' or d % 180 != 90) and abs(fval(fn, d) - v) < 1e-9)
    b.add(f"0 ≤ θ < {('2π' if k == 1 else '4π')} ব্যবধিতে {fn} θ = {t} সমীকরণের কয়টি সমাধান আছে?", n, setw(n, [n // 2, n + 1, n * 2, n - 1]), f"প্রতি 2π ব্যবধিতে 2টি সমাধান।", M)
def m_sq(b):
    fn = R.choice(['sin', 'cos']); t, v = R.choice([('1/4', .25), ('3/4', .75), ('1/2', .5)])
    ds = [d for d in CAND if d < 360 and abs(fval(fn, d) ** 2 - v) < 1e-9]
    ok = degset(ds)
    b.add(f"{fn}²θ = {t} (0 ≤ θ < 2π) হলে θ-এর মানসমূহ কোনটি?", ok, setw(ok, [degset(ds[:2]), degset(ds[::2]), degset([d for d in CAND if d < 360 and abs(fval(fn, d) - v) < 1e-9]) or degset([45, 135])]), "উভয় চিহ্নের মান নিয়ে চার চতুর্ভাগেই সমাধান।", M)
def m_lin(b):
    fn = R.choice(['sin', 'cos']); k = R.choice([2]); t, v = R.choice([('1', 1), ('−1', -1), ('√3', 3 ** .5), ('−√3', -(3 ** .5)), ('√2', 2 ** .5), ('0', 0)])
    ds = solve(fn, v / k, 0, 360, strict_hi=True)
    if not ds: return
    ok = degset(ds)
    b.add(f"2{fn} θ = {t} (0 ≤ θ < 2π) সমীকরণের সমাধান সেট কোনটি?", ok, setw(ok, [degset([(d + 180) % 360 for d in ds]), degset(ds[:1]), degset([(d + 30) % 360 for d in ds]), degset([(360 - d) % 360 for d in ds]) if {(360 - d) % 360 for d in ds} != set(ds) else degset([(d + 60) % 360 for d in ds])]), f"{fn} θ = {t}/2।", M)
def h_quad_eq(b):
    # 2sin²θ − 3sinθ + 1 = 0 ⇒ sinθ = 1, 1/2
    fn = R.choice(['sin', 'cos'])
    opts = [((1, .5), '2{f}²θ − 3{f}θ + 1 = 0'), ((-1, .5), '2{f}²θ + {f}θ − 1 = 0'), ((1, -.5), '2{f}²θ − {f}θ − 1 = 0'), ((-1, -.5), '2{f}²θ + 3{f}θ + 1 = 0')]
    (v1, v2), eq = R.choice(opts)
    ds = sorted(set(solve(fn, v1, 0, 360, True) + solve(fn, v2, 0, 360, True)))
    ok = degset(ds)
    alt = sorted(set(solve(fn, -v1, 0, 360, True) + solve(fn, -v2, 0, 360, True)))
    b.add(f"{eq.format(f=fn)} (0 ≤ θ < 2π) সমীকরণের সমাধান সেট কোনটি?", ok, setw(ok, [degset(alt), degset(solve(fn, v2, 0, 360, True)), degset(solve(fn, v1, 0, 360, True)), degset(ds[:-1]) if len(ds) > 2 else degset([0])]), f"{fn} θ = {num(F(v1).limit_denominator(2))} বা {num(F(v2).limit_denominator(2))}।", H)
def h_mixed(b):
    # sin²θ − cos²θ = cos θ ধরণের: 2cos²θ + cosθ − 1 = 0 ⇒ cosθ = 1/2, −1
    ds = sorted(set(solve('cos', .5, 0, 360, True) + solve('cos', -1, 0, 360, True)))
    ok = degset(ds)
    b.add("sin²θ − cos²θ = cos θ (0 ≤ θ < 2π) সমীকরণের সমাধান সেট কোনটি?", ok, [degset(solve('cos', .5, 0, 360, True)), degset([60, 180]), degset([0, 120, 240])], "1 − 2cos²θ = cos θ ⇒ (2cos θ − 1)(cos θ + 1) = 0।", H)
    ds2 = sorted(set(solve('sin', .5, 0, 360, True) + solve('sin', -1, 0, 360, True)))
    b.add("cos²θ − sin²θ = sin θ (0 ≤ θ < 2π) সমীকরণের সমাধান সেট কোনটি?", degset(ds2), [degset(solve('sin', .5, 0, 360, True)), degset([30, 270]), degset([90, 210, 330])], "1 − 2sin²θ = sin θ ⇒ (2sin θ − 1)(sin θ + 1) = 0।", H)
    ds3 = sorted(set(solve('tan', 1, 0, 360, True) + solve('tan', -1, 0, 360, True)))
    b.add("tan²θ = 1 (0 ≤ θ < 2π) সমীকরণের সমাধান সেট কোনটি?", degset(ds3), [degset(solve('tan', 1, 0, 360, True)), degset([45, 135]), degset([45, 315])], "tan θ = ±1।", H)
    ds4 = sorted(set(solve('tan', 3 ** .5, 0, 360, True) + solve('tan', -(3 ** .5), 0, 360, True)))
    b.add("tan²θ = 3 (0 ≤ θ < 2π) সমীকরণের সমাধান সেট কোনটি?", degset(ds4), [degset(solve('tan', 3 ** .5, 0, 360, True)), degset([60, 120]), degset([30, 150, 210, 330])], "tan θ = ±√3।", H)
def h_sec(b):
    t, v = R.choice([('2', .5), ('−2', -.5), ('√2', 2 ** -.5), ('−√2', -(2 ** -.5)), ('2/√3', 3 ** .5 / 2), ('−2/√3', -(3 ** .5) / 2)])
    ds = solve('cos', v, 0, 360, True)
    ok = degset(ds)
    b.add(f"sec θ = {t} (0 ≤ θ < 2π) সমীকরণের সমাধান সেট কোনটি?", ok, setw(ok, [degset(solve('sin', v, 0, 360, True)), degset([(d + 180) % 360 for d in ds]), degset(ds[:1]), degset([(d + 90) % 360 for d in ds])]), f"cos θ = 1/sec θ।", H)
def h_general(b):
    fn, t, v = R.choice([('sin', '1/2', 30), ('sin', '√3/2', 60), ('sin', '1/√2', 45), ('cos', '1/2', 60), ('cos', '√3/2', 30), ('cos', '1/√2', 45), ('tan', '1', 45), ('tan', '√3', 60), ('tan', '1/√3', 30)])
    a = rad(v)
    ok = {'sin': f"θ = nπ + (−1)ⁿ{a}", 'cos': f"θ = 2nπ ± {a}", 'tan': f"θ = nπ + {a}"}[fn]
    b.add(f"{fn} θ = {t} সমীকরণের সাধারণ সমাধান কোনটি? (n ∈ Z)", ok, setw(ok, [f"θ = nπ + (−1)ⁿ{a}", f"θ = 2nπ ± {a}", f"θ = nπ + {a}", f"θ = 2nπ + {a}"]), "সাধারণ সমাধানের সূত্র।", H)
p83 = run('8.3', R, fx83, [e_basic, e_deg], [m_full, m_count, m_sq, m_lin], [h_quad_eq, h_mixed, h_sec, h_general], caps=(12, 9, 8))
save('h8', p81 + p82 + p83)

# ---------------- 9.1 মূলদ সূচক ----------------
fx91 = [
 ("a^(m/n) = কত? (a > 0)", "ⁿ√(aᵐ)", ["ᵐ√(aⁿ)", "aᵐ/n", "aᵐ⁻ⁿ"], "মূলদ সূচকের সংজ্ঞা।", E),
 ("(aᵐ)ⁿ = কত?", "aᵐⁿ", ["aᵐ⁺ⁿ", "aᵐ⁻ⁿ", "(aⁿ)ᵐ⁺¹"], "সূচকের ঘাত নিয়ম।", E),
 ("(ab)ⁿ = কত?", "aⁿbⁿ", ["abⁿ", "aⁿb", "(a + b)ⁿ"], "গুণফলের ঘাত।", E),
 ("aᵐ ÷ aⁿ = কত? (a ≠ 0)", "aᵐ⁻ⁿ", ["aᵐ⁺ⁿ", "aᵐ/ⁿ", "aⁿ⁻ᵐ"], "ভাগের নিয়ম।", E),
 ("a^(1/n)-এর অর্থ কী?", "a-এর n-তম মূল", ["a-এর n গুণ", "a ÷ n", "aⁿ-এর অন্যোন্যক"], "ⁿ√a।", E),
]
POW = [(4, 2), (8, 3), (9, 2), (16, 2), (16, 4), (25, 2), (27, 3), (32, 5), (36, 2), (49, 2), (64, 2), (64, 3), (64, 6), (81, 2), (81, 4), (100, 2), (125, 3), (128, 7), (243, 5), (256, 4), (343, 3), (1000, 3)]
def e_frac(b):
    a, n = R.choice(POW); r = round(a ** (1 / n)); m = R.randint(1, 4)
    if math.gcd(m, n) > 1 and m > 1: return
    v = r ** m
    b.add(f"{a}^({m}/{n}) = কত?".replace('^(1/', '^(1/'), v, setw(v, [r, a * m // n if a * m % n == 0 else v + 1, v * r, r ** (m + 1)]), f"({a}^(1/{n})){sup(m)} = {r}{sup(m)} = {v}।", E)
def e_negfrac(b):
    a, n = R.choice(POW); r = round(a ** (1 / n))
    ok = f"1/{r}"
    b.add(f"{a}^(−1/{n}) = কত?", ok, setw(ok, [f"−{r}", str(r), f"1/{a}", f"−1/{r}"]), f"1/{a}^(1/{n}) = 1/{r}।", E)
def e_law(b):
    base = R.choice(['a', 'x', '2', '3', '5']); m, n = R.sample(range(-4, 8), 2)
    s = m + n
    ok = f"{base}{sup(s)}" if s not in (0, 1) else ('1' if s == 0 else base)
    b.add(f"{base}{sup(m)} × {base}{sup(n)} = কত?".replace(f'{base}¹ ', f'{base} ').replace(f'{base}⁰', '1'), ok, setw(ok, [f"{base}{sup(m * n)}" if m * n not in (0, 1) else f"{base}{sup(s + 2)}", f"{base}{sup(m - n)}" if m - n not in (0, 1) else f"{base}{sup(s + 3)}", f"{base}{sup(s + 1)}" if s + 1 not in (0, 1) else f"{base}{sup(s - 2)}"]), f"সূচক যোগ: {m} + ({n}) = {s}।", E)
def e_pow(b):
    base = R.choice(['a', 'x', 'y']); m, n = R.randint(2, 5), R.randint(2, 4)
    ok = f"{base}{sup(m * n)}"
    b.add(f"({base}{sup(m)}){sup(n)} = কত?", ok, setw(ok, [f"{base}{sup(m + n)}", f"{base}{sup(m ** n)}" if m ** n != m * n else f"{base}{sup(m * n + 1)}", f"{n}{base}{sup(m)}"]), f"{m} × {n} = {m * n}।", E)
def m_simplify(b):
    a, n = R.choice(POW); r = round(a ** (1 / n)); m = R.randint(2, 3)
    v = F(1, r ** m)
    b.add(f"({a})^(−{m}/{n}) = কত?", fr(v), setw(fr(v), [str(r ** m), fr(F(-1, r ** m)) if False else fr(F(1, r ** (m - 1))), fr(F(m, r * n)), fr(F(1, r ** m + 1))]), f"1/({r}{sup(m)}) = {fr(v)}।", M)
def m_eq(b):
    a, n = R.choice(POW); r = round(a ** (1 / n))
    # x^(1/n) = r ⇒ x = a
    b.add(f"x^(1/{n}) = {r} হলে x = কত?", a, setw(a, [r * n, r ** (n + 1), a + r, r]), f"x = {r}{sup(n)} = {a}।", M)
def m_expr(b):
    x = R.choice([2, 3, 4, 5]); m, n = R.randint(1, 4), R.randint(1, 4)
    # (x^(m) · x^(n)) / x^(m+n−1) = x
    num_ = f"{x}^({m}/2) × {x}^({n}/2)"
    v = F(m + n, 2)
    if v.denominator != 1: return
    val = x ** int(v)
    b.add(f"{num_} = কত?", val, setw(val, [x ** (m * n), x ** (m + n), val * x, val + x]), f"{x}^(({m} + {n})/2) = {x}{sup(int(v))} = {val}।", M)
def m_root(b):
    k = R.randint(2, 4); p = R.randint(2, 6)
    ok = f"x^({p}/{k})" if math.gcd(p, k) == 1 else f"x{sup(p // k)}" if p % k == 0 else f"x^({p // math.gcd(p, k)}/{k // math.gcd(p, k)})"
    b.add(f"{['', '', '', '∛', '∜'][k] if k > 2 else '√'}(x{sup(p)})-কে সূচক আকারে লিখলে কোনটি?", ok, setw(ok, [f"x^({k}/{p})", f"x{sup(p * k)}", f"x{sup(p + k)}", f"x{sup(p - k)}" if p - k > 1 else f"x^(1/{p * k})"]), f"ᵏ√(xᵖ) = x^(p/k)।", M)
def m_compare(b):
    pairs = [(2, 3, 3, 2), (2, 5, 5, 2), (3, 4, 4, 3)]
    a, m, c, n = R.choice(pairs)
    v1, v2 = a ** m, c ** n
    ok = f"{a}{sup(m)} {'>' if v1 > v2 else '<'} {c}{sup(n)}"
    b.add(f"{a}{sup(m)} ও {c}{sup(n)}-এর মধ্যে সম্পর্ক কোনটি?", ok, setw(ok, [f"{a}{sup(m)} {'<' if v1 > v2 else '>'} {c}{sup(n)}", f"{a}{sup(m)} = {c}{sup(n)}", "তুলনা করা যায় না"]), f"{v1} ও {v2}।", M)
def h_eq2(b):
    k = R.choice([3, 5]); r = R.randint(2, 4)
    # x^(2/k) = r² ⇒ x = r^k (ধনাত্মক)
    b.add(f"x^(2/{k}) = {r * r} এবং x > 0 হলে x = কত?", r ** k, setw(r ** k, [r ** (2 * k), r * k, (r * r) ** k, r ** (k + 1)]), f"x^(1/{k}) = {r} ⇒ x = {r}{sup(k)} = {r ** k}।", H)
def h_value(b):
    a = R.choice([2, 3, 5]); m = R.randint(1, 3)
    # (a^(x+1)·a^(x−1)) / a^(2x) = 1
    b.add(f"({a}^(x + {m}) × {a}^(x − {m})) ÷ {a}^(2x) = কত?", 1, setw(1, [a, a ** (2 * m), 0, 2 * a]), "সূচক: (x + m) + (x − m) − 2x = 0।", H)
def h_ratio(b):
    a = R.choice([2, 3]); m, n = R.randint(1, 4), R.randint(1, 4)
    v = F(a ** (m + 2) - a ** m, a ** (m + 1) - a ** (m - 1))
    b.add(f"({a}^(n + 2) − {a}ⁿ)/({a}^(n + 1) − {a}^(n − 1)) = কত?", fr(v), setw(fr(v), [fr(v * a), fr(v / a), '1', fr(v + 1)]), f"লব = {a}ⁿ({a * a} − 1), হর = {a}^(n − 1)({a * a} − 1) ⇒ {a}।", H)
def h_sqrt_nested(b):
    a = R.choice([2, 3, 5])
    # √(a√(a√a)) = a^(7/8)
    ok = f"{a}^(7/8)"
    b.add(f"√({a}√({a}√{a})) = কত?", ok, setw(ok, [f"{a}^(3/4)", f"{a}^(7/4)", f"{a}^(1/8)", f"{a}^(3/8)"]), f"ভিতর থেকে: {a}^(1/2), {a}^(3/4), {a}^(7/8)।", H)
p91 = run('9.1', R, fx91, [e_frac, e_negfrac, e_law, e_pow], [m_simplify, m_eq, m_expr, m_root, m_compare], [h_eq2, h_value, h_ratio, h_sqrt_nested])

# ---------------- 9.2 লগারিদম ও ফাংশন ----------------
fx92 = [
 ("aˣ = N হলে x = কত? (a > 0, a ≠ 1)", "logₐN", ["log_N a", "N/a", "aᴺ"], "লগারিদমের সংজ্ঞা।", E),
 ("y = aˣ (a > 0, a ≠ 1) সূচকীয় ফাংশনের রেঞ্জ কোনটি?", "(0, ∞)", ["R", "[0, ∞)", "(−∞, 0)"], "aˣ সবসময় ধনাত্মক।", E),
 ("y = logₐx ফাংশনের ডোমেন কোনটি?", "(0, ∞)", ["R", "[0, ∞)", "(1, ∞)"], "শুধু ধনাত্মক সংখ্যার লগারিদম সংজ্ঞায়িত।", E),
 ("y = aˣ (a > 1)-এর লেখচিত্র কোন বিন্দু দিয়ে যায়?", "(0, 1)", ["(1, 0)", "(0, 0)", "(1, 1)"], "a⁰ = 1।", E),
 ("y = logₐx-এর লেখচিত্র কোন বিন্দু দিয়ে যায়?", "(1, 0)", ["(0, 1)", "(0, 0)", "(a, 0)"], "logₐ1 = 0।", E),
 ("y = aˣ ও y = logₐx পরস্পরের কী?", "বিপরীত ফাংশন", ["সমান ফাংশন", "জোড় ফাংশন", "ধ্রুবক ফাংশন"], "একটি অপরটির বিপরীত।", M),
 ("প্রাকৃতিক লগারিদমের ভিত্তি কোনটি?", "e", ["10", "2", "π"], "ln x = logₑx।", E),
 ("logₐb × log_b a = কত?", "1", ["0", "ab", "a/b"], "ভিত্তি পরিবর্তন সূত্র।", M),
 ("0 < a < 1 হলে y = aˣ ফাংশনটি কেমন?", "ক্রমহ্রাসমান", ["ক্রমবর্ধমান", "ধ্রুবক", "পর্যাবৃত্ত"], "x বাড়লে aˣ কমে।", M),
]
def e_logval(b):
    base = R.choice([2, 3, 4, 5, 10]); n = R.randint(-3, 5); v = F(base) ** n
    b.add(f"log_{base} {fr(v)} = কত?", num(n), setw(num(n), [num(-n) if n else '1', num(n + 1), num(n - 1), fr(v)]), f"{base}{sup(n)} = {fr(v)}।", E)
def e_logrule(b):
    a, c = R.choice([(2, 50), (4, 25), (5, 20), (8, 125), (25, 4), (20, 50), (200, 5), (40, 25), (125, 8), (250, 4)])
    v = round(math.log10(a * c))
    b.add(f"log {a} + log {c} = কত? (ভিত্তি 10)", v, setw(v, [v + 1, v - 1, a + c, a * c]), f"log {a * c} = {v}।", E)
def e_dom(b):
    a = R.randint(-7, 9)
    ok = f"({num(a)}, ∞)"
    b.add(f"f(x) = log(x {'−' if a >= 0 else '+'} {abs(a)}) ফাংশনের ডোমেন কোনটি?".replace('log(x − 0)', 'log x'), ok, setw(ok, [f"[{num(a)}, ∞)", f"(−∞, {num(a)})", f"({num(-a)}, ∞)" if a else "(1, ∞)", "R"]), f"x {'−' if a >= 0 else '+'} {abs(a)} > 0।", E)
def e_ln(b):
    n = R.randint(-4, 6)
    b.add(f"ln(e{sup(n)}) = কত?", num(n), setw(num(n), [num(-n) if n else '1', 'e', num(n + 1), '0' if n else '2']), f"ln eⁿ = n।", E)
def m_diff(b):
    a, c = R.choice([(50, 5), (200, 2), (1000, 10), (80, 8), (300, 3), (5000, 5), (700, 7), (2000, 20)])
    v = round(math.log10(a / c))
    b.add(f"log {a} − log {c} = কত? (ভিত্তি 10)", v, setw(v, [v + 1, v - 1, a - c, a // c]), f"log({a}/{c}) = log {a // c} = {v}।", M)
def m_pow(b):
    base = R.choice([2, 3, 5]); n = R.randint(2, 5); k = R.randint(2, 4)
    v = n * k
    b.add(f"log_{base} ({base}{sup(n)}){sup(k)} = কত?", v, setw(v, [n + k, n ** k, v + 1, base * v]), f"{k} × {n} = {v}।", M)
def m_change(b):
    a, c = R.choice([(4, 8), (8, 4), (9, 27), (27, 9), (4, 32), (16, 8), (25, 125), (125, 25), (8, 16), (32, 8), (81, 27)])
    import math as m
    p = 2 if a in (4, 8, 16, 32) else (3 if a in (9, 27, 81) else 5)
    v = F(round(m.log(c, p)), round(m.log(a, p)))
    b.add(f"log_{a} {c} = কত?", fr(v), setw(fr(v), [fr(1 / v), fr(v + 1), fr(F(c, a)), str(c - a)]), f"log_{p} {c} / log_{p} {a} = {fr(v)}।", M)
def m_given(b):
    a, c = R.choice([(2, 3), (2, 5), (3, 5), (2, 7)])
    # log 2 = p, log 3 = q হলে log 12 = 2p + q ইত্যাদি
    m_, n = R.randint(0, 3), R.randint(0, 3)
    if m_ + n < 2 or (m_ == 0 or n == 0): return
    N = a ** m_ * c ** n
    ok = f"{m_ if m_ > 1 else ''}p + {n if n > 1 else ''}q"
    b.add(f"log {a} = p ও log {c} = q হলে log {N} = কত?", ok, setw(ok, [f"{n if n > 1 else ''}p + {m_ if m_ > 1 else ''}q", f"{m_ * n}pq", f"{m_ + n}(p + q)", f"{m_ if m_ > 1 else ''}p − {n if n > 1 else ''}q"]), f"{N} = {a}{sup(m_)} × {c}{sup(n)}।", M)
def m_inv(b):
    base = R.choice([2, 3, 5, 10]); a = R.randint(-3, 4)
    ok = f"{base}^(x {'−' if a >= 0 else '+'} {abs(a)})" if a else f"{base}ˣ"
    b.add(f"f(x) = log_{base} x {'+' if a >= 0 else '−'} {abs(a)} হলে f⁻¹(x) = কত?".replace(' + 0 হলে', ' হলে'), ok, setw(ok, [f"{base}^(x {'+' if a >= 0 else '−'} {abs(a)})" if a else f"{base}^(−x)", f"log_{base}(x − ({num(a)}))", f"x{sup(base)}", f"{base}ˣ {'−' if a >= 0 else '+'} {abs(a)}" if a else f"x/{base}"]), f"y = log_{base} x + ({num(a)}) ⇒ x = {base}^(y − ({num(a)}))।", M)
def h_dom2(b):
    a, c = sorted(R.sample(range(-6, 8), 2))
    ok = f"x < {num(a)} অথবা x > {num(c)}"
    fac = lambda v: 'x' if v == 0 else f"(x {'−' if v > 0 else '+'} {abs(v)})"
    b.add(f"f(x) = log({fac(a)}{fac(c)}) ফাংশনের ডোমেন কোনটি?", ok, setw(ok, [f"{num(a)} < x < {num(c)}", f"x ≤ {num(a)} অথবা x ≥ {num(c)}", f"x > {num(c)}", f"{num(a)} ≤ x ≤ {num(c)}"]), "গুণফল ধনাত্মক হতে হবে।", H)
def h_eq(b):
    base = R.choice([2, 3]); k = R.randint(1, 3)
    # log_b x + log_b (x − d) = k
    v = base ** k; cand = [(d, x) for x in range(2, 40) for d in range(1, 30) if x * (x - d) == v and x - d > 0]
    if not cand: return
    d, x = R.choice(cand)
    b.add(f"log_{base} x + log_{base}(x − {d}) = {k} হলে x = কত?", x, setw(x, [x - d, -(x - d) if x - d else x + 2, v, x + 1]), f"x(x − {d}) = {v} ⇒ x = {x}।", H)
def h_range(b):
    a = R.choice([2, 3, 5]); c = R.randint(-6, 6)
    ok = f"({num(c)}, ∞)"
    b.add(f"f(x) = {a}ˣ {'+' if c >= 0 else '−'} {abs(c)} ফাংশনের রেঞ্জ কোনটি?".replace(' + 0 ফাংশনের', ' ফাংশনের'), ok, setw(ok, [f"[{num(c)}, ∞)", "R", f"({num(c + 1)}, ∞)", f"(−∞, {num(c)})"]), f"{a}ˣ > 0 ⇒ f(x) > {num(c)}।", H)
def h_chain(b):
    a, c, d = R.choice([(2, 3, 4), (3, 4, 9), (2, 5, 8), (4, 5, 16), (3, 2, 27), (5, 2, 25)])
    # log_a c × log_c d = log_a d
    v = round(math.log(d, a))
    b.add(f"log_{a} {c} × log_{c} {d} = কত?", v, setw(v, [v + 1, c, d // a if d // a != v else v + 2, round(math.log(c, a) * 2)]), f"= log_{a} {d} = {v}।", H)
p92 = run('9.2', R, fx92, [e_logval, e_logrule, e_dom, e_ln], [m_diff, m_pow, m_change, m_given, m_inv], [h_dom2, h_eq, h_range, h_chain])
save('h9', p91 + p92)

# ---------------- 10.1 (1 + x)ⁿ ----------------
C = math.comb
fx101 = [
 ("(1 + x)ⁿ-এর বিস্তৃতিতে মোট কয়টি পদ থাকে?", "n + 1", ["n", "n − 1", "2n"], "পদসংখ্যা n + 1।", E),
 ("ⁿC₀ = কত?", "1", ["0", "n", "n!"], "শূন্য বস্তু বাছাইয়ের একটি উপায়।", E),
 ("ⁿCᵣ = কত?", "ⁿCₙ₋ᵣ", ["ⁿCᵣ₊₁", "ʳCₙ", "ⁿ⁺¹Cᵣ"], "সমপূরক বাছাই।", E),
 ("প্যাসকেলের ত্রিভুজে প্রতিটি সংখ্যা কীভাবে পাওয়া যায়?", "উপরের সারির পাশাপাশি দুটি সংখ্যার যোগফল", ["উপরের দুটি সংখ্যার গুণফল", "সারি নম্বরের বর্গ", "আগের সংখ্যার দ্বিগুণ"], "ⁿCᵣ + ⁿCᵣ₋₁ = ⁿ⁺¹Cᵣ।", E),
 ("(1 + x)ⁿ-এর বিস্তৃতিতে সহগগুলোর যোগফল কত?", "2ⁿ", ["n²", "n!", "2n"], "x = 1 বসিয়ে।", E),
]
def e_terms(b):
    n = R.randint(3, 20)
    b.add(f"(1 + x){sup(n)}-এর বিস্তৃতিতে পদসংখ্যা কত?", n + 1, setw(n + 1, [n, n + 2, 2 * n, n - 1]), f"n + 1 = {n + 1}।", E)
def e_ncr(b):
    n = R.randint(4, 12); r = R.randint(2, n - 2)
    v = C(n, r)
    b.add(f"{n}C{r} = কত?".replace('C', 'C'), v, setw(v, [C(n, r - 1), C(n, r + 1) if C(n, r + 1) != v else v + n, n * r, v + 1]), f"{n}!/({r}!·{n - r}!) = {v}।", E)
def e_coef(b):
    n = R.randint(4, 10); r = R.randint(1, n - 1)
    v = C(n, r)
    b.add(f"(1 + x){sup(n)}-এর বিস্তৃতিতে x{sup(r)}-এর সহগ কত?".replace('x¹', 'x'), v, setw(v, [C(n, r - 1) if C(n, r - 1) != v else v + 2, n * r, C(n + 1, r), v + 1]), f"{n}C{r} = {v}।", E)
def e_sum(b):
    n = R.randint(3, 12)
    b.add(f"(1 + x){sup(n)}-এর বিস্তৃতিতে সহগগুলোর যোগফল কত?", 2 ** n, setw(2 ** n, [n * n, 2 * n, 2 ** (n - 1), 2 ** n + 1]), f"x = 1 বসিয়ে 2{sup(n)} = {2 ** n}।", E)
def m_coef_k(b):
    n = R.randint(3, 8); r = R.randint(1, min(n, 4)); k = R.choice([2, 3, -2, -1, 4])
    v = C(n, r) * k ** r
    ks = f"{k}x" if k > 0 else f"−{abs(k)}x".replace('−1x', '−x')
    b.add(f"(1 {'+' if k > 0 else '−'} {abs(k) if abs(k) > 1 else ''}x){sup(n)}-এর বিস্তৃতিতে x{sup(r)}-এর সহগ কত?".replace('x¹', 'x'), num(v), setw(num(v), [num(C(n, r)), num(-v), num(C(n, r) * k), num(v + C(n, r))]), f"{n}C{r} × ({num(k)}){sup(r)} = {num(v)}।", M)
def m_middle(b):
    n = 2 * R.randint(2, 6)
    v = C(n, n // 2)
    b.add(f"(1 + x){sup(n)}-এর বিস্তৃতিতে মধ্যপদের সহগ কত?", v, setw(v, [C(n, n // 2 - 1), 2 ** (n // 2), n * n // 4, v + 1]), f"মধ্যপদ {n // 2 + 1}-তম; সহগ {n}C{n // 2} = {v}।", M)
def m_pascal(b):
    n = R.randint(4, 8)
    row = ', '.join(str(C(n, r)) for r in range(n + 1))
    wrong = ', '.join(str(C(n - 1, r)) for r in range(n)); w2 = ', '.join(str(C(n + 1, r)) for r in range(n + 2))
    w3 = ', '.join(str(C(n, r) + (1 if 0 < r < n else 0)) for r in range(n + 1))
    b.add(f"প্যাসকেলের ত্রিভুজের কোন সারিটি (1 + x){sup(n)}-এর সহগ নির্দেশ করে?", row, [wrong, w2, w3], f"{n}C0, {n}C1, …, {n}C{n}।", M)
def m_nfind(b):
    n = R.randint(4, 15); r = R.randint(2, 3)
    v = C(n, r)
    b.add(f"nC{r} = {v} হলে n = কত?", n, setw(n, [n + 1, n - 1, v // r if v // r != n else n + 2, r + n]), f"{n}C{r} = {v}।", M)
def m_value(b):
    n = R.randint(2, 5)
    # (1.1)^n এর মান? সহজ: (1 + 0.1)^n প্রথম তিন পদ
    approx = F(1) + F(n, 10) + F(C(n, 2), 100)
    s = f"{float(approx):.2f}"
    b.add(f"(1.1){sup(n)}-এর বিস্তৃতির প্রথম তিনটি পদ নিয়ে আসন্ন মান কত?", s, setw(s, [f"{float(approx + F(1, 10)):.2f}", f"{1 + n / 10:.2f}", f"{float(approx - F(C(n, 2), 200)):.3f}", f"{float(approx + F(1, 100)):.2f}"]), f"1 + {n}(0.1) + {C(n, 2)}(0.01) = {s}।", M)
def h_ratio(b):
    n = R.randint(5, 12); r = R.randint(1, n - 2)
    v = F(C(n, r + 1), C(n, r))
    b.add(f"(1 + x){sup(n)}-এর বিস্তৃতিতে x{sup(r + 1)} ও x{sup(r)}-এর সহগের অনুপাত কত?".replace('x¹', 'x'), fr(v), setw(fr(v), [fr(1 / v), fr(F(n - r, r)), fr(F(r + 1, n)), fr(v + 1)]), f"{n}C{r + 1}/{n}C{r} = ({n} − {r})/({r} + 1) = {fr(v)}।", H)
def h_equal(b):
    n = R.randint(6, 20); r = R.randint(1, n // 2 - 1)
    # nC r = nC s, s ≠ r ⇒ s = n − r
    b.add(f"(1 + x){sup(n)}-এর বিস্তৃতিতে x{sup(r)} ও xᵏ-এর সহগ সমান (k ≠ {r}) হলে k = কত?".replace('x¹', 'x'), n - r, setw(n - r, [n - r + 1, n - r - 1, r + 1, n]), f"{n}C{r} = {n}C{n - r}।", H)
def h_sum_even(b):
    n = R.randint(3, 12)
    b.add(f"(1 + x){sup(n)}-এর বিস্তৃতিতে জোড় স্থানীয় পদগুলোর সহগের যোগফল কত?", 2 ** (n - 1), setw(2 ** (n - 1), [2 ** n, 2 ** (n - 2), n, 2 ** (n - 1) + 1]), f"বিজোড় ও জোড় স্থানের সহগের যোগফল সমান = 2{sup(n - 1)}।", H)
def h_find_n(b):
    n = R.randint(4, 12)
    b.add(f"(1 + x)ⁿ-এর বিস্তৃতিতে সহগগুলোর যোগফল {2 ** n} হলে n = কত?", n, setw(n, [n + 1, n - 1, 2 * n, 2 ** n // 2]), f"2ⁿ = {2 ** n}।", H)
p101 = run('10.1', R, fx101, [e_terms, e_ncr, e_coef, e_sum], [m_coef_k, m_middle, m_pascal, m_nfind, m_value], [h_ratio, h_equal, h_sum_even, h_find_n])

# ---------------- 10.2 (x + y)ⁿ ও সাধারণ পদ ----------------
fx102 = [
 ("(a + b)ⁿ-এর বিস্তৃতিতে (r + 1)-তম পদ কোনটি?", "ⁿCᵣ aⁿ⁻ʳ bʳ", ["ⁿCᵣ₊₁ aⁿ⁻ʳ bʳ", "ⁿCᵣ aʳ bⁿ⁻ʳ⁺¹", "ⁿCᵣ₋₁ aⁿ bʳ"], "সাধারণ পদ Tᵣ₊₁।", E),
 ("(a + b)ⁿ-এ n জোড় হলে মধ্যপদ কোনটি?", "(n/2 + 1)-তম পদ", ["(n/2)-তম পদ", "(n + 1)-তম পদ", "দুটি মধ্যপদ"], "পদসংখ্যা বিজোড়।", M),
 ("(a + b)ⁿ-এ n বিজোড় হলে মধ্যপদ কয়টি?", "2টি", ["1টি", "3টি", "কোনোটি নয়"], "পদসংখ্যা জোড়।", M),
 ("(a − b)ⁿ-এর বিস্তৃতিতে পদগুলোর চিহ্ন কেমন?", "পর্যায়ক্রমে + ও −", ["সব ধনাত্মক", "সব ঋণাত্মক", "প্রথম অর্ধেক ঋণাত্মক"], "(−b)ʳ-এর জন্য।", E),
]
def e_gen(b):
    n = R.randint(4, 9); a = R.choice([1, 2, 3]); c = R.choice([1, 2, 3]); r = R.randint(1, n - 1)
    v = C(n, r) * a ** (n - r) * c ** r
    b.add(f"({a if a > 1 else ''}x + {c if c > 1 else ''}y){sup(n)}-এর বিস্তৃতিতে x{sup(n - r)}y{sup(r)}-এর সহগ কত?".replace('x¹', 'x').replace('y¹', 'y'), v, setw(v, [C(n, r), C(n, r) * a ** r * c ** (n - r) if a != c else v + C(n, r), v * 2, C(n, r - 1) * a ** (n - r) * c ** r]), f"{n}C{r}·{a}{sup(n - r)}·{c}{sup(r)} = {v}।", E)
def e_term(b):
    n = R.randint(4, 8); r = R.randint(1, n)
    v = C(n, r - 1)
    b.add(f"(x + y){sup(n)}-এর বিস্তৃতিতে {r}-তম পদের সহগ কত?", v, setw(v, [C(n, r) if C(n, r) != v else v + 1, n * r, C(n + 1, r), v + 2]), f"T{r} = {n}C{r - 1} … ⇒ সহগ {v}।", E)
def e_first(b):
    n = R.randint(3, 8); a = R.randint(2, 4)
    ok = f"{a ** n}x{sup(n)}"
    b.add(f"({a}x + y){sup(n)}-এর বিস্তৃতির প্রথম পদ কোনটি?", ok, setw(ok, [f"{a}x{sup(n)}", f"{a * n}x{sup(n)}", f"{a ** n}x{sup(n - 1)}", f"{a ** (n - 1)}x{sup(n)}"]), f"({a}x){sup(n)} = {ok}।", E)
def m_indep(b):
    n = 2 * R.randint(2, 5); k = R.choice([1, 2, 3])
    # (x + k/x)^n: x-মুক্ত পদ r = n/2 ⇒ C(n, n/2) k^(n/2)
    v = C(n, n // 2) * k ** (n // 2)
    b.add(f"(x + {k if k > 1 else 1}/x){sup(n)}-এর বিস্তৃতিতে x-বর্জিত পদ কত?", v, setw(v, [C(n, n // 2), v * k, C(n, n // 2 - 1) * k ** (n // 2), v + 1]), f"n − 2r = 0 ⇒ r = {n // 2}; {n}C{n // 2}·{k}{sup(n // 2)} = {v}।", M)
def m_indep2(b):
    n = 3 * R.randint(1, 4); k = R.choice([1, 2, -1])
    # (x² + k/x)^n: 2(n − r) − r = 0 ⇒ r = 2n/3
    r = 2 * n // 3; v = C(n, r) * k ** r
    b.add(f"(x² {'+' if k > 0 else '−'} {abs(k) if abs(k) > 1 else 1}/x){sup(n)}-এর বিস্তৃতিতে x-বর্জিত পদ কত?", num(v), setw(num(v), [num(C(n, r)), num(-v) if v else '1', num(C(n, n // 3) * k ** (n // 3)) if C(n, n // 3) * k ** (n // 3) != v else num(v + 3), num(v + n)]), f"2({n} − r) − r = 0 ⇒ r = {r}।", M)
def m_neg(b):
    n = R.randint(4, 8); r = R.randint(1, n - 1); c = R.choice([1, 2, 3])
    v = C(n, r) * (-c) ** r
    b.add(f"(x − {c if c > 1 else ''}y){sup(n)}-এর বিস্তৃতিতে x{sup(n - r)}y{sup(r)}-এর সহগ কত?".replace('x¹', 'x').replace('y¹', 'y'), num(v), setw(num(v), [num(-v), num(C(n, r)), num(C(n, r) * c), num(v + 1)]), f"{n}C{r}(−{c}){sup(r)} = {num(v)}।", M)
def m_middle(b):
    n = 2 * R.randint(2, 4); a, c = R.choice([(1, 2), (2, 1), (1, 3), (2, 3), (3, 1)])
    r = n // 2; v = C(n, r) * a ** (n - r) * c ** r
    b.add(f"({a if a > 1 else ''}x + {c if c > 1 else ''}y){sup(n)}-এর বিস্তৃতিতে মধ্যপদের সহগ কত?", v, setw(v, [C(n, r), C(n, r - 1) * a ** (n - r + 1) * c ** (r - 1), v * 2, v + C(n, r)]), f"{r + 1}-তম পদ: {n}C{r}·{a}{sup(n - r)}·{c}{sup(r)} = {v}।", M)
def m_sumcoef(b):
    n = R.randint(2, 7); a, c = R.choice([(2, 1), (1, 2), (3, 1), (2, -1), (3, -2), (1, -2)])
    v = (a + c) ** n
    b.add(f"({a if a > 1 else ''}x {'+' if c > 0 else '−'} {abs(c) if abs(c) > 1 else ''}y){sup(n)}-এর বিস্তৃতিতে সহগগুলোর যোগফল কত?", num(v), setw(num(v), [num(2 ** n), num(a ** n + c ** n), num((a - c) ** n), num(v + 1)]), f"x = y = 1 বসিয়ে ({num(a + c)}){sup(n)} = {num(v)}।", M)
def h_xpow(b):
    n = R.randint(5, 9); k = R.choice([1, 2])
    # (x + k/x)^n-এ x^p-এর সহগ, p = n − 2r
    r = R.randint(0, n); p = n - 2 * r
    if p == 0: return
    v = C(n, r) * k ** r
    b.add(f"(x + {k}/x){sup(n)}-এর বিস্তৃতিতে x{sup(p)}-এর সহগ কত?".replace('x¹', 'x'), v, setw(v, [C(n, r), C(n, r + 1) * k ** (r + 1) if r < n else v + 3, v * 2, C(n, r) * k ** (n - r) if k ** (n - r) != k ** r else v + 1]), f"{n} − 2r = {p} ⇒ r = {r}; {n}C{r}·{k}{sup(r)} = {v}।", H)
def h_n_from_terms(b):
    n = R.randint(5, 12); r = R.randint(2, 3)
    # (1 + x)^n-এ 2য় ও 3য় পদের সহগের অনুপাত
    v = F(C(n, 2), C(n, 1))
    b.add(f"(1 + x)ⁿ-এর বিস্তৃতিতে তৃতীয় ও দ্বিতীয় পদের সহগের অনুপাত {fr(v)} হলে n = কত?", n, setw(n, [n + 1, n - 1, 2 * n, int(v) + 1 if int(v) + 1 != n else n + 2]), f"ⁿC₂/ⁿC₁ = (n − 1)/2 = {fr(v)}।", H)
def h_greatest(b):
    n = R.randint(4, 10)
    v = max(C(n, r) for r in range(n + 1))
    b.add(f"(1 + x){sup(n)}-এর বিস্তৃতিতে বৃহত্তম সহগ কত?", v, setw(v, [2 ** n, C(n, n // 2 - 1), n * n, v + 1]), f"মধ্যপদ(গুলো)-এর সহগ {n}C{n // 2} = {v}।", H)
def h_value(b):
    a, c = R.choice([(1, 1), (2, 1), (1, 2)]); n = R.randint(3, 5)
    # (√2 + 1)^n + (√2 − 1)^n ধরনের? সরল: (x + 1)^n − (x − 1)^n এ x³-এর সহগ
    p = R.randint(0, n - 1)
    if (n - p) % 2 == 0: return
    v = 2 * C(n, p)
    b.add(f"(x + 1){sup(n)} − (x − 1){sup(n)}-এর বিস্তৃতিতে x{sup(p)}-এর সহগ কত?".replace('x¹', 'x').replace('x⁰', 'ধ্রুবক পদ'), v, setw(v, [C(n, p), 0, 2 ** n, v + 2]), f"বিজোড় ঘাতের (1-এর) পদগুলো দ্বিগুণ হয় ⇒ 2·{n}C{p} = {v}।", H)
p102 = run('10.2', R, fx102, [e_gen, e_term, e_first], [m_indep, m_indep2, m_neg, m_middle, m_sumcoef], [h_xpow, h_n_from_terms, h_greatest, h_value])
save('h10', p101 + p102)

# ---------------- 11 স্থানাঙ্ক জ্যামিতি ----------------
def P(x, y): return f"({num(x)}, {num(y)})"
def dist2(a, b): return (a[0] - b[0]) ** 2 + (a[1] - b[1]) ** 2
def rpt(lo=-6, hi=8): return (R.randint(lo, hi), R.randint(lo, hi))
def sqf(v):
    r = math.isqrt(v)
    return str(r) if r * r == v else surd(v)
fx111 = [
 ("(x₁, y₁) ও (x₂, y₂) বিন্দুদ্বয়ের দূরত্ব কত?", "√((x₂ − x₁)² + (y₂ − y₁)²)", ["(x₂ − x₁) + (y₂ − y₁)", "√((x₂ + x₁)² + (y₂ + y₁)²)", "(x₂ − x₁)² + (y₂ − y₁)²"], "দূরত্বের সূত্র।", E),
 ("মূলবিন্দু থেকে (x, y) বিন্দুর দূরত্ব কত?", "√(x² + y²)", ["x + y", "x² + y²", "√(x + y)"], "(0, 0) থেকে দূরত্ব।", E),
 ("x-অক্ষের উপর যেকোনো বিন্দুর কোটি কত?", "0", ["1", "x", "অসংজ্ঞায়িত"], "x-অক্ষে y = 0।", E),
 ("(x₁, y₁) ও (x₂, y₂)-এর সংযোগ রেখাংশের মধ্যবিন্দু কোনটি?", "((x₁ + x₂)/2, (y₁ + y₂)/2)", ["((x₁ − x₂)/2, (y₁ − y₂)/2)", "(x₁ + x₂, y₁ + y₂)", "((x₁ + y₁)/2, (x₂ + y₂)/2)"], "মধ্যবিন্দুর সূত্র।", E),
]
def e_dist(b):
    a = rpt(); dx, dy = R.choice([(3, 4), (4, 3), (5, 12), (12, 5), (6, 8), (8, 6), (0, 5), (7, 0), (8, 15), (1, 1), (2, 3), (1, 2)])
    sx, sy = R.choice([1, -1]), R.choice([1, -1]); c = (a[0] + sx * dx, a[1] + sy * dy)
    ok = sqf(dx * dx + dy * dy)
    b.add(f"{P(*a)} ও {P(*c)} বিন্দুদ্বয়ের মধ্যবর্তী দূরত্ব কত একক?", ok, setw(ok, [str(dx + dy), str(dx * dx + dy * dy), sqf(dx * dx + dy * dy + 2), sqf((dx + 1) ** 2 + dy * dy)]), f"√({dx}² + {dy}²) = {ok}।", E)
def e_origin(b):
    x, y = R.choice([(3, 4), (5, 12), (6, 8), (8, 15), (1, 1), (2, 2), (1, 3), (7, 24), (2, 5)])
    x, y = x * R.choice([1, -1]), y * R.choice([1, -1])
    ok = sqf(x * x + y * y)
    b.add(f"মূলবিন্দু থেকে {P(x, y)} বিন্দুর দূরত্ব কত?", ok, setw(ok, [str(abs(x) + abs(y)), str(x * x + y * y), sqf(x * x + y * y + 1), sqf(abs(x * x - y * y)) if x * x != y * y else '0']), f"√({x * x} + {y * y}) = {ok}।", E)
def e_mid(b):
    a, c = rpt(), rpt()
    if (a[0] + c[0]) % 2 or (a[1] + c[1]) % 2 or a == c: return
    m = ((a[0] + c[0]) // 2, (a[1] + c[1]) // 2)
    ok = P(*m)
    b.add(f"{P(*a)} ও {P(*c)} বিন্দুদ্বয়ের সংযোগ রেখাংশের মধ্যবিন্দু কোনটি?", ok, setw(ok, [P(a[0] + c[0], a[1] + c[1]), P((c[0] - a[0]) // 2, (c[1] - a[1]) // 2), P(m[1], m[0]), P(m[0] + 1, m[1])]), "মধ্যবিন্দুর সূত্র।", E)
def m_unknown(b):
    a = rpt(); dx, dy = R.choice([(3, 4), (4, 3), (5, 12), (12, 5), (6, 8), (8, 6), (8, 15)])
    k = a[1] + dy
    x2 = a[0] + dx
    # (x2, k) বিন্দু: (a) থেকে দূরত্ব d; k অজানা ⇒ k = a1 ± dy
    d = math.isqrt(dx * dx + dy * dy)
    ok = f"{num(a[1] + dy)} বা {num(a[1] - dy)}"
    b.add(f"{P(*a)} ও ({num(x2)}, k) বিন্দুদ্বয়ের দূরত্ব {d} একক হলে k = কত?", ok, setw(ok, [f"{num(a[1] + dy)}", f"{num(dy)} বা {num(-dy)}", f"{num(a[1] + dx)} বা {num(a[1] - dx)}", f"{num(a[1] + d)} বা {num(a[1] - d)}"]), f"({dx})² + (k − {num(a[1])})² = {d * d} ⇒ k − {num(a[1])} = ±{dy}।", M)
def m_type(b):
    kind = R.choice(['eq', 'iso', 'right', 'sc'])
    if kind == 'right':
        o = rpt(); dx, dy = R.randint(1, 6), R.randint(1, 6)
        A, B, Cc = o, (o[0] + dx, o[1]), (o[0], o[1] + dy)
    elif kind == 'iso':
        o = rpt(); dx, h = R.randint(1, 5), R.randint(1, 6)
        A, B, Cc = (o[0] - dx, o[1]), (o[0] + dx, o[1]), (o[0], o[1] + h)
        if h * h + dx * dx == 4 * dx * dx or h == dx: return
    elif kind == 'sc':
        A, B, Cc = rpt(), rpt(), rpt()
        ds = sorted([dist2(A, B), dist2(B, Cc), dist2(Cc, A)])
        if len(set(ds)) < 3 or ds[0] + ds[1] == ds[2] or ds[0] == 0: return
        if (B[0] - A[0]) * (Cc[1] - A[1]) - (B[1] - A[1]) * (Cc[0] - A[0]) == 0: return
    else:
        return
    ds = sorted([dist2(A, B), dist2(B, Cc), dist2(Cc, A)])
    ok = 'সমকোণী' if ds[0] + ds[1] == ds[2] else ('সমদ্বিবাহু' if len(set(ds)) < 3 else 'বিষমবাহু')
    if ok == 'সমকোণী' and len(set(ds)) < 3: ok = 'সমকোণী সমদ্বিবাহু'
    b.add(f"{P(*A)}, {P(*B)}, {P(*Cc)} শীর্ষবিশিষ্ট ত্রিভুজটি কোন ধরনের?", ok, setw(ok, ['সমবাহু', 'সমদ্বিবাহু', 'সমকোণী', 'বিষমবাহু', 'সমকোণী সমদ্বিবাহু']), f"বাহুর বর্গ: {', '.join(str(d) for d in ds)}।", M)
def m_equid(b):
    a, c = rpt(), rpt()
    if a[1] == c[1]: return
    # x-অক্ষের উপর (x, 0) যা a ও c থেকে সমদূরবর্তী: (x − a0)² + a1² = (x − c0)² + c1²
    num_ = c[0] ** 2 + c[1] ** 2 - a[0] ** 2 - a[1] ** 2; den = 2 * (c[0] - a[0])
    if den == 0 or num_ % den: return
    x = num_ // den
    ok = P(x, 0)
    b.add(f"x-অক্ষের উপর অবস্থিত যে বিন্দুটি {P(*a)} ও {P(*c)} থেকে সমদূরবর্তী, সেটি কোনটি?", ok, setw(ok, [P(0, x), P(-x, 0) if x else P(1, 0), P(x + 1, 0), P((a[0] + c[0]) / 2 if (a[0] + c[0]) % 2 == 0 else x + 2, 0)]), f"(x − {num(a[0])})² + {a[1] * a[1]} = (x − {num(c[0])})² + {c[1] * c[1]} ⇒ x = {num(x)}।", M)
def m_section(b):
    a, c = rpt(), rpt(); m, n = R.choice([(1, 2), (2, 1), (1, 3), (3, 1), (2, 3), (3, 2)])
    px, py = F(m * c[0] + n * a[0], m + n), F(m * c[1] + n * a[1], m + n)
    if px.denominator > 1 or py.denominator > 1 or a == c: return
    ok = P(px, py)
    qx, qy = F(n * c[0] + m * a[0], m + n), F(n * c[1] + m * a[1], m + n)
    b.add(f"{P(*a)} ও {P(*c)} বিন্দুদ্বয়ের সংযোগ রেখাংশকে {m} : {n} অনুপাতে অন্তর্বিভক্তকারী বিন্দু কোনটি?", ok, setw(ok, [P(qx, qy), P(F(a[0] + c[0], 2), F(a[1] + c[1], 2)), P(px + 1, py), P(py, px)]), "((mx₂ + nx₁)/(m + n), (my₂ + ny₁)/(m + n))।", M)
def m_perim(b):
    o = rpt(); a, c = R.randint(1, 8), R.randint(1, 8)
    pts = [o, (o[0] + a, o[1]), (o[0] + a, o[1] + c), (o[0], o[1] + c)]
    v = 2 * (a + c)
    b.add(f"{', '.join(P(*p) for p in pts)} শীর্ষবিশিষ্ট আয়তক্ষেত্রের পরিসীমা কত?", v, setw(v, [a * c, a + c, v + 2, 2 * a * c]), f"দৈর্ঘ্য {a}, প্রস্থ {c} ⇒ {v}।", M)
def h_circ(b):
    c = rpt(); dx, dy = R.choice([(3, 4), (5, 12), (6, 8), (8, 6), (0, 5), (4, 3)])
    p = (c[0] + dx, c[1] + dy); r = math.isqrt(dx * dx + dy * dy); q = (c[0] - dx, c[1] - dy)
    ok = P(*q)
    b.add(f"একটি বৃত্তের কেন্দ্র {P(*c)} এবং একটি ব্যাসের এক প্রান্ত {P(*p)} হলে অপর প্রান্ত কোনটি?", ok, setw(ok, [P(c[0] + dy, c[1] + dx), P(p[0] - c[0], p[1] - c[1]), P(2 * p[0] - c[0], 2 * p[1] - c[1]), P(-p[0], -p[1])]), "কেন্দ্র ব্যাসের মধ্যবিন্দু।", H)
def h_fourth(b):
    A, B, Cc = rpt(), rpt(), rpt()
    if (B[0] - A[0]) * (Cc[1] - A[1]) - (B[1] - A[1]) * (Cc[0] - A[0]) == 0: return
    D = (A[0] + Cc[0] - B[0], A[1] + Cc[1] - B[1])
    ok = P(*D)
    b.add(f"ABCD সামান্তরিকের A{P(*A)}, B{P(*B)}, C{P(*Cc)} হলে D-এর স্থানাঙ্ক কোনটি?", ok, setw(ok, [P(A[0] + B[0] - Cc[0], A[1] + B[1] - Cc[1]), P(B[0] + Cc[0] - A[0], B[1] + Cc[1] - A[1]), P(D[0] + 1, D[1]), P(D[1], D[0])]), "কর্ণদ্বয়ের মধ্যবিন্দু একই: A + C = B + D।", H)
def h_centroid(b):
    A, B, Cc = rpt(), rpt(), rpt()
    sx, sy = A[0] + B[0] + Cc[0], A[1] + B[1] + Cc[1]
    if sx % 3 or sy % 3: return
    ok = P(sx // 3, sy // 3)
    b.add(f"{P(*A)}, {P(*B)}, {P(*Cc)} শীর্ষবিশিষ্ট ত্রিভুজের ভরকেন্দ্র কোনটি?", ok, setw(ok, [P(sx, sy), P(F(sx, 2), F(sy, 2)), P(sy // 3, sx // 3), P(sx // 3 + 1, sy // 3)]), "((x₁ + x₂ + x₃)/3, (y₁ + y₂ + y₃)/3)।", H)
def h_circum(b):
    o = rpt(-3, 4); a, c = R.randint(1, 6), R.randint(1, 6)
    A, B, Cc = o, (o[0] + 2 * a, o[1]), (o[0], o[1] + 2 * c)
    ok = P(o[0] + a, o[1] + c)
    b.add(f"{P(*A)}, {P(*B)}, {P(*Cc)} শীর্ষবিশিষ্ট সমকোণী ত্রিভুজের পরিকেন্দ্র কোনটি?", ok, setw(ok, [P(*A), P(F(3 * o[0] + 2 * a, 3), F(3 * o[1] + 2 * c, 3)), P(o[0] + 2 * a, o[1] + 2 * c), P(o[0] + c, o[1] + a) if a != c else P(o[0] + a + 1, o[1] + c)]), "অতিভুজের মধ্যবিন্দু পরিকেন্দ্র।", H)
p111 = run('11.1', R, fx111, [e_dist, e_origin, e_mid], [m_unknown, m_type, m_equid, m_section, m_perim], [h_circ, h_fourth, h_centroid, h_circum])

fx112 = [
 ("তিনটি বিন্দু সমরেখ হলে তাদের দ্বারা গঠিত ত্রিভুজের ক্ষেত্রফল কত?", "0", ["1", "অসীম", "ঋণাত্মক"], "সমরেখ বিন্দু ত্রিভুজ গঠন করে না।", E),
 ("(x₁, y₁), (x₂, y₂), (x₃, y₃) শীর্ষবিশিষ্ট ত্রিভুজের ক্ষেত্রফল কোনটি?", "½|x₁(y₂ − y₃) + x₂(y₃ − y₁) + x₃(y₁ − y₂)|", ["|x₁y₁ + x₂y₂ + x₃y₃|", "½(x₁ + x₂ + x₃)(y₁ + y₂ + y₃)", "x₁(y₂ − y₃) + x₂(y₃ − y₁)"], "স্থানাঙ্কের সাহায্যে ক্ষেত্রফল।", E),
 ("শীর্ষবিন্দুগুলো ঘড়ির কাঁটার বিপরীত দিকে নিলে নির্ণায়ক পদ্ধতিতে পাওয়া ক্ষেত্রফল কেমন হয়?", "ধনাত্মক", ["ঋণাত্মক", "শূন্য", "অসংজ্ঞায়িত"], "ঘড়ির কাঁটার দিকে নিলে ঋণাত্মক আসে।", M),
]
def tarea(A, B, Cc): return F(abs(A[0] * (B[1] - Cc[1]) + B[0] * (Cc[1] - A[1]) + Cc[0] * (A[1] - B[1])), 2)
def e_area(b):
    A, B, Cc = rpt(-5, 6), rpt(-5, 6), rpt(-5, 6); v = tarea(A, B, Cc)
    if v == 0: return
    b.add(f"{P(*A)}, {P(*B)}, {P(*Cc)} শীর্ষবিশিষ্ট ত্রিভুজের ক্ষেত্রফল কত বর্গ একক?", fr(v), setw(fr(v), [fr(v * 2), fr(v / 2), fr(v + 1), fr(v + F(1, 2))]), f"½|…| = {fr(v)}।", E)
def e_axis(b):
    a, c = R.randint(1, 12), R.randint(1, 12)
    v = F(a * c, 2)
    b.add(f"(0, 0), ({a}, 0), (0, {c}) শীর্ষবিশিষ্ট ত্রিভুজের ক্ষেত্রফল কত বর্গ একক?", fr(v), setw(fr(v), [str(a * c), fr(v + 1), str(a + c), fr(F(a + c, 2))]), f"½ × {a} × {c} = {fr(v)}।", E)
def e_col(b):
    A = rpt(); d = (R.randint(-3, 3), R.randint(-3, 3))
    if d == (0, 0): return
    k1, k2 = R.sample([1, 2, 3, -1, -2], 2)
    B, Cc = (A[0] + k1 * d[0], A[1] + k1 * d[1]), (A[0] + k2 * d[0], A[1] + k2 * d[1])
    b.add(f"{P(*A)}, {P(*B)}, {P(*Cc)} বিন্দু তিনটি কেমন?", "সমরেখ", ["সমকোণী ত্রিভুজের শীর্ষ", "সমবাহু ত্রিভুজের শীর্ষ", "সমদ্বিবাহু ত্রিভুজের শীর্ষ"], "ক্ষেত্রফল শূন্য।", E)
def m_quad(b):
    pts = [rpt(-5, 6) for _ in range(4)]
    # উত্তল চতুর্ভুজ ক্রমে: ঘড়ির কাঁটার বিপরীত ক্রমে সাজাই
    cx, cy = sum(p[0] for p in pts) / 4, sum(p[1] for p in pts) / 4
    pts.sort(key=lambda p: math.atan2(p[1] - cy, p[0] - cx))
    if len(set(pts)) < 4: return
    s = sum(pts[i][0] * pts[(i + 1) % 4][1] - pts[(i + 1) % 4][0] * pts[i][1] for i in range(4))
    v = F(abs(s), 2)
    # উত্তলতা যাচাই
    def cr(o, a, c): return (a[0] - o[0]) * (c[1] - o[1]) - (a[1] - o[1]) * (c[0] - o[0])
    if not all(cr(pts[i], pts[(i + 1) % 4], pts[(i + 2) % 4]) > 0 for i in range(4)): return
    b.add(f"{', '.join(P(*p) for p in pts)} শীর্ষবিশিষ্ট চতুর্ভুজের ক্ষেত্রফল কত বর্গ একক?", fr(v), setw(fr(v), [fr(v * 2), fr(v + 2), fr(v / 2), fr(v + 1)]), f"½|Σ(xᵢyᵢ₊₁ − xᵢ₊₁yᵢ)| = {fr(v)}।", M)
def m_kcol(b):
    A = rpt(); d = (R.randint(1, 3), R.randint(-3, 3)); k = R.randint(2, 3)
    B = (A[0] + d[0], A[1] + d[1]); Cc = (A[0] + k * d[0], A[1] + k * d[1])
    b.add(f"{P(*A)}, {P(*B)}, ({num(Cc[0])}, p) বিন্দু তিনটি সমরেখ হলে p = কত?", num(Cc[1]), setw(num(Cc[1]), [num(Cc[1] + 1), num(-Cc[1]) if Cc[1] else '1', num(B[1] + d[1] + 1), num(Cc[0])]), f"ঢাল সমান: p = {num(Cc[1])}।", M)
def m_karea(b):
    a = R.randint(1, 10); h = R.randint(1, 10)
    v = F(a * h, 2)
    b.add(f"(0, 0), ({a}, 0) ও (k, {h}) শীর্ষবিশিষ্ট ত্রিভুজের ক্ষেত্রফল কত (k যেকোনো বাস্তব সংখ্যা)?", fr(v), setw(fr(v), [str(a * h), fr(v + 1), "k-এর উপর নির্ভরশীল", fr(F(a + h, 2))]), f"ভূমি {a}, উচ্চতা {h}; ক্ষেত্রফল {fr(v)}।", M)
def m_mid_tri(b):
    A, B, Cc = rpt(-5, 6), rpt(-5, 6), rpt(-5, 6); v = tarea(A, B, Cc)
    if v == 0: return
    b.add(f"{P(*A)}, {P(*B)}, {P(*Cc)} ত্রিভুজের বাহুগুলোর মধ্যবিন্দু যোগ করে গঠিত ত্রিভুজের ক্ষেত্রফল কত?", fr(v / 4), setw(fr(v / 4), [fr(v / 2), fr(v), fr(v / 3), fr(v * 2)]), f"মূল ক্ষেত্রফল {fr(v)}-এর এক-চতুর্থাংশ।", M)
def h_k_area(b):
    A = rpt(-4, 5); B = rpt(-4, 5); t = R.randint(-4, 5)
    # (t, k) এমন যাতে ক্ষেত্রফল নির্দিষ্ট: সূত্রটি k-তে রৈখিক
    k = R.randint(-5, 6); Cc = (t, k)
    v = tarea(A, B, Cc)
    if v == 0 or A[0] == B[0]: return
    # অপর মান
    coef = A[0] - B[0]   # ক্ষেত্রফল*2 = |… + k(x1 − x2)|
    base = A[0] * B[1] + B[0] * (-A[1]) + t * (A[1] - B[1])
    s = base + k * coef
    k2 = F(-s - base, coef)
    ok = f"{num(k)} বা {num(k2)}" if k2 != k else num(k)
    b.add(f"{P(*A)}, {P(*B)}, ({num(t)}, k) শীর্ষবিশিষ্ট ত্রিভুজের ক্ষেত্রফল {fr(v)} বর্গ একক হলে k = কত?", ok, setw(ok, [num(k), f"{num(-k)} বা {num(-k2)}", f"{num(k + 1)} বা {num(k2 - 1)}", f"{num(k)} বা {num(k2 + 2)}"]), "ক্ষেত্রফলের সূত্রে পরমমান থাকায় দুটি মান।", H)
def h_ratio(b):
    A, B = rpt(), rpt()
    if A[1] * B[1] >= 0: return
    # x-অক্ষ AB-কে কী অনুপাতে ভাগ করে: |y1| : |y2|
    g = math.gcd(abs(A[1]), abs(B[1]))
    ok = f"{abs(A[1]) // g} : {abs(B[1]) // g}"
    b.add(f"x-অক্ষ {P(*A)} ও {P(*B)} বিন্দুর সংযোগ রেখাংশকে কী অনুপাতে বিভক্ত করে?", ok, setw(ok, [f"{abs(B[1]) // g} : {abs(A[1]) // g}", f"{abs(A[0])} : {abs(B[0])}" if A[0] and B[0] else "1 : 1", "1 : 1", f"{abs(A[1]) + abs(B[1])} : 1"]), f"y-স্থানাঙ্ক শূন্য হয় এমন বিন্দু: অনুপাত {ok}।", H)
def h_eqtri(b):
    a = 2 * R.randint(1, 6)
    ok = surd(3, a * a // 4) if a * a // 4 > 1 else '√3'
    v = F(a * a, 4)
    s = f"{v.numerator if v.numerator > 1 else ''}√3" if v.denominator == 1 else f"{v.numerator}√3/{v.denominator}"
    b.add(f"(0, 0) ও ({a}, 0) দুটি শীর্ষবিশিষ্ট সমবাহু ত্রিভুজের ক্ষেত্রফল কত বর্গ একক?", s, setw(s, [f"{a * a // 2 if a * a // 2 > 1 else ''}√3", str(a * a // 2), f"{a}√3", f"{a * a}√3/2" if a * a % 2 else f"{a * a // 2}√3/2" if a * a // 2 > 1 else '√3/2']), f"(√3/4) × {a}² = {s}।", H)
p112 = run('11.2', R, fx112, [e_area, e_axis, e_col], [m_quad, m_kcol, m_karea, m_mid_tri], [h_k_area, h_ratio, h_eqtri])

fx113 = [
 ("(x₁, y₁) ও (x₂, y₂) বিন্দুগামী রেখার ঢাল কত?", "(y₂ − y₁)/(x₂ − x₁)", ["(x₂ − x₁)/(y₂ − y₁)", "(y₂ + y₁)/(x₂ + x₁)", "y₂y₁/x₂x₁"], "ঢালের সূত্র।", E),
 ("x-অক্ষের সমান্তরাল রেখার ঢাল কত?", "0", ["1", "অসংজ্ঞায়িত", "−1"], "y পরিবর্তিত হয় না।", E),
 ("y-অক্ষের সমান্তরাল রেখার ঢাল কেমন?", "অসংজ্ঞায়িত", ["0", "1", "−1"], "x পরিবর্তিত হয় না; হর শূন্য।", E),
 ("দুটি রেখা সমান্তরাল হলে তাদের ঢাল কেমন?", "সমান", ["গুণফল −1", "যোগফল 0", "অনুপাত −1"], "m₁ = m₂।", E),
 ("দুটি রেখা পরস্পর লম্ব হলে তাদের ঢালের গুণফল কত?", "−1", ["1", "0", "অসংজ্ঞায়িত"], "m₁m₂ = −1।", E),
 ("রেখাটি x-অক্ষের ধনাত্মক দিকের সাথে θ কোণ উৎপন্ন করলে ঢাল কত?", "tan θ", ["sin θ", "cos θ", "cot θ"], "m = tan θ।", E),
]
def e_slope(b):
    A, B = rpt(), rpt()
    if A[0] == B[0] or A == B: return
    m = F(B[1] - A[1], B[0] - A[0])
    b.add(f"{P(*A)} ও {P(*B)} বিন্দুগামী রেখার ঢাল কত?", num(m), setw(num(m), [num(1 / m) if m else '1', num(-m) if m else '−1', num(-1 / m) if m else '2', num(m + 1)]), f"({num(B[1])} − ({num(A[1])}))/({num(B[0])} − ({num(A[0])})) = {num(m)}।", E)
def e_angle(b):
    d, v = R.choice([(30, '1/√3'), (45, '1'), (60, '√3'), (120, '−√3'), (135, '−1'), (150, '−1/√3'), (0, '0')])
    b.add(f"একটি রেখা x-অক্ষের ধনাত্মক দিকের সাথে {d}° কোণ উৎপন্ন করলে ঢাল কত?", v, setw(v, ['1/√3', '1', '√3', '−√3', '−1', '−1/√3', '0']), f"m = tan {d}° = {v}।", E)
def e_par(b):
    m = F(R.randint(-6, 6), R.choice([1, 2, 3]))
    b.add(f"ঢাল {num(m)} বিশিষ্ট রেখার সমান্তরাল রেখার ঢাল কত?", num(m), setw(num(m), [num(-m) if m else '1', num(-1 / m) if m else 'অসংজ্ঞায়িত', num(1 / m) if m else '−1', num(m + 1)]), "সমান্তরাল রেখার ঢাল সমান।", E)
def m_perp(b):
    m = F(R.choice([v for v in range(-6, 7) if v]), R.choice([1, 2, 3]))
    ok = num(-1 / m)
    b.add(f"ঢাল {num(m)} বিশিষ্ট রেখার উপর লম্ব রেখার ঢাল কত?", ok, setw(ok, [num(m), num(1 / m), num(-m), num(-1 / m + 1)]), "m₁m₂ = −1।", M)
def m_k(b):
    A = rpt(); m = R.choice([v for v in range(-4, 5) if v]); dx = R.choice([v for v in range(-4, 5) if v])
    B = (A[0] + dx, A[1] + m * dx)
    b.add(f"{P(*A)} ও ({num(B[0])}, k) বিন্দুগামী রেখার ঢাল {num(m)} হলে k = কত?", num(B[1]), setw(num(B[1]), [num(B[1] + 1), num(A[1] - m * dx), num(m * dx), num(B[1] - 2)]), f"(k − {num(A[1])})/{num(dx)} = {num(m)} ⇒ k = {num(B[1])}।", M)
def m_eqslope(b):
    a, c = R.choice([v for v in range(-6, 7) if v]), R.choice([v for v in range(-6, 7) if v]); k = R.randint(-9, 9)
    m = F(-a, c)
    b.add(f"{pfmt({k_: v for k_, v in {(1, 0): a, (0, 1): c, (0, 0): k}.items() if v}, ('x', 'y'))} = 0 রেখার ঢাল কত?", num(m), setw(num(m), [num(-m) if m else '1', num(F(c, a)), num(F(-c, a)), num(F(-k, c)) if F(-k, c) != m else num(m + 1)]), f"y = −({a}/{c})x − … ⇒ ঢাল {num(m)}।", M)
def m_col_slope(b):
    A = rpt(); d = (R.randint(1, 3), R.randint(-3, 3)); k = R.randint(2, 4)
    Cc = (A[0] + k * d[0], A[1] + k * d[1]); B = (A[0] + d[0], A[1] + d[1])
    ok = 'সমরেখ'
    b.add(f"AB ও BC-এর ঢাল সমান হলে A{P(*A)}, B{P(*B)}, C{P(*Cc)} বিন্দু তিনটি কেমন?", ok, ['পরস্পর লম্ব', 'সমবাহু ত্রিভুজের শীর্ষ', 'বৃত্তের উপর'], f"ঢাল = {num(F(d[1], d[0]))}; সমরেখ।", M)
def h_perp_k(b):
    m1 = F(R.choice([v for v in range(-5, 6) if v]), R.choice([1, 2])); A = rpt(); dx = R.choice([v for v in range(-4, 5) if v])
    m2 = -1 / m1; ky = A[1] + m2 * dx
    if ky.denominator > 1: return
    b.add(f"ঢাল {num(m1)} বিশিষ্ট রেখার উপর লম্ব একটি রেখা {P(*A)} ও ({num(A[0] + dx)}, k) বিন্দুগামী হলে k = কত?", num(ky), setw(num(ky), [num(A[1] + m1 * dx) if A[1] + m1 * dx != ky else num(ky + 1), num(ky + 1), num(-ky) if ky else '2', num(A[1] - m2 * dx)]), f"লম্বের ঢাল {num(m2)}; k = {num(ky)}।", H)
def h_angle_between(b):
    pairs = [(F(1), F(-1), '90°'), (F(0), F(1), '45°'), (F(1), F(1), '0°')]
    # tan θ = |(m1 − m2)/(1 + m1 m2)|
    m1, m2 = R.choice([(1, 0), (0, 1), (1, -1), (3, F(1, 3) * -3)])  # সহজ রাখতে
    opts = [((F(1), F(0)), '45°'), ((F(1), F(-1)), '90°'), ((F(2), F(-1, 2)), '90°'), ((F(1, 3) * 3, F(0)), '45°')]
    (m1, m2), ok = R.choice(opts)
    # √3 ঢালের সাথে 1/√3: 30°
    b.add(f"ঢাল {num(m1)} ও {num(m2)} বিশিষ্ট রেখাদ্বয়ের মধ্যবর্তী সূক্ষ্মকোণ কত?", ok, setw(ok, ['0°', '30°', '45°', '60°', '90°']), "tan θ = |(m₁ − m₂)/(1 + m₁m₂)|।", H)
    m = R.choice([v for v in range(-6, 7) if v]); c1, c2 = R.sample([v for v in range(-9, 10) if v], 2)
    ln = lambda c: 'y = ' + pfmt({(1,): m, (0,): c}, X)
    b.add(f"{ln(c1)} এবং {ln(c2)} রেখাদ্বয় কেমন?", 'সমান্তরাল', ['পরস্পর লম্ব', 'একই রেখা', 'মূলবিন্দুতে ছেদ করে'], "ঢাল সমান কিন্তু ছেদাংশ ভিন্ন।", H)
def h_slope_from_angle(b):
    A = rpt(); d = R.choice([45, 135])
    m = 1 if d == 45 else -1; dx = R.randint(1, 6)
    ok = num(A[1] + m * dx)
    b.add(f"{P(*A)} বিন্দুগামী একটি রেখা x-অক্ষের ধনাত্মক দিকের সাথে {d}° কোণ উৎপন্ন করে। রেখাটি ({num(A[0] + dx)}, k) বিন্দু দিয়ে গেলে k = কত?", ok, setw(ok, [num(A[1] - m * dx), num(A[1] + dx + 1), num(A[0] + m * dx), num(A[1])]), f"ঢাল {m}; k = {ok}।", H)
p113 = run('11.3', R, fx113, [e_slope, e_angle, e_par], [m_perp, m_k, m_eqslope, m_col_slope], [h_perp_k, h_angle_between, h_slope_from_angle])

def L(a, c, k):
    return pfmt({k_: v for k_, v in {(1, 0): a, (0, 1): c, (0, 0): k}.items() if v}, ('x', 'y')) + ' = 0'
def norm(a, c, k):
    g = math.gcd(math.gcd(abs(a), abs(c)), abs(k)) or 1
    a, c, k = a // g, c // g, k // g
    if a < 0 or (a == 0 and c < 0): a, c, k = -a, -c, -k
    return a, c, k
fx114 = [
 ("ঢাল m ও y-অক্ষের ছেদাংশ c হলে রেখার সমীকরণ কোনটি?", "y = mx + c", ["y = cx + m", "x = my + c", "y = m(x + c)"], "ঢাল-ছেদাংশ আকার।", E),
 ("(x₁, y₁) বিন্দুগামী ও ঢাল m বিশিষ্ট রেখার সমীকরণ কোনটি?", "y − y₁ = m(x − x₁)", ["y + y₁ = m(x + x₁)", "y − x₁ = m(x − y₁)", "y = m(x − x₁) − y₁"], "বিন্দু-ঢাল আকার।", E),
 ("x ও y অক্ষের ছেদাংশ যথাক্রমে a ও b হলে রেখার সমীকরণ কোনটি?", "x/a + y/b = 1", ["x/b + y/a = 1", "ax + by = 1", "x/a − y/b = 1"], "ছেদাংশ আকার।", E),
 ("x-অক্ষের সমীকরণ কোনটি?", "y = 0", ["x = 0", "y = x", "x + y = 0"], "x-অক্ষে সর্বত্র y = 0।", E),
 ("মূলবিন্দুগামী রেখার সাধারণ সমীকরণ কোনটি?", "y = mx", ["y = mx + c (c ≠ 0)", "x = c", "y = c"], "c = 0।", E),
]
def e_mc(b):
    m, c = R.choice([v for v in range(-6, 7) if v]), R.randint(-9, 9)
    ok = f"y = {pfmt({k: v for k, v in {(1,): m, (0,): c}.items() if v}, X)}"
    b.add(f"ঢাল {num(m)} এবং y-অক্ষের ছেদাংশ {num(c)} বিশিষ্ট রেখার সমীকরণ কোনটি?", ok, setw(ok, [f"y = {pfmt({k: v for k, v in {(1,): c, (0,): m}.items() if v}, X)}" if c else f"y = {num(m)}", f"y = {pfmt({k: v for k, v in {(1,): -m, (0,): c}.items() if v}, X)}", f"y = {pfmt({k: v for k, v in {(1,): m, (0,): -c}.items() if v}, X)}" if c else f"y = {pfmt({(1,): m, (0,): 1}, X)}"]), "y = mx + c।", E)
def e_intercepts(b):
    a, c = R.choice([v for v in range(-8, 9) if abs(v) > 1]), R.choice([v for v in range(-8, 9) if abs(v) > 1])
    ok = f"x/{a if a > 0 else '(' + num(a) + ')'} + y/{c if c > 0 else '(' + num(c) + ')'} = 1"
    w = f"x/{c if c > 0 else '(' + num(c) + ')'} + y/{a if a > 0 else '(' + num(a) + ')'} = 1"
    b.add(f"x-অক্ষ ও y-অক্ষের ছেদাংশ যথাক্রমে {num(a)} ও {num(c)} হলে রেখার সমীকরণ কোনটি?", ok, setw(ok, [w, pfmt({(1, 0): a, (0, 1): c}, ('x', 'y')) + ' = 1', f"x/{a if a > 0 else '(' + num(a) + ')'} − y/{c if c > 0 else '(' + num(c) + ')'} = 1"]), "x/a + y/b = 1।", E)
def e_yint(b):
    a, c, k = R.choice([v for v in range(-6, 7) if v]), R.choice([v for v in range(-6, 7) if v]), R.choice([v for v in range(-12, 13) if v])
    v = F(-k, c)
    b.add(f"{L(a, c, k)} রেখাটি y-অক্ষকে কোন বিন্দুতে ছেদ করে?", P(0, v), setw(P(0, v), [P(v, 0), P(0, -v), P(F(-k, a), 0), P(0, F(-k, a)) if F(-k, a) != v else P(0, v + 1)]), f"x = 0 বসিয়ে y = {num(v)}।", E)
def m_two(b):
    A, B = rpt(), rpt()
    if A[0] == B[0] or A == B: return
    a, c, k = norm(B[1] - A[1], A[0] - B[0], B[0] * A[1] - A[0] * B[1])
    ok = L(a, c, k)
    w1 = L(*norm(a, -c, k)) if c else L(a, 1, k); w2 = L(*norm(a, c, -k)) if k else L(a, c, 1); w3 = L(*norm(c, a, k)) if (c, a) != (a, c) else L(a, c, k + 1)
    b.add(f"{P(*A)} ও {P(*B)} বিন্দুগামী রেখার সমীকরণ কোনটি?", ok, setw(ok, [w1, w2, w3, L(a, c, k + 2)]), "(y − y₁)/(y₁ − y₂) = (x − x₁)/(x₁ − x₂)।", M)
def m_pt_slope(b):
    A = rpt(); m = F(R.choice([v for v in range(-5, 6) if v]), R.choice([1, 2, 3]))
    # y − y1 = m(x − x1) ⇒ m.num x − m.den y + (m.den y1 − m.num x1) = 0
    a, c, k = norm(m.numerator, -m.denominator, m.denominator * A[1] - m.numerator * A[0])
    ok = L(a, c, k)
    b.add(f"{P(*A)} বিন্দুগামী ও {num(m)} ঢালবিশিষ্ট রেখার সমীকরণ কোনটি?", ok, setw(ok, [L(*norm(a, -c, k)), L(*norm(a, c, -k)) if k else L(a, c, 3), L(*norm(c, a, k)) if a != -c else L(a, c, k + 1), L(a, c, k + 1)]), "y − y₁ = m(x − x₁)।", M)
def m_inter(b):
    x, y = R.randint(-5, 6), R.randint(-5, 6)
    a1, c1 = R.choice([1, 2, 3, -1]), R.choice([1, 2, -1, -2]); a2, c2 = R.choice([1, 2, -1, 3]), R.choice([1, -1, 3, -2])
    if a1 * c2 == a2 * c1: return
    k1, k2 = -(a1 * x + c1 * y), -(a2 * x + c2 * y)
    ok = P(x, y)
    b.add(f"{L(a1, c1, k1)} এবং {L(a2, c2, k2)} রেখাদ্বয়ের ছেদবিন্দু কোনটি?", ok, setw(ok, [P(y, x), P(-x, -y), P(x + 1, y), P(x, y - 1)]), f"সমাধান করে ({num(x)}, {num(y)})।", M)
def m_par_line(b):
    a, c = R.choice([1, 2, 3, -2]), R.choice([1, -1, 2, -3]); k = R.randint(-9, 9); A = rpt()
    k2 = -(a * A[0] + c * A[1])
    ok = L(*norm(a, c, k2))
    b.add(f"{P(*A)} বিন্দুগামী এবং {L(a, c, k)} রেখার সমান্তরাল রেখার সমীকরণ কোনটি?", ok, setw(ok, [L(*norm(c, -a, -(c * A[0] - a * A[1]))), L(*norm(a, c, -k2)) if k2 else L(a, c, 2), L(*norm(a, -c, -(a * A[0] - c * A[1]))), L(*norm(a, c, k2 + 1))]), "ax + by + k′ = 0 আকারে, বিন্দু বসিয়ে k′।", M)
def h_perp_line(b):
    a, c = R.choice([1, 2, 3, -2]), R.choice([1, -1, 2, -3]); k = R.randint(-9, 9); A = rpt()
    # লম্ব: c x − a y + k′ = 0
    k2 = -(c * A[0] - a * A[1])
    ok = L(*norm(c, -a, k2))
    b.add(f"{P(*A)} বিন্দুগামী এবং {L(a, c, k)} রেখার উপর লম্ব রেখার সমীকরণ কোনটি?", ok, setw(ok, [L(*norm(a, c, -(a * A[0] + c * A[1]))), L(*norm(c, a, -(c * A[0] + a * A[1]))), L(*norm(c, -a, -k2)) if k2 else L(c, -a, 3), L(*norm(c, -a, k2 + 1))]), "লম্ব রেখা: bx − ay + k′ = 0।", H)
def h_tri_area(b):
    a, c = R.choice([v for v in range(-8, 9) if abs(v) > 1]), R.choice([v for v in range(-8, 9) if abs(v) > 1])
    v = F(abs(a * c), 2)
    b.add(f"x/{a if a > 0 else '(' + num(a) + ')'} + y/{c if c > 0 else '(' + num(c) + ')'} = 1 রেখাটি অক্ষদ্বয়ের সাথে যে ত্রিভুজ গঠন করে তার ক্ষেত্রফল কত বর্গ একক?", fr(v), setw(fr(v), [str(abs(a * c)), fr(v + 1), str(abs(a) + abs(c)), fr(F(abs(a + c), 2)) if F(abs(a + c), 2) != v else fr(v * 3)]), f"½ × |{num(a)}| × |{num(c)}| = {fr(v)}।", H)
def h_conc(b):
    x, y = R.randint(-4, 5), R.randint(-4, 5)
    a1, c1 = 1, R.choice([1, 2, -1]); a2, c2 = R.choice([2, 3, -1]), R.choice([1, -2, 3])
    if a1 * c2 == a2 * c1: return
    k1, k2 = -(a1 * x + c1 * y), -(a2 * x + c2 * y); p = R.choice([v for v in range(-4, 5) if v])
    # তৃতীয় রেখা p x + y + k = 0 একই বিন্দুগামী ⇒ k = −(p x + y)
    k = -(p * x + y)
    b.add(f"{L(a1, c1, k1)}, {L(a2, c2, k2)} এবং {pfmt({(1, 0): p, (0, 1): 1}, ('x', 'y'))} + k = 0 রেখা তিনটি সমবিন্দু হলে k = কত?", num(k), setw(num(k), [num(-k) if k else '1', num(k + 1), num(p * x - y) if p * x - y != k else num(k + 2), num(x + y)]), f"প্রথম দুটির ছেদবিন্দু ({num(x)}, {num(y)}) বসিয়ে k = {num(k)}।", H)
def h_dist_pt(b):
    a, c = R.choice([(3, 4), (4, 3), (5, 12), (12, 5), (6, 8), (8, 6), (1, 0), (0, 1)]); a *= R.choice([1, -1])
    A = rpt(); d = R.randint(1, 6); n = math.isqrt(a * a + c * c)
    k = d * n - (a * A[0] + c * A[1])
    b.add(f"{P(*A)} বিন্দু থেকে {L(a, c, k)} রেখার লম্ব দূরত্ব কত একক?", d, setw(d, [d * n, d + 1, abs(k), F(d, n) if n > 1 else d + 2]), f"|{num(a)}·{num(A[0])} + {num(c)}·{num(A[1])} + {num(k)}|/√({a * a + c * c}) = {d}।", H)
p114 = run('11.4', R, fx114, [e_mc, e_intercepts, e_yint], [m_two, m_pt_slope, m_inter, m_par_line], [h_perp_line, h_tri_area, h_conc, h_dist_pt])
save('h11', p111 + p112 + p113 + p114)

# ---------------- 12 সমতলীয় ভেক্টর ----------------
def V(x, y): return f"{pfmt({k: v for k, v in {(1, 0): x, (0, 1): y}.items() if v}, ('i', 'j'))}" if (x or y) else '0'
fx12 = [
 ("যে রাশির মান ও দিক উভয়ই আছে তাকে কী বলে?", "ভেক্টর রাশি", ["স্কেলার রাশি", "ধ্রুবক", "অনুপাত"], "ভেক্টরের সংজ্ঞা।", E),
 ("কোনটি স্কেলার রাশি?", "ভর", ["বেগ", "সরণ", "বল"], "ভরের দিক নেই।", E),
 ("কোনটি ভেক্টর রাশি?", "সরণ", ["দূরত্ব", "দ্রুতি", "সময়"], "সরণের দিক আছে।", E),
 ("যে ভেক্টরের মান শূন্য তাকে কী বলে?", "শূন্য ভেক্টর", ["একক ভেক্টর", "সমান ভেক্টর", "বিপরীত ভেক্টর"], "শূন্য ভেক্টরের দিক অনির্দিষ্ট।", E),
 ("যে ভেক্টরের মান 1 তাকে কী বলে?", "একক ভেক্টর", ["শূন্য ভেক্টর", "অবস্থান ভেক্টর", "সমরেখ ভেক্টর"], "মান 1।", E),
 ("AB⃗ + BC⃗ = কত?", "AC⃗", ["CA⃗", "BA⃗", "0"], "ভেক্টর যোগের ত্রিভুজ বিধি।", E),
 ("AB⃗ + BA⃗ = কত?", "0", ["2AB⃗", "AB⃗", "BA⃗"], "বিপরীত ভেক্টরের যোগফল শূন্য।", E),
 ("ভেক্টর যোগের বিনিময় বিধি কোনটি?", "a⃗ + b⃗ = b⃗ + a⃗", ["a⃗ + (b⃗ + c⃗) = (a⃗ + b⃗) + c⃗", "m(a⃗ + b⃗) = ma⃗ + mb⃗", "a⃗ + 0 = a⃗"], "বিনিময় বিধি।", M),
 ("ত্রিভুজের দুই বাহুর মধ্যবিন্দুর সংযোগ রেখাংশ তৃতীয় বাহুর কেমন?", "সমান্তরাল ও অর্ধেক", ["লম্ব ও সমান", "সমান্তরাল ও সমান", "লম্ব ও অর্ধেক"], "ভেক্টর পদ্ধতিতে প্রমাণযোগ্য।", M),
 ("a⃗ ও b⃗ সমরেখ হলে কোনটি সত্য?", "a⃗ = mb⃗ (m স্কেলার)", ["a⃗ + b⃗ = 0 সবসময়", "|a⃗| = |b⃗| সবসময়", "a⃗ ⊥ b⃗"], "সমরেখ ভেক্টর একটি অপরটির স্কেলার গুণিতক।", M),
]
def e_mag(b):
    x, y = R.choice([(3, 4), (5, 12), (6, 8), (8, 15), (1, 1), (2, 3), (1, 2), (7, 24), (0, 5), (4, 0)])
    x, y = x * R.choice([1, -1]), y * R.choice([1, -1])
    ok = sqf(x * x + y * y)
    b.add(f"a⃗ = {V(x, y)} হলে |a⃗| = কত?", ok, setw(ok, [str(abs(x) + abs(y)), str(x * x + y * y), sqf(x * x + y * y + 1), sqf(abs(x * x - y * y)) if x * x != y * y else '0']), f"√({x * x} + {y * y}) = {ok}।", E)
def e_add(b):
    a, c = rpt(-5, 6), rpt(-5, 6)
    s = (a[0] + c[0], a[1] + c[1])
    ok = V(*s)
    b.add(f"a⃗ = {V(*a)} ও b⃗ = {V(*c)} হলে a⃗ + b⃗ = কত?", ok, setw(ok, [V(a[0] - c[0], a[1] - c[1]), V(s[1], s[0]), V(s[0] + 1, s[1]), V(-s[0], -s[1]) if s != (0, 0) else V(1, 1)]), "অনুরূপ উপাংশ যোগ।", E)
def e_scal(b):
    a = rpt(-5, 6); k = R.choice([2, 3, -2, -3, 4])
    if a == (0, 0): return
    ok = V(k * a[0], k * a[1])
    b.add(f"a⃗ = {V(*a)} হলে {k}a⃗ = কত?", ok, setw(ok, [V(k * a[0], a[1]), V(a[0], k * a[1]), V(-k * a[0], -k * a[1]), V(k + a[0], k + a[1])]), "প্রতিটি উপাংশকে গুণ।", E)
def e_ab(b):
    A, B = rpt(), rpt()
    if A == B: return
    ok = V(B[0] - A[0], B[1] - A[1])
    b.add(f"A{P(*A)} ও B{P(*B)} হলে AB⃗ = কত?", ok, setw(ok, [V(A[0] - B[0], A[1] - B[1]), V(A[0] + B[0], A[1] + B[1]), V(B[1] - A[1], B[0] - A[0]) if B[1] - A[1] != B[0] - A[0] else V(B[0] - A[0] + 1, B[1] - A[1])]), "AB⃗ = OB⃗ − OA⃗।", E)
def m_unit(b):
    x, y = R.choice([(3, 4), (5, 12), (6, 8), (8, 15), (4, 3), (12, 5), (7, 24)]); x, y = x * R.choice([1, -1]), y * R.choice([1, -1])
    n = math.isqrt(x * x + y * y)
    ok = f"({V(x, y)})/{n}"
    b.add(f"a⃗ = {V(x, y)}-এর দিকে একক ভেক্টর কোনটি?", ok, setw(ok, [V(x, y), f"({V(y, x)})/{n}", f"({V(x, y)})/{n * n}", f"({V(-x, -y)})/{n}"]), f"a⃗/|a⃗| = ({V(x, y)})/{n}।", M)
def m_lin(b):
    a, c = rpt(-4, 5), rpt(-4, 5); p, q = R.choice([2, 3, -1]), R.choice([2, -2, 3, 1])
    s = (p * a[0] + q * c[0], p * a[1] + q * c[1])
    ok = V(*s)
    b.add(f"a⃗ = {V(*a)}, b⃗ = {V(*c)} হলে {p if p != -1 else '−'}a⃗ {'+' if q > 0 else '−'} {abs(q) if abs(q) != 1 else ''}b⃗ = কত?".replace(' −a⃗', ' −a⃗'), ok, setw(ok, [V(p * a[0] - q * c[0], p * a[1] - q * c[1]), V(q * a[0] + p * c[0], q * a[1] + p * c[1]), V(s[0] + 1, s[1]), V(s[1], s[0])]), "উপাংশ অনুযায়ী হিসাব।", M)
def m_col(b):
    a = (R.randint(1, 5), R.randint(-5, 5)); k = R.choice([2, 3, -2, F(1, 2) * 2])
    k = int(k); c = (k * a[0], k * a[1])
    b.add(f"a⃗ = {V(*a)} ও b⃗ = {V(c[0], 0)}{' ' if False else ''} + pj (অর্থাৎ b⃗ = {num(c[0])}i + pj) সমরেখ হলে p = কত?", num(c[1]), setw(num(c[1]), [num(-c[1]) if c[1] else '1', num(a[1]), num(c[1] + k), num(F(a[1], k)) if F(a[1], k) != c[1] else num(c[1] + 1)]), f"b⃗ = {k}a⃗ ⇒ p = {num(c[1])}।", M)
def m_mid(b):
    A, B = rpt(), rpt()
    if (A[0] + B[0]) % 2 or (A[1] + B[1]) % 2 or A == B: return
    ok = V((A[0] + B[0]) // 2, (A[1] + B[1]) // 2)
    b.add(f"A ও B বিন্দুর অবস্থান ভেক্টর যথাক্রমে {V(*A)} ও {V(*B)} হলে AB-এর মধ্যবিন্দুর অবস্থান ভেক্টর কোনটি?", ok, setw(ok, [V(A[0] + B[0], A[1] + B[1]), V((B[0] - A[0]) // 2, (B[1] - A[1]) // 2), V((A[0] + B[0]) // 2 + 1, (A[1] + B[1]) // 2), V(B[0] - A[0], B[1] - A[1])]), "(a⃗ + b⃗)/2।", M)
def m_magsum(b):
    a, c = rpt(-4, 5), rpt(-4, 5); s = (a[0] + c[0], a[1] + c[1])
    if s == (0, 0): return
    ok = sqf(s[0] ** 2 + s[1] ** 2)
    b.add(f"a⃗ = {V(*a)}, b⃗ = {V(*c)} হলে |a⃗ + b⃗| = কত?", ok, setw(ok, [sqf(a[0] ** 2 + a[1] ** 2 + c[0] ** 2 + c[1] ** 2) if a[0] ** 2 + a[1] ** 2 + c[0] ** 2 + c[1] ** 2 else '1', str(abs(s[0]) + abs(s[1])), sqf(s[0] ** 2 + s[1] ** 2 + 1), sqf((a[0] - c[0]) ** 2 + (a[1] - c[1]) ** 2) if (a[0] - c[0]) ** 2 + (a[1] - c[1]) ** 2 else '2']), f"a⃗ + b⃗ = {V(*s)}।", M)
def h_mn(b):
    a, c = (R.randint(1, 4), R.randint(-3, 3)), (R.randint(-3, 3), R.randint(1, 4))
    if a[0] * c[1] - a[1] * c[0] == 0: return
    m, n = R.randint(-3, 4), R.randint(-3, 4)
    t = (m * a[0] + n * c[0], m * a[1] + n * c[1])
    ok = f"m = {num(m)}, n = {num(n)}"
    b.add(f"a⃗ = {V(*a)}, b⃗ = {V(*c)} এবং ma⃗ + nb⃗ = {V(*t)} হলে m ও n-এর মান কত?", ok, setw(ok, [f"m = {num(n)}, n = {num(m)}", f"m = {num(m + 1)}, n = {num(n)}", f"m = {num(-m)}, n = {num(-n)}" if (m, n) != (0, 0) else "m = 1, n = 1", f"m = {num(m)}, n = {num(n - 1)}"]), "উপাংশ মিলিয়ে দুটি সমীকরণ।", H)
def h_section(b):
    A, B = rpt(), rpt(); m, n = R.choice([(1, 2), (2, 1), (1, 3), (3, 1), (2, 3)])
    px, py = F(m * B[0] + n * A[0], m + n), F(m * B[1] + n * A[1], m + n)
    if px.denominator > 1 or py.denominator > 1 or A == B: return
    ok = V(int(px), int(py))
    qx, qy = F(n * B[0] + m * A[0], m + n), F(n * B[1] + m * A[1], m + n)
    b.add(f"A ও B-এর অবস্থান ভেক্টর {V(*A)} ও {V(*B)}। AB-কে {m} : {n} অনুপাতে অন্তর্বিভক্তকারী বিন্দুর অবস্থান ভেক্টর কোনটি?", ok, setw(ok, [f"({V(qx.numerator, qy.numerator)})/{qx.denominator}" if qx.denominator > 1 or qy.denominator > 1 else V(int(qx), int(qy)), V(A[0] + B[0], A[1] + B[1]), V(int(px) + 1, int(py)), V(int(py), int(px))]), "(na⃗ + mb⃗)/(m + n)।", H)
def h_paral(b):
    A, B, Cc = rpt(), rpt(), rpt()
    if (B[0] - A[0]) * (Cc[1] - A[1]) - (B[1] - A[1]) * (Cc[0] - A[0]) == 0: return
    D = (A[0] + Cc[0] - B[0], A[1] + Cc[1] - B[1])
    ok = V(*D)
    b.add(f"ABCD সামান্তরিকের A, B, C-এর অবস্থান ভেক্টর যথাক্রমে {V(*A)}, {V(*B)}, {V(*Cc)} হলে D-এর অবস্থান ভেক্টর কোনটি?", ok, setw(ok, [V(B[0] + Cc[0] - A[0], B[1] + Cc[1] - A[1]), V(A[0] + B[0] - Cc[0], A[1] + B[1] - Cc[1]), V(D[0] + 1, D[1]), V(D[1], D[0])]), "AD⃗ = BC⃗ ⇒ d⃗ = a⃗ + c⃗ − b⃗।", H)
def h_magk(b):
    x, y = R.choice([(3, 4), (4, 3), (5, 12), (12, 5), (6, 8), (8, 6)])
    n = math.isqrt(x * x + y * y)
    ok = f"±{y}"
    b.add(f"a⃗ = {x}i + kj এবং |a⃗| = {n} হলে k = কত?", ok, setw(ok, [str(y), f"±{n - x}", f"±{y * y}", f"±{x}"]), f"{x * x} + k² = {n * n} ⇒ k = ±{y}।", H)
p12 = run(None, R, fx12, [e_mag, e_add, e_scal, e_ab], [m_unit, m_lin, m_col, m_mid, m_magsum], [h_mn, h_section, h_paral, h_magk])
save('h12', p12)

# ---------------- 13 ঘন জ্যামিতি ----------------
fx13 = [
 ("একটি ঘনকের কয়টি তল আছে?", "6টি", ["8টি", "12টি", "4টি"], "ঘনকের 6টি বর্গাকার তল।", E),
 ("একটি ঘনকের কয়টি ধার আছে?", "12টি", ["6টি", "8টি", "10টি"], "ঘনকের 12টি ধার।", E),
 ("একটি ঘনকের কয়টি শীর্ষবিন্দু আছে?", "8টি", ["6টি", "12টি", "4টি"], "ঘনকের 8টি শীর্ষ।", E),
 ("দুটি সরলরেখা একই সমতলে নেই এবং পরস্পর ছেদও করে না—এদের কী বলে?", "নৈকতলীয় (স্ক্যু) রেখা", ["সমান্তরাল রেখা", "লম্ব রেখা", "সমবিন্দু রেখা"], "ভিন্ন সমতলে অবস্থিত অছেদী রেখা।", E),
 ("একটি সমতল নির্দিষ্ট করতে কমপক্ষে কয়টি অসমরেখ বিন্দু লাগে?", "3টি", ["2টি", "4টি", "1টি"], "তিনটি অসমরেখ বিন্দু একটি সমতল নির্দিষ্ট করে।", E),
 ("দুটি ভিন্ন সমতল পরস্পর ছেদ করলে ছেদাংশ কী হয়?", "একটি সরলরেখা", ["একটি বিন্দু", "একটি সমতল", "একটি বৃত্ত"], "দুই সমতলের ছেদ রেখা।", E),
 ("অয়লারের সূত্র অনুযায়ী বহুতলকের জন্য কোনটি সত্য? (V শীর্ষ, E ধার, F তল)", "V − E + F = 2", ["V + E − F = 2", "V + E + F = 2", "V − E − F = 0"], "অয়লারের সূত্র।", M),
 ("সুষম চতুস্তলকের কয়টি তল আছে?", "4টি", ["3টি", "6টি", "8টি"], "চারটি সমবাহু ত্রিভুজাকার তল।", M),
 ("একটি প্রিজমের ভূমির বাহু n হলে মোট তলের সংখ্যা কত?", "n + 2", ["n", "2n", "n + 1"], "n টি পার্শ্বতল + 2টি ভূমি।", M),
 ("একটি পিরামিডের ভূমির বাহু n হলে মোট তলের সংখ্যা কত?", "n + 1", ["n", "2n", "n + 2"], "n টি পার্শ্বতল + 1টি ভূমি।", M),
]
def e_cube(b):
    a = R.randint(2, 15)
    b.add(f"{a} সেমি ধারবিশিষ্ট ঘনকের আয়তন কত ঘন সেমি?", a ** 3, setw(a ** 3, [6 * a * a, a * a, 3 * a, a ** 3 + a]), f"{a}³ = {a ** 3}।", E)
def e_cube_s(b):
    a = R.randint(2, 15)
    b.add(f"{a} সেমি ধারবিশিষ্ট ঘনকের সমগ্রতলের ক্ষেত্রফল কত বর্গ সেমি?", 6 * a * a, setw(6 * a * a, [a ** 3, 4 * a * a, 12 * a, 6 * a]), f"6 × {a}² = {6 * a * a}।", E)
def e_cuboid(b):
    l, w, h = R.randint(2, 15), R.randint(2, 12), R.randint(2, 10)
    v = l * w * h
    b.add(f"একটি আয়তাকার ঘনবস্তুর দৈর্ঘ্য {l}, প্রস্থ {w} ও উচ্চতা {h} সেমি হলে আয়তন কত ঘন সেমি?", v, setw(v, [2 * (l * w + w * h + h * l), l + w + h, v + l, 2 * v]), f"{l} × {w} × {h} = {v}।", E)
def e_cyl(b):
    r, h = R.choice([7, 14, 21, 3.5]), R.randint(2, 20)
    if r == 3.5: return
    v = F(22, 7) * r * r * h
    b.add(f"{r} সেমি ব্যাসার্ধ ও {h} সেমি উচ্চতার সিলিন্ডারের আয়তন কত ঘন সেমি? (π = 22/7)", fr(v), setw(fr(v), [fr(2 * F(22, 7) * r * h), fr(v / 3), fr(v * 2), fr(F(22, 7) * r * h)]), f"πr²h = {fr(v)}।", E)
def m_cuboid_s(b):
    l, w, h = R.randint(2, 15), R.randint(2, 12), R.randint(2, 10)
    S = 2 * (l * w + w * h + h * l)
    b.add(f"দৈর্ঘ্য {l}, প্রস্থ {w} ও উচ্চতা {h} সেমি বিশিষ্ট আয়তাকার ঘনবস্তুর সমগ্রতলের ক্ষেত্রফল কত বর্গ সেমি?", S, setw(S, [l * w * h, S // 2, S + 2 * l * w, 2 * (l + w) * h]), f"2(lw + wh + hl) = {S}।", M)
def m_diag(b):
    l, w, h = R.choice([(3, 4, 12), (2, 3, 6), (1, 4, 8), (2, 6, 9), (4, 4, 7), (6, 6, 7), (2, 10, 11), (8, 9, 12), (12, 16, 21)])
    d = math.isqrt(l * l + w * w + h * h)
    b.add(f"দৈর্ঘ্য {l}, প্রস্থ {w} ও উচ্চতা {h} সেমি বিশিষ্ট আয়তাকার ঘনবস্তুর কর্ণের দৈর্ঘ্য কত সেমি?", d, setw(d, [l + w + h, d + 1, l * w * h // d if l * w * h // d != d else d + 2, math.isqrt(l * l + w * w) if math.isqrt(l * l + w * w) != d else d - 1]), f"√({l}² + {w}² + {h}²) = {d}।", M)
def m_cone(b):
    r, h = R.choice([(3, 4), (5, 12), (6, 8), (7, 24), (8, 15), (9, 12)])
    l = math.isqrt(r * r + h * h)
    ok = f"{r * l}π"
    b.add(f"ভূমির ব্যাসার্ধ {r} সেমি ও উচ্চতা {h} সেমি বিশিষ্ট শঙ্কুর বক্রতলের ক্ষেত্রফল কত বর্গ সেমি?", ok, setw(ok, [f"{r * h}π", f"{r * (l + r)}π", f"{r * r * h // 3}π" if r * r * h % 3 == 0 else f"{r * r * h}π/3", f"{2 * r * l}π"]), f"হেলানো উচ্চতা {l}; πrl = {ok}।", M)
def m_cone_v(b):
    r, h = R.randint(2, 12), 3 * R.randint(1, 6)
    ok = f"{r * r * h // 3}π"
    b.add(f"ভূমির ব্যাসার্ধ {r} সেমি ও উচ্চতা {h} সেমি বিশিষ্ট শঙ্কুর আয়তন কত ঘন সেমি?", ok, setw(ok, [f"{r * r * h}π", f"{r * h}π", f"{2 * r * r * h // 3}π", f"{r * r * h // 3 + r}π"]), f"(1/3)πr²h = {ok}।", M)
def m_sphere(b):
    r = 3 * R.randint(1, 5)
    ok = f"{4 * r ** 3 // 3}π"
    b.add(f"{r} সেমি ব্যাসার্ধের গোলকের আয়তন কত ঘন সেমি?", ok, setw(ok, [f"{4 * r * r}π", f"{r ** 3}π", f"{2 * r ** 3 // 3}π", f"{4 * r ** 3}π"]), f"(4/3)πr³ = {ok}।", M)
def m_sphere_s(b):
    r = R.randint(2, 15)
    ok = f"{4 * r * r}π"
    b.add(f"{r} সেমি ব্যাসার্ধের গোলকের পৃষ্ঠতলের ক্ষেত্রফল কত বর্গ সেমি?", ok, setw(ok, [f"{2 * r * r}π", f"{r * r}π", f"{4 * r ** 3}π/3" if (4 * r ** 3) % 3 else f"{4 * r ** 3 // 3}π", f"{4 * r}π"]), f"4πr² = {ok}।", M)
def m_euler(b):
    kind = R.choice([('প্রিজম', lambda n: (2 * n, 3 * n, n + 2)), ('পিরামিড', lambda n: (n + 1, 2 * n, n + 1))])
    n = R.randint(3, 10); V_, E_, F_ = kind[1](n)
    q = R.choice(['ধার', 'শীর্ষবিন্দু', 'তল'])
    v = {'ধার': E_, 'শীর্ষবিন্দু': V_, 'তল': F_}[q]
    b.add(f"ভূমি {n} বাহুবিশিষ্ট বহুভুজ এমন একটি {kind[0]}-এর মোট {q} কয়টি?", v, setw(v, [E_, V_, F_, v + 1, v + 2]), f"শীর্ষ {V_}, ধার {E_}, তল {F_}; V − E + F = 2।", M)
def h_melt(b):
    r = R.randint(1, 4); R_ = r * R.randint(2, 4)
    n = (R_ // r) ** 3
    b.add(f"{R_} সেমি ব্যাসার্ধের একটি নিরেট গোলক গলিয়ে {r} সেমি ব্যাসার্ধের কয়টি গোলক তৈরি করা যাবে?", n, setw(n, [(R_ // r) ** 2, R_ // r, n * 2, n - 1]), f"({R_}/{r})³ = {n}।", H)
def h_pyr(b):
    a, h = 2 * R.randint(2, 8), R.randint(3, 15)
    v = F(a * a * h, 3)
    b.add(f"ভূমির বাহু {a} সেমি ও উচ্চতা {h} সেমি বিশিষ্ট বর্গাকার পিরামিডের আয়তন কত ঘন সেমি?", fr(v), setw(fr(v), [str(a * a * h), fr(v / 2), fr(F(a * h, 3)), fr(v + a)]), f"(1/3) × {a}² × {h} = {fr(v)}।", H)
def h_slant(b):
    a, h = R.choice([(6, 4), (10, 12), (16, 6), (14, 24), (18, 12), (24, 5), (30, 8)])
    l = math.isqrt((a // 2) ** 2 + h * h)
    if l * l != (a // 2) ** 2 + h * h: return
    S = 2 * a * l
    b.add(f"ভূমির বাহু {a} সেমি ও উচ্চতা {h} সেমি বিশিষ্ট বর্গাকার পিরামিডের পার্শ্বতলগুলোর মোট ক্ষেত্রফল কত বর্গ সেমি?", S, setw(S, [S + a * a, 4 * a * h, a * l, 2 * a * h]), f"হেলানো উচ্চতা √({a // 2}² + {h}²) = {l}; 4 × ½ × {a} × {l} = {S}।", H)
def h_cyl_cone(b):
    r, h = R.randint(2, 9), R.randint(2, 12)
    b.add(f"একই ভূমি ({r} সেমি ব্যাসার্ধ) ও একই উচ্চতা ({h} সেমি) বিশিষ্ট সিলিন্ডার ও শঙ্কুর আয়তনের অনুপাত কত?", "3 : 1", ["1 : 3", "2 : 1", "1 : 1"], "πr²h : (1/3)πr²h = 3 : 1।", H)
    a = R.randint(2, 9)
    b.add(f"একটি ঘনকের প্রতিটি ধার {a} সেমি থেকে দ্বিগুণ করা হলে আয়তন কত গুণ হবে?", "8 গুণ", ["2 গুণ", "4 গুণ", "6 গুণ"], "ধার দ্বিগুণ হলে আয়তন 2³ = 8 গুণ।", H)
def h_water(b):
    l, w = R.randint(5, 20), R.randint(4, 15); r = R.choice([1, 2, 3]); n = R.randint(1, 6)
    rise = F(4 * r ** 3 * n, 3 * l * w)
    pf = lambda q: (f"{q.numerator if q.numerator > 1 else ''}π/{q.denominator}" if q.denominator > 1 else f"{q.numerator}π")
    ok = pf(rise)
    b.add(f"{l} সেমি × {w} সেমি ভূমির একটি আয়তাকার পাত্রের পানিতে {r} সেমি ব্যাসার্ধের {n}টি লোহার গোলক সম্পূর্ণ ডোবালে পানির উচ্চতা কত সেমি বাড়বে?", ok, setw(ok, [pf(rise * 3), pf(rise / n) if n > 1 else pf(rise * 2), pf(F(4 * r * r * n, l * w)), pf(rise * 4)]), f"মোট আয়তন {n} × (4/3)π·{r}³; ÷ ({l} × {w})।", H)
p13 = run(None, R, fx13, [e_cube, e_cube_s, e_cuboid, e_cyl], [m_cuboid_s, m_diag, m_cone, m_cone_v, m_sphere, m_sphere_s, m_euler], [h_melt, h_pyr, h_slant, h_cyl_cone, h_water])
save('h13', p13)

# ---------------- 14 সম্ভাবনা ----------------
fx14 = [
 ("নিশ্চিত ঘটনার সম্ভাবনা কত?", "1", ["0", "1/2", "অসীম"], "নিশ্চিত ঘটনা অবশ্যই ঘটে।", E),
 ("অসম্ভব ঘটনার সম্ভাবনা কত?", "0", ["1", "1/2", "−1"], "কখনো ঘটে না।", E),
 ("কোনো ঘটনার সম্ভাবনা P হলে কোনটি সত্য?", "0 ≤ P ≤ 1", ["−1 ≤ P ≤ 1", "P > 1", "0 < P < 2"], "সম্ভাবনার মান 0 থেকে 1।", E),
 ("P(A) = 0.3 হলে A না ঘটার সম্ভাবনা কত?", "0.7", ["0.3", "1.3", "0"], "P(A′) = 1 − P(A)।", E),
 ("একটি মুদ্রা একবার নিক্ষেপ করলে নমুনাক্ষেত্র কোনটি?", "{H, T}", ["{H}", "{H, H, T}", "{1, 2}"], "হেড বা টেল।", E),
 ("দুটি ঘটনা একসাথে ঘটতে না পারলে তাদের কী বলে?", "পরস্পর বর্জনশীল ঘটনা", ["স্বাধীন ঘটনা", "নিশ্চিত ঘটনা", "পূরক ঘটনা"], "A ∩ B = ∅।", M),
 ("A ও B পরস্পর বর্জনশীল হলে P(A ∪ B) = কত?", "P(A) + P(B)", ["P(A)·P(B)", "P(A) − P(B)", "1"], "যোগ নিয়ম।", M),
 ("A ও B স্বাধীন ঘটনা হলে P(A ∩ B) = কত?", "P(A)·P(B)", ["P(A) + P(B)", "0", "P(A)/P(B)"], "গুণ নিয়ম।", M),
]
def e_die(b):
    kind = R.choice(['জোড়', 'বিজোড়', 'মৌলিক', '3-এর গুণিতক', '4-এর চেয়ে বড়', '5-এর চেয়ে ছোট', '6-এর গুণনীয়ক'])
    tests = {'জোড়': lambda n: n % 2 == 0, 'বিজোড়': lambda n: n % 2, 'মৌলিক': lambda n: n in (2, 3, 5), '3-এর গুণিতক': lambda n: n % 3 == 0, '4-এর চেয়ে বড়': lambda n: n > 4, '5-এর চেয়ে ছোট': lambda n: n < 5, '6-এর গুণনীয়ক': lambda n: 6 % n == 0}
    k = sum(1 for n in range(1, 7) if tests[kind](n)); v = F(k, 6)
    b.add(f"একটি ছক্কা একবার নিক্ষেপ করলে {kind} সংখ্যা আসার সম্ভাবনা কত?", fr(v), setw(fr(v), [fr(1 - v) if 1 - v != v else '1/3', fr(F(k, 12)), fr(F(1, 6)), fr(F(k + 1, 6))]), f"অনুকূল ফলাফল {k}টি; {k}/6 = {fr(v)}।", E)
def e_ball(b):
    r, g, w = R.randint(1, 10), R.randint(1, 10), R.randint(0, 8)
    t = r + g + w; col = R.choice([('লাল', r), ('সবুজ', g)] + ([('সাদা', w)] if w else []))
    v = F(col[1], t)
    b.add(f"একটি থলিতে {r}টি লাল, {g}টি সবুজ{f' ও {w}টি সাদা' if w else ''} বল আছে। দৈবভাবে একটি বল তুললে সেটি {col[0]} হওয়ার সম্ভাবনা কত?", fr(v), setw(fr(v), [fr(1 - v) if 1 - v != v else fr(v / 2), fr(F(col[1], t - col[1])) if t - col[1] else '1', fr(F(1, t)), fr(F(col[1] + 1, t))]), f"{col[1]}/{t} = {fr(v)}।", E)
def e_comp(b):
    p = F(R.randint(1, 19), 20)
    s = f"{float(p):g}"; c = f"{float(1 - p):g}"
    b.add(f"কোনো ঘটনা ঘটার সম্ভাবনা {s} হলে ঘটনাটি না ঘটার সম্ভাবনা কত?", c, setw(c, [s, f"{float(1 + p):g}", f"{float(p / 2):g}", '1']), f"1 − {s} = {c}।", E)
def e_coin2(b):
    k = R.choice([0, 1, 2]); n = 2
    v = F(math.comb(2, k), 4)
    txt = {0: 'কোনো হেড না', 1: 'ঠিক একটি হেড', 2: 'দুটিই হেড'}[k]
    b.add(f"দুটি মুদ্রা একসাথে নিক্ষেপ করলে {txt} আসার সম্ভাবনা কত?", fr(v), setw(fr(v), ['1/4', '1/2', '3/4', '1/3', '2/3']), f"নমুনাক্ষেত্র {{HH, HT, TH, TT}}; অনুকূল {math.comb(2, k)}টি।", E)
def m_two_dice(b):
    s = R.randint(2, 12); k = sum(1 for a in range(1, 7) for c in range(1, 7) if a + c == s); v = F(k, 36)
    b.add(f"দুটি ছক্কা একসাথে নিক্ষেপ করলে উঠে আসা সংখ্যার যোগফল {s} হওয়ার সম্ভাবনা কত?", fr(v), setw(fr(v), [fr(F(k + 1, 36)), fr(F(k, 12)), fr(F(1, 6)) if F(1, 6) != v else '5/36', fr(F(max(k - 1, 1), 36)) if F(max(k - 1, 1), 36) != v else '1/18']), f"অনুকূল {k}টি; {k}/36 = {fr(v)}।", M)
def m_cards(b):
    kind, k = R.choice([('টেক্কা', 4), ('লাল কার্ড', 26), ('হরতনের কার্ড', 13), ('রাজা', 4), ('ছবিযুক্ত কার্ড (J, Q, K)', 12), ('কালো রাজা', 2), ('ইস্কাপনের টেক্কা', 1), ('টেক্কা বা রাজা', 8)])
    v = F(k, 52)
    b.add(f"52টি তাসের প্যাকেট থেকে দৈবভাবে একটি তাস টানলে সেটি {kind} হওয়ার সম্ভাবনা কত?", fr(v), setw(fr(v), [fr(F(k, 26)) if k <= 26 else '1/4', fr(F(1, 52)) if k != 1 else '1/13', fr(1 - v), fr(F(k + 1, 52))]), f"{k}/52 = {fr(v)}।", M)
def m_coin3(b):
    k = R.randint(0, 3); kind = R.choice(['ঠিক', 'কমপক্ষে'])
    if kind == 'ঠিক': cnt = math.comb(3, k)
    else: cnt = sum(math.comb(3, i) for i in range(k, 4))
    if kind == 'কমপক্ষে' and k == 0: return
    v = F(cnt, 8)
    b.add(f"তিনটি মুদ্রা একসাথে নিক্ষেপ করলে {kind} {k}টি হেড আসার সম্ভাবনা কত?", fr(v), setw(fr(v), ['1/8', '3/8', '1/2', '7/8', '1/4', '5/8']), f"নমুনাক্ষেত্রে 8টি ফলাফল; অনুকূল {cnt}টি।", M)
def m_two_draw(b):
    r, g = R.randint(2, 8), R.randint(2, 8); t = r + g
    v = F(r, t) * F(r - 1, t - 1)
    b.add(f"একটি থলিতে {r}টি লাল ও {g}টি সবুজ বল আছে। প্রতিস্থাপন না করে পরপর দুটি বল তুললে দুটিই লাল হওয়ার সম্ভাবনা কত?", fr(v), setw(fr(v), [fr(F(r, t) ** 2), fr(F(r, t)), fr(F(r * g, t * (t - 1))), fr(v * 2)]), f"({r}/{t}) × ({r - 1}/{t - 1}) = {fr(v)}।", M)
def m_with_rep(b):
    r, g = R.randint(1, 8), R.randint(1, 8); t = r + g
    v = F(r, t) * F(g, t)
    b.add(f"একটি থলিতে {r}টি লাল ও {g}টি সবুজ বল আছে। প্রতিস্থাপনসহ পরপর দুটি বল তুললে প্রথমটি লাল ও দ্বিতীয়টি সবুজ হওয়ার সম্ভাবনা কত?", fr(v), setw(fr(v), [fr(F(r, t) * F(g, t - 1)), fr(2 * v), fr(F(r, t) + F(g, t)) if F(r, t) + F(g, t) != 1 else fr(v + F(1, t * t)), fr(F(r * g, (t + 1) ** 2))]), f"({r}/{t}) × ({g}/{t}) = {fr(v)}।", M)
def m_number(b):
    n = R.choice([20, 25, 30, 40, 50, 100]); d = R.choice([3, 4, 5, 6, 7])
    k = n // d; v = F(k, n)
    b.add(f"1 থেকে {n} পর্যন্ত সংখ্যা থেকে দৈবভাবে একটি নিলে সেটি {d}-এর গুণিতক হওয়ার সম্ভাবনা কত?", fr(v), setw(fr(v), [fr(F(k + 1, n)), fr(F(1, d)) if F(1, d) != v else fr(F(k - 1, n)), fr(1 - v), fr(F(k, n + 1))]), f"গুণিতক {k}টি; {k}/{n} = {fr(v)}।", M)
def h_atleast(b):
    n = R.randint(2, 5)
    v = 1 - F(1, 2 ** n)
    b.add(f"একটি মুদ্রা {n} বার নিক্ষেপ করলে কমপক্ষে একটি হেড আসার সম্ভাবনা কত?", fr(v), setw(fr(v), [fr(F(1, 2 ** n)), fr(F(n, 2 ** n)), '1/2', fr(1 - F(n, 2 ** n)) if 1 - F(n, 2 ** n) != v else fr(v - F(1, 2 ** n))]), f"1 − P(সব টেল) = 1 − 1/{2 ** n} = {fr(v)}।", H)
def h_union(b):
    pa, pb = F(R.randint(2, 7), 10), F(R.randint(2, 7), 10)
    pab = pa * pb
    v = pa + pb - pab
    s = lambda x: f"{float(x):g}"
    b.add(f"A ও B স্বাধীন ঘটনা; P(A) = {s(pa)} ও P(B) = {s(pb)} হলে P(A ∪ B) = কত?", s(v), setw(s(v), [s(pa + pb) if pa + pb <= 1 else s(v + F(1, 100)), s(pab), s(1 - pab), s(v - F(1, 10))]), f"{s(pa)} + {s(pb)} − {s(pab)} = {s(v)}।", H)
def h_dice_diff(b):
    kind = R.choice(['দুটি সংখ্যা সমান', 'যোগফল জোড়', 'গুণফল জোড়', 'যোগফল 7-এর বেশি', 'অন্তত একটিতে 6'])
    tests = {'দুটি সংখ্যা সমান': lambda a, c: a == c, 'যোগফল জোড়': lambda a, c: (a + c) % 2 == 0, 'গুণফল জোড়': lambda a, c: a * c % 2 == 0, 'যোগফল 7-এর বেশি': lambda a, c: a + c > 7, 'অন্তত একটিতে 6': lambda a, c: a == 6 or c == 6}
    k = sum(1 for a in range(1, 7) for c in range(1, 7) if tests[kind](a, c)); v = F(k, 36)
    b.add(f"দুটি ছক্কা একসাথে নিক্ষেপ করলে {kind} হওয়ার সম্ভাবনা কত?", fr(v), setw(fr(v), [fr(1 - v) if 1 - v != v else '1/4', fr(F(k, 72)), fr(F(k + 1, 36)), fr(F(1, 6)) if F(1, 6) != v else '5/36']), f"অনুকূল {k}টি; {k}/36 = {fr(v)}।", H)
def h_comb(b):
    r, g = R.randint(2, 7), R.randint(2, 7); t = r + g
    v = F(math.comb(r, 1) * math.comb(g, 1), math.comb(t, 2))
    b.add(f"একটি থলিতে {r}টি লাল ও {g}টি সবুজ বল আছে। একসাথে দুটি বল তুললে একটি লাল ও একটি সবুজ হওয়ার সম্ভাবনা কত?", fr(v), setw(fr(v), [fr(F(r * g, t * t)), fr(v / 2), fr(F(math.comb(r, 2), math.comb(t, 2))), fr(1 - v) if 1 - v != v else fr(v + F(1, t))]), f"({r} × {g})/{t}C2 = {fr(v)}।", H)
def h_find_n(b):
    r = R.randint(2, 10); p = R.choice([F(1, 2), F(1, 3), F(1, 4), F(2, 5), F(1, 5), F(3, 5)])
    t = F(r) / p
    if t.denominator > 1: return
    g = int(t) - r
    if g <= 0: return
    b.add(f"একটি থলিতে {r}টি লাল এবং কিছু সবুজ বল আছে। দৈবভাবে একটি বল তুললে তা লাল হওয়ার সম্ভাবনা {fr(p)} হলে সবুজ বল কয়টি?", g, setw(g, [int(t), g + 1, r, g - 1 if g > 1 else g + 2]), f"{r}/({r} + x) = {fr(p)} ⇒ x = {g}।", H)
p14 = run(None, R, fx14, [e_die, e_ball, e_comp, e_coin2], [m_two_dice, m_cards, m_coin3, m_two_draw, m_with_rep, m_number], [h_atleast, h_union, h_dice_diff, h_comb, h_find_n])
save('h14', p14)
