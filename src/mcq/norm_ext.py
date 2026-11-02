import json, glob, re, collections, math
R1 = re.compile(r'(?<![\w.\d/])1([xyt])(?![\w])')
R1b = re.compile(r'(?<![\w.\d/])1([xy][²³⁴⁵⁶])')
Z = re.compile(r'\s[+−]\s0(?![.\d/])(?=\)|$|\s*=|\s*হ|-এর|\s*\|)')
def fix(t):
    t = R1.sub(r'\1', t); t = R1b.sub(r'\1', t)
    t = t.replace('(1/1) ', '').replace('(-', '(−')
    t = Z.sub('', t)
    t = t.replace('+ −', '− ').replace('− −', '+ ')
    t = re.sub(r'(?<![\w)\]°])-(?=\d)', '−', t)
    t = re.sub(r'(?<![\w/^])(\d+)/(\d+)√(\d+)', r'\1√\3/\2', t)
    t = re.sub(r'(?<![\w/^(])(\d+)/(\d+)π', r'\1π/\2', t)
    def _np(m):
        k, d = int(m.group(1) or 1), int(m.group(2)); g = math.gcd(k, d); k, d = k // g, d // g
        return (f"{k if k > 1 else ''}nπ" + (f"/{d}" if d > 1 else ''))
    t = re.sub(r'(?<![\w(])(\d*)nπ/(\d+)', _np, t)
    t = t.replace('± −', '± ')
    t = re.sub(r'\s+', ' ', t).replace('  ', ' ')
    return t
if __name__ == "__main__":
    drop = collections.Counter(); changed = 0
    for f in glob.glob('ext/*.json'):
        if 'need' in f: continue
        items = json.load(open(f)); out = []
        for x in items:
            q2 = fix(x['q']); o2 = [fix(o) for o in x['o']]
            if q2 != x['q'] or o2 != x['o']: changed += 1
            if len(set(o2)) < 4: drop[(f, x.get('ex'), x['lv'])] += 1; continue
            x['q'], x['o'] = q2, o2; out.append(x)
        json.dump(out, open(f, 'w'), ensure_ascii=False, indent=1)
    print('changed', changed, 'dropped', sum(drop.values())); print(dict(drop))
