#!/usr/bin/env python3
"""দশম শ্রেণি সাধারণ গণিত, অধ্যায় 2 (সেট ও ফাংশন):
অনুশীলনী 2.1 (সেট) ও 2.2 (অন্বয় ও ফাংশন) — প্রতিটিতে 30 সহজ + 50 মধ্যম + 20 কঠিন = 100 MCQ।
হিসাবের উত্তর কোডে গণনা করা; সংখ্যা ইংরেজি অঙ্কে। আউটপুট: src/mcq/ch2.json"""
import json, random, pathlib, itertools, math
from fractions import Fraction as F

R = random.Random(2026103102)
E, M, H = 'সহজ', 'মধ্যম', 'কঠিন'

def S(xs):
    xs = sorted(set(xs), key=lambda v: (isinstance(v, str), v))
    return '∅' if not xs else '{' + ', '.join(str(x) for x in xs) + '}'
def P(pairs):
    return '{' + ', '.join(f'({a}, {b})' for a, b in sorted(pairs)) + '}'
def fr(x):
    x = F(x)
    return str(x.numerator) if x.denominator == 1 else f'{x.numerator}/{x.denominator}'

def poly_str(a, b, c=None):
    """ax + b  বা  ax² + bx + c"""
    def term(coef, var, first):
        if coef == 0: return ''
        sign = '' if first else (' + ' if coef > 0 else ' − ')
        if first and coef < 0: sign = '−'
        mag = abs(coef)
        if var and mag == 1: return sign + var
        return sign + f'{mag}{var}'
    if c is None:
        s = term(a, 'x', True); s += term(b, '', not s); return s or '0'
    s = term(a, 'x²', True); s += term(b, 'x', not s); s += term(c, '', not s); return s or '0'

class Bank:
    def __init__(s, ex): s.ex, s.items, s.seen = ex, [], set()
    def add(s, q, c, wrong, e, lv):
        c = str(c); opts = [c]
        for w in wrong:
            w = str(w)
            if w not in opts: opts.append(w)
        if len(opts) < 4: return False       # বিকল্প কম হলে প্রশ্ন বাদ
        opts = opts[:4]
        key = q + '|' + c
        if key in s.seen: return False
        s.seen.add(key)
        R.shuffle(opts)
        s.items.append({'q': q, 'o': opts, 'a': opts.index(c), 'e': e, 'lv': lv, 'ex': s.ex})
        return True
    def count(s, lv): return sum(1 for x in s.items if x['lv'] == lv)

def near_int(v, k=3):
    out = []
    for d in (1, -1, 2, -2, 3, 4, -3, 5):
        if v + d not in out and v + d != v: out.append(v + d)
        if len(out) == k: break
    return out

def fill(bank, lv, need, gens, cap=6):
    tries, used = 0, {}
    while bank.count(lv) < need:
        tries += 1
        assert tries < 40000, (bank.ex, lv, bank.count(lv))
        live = [g for g in gens if used.get(g.__name__, 0) < cap] or gens
        g = R.choice(live); before = bank.count(lv); g()
        if bank.count(lv) > before: used[g.__name__] = used.get(g.__name__, 0) + 1

