#!/usr/bin/env python3
"""অধ্যায় 9 ত্রিকোণমিতিক অনুপাত: 9.1 অনুপাত ও সম্পর্ক (অভেদ) · 9.2 নির্দিষ্ট কোণের অনুপাত (0°, 30°, 45°, 60°, 90°)"""
import random, pathlib, sys, re
from fractions import Fraction as F
import sympy as sp
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from mcqlib import run, save, E, M, H, fr, near, num

R = random.Random(2026103109)
def S(x):
    x = sp.radsimp(sp.together(x))
    if x == sp.zoo: return 'অসংজ্ঞায়িত'
    s = str(x)
    s = re.sub(r'sqrt\((\d+)\)', r'√\1', s).replace('*', '').replace('-', '−')
    return s
TRI = [(3, 4, 5), (5, 12, 13), (8, 15, 17), (7, 24, 25), (20, 21, 29), (9, 40, 41), (12, 35, 37)]
NAMES = ['sin', 'cos', 'tan', 'cosec', 'sec', 'cot']
def ratios(o, a, h):
    o, a, h = map(sp.Integer, (o, a, h))
    return {'sin': o / h, 'cos': a / h, 'tan': o / a, 'cosec': h / o, 'sec': h / a, 'cot': a / o}
fx91 = [
 ("sin²θ + cos²θ = কত?", "1", ["0", "2", "tanθ"], "মৌলিক অভেদ।", E),
 ("sec²θ − tan²θ = কত?", "1", ["0", "−1", "2"], "1 + tan²θ = sec²θ।", E),
 ("cosec²θ − cot²θ = কত?", "1", ["0", "−1", "2"], "1 + cot²θ = cosec²θ।", E),
 ("tanθ = কত?", "sinθ/cosθ", ["cosθ/sinθ", "1/sinθ", "sinθ × cosθ"], "সংজ্ঞা অনুযায়ী।", E),
 ("cosecθ এর বিপরীত অনুপাত কোনটি?", "sinθ", ["cosθ", "tanθ", "secθ"], "cosecθ = 1/sinθ।", E),
 ("secθ এর বিপরীত অনুপাত কোনটি?", "cosθ", ["sinθ", "cotθ", "tanθ"], "secθ = 1/cosθ।", E),
 ("tanθ × cotθ = কত?", "1", ["0", "tan²θ", "sinθ"], "পরস্পর বিপরীত।", E),
 ("সমকোণী ত্রিভুজে sinθ এর মান সর্বদা কোন সীমায়? (θ সূক্ষ্মকোণ)", "0 < sinθ < 1", ["sinθ > 1", "sinθ < 0", "sinθ = 1"], "লম্ব < অতিভুজ।", M),
 ("(1 − sin²θ)/cos²θ = কত?", "1", ["0", "tan²θ", "sec²θ"], "1 − sin²θ = cos²θ।", M),
 ("cosθ × tanθ = কত?", "sinθ", ["cosθ", "1", "secθ"], "cosθ × sinθ/cosθ।", M),
 ("sec²θ + cosec²θ = কত?", "sec²θ cosec²θ", ["1", "2", "tan²θ + cot²θ"], "1/cos² + 1/sin² = (sin² + cos²)/(sin²cos²)।", H),
 ("(1 + tan²θ)(1 − sin²θ) = কত?", "1", ["0", "sec²θ", "cos²θ"], "sec²θ × cos²θ = 1।", H),
 ("(secθ + tanθ)(secθ − tanθ) = কত?", "1", ["0", "2secθ", "sec²θ + tan²θ"], "sec²θ − tan²θ = 1।", H),
 ("(cosecθ − cotθ)(cosecθ + cotθ) = কত?", "1", ["0", "2cotθ", "−1"], "cosec²θ − cot²θ = 1।", H),
]
def e_side(b):
    o, a, h = R.choice(TRI); f = R.choice(['sin', 'cos', 'tan'])
    v = ratios(o, a, h)[f]; others = [S(ratios(o, a, h)[g]) for g in NAMES if g != f]
    b.add(f"সমকোণী ত্রিভুজ ABC-এ ∠B = 90°, AB = {a}, BC = {o}, AC = {h}। ∠A = θ হলে {f}θ = কত?", S(v), [x for x in others if x != S(v)][:3], f"{f}θ = {'লম্ব/অতিভুজ' if f == 'sin' else 'ভূমি/অতিভুজ' if f == 'cos' else 'লম্ব/ভূমি'} = {S(v)}।", E)
