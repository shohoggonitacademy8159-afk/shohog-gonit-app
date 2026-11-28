# এসএসসি সিলেবাসে নেই এমন প্রশ্ন লুকানোর নিয়ম (মুছে ফেলা নয়: MCQ তে del=1, সংক্ষিপ্ত sq.js থেকে বাদ) — দেখো SYLLABUS.md
import re
RULES = {
    ('c10h', '11'): re.compile(
        r'অন্তর্বিভক্ত|বহির্বিভক্ত|কী অনুপাতে|অনুপাতে বিভক্ত|'
        r'রেখার সমান্তরাল|সমান্তরাল রেখাদ্বয়|সমান্তরাল হলে|সমান্তরাল কি না|দুটি রেখা সমান্তরাল|'
        r'উপর লম্ব|লম্ব রেখা|লম্ব হলে|পরস্পর লম্ব|লম্ব কি না|লম্ব দূরত্ব|লম্বদ্বিখণ্ডক|'
        r'রেখাদ্বয় কেমন|রেখাদ্বয়ের মধ্যবর্তী দূরত্ব|∥|⊥'),
}
# ঢালের সমান্তরাল/লম্ব শর্ত দিয়ে প্রমাণ — নিয়মে ধরা পড়ে না, তাই নম্বর দিয়ে (সংক্ষিপ্ত)
EXTRA_SQ = {('c10h', '11'): {'b73', 'b83'}}
def hidden(cid, ch, q, n=None):
    r = RULES.get((cid, str(ch)))
    return bool(r and r.search(q)) or (n is not None and str(n) in EXTRA_SQ.get((cid, str(ch)), set()))
def hide_mcq(bank):
    k = 0
    for (cid, ch) in RULES:
        for x in bank.get(cid, {}).get(ch, []):
            if not x.get('del') and hidden(cid, ch, x['q']): x['del'] = 1; k += 1
    return k
