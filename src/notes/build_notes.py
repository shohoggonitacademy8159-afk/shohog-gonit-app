#!/usr/bin/env python3
"""src/notes/<course>_<index>.md → www/notes.js (window.SOHOG_NOTES)
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

notes = {}
for f in sorted(here.glob('*.md')):
    m = re.match(r'([a-z0-9]+)_(\d+)\.md$', f.name)
    if not m: continue
    src = f.read_text(encoding='utf-8')
    tm = re.match(r'#\s+(.+)\n', src)
    title = tm.group(1).strip() if tm else ''
    body = src[tm.end():] if tm else src
    h = markdown.markdown(body, extensions=['tables', 'fenced_code', 'sane_lists', 'nl2br'])
    h = math_blocks(h)
    h = h.replace('<table>', '<div class="bn-tw"><table>').replace('</table>', '</table></div>')
    notes[f'{m.group(1)}:{m.group(2)}'] = {'title': title, 'html': h}

out = root / 'www' / 'notes.js'
out.write_text('/* স্বয়ংক্রিয়ভাবে তৈরি: src/notes/build_notes.py — হাতে বদলাবে না */\nwindow.SOHOG_NOTES=' + json.dumps(notes, ensure_ascii=False) + ';\n', encoding='utf-8')
print('notes', {k: len(v['html']) for k, v in notes.items()})
