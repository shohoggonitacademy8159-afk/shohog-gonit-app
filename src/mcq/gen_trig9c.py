#!/usr/bin/env python3
"""নবম-দশম সাধারণ গণিত অনুশীলনী 9.1 — ২য় সেট (ত্রিকোণমিতিক অভেদ ও মান নির্ণয়): নিজস্ব নতুন প্রশ্ন,
নিজের ভাষা ও ব্যাখ্যা। প্রতিটি অভেদ/মান sympy দিয়ে যাচাই। ফলাফল: src/mcq/ch9c.json"""
import json, random, pathlib
import sympy as sp

R = random.Random(9102)
OUT = []
t = sp.symbols('t')
S, C, Tn, Ct, Sc, Cs = sp.sin(t), sp.cos(t), sp.tan(t), sp.cot(t), sp.sec(t), sp.csc(t)
same = lambda a, b: sp.simplify(sp.expand_trig(a - b)) == 0 or abs(float((a - b).subs(t, 0.731))) < 1e-12


def add(q, right, wrong, e, lv, ok=True):
    assert ok, q
    ws = [w for w in dict.fromkeys(wrong) if w != right]
    assert len(ws) >= 3, (q, right, wrong)
    o = [right] + ws[:3]; R.shuffle(o)
    OUT.append({'q': q, 'o': o, 'a': o.index(right), 'e': e, 'lv': lv, 'ex': '9.1'})


def multi(stem, st, ok, e, lv):
    combos = ['i ও ii', 'i ও iii', 'ii ও iii', 'i, ii ও iii']
    OUT.append({'q': f'{stem}\ni. {st[0]}\nii. {st[1]}\niii. {st[2]}\nনিচের কোনটি সঠিক?', 'o': combos,
                'a': {(0, 1): 0, (0, 2): 1, (1, 2): 2, (0, 1, 2): 3}[ok], 'e': e, 'lv': lv, 'ex': '9.1'})


# ---- অভেদ সরলীকরণ (প্রতিটি সংখ্যাগতভাবে যাচাই) ----
add('(1 + cosθ)(1 − cosθ)(1 + cot²θ) = কত?', '1', ['sin²θ', 'cosec²θ', '0'], '(1 − cos²θ)·cosec²θ = sin²θ·cosec²θ = 1', 'মধ্যম', same((1 + C) * (1 - C) * (1 + Ct**2), 1))
add('sinθ/(1 + cosθ) + (1 + cosθ)/sinθ = কত?', '2cosecθ', ['2secθ', '2sinθ', '1'], 'লব = sin²θ + 1 + 2cosθ + cos²θ = 2(1 + cosθ); হর = sinθ(1 + cosθ) ⇒ 2/sinθ', 'কঠিন', same(S / (1 + C) + (1 + C) / S, 2 * Cs))
add('(sinθ + cosθ)² + (sinθ − cosθ)² = কত?', '2', ['1', '0', '4sinθcosθ'], 'দুটি বর্গ যোগ করলে 2(sin²θ + cos²θ) = 2', 'সহজ', same((S + C)**2 + (S - C)**2, 2))
add('sec⁴θ − sec²θ নিচের কোনটির সমান?', 'tan⁴θ + tan²θ', ['tan⁴θ − tan²θ', '1', 'sec²θ·cot²θ'], 'sec²θ(sec²θ − 1) = (1 + tan²θ)tan²θ', 'কঠিন', same(Sc**4 - Sc**2, Tn**4 + Tn**2))
add('cosθ/(1 − tanθ) + sinθ/(1 − cotθ) = কত?', 'sinθ + cosθ', ['sinθ − cosθ', '1', 'secθ + cosecθ'], 'প্রথমটি = cos²θ/(cosθ − sinθ), দ্বিতীয়টি = sin²θ/(sinθ − cosθ); যোগফল = (cos²θ − sin²θ)/(cosθ − sinθ)', 'কঠিন', same(C / (1 - Tn) + S / (1 - Ct), S + C))
add('(cosecθ − sinθ)(secθ − cosθ) = কত?', 'sinθ·cosθ', ['1', 'tanθ', 'secθ·cosecθ'], '(cos²θ/sinθ)·(sin²θ/cosθ) = sinθcosθ', 'কঠিন', same((Cs - S) * (Sc - C), S * C))
add('(1 − sinθ)/(1 + sinθ) নিচের কোনটির সমান?', '(secθ − tanθ)²', ['(secθ + tanθ)²', 'sec²θ − tan²θ', '(1 − tanθ)²'], 'লব-হরকে (1 − sinθ) দিয়ে গুণ: (1 − sinθ)²/cos²θ = (secθ − tanθ)²', 'কঠিন', same((1 - S) / (1 + S), (Sc - Tn)**2))
add('1/(1 + sin²θ) + 1/(1 + cosec²θ) = কত?', '1', ['2', 'sin²θ', '1/2'], 'দ্বিতীয় পদে লব-হরকে sin²θ দিয়ে গুণ: sin²θ/(sin²θ + 1); যোগফল = (1 + sin²θ)/(1 + sin²θ) = 1', 'মধ্যম', same(1 / (1 + S**2) + 1 / (1 + Cs**2), 1))
add('tan²θ − sin²θ নিচের কোনটির সমান?', 'tan²θ·sin²θ', ['cos²θ', 'tan²θ·cos²θ', '1'], 'sin²θ(1/cos²θ − 1) = sin²θ·tan²θ', 'মধ্যম', same(Tn**2 - S**2, Tn**2 * S**2))
add('cot²θ − 1/sin²θ = কত?', '−1', ['1', '0', 'cos²θ'], 'cot²θ − cosec²θ = −1', 'সহজ', same(Ct**2 - 1 / S**2, -1))
add('sin⁶θ + cos⁶θ নিচের কোনটির সমান?', '1 − 3sin²θcos²θ', ['1 − 2sin²θcos²θ', '1', '1 + 3sin²θcos²θ'], 'a³ + b³ = (a + b)³ − 3ab(a + b), যেখানে a = sin²θ, b = cos²θ', 'কঠিন', same(S**6 + C**6, 1 - 3 * S**2 * C**2))
add('cos²θ(1 + tan²θ) + sin²θ(1 + cot²θ) = কত?', '2', ['1', '0', 'sec²θ + cosec²θ'], 'cos²θ·sec²θ + sin²θ·cosec²θ = 1 + 1', 'সহজ', same(C**2 * (1 + Tn**2) + S**2 * (1 + Ct**2), 2))
add('(secθ + tanθ)(1 − sinθ) = কত?', 'cosθ', ['sinθ', '1', 'secθ'], '((1 + sinθ)/cosθ)(1 − sinθ) = cos²θ/cosθ = cosθ', 'মধ্যম', same((Sc + Tn) * (1 - S), C))

