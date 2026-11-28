import base64
FONTS=open('/tmp/reel/fonts.css').read()
LOGO='data:image/png;base64,'+base64.b64encode(open('logo.png','rb').read()).decode()
def f(n,d): return f'<span class="fr"><span>{n}</span><span>{d}</span></span>'
ix=f('1','x'); ix2=f('1','x²'); ix3=f('1','x³'); ix4=f('1','x⁴')
def box(title,body,cls='g'): return f'<div class="box {cls}"><div class="bt">{title}</div>{body}</div>'
def formula(n,eq,when,ex): return f'<div class="fm"><div class="fn">{n}</div><div class="fb"><div class="eq">{eq}</div><div class="fw"><b>কখন:</b> {when}</div><div class="fx"><b>উদাহরণ:</b> {ex}</div></div></div>'
def solved(no,lv,q,given,find,rule,steps,ans):
    st=''.join(f'<li>{s}</li>' for s in steps)
    return f'''<div class="sv"><div class="svh"><span class="sn">উদাহরণ {no}</span><span class="lv {lv[0]}">{lv[1]}</span></div>
<div class="q">{q}</div>
<table class="gf"><tr><td>দেওয়া আছে</td><td>{given}</td></tr><tr><td>নির্ণয় করতে হবে</td><td>{find}</td></tr><tr><td>ব্যবহৃত সূত্র</td><td>{rule}</td></tr></table>
<ol class="steps">{st}</ol><div class="ans">উত্তর: {ans}</div></div>'''
E=('e','সহজ'); M=('m','মাঝারি'); H=('h','কঠিন')
CSS='''
@page{size:A4;margin:14mm 13mm 16mm 13mm}
*{box-sizing:border-box}
body{font-family:'Hind Siliguri',sans-serif;color:#1f2a1f;font-size:11.6pt;line-height:1.62;margin:0}
h2{break-after:avoid;page-break-after:avoid;font-family:'Baloo Da 2','Hind Siliguri';font-weight:800;color:#1e6b3a;font-size:17pt;margin:0 0 8px;padding:6px 12px;border-left:6px solid #e8a317;background:linear-gradient(90deg,#fff7e0,#fff 70%);border-radius:0 10px 10px 0}
h3{break-after:avoid;color:#c0570a;font-size:13pt;margin:12px 0 4px}
.page{page-break-after:always}
.sec{margin-bottom:14px}
p{margin:4px 0}
.fr{display:inline-flex;flex-direction:column;vertical-align:middle;text-align:center;line-height:1.05;font-size:.9em;margin:0 1px}
.fr>span:first-child{border-bottom:1.2px solid currentColor;padding:0 2px}
.fr>span:last-child{padding:0 2px}
.box{border-radius:12px;padding:10px 14px;margin:8px 0;break-inside:avoid}
.box .bt{font-weight:700;margin-bottom:4px}
.box.g{background:#eef8f0;border:1.5px solid #8cc9a0}.box.g .bt{color:#1e6b3a}
.box.o{background:#fff3e6;border:1.5px solid #f2b179}.box.o .bt{color:#c0570a}
.box.y{background:#fffaeb;border:1.5px solid #ecc85a}.box.y .bt{color:#9a6b00}
.box.r{background:#fff1f0;border:1.5px solid #f0a8a0}.box.r .bt{color:#b42318}
ul,ol{margin:4px 0;padding-left:22px}
li{margin:2px 0}
.fm{display:flex;gap:10px;border:1.5px solid #ecc85a;background:#fffdf5;border-radius:12px;padding:8px 12px;margin:7px 0;break-inside:avoid}
.fn{flex:0 0 30px;height:30px;border-radius:50%;background:#e8a317;color:#fff;font-weight:700;display:grid;place-items:center}
.fb{flex:1}.eq{font-size:13pt;font-weight:600;color:#1e6b3a}
.fw,.fx{font-size:10.6pt}
.sv{border:1.5px solid #cfe5d5;border-radius:12px;padding:10px 14px;margin:9px 0;break-inside:avoid;background:#fff}
.svh{display:flex;justify-content:space-between;align-items:center;margin-bottom:4px}
.sn{font-weight:700;color:#1e6b3a}
.lv{font-size:9.5pt;font-weight:700;padding:1px 10px;border-radius:999px}
.lv.e{background:#e3f5e8;color:#1e6b3a}.lv.m{background:#fff1d6;color:#9a6b00}.lv.h{background:#ffe4d1;color:#c0570a}
.q{font-weight:600;margin-bottom:5px}
table.gf{border-collapse:collapse;width:100%;font-size:10.6pt;margin-bottom:4px}
table.gf td{border:1px solid #e3eee6;padding:3px 8px;vertical-align:middle}
table.gf td:first-child{width:28%;background:#f4faf5;color:#1e6b3a;font-weight:600}
.steps{margin:4px 0 2px}
.ans{display:inline-block;background:#1e6b3a;color:#fff;border-radius:8px;padding:2px 12px;font-weight:600;margin-top:3px}
.two{columns:2;column-gap:22px}
.two li{break-inside:avoid}
.mcq{break-inside:avoid;margin:6px 0}
.mcq .op{display:grid;grid-template-columns:1fr 1fr;gap:0 16px;padding-left:22px;font-size:10.8pt}
.key{display:grid;grid-template-columns:repeat(5,1fr);gap:4px;text-align:center}
.key div{border:1px solid #ecc85a;border-radius:8px;padding:2px;background:#fffaeb}
table.mk{border-collapse:collapse;width:100%;font-size:10.8pt}
table.mk td,table.mk th{border:1px solid #d9e7dc;padding:4px 8px}
table.mk th{background:#eef8f0;color:#1e6b3a}
.cover{height:265mm;display:flex;flex-direction:column;align-items:center;justify-content:center;text-align:center;background:radial-gradient(circle at 50% 30%,#fff8e3,#fff 60%);border:3px solid #e8a317;border-radius:22px;position:relative}
.cover img{width:150px;height:150px;border-radius:30px;box-shadow:0 8px 24px rgba(160,110,0,.25)}
.brand{font-family:'Baloo Da 2';font-weight:800;font-size:40pt;color:#1e6b3a;margin-top:14px;line-height:1.1}
.brand b{color:#e3261b}
.tag{font-size:15pt;font-weight:600;color:#9a6b00;background:#fff1c2;border-radius:999px;padding:3px 22px;margin-top:6px}
.cv1{margin-top:34px;font-size:20pt;font-weight:700;color:#c0570a}
.cv2{font-family:'Baloo Da 2';font-size:28pt;font-weight:800;color:#1e6b3a;line-height:1.2}
.cv3{font-size:13pt;color:#555;margin-top:4px}
.cvbar{display:flex;gap:10px;margin-top:30px}
.cvbar span{border:1.5px solid #8cc9a0;background:#eef8f0;color:#1e6b3a;border-radius:10px;padding:4px 12px;font-size:10.5pt;font-weight:600}
.cvf{position:absolute;bottom:16px;font-size:10pt;color:#888}
.ov{display:grid;grid-template-columns:1fr 1fr;gap:10px}
.star{color:#e8a317}
.last h2{background:linear-gradient(90deg,#ffe9c7,#fff 70%)}
.cram{display:grid;grid-template-columns:1fr 1fr;gap:8px;font-size:10.6pt}
.cram .box{margin:0;padding:7px 11px}
'''
H_=[]
add=H_.append
# ---------- প্রচ্ছদ
add(f'''<div class="page"><div class="cover"><img src="{LOGO}"><div class="brand">অংকবাড়ি<b>+</b></div><div class="tag">গণিত শেখার নতুন ঠিকানা</div>
<div class="cv1">SSC সাধারণ গণিত</div><div class="cv2">অধ্যায় ৩: বীজগাণিতিক রাশি</div><div class="cv3">অনুশীলনী ৩.১ · বর্গ ও ঘনের সূত্র এবং প্রয়োগ</div>
<div class="cvbar"><span>সূত্র ও প্রয়োগ</span><span>ধাপে ধাপে সমাধান</span><span>MCQ ও Self Test</span><span>শেষ মুহূর্তের রিভিশন</span></div>
<div class="cvf">Lecture Sheet · অংকবাড়ি+</div></div></div>''')
# ---------- ১ পরিচিতি + ২ পূর্বজ্ঞান
add(f'''<div class="sec"><h2>১. অধ্যায়ের পরিচিতি</h2>
<p><b>অধ্যায়:</b> বীজগাণিতিক রাশি (অনুশীলনী ৩.১ — বীজগাণিতিক সূত্র ও এদের প্রয়োগ)</p>
<div class="ov">{box('কেন গুরুত্বপূর্ণ','<ul><li>উচ্চতর গণিতসহ পরের প্রায় সব অধ্যায়ে এই সূত্রগুলো লাগে।</li><li>বড় হিসাব (যেমন 105², 998²) মুখে মুখে করা যায়।</li><li>SSC তে MCQ ও সৃজনশীল—দুই অংশেই নিয়মিত প্রশ্ন আসে।</li></ul>','y')}
{box('এই অধ্যায় শেষে তুমি পারবে','<ul><li>বর্গ ও ঘনের সূত্রগুলো লিখতে ও প্রমাণ বুঝতে</li><li>সূত্র দিয়ে রাশির বিস্তৃতি ও সরলীকরণ করতে</li><li>a + b, ab দেওয়া থাকলে অন্য রাশির মান বের করতে</li><li>x + '+ix+' ধরনের রাশির মান নির্ণয় করতে</li></ul>','g')}</div></div>
<div class="sec"><h2>২. প্রয়োজনীয় পূর্বজ্ঞান</h2><ul class="two">
<li>চলক, সহগ, পদ ও বীজগাণিতিক রাশির ধারণা</li><li>সূচকের নিয়ম: a<sup>m</sup>·a<sup>n</sup> = a<sup>m+n</sup>, (ab)<sup>n</sup> = a<sup>n</sup>b<sup>n</sup></li>
<li>চিহ্নের নিয়ম: (−)×(−) = (+), (−)×(+) = (−)</li><li>বীজগাণিতিক রাশির যোগ, বিয়োগ ও গুণ</li>
<li>বর্গমূল ও সহজ করণী (√2, √3) এর গুণ</li><li>(√a + √b)(√a − √b) = a − b ধরনের গুণফল</li></ul></div>''')
# ---------- ৩ মূল ধারণা
add(f'''<div class="sec"><h2>৩. মূল ধারণা</h2>
<h3>৩.১ বীজগাণিতিক সূত্র কী?</h3>
<p>যে সমতা চলকের <b>সকল মানের জন্য</b> সত্য, তাকে <b>অভেদ</b> বা <b>বীজগাণিতিক সূত্র</b> বলে। যেমন (a + b)² = a² + 2ab + b² — a, b এর যেকোনো মান বসালে দুই পক্ষ সমান হয়।</p>
{box('যাচাই করে দেখো','a = 3, b = 2 হলে বামপক্ষ (3 + 2)² = 25 এবং ডানপক্ষ 9 + 12 + 4 = 25 ✔','g')}
<h3>৩.২ বর্গ মানে নিজের সাথে গুণ</h3>
<p>(a + b)² = (a + b)(a + b) = a² + ab + ab + b² = a² + 2ab + b²। তাই <b>মাঝের পদ 2ab কখনো বাদ যায় না।</b></p>
<h3>৩.৩ ঘন মানে তিনবার গুণ</h3>
<p>(a + b)³ = (a + b)²(a + b) = (a² + 2ab + b²)(a + b) = a³ + 3a²b + 3ab² + b³ = a³ + b³ + 3ab(a + b)।</p>
<h3>৩.৪ সূত্রে a, b যেকোনো রাশি হতে পারে</h3>
<p>সূত্রের a, b এর জায়গায় 2x, 3y, √3, {ix} — যেকোনো কিছু বসানো যায়। যেমন (2x + 3y)² এ a = 2x, b = 3y ধরলে = (2x)² + 2(2x)(3y) + (3y)² = 4x² + 12xy + 9y²।</p>
<h3>৩.৫ "মান নির্ণয়" অংকের মূল কৌশল</h3>
<p>যা দেওয়া আছে (যেমন a + b ও ab) আর যা চাওয়া হয়েছে (যেমন a² + b²) — দুটিকে জোড়া দেয় এমন সূত্র বেছে নাও। দেওয়া মানগুলো সরাসরি বসাও; a ও b আলাদা করে বের করার দরকার নেই।</p>
<h3>৩.৬ x ও {ix} এর জোড়</h3>
<p>x · {ix} = 1, তাই a = x, b = {ix} ধরলে ab = 1 হয়ে সূত্রগুলো খুব সহজ হয়ে যায়: x² + {ix2} = (x + {ix})² − 2।</p></div>''')
# ---------- ৪ সূত্র
fs=[
('(a + b)² = a² + 2ab + b²','দুইটি পদের যোগফলের বর্গ বিস্তৃত করতে বা বড় সংখ্যার বর্গ করতে','(x + 4)² = x² + 8x + 16 ; 103² = (100 + 3)² = 10609'),
('(a − b)² = a² − 2ab + b²','দুইটি পদের অন্তরের বর্গ','(3x − 1)² = 9x² − 6x + 1 ; 99² = (100 − 1)² = 9801'),
('a² + b² = (a + b)² − 2ab = (a − b)² + 2ab','a + b (বা a − b) ও ab জানা থাকলে a² + b² বের করতে','a + b = 5, ab = 6 ⇒ a² + b² = 25 − 12 = 13'),
('(a + b)² = (a − b)² + 4ab ; (a − b)² = (a + b)² − 4ab','a + b থেকে a − b বা উল্টোটা বের করতে','a + b = 7, ab = 10 ⇒ (a − b)² = 49 − 40 = 9 ⇒ a − b = ±3'),
('(a + b)² + (a − b)² = 2(a² + b²) ; (a + b)² − (a − b)² = 4ab','দুটি বর্গের যোগ/বিয়োগ সরল করতে','(x + 2)² − (x − 2)² = 4·x·2 = 8x'),
(f'ab = ({f("a + b","2")})² − ({f("a − b","2")})²','গুণফলকে দুটি বর্গের অন্তররূপে লিখতে','12 = ((6 + 2)/2)² − ((6 − 2)/2)² = 16 − 4'),
('a² − b² = (a + b)(a − b)','বর্গের অন্তর বা (a + b)(a − b) গুণ করতে','(2x + 5)(2x − 5) = 4x² − 25 ; 52 × 48 = 2500 − 4 = 2496'),
('(x + a)(x + b) = x² + (a + b)x + ab','একই প্রথম পদবিশিষ্ট দুটি দ্বিপদীর গুণ','(x + 5)(x − 3) = x² + 2x − 15'),
('(a + b + c)² = a² + b² + c² + 2ab + 2bc + 2ca','তিন পদের বর্গ; অথবা a + b + c ও ab + bc + ca দিয়ে a² + b² + c²','a + b + c = 6, ab + bc + ca = 11 ⇒ a² + b² + c² = 36 − 22 = 14'),
('(a + b)³ = a³ + 3a²b + 3ab² + b³ = a³ + b³ + 3ab(a + b)','যোগফলের ঘন','(x + 2)³ = x³ + 6x² + 12x + 8'),
('(a − b)³ = a³ − 3a²b + 3ab² − b³ = a³ − b³ − 3ab(a − b)','অন্তরের ঘন','(x − 1)³ = x³ − 3x² + 3x − 1'),
('a³ + b³ = (a + b)(a² − ab + b²) = (a + b)³ − 3ab(a + b)','a + b ও ab জানা থাকলে a³ + b³','a + b = 4, ab = 3 ⇒ a³ + b³ = 64 − 36 = 28'),
('a³ − b³ = (a − b)(a² + ab + b²) = (a − b)³ + 3ab(a − b)','a − b ও ab জানা থাকলে a³ − b³','a − b = 2, ab = 3 ⇒ a³ − b³ = 8 + 18 = 26'),
(f'x² + {ix2} = (x + {ix})² − 2 = (x − {ix})² + 2','x + '+ix+' বা x − '+ix+' জানা থাকলে','x + '+ix+' = 3 ⇒ x² + '+ix2+' = 9 − 2 = 7'),
(f'x³ + {ix3} = (x + {ix})³ − 3(x + {ix}) ; x³ − {ix3} = (x − {ix})³ + 3(x − {ix})','x ও '+ix+' এর ঘনের যোগ/বিয়োগ','x + '+ix+' = 3 ⇒ x³ + '+ix3+' = 27 − 9 = 18'),
]
add('<div class="sec"><h2>৪. গুরুত্বপূর্ণ সূত্র</h2>'+''.join(formula(i+1,*t) for i,t in enumerate(fs))+'</div>')
# ---------- ৫ ও ৬ সমাধান (সহজ → মাঝারি → কঠিন)
S=[
(E,'(3x + 5y)² এর বিস্তৃতি নির্ণয় কর।','রাশি (3x + 5y)²','বিস্তৃতি','(a + b)² = a² + 2ab + b², যেখানে a = 3x, b = 5y',['(3x + 5y)² = (3x)² + 2·(3x)·(5y) + (5y)²','= 9x² + 30xy + 25y²'],'9x² + 30xy + 25y²'),
(E,'সূত্রের সাহায্যে 105² এর মান নির্ণয় কর।','সংখ্যা 105','105²','(a + b)², 105 = 100 + 5',['105² = (100 + 5)²','= 100² + 2·100·5 + 5² = 10000 + 1000 + 25','= 11025'],'11025'),
(E,'(2a − 3b)² এর বিস্তৃতি নির্ণয় কর।','রাশি (2a − 3b)²','বিস্তৃতি','(a − b)² = a² − 2ab + b²',['(2a − 3b)² = (2a)² − 2·(2a)·(3b) + (3b)²','= 4a² − 12ab + 9b²'],'4a² − 12ab + 9b²'),
(M,'a + b = 7 এবং ab = 12 হলে a² + b² ও a − b এর মান নির্ণয় কর।','a + b = 7, ab = 12','a² + b² ও a − b','a² + b² = (a + b)² − 2ab ; (a − b)² = (a + b)² − 4ab',['a² + b² = 7² − 2·12 = 49 − 24 = 25','(a − b)² = 7² − 4·12 = 49 − 48 = 1','∴ a − b = ±√1 = ±1 (বর্গমূলে ± চিহ্ন ভুলবে না)'],'a² + b² = 25 ; a − b = ±1'),
(M,f'x − {ix} = 3 হলে x² + {ix2} এবং x⁴ + {ix4} এর মান নির্ণয় কর।',f'x − {ix} = 3',f'x² + {ix2}, x⁴ + {ix4}',f'x² + {ix2} = (x − {ix})² + 2',[f'x² + {ix2} = 3² + 2 = 11',f'x⁴ + {ix4} = (x² + {ix2})² − 2 (একই সূত্র, x² কে চলক ধরে)','= 11² − 2 = 121 − 2 = 119'],f'x² + {ix2} = 11 ; x⁴ + {ix4} = 119'),
(M,'a + b + c = 9 এবং ab + bc + ca = 26 হলে a² + b² + c² এর মান কত?','a + b + c = 9, ab + bc + ca = 26','a² + b² + c²','(a + b + c)² = a² + b² + c² + 2(ab + bc + ca)',['81 = a² + b² + c² + 2·26','a² + b² + c² = 81 − 52 = 29'],'29'),
(M,'(2x + 3)³ এর বিস্তৃতি নির্ণয় কর।','রাশি (2x + 3)³','বিস্তৃতি','(a + b)³ = a³ + 3a²b + 3ab² + b³',['= (2x)³ + 3·(2x)²·3 + 3·(2x)·3² + 3³','= 8x³ + 36x² + 54x + 27'],'8x³ + 36x² + 54x + 27'),
(M,f'x + {ix} = 4 হলে x³ + {ix3} এর মান নির্ণয় কর।',f'x + {ix} = 4',f'x³ + {ix3}',f'x³ + {ix3} = (x + {ix})³ − 3(x + {ix})',['= 4³ − 3·4','= 64 − 12 = 52'],'52'),
(M,'a − b = 5 এবং ab = 36 হলে a³ − b³ এর মান নির্ণয় কর।','a − b = 5, ab = 36','a³ − b³','a³ − b³ = (a − b)³ + 3ab(a − b)',['= 5³ + 3·36·5','= 125 + 540 = 665'],'665'),
(M,'সরল কর: (5x − 4)² + (4 − 3x)² + 2(5x − 4)(4 − 3x)','রাশিটি A² + B² + 2AB আকারের','সরল মান','A² + 2AB + B² = (A + B)², যেখানে A = 5x − 4, B = 4 − 3x',['রাশি = (A + B)²','A + B = 5x − 4 + 4 − 3x = 2x','∴ রাশি = (2x)² = 4x²'],'4x²'),
(H,f'a = √3 + √2 হলে a³ + {f("1","a³")} এর মান নির্ণয় কর।','a = √3 + √2',f'a³ + {f("1","a³")}',f'a³ + {f("1","a³")} = (a + {f("1","a")})³ − 3(a + {f("1","a")})',[f'{f("1","a")} = {f("1","√3 + √2")} = {f("√3 − √2","(√3 + √2)(√3 − √2)")} = {f("√3 − √2","3 − 2")} = √3 − √2',f'a + {f("1","a")} = (√3 + √2) + (√3 − √2) = 2√3',f'a³ + {f("1","a³")} = (2√3)³ − 3·2√3 = 24√3 − 6√3','= 18√3'],'18√3'),
(H,'a + b + c = 0 হলে দেখাও যে, a³ + b³ + c³ = 3abc','a + b + c = 0','a³ + b³ + c³ = 3abc প্রমাণ','(a + b)³ = a³ + b³ + 3ab(a + b)',['a + b = −c','উভয় পক্ষকে ঘন করে: (a + b)³ = −c³','a³ + b³ + 3ab(a + b) = −c³','a³ + b³ + 3ab(−c) = −c³ [a + b = −c বসিয়ে]','∴ a³ + b³ + c³ = 3abc (প্রমাণিত)'],'প্রমাণিত'),
(H,f'x = 2 + √3 হলে x² + {ix2} এবং x³ + {ix3} এর মান নির্ণয় কর।','x = 2 + √3',f'x² + {ix2}, x³ + {ix3}','x + 1/x এর সূত্র',[f'{ix} = {f("1","2 + √3")} = {f("2 − √3","4 − 3")} = 2 − √3',f'x + {ix} = 2 + √3 + 2 − √3 = 4',f'x² + {ix2} = 4² − 2 = 14',f'x³ + {ix3} = 4³ − 3·4 = 52'],f'x² + {ix2} = 14 ; x³ + {ix3} = 52'),
]
add('<div class="sec"><h2>৫–৬. ধাপে ধাপে সমাধান ও গুরুত্বপূর্ণ উদাহরণ</h2><p>উদাহরণগুলো <b>সহজ → মাঝারি → কঠিন</b> ক্রমে সাজানো। প্রতিটিতে একই ছকে ভাবো: কী দেওয়া আছে → কী চাই → কোন সূত্র জোড়া দেয় → বসাও।</p>'+''.join(solved(i+1,*t) for i,t in enumerate(S))+'</div>')
# ---------- ৭ পরীক্ষায় গুরুত্বপূর্ণ
add(f'''<div class="sec"><h2>৭. পরীক্ষায় বেশি গুরুত্বপূর্ণ বিষয়</h2><div class="ov">
{box('<span class="star">⭐</span> গুরুত্বপূর্ণ সূত্র',f'<ul><li>a² + b² = (a + b)² − 2ab</li><li>(a − b)² = (a + b)² − 4ab</li><li>a³ ± b³ = (a ± b)³ ∓ 3ab(a ± b)</li><li>x² + {ix2} = (x ± {ix})² ∓ 2</li><li>x³ + {ix3} = (x + {ix})³ − 3(x + {ix})</li></ul>','y')}
{box('<span class="star">⭐</span> গুরুত্বপূর্ণ অংকের ধরন','<ul><li>সূত্র দিয়ে বিস্তৃতি (বর্গ ও ঘন)</li><li>a + b, ab দিয়ে অন্য রাশির মান</li><li>x = √3 + √2 ধরনের করণী দিয়ে মান</li><li>A² ± 2AB + B² আকারে সরলীকরণ</li><li>a + b + c = 0 সংক্রান্ত প্রমাণ</li></ul>','g')}
{box('<span class="star">⭐</span> সম্ভাব্য প্রশ্নের ধরন','<ul><li><b>MCQ:</b> সরাসরি মান, সহগ, i/ii/iii ধরনের</li><li><b>সৃজনশীল ক:</b> একটি সূত্র প্রয়োগ (২ নম্বর)</li><li><b>খ/গ:</b> করণীসহ মান নির্ণয়, প্রমাণ, x⁴ + 1/x⁴ বা ঘনের মান (৪ নম্বর)</li></ul>','o')}
{box('<span class="star">⭐</span> যেখানে বেশি ভুল হয়','<ul><li>মাঝের পদ 2ab বা 3ab(a + b) বাদ পড়া</li><li>বর্গমূলের সময় ± না লেখা</li><li>(2x)² কে 2x² লেখা</li><li>a³ − b³ এর উৎপাদকে চিহ্ন উল্টে ফেলা</li></ul>','r')}</div></div>''')
# ---------- ৮ সাধারণ ভুল
mist=[('(a + b)² = a² + b²','(a + b)² = a² + 2ab + b²','বর্গ মানে (a + b)(a + b); গুণ করলে 2ab আসবেই।'),
('(3x)² = 3x²','(3x)² = 9x²','বন্ধনীর ভেতরের সহগসহ পুরো পদটির বর্গ হয়।'),
('(a − b)² = 49 ⇒ a − b = 7','a − b = ±7','বর্গমূল নিলে দুটি মান; প্রশ্নে শর্ত (যেমন a > b) না থাকলে ± রাখো।'),
('(a + b)³ = a³ + b³','(a + b)³ = a³ + b³ + 3ab(a + b)','ঘনের বিস্তৃতিতে চারটি পদ থাকে।'),
('a³ − b³ = (a − b)(a² − ab + b²)','a³ − b³ = (a − b)(a² + ab + b²)','মনে রাখো: দ্বিতীয় বন্ধনীর মাঝের চিহ্ন প্রথম বন্ধনীর <b>বিপরীত</b>।'),
(f'x − {ix} = 3 ⇒ x² + {ix2} = 9 − 2',f'x² + {ix2} = 9 + 2 = 11',f'x − {ix} হলে <b>+2</b>, x + {ix} হলে <b>−2</b>।'),
('−(a − b)² = −a² − 2ab − b²','−(a − b)² = −a² + 2ab − b²','আগে বিস্তৃতি বন্ধনীতে রেখে তারপর বাইরের − চিহ্ন সব পদে দাও।')]
add('<div class="sec"><h2>৮. সাধারণ ভুল ও এড়ানোর উপায়</h2><table class="mk"><tr><th>ভুল লেখা ✘</th><th>সঠিক ✔</th><th>কীভাবে এড়াবে</th></tr>'+''.join(f'<tr><td style="color:#b42318">{a}</td><td style="color:#1e6b3a;font-weight:600">{b}</td><td>{c}</td></tr>' for a,b,c in mist)+'</table></div>')
# ---------- ৯ Quick Revision
add(f'''<div class="sec"><h2>৯. দ্রুত রিভিশন (Quick Revision)</h2><div class="cram">
{box('সংজ্ঞা','<b>অভেদ/সূত্র:</b> চলকের সকল মানের জন্য সত্য সমতা।<br><b>বর্গ:</b> রাশিকে নিজের সাথে একবার গুণ। <b>ঘন:</b> তিনবার গুণ।','g')}
{box('বর্গের সূত্র','(a ± b)² = a² ± 2ab + b²<br>a² + b² = (a ± b)² ∓ 2ab<br>(a ± b)² = (a ∓ b)² ± 4ab<br>a² − b² = (a + b)(a − b)','y')}
{box('ঘনের সূত্র','(a ± b)³ = a³ ± b³ ± 3ab(a ± b)<br>a³ ± b³ = (a ± b)(a² ∓ ab + b²)<br>a³ ± b³ = (a ± b)³ ∓ 3ab(a ± b)','o')}
{box('কৌশল',f'১. চাওয়া রাশি ও দেওয়া রাশি জোড়া দেয় এমন সূত্র খোঁজো।<br>২. x ও {ix} এ ab = 1।<br>৩. করণী থাকলে আগে {ix} এর হর মূলদ করো।<br>৪. A² ± 2AB + B² দেখলেই (A ± B)²।','g')}</div></div>''')
# ---------- ১০ অনুশীলনী
L1=['(2x + 5)²','(3a − 4b)²','সূত্রের সাহায্যে 98²','(x + 5)(x − 3)','(a + b − c)²','(x − 2y)³']
A1=['4x² + 20x + 25','9a² − 24ab + 16b²','9604','x² + 2x − 15','a² + b² + c² + 2ab − 2bc − 2ca','x³ − 6x²y + 12xy² − 8y³']
L2=['a + b = 5, ab = 6 হলে a² + b² ও a³ + b³ এর মান নির্ণয় কর।',f'x + {ix} = 3 হলে x² + {ix2} ও x³ + {ix3} এর মান নির্ণয় কর।','a − b = 3, ab = 10 হলে a² + b² ও a + b এর মান নির্ণয় কর।','a + b + c = 10 এবং a² + b² + c² = 38 হলে ab + bc + ca এর মান নির্ণয় কর।','সরল কর: (2a + 3b)² − (2a − 3b)²','সূত্রের সাহায্যে 997² এর মান নির্ণয় কর।']
A2=['13 ; 35',f'7 ; 18','29 ; ±7','31','24ab','994009']
L3=[f'x = √5 + 2 হলে x³ + {ix3} এর মান নির্ণয় কর।',f'x − {ix} = 4 হলে x³ − {ix3} এর মান নির্ণয় কর।',f'a + b + c = 0 হলে দেখাও যে, {f("a²","bc")} + {f("b²","ca")} + {f("c²","ab")} = 3',f'x² − 4x + 1 = 0 হলে x² + {ix2} ও x⁴ + {ix4} এর মান নির্ণয় কর। [সংকেত: x দিয়ে ভাগ কর]']
A3=['34√5','76','প্রমাণ: বামপক্ষ = (a³ + b³ + c³)/abc = 3abc/abc = 3','14 ; 194']
def lst(qs): return '<ol>'+''.join(f'<li>{q}</li>' for q in qs)+'</ol>'
def ans(a): return '<p style="font-size:10.4pt;color:#555"><b>উত্তর:</b> '+' ; '.join(f'({i+1}) {x}' for i,x in enumerate(a))+'</p>'
add('<div class="sec"><h2>১০. অনুশীলনী</h2>'+box('Level 1 — Basic: বিস্তৃতি নির্ণয় কর',lst(L1)+ans(A1),'g')+box('Level 2 — Standard (SSC উপযোগী)',lst(L2)+ans(A2),'y')+box('Level 3 — Challenge',lst(L3)+ans(A3),'o')+'</div>')
# ---------- ১১ MCQ
MQ=[('(a + b)² − (a − b)² = কত?',['2ab','4ab','2(a² + b²)','0'],1),('a + b = 5, ab = 4 হলে a² + b² = কত?',['17','21','25','9'],0),
(f'x + {ix} = 2 হলে x² + {ix2} = কত?',['2','4','0','6'],0),('(x − 2)³ এর বিস্তৃতিতে x এর সহগ কত?',['−12','12','6','−6'],1),('101² = কত?',['10201','10101','10001','10021'],0),
('a³ − b³ = কোনটি?',['(a − b)(a² + ab + b²)','(a − b)(a² − ab + b²)','(a + b)(a² − ab + b²)','(a − b)³'],0),('a + b + c = 0 হলে a³ + b³ + c³ = কত?',['0','abc','3abc','−3abc'],2),
('a − b = 4, ab = 5 হলে (a + b)² = কত?',['36','26','16','6'],0),(f'x − {ix} = 1 হলে x³ − {ix3} = কত?',['1','2','3','4'],3),
('a + b = 3, ab = 2 হলে—<br>i. a² + b² = 5 &nbsp; ii. (a − b)² = 1 &nbsp; iii. a³ + b³ = 9<br>নিচের কোনটি সঠিক?',['i ও ii','i ও iii','ii ও iii','i, ii ও iii'],3)]
L='কখগঘ'
add('<div class="sec"><h2>১১. MCQ Practice</h2>'+''.join(f'<div class="mcq"><b>{i+1}.</b> {q}<div class="op">'+''.join(f'<span>({L[j]}) {o}</span>' for j,o in enumerate(op))+'</div></div>' for i,(q,op,a) in enumerate(MQ))+
 box('Answer Key','<div class="key">'+''.join(f'<div>{i+1}. {L[a]}</div>' for i,(q,op,a) in enumerate(MQ))+'</div>','g')+'</div>')
