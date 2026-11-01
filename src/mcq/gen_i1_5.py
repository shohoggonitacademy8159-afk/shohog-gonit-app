#!/usr/bin/env python3
"""একাদশ শ্রেণি উচ্চতর গণিত ১ম পত্র (h11) অধ্যায় 1–5। অনুশীলনী id: '1.A' (দেখায় 1(A))।
1.A ম্যাট্রিক্স · 1.B নির্ণায়ক · 2.A ভেক্টরের ধারণা ও যোগ · 2.B ত্রিমাত্রিক ভেক্টর · 2.C ডট ও ক্রস গুণন
3.A দূরত্ব ও পোলার স্থানাঙ্ক · 3.B বিভাজন ও ভরকেন্দ্র · 3.C ক্ষেত্রফল · 3.D ঢাল ও সঞ্চারপথ · 3.E সরলরেখার সমীকরণ
3.F ছেদবিন্দু, সমান্তরাল ও লম্ব রেখা, কোণ · 3.G লম্ব দূরত্ব ও সমান্তরাল রেখার দূরত্ব · 4.A বৃত্তের সমীকরণ · 4.B স্পর্শক ও জ্যা
5.A বিন্যাস · 5.B সমাবেশ"""
import random, pathlib, sys, math
from fractions import Fraction as F
sys.path.insert(0, str(pathlib.Path(__file__).resolve().parent))
from mcqlib import run, save, E, M, H, fr, near, num, pfmt, surd, sup

R = random.Random(2026110111)
def W(c, pool):
    out = []
    for w in pool:
        w = str(w)
        if w != str(c) and w not in out: out.append(w)
    return out
def nz(a, b): return R.choice([v for v in range(a, b + 1) if v])
def mat(m): return '[' + ', '.join('(' + ', '.join(num(x) for x in r) + ')' for r in m) + ']'
def det2(m): return m[0][0] * m[1][1] - m[0][1] * m[1][0]
def det3(m):
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1]) - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0]) + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))
def r2(): return [[R.randint(-5, 6) for _ in range(2)] for _ in range(2)]
def mul(a, b): return [[sum(a[i][k] * b[k][j] for k in range(len(b))) for j in range(len(b[0]))] for i in range(len(a))]
def sqf(v):
    r = math.isqrt(v)
    return str(r) if r * r == v else surd(v)
P = lambda x, y: f"({num(x)}, {num(y)})"

# ---------------- 1.A ম্যাট্রিক্স ----------------
fx1a = [
 ("m × n ক্রমের ম্যাট্রিক্সে কয়টি ভুক্তি থাকে?", "mn", ["m + n", "m²", "n²"], "সারি m, কলাম n।", E),
 ("যে বর্গ ম্যাট্রিক্সের মুখ্য কর্ণের সব ভুক্তি 1 ও বাকি সব 0, তাকে কী বলে?", "অভেদক (একক) ম্যাট্রিক্স", ["শূন্য ম্যাট্রিক্স", "কর্ণ ম্যাট্রিক্স নয় এমন", "স্কেলার ম্যাট্রিক্স নয়"], "I দিয়ে প্রকাশ করা হয়।", E),
 ("Aᵀ = A হলে A কোন ধরনের ম্যাট্রিক্স?", "প্রতিসম ম্যাট্রিক্স", ["বিপ্রতিসম ম্যাট্রিক্স", "শূন্য ম্যাট্রিক্স", "অভেদক ম্যাট্রিক্স"], "ট্রান্সপোজ নিজের সমান।", E),
 ("Aᵀ = −A হলে A কোন ধরনের ম্যাট্রিক্স?", "বিপ্রতিসম ম্যাট্রিক্স", ["প্রতিসম ম্যাট্রিক্স", "কর্ণ ম্যাট্রিক্স", "অভেদক ম্যাট্রিক্স"], "বিপ্রতিসমের মুখ্য কর্ণ শূন্য।", M),
 ("A ম্যাট্রিক্সের ক্রম 2 × 3 ও B-এর ক্রম 3 × 4 হলে AB-এর ক্রম কত?", "2 × 4", ["3 × 3", "4 × 2", "গুণ সম্ভব নয়"], "(m × n)(n × p) = m × p।", E),
 ("A² = A হলে A কোন ধরনের ম্যাট্রিক্স?", "সমঘাতি (idempotent)", ["শূন্যঘাতি", "অভেদক", "বিপ্রতিসম"], "সংজ্ঞা।", M),
 ("(AB)ᵀ = কত?", "BᵀAᵀ", ["AᵀBᵀ", "AB", "BA"], "ট্রান্সপোজের বিপরীত ক্রম।", M),
 ("ম্যাট্রিক্স গুণন সাধারণভাবে কোন বিধি মানে না?", "বিনিময় বিধি", ["সংযোগ বিধি", "বণ্টন বিধি", "কোনোটিই নয়"], "সাধারণত AB ≠ BA।", M),
]
def e_add(b):
    A, B = r2(), r2(); S = [[A[i][j] + B[i][j] for j in range(2)] for i in range(2)]
    b.add(f"A = {mat(A)}, B = {mat(B)} হলে A + B = কত?", mat(S), W(mat(S), [mat([[A[i][j] - B[i][j] for j in range(2)] for i in range(2)]), mat(mul(A, B)), mat([[S[i][j] + (1 if i == j else 0) for j in range(2)] for i in range(2)]), mat([[S[j][i] for j in range(2)] for i in range(2)])]), "অনুরূপ ভুক্তি যোগ।", E)
def e_scal(b):
    A = r2(); k = R.choice([2, 3, -2, -1, 4])
    S = [[k * x for x in r] for r in A]
    b.add(f"A = {mat(A)} হলে {num(k)}A = কত?", mat(S), W(mat(S), [mat([[A[0][0] * k, A[0][1]], A[1]]), mat([[x + k for x in r] for r in A]), mat([[-x for x in r] for r in S]), mat([[S[j][i] for j in range(2)] for i in range(2)])]), "প্রতিটি ভুক্তিকে গুণ।", E)
def e_tr(b):
    m, n = R.randint(2, 3), R.randint(2, 3); A = [[R.randint(-5, 9) for _ in range(n)] for _ in range(m)]
    T = [[A[i][j] for i in range(m)] for j in range(n)]
    if A == T: return
    b.add(f"A = {mat(A)} হলে Aᵀ = কত?", mat(T), W(mat(T), [mat(A), mat([[-x for x in r] for r in T]), mat([r[::-1] for r in T]), mat(T[::-1])]), "সারি ও কলাম বিনিময়।", E)
def e_order(b):
    m, n, p = R.randint(1, 5), R.randint(1, 5), R.randint(1, 5)
    b.add(f"A-এর ক্রম {m} × {n} এবং B-এর ক্রম {n} × {p} হলে AB-এর ক্রম কত?", f"{m} × {p}", W(f"{m} × {p}", [f"{n} × {n}", f"{p} × {m}", f"{m} × {n}", f"{n} × {p}", "গুণ সম্ভব নয়"]), "(m × n)(n × p) = m × p।", E)
def m_mul(b):
    A, B = r2(), r2(); C = mul(A, B)
    if C == mul(B, A): return
    b.add(f"A = {mat(A)}, B = {mat(B)} হলে AB = কত?", mat(C), W(mat(C), [mat(mul(B, A)), mat([[A[i][j] * B[i][j] for j in range(2)] for i in range(2)]), mat([[C[i][j] + 1 for j in range(2)] for i in range(2)]), mat([[C[j][i] for j in range(2)] for i in range(2)])]), "সারি × কলাম।", M)
def m_entry(b):
    A, B = r2(), r2(); C = mul(A, B); i, j = R.randint(0, 1), R.randint(0, 1)
    b.add(f"A = {mat(A)}, B = {mat(B)} হলে AB-এর ({i + 1}, {j + 1})-তম ভুক্তি কত?", num(C[i][j]), W(num(C[i][j]), [num(mul(B, A)[i][j]), num(C[i][j] + 1), num(A[i][j] * B[i][j]), num(C[j][i]), num(C[i][j] - 2)]), f"A-এর {i + 1}ম সারি × B-এর {j + 1}ম কলাম।", M)
def m_sq(b):
    A = r2(); C = mul(A, A)
    b.add(f"A = {mat(A)} হলে A² = কত?", mat(C), W(mat(C), [mat([[x * x for x in r] for r in A]), mat([[2 * x for x in r] for r in A]), mat([[C[j][i] for j in range(2)] for i in range(2)]), mat([[C[i][j] + 1 for j in range(2)] for i in range(2)])]), "A × A।", M)
def m_eq(b):
    x, y = R.randint(-6, 8), R.randint(-6, 8); a, c = R.randint(1, 5), R.randint(1, 5)
    b.add(f"[({num(x)} + {a}, {num(y)})] অর্থাৎ (x + {a}, y − {c}) = ({num(x + a)}, {num(y - c)}) হলে (x, y) = কত?".replace(f"[({num(x)} + {a}, {num(y)})] অর্থাৎ ", ''), P(x, y), W(P(x, y), [P(x + a, y - c), P(y, x), P(x - a, y + c), P(x, -y) if y else P(x, 1)]), "অনুরূপ ভুক্তি সমান।", M)
def m_trace(b):
    n = R.randint(2, 3); A = [[R.randint(-5, 9) for _ in range(n)] for _ in range(n)]
    t = sum(A[i][i] for i in range(n))
    b.add(f"A = {mat(A)} হলে A-এর ট্রেস (মুখ্য কর্ণের ভুক্তির যোগফল) কত?", num(t), W(num(t), [num(sum(A[i][n - 1 - i] for i in range(n))), num(sum(map(sum, A))), num(t + 1), num(t - 2)]), "মুখ্য কর্ণের ভুক্তি যোগ।", M)
def h_k(b):
    a, c = R.randint(1, 5), R.randint(-4, 4)
    # A = [(a, 1), (0, c)]; A² = [(a², a + c), (0, c²)]
    v = a + c
    b.add(f"A = [({a}, 1), (0, {num(c)})] হলে A²-এর (1, 2)-তম ভুক্তি কত?", num(v), W(num(v), [num(a * c), num(a * a), num(v + 1), '1']), f"a·1 + 1·{num(c)} = {num(v)}।", H)
def h_sym(b):
    a, c = R.randint(-6, 6), R.randint(-6, 6)
    b.add(f"A = [(2, {num(a)}), (x, 5)] প্রতিসম ম্যাট্রিক্স হলে x = কত?", num(a), W(num(a), [num(-a) if a else '1', '0', num(a + 2), '5']), "a₁₂ = a₂₁।", H)
    b.add(f"A = [(0, {num(c)}), (y, 0)] বিপ্রতিসম ম্যাট্রিক্স হলে y = কত?", num(-c), W(num(-c), [num(c) if c else '1', '0', num(-c + 1), num(c + 2)]), "a₂₁ = −a₁₂।", H)
def h_poly(b):
    A = [[R.randint(-3, 3) for _ in range(2)] for _ in range(2)]; k = R.randint(1, 4)
    C = mul(A, A); S = [[C[i][j] - k * A[i][j] for j in range(2)] for i in range(2)]
    b.add(f"A = {mat(A)} হলে A² − {k}A = কত?", mat(S), W(mat(S), [mat([[C[i][j] + k * A[i][j] for j in range(2)] for i in range(2)]), mat(C), mat([[S[i][j] - (k if i == j else 0) for j in range(2)] for i in range(2)]), mat([[S[j][i] for j in range(2)] for i in range(2)])]), "A² নির্ণয় করে বিয়োগ।", H)
def h_idem(b):
    a = R.randint(2, 5)
    # A = [(a, 1−a)... ] সহজ: [(1, 0), (k, 0)] সমঘাতি
    k = R.randint(-5, 6)
    A = [[1, 0], [k, 0]]
    b.add(f"A = {mat(A)} হলে A² = কত?", mat(A), W(mat(A), [mat([[1, 0], [0, 0]]), mat([[1, 0], [2 * k, 0]]), mat([[1, 0], [k * k, 0]]) if k * k != k else mat([[2, 0], [k, 0]]), mat([[0, 0], [0, 0]])]), "এটি সমঘাতি ম্যাট্রিক্স: A² = A।", H)
p1a = run('1.A', R, fx1a, [e_add, e_scal, e_tr, e_order], [m_mul, m_entry, m_sq, m_eq, m_trace], [h_k, h_sym, h_poly, h_idem])

# ---------------- 1.B নির্ণায়ক ----------------
fx1b = [
 ("কোনো নির্ণায়কের দুটি সারি অভিন্ন হলে তার মান কত?", "0", ["1", "−1", "দ্বিগুণ"], "নির্ণায়কের ধর্ম।", E),
 ("নির্ণায়কের দুটি সারি বিনিময় করলে মান কী হয়?", "চিহ্ন পরিবর্তিত হয়", ["অপরিবর্তিত থাকে", "শূন্য হয়", "দ্বিগুণ হয়"], "নির্ণায়কের ধর্ম।", E),
 ("|A| = 0 হলে A কোন ধরনের ম্যাট্রিক্স?", "ব্যতিক্রমী (singular)", ["অব্যতিক্রমী", "অভেদক", "বিপ্রতিসম"], "বিপরীত নেই।", E),
 ("A-এর বিপরীত ম্যাট্রিক্স থাকার শর্ত কোনটি?", "|A| ≠ 0", ["|A| = 0", "A প্রতিসম", "A = Aᵀ"], "A⁻¹ = adj A/|A|।", E),
 ("|Aᵀ| = কত?", "|A|", ["−|A|", "1/|A|", "0"], "ট্রান্সপোজে নির্ণায়ক অপরিবর্তিত।", M),
 ("3 × 3 ম্যাট্রিক্স A-এর জন্য |kA| = কত?", "k³|A|", ["k|A|", "3k|A|", "k²|A|"], "প্রতিটি সারি থেকে k।", M),
 ("|AB| = কত?", "|A|·|B|", ["|A| + |B|", "|BA|²", "|A|/|B|"], "নির্ণায়কের গুণ ধর্ম।", M),
 ("বিপ্রতিসম 3 × 3 ম্যাট্রিক্সের নির্ণায়কের মান কত?", "0", ["1", "−1", "নির্দিষ্ট নয়"], "বিজোড় ক্রমের বিপ্রতিসম নির্ণায়ক শূন্য।", H),
]
def e_d2(b):
    A = r2(); d = det2(A)
    b.add(f"|{mat(A)}| নির্ণায়কের মান কত?", num(d), W(num(d), [num(A[0][0] * A[1][1] + A[0][1] * A[1][0]), num(-d) if d else '1', num(d + 1), num(A[0][0] * A[0][1] - A[1][0] * A[1][1])]), "ad − bc।", E)
