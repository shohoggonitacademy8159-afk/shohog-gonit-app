#!/usr/bin/env python3
"""উচ্চতর গণিত (দশম, c10h) অধ্যায় 1–4:
1.1 সেট · 1.2 অন্বয় ও ফাংশন · 2 বীজগাণিতিক রাশি · 3.1 পিথাগোরাস/অ্যাপোলোনিয়াস/মধ্যমা · 3.2 ত্রিভুজের কেন্দ্র, টলেমি, বৃত্তস্থ চতুর্ভুজ · 4 জ্যামিতিক অঙ্কন"""
import random, pathlib, sys, math
from fractions import Fraction as F
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from mcqlib import run, save, E, M, H, fr, near, num, pfmt, lin, surd, sup

R = random.Random(2026110101)
def S(xs): return '{' + ', '.join(str(x) for x in sorted(xs)) + '}' if xs else '∅'
def setw(c, pool):
    out = []
    for w in pool:
        if w != c and w not in out: out.append(w)
    return out

# ---------------- 1.1 সেট ----------------
fx11 = [
 ("যে সেটের কোনো উপাদান নেই তাকে কী বলে?", "ফাঁকা সেট", ["সার্বিক সেট", "শক্তি সেট", "উপসেট"], "ফাঁকা সেট ∅ দিয়ে প্রকাশ করা হয়।", E),
 ("A ⊆ B এবং B ⊆ A হলে কোনটি সত্য?", "A = B", ["A ⊂ B", "A ∩ B = ∅", "A ∪ B = ∅"], "পরস্পরের উপসেট হলে সেট দুটি সমান।", E),
 ("A সেটের শক্তি সেটকে কী দিয়ে প্রকাশ করা হয়?", "P(A)", ["A′", "n(A)", "A × A"], "সকল উপসেটের সেট P(A)।", E),
 ("ফাঁকা সেটের শক্তি সেটে কয়টি উপাদান?", "1", ["0", "2", "অসীম"], "P(∅) = {∅}; একটি উপাদান।", E),
 ("(A ∪ B)′ = কত? (ডি মরগানের সূত্র)", "A′ ∩ B′", ["A′ ∪ B′", "A ∩ B", "A′ − B′"], "ডি মরগান: সংযোগের পূরক = পূরকদ্বয়ের ছেদ।", E),
 ("(A ∩ B)′ = কত?", "A′ ∪ B′", ["A′ ∩ B′", "A ∪ B", "A − B"], "ডি মরগান: ছেদের পূরক = পূরকদ্বয়ের সংযোগ।", E),
 ("A − B = কত?", "A ∩ B′", ["A ∪ B′", "A′ ∩ B", "B − A"], "A − B হলো A-এর যে উপাদান B-তে নেই।", M),
 ("A ∪ (B ∩ C) = কত?", "(A ∪ B) ∩ (A ∪ C)", ["(A ∩ B) ∪ (A ∩ C)", "(A ∪ B) ∪ C", "A ∩ (B ∪ C)"], "সংযোগের বণ্টন বিধি।", M),
 ("A ∩ (B ∪ C) = কত?", "(A ∩ B) ∪ (A ∩ C)", ["(A ∪ B) ∩ (A ∪ C)", "(A ∩ B) ∩ C", "A ∪ (B ∩ C)"], "ছেদের বণ্টন বিধি।", M),
 ("A ⊆ B হলে A ∪ B = কত?", "B", ["A", "A ∩ B", "∅"], "A-এর সব উপাদান B-তে আছে।", M),
 ("A ⊆ B হলে A ∩ B = কত?", "A", ["B", "∅", "A ∪ B"], "সাধারণ উপাদান A-এর সবই।", M),
 ("প্রাকৃতিক সংখ্যার সেট N ও পূর্ণসংখ্যার সেট Z হলে N ∩ Z = ?", "N", ["Z", "∅", "Q"], "N ⊂ Z।", E),
]
def p_rand_sets():
    U = list(range(1, R.randint(8, 12) + 1))
    A = set(R.sample(U, R.randint(3, 6))); B = set(R.sample(U, R.randint(3, 6)))
    return U, A, B
def e_union(b):
    U, A, B = p_rand_sets(); c = A | B
    b.add(f"A = {S(A)}, B = {S(B)} হলে A ∪ B = কত?", S(c), setw(S(c), [S(A & B) if A & B else S(A), S(A - B), S(B - A), S(A ^ B), S(c | {max(U) + 1})]), "উভয় সেটের সকল উপাদান একবার করে।", E)
def e_inter(b):
    U, A, B = p_rand_sets(); c = A & B
    if not c: return
    b.add(f"A = {S(A)}, B = {S(B)} হলে A ∩ B = কত?", S(c), setw(S(c), [S(A | B), S(A - B), S(B - A), S(A ^ B)]), "উভয় সেটে যে উপাদান সাধারণ।", E)
def e_diff(b):
    U, A, B = p_rand_sets(); c = A - B
    if not c or c == A: return
    b.add(f"A = {S(A)}, B = {S(B)} হলে A − B = কত?", S(c), setw(S(c), [S(B - A), S(A & B), S(A | B), S(A)]), "A-এর যে উপাদান B-তে নেই।", E)
def e_comp(b):
    n = R.randint(6, 10); U = list(range(1, n + 1)); A = set(R.sample(U, R.randint(2, 5))); c = set(U) - A
    b.add(f"U = {S(U)} এবং A = {S(A)} হলে A′ = কত?", S(c), setw(S(c), [S(A), S(c - {min(c)}), S(c | {min(A)}), S(set(U))]), "U-এর যে উপাদান A-তে নেই।", E)
def e_pow(b):
    n = R.randint(1, 7)
    b.add(f"কোনো সেটের উপাদান সংখ্যা {n} হলে তার শক্তি সেটের উপাদান সংখ্যা কত?", 2 ** n, setw(2 ** n, [2 * n, n * n, 2 ** n - 1, 2 ** (n + 1)]), f"n(P(A)) = 2ⁿ = 2{sup(n)} = {2 ** n}।", E)
def e_proper(b):
    n = R.randint(2, 7)
    b.add(f"{n}টি উপাদানবিশিষ্ট সেটের প্রকৃত উপসেট কয়টি?", 2 ** n - 1, setw(2 ** n - 1, [2 ** n, 2 * n, 2 ** n - 2, n * n]), f"মোট উপসেট 2{sup(n)} = {2 ** n}; সেটটি নিজে বাদে {2 ** n - 1}।", E)
def e_card(b):
    a, bb = R.randint(10, 40), R.randint(10, 40); i = R.randint(2, min(a, bb) - 1)
    c = a + bb - i
    b.add(f"n(A) = {a}, n(B) = {bb}, n(A ∩ B) = {i} হলে n(A ∪ B) = কত?", c, setw(c, [a + bb, a + bb + i, c - 1, abs(a - bb) + i]), f"n(A ∪ B) = {a} + {bb} − {i} = {c}।", E)
def m_card_i(b):
    a, bb = R.randint(15, 50), R.randint(15, 50); i = R.randint(3, min(a, bb) - 2); u = a + bb - i
    b.add(f"n(A ∪ B) = {u}, n(A) = {a}, n(B) = {bb} হলে n(A ∩ B) = কত?", i, setw(i, [a + bb, u - a, u - bb, i + 2]), f"n(A ∩ B) = {a} + {bb} − {u} = {i}।", M)
def m_venn(b):
    n = R.randint(60, 200); a, c = R.randint(20, 60), R.randint(20, 60); both = R.randint(5, min(a, c) - 3)
    nei = n - (a + c - both)
    if nei < 1: return
    subj = R.choice([("ফুটবল", "ক্রিকেট", "খেলে"), ("বাংলা", "ইংরেজি", "পছন্দ করে"), ("চা", "কফি", "পান করে"), ("গণিতে", "বিজ্ঞানে", "পাস করেছে")])
    b.add(f"{n} জন শিক্ষার্থীর মধ্যে {a} জন {subj[0]}, {c} জন {subj[1]} এবং {both} জন উভয়টি {subj[2]}। কতজন কোনোটিই {subj[2]} না?", nei, setw(nei, [n - a - c, n - (a + c + both), nei + both, a + c - both]), f"কমপক্ষে একটি = {a} + {c} − {both} = {a + c - both}; কোনোটিই না = {n} − {a + c - both} = {nei}।", M)
def m_only(b):
    a, c = R.randint(20, 60), R.randint(20, 60); both = R.randint(5, min(a, c) - 3)
    b.add(f"n(A) = {a}, n(B) = {c}, n(A ∩ B) = {both} হলে শুধু A-তে আছে এমন উপাদান কয়টি, অর্থাৎ n(A − B) = ?", a - both, setw(a - both, [c - both, a + both, a, a + c - both]), f"n(A − B) = {a} − {both} = {a - both}।", M)