# ---- মান নির্ণয় (নিজস্ব সংখ্যা) ----
th = sp.pi / 4
add('θ সূক্ষ্মকোণ এবং sinθ − cosθ = 0 হলে sin⁴θ + cos⁴θ = কত?', '1/2', ['1', '1/4', '2'], 'sinθ = cosθ ⇒ θ = 45° ⇒ (1/√2)⁴ × 2 = 1/2', 'মধ্যম', sp.nsimplify(sp.sin(th)**4 + sp.cos(th)**4) == sp.Rational(1, 2))
add('sinθ·cosθ = 1/4 হলে (sinθ + cosθ)² = কত?', '3/2', ['1/2', '5/4', '1/16'], '1 + 2sinθcosθ = 1 + 1/2 = 3/2', 'মধ্যম')
add('tanθ + cotθ = 2 হলে tan²θ + cot²θ = কত?', '2', ['4', '0', '1'], '(tanθ + cotθ)² = tan²θ + cot²θ + 2 ⇒ 4 − 2 = 2', 'মধ্যম')
s, c = sp.Rational(12, 13), sp.Rational(5, 13)
add('θ সূক্ষ্মকোণ এবং secθ = 13/5 হলে (2sinθ − 3cosθ)/(4sinθ − 9cosθ) = কত?', '3', ['1/3', '9/13', '−3'], 'cosθ = 5/13, sinθ = 12/13 ⇒ (24 − 15)/(48 − 45) = 9/3 = 3', 'কঠিন', (2 * s - 3 * c) / (4 * s - 9 * c) == 3)
s, c = sp.Rational(4, 5), sp.Rational(3, 5)
add('θ সূক্ষ্মকোণ এবং 5cosθ = 3 হলে (cosecθ − cotθ)/(cosecθ + cotθ) = কত?', '1/4', ['4', '1/2', '2'], 'sinθ = 4/5 ⇒ cosecθ = 5/4, cotθ = 3/4 ⇒ (1/2)/(2) = 1/4', 'কঠিন', (1 / s - c / s) / (1 / s + c / s) == sp.Rational(1, 4))
add('θ সূক্ষ্মকোণ এবং 3tanθ = √3 হলে sinθ·secθ = কত?', '1/√3', ['√3', '1/2', '√3/2'], 'sinθ·secθ = sinθ/cosθ = tanθ = √3/3 = 1/√3', 'মধ্যম')
add('θ সূক্ষ্মকোণ এবং cosecθ = 2 হলে cot²θ + cosec²θ = কত?', '7', ['5', '3', '4'], 'cot²θ = cosec²θ − 1 = 3 ⇒ 3 + 4 = 7', 'মধ্যম')

multi('যেকোনো সূক্ষ্মকোণ θ এর জন্য—', ['1 + tan²θ = sec²θ', 'cosec²θ − 1 = cot²θ', 'sinθ·secθ = cotθ'], (0, 1), 'sinθ·secθ = sinθ/cosθ = tanθ, তাই iii ভুল।', 'মধ্যম')
multi('θ সূক্ষ্মকোণ এবং secθ = 5/4 হলে—', ['cosθ = 4/5', 'tanθ = 3/4', 'sinθ·secθ = 3/4'], (0, 1, 2), 'sinθ = 3/5; sinθ·secθ = tanθ = 3/4 — তিনটিই সঠিক।', 'মধ্যম')
multi('(1 + sinθ)(1 − sinθ) এর মান—', ['cos²θ', '1/sec²θ', 'sin²θ − 1'], (0, 1), '1 − sin²θ = cos²θ = 1/sec²θ; sin²θ − 1 = −cos²θ', 'মধ্যম')

pathlib.Path(__file__).with_name('ch9c.json').write_text(json.dumps(OUT, ensure_ascii=False, indent=1), encoding='utf-8')
print(len(OUT), 'questions')