# ====================================================================
#                         অনুশীলনী 2.1: সেট
# ====================================================================
b1 = Bank('2.1')
concept_easy_1 = [
 ("ফাঁকা সেটকে কোন প্রতীক দিয়ে প্রকাশ করা হয়?", "∅", ["0", "{0}", "U"], "যে সেটে কোনো উপাদান নেই তাকে ফাঁকা সেট বলে; প্রতীক ∅ বা { }।"),
 ("সেট প্রকাশের পদ্ধতি কয়টি?", "2টি", ["1টি", "3টি", "4টি"], "তালিকা পদ্ধতি ও সেট গঠন পদ্ধতি।"),
 ("{x : x স্বাভাবিক সংখ্যা} সেটটি কোন ধরনের?", "অসীম সেট", ["সসীম সেট", "ফাঁকা সেট", "একক সেট"], "স্বাভাবিক সংখ্যা অসংখ্য, তাই সেটটি অসীম।"),
 ("ফাঁকা সেট যেকোনো সেটের কী?", "উপসেট", ["প্রকৃত সুপারসেট", "পূরক সেট", "সমান সেট"], "∅ প্রত্যেক সেটের উপসেট।"),
 ("যেকোনো সেট A-এর জন্য নিচের কোনটি সর্বদা সত্য?", "A ⊆ A", ["A ⊂ ∅", "A = ∅", "A ∩ A = ∅"], "প্রত্যেক সেট নিজের উপসেট।"),
 ("A ∩ B = ∅ হলে A ও B-কে কী বলে?", "নিশ্চেদ সেট", ["সমান সেট", "উপসেট", "শক্তি সেট"], "যে দুই সেটের কোনো সাধারণ উপাদান নেই তারা নিশ্চেদ সেট।"),
 ("U সার্বিক সেট হলে A ∪ A′ = কত?", "U", ["∅", "A", "A′"], "একটি সেট ও তার পূরক মিলে সার্বিক সেট।"),
 ("A ∩ A′ = কত?", "∅", ["U", "A", "A′"], "কোনো উপাদান একই সাথে A-তে ও A-এর বাইরে থাকতে পারে না।"),
 ("(A′)′ = কত?", "A", ["A′", "U", "∅"], "পূরকের পূরক মূল সেট।"),
 ("সেটের উপাদান লেখার সময় একই উপাদান কয়বার লেখা হয়?", "একবার", ["দুইবার", "যতবার আসে ততবার", "লেখা হয় না"], "সেটে প্রত্যেক উপাদান একবারই লেখা হয়।"),
 ("কোনো সেটের সকল উপসেটের সেটকে কী বলে?", "শক্তি সেট", ["সার্বিক সেট", "পূরক সেট", "ফাঁকা সেট"], "P(A) হলো A-এর সকল উপসেটের সেট।"),
 ("(a, b) = (b, a) হবে কখন?", "a = b হলে", ["সর্বদা", "কখনো না", "a > b হলে"], "ক্রমজোড়ে ক্রম গুরুত্বপূর্ণ; সমান হতে হলে a = b লাগবে।"),
 ("A × B কে কী বলে?", "কার্তেসীয় গুণজ", ["সংযোগ সেট", "ছেদ সেট", "শক্তি সেট"], "A × B = {(x, y) : x ∈ A, y ∈ B}।"),
 ("A ⊆ B হলে A ∪ B = কত?", "B", ["A", "∅", "A ∩ B"], "A-এর সব উপাদান B-তে আছে, তাই সংযোগ B।"),
 ("A ⊆ B হলে A ∩ B = কত?", "A", ["B", "∅", "U"], "A-এর সব উপাদানই সাধারণ উপাদান।"),
]
for q, c, w, e in concept_easy_1: b1.add(q, c, w, e, E)

def e_card():
    xs = R.sample(range(1, 30), R.randint(3, 7))
    n = len(xs)
    b1.add(f"A = {S(xs)} হলে n(A) = কত?", n, near_int(n), f"A-তে {n}টি উপাদান আছে।", E)
def e_union():
    a = set(R.sample(range(1, 12), 3)); b = set(R.sample(range(1, 12), 3))
    u = a | b
    b1.add(f"A = {S(a)}, B = {S(b)} হলে A ∪ B = কত?", S(u), [S(a & b), S(a), S(u | {max(u) + 1})], "সংযোগ সেটে দুই সেটের সব উপাদান একবার করে থাকে।", E)
def e_inter():
    a = set(R.sample(range(1, 10), 4)); b = set(R.sample(range(1, 10), 4))
    i = a & b
    b1.add(f"A = {S(a)}, B = {S(b)} হলে A ∩ B = কত?", S(i), [S(a | b), S(a - b), S(b - a)], "ছেদ সেটে শুধু সাধারণ উপাদান থাকে।", E)
def e_subsets():
    n = R.randint(1, 5); xs = R.sample('abcdefgh', n)
    b1.add(f"A = {S(xs)} সেটটির উপসেট সংখ্যা কত?", 2 ** n, [n, 2 * n, 2 ** n - 1], f"n উপাদানের সেটের উপসেট 2ⁿ টি; 2^{n} = {2 ** n}।", E)
def e_prod_size():
    m, n = R.randint(2, 5), R.randint(2, 5)
    b1.add(f"n(A) = {m} এবং n(B) = {n} হলে n(A × B) = কত?", m * n, [m + n, m * n + 1, abs(m - n) + m], f"n(A × B) = n(A) × n(B) = {m} × {n} = {m * n}।", E)
def e_member():
    xs = R.sample(range(1, 20), 4); y = R.choice([v for v in range(1, 20) if v not in xs])
    b1.add(f"A = {S(xs)} হলে নিচের কোনটি সত্য?", f"{y} ∉ A", [f"{y} ∈ A", f"{xs[0]} ∉ A", f"{xs[1]} ∉ A"], f"{y} সংখ্যাটি A-এর উপাদান নয়।", E)
fill(b1, E, 30, [e_card, e_union, e_inter, e_subsets, e_prod_size, e_member])

