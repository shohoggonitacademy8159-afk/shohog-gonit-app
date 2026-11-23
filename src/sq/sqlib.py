# সংক্ষিপ্ত প্রশ্নব্যাংকের সহায়ক: rec() আবৃত্ত দশমিক → Fraction, save() json লেখে
import json, os
from fractions import Fraction as F
LV={'ম':'মধ্যম','ক':'কঠিন','স':'সহজ'}
def rec(whole, nonrep, rep):
    """whole.nonrep(rep আবৃত্ত) → Fraction, যেমন rec(1,'2','345') = 1.2345345…"""
    a=int(str(whole)+nonrep+rep); b=int(str(whole)+nonrep) if (nonrep or True) else 0
    return F(a-b, int('9'*len(rep)+'0'*len(nonrep)))
def build(groups, start=1):
    """groups: [(ex or None, [(q,a,lv),...]), ...] → items, n = b<start>…"""
    out=[]; k=start
    for ex,L in groups:
        seen=set()
        for q,a,lv in L:
            assert q not in seen, q; seen.add(q)
            it={'n':f'b{k}','q':q,'a':a,'lv':LV[lv]}
            if ex: it['ex']=ex
            out.append(it); k+=1
    return out
def save(cid,ch,items):
    p=os.path.join(os.path.dirname(os.path.abspath(__file__)),f'{cid}_{ch}.json')
    ns=[x['n'] for x in items]; assert len(ns)==len(set(ns))
    json.dump(items,open(p,'w'),ensure_ascii=False,indent=1); print(os.path.basename(p),len(items))
