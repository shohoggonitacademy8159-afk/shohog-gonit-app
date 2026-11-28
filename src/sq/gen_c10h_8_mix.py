# উচ্চতর গণিত অধ্যায় ৮, অনুশীলনী 8.2 (পাঠ্যবইয়ের অংকগুলো মিশিয়ে): ১৩টি সংক্ষিপ্ত প্রশ্ন (c10h_8.json এর শেষে b91–b103)
# এবং ২০টি MCQ (src/mcq/ext/L1_c10h_8.json — আগের সব MCQ এর নম্বর অপরিবর্তিত রেখে শেষে যোগ হয়)। সব উত্তর কোডে যাচাই করা
import json, os, math as M
from sympy import Rational as R, pi, sqrt, sin, cos, tan, cot, sec, csc, simplify, symbols
Z=lambda e: simplify(e)==0
HERE=os.path.dirname(os.path.abspath(__file__))
def roots(f,lo,hi,closed=False,n=200000):
    # f এর মূলগুলো [lo,hi] এ (সংখ্যাগত), π এর ভগ্নাংশ হিসেবে মেলানোর জন্য float তালিকা
    xs=[lo+(hi-lo)*i/n for i in range(n+1)]; out=[]
    for i in range(1,n):
        try: a,b,c=abs(f(xs[i-1])),abs(f(xs[i])),abs(f(xs[i+1]))
        except (ZeroDivisionError,ValueError): continue
        if b<=a and b<=c and b<1e-3:
            if not out or xs[i]-out[-1]>1e-3: out.append(xs[i])
    if closed:
        for e in (lo,hi):
            if abs(f(e))<1e-9 and all(abs(e-o)>1e-3 for o in out): out.append(e)
    return sorted(out)