# ---- মধ্যম ----
def divisors(n): return [d for d in range(1, n + 1) if n % d == 0]
def m_roster_div():
    n = R.choice([6, 8, 10, 12, 15, 16, 18, 20, 24, 28, 30, 36])
    d = divisors(n)
    b1.add(f"{{x : x ∈ N এবং x, {n}-এর গুণনীয়ক}} সেটটিকে তালিকা পদ্ধতিতে লিখলে কোনটি হবে?", S(d), [S(d[1:]), S(d[:-1]), S(d + [2 * n])], f"{n}-এর গুণনীয়কগুলো: {', '.join(map(str, d))}।", M)
def m_roster_less():
    k = R.randint(4, 9)
    b1.add(f"{{x ∈ N : x < {k}}} = কত?", S(range(1, k)), [S(range(0, k)), S(range(1, k + 1)), S(range(0, k + 1))], f"{k}-এর চেয়ে ছোট স্বাভাবিক সংখ্যা 1 থেকে {k - 1}।", M)
def m_roster_quad():
    r1, r2 = R.sample(range(-4, 7), 2)
    s_, p_ = -(r1 + r2), r1 * r2
    poly = poly_str(1, s_, p_)
    ans = S([r1, r2])
    b1.add(f"{{x ∈ R : {poly} = 0}} = কত?", ans, [S([-r1, -r2]), S([r1]), S([r1, r2, 0]) if 0 not in (r1, r2) else S([r1 + 1, r2])],
           f"{poly} = (x − ({r1}))(x − ({r2})) = 0, তাই x = {r1} অথবা {r2}।", M)
def m_diff():
    a = set(R.sample(range(1, 12), 5)); b = set(R.sample(range(1, 12), 5))
    if not a - b or a - b == b - a: return
    b1.add(f"A = {S(a)}, B = {S(b)} হলে A \\ B = কত?", S(a - b), [S(b - a), S(a & b), S(a | b)], "A \\ B = A-তে আছে কিন্তু B-তে নেই এমন উপাদান।", M)
def m_compl():
    U = set(range(1, R.randint(8, 11))); a = set(R.sample(sorted(U), 4))
    b1.add(f"U = {S(U)}, A = {S(a)} হলে A′ = কত?", S(U - a), [S(a), S(U), S((U - a) | {min(a)})], "A′ = U-এর যে উপাদানগুলো A-তে নেই।", M)
def m_demorgan():
    U = set(range(1, 9)); a = set(R.sample(sorted(U), 3)); b = set(R.sample(sorted(U), 3))
    t = R.choice(['u', 'i'])
    if t == 'u':
        ans = U - (a | b)
        b1.add(f"U = {S(U)}, A = {S(a)}, B = {S(b)} হলে (A ∪ B)′ = কত?", S(ans), [S(U - (a & b)), S(a | b), S((U - a) | (U - b)) if (U - a) | (U - b) != ans else S(a)],
               f"A ∪ B = {S(a | b)}; এর পূরক {S(ans)} (= A′ ∩ B′)।", M)
    else:
        ans = U - (a & b)
        b1.add(f"U = {S(U)}, A = {S(a)}, B = {S(b)} হলে (A ∩ B)′ = কত?", S(ans), [S(U - (a | b)), S(a & b), S(a | b) if a | b != ans else S(U)],
               f"A ∩ B = {S(a & b)}; এর পূরক {S(ans)} (= A′ ∪ B′)।", M)
def m_union_count():
    na, nb = R.randint(10, 40), R.randint(10, 40); ni = R.randint(2, min(na, nb) - 1)
    u = na + nb - ni
    b1.add(f"n(A) = {na}, n(B) = {nb} এবং n(A ∩ B) = {ni} হলে n(A ∪ B) = কত?", u, [na + nb, u - ni, na + nb + ni], f"n(A ∪ B) = n(A) + n(B) − n(A ∩ B) = {na} + {nb} − {ni} = {u}।", M)
def m_inter_count():
    na, nb = R.randint(10, 40), R.randint(10, 40); ni = R.randint(2, min(na, nb) - 1); u = na + nb - ni
    b1.add(f"n(A) = {na}, n(B) = {nb} এবং n(A ∪ B) = {u} হলে n(A ∩ B) = কত?", ni, near_int(ni), f"n(A ∩ B) = {na} + {nb} − {u} = {ni}।", M)
def m_pair():
    a, b = R.randint(1, 9), R.randint(1, 9)
    x, y = a + b, a - b
    # (x+y, x−y) = (p, q)
    b1.add(f"(x + y, x − y) = ({x}, {y}) হলে x = কত?", a, [b, x, a + 1], f"x + y = {x}, x − y = {y}; যোগ করে 2x = {2 * a}, x = {a}।", M)
def m_cart():
    a = R.sample(range(1, 6), 2); b = R.sample('abc', 2)
    prod = [(x, y) for x in sorted(a) for y in sorted(b)]
    rev = [(y, x) for x in sorted(a) for y in sorted(b)]
    b1.add(f"A = {S(a)}, B = {S(b)} হলে A × B = কত?", P(prod), [P(rev), P(prod[:3]), P([(x, x) for x in sorted(a)])], "A × B-তে প্রথম উপাদান A থেকে, দ্বিতীয় উপাদান B থেকে।", M)