def e_recip(b):
    o, a, h = R.choice(TRI); f, g = R.choice([('sin', 'cosec'), ('cos', 'sec'), ('tan', 'cot')])
    if R.random() < .5: f, g = g, f
    v = ratios(o, a, h)
    b.add(f"{f}θ = {S(v[f])} হলে {g}θ = কত?", S(v[g]), [S(v[f]), S(-v[g]), S(v[g] + 1)], f"{g}θ = 1/{f}θ।", E)
def m_fromsin(b):
    o, a, h = R.choice(TRI); f, g = R.choice([('sin', 'cos'), ('cos', 'sin'), ('sin', 'tan'), ('cos', 'tan'), ('tan', 'sin'), ('tan', 'cos'), ('sin', 'sec'), ('cos', 'cosec'), ('tan', 'sec')])
    v = ratios(o, a, h)
    b.add(f"θ সূক্ষ্মকোণ এবং {f}θ = {S(v[f])} হলে {g}θ = কত?", S(v[g]), list(dict.fromkeys(S(v[x]) for x in NAMES if x not in (f, g) and S(v[x]) != S(v[g])))[:3], f"ত্রিভুজের বাহু {o}, {a}, {h} ধরে {g}θ = {S(v[g])}।", M)
def m_expr(b):
    o, a, h = R.choice(TRI); v = ratios(o, a, h)
    kind = R.choice([0, 1, 2, 3])
    if kind == 0: q, val = f"tanθ = {S(v['tan'])} হলে (sinθ + cosθ) = কত?", v['sin'] + v['cos']
    elif kind == 1: q, val = f"sinθ = {S(v['sin'])} হলে (1 − cos²θ) = কত?", v['sin'] ** 2
    elif kind == 2: q, val = f"cosθ = {S(v['cos'])} হলে (secθ − tanθ) = কত?", v['sec'] - v['tan']
    else: q, val = f"tanθ = {S(v['tan'])} হলে (sinθ × cosθ) = কত?", v['sin'] * v['cos']
    b.add(q, S(val), [S(val + 1), S(val * 2), S(1 - val) if S(1 - val) != S(val) else S(val + 2)], f"বাহু {o}, {a}, {h} ধরে হিসাব করে {S(val)}।", M)
def m_sq(b):
    o, a, h = R.choice(TRI); f = R.choice(['sin', 'cos', 'tan'])
    v = ratios(o, a, h)
    g = {'sin': 'cos', 'cos': 'sin', 'tan': 'sec'}[f]; val = v[g] ** 2
    b.add(f"{f}θ = {S(v[f])} হলে {g}²θ = কত?", S(val), [S(v[f] ** 2), S(val + 1) if g != 'sec' else S(val - 1), S(v[g])], f"অভেদ ব্যবহার করে {g}²θ = {S(val)}।", M)
def h_ratio_expr(b):
    o, a, h = R.choice(TRI); v = ratios(o, a, h)
    val = (v['sin'] + v['cos']) / (v['sin'] - v['cos'])
    if o == a: return
    b.add(f"tanθ = {S(v['tan'])} হলে (sinθ + cosθ)/(sinθ − cosθ) = কত?", S(val), [S(-val), S((v['tan'] - 1) / (v['tan'] + 1)), S(val + 1)], f"লব ও হরকে cosθ দিয়ে ভাগ: (tanθ + 1)/(tanθ − 1) = {S(val)}।", H)
def h_k(b):
    p, q = R.choice([(3, 4), (5, 12), (8, 15), (7, 24), (1, 1), (2, 3), (1, 2)])
    val = sp.Rational(p, q)
    # p tanθ = q ⇒ ...
    t = sp.Rational(q, p)
    expr = (p * sp.Integer(1) * t - 1) / (p * t + 1) if False else None
    s_ = t / sp.sqrt(1 + t ** 2); c_ = 1 / sp.sqrt(1 + t ** 2)
    v = (s_ - c_) / (s_ + c_)
    b.add(f"{p}tanθ = {q} হলে (sinθ − cosθ)/(sinθ + cosθ) = কত?", S(v), [S(-v) if v != 0 else '1', S((s_ + c_) / (s_ - c_)) if s_ != c_ else '2', S(v + 1)], f"tanθ = {S(t)}; (tanθ − 1)/(tanθ + 1) = {S(v)}।", H)
