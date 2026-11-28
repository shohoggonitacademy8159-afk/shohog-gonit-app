# এসএসসি উচ্চতর গণিত অধ্যায় ৯ (সূচকীয় ও লগারিদমীয় ফাংশন): ৪টি সৃজনশীল প্রশ্ন — সহজ ১, মধ্যম ২, কঠিন ১ (শুধু উত্তর)
import json, os
from sympy import Rational as R, Integer as I, symbols, solve, simplify, log, nsimplify, expand, cbrt, root
x=symbols('x',real=True)
# ১
u,v=root(2,3),1/root(2,3); X=u+v
assert simplify(u*v)==1 and simplify(u**3+v**3-R(5,2))==0 and simplify(2*X**3-6*X-5)==0 and (2**4,3**3)==(16,27)
# ২
assert solve(I(2)**x-8,x)==[3] and solve(I(8)**x-4,x)==[R(2,3)] and solve(I(4)**x-2,x)==[R(1,2)] and 3*R(2,3)*R(1,2)==1
# ৩
assert simplify(log(9-1,2))==3 and simplify(log(5-1,2))==2 and sorted(solve(x**2-1-8,x))==[-3,3]
# ৪
assert simplify(log(32,8))==R(5,3) and simplify(log(125,25))==R(3,2)
l2,l3=0.3010,0.4771; assert abs(3*l2+2*l3-1.8572)<1e-9 and abs(l3-l2-0.1761)<1e-9 and f'{l3/(l3-l2):.2f}'=='2.71'
CQ=[
('সহজ','9.1','x = 2^(1/3) + 2^(−1/3)',
 ['2^(1/3) · 2^(−1/3) এর মান এবং (2^(1/3))³ + (2^(−1/3))³ এর মান নির্ণয় কর।','প্রমাণ কর যে, 2x³ − 6x = 5','2^(1/3) ও 3^(1/4) এর মধ্যে কোনটি বড় তা নির্ণয় কর।'],
 'ক) 1 ; 2 + 1/2 = 5/2\nখ) x³ = 5/2 + 3·1·x ⇒ 2x³ = 5 + 6x ⇒ 2x³ − 6x = 5 (প্রমাণিত)\nগ) উভয়কে 12 ঘাতে তুলে 2⁴ = 16 ও 3³ = 27 ⇒ 3^(1/4) বড়'),
('মধ্যম','9.1','aˣ = b, bʸ = c এবং cᶻ = a, যেখানে a, b, c ধনাত্মক এবং 1 এর সমান নয়।',
 ['দেখাও যে, c = a^(xy)','প্রমাণ কর যে, xyz = 1','a = 2, b = 8 এবং c = 4 হলে x, y, z এর মান নির্ণয় কর এবং xyz = 1 যাচাই কর।'],
 'ক) c = bʸ = (aˣ)ʸ = a^(xy)\nখ) a = cᶻ = a^(xyz) ⇒ xyz = 1 (প্রমাণিত)\nগ) x = 3, y = 2/3, z = 1/2 ; 3 × 2/3 × 1/2 = 1'),
('মধ্যম','9.2','f(x) = log₂(x − 1)',
 ['f(9) ও f(5) এর মান নির্ণয় কর।','f এর ডোমেন ও রেঞ্জ নির্ণয় কর এবং বিপরীত ফাংশন f⁻¹(x) নির্ণয় কর।','সমাধান কর: f(x) + f(x + 2) = 3'],
 'ক) f(9) = log₂8 = 3 ; f(5) = log₂4 = 2\nখ) ডোমেন x > 1, রেঞ্জ সকল বাস্তব সংখ্যা ; f⁻¹(x) = 2ˣ + 1\nগ) log₂[(x − 1)(x + 1)] = 3 ⇒ x² − 1 = 8 ⇒ x = ±3 ; ডোমেন অনুযায়ী x = 3'),
('কঠিন','9.2','log 2 = 0.3010 এবং log 3 = 0.4771',
 ['log₈32 এবং log₂₅125 এর মান নির্ণয় কর।','log 72 এবং log 1.5 এর মান নির্ণয় কর।','সমাধান কর: 2ˣ = 3^(x − 1) (দুই দশমিক স্থান পর্যন্ত)'],
 'ক) 5/3 ; 3/2\nখ) log 72 = 3 log 2 + 2 log 3 = 1.8572 ; log 1.5 = log 3 − log 2 = 0.1761\nগ) x log 2 = (x − 1) log 3 ⇒ x = log 3/(log 3 − log 2) = 0.4771/0.1761 ≈ 2.71'),
]
items=[]
for i,(lv,ex,st,p_,a_) in enumerate(CQ):
    assert len(p_)==3 and a_.count('ক)')==1 and a_.count('খ)')==1 and a_.count('গ)')==1, i
    items.append({'n':f'b{i+1}','ex':ex,'stem':st,'p':p_,'a':a_,'lv':lv})
json.dump(items,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'cq_c10h_9.json'),'w'),ensure_ascii=False,indent=1); print('cq_c10h_9',len(items))