def m_power_list():
    xs = sorted(R.sample(range(1, 9), 2)); a, c = xs
    ans = '{∅, {%d}, {%d}, {%d, %d}}' % (a, c, a, c)
    b1.add(f"A = {S(xs)} হলে P(A) = কত?", ans, ['{{%d}, {%d}, {%d, %d}}' % (a, c, a, c), '{∅, {%d}, {%d}}' % (a, c), '{∅, {%d, %d}}' % (a, c)], "P(A)-তে ∅ ও A সহ সব উপসেট থাকে, মোট 2² = 4টি।", M)
def m_proper():
    n = R.randint(2, 6)
    b1.add(f"{n} উপাদানবিশিষ্ট একটি সেটের প্রকৃত উপসেট কয়টি?", 2 ** n - 1, [2 ** n, 2 ** n - 2, n], f"প্রকৃত উপসেট = 2ⁿ − 1 = {2 ** n} − 1 = {2 ** n - 1} (সেটটি নিজে বাদ)।", M)
def m_divset_inter():
    p, q = R.sample([12, 18, 20, 24, 30, 36], 2)
    a, b = set(divisors(p)), set(divisors(q))
    b1.add(f"A = {p}-এর গুণনীয়কসমূহের সেট, B = {q}-এর গুণনীয়কসমূহের সেট হলে A ∩ B = কত?", S(a & b), [S(a | b), S(a - b), S((a & b) - {1})], f"সাধারণ গুণনীয়ক অর্থাৎ গ.সা.গু {math.gcd(p, q)}-এর গুণনীয়কসমূহ।", M)
fill(b1, M, 50, [m_roster_div, m_roster_less, m_roster_quad, m_diff, m_compl, m_demorgan, m_union_count, m_inter_count, m_pair, m_cart, m_power_list, m_proper, m_divset_inter])

# ---- কঠিন ----
def h_venn_neither():
    tot = R.randint(40, 100); a = R.randint(15, tot - 10); b = R.randint(15, tot - 10); both = R.randint(3, min(a, b) - 2)
    if a + b - both > tot: return
    nei = tot - (a + b - both)
    b1.add(f"কোনো শ্রেণির {tot} জন শিক্ষার্থীর মধ্যে {a} জন গণিত, {b} জন ইংরেজি এবং {both} জন উভয় বিষয় পছন্দ করে। কতজন কোনোটিই পছন্দ করে না?",
           nei, [tot - a - b + 2 * both if tot - a - b + 2 * both != nei else nei + 2, tot - (a + b), nei + both], f"অন্তত একটি = {a} + {b} − {both} = {a + b - both}; কোনোটিই নয় = {tot} − {a + b - both} = {nei}।", H)
def h_venn_only():
    a = R.randint(20, 60); b = R.randint(20, 60); both = R.randint(5, min(a, b) - 3)
    b1.add(f"একটি জরিপে {a} জন চা ও {b} জন কফি পছন্দ করে; {both} জন উভয়ই পছন্দ করে। শুধু চা পছন্দ করে কতজন?", a - both, [a, b - both, a + b - both], f"শুধু চা = {a} − {both} = {a - both}।", H)
def h_pair2():
    x, y = R.randint(-5, 8), R.randint(-5, 8)
    p, q = 2 * x + y, x - 3 * y
    b1.add(f"(2x + y, x − 3y) = ({p}, {q}) হলে (x, y) = কত?", f"({x}, {y})", [f"({y}, {x})", f"({x}, {-y})", f"({-x}, {y})"], f"2x + y = {p} ও x − 3y = {q} সমাধান করে x = {x}, y = {y}।", H)
def h_power_prod():
    m, n = R.randint(1, 3), R.randint(1, 3)
    b1.add(f"n(A) = {m}, n(B) = {n} হলে P(A × B)-এর উপাদান সংখ্যা কত?", 2 ** (m * n), [2 ** (m + n), m * n, 2 ** (m * n) - 1], f"n(A × B) = {m * n}; তাই উপসেট সংখ্যা 2^{m * n} = {2 ** (m * n)}।", H)
def h_sym():
    a = set(R.sample(range(1, 10), 4)); b = set(R.sample(range(1, 10), 4))
    s = (a - b) | (b - a)
    if not s: return
    b1.add(f"A = {S(a)}, B = {S(b)} হলে (A \\ B) ∪ (B \\ A) = কত?", S(s), [S(a & b), S(a | b), S(a - b)], f"A \\ B = {S(a - b)}, B \\ A = {S(b - a)}; সংযোগ {S(s)}।", H)
