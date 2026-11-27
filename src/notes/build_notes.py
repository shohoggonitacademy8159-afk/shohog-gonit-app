#!/usr/bin/env python3
"""src/notes/<course>_<index>[_<ক্রম>].md → www/notes.js (একটি অধ্যায়ে একাধিক নোট) (window.SOHOG_NOTES)
অ্যাপের সাথে আসা স্থায়ী নোট: শিরোনাম (# …), টেবিল, তালিকা; [a b; c d] → ম্যাট্রিক্স, |a b; c d| → নির্ণায়ক
চালাও: python3 src/notes/build_notes.py
"""
import re, json, pathlib, html
import markdown

here = pathlib.Path(__file__).resolve().parent
root = here.parent.parent

def grid(body, cls):
    rows = [r.split() for r in body.split(';')]
    w = max(len(r) for r in rows)
    assert all(len(r) == w for r in rows), body
    cells = ''.join(f'<i>{c}</i>' for r in rows for c in r)
    return f'<span class="{cls}"><span class="mx-g" style="grid-template-columns:repeat({w},auto)">{cells}</span></span>'

def math_blocks(h):
    # নির্ণায়ক: |…; …|   (টেবিলের ঘরের ভেতরের লেখাতেও কাজ করে)
    h = re.sub(r'\|([^|<>\n;]+(?:;[^|<>\n;]+)+)\|', lambda m: grid(m.group(1), 'mx mx-d'), h)
    # ম্যাট্রিক্স: […; …]
    h = re.sub(r'\[([^\[\]<>\n;]+(?:;[^\[\]<>\n;]+)+)\]', lambda m: grid(m.group(1), 'mx mx-m'), h)
    return h


# ---------- ভগ্নাংশ (উপর-নিচে) ও মূল চিহ্ন (পুরো রাশির উপর দাগ) ----------
TOK = re.compile(r'[0-9A-Za-zα-ωθπ′°₀-₉ₐ-ₜᵢⱼᵧᵦ⁰-⁹ⁿ¹²³⁺⁻ᵀᵏ·-]')
OPEN = {'(': ')', '[': ']'}; CLOSE = {')': '(', ']': '['}
def _match_f(s, k):
    o, c, d = s[k], OPEN[s[k]], 0
    for z in range(k, len(s)):
        if s[z] == o: d += 1
        elif s[z] == c:
            d -= 1
            if d == 0: return z
    return -1
def _match_b(s, j):
    c, o, d = s[j], CLOSE[s[j]], 0
    for z in range(j, -1, -1):
        if s[z] == c: d += 1
        elif s[z] == o:
            d -= 1
            if d == 0: return z
    return -1

class Math:
    def __init__(self): self.ph = []
    def put(self, html):
        self.ph.append(html); return chr(0xe000 + len(self.ph) - 1)
    def out(self, s):
        for _ in range(20):
            n = re.sub(r'[-]', lambda m: self.ph[ord(m.group(0)) - 0xe000], s)
            if n == s: break
            s = n
        return s
    def roots(self, s):
        i = 0
        while (i := s.find('√', i)) != -1:
            k = i + 1
            if k < len(s) and s[k] in OPEN:
                e = _match_f(s, k)
                if e < 0: i += 1; continue
                inner = self.fmt(s[k+1:e]); end = e + 1
            else:
                e = k
                while e < len(s) and TOK.match(s[e]): e += 1
                if e == k: i += 1; continue
                inner = self.fmt(s[k:e]); end = e
            s = s[:i] + self.put(f'<span class="rt">√<span class="rt-in">{inner}</span></span>') + s[end:]
            i += 1
        return s
    def fracs(self, s):
        i = 0
        while (i := s.find('/', i)) != -1:
            j = i - 1
            while j >= 0 and s[j] == ' ': j -= 1
            L = None
            if j >= 0 and s[j] in CLOSE:
                k = _match_b(s, j)
                if k >= 0:
                    a = k
                    while a > 0 and TOK.match(s[a-1]): a -= 1
                    L, num = a, (s[k+1:j] if a == k else s[a:j+1])
            elif j >= 0 and s[j] == '|':
                k = s.rfind('|', 0, j)
                if k >= 0 and j - k >= 2: L, num = k, s[k:j+1]
            else:
                a = j
                while a >= 0 and TOK.match(s[a]): a -= 1
                if a < j: L, num = a + 1, s[a+1:j+1]
            k = i + 1
            while k < len(s) and s[k] == ' ': k += 1
            R = None; sg = ''
            if k < len(s) and s[k] in '−-': sg = s[k]; k += 1
            if k < len(s) and s[k] in OPEN:
                e = _match_f(s, k)
                if e >= 0: R, den = e + 1, (sg + s[k:e+1] if sg else s[k+1:e])
            elif k < len(s) and s[k] == '|':
                e = s.find('|', k + 1)
                if e > k + 1: R, den = e + 1, sg + s[k:e+1]
            else:
                e = k
                while e < len(s) and TOK.match(s[e]): e += 1
                if e > k: R, den = e, sg + s[k:e]
            if L is None or R is None: i += 1; continue
            h = f'<span class="frc"><span>{self.fmt(num)}</span><span>{self.fmt(den)}</span></span>'
            s = s[:L] + self.put(h) + s[R:]
            i = L + 1
        return s
    def fmt(self, s): return self.fracs(self.roots(s))

def frac_root(h):
    M = Math()
    h = re.sub(r'<(sub|sup)>(.*?)</\1>', lambda m: M.put(m.group(0)), h)       # নিচের/উপরের লেখা একটি অক্ষর হিসেবে
    parts = re.split(r'(<[^>]+>)', h)
    for n, p in enumerate(parts):
        if p and not p.startswith('<'): parts[n] = M.fmt(p)
    return M.out(''.join(parts))

notes = {}
for f in sorted(here.glob('*.md'), key=lambda f: [int(x) if x.isdigit() else x for x in re.split(r'[_.]', f.name)]):
    m = re.match(r'([a-z0-9]+)_(\d+)(?:_(\d+))?\.md$', f.name)
    if not m: continue
    src = f.read_text(encoding='utf-8')
    tm = re.match(r'#\s+(.+)\n', src)
    title = tm.group(1).strip() if tm else ''
    body = src[tm.end():] if tm else src
    h = markdown.markdown(body, extensions=['tables', 'fenced_code', 'sane_lists', 'nl2br'])
    h = math_blocks(h)
    h = frac_root(h)
    h = h.replace('<table>', '<div class="bn-tw"><table>').replace('</table>', '</table></div>')
    notes.setdefault(f'{m.group(1)}:{m.group(2)}', []).append({'title': title, 'html': h})

out = root / 'www' / 'notes.js'
out.write_text('/* স্বয়ংক্রিয়ভাবে তৈরি: src/notes/build_notes.py — হাতে বদলাবে না */\nwindow.SOHOG_NOTES=' + json.dumps(notes, ensure_ascii=False) + ';\n', encoding='utf-8')
print('notes', {k: [n['title'][:20] for n in v] for k, v in notes.items()})
