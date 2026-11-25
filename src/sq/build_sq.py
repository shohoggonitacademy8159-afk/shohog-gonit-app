# src/sq/<cid>_<ch>.json → সংক্ষিপ্ত, src/sq/cq_<cid>_<ch>.json → সৃজনশীল, cqb_<cid>_<ch>.json → বোর্ড সৃজনশীল (শেষে যোগ); www/sq.js লেখে (অ্যাপের ভেতরের প্রশ্নব্যাংক)
import json, glob, os, re
here=os.path.dirname(os.path.abspath(__file__)); SQ={}; CQ={}
for f in sorted(glob.glob(os.path.join(here,'*.json'))):
    m=re.match(r'(cqb_|cq_)?([a-z0-9]+?)_(\d+)\.json$',os.path.basename(f))
    if not m: continue
    d=(CQ if m.group(1) else SQ).setdefault(m.group(2),{})
    if m.group(1)=='cqb_': d[m.group(3)]=d.get(m.group(3),[])+json.load(open(f))   # বোর্ড প্রশ্ন: অধ্যায়ের সৃজনশীলের শেষে
    else: d[m.group(3)]=json.load(open(f))
js=lambda o: json.dumps(o,ensure_ascii=False,separators=(',',':'))
open(os.path.join(here,'..','..','www','sq.js'),'w').write('window.SOHOG_SQ='+js(SQ)+';\nwindow.SOHOG_CQ='+js(CQ)+';\n')
print('SQ',{k:sum(map(len,d.values())) for k,d in SQ.items()},'CQ',{k:{c:len(v) for c,v in d.items()} for k,d in CQ.items()})