def h_quad_power():
    r1, r2 = R.sample(range(1, 7), 2)
    s_, p_ = r1 + r2, r1 * r2
    b1.add(f"A = {{x ∈ N : x² − {s_}x + {p_} = 0}} হলে P(A)-এর উপাদান সংখ্যা কত?", 4, [2, 3, 8], f"x = {r1}, {r2}; n(A) = 2, তাই n(P(A)) = 2² = 4।", H)
def h_cart_inter():
    a = set(R.sample(range(1, 6), 2)); b = set(R.sample(range(1, 6), 2)); c = set(R.sample(range(1, 6), 2))
    ans = [(x, y) for x in sorted(a) for y in sorted(b & c)]
    if not ans: return
    b1.add(f"A = {S(a)}, B = {S(b)}, C = {S(c)} হলে A × (B ∩ C) = কত?", P(ans), [P([(x, y) for x in sorted(a) for y in sorted(b | c)]), P([(y, x) for x, y in ans]), P([(x, y) for x in sorted(a) for y in sorted(b)])],
           f"B ∩ C = {S(b & c)}; তারপর A-এর প্রত্যেক উপাদানের সাথে জোড়।", H)
def h_divisible():
    lo, hi = 1, R.choice([30, 40, 50, 60]); p, q = R.sample([2, 3, 5], 2)
    a = {x for x in range(lo, hi + 1) if x % p == 0}; b = {x for x in range(lo, hi + 1) if x % q == 0}
    u = len(a | b)
    b1.add(f"1 থেকে {hi} পর্যন্ত কতগুলো স্বাভাবিক সংখ্যা {p} অথবা {q} দ্বারা বিভাজ্য?", u, [len(a) + len(b), len(a & b), u + 1], f"{p} দ্বারা {len(a)}টি, {q} দ্বারা {len(b)}টি, উভয় দ্বারা {len(a & b)}টি; মোট {len(a)} + {len(b)} − {len(a & b)} = {u}।", H)
fill(b1, H, 20, [h_venn_neither, h_venn_only, h_pair2, h_power_prod, h_sym, h_quad_power, h_cart_inter, h_divisible])

# ====================================================================
#                   অনুশীলনী 2.2: অন্বয় ও ফাংশন
# ====================================================================
b2 = Bank('2.2')
concept_easy_2 = [
 ("A ও B দুইটি সেট হলে A থেকে B-এ একটি অন্বয় হলো কোনটির উপসেট?", "A × B", ["A ∪ B", "A ∩ B", "B × A"], "A থেকে B-এ অন্বয় R ⊆ A × B।"),
 ("কোনো অন্বয়ের ক্রমজোড়গুলোর প্রথম উপাদানের সেটকে কী বলে?", "ডোমেন", ["রেঞ্জ", "কোডোমেন", "শক্তি সেট"], "ডোমেন = প্রথম উপাদানগুলোর সেট।"),
 ("কোনো অন্বয়ের ক্রমজোড়গুলোর দ্বিতীয় উপাদানের সেটকে কী বলে?", "রেঞ্জ", ["ডোমেন", "উপসেট", "সার্বিক সেট"], "রেঞ্জ = দ্বিতীয় উপাদানগুলোর সেট।"),
 ("যে অন্বয়ে ডোমেনের প্রত্যেক উপাদানের সাথে রেঞ্জের একটিমাত্র উপাদান সম্পর্কিত, তাকে কী বলে?", "ফাংশন", ["সেট", "ক্রমজোড়", "শক্তি সেট"], "ফাংশনে প্রত্যেক x-এর জন্য ঠিক একটি y থাকে।"),
 ("y = f(x) ফাংশনে x-কে কী বলে?", "স্বাধীন চলক", ["অধীন চলক", "ধ্রুবক", "রেঞ্জ"], "x স্বাধীন চলক, y অধীন চলক।"),
 ("y = f(x) ফাংশনে y-কে কী বলে?", "অধীন চলক", ["স্বাধীন চলক", "ডোমেন", "ধ্রুবক"], "y-এর মান x-এর উপর নির্ভর করে।"),
 ("উল্লম্ব রেখা পরীক্ষায় একটি লেখচিত্র ফাংশন হবে যদি যেকোনো উল্লম্ব রেখা লেখচিত্রকে —", "সর্বোচ্চ একবার ছেদ করে", ["অন্তত দুবার ছেদ করে", "কখনো ছেদ না করে", "ঠিক তিনবার ছেদ করে"], "একটি x-এর জন্য একাধিক y থাকলে তা ফাংশন নয়।"),
 ("এক-এক ফাংশনে ডোমেনের ভিন্ন উপাদানের প্রতিচ্ছবি কেমন হয়?", "ভিন্ন", ["একই", "শূন্য", "ঋণাত্মক"], "f(a) = f(b) হলে a = b, এটিই এক-এক ফাংশন।"),
 ("y = 3x + 2 সরলরেখার ঢাল কত?", "3", ["2", "1/3", "5"], "y = mx + c আকারে m হলো ঢাল।"),
 ("{(1, 2), (1, 3), (2, 4)} অন্বয়টি কি ফাংশন?", "না, কারণ 1-এর দুটি প্রতিচ্ছবি", ["হ্যাঁ", "না, কারণ 4 বেশি বড়", "হ্যাঁ, কারণ সব সংখ্যা ধনাত্মক"], "ডোমেনের 1-এর সাথে 2 ও 3 দুটি উপাদান সম্পর্কিত।"),
]
for q, c, w, e in concept_easy_2: b2.add(q, c, w, e, E)