def m_build(b):
    k = R.randint(10, 90); els = [x for x in range(1, 20) if x * x < k]
    b.add(f"A = {{x ∈ N : x² < {k}}} হলে n(A) = কত?", len(els), setw(len(els), [len(els) + 1, len(els) - 1, k // 2, len(els) + 2]), f"A = {S(els)}; উপাদান {len(els)}টি।", M)
def m_factor(b):
    n = R.choice([12, 18, 20, 24, 28, 30, 36, 40, 42, 45, 48, 50, 54, 56, 60, 72, 84, 90, 96, 100])
    d = [x for x in range(1, n + 1) if n % x == 0]
    L = len(d); b.add(f"A = {{x : x, {n}-এর গুণনীয়ক}} হলে A-এর শক্তি সেটের উপাদান কয়টি?", f"2{sup(L)}", setw(f"2{sup(L)}", [f"2{sup(L - 1)}", f"2{sup(L + 1)}", f"{L}²", str(L)]), f"A = {S(d)}; n(A) = {L}; n(P(A)) = 2{sup(L)}।", M)
def m_cart(b):
    a, c = R.randint(2, 6), R.randint(2, 6)
    b.add(f"n(A) = {a} ও n(B) = {c} হলে n(A × B) = কত?", a * c, setw(a * c, [a + c, 2 ** (a + c), a * c + 1, a ** c]), f"n(A × B) = {a} × {c} = {a * c}।", M)
def m_cartel(b):
    A = sorted(R.sample(range(1, 7), 2)); B = sorted(R.sample(list('abcpqxy'), 2))
    c = '{' + ', '.join(f'({x}, {y})' for x in A for y in B) + '}'
    w1 = '{' + ', '.join(f'({y}, {x})' for x in A for y in B) + '}'
    w2 = '{' + ', '.join(f'({x}, {y})' for x, y in zip(A, B)) + '}'
    w3 = '{' + ', '.join(f'({x}, {y})' for x in A for y in B[:1]) + '}'
    b.add(f"A = {S(A)}, B = {{{', '.join(B)}}} হলে A × B = কত?", c, [w1, w2, w3], "প্রথম উপাদান A থেকে, দ্বিতীয় উপাদান B থেকে নিয়ে সকল ক্রমজোড়।", M)
def m_symd(b):
    U, A, B = p_rand_sets(); c = (A - B) | (B - A)
    if not c or not (A & B): return
    b.add(f"A = {S(A)}, B = {S(B)} হলে (A − B) ∪ (B − A) = কত?", S(c), setw(S(c), [S(A & B), S(A | B), S(A - B), S(B - A)]), "যে উপাদান ঠিক একটি সেটে আছে।", M)
def m_dm(b):
    n = R.randint(7, 10); U = list(range(1, n + 1)); A = set(R.sample(U, 4)); B = set(R.sample(U, 4)); c = set(U) - (A | B)
    if not c: return
    b.add(f"U = {S(U)}, A = {S(A)}, B = {S(B)} হলে (A ∪ B)′ = কত?", S(c), setw(S(c), [S(set(U) - (A & B)), S(A | B), S(A & B) if A & B else '∅', S(c | {min(A)})]), "U থেকে A ∪ B-এর উপাদান বাদ।", M)
def m_eqn(b):
    r1, r2 = R.sample(range(-6, 7), 2)
    s, p = r1 + r2, r1 * r2
    q = f"A = {{x ∈ R : {pfmt(lin([0], 0)) if False else ''}x² {'−' if s > 0 else '+'} {abs(s)}x {'+' if p >= 0 else '−'} {abs(p)} = 0}} হলে A = কত?".replace('x² + 0x', 'x²').replace('x² − 0x', 'x²').replace(' + 0 = 0', ' = 0').replace(' − 0 = 0', ' = 0')
    c = S({r1, r2}); b.add(q, c, setw(c, [S({-r1, -r2}), S({r1, -r2}), S({-r1, r2}), S({r1 + 1, r2})]), f"(x − {r1})(x − {r2}) = 0 ⇒ x = {r1}, {r2}।".replace('− -', '+ '), M)
def h_three(b):
    a, bb, c = R.randint(20, 50), R.randint(20, 50), R.randint(20, 50)
    ab, bc, ca = R.randint(5, 15), R.randint(5, 15), R.randint(5, 15); abc = R.randint(1, min(ab, bc, ca) - 1)
    u = a + bb + c - ab - bc - ca + abc
    b.add(f"n(A) = {a}, n(B) = {bb}, n(C) = {c}, n(A ∩ B) = {ab}, n(B ∩ C) = {bc}, n(C ∩ A) = {ca}, n(A ∩ B ∩ C) = {abc} হলে n(A ∪ B ∪ C) = কত?", u, setw(u, [u - abc, u + abc, a + bb + c, u - 2 * abc]), f"{a} + {bb} + {c} − {ab} − {bc} − {ca} + {abc} = {u}।", H)
def h_pp(b):
    n = R.randint(1, 3)
    c = 2 ** (2 ** n)
    b.add(f"n(A) = {n} হলে n(P(P(A))) = কত?", c, setw(c, [2 ** n, 2 ** (n + 1), 4 ** n, c * 2]), f"n(P(A)) = 2{sup(n)} = {2 ** n}; n(P(P(A))) = 2{sup(2 ** n)} = {c}।", H)
def h_venn_pct(b):
    a, c = R.choice(range(40, 80, 5)), R.choice(range(30, 75, 5)); fail_both = R.choice(range(5, 30, 5))
    # ফেল: a% গণিতে, c% ইংরেজিতে, উভয়ে fail_both% → উভয়ে পাস
    pas = 100 - (a + c - fail_both)
    if pas <= 0 or fail_both >= min(a, c): return
    b.add(f"কোনো পরীক্ষায় {a}% শিক্ষার্থী গণিতে, {c}% ইংরেজিতে এবং {fail_both}% উভয় বিষয়ে ফেল করেছে। উভয় বিষয়ে পাস করেছে কত শতাংশ?", f"{pas}%", setw(f"{pas}%", [f"{100 - a - c}%", f"{fail_both}%", f"{pas + fail_both}%", f"{100 - a}%"]), f"অন্তত একটিতে ফেল = {a} + {c} − {fail_both} = {a + c - fail_both}%; উভয়ে পাস = {pas}%।", H)
def h_venn_num(b):
    tot = R.randint(100, 300); a, c = R.randint(40, 100), R.randint(40, 100); nei = R.randint(5, 30)
    both = a + c + nei - tot
    if both <= 0 or both >= min(a, c): return
    b.add(f"{tot} জনের মধ্যে {a} জন বাংলা ও {c} জন ইংরেজি পত্রিকা পড়ে; {nei} জন কোনোটিই পড়ে না। কতজন উভয় পত্রিকা পড়ে?", both, setw(both, [both + nei, a + c - tot, tot - a - c + nei, both + 1]), f"কমপক্ষে একটি = {tot} − {nei} = {tot - nei}; উভয় = {a} + {c} − {tot - nei} = {both}।", H)
def h_subset_k(b):
    n, k = R.randint(4, 7), R.randint(2, 3)
    c = math.comb(n, k)
    b.add(f"{n}টি উপাদানবিশিষ্ট সেটের ঠিক {k}টি উপাদানবিশিষ্ট উপসেট কয়টি?", c, setw(c, [2 ** n, n * k, c + n, math.comb(n, k - 1) if math.comb(n, k - 1) != c else c + 1]), f"ⁿCₖ = {n}C{k} = {c}।", H)
def h_power_solve(b):
    n = R.randint(3, 8); m = 2 ** n
    b.add(f"কোনো সেটের প্রকৃত উপসেট {m - 1}টি হলে সেটটির উপাদান সংখ্যা কত?", n, setw(n, [n + 1, n - 1, m // 2, m - 1]), f"2ⁿ − 1 = {m - 1} ⇒ 2ⁿ = {m} ⇒ n = {n}।", H)
p11 = run('1.1', R, fx11, [e_union, e_inter, e_diff, e_comp, e_pow, e_proper, e_card], [m_card_i, m_venn, m_only, m_build, m_factor, m_cart, m_cartel, m_symd, m_dm, m_eqn], [h_three, h_pp, h_venn_pct, h_venn_num, h_subset_k, h_power_solve])

# ---------------- 1.2 অন্বয় ও ফাংশন ----------------
X = ('x',)
def lx(a, c): return pfmt(lin([a], c), X)
fx12 = [
 ("অন্বয়ের প্রথম উপাদানগুলোর সেটকে কী বলে?", "ডোমেন", ["রেঞ্জ", "সহডোমেন", "শক্তি সেট"], "ক্রমজোড়ের প্রথম উপাদানের সেট ডোমেন।", E),
 ("অন্বয়ের দ্বিতীয় উপাদানগুলোর সেটকে কী বলে?", "রেঞ্জ", ["ডোমেন", "উপসেট", "সার্বিক সেট"], "ক্রমজোড়ের দ্বিতীয় উপাদানের সেট রেঞ্জ।", E),
 ("কোন অন্বয়টি ফাংশন নয়?", "{(1, 2), (1, 3), (2, 4)}", ["{(1, 2), (2, 3), (3, 4)}", "{(1, 5), (2, 5), (3, 5)}", "{(0, 0), (1, 1)}"], "1-এর দুটি ভিন্ন প্রতিচ্ছবি আছে।", E),
 ("ফাংশন f এক-এক হবে যদি—", "f(a) = f(b) হলে a = b হয়", ["f(a) = f(b) হলে a ≠ b হয়", "রেঞ্জ ফাঁকা হয়", "ডোমেন অসীম হয়"], "এক-এক ফাংশনের সংজ্ঞা।", E),
 ("কোন ফাংশনের বিপরীত ফাংশন থাকে?", "এক-এক ও সার্বিক ফাংশনের", ["যেকোনো ফাংশনের", "ধ্রুবক ফাংশনের", "শুধু দ্বিঘাত ফাংশনের"], "বিপরীত ফাংশনের জন্য ফাংশনটি এক-এক ও সার্বিক হতে হয়।", M),
 ("f(x) = x² (x ∈ R) ফাংশনটি কেমন?", "এক-এক নয়", ["এক-এক", "বিপরীত ফাংশন আছে", "ধ্রুবক"], "f(2) = f(−2) = 4।", M),
 ("f(x) = |x| ফাংশনের রেঞ্জ কোনটি?", "[0, ∞)", ["R", "(0, ∞)", "(−∞, 0]"], "পরমমান কখনো ঋণাত্মক নয়।", M),
 ("y = f(x) ও y = f⁻¹(x)-এর লেখচিত্র কোন রেখা সাপেক্ষে প্রতিসম?", "y = x", ["x-অক্ষ", "y-অক্ষ", "y = −x"], "বিপরীত ফাংশনের লেখচিত্র y = x রেখায় প্রতিফলন।", M),
]
def e_val(b):
    a, c, k = R.choice([v for v in range(-6, 8) if v not in (0, 1)]), R.randint(-9, 9), R.randint(-5, 6)
    v = a * k + c
    b.add(f"f(x) = {lx(a, c)} হলে f({num(k)}) = কত?", num(v), [num(w) for w in near(v)], f"f({num(k)}) = {a} × ({num(k)}) {'+' if c >= 0 else '−'} {abs(c)} = {num(v)}।", E)
def e_val2(b):
    a, c, k = R.randint(1, 4), R.randint(-9, 9), R.randint(-4, 4)
    v = a * k * k + c
    b.add(f"f(x) = {pfmt({(2,): a, (0,): c} if c else {(2,): a}, X)} হলে f({num(k)}) = কত?", num(v), [num(w) for w in near(v)] if k else [num(v + a), num(v - 1), num(v + 2)], f"f({num(k)}) = {a}({num(k)})² {'+' if c >= 0 else '−'} {abs(c)} = {num(v)}।", E)
def e_dom(b):
    xs = R.sample(range(-5, 10), 4); ys = [R.randint(-5, 10) for _ in xs]
    rel = '{' + ', '.join(f'({x}, {y})' for x, y in zip(xs, ys)) + '}'
    c = S(set(xs)); b.add(f"R = {rel} অন্বয়ের ডোমেন কোনটি?", c, setw(c, [S(set(ys)), S(set(xs) | set(ys)), S(set(xs[:3])), S(set(xs) - {xs[0]} | {xs[0] + 1})]), "ক্রমজোড়গুলোর প্রথম উপাদান।", E)
def e_ran(b):
    xs = R.sample(range(-5, 10), 4); ys = R.sample(range(-5, 12), 4)
    rel = '{' + ', '.join(f'({x}, {y})' for x, y in zip(xs, ys)) + '}'
    c = S(set(ys)); b.add(f"R = {rel} অন্বয়ের রেঞ্জ কোনটি?", c, setw(c, [S(set(xs)), S(set(xs) | set(ys)), S(set(ys[:3])), S(set(ys) - {ys[0]} | {ys[0] + 1})]), "ক্রমজোড়গুলোর দ্বিতীয় উপাদান।", E)
def e_rule(b):
    A = sorted(R.sample(range(-3, 6), 4)); a, c = R.randint(1, 4), R.randint(-4, 5)
    rel = '{' + ', '.join(f'({x}, {a * x + c})' for x in A) + '}'
    ok = f"y = {lx(a, c)}"; b.add(f"R = {rel} অন্বয়টি কোন নিয়মে গঠিত?", ok, setw(ok, [f"y = {lx(a + 1, c - A[0])}", f"y = {lx(a, c + 1)}", f"y = {lx(c if c not in (0, a) else a + 2, a)}"]), "প্রতিটি ক্রমজোড়ে যাচাই করলে মেলে।", E)
def m_inv(b):
    a, c = R.choice([v for v in range(-5, 7) if v not in (0, 1, -1)]), R.randint(-9, 9); y = R.randint(-6, 8)
    # f⁻¹(k): ax + c = k ⇒ x = (k − c)/a ; k নির্বাচন যাতে পূর্ণসংখ্যা
    k = a * y + c
    b.add(f"f(x) = {lx(a, c)} হলে f⁻¹({num(k)}) = কত?", num(y), [num(w) for w in near(y)], f"f(x) = {num(k)} ⇒ x = ({num(k)} {'−' if c >= 0 else '+'} {abs(c)})/{num(a)} = {num(y)}।", M)
def m_inv_expr(b):
    a, c = R.choice([2, 3, 4, 5, 6, 7]), R.choice([v for v in range(-7, 8) if v])
    ok = f"(x {'−' if c > 0 else '+'} {abs(c)})/{num(a)}"
    b.add(f"f(x) = {lx(a, c)} হলে f⁻¹(x) = কত?", ok, [f"(x {'+' if c > 0 else '−'} {abs(c)})/{num(a)}", f"{num(a)}x {'−' if c > 0 else '+'} {abs(c)}", f"1/({lx(a, c)})"], f"y = {lx(a, c)} ⇒ x = (y {'−' if c > 0 else '+'} {abs(c)})/{num(a)}।", M)
def m_domfrac(b):
    a, c = R.randint(-8, 8), R.choice([v for v in range(-9, 10) if v])
    if a == -c: return
    ok = f"R − {{{num(c)}}}"
    b.add(f"f(x) = (x {'+' if a >= 0 else '−'} {abs(a)})/(x {'−' if c > 0 else '+'} {abs(c)}) ফাংশনের ডোমেন কোনটি?", ok, [f"R − {{{num(-c)}}}", f"R − {{{num(-a)}}}" if -a != c else f"R − {{{num(c + 1)}}}", "R"], f"হর শূন্য হয় x = {num(c)}-এ; তাই বাদ।", M)
def m_comp(b):
    a, c, p, q = R.randint(1, 4), R.randint(-5, 5), R.randint(1, 4), R.randint(-5, 5); k = R.randint(-3, 4)
    g = p * k + q; v = a * g + c
    w2 = p * (a * k + c) + q
    if w2 == v: return
    b.add(f"f(x) = {lx(a, c)} ও g(x) = {lx(p, q)} হলে (f∘g)({num(k)}) = কত?", num(v), [num(w2), num(v + 1), num(g)] if g not in (v, w2, v + 1) else [num(w2), num(v + 1), num(v - 2)], f"g({num(k)}) = {num(g)}; f({num(g)}) = {num(v)}।", M)
def m_root(b):
    r1, r2 = R.sample(range(-6, 8), 2); s, p = r1 + r2, r1 * r2
    expr = pfmt({(2,): 1, (1,): -s, (0,): p} if s else {(2,): 1, (0,): p}, X) if p else pfmt({(2,): 1, (1,): -s}, X)
    c = S({r1, r2})
    b.add(f"f(x) = {expr} হলে f(x) = 0-এর সমাধান সেট কোনটি?", c, setw(c, [S({-r1, -r2}), S({r1, -r2}), S({-r1, r2}), S({r1 + 1, r2 - 1})]), f"উৎপাদকে (x {'−' if r1 >= 0 else '+'} {abs(r1)})(x {'−' if r2 >= 0 else '+'} {abs(r2)}) = 0।", M)
def m_frac_val(b):
    a, c = R.randint(1, 6), R.randint(1, 6); k = R.randint(-4, 9)
    if k == c: return
    v = F(k + a, k - c)
    b.add(f"f(x) = (x + {a})/(x − {c}) হলে f({num(k)}) = কত?", fr(v) if v >= 0 else '−' + fr(-v), [num(w) for w in (v + 1, -v if v != 0 else 2, F(k - a, k + c) if k + c else v + 2)], f"f({num(k)}) = ({num(k + a)})/({num(k - c)}) = {num(v)}।", M)
def m_find_a(b):
    a, k, c = R.choice([v for v in range(-5, 7) if v]), R.randint(1, 5), R.choice([v for v in range(-6, 7) if v])
    v = a * k + c
    b.add(f"f(x) = ax {'+' if c >= 0 else '−'} {abs(c)} এবং f({k}) = {num(v)} হলে a = কত?", num(a), [num(w) for w in near(a)], f"{k}a {'+' if c >= 0 else '−'} {abs(c)} = {num(v)} ⇒ a = {num(a)}।", M)
def h_sqrtdom(b):
    a = R.randint(-6, 9)
    ok = f"[{num(a)}, ∞)"
    b.add(f"f(x) = √(x {'−' if a >= 0 else '+'} {abs(a)}) ফাংশনের ডোমেন কোনটি?", ok, [f"({num(a)}, ∞)", f"(−∞, {num(a)}]", f"[{num(-a)}, ∞)" if a else "R"], f"x {'−' if a >= 0 else '+'} {abs(a)} ≥ 0 ⇒ x ≥ {num(a)}।", H)
def h_sqrt2(b):
    a = R.randint(2, 9)
    ok = f"[−{a}, {a}]"
    b.add(f"f(x) = √({a * a} − x²) ফাংশনের ডোমেন কোনটি?", ok, [f"(−{a}, {a})", f"[0, {a}]", f"R − {{−{a}, {a}}}"], f"{a * a} − x² ≥ 0 ⇒ −{a} ≤ x ≤ {a}।", H)
def h_range_sq(b):
    c = R.randint(-9, 9)
    ok = f"[{num(c)}, ∞)"
    b.add(f"f(x) = x² {'+' if c >= 0 else '−'} {abs(c)} (x ∈ R) ফাংশনের রেঞ্জ কোনটি?", ok, [f"({num(c)}, ∞)", "R", f"(−∞, {num(c)}]"], f"x² ≥ 0 ⇒ f(x) ≥ {num(c)}।", H)
def h_inv_frac(b):
    a, c = R.randint(1, 6), R.randint(1, 6); y = R.choice([v for v in range(-5, 8) if v != 1])
    x = F(a + c * y, y - 1)
    # f(x) = (x + a)/(x − c); f(x) = y ⇒ x = (a + cy)/(y − 1)
    b.add(f"f(x) = (x + {a})/(x − {c}) হলে f⁻¹({num(y)}) = কত?", num(x), [num(x + 1), num(F(a - c * y, y - 1)) if F(a - c * y, y - 1) != x else num(x + 2), num(-x) if x else num(x - 1)], f"(x + {a})/(x − {c}) = {num(y)} ⇒ x = ({a} + {c}·({num(y)}))/({num(y)} − 1) = {num(x)}।", H)
def h_fog_expr(b):
    a, c = R.randint(2, 4), R.randint(-5, 5)
    q = R.choice([v for v in range(-4, 5) if v])
    # f(x) = ax + c, g(x) = x² + q ⇒ f(g(x)) = ax² + aq + c
    ok = pfmt({(2,): a, (0,): a * q + c} if a * q + c else {(2,): a}, X)
    w = pfmt({(2,): a * a, (1,): 2 * a * c, (0,): c * c + q} if c * c + q else {(2,): a * a, (1,): 2 * a * c}, X) if c else pfmt({(2,): a * a, (0,): q}, X)
    b.add(f"f(x) = {lx(a, c)} এবং g(x) = x² {'+' if q > 0 else '−'} {abs(q)} হলে f(g(x)) = কত?", ok, setw(ok, [w, pfmt({(2,): a, (0,): q + c} if q + c else {(2,): a}, X), pfmt({(2,): 1, (0,): a * q + c} if a * q + c else {(2,): 1}, X), pfmt({(2,): a, (0,): a * q - c} if a * q - c else {(2,): a + 1}, X)]), f"f(g(x)) = {a}(x² {'+' if q > 0 else '−'} {abs(q)}) {'+' if c >= 0 else '−'} {abs(c)} = {ok}।", H)
def h_selfinv(b):
    a = R.randint(2, 9)
    b.add(f"f(x) = (x + {a})/(x − 1) হলে f(f({a + 1}))-এর মান কত?", a + 1, setw(a + 1, [F(2 * a + 1, a) if F(2 * a + 1, a).denominator == 1 else a + 2, a, 1, a + 3]), f"এখানে f(f(x)) = x, কারণ f-এর বিপরীত f নিজেই; তাই মান {a + 1}।", H)
p12 = run('1.2', R, fx12, [e_val, e_val2, e_dom, e_ran, e_rule], [m_inv, m_inv_expr, m_domfrac, m_comp, m_root, m_frac_val, m_find_a], [h_sqrtdom, h_sqrt2, h_range_sq, h_inv_frac, h_fog_expr, h_selfinv])
save('h1', p11 + p12)

# ---------------- 2 বীজগাণিতিক রাশি ----------------
def poly(cs):
    """cs = [a_n, …, a_0]"""
    n = len(cs) - 1
    return pfmt({(n - i,): c for i, c in enumerate(cs) if c}, X)
def pev(cs, x): return sum(c * x ** (len(cs) - 1 - i) for i, c in enumerate(cs))
fx2 = [
 ("x³ + 2x² − 5x + 1 বহুপদীর মাত্রা কত?", "3", ["2", "1", "4"], "চলকের সর্বোচ্চ ঘাত 3।", E),
 ("ভাগশেষ উপপাদ্য অনুযায়ী P(x)-কে (x − a) দিয়ে ভাগ করলে ভাগশেষ কত?", "P(a)", ["P(−a)", "P(0)", "a"], "ভাগশেষ উপপাদ্য।", E),
 ("P(a) = 0 হলে (x − a) সম্পর্কে কী বলা যায়?", "P(x)-এর একটি উৎপাদক", ["P(x)-এর ভাগশেষ a", "P(x)-এর মূল নয়", "কিছুই বলা যায় না"], "উৎপাদক উপপাদ্য।", E),
 ("কোনটি প্রতিসম রাশি?", "a² + b² + c²", ["a² − b²", "a − b + c", "a³ + 2b"], "যেকোনো দুটি চলক বিনিময়েও রাশি অপরিবর্তিত।", E),
 ("কোনটি চক্র-ক্রমিক রাশি?", "a(b − c) + b(c − a) + c(a − b)", ["a² + b²", "a − b", "ab + c"], "a → b → c → a বসালে রাশি একই থাকে।", E),
 ("a + b + c = 0 হলে a³ + b³ + c³ = কত?", "3abc", ["0", "abc", "−3abc"], "a³ + b³ + c³ − 3abc = (a + b + c)(…)।", E),
 ("a³ + b³ + c³ − 3abc = কত?", "(a + b + c)(a² + b² + c² − ab − bc − ca)", ["(a + b + c)³", "(a − b)(b − c)(c − a)", "(a + b + c)(ab + bc + ca)"], "পরিচিত অভেদ।", M),
 ("যে রাশির প্রতিটি পদের মাত্রা সমান তাকে কী বলে?", "সমমাত্রিক রাশি", ["প্রতিসম রাশি", "চক্র-ক্রমিক রাশি", "মূলদ রাশি"], "প্রতিটি পদের মাত্রা সমান।", E),
 ("x²y + xy² + y³ রাশিটির মাত্রা কত?", "3", ["2", "4", "6"], "প্রতিটি পদের মাত্রা 3; সমমাত্রিক।", E),
 ("P(x)/Q(x) প্রকৃত ভগ্নাংশ হবে যদি—", "P(x)-এর মাত্রা Q(x)-এর মাত্রার চেয়ে কম হয়", ["P(x)-এর মাত্রা বেশি হয়", "উভয়ের মাত্রা সমান হয়", "Q(x) ধ্রুবক হয়"], "প্রকৃত মূলদ ভগ্নাংশের সংজ্ঞা।", M),
]
def rpoly():
    n = R.choice([2, 3, 3, 4]); cs = [R.choice([1, 1, 2, 3, -1, -2])] + [R.randint(-6, 6) for _ in range(n)]
    return cs
def e_peval(b):
    cs = rpoly(); a = R.randint(-3, 3); v = pev(cs, a)
    b.add(f"P(x) = {poly(cs)} হলে P({num(a)}) = কত?", num(v), [num(w) for w in near(v)], f"x = {num(a)} বসিয়ে P({num(a)}) = {num(v)}।", E)
def e_rem(b):
    cs = rpoly(); a = R.choice([v for v in range(-3, 4) if v]); v = pev(cs, a)
    b.add(f"{poly(cs)}-কে (x {'−' if a > 0 else '+'} {abs(a)}) দিয়ে ভাগ করলে ভাগশেষ কত?", num(v), [num(pev(cs, -a)) if pev(cs, -a) != v else num(v + 2), num(v + 1), num(v - 1)], f"ভাগশেষ = P({num(a)}) = {num(v)}।", E)
def e_deg(b):
    n = R.randint(2, 6); cs = [R.randint(1, 5)] + [R.randint(-5, 5) for _ in range(n)]
    if not any(cs[1:]): return
    b.add(f"{poly(cs)} বহুপদীর মাত্রা কত?", n, setw(n, [n - 1, n + 1, len([c for c in cs if c]), 2 * n]), f"সর্বোচ্চ ঘাত {n}।", E)
def e_lead(b):
    n = R.randint(2, 5); cs = [R.choice([2, 3, 4, 5, -2, -3, 7])] + [R.randint(-5, 5) for _ in range(n)]
    if not any(cs[1:]) or cs[-1] == cs[0]: return
    b.add(f"{poly(cs)} বহুপদীর মুখ্য সহগ কত?", num(cs[0]), setw(num(cs[0]), [num(cs[-1]) if cs[-1] else '0', num(n), '1', num(-cs[0])]), "সর্বোচ্চ ঘাতের পদের সহগ।", E)
def e_abc(b):
    a, c = R.randint(-6, 6), R.randint(-6, 6); bb = -a - c
    if 0 in (a, bb, c): return
    v = 3 * a * bb * c
    b.add(f"a = {num(a)}, b = {num(bb)}, c = {num(c)} হলে a³ + b³ + c³ = কত?", num(v), [num(a * bb * c), num(-v), '0'] if v else None, f"a + b + c = 0 ⇒ a³ + b³ + c³ = 3abc = {num(v)}।", E)
def m_kfac(b):
    a = R.choice([v for v in range(-3, 4) if v]); cs = [1, R.randint(-5, 5), R.randint(-6, 6)]
    rest = pev(cs + [0], a)   # x³ + p x² + q x + k ; k = −(a³ + p a² + q a)
    k = -rest
    if cs[1] in (0, 1, -1) or cs[2] in (0, 1, -1): return
    b.add(f"x³ {'' if True else ''}{'+ ' + str(cs[1]) + 'x²' if cs[1] > 0 else ('− ' + str(-cs[1]) + 'x²' if cs[1] < 0 else '')} {'+ ' + str(cs[2]) + 'x' if cs[2] > 0 else ('− ' + str(-cs[2]) + 'x' if cs[2] < 0 else '')} + k-এর একটি উৎপাদক (x {'−' if a > 0 else '+'} {abs(a)}) হলে k = কত?".replace('  ', ' ').replace('x³  +', 'x³ +'), num(k), [num(-k) if k else '1', num(k + 1), num(k - 2)], f"P({num(a)}) = 0 ⇒ k = {num(k)}।", M)
def m_remk(b):
    a = R.choice([v for v in range(-3, 4) if v]); p, q = R.randint(-5, 5), R.randint(-6, 6); r = R.randint(-8, 8)
    # x³ + kx² + px + q ÷ (x − a) ভাগশেষ r ⇒ a³ + k a² + p a + q = r
    num_ = r - a ** 3 - p * a - q
    if num_ % (a * a): return
    k = num_ // (a * a)
    body = poly([1, 0, p, q]).replace('x³', 'x³ + kx²', 1)
    b.add(f"{body}-কে (x {'−' if a > 0 else '+'} {abs(a)}) দিয়ে ভাগ করলে ভাগশেষ {num(r)} হয়। k = কত?", num(k), [num(w) for w in near(k)], f"P({num(a)}) = {num(r)} থেকে k = {num(k)}।", M)
def m_remlin(b):
    p, q = R.choice([(1, 2), (2, 1), (3, 1), (1, 3), (3, 2), (2, 3)]); sgn = R.choice([1, -1])
    cs = [R.choice([2, 4, 6, 8])] + [R.randint(-5, 5) for _ in range(2)] + [R.randint(-6, 6)]
    x0 = F(sgn * q, p); v = sum(F(c) * x0 ** (3 - i) for i, c in enumerate(cs))
    if v.denominator > 8: return
    b.add(f"{poly(cs)}-কে ({p if p > 1 else ''}x {'−' if sgn > 0 else '+'} {q}) দিয়ে ভাগ করলে ভাগশেষ কত?", num(v), [num(sum(F(c) * (-x0) ** (3 - i) for i, c in enumerate(cs))), num(v + 1), num(v * 2) if v else '1'], f"ভাগশেষ = P({num(x0)}) = {num(v)}।", M)
def m_pf1(b):
    a, c = R.sample([v for v in range(-5, 7) if v], 2)
    A = F(1, a - c)
    b.add(f"1/((x {'−' if a >= 0 else '+'} {abs(a)})(x {'−' if c >= 0 else '+'} {abs(c)})) = A/(x {'−' if a >= 0 else '+'} {abs(a)}) + B/(x {'−' if c >= 0 else '+'} {abs(c)}) হলে A = কত?".replace('x − 0', 'x').replace('x + 0', 'x'), num(A), setw(num(A), [num(-A), num(F(1, a + c)) if a + c else '1', num(a - c), '1']), f"x = {num(a)} বসিয়ে A = 1/({num(a)} − ({num(c)})) = {num(A)}।", M)
def m_sq(b):
    s, p = R.randint(-7, 9), R.randint(-6, 10)
    v = s * s - 2 * p
    b.add(f"a + b + c = {num(s)} এবং ab + bc + ca = {num(p)} হলে a² + b² + c² = কত?", num(v), setw(num(v), [num(s * s + 2 * p), num(s * s - p), num(s * s), num(v + 1)]), f"a² + b² + c² = ({num(s)})² − 2({num(p)}) = {num(v)}।", M)
def m_cubesum(b):
    s, p = R.randint(1, 6), R.randint(-6, 6)
    v = s ** 3 - 3 * s * p
    b.add(f"x + y = {s} এবং xy = {num(p)} হলে x³ + y³ = কত?", num(v), setw(num(v), [num(s ** 3 + 3 * s * p), num(s ** 3 - p), num(s ** 3), num(v + s)]), f"x³ + y³ = (x + y)³ − 3xy(x + y) = {s ** 3} − 3({num(p)})({s}) = {num(v)}।", M)
def m_factor_cubic(b):
    r = sorted(R.sample(range(-4, 5), 3))
    if 0 in r: return
    cs = [1, -sum(r), r[0] * r[1] + r[1] * r[2] + r[0] * r[2], -r[0] * r[1] * r[2]]
    fac = lambda v: f"(x {'−' if v > 0 else '+'} {abs(v)})"
    ok = ''.join(fac(v) for v in r)
    b.add(f"{poly(cs)}-এর উৎপাদক বিশ্লেষণ কোনটি?", ok, [''.join(fac(-v) for v in r), fac(r[0]) + fac(-r[1]) + fac(r[2]), fac(r[0]) + fac(r[1]) + fac(-r[2])], f"P({r[0]}) = P({r[1]}) = P({r[2]}) = 0।", M)
def m_cyc(b):
    a, bb, c = R.sample(range(-5, 8), 3)
    v = a * (bb - c) + bb * (c - a) + c * (a - bb)
    w = (a - bb) * (bb - c) * (c - a)
    b.add(f"a = {num(a)}, b = {num(bb)}, c = {num(c)} হলে a²(b − c) + b²(c − a) + c²(a − b) = কত?", num(-w), setw(num(-w), [num(w), '0', num(a * bb * c), num(-w + 1)]), f"রাশিটি = −(a − b)(b − c)(c − a) = {num(-w)}।", M)
def h_pf2(b):
    a, c = R.sample([v for v in range(-4, 6) if v], 2); p, q = R.randint(1, 5), R.randint(-6, 6)
    A = F(p * a + q, a - c); B = F(p * c + q, c - a)
    if A.denominator > 6: return
    fa = f"(x {'−' if a >= 0 else '+'} {abs(a)})".replace('x − 0', 'x').replace('(x + 0)', '(x)')
    fc = f"(x {'−' if c >= 0 else '+'} {abs(c)})".replace('x − 0', 'x').replace('(x + 0)', '(x)')
    top = lx(p, q)
    b.add(f"({top})/({fa}{fc}) = A/{fa} + B/{fc} হলে A = কত?".replace('/(x)', '/x'), num(A), setw(num(A), [num(B), num(-A), num(A + 1), num(p)]), f"x = {num(a)} বসিয়ে A = ({num(p * a + q)})/({num(a - c)}) = {num(A)}।", H)
def h_two_rem(b):
    a, c = R.sample([v for v in range(-3, 4) if v], 2); p, q = R.randint(-5, 5), R.randint(-5, 5)
    # x³ + px² + mx + n, P(a) = r1, P(c) = r2 থেকে m
    m, n = R.randint(-6, 6), R.randint(-6, 6)
    r1 = a ** 3 + p * a * a + m * a + n; r2 = c ** 3 + p * c * c + m * c + n
    pp = poly([1, p, 0, 0]).replace('', '')
    body = (pp + ' + mx + n').replace('  ', ' ')
    b.add(f"{body}-কে (x {'−' if a > 0 else '+'} {abs(a)}) ও (x {'−' if c > 0 else '+'} {abs(c)}) দিয়ে ভাগ করলে ভাগশেষ যথাক্রমে {num(r1)} ও {num(r2)}। m = কত?", num(m), [num(w) for w in (n if n != m else m + 3, m + 1, -m if m else m - 2)], f"দুটি সমীকরণ সমাধান করে m = {num(m)}, n = {num(n)}।", H)
def h_abc3(b):
    s, p = R.randint(1, 6), R.randint(-5, 8); q = R.randint(-6, 6)
    a2 = s * s - 2 * p; v = s * (a2 - p) + 3 * q
    b.add(f"a + b + c = {s}, ab + bc + ca = {num(p)} এবং abc = {num(q)} হলে a³ + b³ + c³ = কত?", num(v), setw(num(v), [num(s * (a2 - p)), num(v - 6 * q) if q else num(v + 2), num(s ** 3), num(v + 1)]), f"a² + b² + c² = {a2}; a³ + b³ + c³ = {s}({a2} − {num(p)}) + 3({num(q)}) = {num(v)}।", H)
def h_recip(b):
    k = R.randint(3, 9)
    v = k ** 3 - 3 * k
    b.add(f"x + 1/x = {k} হলে x³ + 1/x³ = কত?", v, setw(v, [k ** 3, k ** 3 + 3 * k, k * k - 2, v + 1]), f"x³ + 1/x³ = {k}³ − 3·{k} = {v}।", H)
def h_recip2(b):
    k = R.randint(2, 8)
    v = (k * k - 2) ** 2 - 2
    b.add(f"x + 1/x = {k} হলে x⁴ + 1/x⁴ = কত?", v, setw(v, [k ** 4, (k * k - 2) ** 2, k ** 4 - 4, v + 2]), f"x² + 1/x² = {k * k - 2}; x⁴ + 1/x⁴ = {k * k - 2}² − 2 = {v}।", H)
def h_common(b):
    a = R.choice([v for v in range(-3, 4) if v]); p = R.randint(-4, 4)
    # x² + px + k এবং x² + (p+1)x + ... both have (x − a): k = −(a² + pa)
    k = -(a * a + p * a)
    q = R.randint(-4, 4); l = -(a * a + q * a)
    if p == q: return
    b.add(f"x² {'+' if p >= 0 else '−'} {abs(p)}x + k এবং x² {'+' if q >= 0 else '−'} {abs(q)}x + l রাশি দুটির সাধারণ উৎপাদক (x {'−' if a > 0 else '+'} {abs(a)}) হলে k − l = কত?".replace(' + 0x', '').replace(' − 0x', ''), num(k - l), [num(l - k), num(k + l), num(k - l + a)] if len({k - l, l - k, k + l, k - l + a}) == 4 else [num(k - l + 1), num(k - l - 1), num(k - l + 2)], f"k = {num(k)}, l = {num(l)} ⇒ k − l = {num(k - l)}।", H)
p2 = run(None, R, fx2, [e_peval, e_rem, e_deg, e_lead, e_abc], [m_kfac, m_remk, m_remlin, m_pf1, m_sq, m_cubesum, m_factor_cubic, m_cyc], [h_pf2, h_two_rem, h_abc3, h_recip, h_recip2, h_common])
save('h2', p2)

# ---------------- 3.1 পিথাগোরাস, অ্যাপোলোনিয়াস, মধ্যমা ----------------
TRI = [(a, b, c) for a in range(3, 21) for b in range(a, 21) for c in range(b, 21) if a + b > c]
fx31 = [
 ("অ্যাপোলোনিয়াসের উপপাদ্য অনুযায়ী ΔABC-এর মধ্যমা AD হলে AB² + AC² = কত?", "2(AD² + BD²)", ["AD² + BD²", "2AD² + BD²", "4(AD² + BD²)"], "অ্যাপোলোনিয়াসের উপপাদ্য।", E),
 ("ত্রিভুজের মধ্যমাত্রয়ের ছেদবিন্দুকে কী বলে?", "ভরকেন্দ্র", ["লম্ববিন্দু", "অন্তঃকেন্দ্র", "পরিকেন্দ্র"], "মধ্যমাত্রয় ভরকেন্দ্রে মিলিত হয়।", E),
 ("ভরকেন্দ্র প্রতিটি মধ্যমাকে শীর্ষ থেকে কী অনুপাতে বিভক্ত করে?", "2 : 1", ["1 : 2", "1 : 1", "3 : 1"], "শীর্ষবিন্দু থেকে 2 : 1।", E),
 ("ΔABC-এ ∠C স্থূলকোণ এবং BC-এর বর্ধিতাংশে A থেকে লম্ব AD হলে AB² = কত?", "AC² + BC² + 2BC·CD", ["AC² + BC² − 2BC·CD", "AC² + BC²", "AC² − BC² + 2BC·CD"], "পিথাগোরাসের উপপাদ্যের বিস্তৃতি (স্থূলকোণ)।", M),
 ("ΔABC-এ ∠C সূক্ষ্মকোণ এবং BC-এর উপর A থেকে লম্ব AD হলে AB² = কত?", "AC² + BC² − 2BC·CD", ["AC² + BC² + 2BC·CD", "AC² + BC²", "AC² − BC²"], "পিথাগোরাসের উপপাদ্যের বিস্তৃতি (সূক্ষ্মকোণ)।", M),
 ("ত্রিভুজের তিন মধ্যমার বর্গের সমষ্টি বাহুত্রয়ের বর্গের সমষ্টির কত গুণ?", "3/4 গুণ", ["1/2 গুণ", "সমান", "4/3 গুণ"], "AD² + BE² + CF² = (3/4)(a² + b² + c²)।", M),
 ("সমকোণী ত্রিভুজের অতিভুজের মধ্যবিন্দু থেকে শীর্ষবিন্দুত্রয়ের দূরত্ব কেমন?", "সমান", ["অসমান", "অতিভুজের সমান", "শূন্য"], "অতিভুজের মধ্যবিন্দু পরিকেন্দ্র।", M),
]
def med2(a, b, c): return F(2 * b * b + 2 * c * c - a * a, 4)   # a-এর উপর মধ্যমার বর্গ
def perfect(v):
    v = F(v); return v >= 0 and math.isqrt(v.numerator) ** 2 == v.numerator and math.isqrt(v.denominator) ** 2 == v.denominator
def sq(v):
    v = F(v)
    if v.denominator == 1:
        r = math.isqrt(v.numerator)
        if r * r == v.numerator: return str(r)
        return surd(v.numerator)
    n, d = v.numerator, v.denominator
    if math.isqrt(d) ** 2 == d: return f"{surd(n)}/{math.isqrt(d)}" if math.isqrt(n) ** 2 != n else fr(F(math.isqrt(n), math.isqrt(d)))
    return f"√({fr(v)})"
def e_ag(b):
    d = 3 * R.randint(2, 15)
    b.add(f"ΔABC-এর মধ্যমা AD = {d} সেমি এবং G ভরকেন্দ্র হলে AG = কত সেমি?", 2 * d // 3, setw(2 * d // 3, [d // 3, d // 2 if d % 2 == 0 else d - 1, d, 2 * d]), f"AG = (2/3) × {d} = {2 * d // 3}।", E)
def e_gd(b):
    d = 3 * R.randint(2, 15)
    b.add(f"ΔABC-এর মধ্যমা AD = {d} সেমি এবং G ভরকেন্দ্র হলে GD = কত সেমি?", d // 3, setw(d // 3, [2 * d // 3, d, d // 3 + 1, d - 1]), f"GD = (1/3) × {d} = {d // 3}।", E)
def e_apo(b):
    ad, bd = R.randint(2, 12), R.randint(2, 12)
    v = 2 * (ad * ad + bd * bd)
    b.add(f"ΔABC-এ AD মধ্যমা, AD = {ad} সেমি ও BD = {bd} সেমি হলে AB² + AC² = কত বর্গ সেমি?", v, setw(v, [ad * ad + bd * bd, 4 * (ad * ad + bd * bd), v + 2 * bd, (ad + bd) ** 2]), f"2(AD² + BD²) = 2({ad * ad} + {bd * bd}) = {v}।", E)
def e_hyp(b):
    a, c = R.choice([(3, 4), (6, 8), (5, 12), (8, 15), (9, 12), (7, 24), (12, 16), (20, 21)])
    h = math.isqrt(a * a + c * c)
    b.add(f"সমকোণী ত্রিভুজের সমকোণ সংলগ্ন বাহু {a} ও {c} সেমি হলে অতিভুজের মধ্যমার দৈর্ঘ্য কত সেমি?", fr(F(h, 2)), setw(fr(F(h, 2)), [str(h), fr(F(a + c, 2)), fr(F(h, 3)), fr(F(h + 1, 2))]), f"অতিভুজ {h}; মধ্যমা = অতিভুজের অর্ধেক = {fr(F(h, 2))}।", E)
def e_ctype(b):
    a, bb, c = R.choice(TRI)
    t = a * a + bb * bb - c * c
    ok = 'সমকোণী' if t == 0 else ('সূক্ষ্মকোণী' if t > 0 else 'স্থূলকোণী')
    b.add(f"কোনো ত্রিভুজের বাহু {a}, {bb}, {c} একক হলে ত্রিভুজটি কেমন?", ok, setw(ok, ['সমকোণী', 'সূক্ষ্মকোণী', 'স্থূলকোণী', 'ত্রিভুজ গঠন অসম্ভব']), f"{a}² + {bb}² = {a * a + bb * bb}, {c}² = {c * c}।", E)
def m_median(b):
    a, bb, c = R.choice(TRI); m = med2(a, bb, c)
    if m <= 0 or not perfect(m): return
    ok = sq(m)
    if '√(' in ok: return
    b.add(f"ΔABC-এ BC = {a}, CA = {bb}, AB = {c} একক হলে BC-এর উপর অঙ্কিত মধ্যমা AD-এর দৈর্ঘ্য কত?", ok, setw(ok, [fr(F(math.isqrt(m.numerator), math.isqrt(m.denominator)) + 1), fr(F(bb + c, 2)), fr(F(math.isqrt(m.numerator), math.isqrt(m.denominator)) * 2), fr(F(a, 2))]), f"AD² = (2·{bb}² + 2·{c}² − {a}²)/4 = {fr(m)}।", M)
def m_side_from_med(b):
    a, bb = R.randint(4, 16), R.randint(4, 16); ad = R.randint(2, 14)
    # AB² + AC² = 2(AD² + BD²), BC = 2·BD = a → AC² = 2AD² + a²/2 − AB²
    if a % 2: return
    v = 2 * ad * ad + a * a // 2 - bb * bb
    if v <= 0 or math.isqrt(v) ** 2 != v: return
    ac = math.isqrt(v)
    if not (ac + bb > a and ac + a > bb and a + bb > ac): return
    b.add(f"ΔABC-এ BC = {a} সেমি, AB = {bb} সেমি এবং মধ্যমা AD = {ad} সেমি হলে AC = কত সেমি?", ac, setw(ac, [ac + 1, ac - 1, ad, bb + 1]), f"AB² + AC² = 2(AD² + BD²) ⇒ AC² = 2({ad * ad} + {(a // 2) ** 2}) − {bb * bb} = {v}।", M)
def m_obtuse(b):
    ac, bc, cd = R.randint(3, 12), R.randint(3, 12), R.randint(1, 6)
    if cd >= ac: return
    v = ac * ac + bc * bc + 2 * bc * cd
    b.add(f"ΔABC-এ ∠ACB স্থূলকোণ; BC-এর বর্ধিতাংশের উপর AD লম্ব। AC = {ac}, BC = {bc}, CD = {cd} হলে AB² = কত?", v, setw(v, [ac * ac + bc * bc, ac * ac + bc * bc - 2 * bc * cd, v + bc, ac * ac + bc * bc + bc * cd]), f"AB² = AC² + BC² + 2BC·CD = {ac * ac} + {bc * bc} + {2 * bc * cd} = {v}।", M)
def m_acute(b):
    ac, bc, cd = R.randint(4, 14), R.randint(4, 14), R.randint(1, 6)
    if cd >= min(ac, bc): return
    v = ac * ac + bc * bc - 2 * bc * cd
    b.add(f"ΔABC-এ ∠ACB সূক্ষ্মকোণ; BC-এর উপর AD লম্ব। AC = {ac}, BC = {bc}, CD = {cd} হলে AB² = কত?", v, setw(v, [ac * ac + bc * bc, ac * ac + bc * bc + 2 * bc * cd, v - bc, ac * ac + bc * bc - bc * cd]), f"AB² = AC² + BC² − 2BC·CD = {v}।", M)
def m_proj(b):
    a, bb, c = R.choice(TRI)
    # c² = a² + b² − 2a·CD (∠C সূক্ষ্ম) ⇒ CD = (a² + b² − c²)/(2a)
    t = a * a + bb * bb - c * c
    if t <= 0: return
    cd = F(t, 2 * a)
    b.add(f"ΔABC-এ BC = {a}, CA = {bb}, AB = {c} এবং A থেকে BC-এর উপর লম্ব AD হলে CD = কত?", fr(cd), setw(fr(cd), [fr(F(t, a)), fr(cd + 1), fr(F(a * a + c * c - bb * bb, 2 * a)) if a * a + c * c - bb * bb > 0 else fr(cd * 2), fr(F(t, 2 * bb))]), f"AB² = AC² + BC² − 2BC·CD ⇒ CD = ({bb}² + {a}² − {c}²)/(2·{a}) = {fr(cd)}।", M)
def m_cent(b):
    a, bb, c = R.choice(TRI); m = med2(a, bb, c)
    if not perfect(m): return
    ok = sq(m * 4 / 9)
    b.add(f"ΔABC-এ BC = {a}, CA = {bb}, AB = {c} এবং G ভরকেন্দ্র হলে AG = কত? (AD মধ্যমা)", ok, setw(ok, [sq(m), sq(m / 9), sq(m / 4), fr(F(math.isqrt(m.numerator), math.isqrt(m.denominator)) * 2 / 3 + 1)]), f"AD² = {fr(m)}; AG = (2/3)AD।", M)
def h_sum_med(b):
    a, bb, c = R.choice(TRI)
    v = F(3 * (a * a + bb * bb + c * c), 4)
    b.add(f"ΔABC-এর বাহু {a}, {bb}, {c} একক হলে মধ্যমাত্রয়ের বর্গের সমষ্টি কত?", fr(v), setw(fr(v), [str(a * a + bb * bb + c * c), fr(v * F(2, 3)), fr(F(a * a + bb * bb + c * c, 2)), fr(v + 1)]), f"(3/4)({a * a} + {bb * bb} + {c * c}) = {fr(v)}।", H)
def h_gsq(b):
    a, bb, c = R.choice(TRI)
    v = F(a * a + bb * bb + c * c, 3)
    b.add(f"ΔABC-এর বাহু {a}, {bb}, {c} এবং G ভরকেন্দ্র হলে GA² + GB² + GC² = কত?", fr(v), setw(fr(v), [fr(F(3 * (a * a + bb * bb + c * c), 4)), str(a * a + bb * bb + c * c), fr(v * 2), fr(v + 3)]), f"GA² + GB² + GC² = (a² + b² + c²)/3 = {fr(v)}।", H)
def h_side_from_two(b):
    ab, ac = R.randint(5, 15), R.randint(5, 15); bc = 2 * R.randint(2, 10)
    if not (ab + ac > bc and abs(ab - ac) < bc): return
    m = F(2 * ab * ab + 2 * ac * ac - bc * bc, 4)
    if not perfect(m): return
    ok = sq(m)
    b.add(f"ΔABC-এ AB = {ab}, AC = {ac}, BC = {bc} সেমি এবং D, BC-এর মধ্যবিন্দু হলে AD = কত সেমি?", ok, setw(ok, [sq(m + 4), sq(F(ab * ab + ac * ac, 2)), sq(m * 4), str(bc // 2)]), f"AD² = (2·{ab * ab} + 2·{ac * ac} − {bc * bc})/4 = {fr(m)}।", H)
def h_para(b):
    a, c = R.randint(3, 12), R.randint(3, 12); d1 = R.randint(4, 20)
    # সামান্তরিকের কর্ণের বর্গের সমষ্টি = 2(a² + b²)
    t = 2 * (a * a + c * c) - d1 * d1
    if t <= 0 or math.isqrt(t) ** 2 != t: return
    d2 = math.isqrt(t)
    b.add(f"একটি সামান্তরিকের দুটি সন্নিহিত বাহু {a} ও {c} সেমি এবং একটি কর্ণ {d1} সেমি হলে অপর কর্ণ কত সেমি?", d2, setw(d2, [d2 + 1, d1, a + c, d2 - 1]), f"d₁² + d₂² = 2(a² + b²) ⇒ d₂² = {2 * (a * a + c * c)} − {d1 * d1} = {t}।", H)
p31 = run('3.1', R, fx31, [e_ag, e_gd, e_apo, e_hyp, e_ctype], [m_median, m_side_from_med, m_obtuse, m_acute, m_proj, m_cent], [h_sum_med, h_gsq, h_side_from_two, h_para])

# ---------------- 3.2 ত্রিভুজের কেন্দ্র, টলেমি, বৃত্তস্থ চতুর্ভুজ ----------------
HERON = [(a, b, c) for (a, b, c) in TRI if (lambda s2: (lambda p: p > 0 and math.isqrt(p) ** 2 == p)(s2 * (s2 - 2 * a) * (s2 - 2 * b) * (s2 - 2 * c)))(a + b + c) and (a + b + c) % 2 == 0]
def area(a, b, c):
    s = F(a + b + c, 2); p = s * (s - a) * (s - b) * (s - c)
    return F(math.isqrt(int(p)))
fx32 = [
 ("ত্রিভুজের কোণত্রয়ের সমদ্বিখণ্ডকগুলো যে বিন্দুতে মিলিত হয় তাকে কী বলে?", "অন্তঃকেন্দ্র", ["পরিকেন্দ্র", "ভরকেন্দ্র", "লম্ববিন্দু"], "অন্তর্বৃত্তের কেন্দ্র।", E),
 ("ত্রিভুজের বাহুগুলোর লম্বদ্বিখণ্ডকগুলো যে বিন্দুতে মিলিত হয় তাকে কী বলে?", "পরিকেন্দ্র", ["অন্তঃকেন্দ্র", "ভরকেন্দ্র", "লম্ববিন্দু"], "পরিবৃত্তের কেন্দ্র।", E),
 ("ত্রিভুজের শীর্ষ থেকে বিপরীত বাহুর উপর লম্বত্রয় যে বিন্দুতে মিলিত হয় তাকে কী বলে?", "লম্ববিন্দু", ["অন্তঃকেন্দ্র", "পরিকেন্দ্র", "ভরকেন্দ্র"], "উচ্চতাত্রয়ের ছেদবিন্দু।", E),
 ("বৃত্তস্থ চতুর্ভুজের বিপরীত কোণদ্বয়ের সমষ্টি কত?", "180°", ["90°", "360°", "120°"], "বৃত্তস্থ চতুর্ভুজের ধর্ম।", E),
 ("টলেমির উপপাদ্য অনুযায়ী বৃত্তস্থ চতুর্ভুজ ABCD-এর জন্য AC·BD = কত?", "AB·CD + AD·BC", ["AB·BC + CD·DA", "AB·CD − AD·BC", "AB² + CD²"], "কর্ণদ্বয়ের গুণফল = বিপরীত বাহুর গুণফলের সমষ্টি।", E),
 ("নববিন্দু বৃত্তের ব্যাসার্ধ পরিবৃত্তের ব্যাসার্ধের কত অংশ?", "অর্ধেক", ["সমান", "দ্বিগুণ", "এক-তৃতীয়াংশ"], "নববিন্দু বৃত্তের ব্যাসার্ধ R/2।", M),
 ("নববিন্দু বৃত্ত কোন বিন্দুগুলো দিয়ে যায়?", "বাহুর মধ্যবিন্দু, উচ্চতার পাদবিন্দু ও লম্ববিন্দু-শীর্ষের সংযোগ রেখার মধ্যবিন্দু", ["শুধু শীর্ষবিন্দু", "অন্তঃকেন্দ্র ও পরিকেন্দ্র", "শুধু বাহুর মধ্যবিন্দু"], "মোট নয়টি বিন্দু।", M),
 ("সমকোণী ত্রিভুজের লম্ববিন্দু কোথায় থাকে?", "সমকোণী শীর্ষবিন্দুতে", ["অতিভুজের মধ্যবিন্দুতে", "ত্রিভুজের বাইরে", "ভরকেন্দ্রে"], "সমকোণ সংলগ্ন বাহু দুটিই উচ্চতা।", M),
 ("স্থূলকোণী ত্রিভুজের পরিকেন্দ্র কোথায় থাকে?", "ত্রিভুজের বাইরে", ["ত্রিভুজের ভিতরে", "একটি বাহুর উপর", "একটি শীর্ষে"], "স্থূলকোণী হলে পরিকেন্দ্র বাইরে।", M),
 ("সমবাহু ত্রিভুজের ভরকেন্দ্র, অন্তঃকেন্দ্র, পরিকেন্দ্র ও লম্ববিন্দু—", "একই বিন্দু", ["ভিন্ন ভিন্ন", "একই রেখায় নয়", "দুটি দুটি করে সমান"], "সমবাহু ত্রিভুজে সব কেন্দ্র মিলে যায়।", E),
 ("পরিকেন্দ্র, ভরকেন্দ্র ও লম্ববিন্দু যে রেখায় থাকে তাকে কী বলে?", "অয়লার রেখা", ["সিমসন রেখা", "মধ্যমা", "স্পর্শক"], "অয়লার রেখা।", H),
]
def e_cyc(b):
    a = R.randint(40, 140)
    b.add(f"বৃত্তস্থ চতুর্ভুজ ABCD-এ ∠A = {a}° হলে ∠C = কত?", f"{180 - a}°", setw(f"{180 - a}°", [f"{a}°", f"{360 - a}°", f"{90 - a}°" if a < 90 else f"{a - 90}°", f"{180 - a + 10}°"]), "বিপরীত কোণের সমষ্টি 180°।", E)
def e_ext(b):
    a = R.randint(50, 130)
    b.add(f"বৃত্তস্থ চতুর্ভুজ ABCD-এর ∠ABC = {a}° হলে D বিন্দুতে বহিঃস্থ কোণ (CD-কে বর্ধিত করে) কত?", f"{a}°", setw(f"{a}°", [f"{180 - a}°", f"{90 + a // 2}°", f"{360 - a}°", f"{a + 10}°"]), "বৃত্তস্থ চতুর্ভুজের বহিঃস্থ কোণ অন্তঃস্থ বিপরীত কোণের সমান।", E)
def e_boc(b):
    a = R.randint(25, 85)
    b.add(f"ΔABC-এর পরিকেন্দ্র O এবং ∠A = {a}° হলে ∠BOC = কত?", f"{2 * a}°", setw(f"{2 * a}°", [f"{a}°", f"{180 - a}°", f"{90 + a // 2}°" if a % 2 == 0 else f"{90 + a}°", f"{180 - 2 * a}°"]), "কেন্দ্রস্থ কোণ বৃত্তস্থ কোণের দ্বিগুণ।", E)
def e_bic(b):
    a = 2 * R.randint(15, 60)
    b.add(f"ΔABC-এর অন্তঃকেন্দ্র I এবং ∠A = {a}° হলে ∠BIC = কত?", f"{90 + a // 2}°", setw(f"{90 + a // 2}°", [f"{2 * a}°", f"{180 - a}°", f"{90 - a // 2}°", f"{a}°"]), "∠BIC = 90° + A/2।", E)
def m_bhc(b):
    a = R.randint(30, 85)
    b.add(f"ΔABC-এর লম্ববিন্দু H এবং ∠A = {a}° হলে ∠BHC = কত?", f"{180 - a}°", setw(f"{180 - a}°", [f"{2 * a}°", f"{90 + a // 2}°", f"{a}°", f"{90 - a}°" if a < 90 else f"{a - 45}°"]), "∠BHC = 180° − A।", M)
def m_ptol(b):
    ab, bc, cd, da = (R.randint(2, 12) for _ in range(4)); ac = R.randint(4, 15)
    t = ab * cd + da * bc
    if t % ac: return
    bd = t // ac
    b.add(f"বৃত্তস্থ চতুর্ভুজ ABCD-এ AB = {ab}, BC = {bc}, CD = {cd}, DA = {da} এবং কর্ণ AC = {ac} হলে কর্ণ BD = কত?", bd, setw(bd, [bd + 1, (ab * bc + cd * da) // ac if (ab * bc + cd * da) % ac == 0 else bd + 2, t, bd - 1]), f"টলেমি: AC·BD = AB·CD + AD·BC = {t} ⇒ BD = {bd}।", M)
def m_inr(b):
    a, bb, c = R.choice(HERON); A = area(a, bb, c); s = F(a + bb + c, 2); r = A / s
    b.add(f"কোনো ত্রিভুজের বাহু {a}, {bb}, {c} একক হলে অন্তর্ব্যাসার্ধ কত একক?", fr(r), setw(fr(r), [fr(A / (2 * s)), fr(F(a * bb * c) / (4 * A)), fr(r + 1), fr(A)]), f"Δ = {A}, s = {fr(s)}; r = Δ/s = {fr(r)}।", M)
def m_circ(b):
    a, bb, c = R.choice(HERON); A = area(a, bb, c); Rr = F(a * bb * c) / (4 * A)
    b.add(f"কোনো ত্রিভুজের বাহু {a}, {bb}, {c} একক হলে পরিব্যাসার্ধ কত একক?", fr(Rr), setw(fr(Rr), [fr(A / F(a + bb + c, 2)), fr(Rr * 2), fr(Rr / 2), fr(Rr + 1)]), f"Δ = {A}; R = abc/(4Δ) = {fr(Rr)}।", M)
def m_heron(b):
    a, bb, c = R.choice(HERON); A = area(a, bb, c)
    b.add(f"কোনো ত্রিভুজের বাহু {a}, {bb}, {c} সেমি হলে ক্ষেত্রফল কত বর্গ সেমি?", A, setw(A, [A * 2, F(a * bb, 2), A + a, F(a + bb + c, 2)]), f"s = {fr(F(a + bb + c, 2))}; Δ = √(s(s − a)(s − b)(s − c)) = {A}।", M)
def m_nine(b):
    a, bb, c = R.choice(HERON); A = area(a, bb, c); Rr = F(a * bb * c) / (4 * A)
    b.add(f"কোনো ত্রিভুজের বাহু {a}, {bb}, {c} একক হলে নববিন্দু বৃত্তের ব্যাসার্ধ কত?", fr(Rr / 2), setw(fr(Rr / 2), [fr(Rr), fr(Rr * 2), fr(A / F(a + bb + c, 2)), fr(Rr / 3)]), f"R = {fr(Rr)}; নববিন্দু বৃত্তের ব্যাসার্ধ R/2 = {fr(Rr / 2)}।", M)
def m_rt_R(b):
    a, c = R.choice([(3, 4), (6, 8), (5, 12), (8, 15), (9, 12), (7, 24), (12, 16), (20, 21), (9, 40)]); h = math.isqrt(a * a + c * c)
    b.add(f"সমকোণী ত্রিভুজের সমকোণ সংলগ্ন বাহু {a} ও {c} হলে পরিব্যাসার্ধ কত?", fr(F(h, 2)), setw(fr(F(h, 2)), [str(h), fr(F(a + c - h, 2)), fr(F(a * c, 2)), fr(F(h, 4))]), f"অতিভুজ {h}; R = অতিভুজ/2 = {fr(F(h, 2))}।", M)
def h_brahma(b):
    a, bb, c, d = (R.randint(2, 14) for _ in range(4))
    s = F(a + bb + c + d, 2); p = (s - a) * (s - bb) * (s - c) * (s - d)
    if p <= 0 or p.denominator != 1 or math.isqrt(int(p)) ** 2 != p: return
    A = math.isqrt(int(p))
    if 2 * max(a, bb, c, d) >= a + bb + c + d: return
    b.add(f"একটি বৃত্তস্থ চতুর্ভুজের বাহু {a}, {bb}, {c}, {d} একক হলে ব্রহ্মগুপ্তের সূত্র অনুযায়ী ক্ষেত্রফল কত বর্গ একক?", A, setw(A, [A * 2, A + 2, a * c, int(s)]), f"s = {fr(s)}; ক্ষেত্রফল = √((s − a)(s − b)(s − c)(s − d)) = {A}।", H)
def h_rt_r(b):
    a, c = R.choice([(3, 4), (6, 8), (5, 12), (8, 15), (9, 12), (7, 24), (12, 16), (20, 21), (9, 40), (12, 35)]); h = math.isqrt(a * a + c * c)
    r = F(a + c - h, 2)
    b.add(f"সমকোণী ত্রিভুজের সমকোণ সংলগ্ন বাহু {a} ও {c} হলে অন্তর্ব্যাসার্ধ কত?", fr(r), setw(fr(r), [fr(F(h, 2)), fr(r + 1), fr(F(a * c, a + c + h)), fr(F(a + c, 4))]), f"r = (a + b − c)/2 = ({a} + {c} − {h})/2 = {fr(r)}।", H)
def h_rR(b):
    a, bb, c = R.choice(HERON); A = area(a, bb, c); s = F(a + bb + c, 2); r = A / s; Rr = F(a * bb * c) / (4 * A)
    v = Rr * r
    b.add(f"কোনো ত্রিভুজের বাহু {a}, {bb}, {c} একক হলে পরিব্যাসার্ধ ও অন্তর্ব্যাসার্ধের গুণফল কত?", fr(v), setw(fr(v), [fr(Rr + r), fr(v * 2), fr(Rr / r), fr(A)]), f"R = {fr(Rr)}, r = {fr(r)}; Rr = {fr(v)}।", H)
def h_aoc_cyc(b):
    a = R.randint(30, 80)
    b.add(f"O কেন্দ্রবিশিষ্ট বৃত্তে বৃত্তস্থ চতুর্ভুজ ABCD-এর ∠ABC = {180 - a}° হলে প্রবৃদ্ধ নয় এমন কেন্দ্রস্থ কোণ ∠AOC = কত?", f"{2 * a}°", setw(f"{2 * a}°", [f"{a}°", f"{360 - 2 * a}°", f"{180 - a}°", f"{2 * (180 - a)}°"]), f"∠ADC = 180° − {180 - a}° = {a}°; ∠AOC = 2 × {a}° = {2 * a}°।", H)
def h_ptol_sq(b):
    s = R.randint(2, 15)
    b.add(f"একটি বর্গের বাহু {s} সেমি। টলেমির উপপাদ্য প্রয়োগ করলে কর্ণদ্বয়ের গুণফল কত বর্গ সেমি?", 2 * s * s, setw(2 * s * s, [s * s, 4 * s * s, s * s + s, 2 * s]), f"AC·BD = AB·CD + AD·BC = {s * s} + {s * s} = {2 * s * s}।", H)
p32 = run('3.2', R, fx32, [e_cyc, e_ext, e_boc, e_bic], [m_bhc, m_ptol, m_inr, m_circ, m_heron, m_nine, m_rt_R], [h_brahma, h_rt_r, h_rR, h_aoc_cyc, h_ptol_sq])
save('h3', p31 + p32)

# ---------------- 4 জ্যামিতিক অঙ্কন ----------------
fx4 = [
 ("একটি সরলরেখাকে সমদ্বিখণ্ডিত করতে কোনটি আঁকা হয়?", "লম্বদ্বিখণ্ডক", ["কোণ সমদ্বিখণ্ডক", "স্পর্শক", "মধ্যমা"], "দুই প্রান্ত থেকে সমান ব্যাসার্ধে বৃত্তচাপ।", E),
 ("বৃত্তের বহিঃস্থ কোনো বিন্দু থেকে বৃত্তে কয়টি স্পর্শক আঁকা যায়?", "2টি", ["1টি", "3টি", "অসংখ্য"], "বহিঃস্থ বিন্দু থেকে দুটি স্পর্শক।", E),
 ("বৃত্তের উপরিস্থ কোনো বিন্দুতে কয়টি স্পর্শক আঁকা যায়?", "1টি", ["2টি", "0টি", "অসংখ্য"], "একটি স্পর্শক, ব্যাসার্ধের উপর লম্ব।", E),
 ("বৃত্তের অভ্যন্তরস্থ বিন্দু থেকে কয়টি স্পর্শক আঁকা যায়?", "0টি", ["1টি", "2টি", "অসংখ্য"], "অভ্যন্তর থেকে কোনো স্পর্শক সম্ভব নয়।", E),
 ("স্পর্শবিন্দুতে অঙ্কিত ব্যাসার্ধ ও স্পর্শকের মধ্যবর্তী কোণ কত?", "90°", ["45°", "60°", "180°"], "স্পর্শক ব্যাসার্ধের উপর লম্ব।", E),
 ("তিনটি অসমরেখ বিন্দু দিয়ে কয়টি বৃত্ত আঁকা যায়?", "1টি", ["2টি", "3টি", "অসংখ্য"], "একটি ও কেবল একটি বৃত্ত।", E),
 ("ত্রিভুজের পরিবৃত্ত আঁকতে কোনগুলো আঁকতে হয়?", "বাহুর লম্বদ্বিখণ্ডক", ["কোণের সমদ্বিখণ্ডক", "মধ্যমা", "উচ্চতা"], "লম্বদ্বিখণ্ডকের ছেদবিন্দু পরিকেন্দ্র।", E),
 ("ত্রিভুজের অন্তর্বৃত্ত আঁকতে কোনগুলো আঁকতে হয়?", "কোণের সমদ্বিখণ্ডক", ["বাহুর লম্বদ্বিখণ্ডক", "মধ্যমা", "উচ্চতা"], "কোণ সমদ্বিখণ্ডকের ছেদবিন্দু অন্তঃকেন্দ্র।", E),
 ("দুটি রেখাংশ a ও b-এর মধ্যসমানুপাতী কোনটি?", "√(ab)", ["(a + b)/2", "ab", "a/b"], "a : x = x : b ⇒ x² = ab।", E),
 ("কোনো রেখাংশকে অন্তঃস্থভাবে মধ্য ও প্রান্তিক অনুপাতে বিভক্ত করা মানে—", "সমগ্র রেখাংশ : বৃহত্তর অংশ = বৃহত্তর অংশ : ক্ষুদ্রতর অংশ", ["দুই অংশ সমান করা", "অংশ দুটির অনুপাত 1 : 2 করা", "রেখাংশকে তিন ভাগ করা"], "স্বর্ণ অনুপাতে বিভক্তি।", M),
 ("ত্রিভুজ অঙ্কনের জন্য তিনটি বাহু দেওয়া থাকলে কোন শর্ত লাগে?", "যেকোনো দুই বাহুর সমষ্টি তৃতীয় বাহু অপেক্ষা বৃহত্তর", ["তিন বাহু সমান", "একটি কোণ সমকোণ", "পরিসীমা জোড়"], "ত্রিভুজের অসমতা।", E),
 ("কোনটি দিয়ে একটি অনন্য ত্রিভুজ আঁকা যায় না?", "তিনটি কোণ", ["তিনটি বাহু", "দুই বাহু ও অন্তর্ভুক্ত কোণ", "দুই কোণ ও অন্তর্ভুক্ত বাহু"], "তিন কোণ দিয়ে অসংখ্য সদৃশ ত্রিভুজ হয়।", M),
 ("স্বর্ণ অনুপাতের মান প্রায় কত?", "1.618", ["1.414", "1.732", "3.14"], "(1 + √5)/2 ≈ 1.618।", M),
 ("বহিঃস্থ বিন্দু থেকে বৃত্তে অঙ্কিত দুটি স্পর্শকের দৈর্ঘ্য কেমন?", "সমান", ["অসমান", "একটি অপরটির দ্বিগুণ", "যোগফল ব্যাসের সমান"], "স্পর্শকদ্বয় সমান।", E),
 ("দুটি বৃত্ত পরস্পরকে বহিঃস্থভাবে স্পর্শ করলে সাধারণ স্পর্শক কয়টি?", "3টি", ["2টি", "4টি", "1টি"], "দুটি সরাসরি ও একটি অনুপ্রস্থ (স্পর্শবিন্দুতে)।", M),
 ("দুটি বৃত্ত পরস্পরকে ছেদ বা স্পর্শ না করে পরস্পরের বাইরে থাকলে সাধারণ স্পর্শক কয়টি?", "4টি", ["2টি", "3টি", "1টি"], "দুটি সরাসরি ও দুটি অনুপ্রস্থ।", M),
 ("দুটি বৃত্ত দুটি বিন্দুতে ছেদ করলে সাধারণ স্পর্শক কয়টি?", "2টি", ["3টি", "4টি", "1টি"], "শুধু দুটি সরাসরি সাধারণ স্পর্শক।", M),
 ("একটি বৃত্ত অপরটিকে অন্তঃস্থভাবে স্পর্শ করলে সাধারণ স্পর্শক কয়টি?", "1টি", ["0টি", "2টি", "3টি"], "স্পর্শবিন্দুতে একটি।", M),
 ("একটি সমকোণ আঁকতে কম্পাস দিয়ে কোন কোণ দুবার নেওয়া হয়?", "60°", ["30°", "45°", "90°"], "60° + 30° (60°-এর অর্ধেক) = 90°; ধাপে 60° চাপ ব্যবহার হয়।", M),
 ("রেখাংশকে সমান n ভাগে ভাগ করতে কোন উপপাদ্য ব্যবহৃত হয়?", "সমান্তরাল রেখার ছেদাংশ উপপাদ্য", ["পিথাগোরাস", "টলেমি", "অ্যাপোলোনিয়াস"], "সমান্তরাল রেখা সমান অংশ ছেদ করে।", H),
]
def e_meanp(b):
    a, c = R.choice([(2, 8), (4, 9), (3, 12), (1, 16), (4, 16), (2, 18), (5, 20), (3, 27), (8, 18), (9, 16), (4, 25), (6, 24), (2, 32), (12, 27), (7, 28)])
    v = math.isqrt(a * c)
    b.add(f"{a} সেমি ও {c} সেমি দৈর্ঘ্যের রেখাংশের মধ্যসমানুপাতী রেখাংশের দৈর্ঘ্য কত সেমি?", v, setw(v, [F(a + c, 2), a * c, v + 1, c - a]), f"√({a} × {c}) = {v}।", E)
def e_ratio(b):
    m, n = R.sample(range(1, 7), 2); k = R.randint(1, 4); L = (m + n) * k
    if math.gcd(m, n) > 1: return
    b.add(f"{L} সেমি দৈর্ঘ্যের একটি রেখাংশকে {m} : {n} অনুপাতে অন্তর্বিভক্ত করলে বৃহত্তর অংশ কত সেমি?", max(m, n) * k, setw(max(m, n) * k, [min(m, n) * k, L // 2 if L % 2 == 0 else L - 1, max(m, n) * k + 1, L]), f"বৃহত্তর অংশ = {L} × {max(m, n)}/{m + n} = {max(m, n) * k}।", E)
def e_tri_ok(b):
    a, c, d = (R.randint(2, 15) for _ in range(3))
    ok = 'হ্যাঁ, আঁকা যাবে' if a + c > d and a + d > c and c + d > a else 'না, আঁকা যাবে না'
    b.add(f"{a} সেমি, {c} সেমি ও {d} সেমি বাহুবিশিষ্ট ত্রিভুজ আঁকা যাবে কি?", ok, ['হ্যাঁ, আঁকা যাবে', 'না, আঁকা যাবে না', 'শুধু সমকোণী হলে', 'শুধু সমবাহু হলে'], "যেকোনো দুই বাহুর সমষ্টি তৃতীয় বাহু অপেক্ষা বৃহত্তর হতে হবে।", E)
def e_third(b):
    a, c = R.randint(3, 15), R.randint(3, 15)
    ok = f"{abs(a - c)} < x < {a + c}"
    b.add(f"ত্রিভুজের দুই বাহু {a} সেমি ও {c} সেমি হলে তৃতীয় বাহু x-এর সম্ভাব্য সীমা কোনটি?", ok, setw(ok, [f"0 < x < {a + c}", f"{abs(a - c)} ≤ x ≤ {a + c}", f"x > {a + c}", f"{min(a, c)} < x < {max(a, c)}"]), "|a − b| < x < a + b।", E)
def e_tang(b):
    r, t = R.choice([(3, 4), (5, 12), (6, 8), (8, 15), (7, 24), (9, 12), (12, 16), (20, 21)])
    d = math.isqrt(r * r + t * t)
    b.add(f"{r} সেমি ব্যাসার্ধের বৃত্তের কেন্দ্র থেকে {d} সেমি দূরের একটি বিন্দু থেকে অঙ্কিত স্পর্শকের দৈর্ঘ্য কত সেমি?", t, setw(t, [d - r, d + r, r, t + 1]), f"√({d}² − {r}²) = {t}।", E)
def m_angle_poly(b):
    n = R.choice([5, 6, 8, 9, 10, 12, 15, 18, 20])
    v = F(180 * (n - 2), n)
    b.add(f"একটি সুষম {n} বাহুবিশিষ্ট বহুভুজের প্রতিটি অন্তঃকোণ কত ডিগ্রি?", f"{fr(v)}°", setw(f"{fr(v)}°", [f"{fr(F(360, n))}°", f"{180 * (n - 2)}°", f"{fr(F(180 * (n - 1), n))}°", f"{fr(v + 10)}°"]), f"{180}({n} − 2)/{n} = {fr(v)}°।", M)
def m_ext_poly(b):
    n = R.choice([5, 6, 8, 9, 10, 12, 15, 18, 20, 24, 30, 36])
    b.add(f"একটি সুষম বহুভুজের প্রতিটি বহিঃকোণ {fr(F(360, n))}° হলে বাহু কয়টি?", n, setw(n, [n + 1, n - 2, n * 2, 360 // n if 360 // n != n else n + 3]), f"বাহু = 360/{fr(F(360, n))} = {n}।", M)
def m_mp_find(b):
    a, x = R.randint(1, 9), R.randint(2, 12)
    if x * x % a: return
    c = x * x // a
    if c == a: return
    b.add(f"a = {a} সেমি এবং a ও b-এর মধ্যসমানুপাতী {x} সেমি হলে b = কত সেমি?", c, setw(c, [x * a, 2 * x - a, c + 1, x]), f"{x}² = {a} × b ⇒ b = {c}।", M)
def m_golden(b):
    L = R.choice([2, 4, 6, 8, 10, 12, 14, 16, 20])
    # বৃহত্তর অংশ x: L/x = x/(L − x) ⇒ x² + Lx − L² = 0 ⇒ x = L(√5 − 1)/2
    h = L // 2
    ok = f"{h if h > 1 else ''}(√5 − 1)" if h != 1 else "√5 − 1"
    b.add(f"{L} সেমি রেখাংশকে মধ্য ও প্রান্তিক অনুপাতে বিভক্ত করলে বৃহত্তর অংশ কত সেমি?", ok, setw(ok, [f"{h if h > 1 else ''}(√5 + 1)", f"{h if h > 1 else ''}(3 − √5)", f"{L}/2", f"{h if h > 1 else ''}√5"]), f"x² + {L}x − {L * L} = 0 ⇒ x = {L}(√5 − 1)/2।", M)
def m_ext_div(b):
    m, n = R.sample(range(1, 8), 2); k = R.randint(1, 4)
    if m == n: return
    L = abs(m - n) * k
    # বহির্বিভক্ত: AP : PB = m : n, P বাইরে; AP = m k, PB = n k
    big = max(m, n) * k
    b.add(f"AB = {L} সেমি রেখাংশকে P বিন্দুতে {max(m, n)} : {min(m, n)} অনুপাতে বহির্বিভক্ত করলে AP = কত সেমি?", big, setw(big, [min(m, n) * k, L, big + L, F(L * max(m, n), m + n)]), f"AP − PB = {L}, AP : PB = {max(m, n)} : {min(m, n)} ⇒ AP = {big}।", M)
def m_inscribed_sq(b):
    r = R.randint(2, 15)
    ok = surd(2, r)
    b.add(f"{r} সেমি ব্যাসার্ধের বৃত্তে অন্তর্লিখিত বর্গের বাহু কত সেমি?", ok, setw(ok, [str(2 * r), str(r), surd(3, r), surd(2, 2 * r)]), f"কর্ণ = ব্যাস = {2 * r}; বাহু = {2 * r}/√2 = {ok}।", M)
def m_hexagon(b):
    r = R.randint(2, 20)
    b.add(f"{r} সেমি ব্যাসার্ধের বৃত্তে অন্তর্লিখিত সুষম ষড়ভুজের বাহু কত সেমি?", r, setw(r, [2 * r, F(r, 2), surd(3, r), r + 1]), "সুষম ষড়ভুজের বাহু = বৃত্তের ব্যাসার্ধ।", M)
def m_eq_inr(b):
    a = 2 * R.randint(1, 10)
    # সমবাহু ত্রিভুজ বাহু a, r = a/(2√3) = a√3/6, R = a/√3 = a√3/3
    g = math.gcd(a, 6); ok = (f"{a // g if a // g > 1 else ''}√3/{6 // g}" if 6 // g > 1 else f"{a // g}√3")
    g3 = math.gcd(a, 3); okR = (f"{a // g3 if a // g3 > 1 else ''}√3/{3 // g3}" if 3 // g3 > 1 else f"{a // g3}√3")
    b.add(f"{a} সেমি বাহুবিশিষ্ট সমবাহু ত্রিভুজের অন্তর্বৃত্তের ব্যাসার্ধ কত সেমি?", ok, setw(ok, [okR, f"{a}√3/2" if a > 1 else '√3/2', str(a // 2), f"{a}/3"]), f"r = a/(2√3) = {ok}।", M)
def h_common_tan(b):
    r1, r2 = R.randint(2, 9), R.randint(2, 9); d = R.randint(r1 + r2 + 1, r1 + r2 + 15)
    if r1 == r2: return
    t = d * d - (r1 - r2) ** 2
    if math.isqrt(t) ** 2 != t: return
    v = math.isqrt(t)
    b.add(f"{r1} সেমি ও {r2} সেমি ব্যাসার্ধের দুটি বৃত্তের কেন্দ্রদ্বয়ের দূরত্ব {d} সেমি হলে সরাসরি সাধারণ স্পর্শকের দৈর্ঘ্য কত সেমি?", v, setw(v, [d, math.isqrt(d * d - (r1 + r2) ** 2) if d * d - (r1 + r2) ** 2 > 0 else v + 2, v + 1, d - r1 - r2]), f"√(d² − (r₁ − r₂)²) = √({d * d} − {(r1 - r2) ** 2}) = {v}।", H)
def h_trans_tan(b):
    r1, r2 = R.randint(2, 9), R.randint(2, 9); d = R.randint(r1 + r2 + 1, r1 + r2 + 15)
    t = d * d - (r1 + r2) ** 2
    if math.isqrt(t) ** 2 != t: return
    v = math.isqrt(t)
    w = math.isqrt(d * d - (r1 - r2) ** 2) if math.isqrt(d * d - (r1 - r2) ** 2) ** 2 == d * d - (r1 - r2) ** 2 else v + 3
    b.add(f"{r1} সেমি ও {r2} সেমি ব্যাসার্ধের দুটি বৃত্তের কেন্দ্রদ্বয়ের দূরত্ব {d} সেমি হলে অনুপ্রস্থ (তির্যক) সাধারণ স্পর্শকের দৈর্ঘ্য কত সেমি?", v, setw(v, [w, d, v + 1, d - r1 - r2]), f"√(d² − (r₁ + r₂)²) = √({d * d} − {(r1 + r2) ** 2}) = {v}।", H)
def h_circ_rel(b):
    r1, r2 = R.randint(2, 10), R.randint(2, 10)
    if r1 == r2: return
    kind = R.choice(['ext', 'int', 'cut', 'out'])
    d = {'ext': r1 + r2, 'int': abs(r1 - r2), 'cut': R.randint(abs(r1 - r2) + 1, r1 + r2 - 1), 'out': r1 + r2 + R.randint(1, 6)}[kind]
    if kind == 'cut' and abs(r1 - r2) + 1 > r1 + r2 - 1: return
    n = {'ext': 3, 'int': 1, 'cut': 2, 'out': 4}[kind]
    b.add(f"{r1} সেমি ও {r2} সেমি ব্যাসার্ধের দুটি বৃত্তের কেন্দ্রদ্বয়ের দূরত্ব {d} সেমি হলে সাধারণ স্পর্শক কয়টি?", f"{n}টি", setw(f"{n}টি", ['1টি', '2টি', '3টি', '4টি']), "কেন্দ্র-দূরত্বের সাথে r₁ + r₂ ও |r₁ − r₂| তুলনা করে।", H)
def h_mp_area(b):
    a, c = R.choice([(2, 8), (4, 9), (3, 12), (4, 16), (2, 18), (5, 20), (3, 27), (8, 18), (9, 16), (4, 25), (6, 24)])
    s = math.isqrt(a * c)
    b.add(f"{a} সেমি × {c} সেমি আয়তক্ষেত্রের সমান ক্ষেত্রফলবিশিষ্ট বর্গ আঁকতে বর্গের বাহু কত সেমি নিতে হবে?", s, setw(s, [F(a + c, 2), a * c, s + 1, 2 * s]), f"বর্গের বাহু = √({a} × {c}) = {s} (মধ্যসমানুপাতী)।", H)
def h_area_tri_sq(b):
    bs, h = 2 * R.randint(2, 12), R.randint(2, 18)
    A = bs * h // 2; s = math.isqrt(A)
    if s * s != A: return
    b.add(f"ভূমি {bs} সেমি ও উচ্চতা {h} সেমি বিশিষ্ট ত্রিভুজের সমান ক্ষেত্রফলের বর্গের বাহু কত সেমি?", s, setw(s, [math.isqrt(bs * h) if math.isqrt(bs * h) ** 2 == bs * h else s + 2, s + 1, A, bs // 2]), f"ক্ষেত্রফল = {A}; বাহু = √{A} = {s}।", H)
p4 = run(None, R, fx4, [e_meanp, e_ratio, e_tri_ok, e_third, e_tang], [m_angle_poly, m_ext_poly, m_mp_find, m_golden, m_ext_div, m_inscribed_sq, m_hexagon, m_eq_inr], [h_common_tan, h_trans_tan, h_circ_rel, h_mp_area, h_area_tri_sq])
save('h4', p4)