def e_singk(b):
    a, c, d = nz(-5, 6), nz(-5, 6), nz(-5, 6)
    # |(a, x), (c, d)| = 0 ⇒ x = ad/c
    if (a * d) % c: return
    x = a * d // c
    b.add(f"|({num(a)}, x), ({num(c)}, {num(d)})| = 0 হলে x = কত?", num(x), W(num(x), [num(-x) if x else '1', num(c * d // a) if (c * d) % a == 0 and c * d // a != x else num(x + 1), num(x + 2), num(a + d)]), f"{num(a)}·{num(d)} − {num(c)}x = 0।", E)
def e_tri(b):
    a, c, d = nz(-5, 6), nz(-5, 6), nz(-5, 6); x, y, z = R.randint(-6, 6), R.randint(-6, 6), R.randint(-6, 6)
    D = a * c * d
    b.add(f"|({num(a)}, {num(x)}, {num(y)}), (0, {num(c)}, {num(z)}), (0, 0, {num(d)})| = কত?", num(D), W(num(D), [num(a + c + d), num(-D), num(D + x), '0']), "ত্রিভুজাকার নির্ণায়ক = কর্ণের ভুক্তির গুণফল।", E)
def m_d3(b):
    A = [[R.randint(-3, 4) for _ in range(3)] for _ in range(3)]; d = det3(A)
    b.add(f"|{mat(A)}| = কত?", num(d), W(num(d), [num(-d) if d else '2', num(d + 1), num(d - 2), num(A[0][0] * A[1][1] * A[2][2])]), "প্রথম সারি বরাবর বিস্তৃতি।", M)
def m_inv(b):
    A = r2(); d = det2(A)
    if d not in (1, -1, 2, -2): return
    Ad = [[A[1][1], -A[0][1]], [-A[1][0], A[0][0]]]
    inv = '[' + ', '.join('(' + ', '.join(num(F(x, d)) for x in r) + ')' for r in Ad) + ']'
    w1 = '[' + ', '.join('(' + ', '.join(num(F(x, -d)) for x in r) + ')' for r in Ad) + ']'
    w2 = mat([[A[1][1], A[0][1]], [A[1][0], A[0][0]]])
    w3 = '[' + ', '.join('(' + ', '.join(num(F(x, d)) for x in r) + ')' for r in A) + ']'
    b.add(f"A = {mat(A)} হলে A⁻¹ = কত?", inv, W(inv, [w1, w2, w3]), f"|A| = {num(d)}; A⁻¹ = adj A/|A|।", M)
def m_minor(b):
    A = [[R.randint(-4, 5) for _ in range(3)] for _ in range(3)]; i, j = R.randint(0, 2), R.randint(0, 2)
    sub = [[A[r][c] for c in range(3) if c != j] for r in range(3) if r != i]; m_ = det2(sub); cof = (-1) ** (i + j) * m_
    q = R.choice(['অনুরাশি', 'সহগুণক'])
    v = m_ if q == 'অনুরাশি' else cof
    b.add(f"|{mat(A)}| নির্ণায়কে a{['₁', '₂', '₃'][i]}{['₁', '₂', '₃'][j]} ভুক্তির {q} কত?", num(v), W(num(v), [num(-v) if v else '1', num(v + 1), num(A[i][j]), num(det3(A))]), f"{i + 1}ম সারি ও {j + 1}ম কলাম বাদ দিয়ে {num(m_)}; সহগুণক = (−1)^(i+j) × অনুরাশি।", M)
def m_scale(b):
    d = R.randint(-6, 8); k = R.choice([2, 3, -2, -1]); n = R.choice([2, 3])
    b.add(f"{n} × {n} ম্যাট্রিক্স A-এর |A| = {num(d)} হলে |{num(k)}A| = কত?", num(k ** n * d), W(num(k ** n * d), [num(k * d), num(n * k * d), num(k ** (n + 1) * d), num(-k ** n * d) if d else '1']), f"|kA| = kⁿ|A| = ({num(k)}){sup(n)} × {num(d)}।", M)
def m_cramer(b):
    x, y = R.randint(-5, 6), R.randint(-5, 6); a1, b1, a2, b2 = nz(-4, 5), nz(-4, 5), nz(-4, 5), nz(-4, 5)
    D = a1 * b2 - a2 * b1
    if D == 0: return
    c1, c2 = a1 * x + b1 * y, a2 * x + b2 * y
    Dx = c1 * b2 - c2 * b1
    lx = lambda p, q: pfmt({(1, 0): p, (0, 1): q}, ('x', 'y'))
    b.add(f"{lx(a1, b1)} = {num(c1)}, {lx(a2, b2)} = {num(c2)} সমীকরণজোটে ক্রেমারের নিয়মে Dₓ = কত?", num(Dx), W(num(Dx), [num(D), num(a1 * c2 - a2 * c1), num(-Dx) if Dx else '1', num(Dx + D)]), f"Dₓ = |({num(c1)}, {num(b1)}), ({num(c2)}, {num(b2)})| = {num(Dx)}; x = Dₓ/D = {num(x)}।", M)
def h_solve(b):
    a, c = R.randint(1, 5), R.randint(1, 6)
    # |(x, a), (c, x)| = 0 ⇒ x² = ac
    v = a * c
    r = math.isqrt(v)
    if r * r != v: return
    b.add(f"|(x, {a}), ({c}, x)| = 0 হলে x = কত?", f"±{r}", W(f"±{r}", [str(r), f"±{v}", f"±{a + c}", "0"]), f"x² − {v} = 0।", H)
def h_inv_det(b):
    d = R.choice([2, 3, 4, 5, -2, -3]); n = R.choice([2, 3])
    b.add(f"{n} × {n} ম্যাট্রিক্স A-এর |A| = {num(d)} হলে |A⁻¹| = কত?", num(F(1, d)), W(num(F(1, d)), [num(d), num(-d), num(F(1, d ** n)), num(F(-1, d))]), "|A⁻¹| = 1/|A|।", H)
    b.add(f"{n} × {n} ম্যাট্রিক্স A-এর |A| = {num(d)} হলে |adj A| = কত?", num(d ** (n - 1)), W(num(d ** (n - 1)), [num(d), num(d ** n), num(F(1, d)), num(-d ** (n - 1))]), "|adj A| = |A|ⁿ⁻¹।", H)
def h_param(b):
    a, c = R.randint(1, 5), R.randint(1, 5)
    # |(1, 1, 1), (a, b, c), (a², b², c²)| = (b − a)(c − a)(c − b)
    x, y, z = R.sample(range(-3, 6), 3)
    v = (y - x) * (z - x) * (z - y)
    b.add(f"|(1, 1, 1), ({num(x)}, {num(y)}, {num(z)}), ({x * x}, {y * y}, {z * z})| = কত?", num(v), W(num(v), [num(-v), '0', num(v * 2), num(v + 1)]), f"(b − a)(c − a)(c − b) = {num(v)}।", H)
def h_sing(b):
    a, c = R.randint(1, 4), R.randint(-4, 5)
    # |(1, 2, 3), (2, k, 6), (a, c, 3a)|: কলাম৩ = 3 × কলাম১ হলে শূন্য: (1,2,3),(2,k,6) → k যেকোনো... ভিন্ন: |(k, 4), (9, k)| = 0
    k2 = a * a * 36
    r = 6 * a
    b.add(f"|(k, {4 * a}), ({9 * a}, k)| ম্যাট্রিক্সটি ব্যতিক্রমী হলে k = কত?", f"±{r}", W(f"±{r}", [str(r), f"±{r * r}", f"±{13 * a}", "0"]), f"k² − {36 * a * a} = 0।", H)
p1b = run('1.B', R, fx1b, [e_d2, e_singk, e_tri], [m_d3, m_inv, m_minor, m_scale, m_cramer], [h_solve, h_inv_det, h_param, h_sing])
save('i1', p1a + p1b)

# ---------------- 2 ভেক্টর ----------------
def V2(x, y): return pfmt({k: v for k, v in {(1, 0): x, (0, 1): y}.items() if v}, ('i', 'j')) if (x or y) else '0'
def V3(x, y, z): return pfmt({k: v for k, v in {(1, 0, 0): x, (0, 1, 0): y, (0, 0, 1): z}.items() if v}, ('î', 'ĵ', 'k̂')) if (x or y or z) else '0'
def rv3(): return (R.randint(-4, 5), R.randint(-4, 5), R.randint(-4, 5))
fx2a = [
 ("যে ভেক্টরের মান 1, তাকে কী বলে?", "একক ভেক্টর", ["শূন্য ভেক্টর", "অবস্থান ভেক্টর", "সমরেখ ভেক্টর"], "সংজ্ঞা।", E),
 ("দুটি ভেক্টরের মান ও দিক উভয়ই সমান হলে তাদের কী বলে?", "সমান ভেক্টর", ["বিপরীত ভেক্টর", "একক ভেক্টর", "সমতলীয় ভেক্টর"], "সংজ্ঞা।", E),
 ("ভেক্টর যোগের সামান্তরিক সূত্রে লব্ধি নির্দেশ করে কোনটি?", "সামান্তরিকের কর্ণ", ["সামান্তরিকের একটি বাহু", "ক্ষেত্রফল", "পরিসীমা"], "সামান্তরিক সূত্র।", E),
 ("a⃗ ও b⃗-এর মধ্যবর্তী কোণ θ হলে লব্ধির মান কত?", "√(a² + b² + 2ab cos θ)", ["a + b", "√(a² + b² − 2ab cos θ)", "√(a² + b²)"], "সামান্তরিক সূত্র।", M),
 ("সমান মানের দুটি বল পরস্পর 120° কোণে ক্রিয়াশীল হলে লব্ধির মান কত?", "প্রতিটি বলের সমান", ["শূন্য", "দ্বিগুণ", "অর্ধেক"], "√(P² + P² − P²) = P।", M),
]
def e_mag2(b):
    x, y = R.choice([(3, 4), (5, 12), (6, 8), (8, 15), (1, 1), (2, 3), (1, 2), (7, 24)]); x *= R.choice([1, -1]); y *= R.choice([1, -1])
    ok = sqf(x * x + y * y)
    b.add(f"a⃗ = {V2(x, y)} হলে |a⃗| = কত?", ok, W(ok, [str(abs(x) + abs(y)), str(x * x + y * y), sqf(x * x + y * y + 1)]), f"√({x * x} + {y * y})।", E)
def e_add2(b):
    a, c = (R.randint(-5, 6), R.randint(-5, 6)), (R.randint(-5, 6), R.randint(-5, 6))
    s = (a[0] + c[0], a[1] + c[1]); ok = V2(*s)
    b.add(f"a⃗ = {V2(*a)}, b⃗ = {V2(*c)} হলে a⃗ − b⃗ = কত?".replace('a⃗ − b⃗', 'a⃗ + b⃗'), ok, W(ok, [V2(a[0] - c[0], a[1] - c[1]), V2(s[1], s[0]), V2(s[0] + 1, s[1]), V2(-s[0], -s[1]) if s != (0, 0) else 'i']), "উপাংশ যোগ।", E)
def e_res(b):
    p, q, th = R.randint(2, 12), R.randint(2, 12), R.choice([0, 60, 90, 120, 180])
    v = p * p + q * q + 2 * p * q * {0: 1, 60: F(1, 2), 90: 0, 120: F(-1, 2), 180: -1}[th]
    v = F(v)
    if v.denominator != 1: return
    v = int(v)
    if v < 0: return
    ok = sqf(v)
    b.add(f"{p} N ও {q} N মানের দুটি বল পরস্পর {th}° কোণে ক্রিয়া করলে লব্ধির মান কত N?", ok, W(ok, [str(p + q), str(abs(p - q)), sqf(p * p + q * q), sqf(v + p)]), f"√({p}² + {q}² + 2·{p}·{q}·cos {th}°) = {ok}।", E)
def m_ab(b):
    A, B = (R.randint(-5, 6), R.randint(-5, 6)), (R.randint(-5, 6), R.randint(-5, 6))
    if A == B: return
    d = (B[0] - A[0], B[1] - A[1]); ok = sqf(d[0] ** 2 + d[1] ** 2)
    b.add(f"A ও B বিন্দুর অবস্থান ভেক্টর {V2(*A)} ও {V2(*B)} হলে |AB⃗| = কত?", ok, W(ok, [sqf((A[0] + B[0]) ** 2 + (A[1] + B[1]) ** 2) if A[0] + B[0] or A[1] + B[1] else '1', str(abs(d[0]) + abs(d[1])), sqf(d[0] ** 2 + d[1] ** 2 + 1)]), f"AB⃗ = {V2(*d)}।", M)
def m_unit2(b):
    x, y = R.choice([(3, 4), (5, 12), (6, 8), (8, 15), (4, 3), (12, 5)]); x *= R.choice([1, -1]); y *= R.choice([1, -1]); n = math.isqrt(x * x + y * y)
    ok = f"({V2(x, y)})/{n}"
    b.add(f"{V2(x, y)} ভেক্টরের দিকে একক ভেক্টর কোনটি?", ok, W(ok, [V2(x, y), f"({V2(y, x)})/{n}", f"({V2(x, y)})/{n * n}", f"({V2(-x, -y)})/{n}"]), "a⃗/|a⃗|।", M)
def m_col(b):
    a = (R.randint(1, 5), R.randint(-5, 5)); k = R.choice([2, 3, -2, -3])
    if not a[1]: return
    b.add(f"{V2(*a)} ও {num(k * a[0])}i + pj ভেক্টরদ্বয় সমান্তরাল হলে p = কত?", num(k * a[1]), W(num(k * a[1]), [num(-k * a[1]), num(a[1]), num(k * a[1] + 1), num(k)]), "অনুপাত সমান।", M)
def m_angle_res(b):
    p = R.randint(2, 12)
    th, v = R.choice([(60, f"{p}√3"), (90, f"{p}√2"), (120, str(p)), (180, '0'), (0, str(2 * p))])
    b.add(f"{p} N মানের দুটি সমান বল পরস্পর {th}° কোণে ক্রিয়া করলে লব্ধি কত N?", v, W(v, [f"{p}√3", f"{p}√2", str(p), str(2 * p), '0']), "R = 2P cos(θ/2)।", M)
def m_midpos(b):
    A, B = (R.randint(-5, 6), R.randint(-5, 6)), (R.randint(-5, 6), R.randint(-5, 6))
    if (A[0] + B[0]) % 2 or (A[1] + B[1]) % 2 or A == B: return
    ok = V2((A[0] + B[0]) // 2, (A[1] + B[1]) // 2)
    b.add(f"A ও B-এর অবস্থান ভেক্টর {V2(*A)} ও {V2(*B)} হলে AB-এর মধ্যবিন্দুর অবস্থান ভেক্টর কোনটি?", ok, W(ok, [V2(A[0] + B[0], A[1] + B[1]), V2((B[0] - A[0]) // 2, (B[1] - A[1]) // 2), V2((A[0] + B[0]) // 2 + 1, (A[1] + B[1]) // 2)]), "(a⃗ + b⃗)/2।", M)
def h_angle(b):
    p, q = R.randint(2, 10), R.randint(2, 10); th = R.choice([60, 120, 90])
    v = p * p + q * q + 2 * p * q * {60: F(1, 2), 90: 0, 120: F(-1, 2)}[th]
    b.add(f"P ও Q বলদ্বয়ের মান {p} ও {q} এবং লব্ধির বর্গ {v}। বলদ্বয়ের মধ্যবর্তী কোণ কত?", f"{th}°", W(f"{th}°", ['30°', '45°', '60°', '90°', '120°', '150°']), f"cos θ = ({v} − {p * p} − {q * q})/(2·{p}·{q})।", H)
def h_mn(b):
    a, c = (R.randint(1, 4), R.randint(-3, 3)), (R.randint(-3, 3), R.randint(1, 4))
    if a[0] * c[1] - a[1] * c[0] == 0: return
    m, n = R.randint(-3, 4), R.randint(-3, 4); t = (m * a[0] + n * c[0], m * a[1] + n * c[1])
    ok = f"m = {num(m)}, n = {num(n)}"
    b.add(f"ma⃗ + nb⃗ = {V2(*t)}, যেখানে a⃗ = {V2(*a)} ও b⃗ = {V2(*c)}। m ও n কত?", ok, W(ok, [f"m = {num(n)}, n = {num(m)}", f"m = {num(m + 1)}, n = {num(n)}", f"m = {num(-m)}, n = {num(-n)}" if (m, n) != (0, 0) else "m = 1, n = 1"]), "উপাংশ মিলিয়ে সমীকরণ।", H)
def h_eqres(b):
    p = R.randint(2, 10)
    b.add(f"দুটি সমান বলের লব্ধি প্রতিটি বলের সমান ({p} N) হলে বলদ্বয়ের মধ্যবর্তী কোণ কত?", "120°", ['60°', '90°', '150°'], "P² = 2P² + 2P² cos θ ⇒ cos θ = −1/2।", H)
    b.add(f"দুটি সমান বলের লব্ধি প্রতিটি বলের √3 গুণ ({p}√3 N) হলে বলদ্বয়ের মধ্যবর্তী কোণ কত?", "60°", ['30°', '90°', '120°'], "3P² = 2P²(1 + cos θ) ⇒ cos θ = 1/2।", H)
p2a = run('2.A', R, fx2a, [e_mag2, e_add2, e_res], [m_ab, m_unit2, m_col, m_angle_res, m_midpos], [h_angle, h_mn, h_eqres])

fx2b = [
 ("ত্রিমাত্রিক স্থানে î, ĵ, k̂ কী নির্দেশ করে?", "x, y, z অক্ষ বরাবর একক ভেক্টর", ["শূন্য ভেক্টর", "অবস্থান ভেক্টর", "সমতলের লম্ব"], "আদর্শ একক ভেক্টর।", E),
 ("ভেক্টর a⃗ x, y, z অক্ষের সাথে α, β, γ কোণ উৎপন্ন করলে cos²α + cos²β + cos²γ = কত?", "1", ["0", "2", "3"], "দিক কোসাইনের ধর্ম।", M),
 ("মূলবিন্দু থেকে (x, y, z) বিন্দুর দূরত্ব কত?", "√(x² + y² + z²)", ["x + y + z", "x² + y² + z²", "√(x + y + z)"], "ত্রিমাত্রিক দূরত্ব।", E),
]
def e_mag3(b):
    x, y, z = R.choice([(1, 2, 2), (2, 3, 6), (1, 4, 8), (2, 6, 9), (4, 4, 7), (3, 4, 12), (1, 1, 1), (1, 2, 3), (2, 1, 2), (6, 6, 7)])
    x, y, z = x * R.choice([1, -1]), y * R.choice([1, -1]), z * R.choice([1, -1])
    ok = sqf(x * x + y * y + z * z)
    b.add(f"a⃗ = {V3(x, y, z)} হলে |a⃗| = কত?", ok, W(ok, [str(abs(x) + abs(y) + abs(z)), str(x * x + y * y + z * z), sqf(x * x + y * y + z * z + 1)]), f"√({x * x} + {y * y} + {z * z})।", E)
def e_add3(b):
    a, c = rv3(), rv3(); s = tuple(a[i] + c[i] for i in range(3)); ok = V3(*s)
    if s == (0, 0, 0): return
    b.add(f"a⃗ = {V3(*a)}, b⃗ = {V3(*c)} হলে a⃗ + b⃗ = কত?", ok, W(ok, [V3(*(a[i] - c[i] for i in range(3))), V3(s[2], s[1], s[0]), V3(s[0] + 1, s[1], s[2]), V3(*(-x for x in s))]), "উপাংশ যোগ।", E)
def e_dist3(b):
    A = rv3(); d = R.choice([(1, 2, 2), (2, 3, 6), (2, 6, 9), (1, 4, 8), (3, 4, 12)]); B = tuple(A[i] + d[i] * R.choice([1, -1]) for i in range(3))
    ok = sqf(sum(x * x for x in d))
    b.add(f"({', '.join(num(x) for x in A)}) ও ({', '.join(num(x) for x in B)}) বিন্দুদ্বয়ের দূরত্ব কত?", ok, W(ok, [str(sum(d)), str(sum(x * x for x in d)), sqf(sum(x * x for x in d) + 2)]), "√(Δx² + Δy² + Δz²)।", E)
def m_unit3(b):
    x, y, z = R.choice([(1, 2, 2), (2, 3, 6), (2, 6, 9), (1, 4, 8), (4, 4, 7), (3, 4, 12)]); x *= R.choice([1, -1])
    n = math.isqrt(x * x + y * y + z * z); ok = f"({V3(x, y, z)})/{n}"
    b.add(f"{V3(x, y, z)}-এর দিকে একক ভেক্টর কোনটি?", ok, W(ok, [V3(x, y, z), f"({V3(x, y, z)})/{n * n}", f"({V3(z, y, x)})/{n}", f"({V3(-x, -y, -z)})/{n}"]), "a⃗/|a⃗|।", M)
def m_dc(b):
    x, y, z = R.choice([(1, 2, 2), (2, 3, 6), (2, 6, 9), (1, 4, 8), (4, 4, 7), (3, 4, 12)]); n = math.isqrt(x * x + y * y + z * z)
    w = R.choice(['x', 'y', 'z']); v = {'x': x, 'y': y, 'z': z}[w]
    b.add(f"{V3(x, y, z)} ভেক্টরটি {w}-অক্ষের সাথে যে কোণ উৎপন্ন করে তার কোসাইন কত?", fr(F(v, n)), W(fr(F(v, n)), [fr(F(n, v)), fr(F(v, n * n)), fr(F(x + y + z - v, n)), fr(F(v + 1, n))]), f"cos = {v}/{n}।", M)
def m_lin3(b):
    a, c = rv3(), rv3(); p, q = R.choice([2, 3, -1]), R.choice([2, -2, 1]); s = tuple(p * a[i] + q * c[i] for i in range(3))
    if s == (0, 0, 0): return
    ok = V3(*s)
    b.add(f"a⃗ = {V3(*a)}, b⃗ = {V3(*c)} হলে {num(p) if p != -1 else '−'}a⃗ {'+' if q > 0 else '−'} {abs(q) if abs(q) != 1 else ''}b⃗ = কত?", ok, W(ok, [V3(*(p * a[i] - q * c[i] for i in range(3))), V3(*(q * a[i] + p * c[i] for i in range(3))), V3(s[0] + 1, s[1], s[2])]), "উপাংশ অনুযায়ী।", M)
def m_par3(b):
    a = (R.randint(1, 4), R.randint(-4, 4), R.randint(-4, 4)); k = R.choice([2, 3, -2])
    if not a[1] or not a[2]: return
    ok = f"p = {num(k * a[1])}, q = {num(k * a[2])}"
    b.add(f"{V3(*a)} ও {num(k * a[0])}î + pĵ + qk̂ ভেক্টরদ্বয় সমান্তরাল হলে p ও q কত?", ok, W(ok, [f"p = {num(a[1])}, q = {num(a[2])}", f"p = {num(-k * a[1])}, q = {num(-k * a[2])}", f"p = {num(k * a[2])}, q = {num(k * a[1])}"]), "অনুপাত সমান।", M)
def h_k3(b):
    x, y, z = R.choice([(1, 2, 2), (2, 3, 6), (2, 6, 9), (1, 4, 8), (3, 4, 12)]); n = math.isqrt(x * x + y * y + z * z)
    b.add(f"a⃗ = {x}î + {y}ĵ + λk̂ এবং |a⃗| = {n} হলে λ = কত?", f"±{z}", W(f"±{z}", [str(z), f"±{z * z}", f"±{n - x - y}" if n - x - y > 0 else f"±{z + 1}", f"±{n}"]), f"{x * x} + {y * y} + λ² = {n * n}।", H)
def h_dcang(b):
    a, ang = R.choice([(1, '60°'), (2, '45°'), (0, '90°')])
    vals = {'60°': ('1/2', '1/√2'), '45°': ('1/√2', '1/2'), '90°': ('0', '1/√2')}
    b.add(f"একটি ভেক্টর x ও y অক্ষের সাথে যথাক্রমে 45° ও 60° কোণ উৎপন্ন করলে z-অক্ষের সাথে কোণ কত (সূক্ষ্মকোণ)?", "60°", ['30°', '45°', '90°'], "cos²45° + cos²60° + cos²γ = 1 ⇒ cos γ = 1/2।", H)
    b.add(f"একটি ভেক্টর তিন অক্ষের সাথে সমান সূক্ষ্মকোণ θ উৎপন্ন করলে cos θ = কত?", "1/√3", ['1/3', '1/√2', '√3/2'], "3cos²θ = 1।", H)
def h_mid3(b):
    A, B = rv3(), rv3(); m, n = R.choice([(1, 2), (2, 1), (1, 3), (3, 1)])
    p = tuple(F(m * B[i] + n * A[i], m + n) for i in range(3))
    if any(x.denominator > 1 for x in p) or A == B: return
    ok = V3(*(int(x) for x in p))
    q = tuple(F(n * B[i] + m * A[i], m + n) for i in range(3))
    b.add(f"A({', '.join(num(x) for x in A)}) ও B({', '.join(num(x) for x in B)})-এর সংযোগ রেখাংশকে {m} : {n} অনুপাতে অন্তর্বিভক্তকারী বিন্দুর অবস্থান ভেক্টর কোনটি?", ok, W(ok, [V3(*(int(x) for x in q)) if all(x.denominator == 1 for x in q) else V3(*(A[i] + B[i] for i in range(3))), V3(*(A[i] + B[i] for i in range(3))), V3(int(p[0]) + 1, int(p[1]), int(p[2]))]), "(na⃗ + mb⃗)/(m + n)।", H)
p2b = run('2.B', R, fx2b, [e_mag3, e_add3, e_dist3], [m_unit3, m_dc, m_lin3, m_par3], [h_k3, h_dcang, h_mid3])

fx2c = [
 ("a⃗ · b⃗ = 0 (a⃗, b⃗ অশূন্য) হলে ভেক্টরদ্বয় কেমন?", "পরস্পর লম্ব", ["সমান্তরাল", "সমান", "বিপরীত"], "cos θ = 0।", E),
 ("a⃗ × b⃗ = 0⃗ (a⃗, b⃗ অশূন্য) হলে ভেক্টরদ্বয় কেমন?", "সমান্তরাল", ["লম্ব", "একক", "কোনোটিই নয়"], "sin θ = 0।", E),
 ("î · î = কত?", "1", ["0", "î", "k̂"], "একক ভেক্টরের ডট গুণফল।", E),
 ("î × ĵ = কত?", "k̂", ["−k̂", "0", "1"], "ডানহাতি পদ্ধতি।", E),
 ("ĵ × î = কত?", "−k̂", ["k̂", "0", "1"], "ক্রস গুণন বিনিময় করলে চিহ্ন বদলায়।", M),
 ("|a⃗ × b⃗| জ্যামিতিকভাবে কী নির্দেশ করে?", "a⃗ ও b⃗ সন্নিহিত বাহুবিশিষ্ট সামান্তরিকের ক্ষেত্রফল", ["ত্রিভুজের পরিসীমা", "ভেক্টরদ্বয়ের যোগফল", "আয়তন"], "|a||b| sin θ।", M),
 ("a⃗ · (b⃗ × c⃗) = 0 হলে ভেক্টর তিনটি কেমন?", "সমতলীয়", ["পরস্পর লম্ব", "সমরেখ নয়", "একক"], "সামান্তরিক ঘনবস্তুর আয়তন শূন্য।", H),
]
def dot(a, c): return sum(a[i] * c[i] for i in range(3))
def cross(a, c): return (a[1] * c[2] - a[2] * c[1], a[2] * c[0] - a[0] * c[2], a[0] * c[1] - a[1] * c[0])
def e_dot(b):
    a, c = rv3(), rv3(); d = dot(a, c)
    b.add(f"a⃗ = {V3(*a)}, b⃗ = {V3(*c)} হলে a⃗ · b⃗ = কত?", num(d), W(num(d), [num(d + 1), num(-d) if d else '1', num(sum(a) * sum(c)), V3(*cross(a, c)) if cross(a, c) != (0, 0, 0) else '2']), "অনুরূপ উপাংশের গুণফলের যোগফল।", E)
def e_perp(b):
    a = (R.randint(1, 5), R.randint(-4, 5), R.randint(-4, 5)); c0, c1 = R.randint(-4, 5), R.randint(-4, 5)
    if not a[2]: return
    rest = a[0] * c0 + a[1] * c1
    if rest % a[2]: return
    z = -rest // a[2]
    b.add(f"{V3(*a)} ও {V3(c0, c1, 0)}{' + ' if True else ''}λk̂ ভেক্টরদ্বয় পরস্পর লম্ব হলে λ = কত?".replace(' + λk̂', ' + λk̂') if (c0 or c1) else None, num(z), W(num(z), [num(-z) if z else '1', num(z + 1), num(rest), '0']), f"ডট গুণফল শূন্য: {num(rest)} + {num(a[2])}λ = 0।", E) if (c0 or c1) else None
def m_cross(b):
    a, c = rv3(), rv3(); x = cross(a, c)
    if x == (0, 0, 0): return
    ok = V3(*x)
    b.add(f"a⃗ = {V3(*a)}, b⃗ = {V3(*c)} হলে a⃗ × b⃗ = কত?", ok, W(ok, [V3(*(-v for v in x)), V3(x[2], x[1], x[0]), V3(x[0] + 1, x[1], x[2])]), "নির্ণায়কের মাধ্যমে।", M)
def m_angle(b):
    a, c, ang = R.choice([((1, 0, 0), (1, 1, 0), '45°'), ((1, 1, 0), (0, 1, 1), '60°'), ((1, 0, 1), (1, 1, 0), '60°'), ((1, 0, 0), (0, 1, 0), '90°'), ((1, 1, 0), (-1, 0, -1), '120°'), ((1, 2, 2), (2, -2, 1), '90°'), ((3, 0, 4), (4, 0, 3), None)])
    if ang is None: return
    b.add(f"{V3(*a)} ও {V3(*c)} ভেক্টরদ্বয়ের মধ্যবর্তী কোণ কত?", ang, W(ang, ['30°', '45°', '60°', '90°', '120°']), "cos θ = a⃗·b⃗/(|a⃗||b⃗|)।", M)
def m_proj(b):
    a = rv3(); c = R.choice([(1, 2, 2), (2, 3, 6), (2, 6, 9), (3, 4, 12), (0, 3, 4), (4, 0, 3)]); n = math.isqrt(dot(c, c))
    v = F(dot(a, c), n)
    b.add(f"a⃗ = {V3(*a)}-এর b⃗ = {V3(*c)}-এর উপর অভিক্ষেপ (স্কেলার) কত?", num(v), W(num(v), [num(F(dot(a, c), n * n)), num(dot(a, c)), num(v + 1), num(-v) if v else '1']), f"a⃗·b⃗/|b⃗| = {dot(a, c)}/{n}।", M)
def m_area(b):
    a, c = rv3(), rv3(); x = cross(a, c); s = dot(x, x)
    if not s: return
    ok = sqf(s); half = f"{ok}/2" if not ok.isdigit() else fr(F(int(ok), 2))
    kind = R.choice(['সামান্তরিক', 'ত্রিভুজ'])
    ans = ok if kind == 'সামান্তরিক' else half
    b.add(f"a⃗ = {V3(*a)} ও b⃗ = {V3(*c)} সন্নিহিত বাহুবিশিষ্ট {kind}ের ক্ষেত্রফল কত?", ans, W(ans, [half if kind == 'সামান্তরিক' else ok, str(abs(dot(a, c))), sqf(s + 1)]), f"|a⃗ × b⃗| = {ok}।", M)
def h_triple(b):
    a, c, d = rv3(), rv3(), rv3(); v = dot(a, cross(c, d))
    b.add(f"a⃗ = {V3(*a)}, b⃗ = {V3(*c)}, c⃗ = {V3(*d)} হলে a⃗ · (b⃗ × c⃗) = কত?", num(v), W(num(v), [num(-v) if v else '1', num(v + 1), num(dot(a, c) * sum(d)), '0' if v else '2']), "তিন ভেক্টরের নির্ণায়ক।", H)
def h_work(b):
    F_ = rv3(); d = rv3(); w = dot(F_, d)
    b.add(f"F⃗ = {V3(*F_)} N বল একটি বস্তুকে d⃗ = {V3(*d)} m সরণ ঘটালে কাজের পরিমাণ কত J?", num(w), W(num(w), [num(w + 1), num(-w) if w else '1', V3(*cross(F_, d)) if cross(F_, d) != (0, 0, 0) else '3', num(abs(w) + 2)]), "W = F⃗ · d⃗।", H)
def h_perp_k(b):
    a, c = (R.randint(1, 4), R.randint(-3, 3), R.randint(1, 3)), (R.randint(-3, 3), R.randint(1, 4), 0)
    # (a + λc) ⟂ c ⇒ a·c + λ c·c = 0
    cc = dot(c, c); ac = dot(a, c)
    if not cc: return
    lam = F(-ac, cc)
    b.add(f"a⃗ = {V3(*a)}, b⃗ = {V3(*c)} এবং (a⃗ + λb⃗) ⊥ b⃗ হলে λ = কত?", num(lam), W(num(lam), [num(-lam) if lam else '1', num(F(ac, cc)) if ac else '2', num(lam + 1), num(F(-cc, ac)) if ac else '−1']), f"a⃗·b⃗ + λ|b⃗|² = 0 ⇒ {ac} + {cc}λ = 0।", H)
p2c = run('2.C', R, fx2c, [e_dot, e_perp], [m_cross, m_angle, m_proj, m_area], [h_triple, h_work, h_perp_k], caps=(16, 13, 7))
save('i2', p2a + p2b + p2c)

# ---------------- 3 সরলরেখা ----------------
def rp(lo=-6, hi=8): return (R.randint(lo, hi), R.randint(lo, hi))
def tarea(A, B, C): return F(abs(A[0] * (B[1] - C[1]) + B[0] * (C[1] - A[1]) + C[0] * (A[1] - B[1])), 2)
def L(a, c, k): return pfmt({kk: v for kk, v in {(1, 0): a, (0, 1): c, (0, 0): k}.items() if v}, ('x', 'y')) + ' = 0'
def norm(a, c, k):
    g = math.gcd(math.gcd(abs(a), abs(c)), abs(k)) or 1; a, c, k = a // g, c // g, k // g
    if a < 0 or (a == 0 and c < 0): a, c, k = -a, -c, -k
    return a, c, k
fx3a = [
 ("পোলার স্থানাঙ্ক (r, θ)-কে কার্তেসীয় স্থানাঙ্কে প্রকাশ করলে কোনটি?", "(r cos θ, r sin θ)", ["(r sin θ, r cos θ)", "(r, rθ)", "(cos θ, sin θ)"], "x = r cos θ, y = r sin θ।", E),
 ("কার্তেসীয় (x, y) বিন্দুর পোলার স্থানাঙ্কে r = কত?", "√(x² + y²)", ["x + y", "x² + y²", "y/x"], "মূলবিন্দু থেকে দূরত্ব।", E),
 ("কোনো বিন্দু চতুর্থ চতুর্ভাগে থাকলে স্থানাঙ্কের চিহ্ন কেমন?", "(+, −)", ["(−, +)", "(−, −)", "(+, +)"], "x ধনাত্মক, y ঋণাত্মক।", E),
]
def e_dist(b):
    A = rp(); d = R.choice([(3, 4), (5, 12), (6, 8), (8, 15), (1, 1), (2, 3), (0, 5), (7, 24)]); B = (A[0] + d[0] * R.choice([1, -1]), A[1] + d[1] * R.choice([1, -1]))
    ok = sqf(d[0] ** 2 + d[1] ** 2)
    b.add(f"{P(*A)} ও {P(*B)} বিন্দুদ্বয়ের দূরত্ব কত?", ok, W(ok, [str(d[0] + d[1]), str(d[0] ** 2 + d[1] ** 2), sqf(d[0] ** 2 + d[1] ** 2 + 2)]), "দূরত্বের সূত্র।", E)
def e_polar(b):
    r = R.randint(2, 10); th, c, s = R.choice([(0, 1, 0), (90, 0, 1), (180, -1, 0), (270, 0, -1), (60, F(1, 2), None), (30, None, F(1, 2)), (45, None, None)])
    if c is None or s is None:
        if th == 60: ok = f"({fr(F(r, 2))}, {fr(F(r, 2)) if False else ''}{r if r > 1 else ''}√3/2)".replace('(', '(', 1)
        return
    ok = P(r * c, r * s)
    b.add(f"পোলার স্থানাঙ্ক ({r}, {th}°)-এর কার্তেসীয় রূপ কোনটি?", ok, W(ok, [P(r * s, r * c), P(-r * c, -r * s) if (c or s) else P(r, r), P(r, th), P(r, 0)]), "x = r cos θ, y = r sin θ।", E)
def e_toPolar(b):
    a = R.randint(1, 9); kind = R.choice(['x+', 'x-', 'y+', 'y-', 'd'])
    pt, ok = {'x+': ((a, 0), f"({a}, 0°)"), 'x-': ((-a, 0), f"({a}, 180°)"), 'y+': ((0, a), f"({a}, 90°)"), 'y-': ((0, -a), f"({a}, 270°)"), 'd': ((a, a), f"({a}√2, 45°)" if a > 1 else "(√2, 45°)")}[kind]
    b.add(f"কার্তেসীয় {P(*pt)} বিন্দুর পোলার স্থানাঙ্ক কোনটি?", ok, W(ok, [f"({a}, 0°)", f"({a}, 90°)", f"({a}, 180°)", f"({a}, 270°)", f"({2 * a}, 45°)"]), "r = √(x² + y²), θ = দিক কোণ।", E)
def m_type(b):
    o = rp(-3, 4); dx, dy = R.randint(1, 6), R.randint(1, 6)
    kind = R.choice(['right', 'iso'])
    if kind == 'right': pts = [o, (o[0] + dx, o[1]), (o[0], o[1] + dy)]
    else: pts = [(o[0] - dx, o[1]), (o[0] + dx, o[1]), (o[0], o[1] + dy)]
    ds = sorted([(pts[i][0] - pts[j][0]) ** 2 + (pts[i][1] - pts[j][1]) ** 2 for i, j in ((0, 1), (1, 2), (0, 2))])
    ok = 'সমকোণী' if ds[0] + ds[1] == ds[2] else ('সমদ্বিবাহু' if len(set(ds)) < 3 else 'বিষমবাহু')
    if ok == 'সমকোণী' and len(set(ds)) < 3: ok = 'সমকোণী সমদ্বিবাহু'
    b.add(f"{', '.join(P(*p) for p in pts)} শীর্ষবিশিষ্ট ত্রিভুজটি কোন ধরনের?", ok, W(ok, ['সমবাহু', 'সমদ্বিবাহু', 'সমকোণী', 'বিষমবাহু', 'সমকোণী সমদ্বিবাহু']), f"বাহুর বর্গ: {', '.join(map(str, ds))}।", M)
def m_k(b):
    A = rp(); d = R.choice([(3, 4), (5, 12), (6, 8), (8, 15)])
    ok = f"{num(A[1] + d[1])} বা {num(A[1] - d[1])}"
    b.add(f"{P(*A)} ও ({num(A[0] + d[0])}, k) বিন্দুদ্বয়ের দূরত্ব {math.isqrt(d[0] ** 2 + d[1] ** 2)} হলে k = কত?", ok, W(ok, [num(A[1] + d[1]), f"{num(d[1])} বা {num(-d[1])}", f"{num(A[1] + d[0])} বা {num(A[1] - d[0])}"]), "দূরত্বের সূত্রে সমীকরণ।", M)
def m_equid(b):
    A, B = rp(), rp()
    if A[1] == B[1]: return
    n_ = B[0] ** 2 + B[1] ** 2 - A[0] ** 2 - A[1] ** 2; dn = 2 * (B[1] - A[1])
    if n_ % dn: return
    y = n_ // dn
    b.add(f"y-অক্ষের উপর যে বিন্দু {P(*A)} ও {P(*B)} থেকে সমদূরবর্তী, সেটি কোনটি?", P(0, y), W(P(0, y), [P(y, 0), P(0, -y) if y else P(0, 1), P(0, y + 1)]), "(0, y) ধরে দূরত্ব সমান।", M)
def m_polar_dist(b):
    r1, r2 = R.randint(1, 8), R.randint(1, 8); a1, a2 = R.choice([(0, 90), (30, 120), (0, 60), (60, 120), (0, 180), (45, 135)])
    d = a2 - a1; c = {90: 0, 60: F(1, 2), 180: -1}[d]
    v = r1 * r1 + r2 * r2 - 2 * r1 * r2 * c
    if v.denominator > 1: return
    ok = sqf(int(v))
    b.add(f"পোলার স্থানাঙ্ক ({r1}, {a1}°) ও ({r2}, {a2}°) বিন্দুদ্বয়ের দূরত্ব কত?", ok, W(ok, [str(r1 + r2), sqf(r1 * r1 + r2 * r2), str(abs(r1 - r2)) if r1 != r2 else '1', sqf(int(v) + 3)]), f"√(r₁² + r₂² − 2r₁r₂cos(θ₂ − θ₁))।", M)
def h_circ(b):
    o = rp(-3, 4); a, c = R.randint(1, 6), R.randint(1, 6)
    pts = [o, (o[0] + 2 * a, o[1]), (o[0], o[1] + 2 * c)]
    ok = P(o[0] + a, o[1] + c)
    b.add(f"{', '.join(P(*p) for p in pts)} বিন্দু তিনটি থেকে সমদূরবর্তী বিন্দু কোনটি?", ok, W(ok, [P(*o), P(o[0] + 2 * a, o[1] + 2 * c), P(F(3 * o[0] + 2 * a, 3), F(3 * o[1] + 2 * c, 3))]), "সমকোণী ত্রিভুজের পরিকেন্দ্র অতিভুজের মধ্যবিন্দু।", H)
def h_perim(b):
    o = rp(); a, c = R.choice([(3, 4), (6, 8), (5, 12), (8, 15)])
    pts = [o, (o[0] + a, o[1]), (o[0], o[1] + c)]; v = a + c + math.isqrt(a * a + c * c)
    b.add(f"{', '.join(P(*p) for p in pts)} শীর্ষবিশিষ্ট ত্রিভুজের পরিসীমা কত?", v, W(v, [a + c, v + 1, a * c // 2, 2 * v]), "তিন বাহুর যোগফল।", H)
def h_rhombus(b):
    o = rp(-3, 3); a, c = R.randint(1, 5), R.randint(1, 5)
    if a == c: return
    pts = [(o[0] - a, o[1]), (o[0], o[1] + c), (o[0] + a, o[1]), (o[0], o[1] - c)]
    b.add(f"{', '.join(P(*p) for p in pts)} শীর্ষবিশিষ্ট চতুর্ভুজটি কোন ধরনের?", 'রম্বস', ['বর্গ', 'আয়তক্ষেত্র', 'ট্রাপিজিয়াম'], "চার বাহু সমান কিন্তু কর্ণ অসমান।", H)
p3a = run('3.A', R, fx3a, [e_dist, e_polar, e_toPolar], [m_type, m_k, m_equid, m_polar_dist], [h_circ, h_perim, h_rhombus])

fx3b = [
 ("(x₁, y₁) ও (x₂, y₂) সংযোগ রেখাংশকে m : n অনুপাতে অন্তর্বিভক্তকারী বিন্দু কোনটি?", "((mx₂ + nx₁)/(m + n), (my₂ + ny₁)/(m + n))", ["((mx₁ + nx₂)/(m + n), (my₁ + ny₂)/(m + n))", "((mx₂ − nx₁)/(m − n), (my₂ − ny₁)/(m − n))", "((x₁ + x₂)/2, (y₁ + y₂)/2)"], "অন্তর্বিভক্তির সূত্র।", E),
 ("বহির্বিভক্তির সূত্রে হর কোনটি?", "m − n", ["m + n", "mn", "m/n"], "((mx₂ − nx₁)/(m − n), …)।", E),
 ("ত্রিভুজের ভরকেন্দ্রের স্থানাঙ্ক কোনটি?", "((x₁ + x₂ + x₃)/3, (y₁ + y₂ + y₃)/3)", ["((x₁ + x₂ + x₃)/2, (y₁ + y₂ + y₃)/2)", "(x₁ + x₂ + x₃, y₁ + y₂ + y₃)", "((x₁x₂x₃)/3, (y₁y₂y₃)/3)"], "শীর্ষবিন্দুর গড়।", E),
]
def e_mid(b):
    A, B = rp(), rp()
    if (A[0] + B[0]) % 2 or (A[1] + B[1]) % 2 or A == B: return
    ok = P((A[0] + B[0]) // 2, (A[1] + B[1]) // 2)
    b.add(f"{P(*A)} ও {P(*B)}-এর মধ্যবিন্দু কোনটি?", ok, W(ok, [P(A[0] + B[0], A[1] + B[1]), P((B[0] - A[0]) // 2, (B[1] - A[1]) // 2), P((A[1] + B[1]) // 2, (A[0] + B[0]) // 2)]), "গড়।", E)
def e_cent(b):
    A, B, C = rp(), rp(), rp(); sx, sy = A[0] + B[0] + C[0], A[1] + B[1] + C[1]
    if sx % 3 or sy % 3: return
    ok = P(sx // 3, sy // 3)
    b.add(f"{P(*A)}, {P(*B)}, {P(*C)} শীর্ষবিশিষ্ট ত্রিভুজের ভরকেন্দ্র কোনটি?", ok, W(ok, [P(sx, sy), P(F(sx, 2), F(sy, 2)), P(sy // 3, sx // 3), P(sx // 3 + 1, sy // 3)]), "শীর্ষের গড়।", E)
def e_other(b):
    A = rp(); M_ = rp()
    B = (2 * M_[0] - A[0], 2 * M_[1] - A[1]); ok = P(*B)
    b.add(f"একটি রেখাংশের এক প্রান্ত {P(*A)} এবং মধ্যবিন্দু {P(*M_)} হলে অপর প্রান্ত কোনটি?", ok, W(ok, [P(F(A[0] + M_[0], 2), F(A[1] + M_[1], 2)), P(M_[0] - A[0], M_[1] - A[1]), P(2 * A[0] - M_[0], 2 * A[1] - M_[1])]), "2M − A।", E)
def m_int(b):
    A, B = rp(), rp(); m, n = R.choice([(1, 2), (2, 1), (1, 3), (3, 1), (2, 3), (3, 2)])
    px, py = F(m * B[0] + n * A[0], m + n), F(m * B[1] + n * A[1], m + n)
    if px.denominator > 1 or py.denominator > 1 or A == B: return
    ok = P(px, py); q = P(F(n * B[0] + m * A[0], m + n), F(n * B[1] + m * A[1], m + n))
    b.add(f"{P(*A)} ও {P(*B)} সংযোগ রেখাংশকে {m} : {n} অনুপাতে অন্তর্বিভক্তকারী বিন্দু কোনটি?", ok, W(ok, [q, P(F(A[0] + B[0], 2), F(A[1] + B[1], 2)), P(px + 1, py)]), "অন্তর্বিভক্তির সূত্র।", M)
def m_ext(b):
    A, B = rp(), rp(); m, n = R.choice([(2, 1), (3, 1), (3, 2), (1, 2), (1, 3), (4, 3)])
    px, py = F(m * B[0] - n * A[0], m - n), F(m * B[1] - n * A[1], m - n)
    if px.denominator > 1 or py.denominator > 1 or A == B: return
    ok = P(px, py); q = P(F(m * B[0] + n * A[0], m + n), F(m * B[1] + n * A[1], m + n))
    b.add(f"{P(*A)} ও {P(*B)} সংযোগ রেখাংশকে {m} : {n} অনুপাতে বহির্বিভক্তকারী বিন্দু কোনটি?", ok, W(ok, [q, P(-px, -py) if (px or py) else P(1, 1), P(px + 1, py)]), "((mx₂ − nx₁)/(m − n), (my₂ − ny₁)/(m − n))।", M)
def m_ratio(b):
    A, B = rp(), rp()
    if A[1] * B[1] >= 0: return
    g = math.gcd(abs(A[1]), abs(B[1])); ok = f"{abs(A[1]) // g} : {abs(B[1]) // g}"
    b.add(f"x-অক্ষ {P(*A)} ও {P(*B)}-এর সংযোগ রেখাংশকে কী অনুপাতে বিভক্ত করে?", ok, W(ok, [f"{abs(B[1]) // g} : {abs(A[1]) // g}", "1 : 1", f"{abs(A[1]) + abs(B[1])} : 1"]), "y = 0 হওয়ার শর্ত।", M)
def m_cent_find(b):
    A, B = rp(), rp(); G = rp()
    C = (3 * G[0] - A[0] - B[0], 3 * G[1] - A[1] - B[1]); ok = P(*C)
    b.add(f"ত্রিভুজের দুটি শীর্ষ {P(*A)} ও {P(*B)} এবং ভরকেন্দ্র {P(*G)} হলে তৃতীয় শীর্ষ কোনটি?", ok, W(ok, [P(G[0] - A[0] - B[0], G[1] - A[1] - B[1]), P(3 * G[0] + A[0] + B[0], 3 * G[1] + A[1] + B[1]), P(C[0] + 1, C[1])]), "3G − A − B।", M)
def h_ratio_y(b):
    A, B = rp(), rp()
    if A[0] * B[0] >= 0: return
    g = math.gcd(abs(A[0]), abs(B[0])); ok = f"{abs(A[0]) // g} : {abs(B[0]) // g}"
    b.add(f"y-অক্ষ {P(*A)} ও {P(*B)}-এর সংযোগ রেখাংশকে কী অনুপাতে বিভক্ত করে?", ok, W(ok, [f"{abs(B[0]) // g} : {abs(A[0]) // g}", "1 : 1", f"{abs(A[0]) + abs(B[0])} : 1"]), "x = 0 হওয়ার শর্ত।", H)
def h_fourth(b):
    A, B, C = rp(), rp(), rp()
    if (B[0] - A[0]) * (C[1] - A[1]) - (B[1] - A[1]) * (C[0] - A[0]) == 0: return
    D = (A[0] + C[0] - B[0], A[1] + C[1] - B[1]); ok = P(*D)
    b.add(f"ABCD সামান্তরিকের A{P(*A)}, B{P(*B)}, C{P(*C)} হলে D কোনটি?", ok, W(ok, [P(B[0] + C[0] - A[0], B[1] + C[1] - A[1]), P(A[0] + B[0] - C[0], A[1] + B[1] - C[1]), P(D[0] + 1, D[1])]), "কর্ণের মধ্যবিন্দু একই।", H)
def h_trisect(b):
    A = rp(); d = (R.randint(-3, 3), R.randint(-3, 3))
    if d == (0, 0): return
    B = (A[0] + 3 * d[0], A[1] + 3 * d[1])
    ok = f"{P(A[0] + d[0], A[1] + d[1])} ও {P(A[0] + 2 * d[0], A[1] + 2 * d[1])}"
    b.add(f"{P(*A)} ও {P(*B)} সংযোগ রেখাংশের ত্রিখণ্ডক বিন্দুদ্বয় কোনটি?", ok, W(ok, [f"{P(A[0] + d[0], A[1] + d[1])} ও {P(B[0] + d[0], B[1] + d[1])}", f"{P(F(A[0] + B[0], 2), F(A[1] + B[1], 2))} ও {P(*B)}", f"{P(A[0] + 2 * d[0], A[1] + d[1])} ও {P(A[0] + d[0], A[1] + 2 * d[1])}"]), "1 : 2 ও 2 : 1 অনুপাতে।", H)
p3b = run('3.B', R, fx3b, [e_mid, e_cent, e_other], [m_int, m_ext, m_ratio, m_cent_find], [h_ratio_y, h_fourth, h_trisect])

fx3c = [
 ("তিনটি বিন্দু সমরেখ হলে তাদের দ্বারা গঠিত ত্রিভুজের ক্ষেত্রফল কত?", "0", ["1", "অসীম", "ঋণাত্মক"], "সমরেখ বিন্দু।", E),
 ("শীর্ষবিন্দু ঘড়ির কাঁটার দিকে নিলে স্থানাঙ্ক পদ্ধতিতে পাওয়া ক্ষেত্রফলের চিহ্ন কেমন হয়?", "ঋণাত্মক", ["ধনাত্মক", "শূন্য", "অসংজ্ঞায়িত"], "বিপরীত দিকে ধনাত্মক।", M),
]
def e_area(b):
    A, B, C = rp(-5, 6), rp(-5, 6), rp(-5, 6); v = tarea(A, B, C)
    if not v: return
    b.add(f"{P(*A)}, {P(*B)}, {P(*C)} শীর্ষবিশিষ্ট ত্রিভুজের ক্ষেত্রফল কত বর্গ একক?", fr(v), W(fr(v), [fr(v * 2), fr(v / 2), fr(v + 1)]), "½|x₁(y₂ − y₃) + …|।", E)
def e_axis(b):
    a, c = R.randint(1, 12), R.randint(1, 12)
    b.add(f"(0, 0), ({a}, 0), (0, {c}) শীর্ষবিশিষ্ট ত্রিভুজের ক্ষেত্রফল কত?", fr(F(a * c, 2)), W(fr(F(a * c, 2)), [str(a * c), str(a + c), fr(F(a * c, 2) + 1)]), "½ × ভূমি × উচ্চতা।", E)
def e_col(b):
    A = rp(); d = (R.randint(-3, 3), R.randint(-3, 3))
    if d == (0, 0): return
    k1, k2 = R.sample([1, 2, 3, -1, -2], 2)
    b.add(f"{P(*A)}, {P(A[0] + k1 * d[0], A[1] + k1 * d[1])}, {P(A[0] + k2 * d[0], A[1] + k2 * d[1])} বিন্দু তিনটি কেমন?", "সমরেখ", ["সমকোণী ত্রিভুজের শীর্ষ", "সমবাহু ত্রিভুজের শীর্ষ", "সমদ্বিবাহু ত্রিভুজের শীর্ষ"], "ক্ষেত্রফল শূন্য।", E)
def m_quad(b):
    pts = [rp(-5, 6) for _ in range(4)]; cx, cy = sum(p[0] for p in pts) / 4, sum(p[1] for p in pts) / 4
    pts.sort(key=lambda p: math.atan2(p[1] - cy, p[0] - cx))
    if len(set(pts)) < 4: return
    def cr(o, a, c): return (a[0] - o[0]) * (c[1] - o[1]) - (a[1] - o[1]) * (c[0] - o[0])
    if not all(cr(pts[i], pts[(i + 1) % 4], pts[(i + 2) % 4]) > 0 for i in range(4)): return
    v = F(abs(sum(pts[i][0] * pts[(i + 1) % 4][1] - pts[(i + 1) % 4][0] * pts[i][1] for i in range(4))), 2)
    b.add(f"{', '.join(P(*p) for p in pts)} শীর্ষবিশিষ্ট চতুর্ভুজের ক্ষেত্রফল কত?", fr(v), W(fr(v), [fr(v * 2), fr(v + 2), fr(v / 2)]), "দুই ত্রিভুজে ভাগ বা সূত্র।", M)
def m_kcol(b):
    A = rp(); d = (R.randint(1, 3), R.randint(-3, 3)); k = R.randint(2, 3)
    B = (A[0] + d[0], A[1] + d[1]); C = (A[0] + k * d[0], A[1] + k * d[1])
    b.add(f"{P(*A)}, {P(*B)}, ({num(C[0])}, p) সমরেখ হলে p = কত?", num(C[1]), W(num(C[1]), [num(C[1] + 1), num(-C[1]) if C[1] else '1', num(C[0])]), "ক্ষেত্রফল শূন্য।", M)
def m_mid(b):
    A, B, C = rp(-5, 6), rp(-5, 6), rp(-5, 6); v = tarea(A, B, C)
    if not v: return
    b.add(f"{P(*A)}, {P(*B)}, {P(*C)} ত্রিভুজের বাহুগুলোর মধ্যবিন্দু দিয়ে গঠিত ত্রিভুজের ক্ষেত্রফল কত?", fr(v / 4), W(fr(v / 4), [fr(v / 2), fr(v), fr(v / 3)]), "মূল ক্ষেত্রফলের এক-চতুর্থাংশ।", M)
def m_polar_area(b):
    r1, r2 = R.randint(1, 8), R.randint(1, 8); d = R.choice([30, 90, 150])
    v = F(r1 * r2, 2) * {30: F(1, 2), 90: 1, 150: F(1, 2)}[d]
    b.add(f"মূলবিন্দু, ({r1}, 0°) ও ({r2}, {d}°) পোলার বিন্দু তিনটি দিয়ে গঠিত ত্রিভুজের ক্ষেত্রফল কত?", fr(v), W(fr(v), [fr(F(r1 * r2, 2)), fr(v * 2), str(r1 * r2)]), "½ r₁r₂ sin(θ₂ − θ₁)।", M)
def h_karea(b):
    A, B = rp(-4, 5), rp(-4, 5); t = R.randint(-4, 5); k = R.randint(-5, 6); C = (t, k)
    v = tarea(A, B, C)
    if not v or A[0] == B[0]: return
    coef = A[0] - B[0]; base = A[0] * B[1] - B[0] * A[1] + t * (A[1] - B[1]); s = base + k * coef
    k2 = F(-s - base, coef); ok = f"{num(k)} বা {num(k2)}" if k2 != k else num(k)
    b.add(f"{P(*A)}, {P(*B)}, ({num(t)}, k) ত্রিভুজের ক্ষেত্রফল {fr(v)} হলে k = কত?", ok, W(ok, [num(k), f"{num(-k)} বা {num(-k2)}", f"{num(k + 1)} বা {num(k2 - 1)}"]), "পরমমান থাকায় দুটি মান।", H)
def h_eqtri(b):
    a = 2 * R.randint(1, 6); v = F(a * a, 4)
    s = f"{v.numerator if v.numerator > 1 else ''}√3"
    b.add(f"(0, 0) ও ({a}, 0) দুটি শীর্ষবিশিষ্ট সমবাহু ত্রিভুজের ক্ষেত্রফল কত?", s, W(s, [f"{a * a // 2}√3", str(a * a // 2), f"{a}√3"]), "(√3/4)a²।", H)
def h_line_axes(b):
    a, c = R.choice([v for v in range(-8, 9) if abs(v) > 1]), R.choice([v for v in range(-8, 9) if abs(v) > 1])
    v = F(abs(a * c), 2)
    b.add(f"x/{a if a > 0 else '(' + num(a) + ')'} + y/{c if c > 0 else '(' + num(c) + ')'} = 1 রেখা ও অক্ষদ্বয় দ্বারা গঠিত ত্রিভুজের ক্ষেত্রফল কত?", fr(v), W(fr(v), [str(abs(a * c)), str(abs(a) + abs(c)), fr(v + 1)]), "½|ab|।", H)
p3c = run('3.C', R, fx3c, [e_area, e_axis, e_col], [m_quad, m_kcol, m_mid, m_polar_area], [h_karea, h_eqtri, h_line_axes])

fx3d = [
 ("x-অক্ষের সমান্তরাল রেখার ঢাল কত?", "0", ["1", "অসংজ্ঞায়িত", "−1"], "উল্লম্ব পরিবর্তন নেই।", E),
 ("y-অক্ষের সমান্তরাল রেখার ঢাল কেমন?", "অসংজ্ঞায়িত", ["0", "1", "−1"], "হর শূন্য।", E),
 ("রেখা x-অক্ষের ধনাত্মক দিকের সাথে θ কোণ করলে ঢাল কত?", "tan θ", ["sin θ", "cos θ", "cot θ"], "m = tan θ।", E),
 ("কোনো বিন্দু নির্দিষ্ট শর্ত মেনে চললে যে পথ রচনা করে তাকে কী বলে?", "সঞ্চারপথ", ["স্পর্শক", "ব্যাস", "ঢাল"], "সংজ্ঞা।", E),
]
def e_slope(b):
    A, B = rp(), rp()
    if A[0] == B[0] or A == B: return
    m = F(B[1] - A[1], B[0] - A[0])
    b.add(f"{P(*A)} ও {P(*B)} বিন্দুগামী রেখার ঢাল কত?", num(m), W(num(m), [num(1 / m) if m else '1', num(-m) if m else '−1', num(-1 / m) if m else '2', num(m + 1)]), "(y₂ − y₁)/(x₂ − x₁)।", E)
def e_ang(b):
    d, v = R.choice([(30, '1/√3'), (45, '1'), (60, '√3'), (120, '−√3'), (135, '−1'), (150, '−1/√3')])
    b.add(f"x-অক্ষের ধনাত্মক দিকের সাথে {d}° কোণে আনত রেখার ঢাল কত?", v, W(v, ['1/√3', '1', '√3', '−√3', '−1', '−1/√3']), f"tan {d}°।", E)
def m_k(b):
    A = rp(); m = nz(-4, 4); dx = nz(-4, 4)
    b.add(f"{P(*A)} ও ({num(A[0] + dx)}, k) বিন্দুগামী রেখার ঢাল {num(m)} হলে k = কত?", num(A[1] + m * dx), W(num(A[1] + m * dx), [num(A[1] - m * dx), num(m * dx), num(A[1] + m * dx + 1)]), "ঢালের সূত্রে সমীকরণ।", M)
def m_locus_circ(b):
    A = rp(-4, 5); r = R.randint(1, 6)
    ok = f"x² + y² {'−' if A[0] > 0 else '+'} {abs(2 * A[0])}x {'−' if A[1] > 0 else '+'} {abs(2 * A[1])}y {'+' if A[0] ** 2 + A[1] ** 2 - r * r >= 0 else '−'} {abs(A[0] ** 2 + A[1] ** 2 - r * r)} = 0".replace(' + 0x', '').replace(' − 0x', '').replace(' + 0y', '').replace(' − 0y', '').replace(' + 0 = 0', ' = 0').replace(' − 0 = 0', ' = 0')
    b.add(f"একটি বিন্দু {P(*A)} থেকে সর্বদা {r} একক দূরে থাকলে তার সঞ্চারপথের সমীকরণ কোনটি?", ok, W(ok, [ok.replace(f"{abs(A[0] ** 2 + A[1] ** 2 - r * r)} = 0", f"{abs(A[0] ** 2 + A[1] ** 2 + r * r)} = 0"), f"(x {'−' if A[0] >= 0 else '+'} {abs(A[0])}) + (y {'−' if A[1] >= 0 else '+'} {abs(A[1])}) = {r}", f"x² + y² = {r * r}"]), "(x − h)² + (y − k)² = r²।", M)
def m_locus_eq(b):
    A, B = rp(), rp()
    if A == B: return
    a, c, k = norm(2 * (B[0] - A[0]), 2 * (B[1] - A[1]), A[0] ** 2 + A[1] ** 2 - B[0] ** 2 - B[1] ** 2)
    ok = L(a, c, k)
    b.add(f"{P(*A)} ও {P(*B)} থেকে সমদূরবর্তী বিন্দুর সঞ্চারপথ কোনটি?", ok, W(ok, [L(*norm(a, c, -k)) if k else L(a, c, 1), L(*norm(c, a, k)), L(*norm(a, -c, k)) if c else L(a, 2, k)]), "লম্বদ্বিখণ্ডক।", M)
def m_col(b):
    A = rp(); d = (R.randint(1, 3), R.randint(-3, 3)); k = R.randint(2, 4)
    b.add(f"A{P(*A)}, B{P(A[0] + d[0], A[1] + d[1])}, C{P(A[0] + k * d[0], A[1] + k * d[1])} বিন্দুগুলোর জন্য AB ও BC-এর ঢাল সমান। বিন্দুগুলো কেমন?", "সমরেখ", ['পরস্পর লম্ব', 'সমবাহু ত্রিভুজের শীর্ষ', 'বৃত্তের উপর'], "সমান ঢাল ও সাধারণ বিন্দু।", M)
def h_perp(b):
    m1 = F(nz(-5, 5), R.choice([1, 2])); A = rp(); dx = nz(-4, 4)
    ky = A[1] + (-1 / m1) * dx
    if ky.denominator > 1: return
    b.add(f"ঢাল {num(m1)} বিশিষ্ট রেখার লম্ব একটি রেখা {P(*A)} ও ({num(A[0] + dx)}, k) বিন্দুগামী হলে k = কত?", num(ky), W(num(ky), [num(A[1] + m1 * dx), num(ky + 1), num(-ky) if ky else '2']), "লম্বের ঢাল −1/m।", H)
def h_locus_ratio(b):
    a = R.randint(1, 6)
    ok = f"x² + y² = {a * a}"
    b.add(f"একটি বিন্দু (−{a}, 0) ও ({a}, 0) থেকে এমনভাবে চলে যে তাদের সাথে সংযোগ রেখা দুটি পরস্পর লম্ব থাকে। সঞ্চারপথ কোনটি?", ok, W(ok, [f"x² − y² = {a * a}", f"x² + y² = {2 * a * a}", f"y² = {4 * a}x"]), f"ঢালের গুণফল −1 ⇒ y² = {a * a} − x²।", H)
def h_slope_area(b):
    m = R.choice([1, -1]); A = rp(); dx = R.randint(1, 6)
    b.add(f"{P(*A)} বিন্দুগামী একটি রেখা x-অক্ষের সাথে {45 if m == 1 else 135}° কোণে আনত। রেখাটি ({num(A[0] + dx)}, k) দিয়ে গেলে k = কত?", num(A[1] + m * dx), W(num(A[1] + m * dx), [num(A[1] - m * dx), num(A[1] + dx + 1), num(A[0] + m * dx)]), f"ঢাল {m}।", H)
p3d = run('3.D', R, fx3d, [e_slope, e_ang], [m_k, m_locus_circ, m_locus_eq, m_col], [h_perp, h_locus_ratio, h_slope_area], caps=(16, 13, 8))

fx3e = [
 ("ঢাল m ও y-ছেদক c বিশিষ্ট রেখার সমীকরণ কোনটি?", "y = mx + c", ["y = cx + m", "x = my + c", "y = m(x + c)"], "ঢাল-ছেদক আকার।", E),
 ("(x₁, y₁) বিন্দুগামী ঢাল m বিশিষ্ট রেখার সমীকরণ কোনটি?", "y − y₁ = m(x − x₁)", ["y + y₁ = m(x + x₁)", "y = mx − y₁", "x − x₁ = m(y − y₁)"], "বিন্দু-ঢাল আকার।", E),
 ("অক্ষদ্বয় থেকে a ও b ছেদক বিশিষ্ট রেখা কোনটি?", "x/a + y/b = 1", ["x/b + y/a = 1", "ax + by = 1", "x/a − y/b = 1"], "ছেদক আকার।", E),
 ("মূলবিন্দু থেকে রেখার উপর লম্ব p এবং লম্বটি x-অক্ষের সাথে α কোণ করলে রেখার সমীকরণ কোনটি?", "x cos α + y sin α = p", ["x sin α + y cos α = p", "x cos α − y sin α = p", "x + y = p"], "লম্ব আকার।", M),
]
def e_mc(b):
    m, c = nz(-6, 6), R.randint(-9, 9)
    ok = 'y = ' + pfmt({k: v for k, v in {(1,): m, (0,): c}.items() if v}, ('x',))
    b.add(f"ঢাল {num(m)} ও y-ছেদক {num(c)} বিশিষ্ট রেখার সমীকরণ কোনটি?", ok, W(ok, ['y = ' + pfmt({k: v for k, v in {(1,): c, (0,): m}.items() if v}, ('x',)) if c else f"y = {num(m)}", 'y = ' + pfmt({k: v for k, v in {(1,): -m, (0,): c}.items() if v}, ('x',)), 'y = ' + pfmt({k: v for k, v in {(1,): m, (0,): -c}.items() if v}, ('x',)) if c else 'y = ' + pfmt({(1,): m, (0,): 1}, ('x',))]), "y = mx + c।", E)
def e_int(b):
    a, c, k = nz(-6, 6), nz(-6, 6), nz(-12, 12)
    xi, yi = F(-k, a), F(-k, c)
    ok = f"x-ছেদক {num(xi)}, y-ছেদক {num(yi)}"
    b.add(f"{L(a, c, k)} রেখার অক্ষদ্বয়ের ছেদক কোনটি?", ok, W(ok, [f"x-ছেদক {num(yi)}, y-ছেদক {num(xi)}", f"x-ছেদক {num(-xi)}, y-ছেদক {num(-yi)}", f"x-ছেদক {num(k)}, y-ছেদক {num(k)}"]), "অপর চলক শূন্য বসিয়ে।", E)
def e_slope_of(b):
    a, c, k = nz(-6, 6), nz(-6, 6), R.randint(-9, 9)
    m = F(-a, c)
    b.add(f"{L(a, c, k)} রেখার ঢাল কত?", num(m), W(num(m), [num(-m), num(F(c, a)), num(F(-c, a)), num(m + 1)]), "−a/b।", E)
def m_two(b):
    A, B = rp(), rp()
    if A[0] == B[0] or A == B: return
    a, c, k = norm(B[1] - A[1], A[0] - B[0], B[0] * A[1] - A[0] * B[1]); ok = L(a, c, k)
    b.add(f"{P(*A)} ও {P(*B)} বিন্দুগামী রেখার সমীকরণ কোনটি?", ok, W(ok, [L(*norm(a, -c, k)) if c else L(a, 1, k), L(*norm(a, c, -k)) if k else L(a, c, 1), L(a, c, k + 2)]), "দুই বিন্দু আকার।", M)
def m_ptm(b):
    A = rp(); m = F(nz(-5, 5), R.choice([1, 2, 3]))
    a, c, k = norm(m.numerator, -m.denominator, m.denominator * A[1] - m.numerator * A[0]); ok = L(a, c, k)
    b.add(f"{P(*A)} বিন্দুগামী ও {num(m)} ঢালবিশিষ্ট রেখার সমীকরণ কোনটি?", ok, W(ok, [L(*norm(a, -c, k)), L(*norm(a, c, -k)) if k else L(a, c, 3), L(a, c, k + 1)]), "y − y₁ = m(x − x₁)।", M)
def m_inter_eq(b):
    a, c = R.choice([v for v in range(-8, 9) if abs(v) > 1]), R.choice([v for v in range(-8, 9) if abs(v) > 1])
    aa, cc, kk = norm(c, a, -a * c); ok = L(aa, cc, kk)
    b.add(f"x-অক্ষ ও y-অক্ষের ছেদক যথাক্রমে {num(a)} ও {num(c)} হলে রেখার সমীকরণ কোনটি?", ok, W(ok, [L(*norm(a, c, -a * c)), L(*norm(c, a, a * c)) if a * c else L(1, 1, 1), L(*norm(c, -a, -a * c))]), "x/a + y/b = 1 থেকে সরল করে।", M)
def m_angle_line(b):
    A = rp(); d, mm = R.choice([(45, 1), (135, -1)])
    a, c, k = norm(mm, -1, A[1] - mm * A[0]); ok = L(a, c, k)
    b.add(f"{P(*A)} বিন্দুগামী এবং x-অক্ষের সাথে {d}° কোণে আনত রেখার সমীকরণ কোনটি?", ok, W(ok, [L(*norm(-mm, -1, A[1] + mm * A[0])), L(a, c, -k) if k else L(a, c, 2), L(1, 1, 0) if (a, c, k) != (1, 1, 0) else L(1, -1, 0)]), f"ঢাল tan {d}° = {mm}।", M)
def h_mid_perp(b):
    A, B = rp(), rp()
    if A == B or (A[0] + B[0]) % 2 or (A[1] + B[1]) % 2: return
    a, c, k = norm(2 * (B[0] - A[0]), 2 * (B[1] - A[1]), A[0] ** 2 + A[1] ** 2 - B[0] ** 2 - B[1] ** 2); ok = L(a, c, k)
    b.add(f"{P(*A)} ও {P(*B)}-এর সংযোগ রেখাংশের লম্বদ্বিখণ্ডকের সমীকরণ কোনটি?", ok, W(ok, [L(*norm(a, c, -k)) if k else L(a, c, 1), L(*norm(c, -a, k)) if (c, -a) != (a, c) else L(a, c, k + 1), L(a, c, k + 1)]), "মধ্যবিন্দুগামী ও লম্ব।", H)
def h_sum_int(b):
    a = R.randint(2, 9); A = (a, a)
    # x/p + y/q = 1, p + q = s, বিন্দু (h, k) দিয়ে যায়
    p, q = R.sample(range(2, 10), 2); h = R.randint(1, p - 1); kk = F(q) * (1 - F(h, p))
    if kk.denominator > 1: return
    ok = f"x/{p} + y/{q} = 1"
    b.add(f"একটি রেখা ({h}, {int(kk)}) বিন্দু দিয়ে যায় এবং অক্ষদ্বয়ের ধনাত্মক ছেদকের যোগফল {p + q}। নিচের কোনটি রেখাটির সম্ভাব্য সমীকরণ?", ok, W(ok, [f"x/{q} + y/{p} = 1" if F(h, q) + F(int(kk), p) != 1 else f"x/{p + 1} + y/{q - 1} = 1", f"x/{p + 1} + y/{q - 1} = 1", f"x/{p - 1} + y/{q + 1} = 1"]), "বিন্দু বসিয়ে যাচাই।", H)
def h_normal(b):
    p = R.randint(1, 8); al, (c, s) = R.choice([(0, ('1', '0')), (90, ('0', '1')), (45, ('1/√2', '1/√2')), (60, ('1/2', '√3/2')), (30, ('√3/2', '1/2'))])
    ok = {0: f"x = {p}", 90: f"y = {p}", 45: f"x + y = {p}√2" if p > 1 else "x + y = √2", 60: f"x + √3y = {2 * p}", 30: f"√3x + y = {2 * p}"}[al]
    b.add(f"মূলবিন্দু থেকে একটি রেখার উপর লম্বের দৈর্ঘ্য {p} এবং লম্বটি x-অক্ষের সাথে {al}° কোণ উৎপন্ন করে। রেখার সমীকরণ কোনটি?", ok, W(ok, [f"x = {p}", f"y = {p}", f"x + y = {p}√2" if p > 1 else "x + y = √2", f"x + √3y = {2 * p}", f"√3x + y = {2 * p}"]), "x cos α + y sin α = p।", H)
p3e = run('3.E', R, fx3e, [e_mc, e_int, e_slope_of], [m_two, m_ptm, m_inter_eq, m_angle_line], [h_mid_perp, h_sum_int, h_normal])

fx3f = [
 ("a₁x + b₁y + c₁ = 0 ও a₂x + b₂y + c₂ = 0 রেখাদ্বয় সমান্তরাল হওয়ার শর্ত কোনটি?", "a₁/a₂ = b₁/b₂", ["a₁a₂ + b₁b₂ = 0", "a₁/a₂ = c₁/c₂", "a₁b₁ = a₂b₂"], "ঢাল সমান।", E),
 ("উপরের রেখাদ্বয় পরস্পর লম্ব হওয়ার শর্ত কোনটি?", "a₁a₂ + b₁b₂ = 0", ["a₁/a₂ = b₁/b₂", "a₁b₂ = a₂b₁", "c₁ = c₂"], "m₁m₂ = −1।", E),
 ("ঢাল m₁ ও m₂ বিশিষ্ট রেখাদ্বয়ের মধ্যবর্তী কোণ θ হলে tan θ = কত?", "±(m₁ − m₂)/(1 + m₁m₂)", ["(m₁ + m₂)/(1 − m₁m₂)", "m₁m₂", "(m₁ − m₂)/(1 − m₁m₂)"], "সূত্র।", M),
]
def e_inter(b):
    x, y = R.randint(-5, 6), R.randint(-5, 6)
    a1, c1, a2, c2 = R.choice([1, 2, 3, -1]), R.choice([1, 2, -1, -2]), R.choice([1, 2, -1, 3]), R.choice([1, -1, 3, -2])
    if a1 * c2 == a2 * c1: return
    k1, k2 = -(a1 * x + c1 * y), -(a2 * x + c2 * y); ok = P(x, y)
    b.add(f"{L(a1, c1, k1)} এবং {L(a2, c2, k2)} রেখাদ্বয়ের ছেদবিন্দু কোনটি?", ok, W(ok, [P(y, x), P(-x, -y) if (x or y) else P(1, 1), P(x + 1, y)]), "সমাধান করে।", E)
def e_par(b):
    a, c = R.choice([1, 2, 3, -2]), R.choice([1, -1, 2, -3]); k = R.randint(-9, 9); A = rp()
    k2 = -(a * A[0] + c * A[1]); ok = L(*norm(a, c, k2))
    b.add(f"{P(*A)} বিন্দুগামী এবং {L(a, c, k)} রেখার সমান্তরাল রেখার সমীকরণ কোনটি?", ok, W(ok, [L(*norm(c, -a, -(c * A[0] - a * A[1]))), L(*norm(a, c, -k2)) if k2 else L(a, c, 2), L(*norm(a, c, k2 + 1))]), "ax + by + k′ = 0।", E)
def m_perp(b):
    a, c = R.choice([1, 2, 3, -2]), R.choice([1, -1, 2, -3]); k = R.randint(-9, 9); A = rp()
    k2 = -(c * A[0] - a * A[1]); ok = L(*norm(c, -a, k2))
    b.add(f"{P(*A)} বিন্দুগামী এবং {L(a, c, k)} রেখার উপর লম্ব রেখার সমীকরণ কোনটি?", ok, W(ok, [L(*norm(a, c, -(a * A[0] + c * A[1]))), L(*norm(c, a, -(c * A[0] + a * A[1]))), L(*norm(c, -a, k2 + 1))]), "bx − ay + k′ = 0।", M)
def m_kpar(b):
    a, c = nz(-5, 5), nz(-5, 5); t = R.choice([2, 3, -2])
    b.add(f"{L(a, c, 3)} ও {pfmt({(1, 0): a * t}, ('x', 'y'))} + ky + 7 = 0 রেখাদ্বয় সমান্তরাল হলে k = কত?", num(c * t), W(num(c * t), [num(-c * t), num(F(-a * a * t, c)) if F(-a * a * t, c) != c * t else num(c * t + 1), num(c)]), "a₁/a₂ = b₁/b₂।", M)
def m_kperp(b):
    a, c = nz(-5, 5), nz(-5, 5); p = nz(-5, 5)
    k = F(-a * p, c)
    b.add(f"{L(a, c, 3)} ও {pfmt({(1, 0): p}, ('x', 'y'))} + ky − 2 = 0 রেখাদ্বয় পরস্পর লম্ব হলে k = কত?", num(k), W(num(k), [num(-k) if k else '1', num(F(c * p, a)), num(k + 1)]), "a₁a₂ + b₁b₂ = 0।", M)
def m_angle(b):
    pairs = [((1, 0), '45°'), ((F(1), F(-1)), '90°'), ((F(3) ** 0, F(0)), '45°')]
    m1, m2, ok = R.choice([(F(1), F(0), '45°'), (F(2), F(-1, 2), '90°'), (F(3), F(-1, 3), '90°'), (F(1, 2), F(-3), '45°'), (F(3), F(1, 2), '45°'), (F(2), F(-3), '45°')])
    b.add(f"ঢাল {num(m1)} ও {num(m2)} বিশিষ্ট রেখাদ্বয়ের মধ্যবর্তী সূক্ষ্মকোণ কত?", ok, W(ok, ['30°', '45°', '60°', '90°']), "|(m₁ − m₂)/(1 + m₁m₂)|।", M)
def h_conc(b):
    x, y = R.randint(-4, 5), R.randint(-4, 5); a1, c1 = 1, R.choice([1, 2, -1]); a2, c2 = R.choice([2, 3, -1]), R.choice([1, -2, 3])
    if a1 * c2 == a2 * c1: return
    k1, k2 = -(a1 * x + c1 * y), -(a2 * x + c2 * y); p = nz(-4, 4); k = -(p * x + y)
    b.add(f"{L(a1, c1, k1)}, {L(a2, c2, k2)} এবং {pfmt({(1, 0): p, (0, 1): 1}, ('x', 'y'))} + k = 0 সমবিন্দু হলে k = কত?", num(k), W(num(k), [num(-k) if k else '1', num(k + 1), num(x + y)]), f"ছেদবিন্দু ({num(x)}, {num(y)}) বসিয়ে।", H)
def h_through_inter(b):
    x, y = R.randint(-4, 5), R.randint(-4, 5); a1, c1, a2, c2 = 1, 1, 1, -1
    k1, k2 = -(x + y), -(x - y)
    a, c, k = norm(y, -x, 0) if (x or y) else (1, 1, 0)
    ok = L(a, c, k)
    if (a, c) == (0, 0): return
    b.add(f"{L(a1, c1, k1)} ও {L(a2, c2, k2)}-এর ছেদবিন্দু ও মূলবিন্দুগামী রেখার সমীকরণ কোনটি?", ok, W(ok, [L(*norm(x, -y, 0)) if (x, -y) != (0, 0) and norm(x, -y, 0) != (a, c, k) else L(1, 1, 0), L(*norm(a, c, 1)), L(1, -1, 0) if (a, c) != (1, -1) else L(1, 2, 0)]), f"ছেদবিন্দু ({num(x)}, {num(y)})।", H)
def h_angle_bis(b):
    m = R.randint(2, 6)
    b.add(f"y = {m}x রেখাটি y = −{m}x রেখার সাথে যে কোণ উৎপন্ন করে তার সমদ্বিখণ্ডক কোনগুলো?", "x = 0 ও y = 0", ["y = x ও y = −x", f"y = {m}x ও y = 0", "শুধু x = 0"], "রেখাদ্বয় অক্ষের সাপেক্ষে প্রতিসম।", H)
p3f = run('3.F', R, fx3f, [e_inter, e_par], [m_perp, m_kpar, m_kperp, m_angle], [h_conc, h_through_inter, h_angle_bis], caps=(16, 13, 10))

fx3g = [
 ("(x₁, y₁) বিন্দু থেকে ax + by + c = 0 রেখার লম্ব দূরত্ব কত?", "|ax₁ + by₁ + c|/√(a² + b²)", ["(ax₁ + by₁ + c)/(a² + b²)", "|ax₁ + by₁|/√(a² + b²)", "|ax₁ + by₁ + c|"], "লম্ব দূরত্বের সূত্র।", E),
 ("ax + by + c₁ = 0 ও ax + by + c₂ = 0 সমান্তরাল রেখার দূরত্ব কত?", "|c₁ − c₂|/√(a² + b²)", ["|c₁ + c₂|/√(a² + b²)", "|c₁ − c₂|", "(c₁ − c₂)/(a + b)"], "সূত্র।", E),
 ("মূলবিন্দু থেকে ax + by + c = 0-এর দূরত্ব কত?", "|c|/√(a² + b²)", ["c/(a + b)", "|c|", "√(a² + b²)/|c|"], "x₁ = y₁ = 0।", E),
]
def e_pd(b):
    a, c = R.choice([(3, 4), (4, 3), (5, 12), (12, 5), (6, 8), (8, 6), (1, 0), (0, 1)]); a *= R.choice([1, -1])
    A = rp(); d = R.randint(1, 6); n = math.isqrt(a * a + c * c); k = d * n - (a * A[0] + c * A[1])
    b.add(f"{P(*A)} বিন্দু থেকে {L(a, c, k)} রেখার লম্ব দূরত্ব কত?", d, W(d, [d * n, d + 1, abs(k), F(d, n) if n > 1 else d + 2]), "সূত্রে বসিয়ে।", E)
def e_origin(b):
    a, c = R.choice([(3, 4), (5, 12), (6, 8), (8, 15), (1, 1), (2, 1)]); k = nz(-20, 20)
    n2 = a * a + c * c; r = math.isqrt(n2)
    ok = fr(F(abs(k), r)) if r * r == n2 else f"{abs(k)}/{surd(n2)}"
    b.add(f"মূলবিন্দু থেকে {L(a, c, k)} রেখার দূরত্ব কত?", ok, W(ok, [str(abs(k)), fr(F(abs(k), a + c)), f"{abs(k)}/{n2}"]), "|c|/√(a² + b²)।", E)
def m_par(b):
    a, c = R.choice([(3, 4), (4, 3), (5, 12), (12, 5), (6, 8), (8, 6)]); k1, k2 = R.sample(range(-20, 21), 2)
    n = math.isqrt(a * a + c * c); v = F(abs(k1 - k2), n)
    b.add(f"{L(a, c, k1)} ও {L(a, c, k2)} রেখাদ্বয়ের মধ্যবর্তী দূরত্ব কত?", fr(v), W(fr(v), [fr(F(abs(k1 + k2), n)), str(abs(k1 - k2)), fr(v + 1)]), "|c₁ − c₂|/√(a² + b²)।", M)
def m_k(b):
    a, c = R.choice([(3, 4), (4, 3), (5, 12), (12, 5)]); d = R.randint(1, 5); n = math.isqrt(a * a + c * c)
    ok = f"±{d * n}"
    b.add(f"মূলবিন্দু থেকে {a}x + {c}y + k = 0 রেখার দূরত্ব {d} হলে k = কত?", ok, W(ok, [str(d * n), f"±{d}", f"±{d * (a + c)}"]), f"|k|/{n} = {d}।", M)
def m_foot(b):
    A = rp(-4, 5)
    # x-অক্ষের উপর লম্বের পাদবিন্দু
    kind = R.choice(['x', 'y'])
    ok = P(A[0], 0) if kind == 'x' else P(0, A[1])
    b.add(f"{P(*A)} বিন্দু থেকে {kind}-অক্ষের উপর অঙ্কিত লম্বের পাদবিন্দু কোনটি?", ok, W(ok, [P(0, A[1]) if kind == 'x' else P(A[0], 0), P(*A), P(0, 0)]), "অক্ষের উপর প্রক্ষেপ।", M)
def h_tri_h(b):
    A, B, C = rp(-4, 5), rp(-4, 5), rp(-4, 5); ar = tarea(A, B, C)
    d2 = (B[0] - C[0]) ** 2 + (B[1] - C[1]) ** 2
    r = math.isqrt(d2)
    if not ar or r * r != d2: return
    h = 2 * ar / r
    b.add(f"{P(*A)}, {P(*B)}, {P(*C)} ত্রিভুজে A থেকে BC-এর উপর লম্বের দৈর্ঘ্য কত?", fr(h), W(fr(h), [fr(ar / r), fr(h + 1), str(r)]), f"2 × ক্ষেত্রফল/BC = {fr(h)}।", H)
def h_bis(b):
    a, c = R.choice([(3, 4), (4, 3), (5, 12), (12, 5)])
    ok1 = L(*norm(a - c, c - a, 0)) if False else None
    # 3x + 4y = 0 ও 4x + 3y = 0-এর কোণ সমদ্বিখণ্ডক: x + y = 0 এবং x − y = 0
    b.add(f"{L(a, c, 0)} ও {L(c, a, 0)} রেখাদ্বয়ের কোণ সমদ্বিখণ্ডকদ্বয় কোনটি?", "x + y = 0 ও x − y = 0", ["x = 0 ও y = 0", f"{a}x = {c}y", "শুধু x + y = 0"], "(ax + by)/√(a² + b²) = ±(…)।", H)
def h_dist_eq(b):
    a, c = R.choice([(3, 4), (4, 3), (5, 12), (12, 5), (6, 8)]); k = R.randint(-15, 15); d = R.randint(1, 4); n = math.isqrt(a * a + c * c)
    ok = f"{L(a, c, k + d * n)} ও {L(a, c, k - d * n)}"
    b.add(f"{L(a, c, k)} রেখার সমান্তরাল এবং তা থেকে {d} একক দূরের রেখাদ্বয় কোনটি?", ok, W(ok, [f"{L(a, c, k + d)} ও {L(a, c, k - d)}", f"{L(c, a, k + d * n)} ও {L(c, a, k - d * n)}", f"{L(a, c, d * n)} ও {L(a, c, -d * n)}"]), f"|k′ − ({num(k)})|/{n} = {d}।", H)
p3g = run('3.G', R, fx3g, [e_pd, e_origin], [m_par, m_k, m_foot], [h_tri_h, h_bis, h_dist_eq], caps=(16, 18, 10))
save('i3', p3a + p3b + p3c + p3d + p3e + p3f + p3g)

# ---------------- 4 বৃত্ত ----------------
def circ(h, k, r2):
    c = h * h + k * k - r2
    s = 'x² + y²'
    if h: s += f" {'−' if h > 0 else '+'} {abs(2 * h)}x"
    if k: s += f" {'−' if k > 0 else '+'} {abs(2 * k)}y"
    if c: s += f" {'+' if c > 0 else '−'} {abs(c)}"
    return s + ' = 0'
fx4a = [
 ("x² + y² + 2gx + 2fy + c = 0 বৃত্তের কেন্দ্র কোনটি?", "(−g, −f)", ["(g, f)", "(−f, −g)", "(2g, 2f)"], "সাধারণ সমীকরণ।", E),
 ("উপরের বৃত্তের ব্যাসার্ধ কত?", "√(g² + f² − c)", ["√(g² + f² + c)", "g² + f² − c", "√(g + f − c)"], "সূত্র।", E),
 ("(h, k) কেন্দ্র ও r ব্যাসার্ধের বৃত্তের সমীকরণ কোনটি?", "(x − h)² + (y − k)² = r²", ["(x + h)² + (y + k)² = r²", "(x − h)² + (y − k)² = r", "x² + y² = r²"], "কেন্দ্র-ব্যাসার্ধ আকার।", E),
 ("ax² + by² + 2hxy + … = 0 বৃত্ত নির্দেশ করার শর্ত কোনটি?", "a = b ≠ 0 এবং h = 0", ["a ≠ b", "h ≠ 0", "a = −b"], "x² ও y²-এর সহগ সমান, xy পদ নেই।", M),
]
def e_cr(b):
    h, k, r = R.randint(-6, 6), R.randint(-6, 6), R.randint(1, 8); ok = f"কেন্দ্র {P(h, k)}, ব্যাসার্ধ {r}"
    b.add(f"{circ(h, k, r * r)} বৃত্তের কেন্দ্র ও ব্যাসার্ধ কোনটি?", ok, W(ok, [f"কেন্দ্র {P(-h, -k)}, ব্যাসার্ধ {r}", f"কেন্দ্র {P(h, k)}, ব্যাসার্ধ {r * r}", f"কেন্দ্র {P(2 * h, 2 * k)}, ব্যাসার্ধ {r}" if (h or k) else f"কেন্দ্র (1, 1), ব্যাসার্ধ {r}"]), "(−g, −f) ও √(g² + f² − c)।", E)
def e_eq(b):
    h, k, r = R.randint(-6, 6), R.randint(-6, 6), R.randint(1, 8); ok = circ(h, k, r * r)
    b.add(f"কেন্দ্র {P(h, k)} ও ব্যাসার্ধ {r} বিশিষ্ট বৃত্তের সমীকরণ কোনটি?", ok, W(ok, [circ(-h, -k, r * r) if (h or k) else circ(1, 0, r * r), circ(h, k, r), circ(h, k, r * r + 2)]), "(x − h)² + (y − k)² = r²।", E)
def e_on(b):
    h, k, r = R.randint(-4, 4), R.randint(-4, 4), R.choice([5, 10, 13]); t = {5: (3, 4), 10: (6, 8), 13: (5, 12)}[r]
    pt = (h + t[0], k + t[1]); ok = 'বৃত্তের উপর'
    alt = R.choice([0, 1, 2]); pt = [pt, (h + 1, k + 1), (h + r, k + r)][alt]; ok = ['বৃত্তের উপর', 'বৃত্তের ভিতরে', 'বৃত্তের বাইরে'][alt]
    b.add(f"{P(*pt)} বিন্দুটি {circ(h, k, r * r)} বৃত্তের সাপেক্ষে কোথায় অবস্থিত?", ok, W(ok, ['বৃত্তের উপর', 'বৃত্তের ভিতরে', 'বৃত্তের বাইরে', 'কেন্দ্রে']), "বিন্দু বসিয়ে মানের চিহ্ন দেখে।", E)
def m_diam(b):
    A, B = rp(-5, 6), rp(-5, 6)
    if A == B: return
    # (x − x1)(x − x2) + (y − y1)(y − y2) = 0
    g, f, c = -(A[0] + B[0]), -(A[1] + B[1]), A[0] * B[0] + A[1] * B[1]
    def ce(g, f, c):
        t = 'x² + y²' + (f" {'+' if g > 0 else '−'} {abs(g) if abs(g) != 1 else ''}x" if g else '') + (f" {'+' if f > 0 else '−'} {abs(f) if abs(f) != 1 else ''}y" if f else '')
        return t + (f" {'+' if c > 0 else '−'} {abs(c)}" if c else '') + ' = 0'
    s = ce(g, f, c)
    b.add(f"{P(*A)} ও {P(*B)} বিন্দুদ্বয়কে ব্যাসের প্রান্তবিন্দু ধরে অঙ্কিত বৃত্তের সমীকরণ কোনটি?", s, W(s, [ce(-g, -f, c), ce(g, f, -c) if c else ce(g, f, 1), ce(g, f, c + 2)]), "(x − x₁)(x − x₂) + (y − y₁)(y − y₂) = 0।", M)
def m_touch_x(b):
    h, k = R.randint(-6, 6), nz(-6, 6); ok = circ(h, k, k * k)
    b.add(f"{P(h, k)} কেন্দ্রবিশিষ্ট এবং x-অক্ষকে স্পর্শ করে এমন বৃত্তের সমীকরণ কোনটি?", ok, W(ok, [circ(h, k, h * h) if h * h != k * k else circ(h, k, k * k + 1), circ(h, k, h * h + k * k), circ(-h, -k, k * k)]), "ব্যাসার্ধ = |k|।", M)
def m_origin(b):
    h, k = R.randint(-6, 6), R.randint(-6, 6)
    if not (h or k): return
    ok = circ(h, k, h * h + k * k)
    b.add(f"{P(h, k)} কেন্দ্রবিশিষ্ট এবং মূলবিন্দুগামী বৃত্তের সমীকরণ কোনটি?", ok, W(ok, [circ(-h, -k, h * h + k * k), circ(h, k, h * h + k * k + 4), circ(h, k, abs(h) + abs(k))]), "ব্যাসার্ধ = মূলবিন্দু থেকে কেন্দ্রের দূরত্ব।", M)
def m_area(b):
    h, k, r = R.randint(-6, 6), R.randint(-6, 6), R.randint(1, 9)
    b.add(f"{circ(h, k, r * r)} বৃত্তের ক্ষেত্রফল কত?", f"{r * r}π", W(f"{r * r}π", [f"{2 * r}π", f"{r}π", f"{r ** 4}π", f"{r * r + 1}π"]), f"r = {r}।", M)
def h_three(b):
    h, k, r = R.randint(-3, 3), R.randint(-3, 3), 5
    pts = [(h + 3, k + 4), (h - 4, k + 3), (h + 5, k)]
    ok = circ(h, k, 25)
    b.add(f"{', '.join(P(*p) for p in pts)} বিন্দুগামী বৃত্তের সমীকরণ কোনটি?", ok, W(ok, [circ(-h, -k, 25) if (h or k) else circ(1, 1, 25), circ(h, k, 16), circ(h, k, 36)]), f"কেন্দ্র {P(h, k)}, ব্যাসার্ধ 5।", H)
def h_touch_both(b):
    a = R.randint(1, 8); s = R.choice([(1, 1), (1, -1), (-1, 1), (-1, -1)])
    ok = circ(s[0] * a, s[1] * a, a * a)
    b.add(f"{['প্রথম', 'দ্বিতীয়', 'চতুর্থ', 'তৃতীয়'][[(1, 1), (-1, 1), (1, -1), (-1, -1)].index(s)]} চতুর্ভাগে অবস্থিত, উভয় অক্ষকে স্পর্শ করে এবং ব্যাসার্ধ {a} এমন বৃত্তের সমীকরণ কোনটি?", ok, W(ok, [circ(-s[0] * a, -s[1] * a, a * a), circ(s[0] * a, s[1] * a, 2 * a * a), circ(s[0] * a, -s[1] * a, a * a)]), f"কেন্দ্র ({num(s[0] * a)}, {num(s[1] * a)})।", H)
def h_intercept(b):
    h, k, r = R.randint(-4, 4), R.randint(-4, 4), R.randint(5, 9)
    if r * r - k * k <= 0: return
    v = r * r - k * k; ch = 2 * math.isqrt(v) if math.isqrt(v) ** 2 == v else None
    ok = str(ch) if ch else f"2√{v}"
    if not ch and math.isqrt(v) ** 2 != v: ok = '2' + surd(v) if not surd(v).startswith('√') else f"2{surd(v)}"
    b.add(f"{circ(h, k, r * r)} বৃত্ত x-অক্ষ থেকে যে জ্যা ছেদ করে তার দৈর্ঘ্য কত?", ok, W(ok, [str(2 * r), surd(v) if math.isqrt(v) ** 2 != v else str(math.isqrt(v)), str(2 * abs(h)) if h else '1']), "2√(g² − c)।", H)
p4a = run('4.A', R, fx4a, [e_cr, e_eq, e_on], [m_diam, m_touch_x, m_origin, m_area], [h_three, h_touch_both, h_intercept])

fx4b = [
 ("বৃত্তের কোনো বিন্দুতে স্পর্শক ও ঐ বিন্দুগামী ব্যাসার্ধের মধ্যবর্তী কোণ কত?", "90°", ["45°", "60°", "180°"], "স্পর্শক ব্যাসার্ধের উপর লম্ব।", E),
 ("x² + y² = a² বৃত্তের (x₁, y₁) বিন্দুতে স্পর্শকের সমীকরণ কোনটি?", "xx₁ + yy₁ = a²", ["xx₁ − yy₁ = a²", "x + y = a", "x₁x² + y₁y² = a²"], "সূত্র।", E),
 ("y = mx + c রেখা x² + y² = a² বৃত্তকে স্পর্শ করার শর্ত কোনটি?", "c² = a²(1 + m²)", ["c = a(1 + m)", "c² = a²(1 − m²)", "c² = a² + m²"], "কেন্দ্র থেকে দূরত্ব = ব্যাসার্ধ।", M),
 ("বহিঃস্থ বিন্দু থেকে বৃত্তে কয়টি স্পর্শক আঁকা যায়?", "2টি", ["1টি", "0টি", "অসংখ্য"], "", E),
]
def e_tan(b):
    x1, y1 = R.choice([(3, 4), (4, 3), (5, 12), (12, 5), (6, 8), (0, 5), (5, 0)]); x1 *= R.choice([1, -1]); y1 *= R.choice([1, -1]); r2 = x1 * x1 + y1 * y1
    ok = pfmt({kk: v for kk, v in {(1, 0): x1, (0, 1): y1}.items() if v}, ('x', 'y')) + f" = {r2}"
    b.add(f"x² + y² = {r2} বৃত্তের {P(x1, y1)} বিন্দুতে স্পর্শকের সমীকরণ কোনটি?", ok, W(ok, [pfmt({kk: v for kk, v in {(1, 0): y1, (0, 1): x1}.items() if v}, ('x', 'y')) + f" = {r2}", pfmt({kk: v for kk, v in {(1, 0): x1, (0, 1): -y1}.items() if v}, ('x', 'y')) + f" = {r2}" if y1 else f"x = {x1 + 1}", pfmt({kk: v for kk, v in {(1, 0): x1, (0, 1): y1}.items() if v}, ('x', 'y')) + f" = {math.isqrt(r2)}"]), "xx₁ + yy₁ = a²।", E)
def e_tlen(b):
    h, k = R.randint(-4, 4), R.randint(-4, 4); r = R.randint(1, 6); d = R.choice([(3, 4), (5, 12), (6, 8), (8, 6)])
    t = R.choice([(3, 4), (5, 12), (6, 8), (8, 15)])
    # স্পর্শকের দৈর্ঘ্য √(S₁)
    P_ = (h + r + R.randint(1, 5), k + R.randint(-3, 3)); S1 = (P_[0] - h) ** 2 + (P_[1] - k) ** 2 - r * r
    ok = sqf(S1)
    b.add(f"{P(*P_)} বিন্দু থেকে {circ(h, k, r * r)} বৃত্তে অঙ্কিত স্পর্শকের দৈর্ঘ্য কত?", ok, W(ok, [str(S1), sqf(S1 + r * r), sqf(S1 + 1)]), "√S₁।", E)
def m_cond(b):
    a, m = R.randint(1, 6), R.randint(-4, 4)
    v = a * a * (1 + m * m); r = math.isqrt(v)
    ok = f"±{r}" if r * r == v else f"±{surd(v)}"
    b.add(f"y = {m}x + c রেখাটি x² + y² = {a * a} বৃত্তকে স্পর্শ করলে c = কত?".replace('y = 0x + c', 'y = c').replace('y = 1x', 'y = x').replace('y = -1x', 'y = −x'), ok, W(ok, [f"±{a}", f"±{a * (1 + abs(m))}", f"±{a * a * (1 + m * m)}"]), "c² = a²(1 + m²)।", M)
def m_touch(b):
    a = R.choice([(3, 4, 5), (5, 12, 13), (6, 8, 10), (8, 6, 10), (12, 5, 13)]); r = a[2]
    k = R.choice([1, -1]) * r * r // 1
    rr = r * r
    b.add(f"{a[0]}x + {a[1]}y = k রেখাটি x² + y² = {rr} বৃত্তকে স্পর্শ করলে k = কত?", f"±{r * r}", W(f"±{r * r}", [f"±{r}", f"±{a[0] + a[1]}", f"±{r * (a[0] + a[1])}"]), f"|k|/{r} = {r}।", M)
def m_chord(b):
    r = R.choice([5, 10, 13, 15, 17, 25]); d = {5: 3, 10: 6, 13: 5, 15: 9, 17: 8, 25: 7}[r]; half = math.isqrt(r * r - d * d)
    b.add(f"{r} সেমি ব্যাসার্ধের বৃত্তের কেন্দ্র থেকে {d} সেমি দূরের জ্যায়ের দৈর্ঘ্য কত?", 2 * half, W(2 * half, [half, 2 * r, 2 * half + 2]), f"2√({r}² − {d}²)।", M)
def m_normal(b):
    h, k = R.randint(-5, 5), R.randint(-5, 5); r = R.randint(2, 6); x1 = h + r; y1 = k
    ok = f"y = {num(k)}"
    b.add(f"{circ(h, k, r * r)} বৃত্তের {P(x1, y1)} বিন্দুতে অভিলম্বের সমীকরণ কোনটি?", ok, W(ok, [f"x = {num(x1)}", f"y = {num(x1)}", f"x = {num(h)}"]), "অভিলম্ব কেন্দ্রগামী; কেন্দ্র ও বিন্দুর কোটি সমান।", M)
def h_tangent_par(b):
    a = R.choice([(3, 4, 5), (5, 12, 13), (6, 8, 10), (4, 3, 5)]); r = a[2]; R2 = r * r
    ok = f"{a[0]}x + {a[1]}y = ±{R2}"
    b.add(f"x² + y² = {R2} বৃত্তের যে স্পর্শকগুলো {a[0]}x + {a[1]}y = 7 রেখার সমান্তরাল, সেগুলো কোনটি?", ok, W(ok, [f"{a[0]}x + {a[1]}y = ±{r}", f"{a[1]}x − {a[0]}y = ±{R2}", f"{a[0]}x + {a[1]}y = ±7"]), f"|k|/{r} = {r}।", H)
def h_common_chord(b):
    a, c = R.randint(1, 6), R.randint(1, 6)
    ok = f"{2 * a}x + {2 * c}y = 0".replace('2x', '2x')
    a1 = norm(2 * a, 2 * c, 0)
    ok = L(*a1)
    b.add(f"x² + y² = 25 ও x² + y² + {2 * a}x + {2 * c}y − 25 = 0 বৃত্তদ্বয়ের সাধারণ জ্যায়ের সমীকরণ কোনটি?", ok, W(ok, [L(*norm(2 * c, 2 * a, 0)) if a != c else L(1, -1, 0), L(*norm(2 * a, 2 * c, -50)), L(1, 1, 0) if a != c else L(1, 2, 0)]), "S₁ − S₂ = 0।", H)
def h_touch_circles(b):
    r1, r2 = R.randint(1, 6), R.randint(1, 6); d = r1 + r2
    b.add(f"x² + y² = {r1 * r1} এবং (x − {d})² + y² = {r2 * r2} বৃত্তদ্বয় পরস্পরকে কীভাবে স্পর্শ করে?", 'বহিঃস্থভাবে', ['অন্তঃস্থভাবে', 'ছেদ করে', 'স্পর্শ করে না'], f"কেন্দ্র-দূরত্ব {d} = r₁ + r₂।", H)
p4b = run('4.B', R, fx4b, [e_tan, e_tlen], [m_cond, m_touch, m_chord, m_normal], [h_tangent_par, h_common_chord, h_touch_circles], caps=(16, 13, 10))
save('i4', p4a + p4b)

# ---------------- 5 বিন্যাস ও সমাবেশ ----------------
Pm, Cm, fact = math.perm, math.comb, math.factorial
fx5a = [
 ("ⁿPᵣ = কত?", "n!/(n − r)!", ["n!/(r!(n − r)!)", "n!/r!", "(n − r)!"], "বিন্যাসের সূত্র।", E),
 ("0! = কত?", "1", ["0", "অসংজ্ঞায়িত", "∞"], "সংজ্ঞা।", E),
 ("n টি ভিন্ন বস্তুকে বৃত্তাকারে সাজানোর উপায় কত?", "(n − 1)!", ["n!", "n!/2", "(n + 1)!"], "বৃত্তাকার বিন্যাস।", M),
 ("n টি বস্তুর p টি এক জাতীয় ও বাকিগুলো ভিন্ন হলে সাজানোর উপায় কত?", "n!/p!", ["n!", "n!/(n − p)!", "p!"], "সূত্র।", M),
]
WORDS = ['BANGLA', 'DHAKA', 'SCIENCE', 'MATHEMATICS', 'COLLEGE', 'PAPER', 'APPLE', 'BOOK', 'LETTER', 'SUCCESS', 'ACADEMY', 'PENCIL', 'NUMBER', 'TRIANGLE', 'ORANGE', 'CIRCLE', 'EXAM']
def word_perm(w):
    from collections import Counter
    v = fact(len(w))
    for c in Counter(w).values(): v //= fact(c)
    return v
def e_npr(b):
    n = R.randint(4, 10); r = R.randint(2, min(4, n))
    v = Pm(n, r)
    b.add(f"{n}P{r} = কত?", v, W(v, [Cm(n, r), Pm(n, r - 1), n * r, v + n]), f"{n}!/{n - r}! = {v}।", E)
def e_fact(b):
    n = R.randint(3, 8)
    b.add(f"{n}! = কত?", fact(n), W(fact(n), [fact(n - 1), fact(n) // 2, n * (n + 1) // 2, fact(n) + n]), "গুণফল।", E)
def e_word(b):
    w = R.choice([x for x in WORDS if len(x) <= 7]); v = word_perm(w)
    b.add(f"'{w}' শব্দের সবগুলো অক্ষর নিয়ে কত প্রকারে সাজানো যায়?", v, W(v, [fact(len(w)), v * 2 if v * 2 != fact(len(w)) else v + 1, v // 2 if v % 2 == 0 and v // 2 != v else v + 3]), "পুনরাবৃত্ত অক্ষরের ফ্যাক্টোরিয়াল দিয়ে ভাগ।", E)
def m_circ(b):
    n = R.randint(4, 9)
    b.add(f"{n} জন লোককে একটি গোল টেবিলের চারদিকে কত প্রকারে বসানো যায়?", fact(n - 1), W(fact(n - 1), [fact(n), fact(n - 1) // 2, fact(n - 2)]), f"({n} − 1)!।", M)
def m_digits(b):
    ds = sorted(R.sample(range(1, 10), R.randint(4, 6))); r = R.randint(2, 3)
    v = Pm(len(ds), r)
    b.add(f"{', '.join(map(str, ds))} অঙ্কগুলো থেকে প্রতিটি একবার নিয়ে {r} অঙ্কের কতগুলো সংখ্যা গঠন করা যায়?", v, W(v, [Cm(len(ds), r), len(ds) ** r, v + len(ds)]), f"{len(ds)}P{r}।", M)
def m_vowel_together(b):
    w = R.choice(['MOTHER', 'FATHER', 'PENCIL', 'NUMBER', 'COPIER', 'DAUGHTER'.replace('DAUGHTER', 'MANGO')])
    vs = [c for c in w if c in 'AEIOU']; cs = [c for c in w if c not in 'AEIOU']
    if len(set(w)) != len(w): return
    v = fact(len(cs) + 1) * fact(len(vs))
    b.add(f"'{w}' শব্দের অক্ষরগুলো সাজালে স্বরবর্ণগুলো একত্রে থাকবে এমন সাজানোর সংখ্যা কত?", v, W(v, [fact(len(w)), fact(len(cs)) * fact(len(vs)), fact(len(cs) + 1)]), f"স্বরগুলো একটি একক: ({len(cs) + 1})! × {len(vs)}!।", M)
def m_npr_find(b):
    n = R.randint(4, 12); v = Pm(n, 2)
    b.add(f"ⁿP₂ = {v} হলে n = কত?", n, W(n, [n + 1, n - 1, v // 2]), f"n(n − 1) = {v}।", M)
def m_even(b):
    ds = sorted(R.sample(range(1, 10), 5)); ev = [d for d in ds if d % 2 == 0]
    if not ev: return
    v = len(ev) * Pm(4, 3)
    b.add(f"{', '.join(map(str, ds))} অঙ্কগুলো থেকে প্রতিটি একবার নিয়ে চার অঙ্কের কতগুলো জোড় সংখ্যা গঠন করা যায়?", v, W(v, [Pm(5, 4), len(ev) * Pm(4, 2), v + 4]), f"একক স্থানে {len(ev)}টি জোড় অঙ্ক × 4P3।", M)
def h_rep(b):
    w = R.choice(['MATHEMATICS', 'SUCCESS', 'COLLEGE', 'ACADEMY', 'STATISTICS', 'ENGINEERING', 'BANANA', 'PEPPER'])
    v = word_perm(w)
    b.add(f"'{w}' শব্দের সবগুলো অক্ষর নিয়ে কত প্রকারে সাজানো যায়?", v, W(v, [fact(len(w)), v * 2, v // 2 if v % 2 == 0 else v + 1]), "n!/(p!q!…)।", H)
def h_neck(b):
    n = R.randint(5, 9)
    b.add(f"{n}টি ভিন্ন রঙের পুঁতি দিয়ে কত প্রকারে মালা গাঁথা যায়?", fact(n - 1) // 2, W(fact(n - 1) // 2, [fact(n - 1), fact(n), fact(n) // 2]), "(n − 1)!/2।", H)
def h_not_together(b):
    n = R.randint(5, 8)
    v = fact(n) - 2 * fact(n - 1)
    b.add(f"{n} জন ছাত্রকে এক সারিতে বসাতে হবে যেন নির্দিষ্ট দুজন একত্রে না বসে। কত প্রকারে বসানো যায়?", v, W(v, [2 * fact(n - 1), fact(n), fact(n) - fact(n - 1)]), f"{n}! − 2 × ({n} − 1)!।", H)
def h_rep_digits(b):
    k, r = R.randint(3, 6), R.randint(2, 4)
    b.add(f"{k}টি ভিন্ন অঙ্ক থেকে পুনরাবৃত্তি অনুমোদিত হলে {r} অঙ্কের কতগুলো সংখ্যা (প্রথম অঙ্ক শূন্য নয়, অঙ্কগুলো 1–{k}) গঠন করা যায়?", k ** r, W(k ** r, [Pm(k, r) if r <= k else k * r, r ** k, k * r]), f"{k}{sup(r)}।", H)
p5a = run('5.A', R, fx5a, [e_npr, e_fact, e_word], [m_circ, m_digits, m_vowel_together, m_npr_find, m_even], [h_rep, h_neck, h_not_together, h_rep_digits])

fx5b = [
 ("ⁿCᵣ = কত?", "n!/(r!(n − r)!)", ["n!/(n − r)!", "n!/r!", "r!/(n − r)!"], "সমাবেশের সূত্র।", E),
 ("ⁿCᵣ = ⁿCₙ₋ᵣ — এটি কী নির্দেশ করে?", "সমপূরক সমাবেশ সমান", ["বিন্যাস সমান", "n = r", "সবসময় 1"], "বাছাই ও বাদ দেওয়ার উপায় সমান।", E),
 ("ⁿCᵣ + ⁿCᵣ₋₁ = কত?", "ⁿ⁺¹Cᵣ", ["ⁿCᵣ₊₁", "ⁿ⁻¹Cᵣ", "2ⁿCᵣ"], "প্যাসকেলের সূত্র।", M),
 ("ⁿPᵣ ও ⁿCᵣ-এর সম্পর্ক কোনটি?", "ⁿPᵣ = r!·ⁿCᵣ", ["ⁿCᵣ = r!·ⁿPᵣ", "ⁿPᵣ = ⁿCᵣ", "ⁿPᵣ = n!·ⁿCᵣ"], "সাজানোর জন্য r! গুণ।", M),
]
def e_ncr(b):
    n = R.randint(4, 12); r = R.randint(2, n - 2); v = Cm(n, r)
    b.add(f"{n}C{r} = কত?", v, W(v, [Pm(n, r), Cm(n, r - 1) if Cm(n, r - 1) != v else v + 1, n * r]), f"= {v}।", E)
def e_team(b):
    n, r = R.randint(5, 12), R.randint(2, 5)
    if r >= n: return
    b.add(f"{n} জন খেলোয়াড় থেকে {r} জনের একটি দল কত প্রকারে বাছাই করা যায়?", Cm(n, r), W(Cm(n, r), [Pm(n, r), Cm(n, r) + n, n * r]), f"{n}C{r}।", E)
def e_lines(b):
    n = R.randint(4, 12)
    b.add(f"কোনো তিনটি সমরেখ নয় এমন {n}টি বিন্দু দিয়ে কয়টি সরলরেখা আঁকা যায়?", Cm(n, 2), W(Cm(n, 2), [Pm(n, 2), Cm(n, 3), n * n]), f"{n}C2।", E)
def m_diag(b):
    n = R.randint(5, 15)
    v = Cm(n, 2) - n
    b.add(f"{n} বাহুবিশিষ্ট বহুভুজের কর্ণ কয়টি?", v, W(v, [Cm(n, 2), n * (n - 3), v + n // 2]), f"{n}C2 − {n}।", M)
def m_tri(b):
    n = R.randint(5, 12)
    b.add(f"কোনো তিনটি সমরেখ নয় এমন {n}টি বিন্দু দিয়ে কয়টি ত্রিভুজ গঠন করা যায়?", Cm(n, 3), W(Cm(n, 3), [Pm(n, 3), Cm(n, 2), Cm(n, 3) + n]), f"{n}C3।", M)
def m_mixed(b):
    a, c = R.randint(4, 9), R.randint(3, 8); p, q = R.randint(1, 3), R.randint(1, 3)
    v = Cm(a, p) * Cm(c, q)
    b.add(f"{a} জন ছাত্র ও {c} জন ছাত্রী থেকে {p} জন ছাত্র ও {q} জন ছাত্রীর একটি কমিটি কত প্রকারে গঠন করা যায়?", v, W(v, [Cm(a + c, p + q), Cm(a, p) + Cm(c, q), v * 2]), f"{a}C{p} × {c}C{q}।", M)
def m_find_n(b):
    n = R.randint(5, 15); r = R.randint(2, 4); s = R.randint(r + 1, n - 1)
    if Cm(n, r) != Cm(n, s): s = n - r
    if s == r: return
    b.add(f"ⁿC{r} = ⁿC{s} হলে n = কত?", r + s, W(r + s, [abs(s - r), r * s, r + s + 1]), "r + s = n।", M)
def h_atleast(b):
    a, c = R.randint(3, 7), R.randint(3, 7); k = R.randint(3, 5)
    v = Cm(a + c, k) - Cm(c, k)
    b.add(f"{a} জন ছাত্র ও {c} জন ছাত্রী থেকে {k} জনের কমিটি গঠন করতে হবে যাতে কমপক্ষে একজন ছাত্র থাকে। কত প্রকারে সম্ভব?", v, W(v, [Cm(a + c, k), Cm(a, 1) * Cm(a + c - 1, k - 1), v + Cm(c, k) + 1]), f"মোট − শুধু ছাত্রী = {Cm(a + c, k)} − {Cm(c, k)}।", H)
def h_select_arrange(b):
    n, r = R.randint(5, 9), R.randint(2, 4)
    v = Cm(n, r) * fact(r)
    b.add(f"{n}টি বই থেকে {r}টি বাছাই করে একটি তাকে সাজানোর উপায় কত?", v, W(v, [Cm(n, r), fact(n), Cm(n, r) + fact(r)]), f"{n}C{r} × {r}! = {n}P{r}।", H)
def h_handshake(b):
    n = R.randint(5, 25)
    b.add(f"একটি সভায় প্রত্যেকে প্রত্যেকের সাথে একবার করমর্দন করলে মোট {Cm(n, 2)}টি করমর্দন হয়। সভায় কতজন ছিলেন?", n, W(n, [n + 1, n - 1, Cm(n, 2) // 2]), f"nC2 = {Cm(n, 2)}।", H)
def h_total(b):
    n = R.randint(3, 8)
    b.add(f"{n}টি ভিন্ন ফল থেকে এক বা একাধিক ফল কত প্রকারে বাছাই করা যায়?", 2 ** n - 1, W(2 ** n - 1, [2 ** n, n * n, fact(n)]), "2ⁿ − 1।", H)
p5b = run('5.B', R, fx5b, [e_ncr, e_team, e_lines], [m_diag, m_tri, m_mixed, m_find_n], [h_atleast, h_select_arrange, h_handshake, h_total])
save('i5', p5a + p5b)