def e_lin_eval():
    a, b = R.choice([2, 3, 4, 5, -2, -3]), R.randint(-6, 7); x = R.randint(-3, 5)
    v = a * x + b
    b2.add(f"f(x) = {poly_str(a, b)} হলে f({x}) = কত?", v, near_int(v), f"f({x}) = {a}×({x}) {'+' if b >= 0 else '−'} {abs(b)} = {v}।", E)
def e_sq_eval():
    x = R.randint(-4, 6); v = x * x
    b2.add(f"f(x) = x² হলে f({x}) = কত?", v, [2 * x, -v if v else 1, v + 1], f"f({x}) = ({x})² = {v}।", E)
def e_domain():
    xs = R.sample(range(1, 9), 3); ys = R.sample(range(1, 9), 3)
    pairs = list(zip(xs, ys))
    b2.add(f"R = {P(pairs)} অন্বয়ের ডোমেন কত?", S(xs), [S(ys), S(xs + ys), S(xs[:2])], "ডোমেন = প্রথম উপাদানগুলোর সেট।", E)
def e_range():
    xs = R.sample(range(1, 9), 3); ys = R.sample(range(10, 19), 3)
    pairs = list(zip(xs, ys))
    b2.add(f"R = {P(pairs)} অন্বয়ের রেঞ্জ কত?", S(ys), [S(xs), S(xs + ys), S(ys[:2])], "রেঞ্জ = দ্বিতীয় উপাদানগুলোর সেট।", E)
def e_point():
    a, b = R.randint(1, 4), R.randint(-3, 5); x = R.randint(0, 4); y = a * x + b
    b2.add(f"নিচের কোন বিন্দুটি y = {poly_str(a, b)} রেখার উপর অবস্থিত?", f"({x}, {y})", [f"({x}, {y + 1})", f"({y}, {x})" if y != x else f"({x + 1}, {y})", f"({x}, {y - 2})"], f"x = {x} বসালে y = {y}।", E)
fill(b2, E, 30, [e_lin_eval, e_sq_eval, e_domain, e_range, e_point])

# ---- মধ্যম ----
def m_quad_eval():
    a, b, c = 1, R.randint(-6, 6), R.randint(-6, 6); x = R.randint(-3, 4)
    v = a * x * x + b * x + c
    b2.add(f"f(x) = {poly_str(a, b, c)} হলে f({x}) = কত?", v, near_int(v), f"f({x}) = ({x})² {'+' if b >= 0 else '−'} {abs(b)}×({x}) {'+' if c >= 0 else '−'} {abs(c)} = {v}।", M)
def m_solve_lin():
    a, b = R.choice([2, 3, 4, 5]), R.randint(-7, 7); x = R.randint(-4, 8); k = a * x + b
    b2.add(f"f(x) = {poly_str(a, b)} এবং f(x) = {k} হলে x = কত?", x, near_int(x), f"{a}x {'+' if b >= 0 else '−'} {abs(b)} = {k} ⇒ {a}x = {k - b} ⇒ x = {x}।", M)
def m_rel_rule():
    A = sorted(R.sample(range(1, 6), 3)); k = R.randint(1, 3)
    B = sorted(set(x + k for x in A) | set(R.sample(range(1, 10), 2)))
    R_ = [(x, x + k) for x in A if x + k in B]
    b2.add(f"A = {S(A)}, B = {S(B)} এবং R = {{(x, y) : x ∈ A, y ∈ B এবং y = x + {k}}} হলে R = কত?", P(R_), [P([(y, x) for x, y in R_]), P([(x, x + k + 1) for x in A]), P(R_[:-1]) if len(R_) > 1 else P([(A[0], A[0])])], f"প্রত্যেক x-এর সাথে {k} যোগ করে B-তে আছে কিনা দেখা হয়েছে।", M)