def h_sum(b):
    o, a, h = R.choice(TRI); v = ratios(o, a, h)
    val = v['sec'] + v['tan']
    b.add(f"sinθ = {S(v['sin'])} হলে secθ + tanθ = কত?", S(val), [S(v['sec'] - v['tan']), S(val + 1), S(v['cosec'] + v['cot'])], f"secθ = {S(v['sec'])}, tanθ = {S(v['tan'])}।", H)
I91 = run('9.1', R, fx91, [e_side, e_recip], [m_fromsin, m_expr, m_sq], [h_ratio_expr, h_k, h_sum], caps=(15, 18, 8))

A = [0, 30, 45, 60, 90]
def tv(f, d):
    r = sp.rad(d) if False else sp.pi * d / 180
    return {'sin': sp.sin(r), 'cos': sp.cos(r), 'tan': sp.tan(r), 'cot': (sp.cot(r) if d else sp.zoo), 'sec': sp.sec(r), 'cosec': (1 / sp.sin(r) if d else sp.zoo)}[f]
fx92 = [
 ("sin 30° = কত?", "1/2", ["√3/2", "1/√2", "1"], "আদর্শ মান।", E),
 ("cos 60° = কত?", "1/2", ["√3/2", "0", "1"], "আদর্শ মান।", E),
 ("tan 45° = কত?", "1", ["0", "√3", "1/√3"], "আদর্শ মান।", E),
 ("sin 90° = কত?", "1", ["0", "1/2", "অসংজ্ঞায়িত"], "আদর্শ মান।", E),
 ("tan 90° এর মান কেমন?", "অসংজ্ঞায়িত", ["0", "1", "√3"], "cos 90° = 0।", E),
 ("θ এর মান 0° থেকে 90° পর্যন্ত বাড়লে sinθ এর মান কেমন হয়?", "0 থেকে 1 পর্যন্ত বাড়ে", ["1 থেকে 0 পর্যন্ত কমে", "অপরিবর্তিত থাকে", "অসীম পর্যন্ত বাড়ে"], "sin 0° = 0, sin 90° = 1।", M),
 ("sin(90° − θ) = কত?", "cosθ", ["sinθ", "tanθ", "−cosθ"], "পূরক কোণের অনুপাত।", M),
 ("tan(90° − θ) = কত?", "cotθ", ["tanθ", "secθ", "−tanθ"], "পূরক কোণের অনুপাত।", M),
]
def fa(f, d): return f"{f} {d}°"
def e_val(b):
    f = R.choice(['sin', 'cos', 'tan', 'sec', 'cosec', 'cot']); d = R.choice(A)
    v = tv(f, d)
    if v == sp.zoo: return
    pool = list(dict.fromkeys(S(tv(f, x)) for x in A if tv(f, x) != sp.zoo))
    pool = [p for p in pool if p != S(v)] + ['2', '√2', '√3/2', '1/2']
    b.add(f"{fa(f, d)} = কত?", S(v), [p for p in dict.fromkeys(pool) if p != S(v)][:3], "আদর্শ কোণের মান।", E)
def e_comp(b):
    d = R.randint(5, 85); f, g = R.choice([('sin', 'cos'), ('cos', 'sin'), ('tan', 'cot'), ('sec', 'cosec')])
    if d == 45: return
    b.add(f"{f} {d}° = {g} x হলে x = কত? (x সূক্ষ্মকোণ)", f"{90 - d}°", [f"{d}°", f"{180 - d}°", f"{abs(90 - 2 * d) if abs(90 - 2 * d) not in (d, 90 - d) and d != 0 else d + 10}°"], f"{f} {d}° = {g}(90° − {d}°)।", E)
def m_expr(b):
    f1, f2 = R.sample(['sin', 'cos', 'tan'], 2); d1, d2 = R.choice([30, 45, 60]), R.choice([30, 45, 60])
    op = R.choice(['+', '×', '−'])
    v1, v2 = tv(f1, d1), tv(f2, d2)
    v = {'+': v1 + v2, '×': v1 * v2, '−': v1 - v2}[op]
    b.add(f"{fa(f1, d1)} {op} {fa(f2, d2)} = কত?", S(v), [S(v1 - v2 if op != '−' else v1 + v2), S(v + sp.Rational(1, 2)), S(v1 * v2 if op != '×' else v1 + v2)], f"{S(v1)} {op} {S(v2)} = {S(v)}।", M)
def m_sq(b):
    f = R.choice(['sin', 'cos', 'tan']); d = R.choice([30, 45, 60])
    k = R.choice([1, 2, 3, 4])
    v = k * tv(f, d) ** 2
    b.add(f"{'' if k == 1 else k}{f}²{d}° = কত?", S(v), [S(k * tv(f, d)), S(v + 1), S(k * tv(f, 90 - d if f != 'tan' else d) ** 2 + sp.Rational(1, 4)) ], f"{f} {d}° = {S(tv(f, d))}; বর্গ করে {k} দিয়ে গুণ।", M)
