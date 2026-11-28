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