def m_inverse():
    a = R.choice([2, 3, 4, 5]); b = R.randint(-6, 6)
    ans = f"(x {'−' if b >= 0 else '+'} {abs(b)})/{a}"
    b2.add(f"f(x) = {poly_str(a, b)} হলে f⁻¹(x) = কত?", ans, [f"(x {'+' if b >= 0 else '−'} {abs(b)})/{a}", f"{a}x {'−' if b >= 0 else '+'} {abs(b)}", f"x/{a} {'−' if b >= 0 else '+'} {abs(b)}"], f"y = {poly_str(a, b)} ⇒ x = (y {'−' if b >= 0 else '+'} {abs(b)})/{a}; তাই f⁻¹(x) = {ans}।", M)
def m_frac_eval():
    p, q, r, s = R.randint(1, 4), R.randint(-3, 3), 1, R.randint(-4, 4)
    x = R.choice([v for v in range(-3, 6) if v + s != 0])
    v = F(p * x + q, x + s)
    den = poly_str(1, s); den = den if den == 'x' else f'({den})'
    b2.add(f"f(x) = ({poly_str(p, q)})/{den} হলে f({x}) = কত?", fr(v), [fr(v + 1), fr(-v) if v != 0 else '1', fr(F(p * x + q, x - s)) if x - s != 0 and F(p * x + q, x - s) != v else fr(v + 2)], f"f({x}) = ({p * x + q})/({x + s}) = {fr(v)}।", M)
def m_sum_vals():
    b, c = R.randint(-5, 5), R.randint(-5, 5); x1, x2 = R.sample(range(-3, 5), 2)
    f = lambda x: x * x + b * x + c
    v = f(x1) + f(x2)
    b2.add(f"f(x) = {poly_str(1, b, c)} হলে f({x1}) + f({x2}) = কত?", v, near_int(v), f"f({x1}) = {f(x1)}, f({x2}) = {f(x2)}; যোগফল {v}।", M)
def m_relations_count():
    m, n = R.randint(1, 3), R.randint(1, 3)
    b2.add(f"n(A) = {m}, n(B) = {n} হলে A থেকে B-এ মোট কতগুলো অন্বয় সম্ভব?", 2 ** (m * n), [m * n, 2 ** (m + n), 2 ** (m * n) - 1], f"অন্বয় হলো A × B-এর উপসেট; n(A × B) = {m * n}, তাই 2^{m * n} = {2 ** (m * n)}টি।", M)
def m_is_function():
    xs = R.sample(range(1, 7), 3)
    good = P([(x, R.randint(1, 9)) for x in xs])
    bad1 = P([(xs[0], 1), (xs[0], 2), (xs[1], 3)])
    bad2 = P([(xs[1], 4), (xs[2], 5), (xs[1], 6)])
    bad3 = P([(xs[2], 7), (xs[2], 8), (xs[0], 2)])
    b2.add("নিচের কোন অন্বয়টি ফাংশন?", good, [bad1, bad2, bad3], "ফাংশনে ডোমেনের কোনো উপাদান দুইবার প্রথম উপাদান হিসেবে আসে না।", M)
def m_x_intercept():
    a = R.choice([1, 2, 3, 4, 5]); x0 = R.randint(-4, 5); b = -a * x0
    b2.add(f"y = {poly_str(a, b)} রেখাটি x-অক্ষকে কোন বিন্দুতে ছেদ করে?", f"({x0}, 0)", [f"(0, {x0})", f"({-x0}, 0)" if x0 else "(1, 0)", f"(0, {b})"], f"y = 0 বসালে {a}x = {-b}, x = {x0}।", M)
def m_y_intercept():
    a = R.choice([2, 3, -2, 4]); b = R.randint(-6, 6)
    b2.add(f"y = {poly_str(a, b)} রেখাটি y-অক্ষকে কোন বিন্দুতে ছেদ করে?", f"(0, {b})", [f"({b}, 0)", f"(0, {a})", f"(0, {b + a})"], f"x = 0 বসালে y = {b}।", M)
fill(b2, M, 50, [m_quad_eval, m_solve_lin, m_rel_rule, m_inverse, m_frac_eval, m_sum_vals, m_relations_count, m_is_function, m_x_intercept, m_y_intercept])

# ---- কঠিন ----
def h_domain_sqrt():
    k = R.randint(-4, 6)
    b2.add(f"f(x) = √(x {'−' if k >= 0 else '+'} {abs(k)}) ফাংশনের ডোমেন কোনটি?", f"{{x ∈ R : x ≥ {k}}}", [f"{{x ∈ R : x > {k}}}", f"{{x ∈ R : x ≤ {k}}}", "R"], f"বর্গমূলের ভিতর অঋণাত্মক হতে হবে: x {'−' if k >= 0 else '+'} {abs(k)} ≥ 0 ⇒ x ≥ {k}।", H)
