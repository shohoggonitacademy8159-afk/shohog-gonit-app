# সব বোর্ড-প্রশ্নের ফাইল (gen_bq_*.py) মিলিয়ে cqb_c10_<ch>.json লেখে, তারপর www/sq.js বানায়
# চালাও: python3 src/sq/bq_build.py   (নতুন বোর্ডের প্রশ্ন: gen_bq_<বোর্ড><সাল>.py বানিয়ে নিচের তালিকায় যোগ করো)
import json, os, sys, glob, importlib
here=os.path.dirname(os.path.abspath(__file__)); sys.path.insert(0,here)
PAPERS=['gen_bq_my25','gen_bq_dn25','gen_bq_sy25']
by={}
for mod in PAPERS:
    for ch,it in importlib.import_module(mod).ITEMS: by.setdefault(ch,[]).append(it)
for f in glob.glob(os.path.join(here,'cqb_c10_*.json')): os.remove(f)
for ch,items in by.items():
    ns=[x['n'] for x in items]; assert len(ns)==len(set(ns)),ch
    json.dump(items,open(os.path.join(here,f'cqb_c10_{ch}.json'),'w'),ensure_ascii=False,indent=1)
print('বোর্ড প্রশ্ন:',{ch:len(v) for ch,v in sorted(by.items())})
exec(open(os.path.join(here,'build_sq.py')).read())
