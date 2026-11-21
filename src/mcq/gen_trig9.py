#!/usr/bin/env python3
"""নবম-দশম সাধারণ গণিত অধ্যায় ৯, অনুশীলনী 9.1 (ত্রিকোণমিতিক অনুপাত): নিজস্ব নতুন প্রশ্ন — নিজের ত্রিভুজ ও সংখ্যা,
নিজের ভাষা ও ব্যাখ্যা। প্রতিটি উত্তর sympy দিয়ে যাচাই করা হয়। ফলাফল: src/mcq/ch9b.json"""
import json, random, pathlib
import sympy as sp

R = random.Random(9101)
OUT = []
t = sp.symbols('t', positive=True)


def add(q, right, wrong, e, lv, check=None):
    if check is not None:
        assert check, q
    ws = [w for w in dict.fromkeys(wrong) if w != right]
    assert len(ws) >= 3, (q, right, wrong)
    o = [right] + ws[:3]; R.shuffle(o)
    OUT.append({'q': q, 'o': o, 'a': o.index(right), 'e': e, 'lv': lv, 'ex': '9.1'})


def multi(stem, st, ok, e, lv):
    combos = ['i ও ii', 'i ও iii', 'ii ও iii', 'i, ii ও iii']
    OUT.append({'q': f'{stem}\ni. {st[0]}\nii. {st[1]}\niii. {st[2]}\nনিচের কোনটি সঠিক?', 'o': combos,
                'a': {(0, 1): 0, (0, 2): 1, (1, 2): 2, (0, 1, 2): 3}[ok], 'e': e, 'lv': lv, 'ex': '9.1'})


eq = lambda a, b: sp.simplify(sp.nsimplify(a) - sp.nsimplify(b)) == 0

# ত্রিভুজ ১: ∠C = 90°, BC = 7, AC = 24 ⇒ AB = 25; θ = ∠A
AB = sp.sqrt(7**2 + 24**2); assert AB == 25
T1 = 'সমকোণী ত্রিভুজ ABC-এ ∠C = 90°, BC = 7 সে.মি., AC = 24 সে.মি. এবং ∠A = θ।'
add(f'{T1} AB = কত সে.মি.?', '25', ['31', '17', '√527'], 'AB² = BC² + AC² = 49 + 576 = 625 ⇒ AB = 25', 'সহজ', AB == 25)
add(f'{T1} sinθ = কত?', '7/25', ['24/25', '7/24', '25/7'], 'sinθ = লম্ব/অতিভুজ = BC/AB = 7/25', 'সহজ')
add(f'{T1} cotθ = কত?', '24/7', ['7/24', '25/24', '24/25'], 'cotθ = ভূমি/লম্ব = AC/BC = 24/7', 'সহজ')
add(f'{T1} cosecθ + cotθ = কত?', '7', ['49/25', '1/7', '31/7'], 'cosecθ = 25/7, cotθ = 24/7; যোগফল = 49/7 = 7', 'মধ্যম', sp.Rational(25, 7) + sp.Rational(24, 7) == 7)
multi(T1, ['cosθ = 24/25', 'tanθ = 7/24', 'secθ = 25/7'], (0, 1), 'secθ = অতিভুজ/ভূমি = 25/24, তাই iii ভুল।', 'মধ্যম')

# ত্রিভুজ ২: ∠Q = 90°, PQ = 9, QR = 40 ⇒ PR = 41
T2 = 'সমকোণী ত্রিভুজ PQR-এ ∠Q = 90°, PQ = 9 একক এবং QR = 40 একক।'
assert sp.sqrt(81 + 1600) == 41
add(f'{T2} PR = কত একক?', '41', ['49', '31', '39'], 'PR = √(9² + 40²) = √1681 = 41', 'সহজ')
add(f'{T2} sec R = কত?', '41/40', ['41/9', '40/41', '9/40'], '∠R এর সন্নিহিত বাহু QR = 40, অতিভুজ PR = 41 ⇒ sec R = 41/40', 'মধ্যম')
add(f'{T2} tan P = কত?', '40/9', ['9/40', '40/41', '41/9'], '∠P এর বিপরীত বাহু QR = 40, সন্নিহিত বাহু PQ = 9 ⇒ tan P = 40/9', 'মধ্যম')
add(f'{T2} sin P + cos R = কত?', '80/41', ['49/41', '1', '81/41'], 'sin P = 40/41, cos R = 40/41 ⇒ যোগফল 80/41 (P ও R পূরক কোণ)', 'কঠিন')