same=lambda got,exp: len(got)==len(exp) and all(abs(g-e*M.pi)<1e-3 for g,e in zip(got,exp))
# ---------- সংক্ষিপ্ত ----------
assert Z(sin(pi/4)/(sin(pi/6)+cos(pi/3))-1/sqrt(2))
assert cot(pi/4)+cot(pi/6)*cot(pi/3)==2
assert (R(-4,5))**2+R(3,5)**2==1
assert Z(cos(7*pi/6)+sqrt(3)/2) and sin(7*pi/6)==-R(1,2) and Z(tan(7*pi/6)-1/sqrt(3))
th=symbols('th'); assert Z((csc(th)**4-csc(th)**2)-(cot(th)**4+cot(th)**2))
assert Z((sin(th)+cos(th))**2+(sin(th)-cos(th))**2-2)
assert Z(cos(pi/6)**2+sin(pi/4)**2+cot(pi/3)**2+tan(pi/6)**2-R(23,12))
assert Z(2*cot(pi/4)**2-cos(pi/6)**2+R(1,2)*tan(pi/3)**2-R(1,3)*sec(pi/6)**2-R(83,36))
assert Z(sum(sin(k*pi/8)**2 for k in (1,3,5,7))-2)
assert Z(cos(5*pi/4)+1/sqrt(2))
assert same(roots(lambda x:2*M.sin(x)**2-1-2*M.cos(x)**2,1e-9,M.pi/2-1e-9),[R(1,3)])
assert same(roots(lambda x:2*M.sin(x)*M.cos(x)-M.cos(x),0,2*M.pi,closed=True),[R(1,6),R(1,2),R(5,6),R(3,2)])
c,s=M.cos(1.0),M.sin(1.0)   # cosθ + sinθ = √2cosθ ⇒ cosθ − sinθ = √2sinθ (θ = π/8 এ যাচাই)
x8=M.pi/8; assert abs(M.cos(x8)+M.sin(x8)-M.sqrt(2)*M.cos(x8))<1e-12 and abs(M.cos(x8)-M.sin(x8)-M.sqrt(2)*M.sin(x8))<1e-12
SQ=[
('sin(π/4)/(sin(π/6) + cos(π/3)) এর মান নির্ণয় কর।','sin(π/4) = 1/√2, sin(π/6) + cos(π/3) = 1/2 + 1/2 = 1 ⇒ মান = 1/√2','সহজ'),
('cot(π/4) + cot(π/6)·cot(π/3) এর মান নির্ণয় কর।','1 + √3 × 1/√3 = 1 + 1 = 2','সহজ'),
('sinA = 3/5 এবং π/2 < A < π হলে cosA ও tanA এর মান নির্ণয় কর।','A দ্বিতীয় চতুর্ভাগে ⇒ cosA = −4/5, tanA = −3/4','সহজ'),
('cosA = −√3/2 এবং sinA ও cosA একই চিহ্নবিশিষ্ট হলে sinA ও tanA এর মান নির্ণয় কর।','উভয়ই ঋণাত্মক ⇒ A তৃতীয় চতুর্ভাগে ⇒ sinA = −1/2, tanA = 1/√3','মধ্যম'),
('প্রমাণ কর: cosec⁴θ − cosec²θ = cot⁴θ + cot²θ','বামপক্ষ = cosec²θ(cosec²θ − 1) = (1 + cot²θ)cot²θ = cot²θ + cot⁴θ = ডানপক্ষ','মধ্যম'),
('প্রমাণ কর: (sinθ + cosθ)² + (sinθ − cosθ)² = 2','বামপক্ষ = 2(sin²θ + cos²θ) = 2','সহজ'),
('cosθ + sinθ = √2 cosθ হলে দেখাও যে, cosθ − sinθ = √2 sinθ','sinθ = (√2 − 1)cosθ ⇒ (√2 + 1)sinθ = cosθ ⇒ cosθ − sinθ = √2 sinθ','মধ্যম'),
('মান নির্ণয় কর: cos²(π/6) + sin²(π/4) + cot²(π/3) + tan²(π/6)','3/4 + 1/2 + 1/3 + 1/3 = 23/12','মধ্যম'),
('মান নির্ণয় কর: 2cot²(π/4) − cos²(π/6) + ½tan²(π/3) − ⅓sec²(π/6)','2 − 3/4 + 3/2 − 4/9 = 83/36','মধ্যম'),
('মান নির্ণয় কর: sin²(π/8) + sin²(3π/8) + sin²(5π/8) + sin²(7π/8)','sin(3π/8) = cos(π/8), sin(5π/8) = cos(π/8)… ⇒ (sin² + cos²)(π/8) × 2 = 2','কঠিন'),
('cosα = −1/√2 এবং π < α < 3π/2 হলে α এর মান নির্ণয় কর।','তৃতীয় চতুর্ভাগে ⇒ α = π + π/4 = 5π/4','মধ্যম'),
('সমাধান কর: 2sin²θ = 1 + 2cos²θ, যখন 0 < θ < π/2','2sin²θ = 1 + 2 − 2sin²θ ⇒ sin²θ = 3/4 ⇒ sinθ = √3/2 ⇒ θ = π/3','মধ্যম'),
('সমাধান কর: 2sinx cosx = cosx, যখন 0 ≤ x ≤ 2π','cosx(2sinx − 1) = 0 ⇒ x = π/2, 3π/2 অথবা sinx = 1/2 ⇒ x = π/6, 5π/6','কঠিন'),
]
assert len(SQ)==13
p=os.path.join(HERE,'c10h_8.json'); cur=json.load(open(p,encoding='utf-8'))
cur=[x for x in cur if int(x['n'][1:])<=90]; assert len(cur)==90
for i,(q,a,lv) in enumerate(SQ): cur.append({'n':f'b{91+i}','q':q,'a':a,'lv':lv,'ex':'8.2'})
json.dump(cur,open(p,'w',encoding='utf-8'),ensure_ascii=False,indent=1)
# ---------- MCQ ----------
assert sin(pi/6)+cos(pi/3)==1 and tan(pi/4)*cot(pi/4)==1 and Z(cos(5*pi/4)+1/sqrt(2)) and sin(5*pi/6)==R(1,2)
assert Z(cot(7*pi/4)+1) and R(-3,5)/R(-4,5)==R(3,4)
assert Z(sqrt(1-R(4,5))-1/sqrt(5))
assert sin(pi/3)==sqrt(3)/2 and sin(pi)==0 and Z(sin(2*pi/4)-1) and Z(cos(3*pi/4)+1/sqrt(2))
assert abs(M.prod(1/M.tan(k*M.pi/20) for k in (1,3,5,7,9))-1)<1e-12
assert same(roots(lambda x:2*M.sin(x)**2-3*M.cos(x),1e-9,M.pi/2-1e-9),[R(1,3)])
assert same(roots(lambda x:6*M.sin(x)**2-11*M.sin(x)+4,1e-9,M.pi/2-1e-9),[R(1,6)])
assert len(roots(lambda x:1/M.tan(x)**2+1/M.sin(x)**2-3,1e-6,2*M.pi-1e-6))==4
assert same(roots(lambda x:2*M.sin(x)*M.cos(x)-M.sin(x),0,2*M.pi,closed=True),[0,R(1,3),1,R(5,3),2])
MQ=[
('sin(π/6) + cos(π/3) = কত?',['1/2','1','√3','3/2'],1,'1/2 + 1/2 = 1','সহজ'),
('tan(π/4)·cot(π/4) = কত?',['0','1','√3','2'],1,'tanθ·cotθ = 1','সহজ'),
('θ তৃতীয় চতুর্ভাগে থাকলে নিচের কোনটি ধনাত্মক?',['sinθ','cosθ','tanθ','secθ'],2,'তৃতীয় চতুর্ভাগে শুধু tan ও cot ধনাত্মক।','সহজ'),
('sec²θ − tan²θ = কত?',['0','1','−1','2'],1,'1 + tan²θ = sec²θ','সহজ'),
('cos(5π/4) = কত?',['1/√2','−1/√2','√3/2','−1/2'],1,'5π/4 = π + π/4, তৃতীয় চতুর্ভাগে cos ঋণাত্মক।','সহজ'),
('sin(5π/6) = কত?',['−1/2','1/2','√3/2','−√3/2'],1,'sin(π − π/6) = sin(π/6)','সহজ'),
('cotα = −1 এবং π < α < 2π হলে α = কত?',['3π/4','5π/4','7π/4','5π/3'],2,'চতুর্থ চতুর্ভাগে cot ঋণাত্মক ⇒ α = 2π − π/4','সহজ'),
('cosθ = −4/5 এবং π < θ < 3π/2 হলে tanθ = কত?',['−3/4','3/4','−4/3','4/3'],1,'sinθ = −3/5 ⇒ tanθ = 3/4','সহজ'),
('sinA = 2/√5 এবং π/2 < A < π হলে cosA = কত?',['1/√5','−1/√5','2/√5','−2'],1,'দ্বিতীয় চতুর্ভাগে cos ঋণাত্মক ⇒ −√(1 − 4/5)','মধ্যম'),
('tanθ + secθ = 2 হলে secθ − tanθ = কত?',['2','1/2','−1/2','4'],1,'(secθ + tanθ)(secθ − tanθ) = 1','মধ্যম'),
('tanθ + secθ = x হলে sinθ = কত?',['(x² − 1)/(x² + 1)','(x² + 1)/(x² − 1)','2x/(x² + 1)','(x² + 1)/(2x)'],0,'secθ − tanθ = 1/x থেকে secθ ও tanθ বের করে sinθ = tanθ/secθ','মধ্যম'),
('sin²(π/4) + sin²(3π/4) + sin²(5π/4) + sin²(7π/4) = কত?',['1','2','0','4'],1,'প্রতিটি পদ 1/2','মধ্যম'),
('cot(π/20)·cot(3π/20)·cot(5π/20)·cot(7π/20)·cot(9π/20) = কত?',['0','1','√3','−1'],1,'cot(9π/20) = tan(π/20), cot(7π/20) = tan(3π/20), cot(π/4) = 1','মধ্যম'),
('0 < θ < π/2 হলে 2sin²θ − 3cosθ = 0 সমীকরণের সমাধান কোনটি?',['π/6','π/4','π/3','π/2'],2,'2cos²θ + 3cosθ − 2 = 0 ⇒ cosθ = 1/2','মধ্যম'),
('0 < θ < π/2 হলে 6sin²θ − 11sinθ + 4 = 0 সমীকরণের সমাধান কোনটি?',['π/6','π/4','π/3','5π/6'],0,'(3sinθ − 4)(2sinθ − 1) = 0 ⇒ sinθ = 1/2','মধ্যম'),
('θ = π/3 হলে sin3θ = কত?',['0','1','−1','√3/2'],0,'sinπ = 0','মধ্যম'),
('θ = π/4 হলে—\ni. sin2θ = 1\nii. tan2θ অসংজ্ঞায়িত\niii. cos3θ = 1/√2\nনিচের কোনটি সঠিক?',['i ও ii','i ও iii','ii ও iii','i, ii ও iii'],0,'cos(3π/4) = −1/√2, তাই iii ভুল।','মধ্যম'),
('a cosθ − b sinθ = c হলে a sinθ + b cosθ = কত?',['±√(a² + b² − c²)','±√(a² − b² + c²)','±√(a² + b² + c²)','a² + b² − c²'],0,'উভয় রাশির বর্গের যোগফল = a² + b²','কঠিন'),
('0 < θ < 2π ব্যবধিতে cot²θ + cosec²θ = 3 সমীকরণের কয়টি সমাধান আছে?',['1টি','2টি','3টি','4টি'],3,'cosec²θ = 2 ⇒ θ = π/4, 3π/4, 5π/4, 7π/4','কঠিন'),
('0 ≤ x ≤ 2π ব্যবধিতে 2sinx cosx = sinx সমীকরণের কয়টি সমাধান আছে?',['3টি','4টি','5টি','6টি'],2,'sinx = 0 ⇒ 0, π, 2π ; cosx = 1/2 ⇒ π/3, 5π/3','কঠিন'),
]
assert len(MQ)==20 and all(len(set(o))==4 for _,o,_,_,_ in MQ)
json.dump([{'q':q,'o':o,'a':a,'e':e,'lv':lv,'ex':'8.2'} for q,o,a,e,lv in MQ],
          open(os.path.join(HERE,'..','mcq','ext','L1_c10h_8.json'),'w',encoding='utf-8'),ensure_ascii=False,indent=1)
print('sq +13, mcq 20')