# ---------- ১২ Self Test
add(f'''<div class="sec"><h2>১২. Self Test (সময়: ২০ মিনিট · পূর্ণমান: ১৫)</h2>{box('প্রশ্ন',f"""<ol><li>(4x − 3y)² এর বিস্তৃতি নির্ণয় কর। [২]</li><li>a + b = 6, ab = 8 হলে a² + b² এর মান কত? [২]</li><li>x − {ix} = 5 হলে x² + {ix2} এর মান নির্ণয় কর। [২]</li><li>a + b = 5, ab = 1 হলে a³ + b³ এর মান নির্ণয় কর। [৩]</li><li>সূত্রের সাহায্যে 1003² এর মান নির্ণয় কর। [২]</li><li>x = √3 + √2 হলে x² + {ix2} এর মান নির্ণয় কর। [৪]</li></ol>""",'y')}
<p style="font-size:10.4pt;color:#555"><b>উত্তর মিলিয়ে নাও:</b> (1) 16x² − 24xy + 9y² ; (2) 20 ; (3) 27 ; (4) 110 ; (5) 1006009 ; (6) x + {ix} = 2√3 ⇒ 12 − 2 = 10 &nbsp;|&nbsp; <b>১৩–১৫:</b> চমৎকার · <b>৯–১২:</b> ভুলগুলো আবার দেখো · <b>৮ বা কম:</b> সূত্র অংশ আবার পড়ো</p></div>''')
# ---------- শেষ পাতা
add(f'''<div class="page" style="page-break-before:always"></div><div class="sec last"><h2>পরীক্ষার আগে শেষবার যা পড়বে</h2><div class="cram">
{box('১. বর্গ','(a + b)² = a² + 2ab + b²<br>(a − b)² = a² − 2ab + b²<br>a² − b² = (a + b)(a − b)<br>(a + b + c)² = a² + b² + c² + 2(ab + bc + ca)','y')}
{box('২. ঘন','(a + b)³ = a³ + b³ + 3ab(a + b)<br>(a − b)³ = a³ − b³ − 3ab(a − b)<br>a³ + b³ = (a + b)(a² − ab + b²)<br>a³ − b³ = (a − b)(a² + ab + b²)','o')}
{box('৩. মান নির্ণয়ের সূত্র','a² + b² = (a + b)² − 2ab = (a − b)² + 2ab<br>(a − b)² = (a + b)² − 4ab<br>a³ + b³ = (a + b)³ − 3ab(a + b)<br>a³ − b³ = (a − b)³ + 3ab(a − b)','g')}
{box('৪. x ও 1/x',f'x² + {ix2} = (x + {ix})² − 2 = (x − {ix})² + 2<br>x³ + {ix3} = (x + {ix})³ − 3(x + {ix})<br>x³ − {ix3} = (x − {ix})³ + 3(x − {ix})<br>x⁴ + {ix4} = (x² + {ix2})² − 2','y')}
{box('৫. করণী থাকলে',f'x = √3 + √2 ⇒ {ix} = √3 − √2<br>x = 2 + √3 ⇒ {ix} = 2 − √3<br>আগে x + {ix} বা x − {ix} বের করো, তারপর সূত্র।','o')}
{box('৬. মনে রাখার কৌশল','• A² + 2AB + B² দেখলেই (A + B)²<br>• a + b + c = 0 ⇒ a³ + b³ + c³ = 3abc<br>• বর্গমূলে ± ; (2x)² = 4x²<br>• a³ − b³ এর দ্বিতীয় বন্ধনীতে +ab','g')}
</div>{box('৭. পরীক্ষার হলে ৩টি চেক','① মাঝের পদ (2ab / 3ab(a ± b)) লিখেছ তো? &nbsp; ② চিহ্ন (+/−) ঠিক আছে তো? &nbsp; ③ বর্গমূল নিলে ± দিয়েছ তো?','r')}</div>''')
html=f'<!DOCTYPE html><html lang="bn"><head><meta charset="utf-8"><style>{FONTS}{CSS}</style></head><body>{"".join(H_)}</body></html>'
open('lecture.html','w').write(html); print('html',len(html))