# ত্রিভুজ ৩: ∠B = 90°, AB = 6, AC = 10 ⇒ BC = 8
add('ΔABC-এ ∠B = 90°, AB = 6 সে.মি. এবং AC = 10 সে.মি. হলে cot C = কত?', '4/3', ['3/4', '3/5', '5/4'], 'BC = √(100 − 36) = 8; ∠C এর জন্য ভূমি BC = 8, লম্ব AB = 6 ⇒ cot C = 8/6 = 4/3', 'মধ্যম', sp.sqrt(100 - 36) == 8)

# একটি অনুপাত থেকে অন্যটি (নিজস্ব সংখ্যা)
s = sp.Rational(20, 29); c = sp.sqrt(1 - s**2)
add('θ সূক্ষ্মকোণ এবং sinθ = 20/29 হলে tanθ = কত?', '20/21', ['21/20', '21/29', '29/21'], 'cosθ = √(1 − 400/841) = 21/29 ⇒ tanθ = 20/21', 'মধ্যম', eq(s / c, sp.Rational(20, 21)))
add('θ সূক্ষ্মকোণ এবং cosθ = 21/29 হলে sin²θ − cos²θ = কত?', '−41/841', ['41/841', '1', '−1/29'], 'sinθ = 20/29; (400 − 441)/841 = −41/841', 'কঠিন', eq(s**2 - c**2, sp.Rational(-41, 841)))
s = sp.Rational(2, 3)
add('θ সূক্ষ্মকোণ এবং sinθ = 2/3 হলে cosθ = কত?', '√5/3', ['1/3', '5/9', '√13/3'], 'cosθ = √(1 − 4/9) = √5/3', 'সহজ', eq(sp.sqrt(1 - s**2), sp.sqrt(5) / 3))
add('θ সূক্ষ্মকোণ এবং secθ = 3 হলে tanθ = কত?', '2√2', ['√2', '8', '1/3'], 'tan²θ = sec²θ − 1 = 8 ⇒ tanθ = 2√2', 'মধ্যম', eq(sp.sqrt(9 - 1), 2 * sp.sqrt(2)))
add('cotθ = 2 হলে cosec²θ = কত?', '5', ['3', '4', '5/4'], 'cosec²θ = 1 + cot²θ = 1 + 4 = 5', 'সহজ')
add('θ সূক্ষ্মকোণ এবং cosθ = 0.6 হলে tanθ = কত?', '4/3', ['3/4', '0.8', '5/3'], 'cosθ = 3/5 ⇒ sinθ = 4/5 ⇒ tanθ = 4/3', 'সহজ')
add('θ সূক্ষ্মকোণ এবং 4tanθ = 3 হলে sinθ + cosθ = কত?', '7/5', ['1', '7/4', '12/25'], 'tanθ = 3/4 ⇒ sinθ = 3/5, cosθ = 4/5 ⇒ যোগফল 7/5', 'মধ্যম')
st, ct = sp.Rational(4, 5), sp.Rational(3, 5)
add('tanθ = 4/3 (θ সূক্ষ্মকোণ) হলে (2sinθ − cosθ)/(2sinθ + cosθ) = কত?', '5/11', ['11/5', '1/3', '5/7'], 'sinθ = 4/5, cosθ = 3/5 ⇒ (8/5 − 3/5)/(8/5 + 3/5) = 5/11', 'কঠিন', eq((2 * st - ct) / (2 * st + ct), sp.Rational(5, 11)))
add('θ সূক্ষ্মকোণ এবং cosθ = p/q হলে cotθ = কত?', 'p/√(q² − p²)', ['√(q² − p²)/p', 'q/√(q² − p²)', '√(q² − p²)/q'], 'ভূমি p, অতিভুজ q ⇒ লম্ব √(q² − p²) ⇒ cotθ = ভূমি/লম্ব', 'মধ্যম')