def h_domain_frac():
    k = R.randint(-5, 6)
    b2.add(f"f(x) = 1/(x {'−' if k >= 0 else '+'} {abs(k)}) ফাংশনের ডোমেন কোনটি?", f"R − {{{k}}}", ["R", f"R − {{{-k}}}" if k else "R − {1}", f"{{x : x > {k}}}"], f"x = {k} হলে হর শূন্য হয়, তাই ঐ মানটি বাদ।", H)
def h_recip():
    a = R.randint(2, 5)
    b2.add(f"f(x) = (x + {a})/(x − {a}) হলে f(1/x) + f(x) = কত? (x ≠ 0, ±1/{a}, ±{a})", "0" if False else "অন্য কিছু", ["", "", ""], "", H) if False else None
def h_find_k():
    b, c = R.randint(-5, 5), R.randint(-5, 5); x0 = R.randint(1, 4); val = R.randint(-6, 10)
    # f(x) = x² + bx + k, f(x0) = val ⇒ k = val − x0² − b x0
    k = val - x0 * x0 - b * x0
    b2.add(f"f(x) = {poly_str(1, b, 0)} + k এবং f({x0}) = {val} হলে k = কত?", k, near_int(k), f"{x0}² {'+' if b >= 0 else '−'} {abs(b)}×{x0} + k = {val} ⇒ k = {k}।", H)
def h_roots():
    r1, r2 = R.sample(range(-4, 6), 2)
    b_, c_ = -(r1 + r2), r1 * r2
    b2.add(f"f(x) = {poly_str(1, b_, c_)} হলে f(x) = 0 এর সমাধান সেট কোনটি?", S([r1, r2]), [S([-r1, -r2]), S([r1, -r2]) if -r2 != r2 else S([r1, r2 + 1]), S([r1 + r2, r1 * r2]) if {r1 + r2, r1 * r2} != {r1, r2} else S([0, 1, 2])],
           f"{poly_str(1, b_, c_)} = (x − ({r1}))(x − ({r2})) = 0।", H)
def h_square_rel():
    A = sorted(R.sample(range(-3, 5), 4))
    sq = {x * x for x in A}
    B = sorted(set(A) | sq)
    rel = [(x, x * x) for x in A if x * x in B]
    b2.add(f"A = {S(A)}, R = {{(x, y) : x ∈ A, y = x²}} হলে R-এর রেঞ্জ কত?", S([y for _, y in rel]), [S(A), S([x * x for x in A] + [1, 0]) if set([x * x for x in A] + [1, 0]) != set(y for _, y in rel) else S(A + [9]), S([abs(x) for x in A]) if set(abs(x) for x in A) != set(y for _, y in rel) else S([2 * x for x in A])],
           "প্রত্যেক x-এর বর্গ নিয়ে রেঞ্জ গঠিত।", H)
def h_comp_val():
    a, b = R.choice([2, 3]), R.randint(-3, 3); x = R.randint(-2, 3)
    f = lambda t: a * t + b
    v = f(f(x))
    b2.add(f"f(x) = {poly_str(a, b)} হলে f(f({x})) = কত?", v, near_int(v), f"f({x}) = {f(x)}; f({f(x)}) = {v}।", H)
def h_onto_value():
    a, b = R.choice([2, 3, 4]), R.randint(-5, 5); y = R.randint(-6, 10)
    x = F(y - b, a)
    b2.add(f"f(x) = {poly_str(a, b)} হলে কোন x-এর জন্য f(x) = {y} হবে?", fr(x), [fr(x + 1), fr(F(y + b, a)) if F(y + b, a) != x else fr(x + 2), fr(-x) if x != 0 else '1'], f"{a}x {'+' if b >= 0 else '−'} {abs(b)} = {y} ⇒ x = {fr(x)}।", H)
fill(b2, H, 20, [h_domain_sqrt, h_domain_frac, h_find_k, h_roots, h_square_rel, h_comp_val, h_onto_value])

def finalize(b):
    out = []
    for lv, n in ((E, 30), (M, 50), (H, 20)):
        out += [x for x in b.items if x['lv'] == lv][:n]
    assert len(out) == 100
    for x in out: assert len(set(x['o'])) == 4 and 0 <= x['a'] < 4 and all(o.strip() for o in x['o']), x
    return out

items = finalize(b1) + finalize(b2)
for i, x in enumerate(items): x['n'] = i + 1
root = pathlib.Path(__file__).resolve().parents[2]
(root / 'src/mcq/ch2.json').write_text(json.dumps(items, ensure_ascii=False, indent=1), encoding='utf-8')
print('ch2:', len(items), {lv: sum(1 for x in items if x['lv'] == lv) for lv in (E, M, H)})