def m_solve(b):
    f = R.choice(['sin', 'cos', 'tan']); d = R.choice([30, 45, 60])
    v = tv(f, d)
    b.add(f"{f}θ = {S(v)} হলে θ = কত? (θ সূক্ষ্মকোণ)", f"{d}°", [f"{x}°" for x in [30, 45, 60, 90] if x != d][:3], f"{f} {d}° = {S(v)}।", M)
def m_two(b):
    f = R.choice(['sin', 'cos']); d = R.choice([15, 20, 30, 45, 22.5])
    d2 = d * 2
    v = tv(f, d2)
    dd = fr(F(str(d)))
    b.add(f"2{f}θ এর বদলে {f} 2θ = {S(v)} হলে θ = কত? (2θ সূক্ষ্মকোণ)" if False else f"{f} 2θ = {S(v)} হলে θ = কত? (θ সূক্ষ্মকোণ)", f"{dd}°", [f"{fr(F(str(d2)))}°", f"{fr(F(str(d)) + 15)}°", f"{fr(F(str(d)) / 2)}°"], f"2θ = {fr(F(str(d2)))}° ⇒ θ = {dd}°।", M)
def h_big(b):
    k = R.choice([0, 1, 2, 3, 4])
    exprs = [("sin²60° + cos²60°", 1), ("tan²60° − sec²60°", -1), ("2sin30°cos30°", sp.sqrt(3) / 2), ("(1 − tan²30°)/(1 + tan²30°)", sp.Rational(1, 2)), ("cos²30° − sin²30°", sp.Rational(1, 2)), ("2tan30°/(1 − tan²30°)", sp.sqrt(3)), ("sin60°cos30° + cos60°sin30°", 1), ("cos60°cos30° − sin60°sin30°", 0), ("sec²45° − tan²45°", 1), ("4cos²60° + 3sec²30° − 2tan²45°", 3), ("tan45° × tan60° × tan30°", 1), ("(sin30° + cos60°)/tan45°", 1), ("3tan²30° + cot²45°", 2), ("cosec²45° − cot²45°", 1)]
    q, v = R.choice(exprs)
    b.add(f"{q} = কত?", S(v), [S(v + 1), S(v - sp.Rational(1, 2)), S(2 * v) if 2 * v != v else '2'], f"আদর্শ মান বসিয়ে {S(v)}।", H)
def h_solve2(b):
    d = R.choice([30, 45, 60])
    f = R.choice(['sin', 'cos', 'tan'])
    k = R.choice([2, 3])
    v = tv(f, d)
    rhs = k * v ** 2
    b.add(f"{k}{f}²θ = {S(rhs)} হলে θ = কত? (θ সূক্ষ্মকোণ)", f"{d}°", [f"{x}°" for x in [30, 45, 60, 90] if x != d][:3], f"{f}²θ = {S(v ** 2)} ⇒ {f}θ = {S(v)} ⇒ θ = {d}°।", H)
def h_ab(b):
    a_, c_ = R.choice([(60, 30), (45, 15), (30, 30), (60, 0), (75, 15), (50, 10), (40, 20), (55, 5)])
    # sin(A + B) = 1, cos(A − B) = ... style
    A_, B_ = a_, c_
    s, d_ = A_ + B_, A_ - B_
    if s not in (30, 45, 60, 90) or d_ not in (0, 30, 45, 60): return
    fs = 'sin' if s in (30, 60, 90) else 'tan'; fd = 'cos' if d_ in (0, 30, 60) else 'tan'
    b.add(f"{fs}(A + B) = {S(tv(fs, s))} এবং {fd}(A − B) = {S(tv(fd, d_))} হলে A = কত? (A + B ও A − B সূক্ষ্ম বা সমকোণ)", f"{A_}°", [f"{B_}°", f"{s}°", f"{A_ + 15}°"] if B_ != A_ + 15 else [f"{B_ + 5}°", f"{s}°", f"{A_ + 10}°"], f"A + B = {s}°, A − B = {d_}° ⇒ A = {A_}°।", H)
I92 = run('9.2', R, fx92, [e_val, e_comp], [m_expr, m_sq, m_solve, m_two], [h_big, h_solve2, h_ab], caps=(30, 20, 14))
save(9, I91 + I92)
