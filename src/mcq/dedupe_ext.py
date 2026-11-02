import json,glob,re,collections,sys
sys.path.insert(0,'.')
from norm_ext import fix
def cc(lbl):
    m=re.match(r'S\d*_(\w+?)_(\d+)$',lbl)
    if m: return m.group(1),m.group(2)
    if lbl=='8x': return 'c10','8'
    if lbl[0] in 'hij': return {'h':'c10h','i':'h11','j':'h12'}[lbl[0]],lbl[1:]
    return 'c10',lbl
b=json.load(open('mcq.json'))
old=set()
for c in b:
    for v in b[c].values():
        for x in v: old.add((c,fix(x['q']),fix(x['o'][x['a']])))
seen=set(); need=collections.defaultdict(dict); cnt=0
for f in sorted(glob.glob('ext/*.json')):
    lbl=f.split('/')[-1][:-5]
    if lbl.startswith('need'): continue
    c,ch=cc(lbl); items=json.load(open(f)); out=[]
    for x in items:
        k=(c,x['q'],x['o'][x['a']])
        if k in seen or k in old:
            key=f"{c}|{ch}|{x.get('ex','-')}"; need[key][x['lv']]=need[key].get(x['lv'],0)+1; cnt+=1; continue
        seen.add(k); out.append(x)
    json.dump(out,open(f,'w'),ensure_ascii=False,indent=1)
print('removed',cnt,dict(need))
json.dump(need,open('ext/need.json','w'),ensure_ascii=False)
