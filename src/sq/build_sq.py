# src/sq/<cid>_<ch>.json -> www/sq.js (অ্যাপের ভেতরের সংক্ষিপ্ত প্রশ্নব্যাংক)
import json, glob, os, re
here=os.path.dirname(os.path.abspath(__file__)); out={}
for f in sorted(glob.glob(os.path.join(here,'*_*.json'))):
    cid,ch=re.match(r'(\w+?)_(\d+)\.json',os.path.basename(f)).groups()
    out.setdefault(cid,{})[ch]=json.load(open(f))
open(os.path.join(here,'..','..','www','sq.js'),'w').write('window.SOHOG_SQ='+json.dumps(out,ensure_ascii=False,separators=(',',':'))+';\n')
print({k:{c:len(v) for c,v in d.items()} for k,d in out.items()})