# সম্পর্ক ও অভেদ
add('secθ − tanθ = 1/3 হলে secθ + tanθ = কত?', '3', ['1/3', '2/3', '9'], 'sec²θ − tan²θ = 1 ⇒ (secθ + tanθ)(secθ − tanθ) = 1 ⇒ secθ + tanθ = 3', 'মধ্যম')
add('cosecθ − cotθ = 1/2 হলে cosecθ = কত?', '5/4', ['3/4', '2', '5/2'], 'cosecθ + cotθ = 2; দুটি যোগ করে 2cosecθ = 5/2 ⇒ cosecθ = 5/4', 'কঠিন')
add('(secθ − cosθ)/tanθ এর সরল মান কোনটি?', 'sinθ', ['cosθ', 'tanθ', '1'], '(1/cosθ − cosθ) ÷ (sinθ/cosθ) = (1 − cos²θ)/sinθ = sinθ', 'কঠিন',
    sp.simplify((1 / sp.cos(t) - sp.cos(t)) / sp.tan(t) - sp.sin(t)) == 0)
add('(1 − sin²θ)·sec²θ = কত?', '1', ['cos²θ', 'tan²θ', '0'], '1 − sin²θ = cos²θ, আর cos²θ·sec²θ = 1', 'সহজ')
add('tanθ + cotθ নিচের কোনটির সমান?', 'secθ·cosecθ', ['1', 'sinθ·cosθ', 'sec²θ'], '(sin²θ + cos²θ)/(sinθcosθ) = 1/(sinθcosθ) = secθ·cosecθ', 'মধ্যম',
    sp.simplify(sp.tan(t) + sp.cot(t) - 1 / (sp.sin(t) * sp.cos(t))) == 0)
add('(1 + cot²θ)/(1 + tan²θ) = কত?', 'cot²θ', ['tan²θ', '1', 'sec²θ'], 'cosec²θ/sec²θ = cos²θ/sin²θ = cot²θ', 'মধ্যম',
    sp.simplify((1 + sp.cot(t)**2) / (1 + sp.tan(t)**2) - sp.cot(t)**2) == 0)
add('θ সূক্ষ্মকোণ এবং sinθ = cosθ হলে tanθ = কত?', '1', ['0', '√3', '1/√3'], 'tanθ = sinθ/cosθ = 1', 'সহজ')
add('নিচের কোনটি কোনো সূক্ষ্মকোণের sin এর মান হতে পারে না?', '5/4', ['3/5', '0.9', '1/√2'], 'সূক্ষ্মকোণে 0 < sinθ < 1; 5/4 > 1', 'সহজ')
multi('tanθ = 5/12 এবং θ সূক্ষ্মকোণ হলে—', ['sinθ = 5/13', 'secθ = 13/12', 'cotθ = 12/13'], (0, 1), 'অতিভুজ 13; cotθ = 12/5, তাই iii ভুল।', 'মধ্যম')
multi('যেকোনো সূক্ষ্মকোণ θ এর জন্য—', ['sinθ·cosecθ = 1', 'sec²θ + tan²θ = 1', 'cosθ = sinθ·cotθ'], (0, 2), 'sec²θ − tan²θ = 1 (যোগ নয়), তাই ii ভুল।', 'মধ্যম')

pathlib.Path(__file__).with_name('ch9b.json').write_text(json.dumps(OUT, ensure_ascii=False, indent=1), encoding='utf-8')
print(len(OUT), 'questions')
