# এসএসসি উচ্চতর গণিত অধ্যায় ২ (বীজগাণিতিক রাশি): ৮টি সৃজনশীল প্রশ্ন — প্রতিটির 'গ' তে আংশিক ভগ্নাংশ (শুধু উত্তর)
# ক (২), খ (৪), গ (৪)। উত্তরের লেখা sympy দিয়ে পার্স করে যাচাই করা হয়
import json, os, re
from sympy import symbols, simplify, factor, expand, Rational
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application
x,a,b,c,t=symbols('x a b c t')
TR=standard_transformations+(implicit_multiplication_application,)
SUP={'²':'**2','³':'**3'}
def P(s):
    s=s.replace('−','-').replace('×','*')
    for k,v in SUP.items(): s=s.replace(k,v)
    return parse_expr(s,transformations=TR,local_dict={'x':x,'a':a,'b':b,'c':c,'t':t})
def same(u,v): return simplify(P(u)-P(v))==0

# ---------- যাচাই ----------
p1='x³ − 6x² + 11x − 6'; assert P(p1).subs(x,1)==0 and P(p1).subs(x,2)==0 and same(p1,'(x − 1)(x − 2)(x − 3)')
assert same('(x² + 1)/(x³ − 6x² + 11x − 6)','1/(x − 1) − 5/(x − 2) + 5/(x − 3)')
p2='2x³ + 3x² − 11x − 6'; assert P(p2).subs(x,1)==-12 and same(p2,'(x − 2)(2x + 1)(x + 3)')
assert same('5(x² + 1)/(2x³ + 3x² − 11x − 6)','1/(x − 2) − 1/(2x + 1) + 2/(x + 3)')
q=P('x³ + a x² + b x − 6'); sol={a:4,b:1}; assert q.subs(sol).subs(x,1)==0 and q.subs(sol).subs(x,-2)==0
assert q.subs(x,1)==a+b-5 and same('x³ + 4x² + x − 6','(x − 1)(x + 2)(x + 3)')
assert same('(x + 5)/(x³ + 4x² + x − 6)','1/(2(x − 1)) − 1/(x + 2) + 1/(2(x + 3))')
e4='a²(b − c) + b²(c − a) + c²(a − b)'; E=P(e4)
assert simplify(E-E.subs({a:b,b:c,c:a},simultaneous=True))==0 and same(e4,'−(a − b)(b − c)(c − a)')
assert same('x²/((x − 1)(x − 2)(x − 3))','1/(2(x − 1)) − 4/(x − 2) + 9/(2(x − 3))')
p5='x³ − 3x + 2'; assert P(p5).subs(x,1)==0 and P(p5).subs(x,-2)==0 and same(p5,'(x − 1)²(x + 2)')
assert same('(5x + 1)/(x³ − 3x + 2)','1/(x − 1) + 2/(x − 1)² − 1/(x + 2)')
assert P('x³ − 1').subs(x,-1)==-2 and same('x³ − 1','(x − 1)(x² + x + 1)')
assert same('3/(x³ − 1)','1/(x − 1) − (x + 2)/(x² + x + 1)')
assert same('x² − 5x + 6','(x − 2)(x − 3)') and same('x³ + 1','(x² − 5x + 6)(x + 5) + 19x − 29')
assert same('(x³ + 1)/(x² − 5x + 6)','x + 5 − 9/(x − 2) + 28/(x − 3)')
R=[1,-2,3]; assert sum(R)==2 and R[0]*R[1]+R[1]*R[2]+R[2]*R[0]==-5 and R[0]*R[1]*R[2]==-6
assert sum(r*r for r in R)==14 and sum(r**3 for r in R)==20 and 2**3-3*2*(-5)+3*(-6)==20
assert same('(t − 1)(t + 2)(t − 3)','t³ − 2t² − 5t + 6') and same('(7t − 1)/(t³ − 2t² − 5t + 6)','2/(t − 3) − 1/(t − 1) − 1/(t + 2)')

CQ=[  # (মান, উদ্দীপক, [ক, খ, গ], উত্তর)
('সহজ',"P(x) = x³ − 6x² + 11x − 6",
 ["P(1) ও P(2) এর মান নির্ণয় কর।","P(x) কে উৎপাদকে বিশ্লেষণ কর।","(x² + 1)/P(x) কে আংশিক ভগ্নাংশে প্রকাশ কর।"],
 "ক) P(1) = 0, P(2) = 0\nখ) (x − 1)(x − 2)(x − 3)\nগ) 1/(x − 1) − 5/(x − 2) + 5/(x − 3)"),
('মধ্যম',"P(x) = 2x³ + 3x² − 11x − 6",
 ["P(x) কে (x − 1) দ্বারা ভাগ করলে ভাগশেষ নির্ণয় কর।","P(x) কে উৎপাদকে বিশ্লেষণ কর।","5(x² + 1)/P(x) কে আংশিক ভগ্নাংশে প্রকাশ কর।"],
 "ক) −12\nখ) (x − 2)(2x + 1)(x + 3)\nগ) 1/(x − 2) − 1/(2x + 1) + 2/(x + 3)"),
('মধ্যম',"P(x) = x³ + ax² + bx − 6 রাশির দুইটি উৎপাদক (x − 1) ও (x + 2)।",
 ["উৎপাদক উপপাদ্য ব্যবহার করে a ও b এর মধ্যে একটি সম্পর্ক নির্ণয় কর।","a ও b এর মান নির্ণয় কর এবং P(x) কে উৎপাদকে বিশ্লেষণ কর।","খ এ প্রাপ্ত P(x) এর জন্য (x + 5)/P(x) কে আংশিক ভগ্নাংশে প্রকাশ কর।"],
 "ক) a + b = 5\nখ) a = 4, b = 1; P(x) = (x − 1)(x + 2)(x + 3)\nগ) 1/(2(x − 1)) − 1/(x + 2) + 1/(2(x + 3))"),
('কঠিন',"E = a²(b − c) + b²(c − a) + c²(a − b)",
 ["দেখাও যে, E একটি চক্রক্রমিক রাশি।","E কে উৎপাদকে বিশ্লেষণ কর।","a = 1, b = 2, c = 3 হলে x²/((x − a)(x − b)(x − c)) কে আংশিক ভগ্নাংশে প্রকাশ কর।"],
 "ক) প্রমাণিত\nখ) −(a − b)(b − c)(c − a)\nগ) 1/(2(x − 1)) − 4/(x − 2) + 9/(2(x − 3))"),
('মধ্যম',"P(x) = x³ − 3x + 2",
 ["P(1) ও P(−2) এর মান নির্ণয় কর।","P(x) কে উৎপাদকে বিশ্লেষণ কর।","(5x + 1)/P(x) কে আংশিক ভগ্নাংশে প্রকাশ কর।"],
 "ক) P(1) = 0, P(−2) = 0\nখ) (x − 1)²(x + 2)\nগ) 1/(x − 1) + 2/(x − 1)² − 1/(x + 2)"),
('মধ্যম',"P(x) = x³ − 1",
 ["P(x) কে (x + 1) দ্বারা ভাগ করলে ভাগশেষ নির্ণয় কর।","P(x) কে উৎপাদকে বিশ্লেষণ কর এবং দেখাও যে, এর একটি উৎপাদক বাস্তব সংখ্যায় আর উৎপাদকে বিশ্লেষণযোগ্য নয়।","3/P(x) কে আংশিক ভগ্নাংশে প্রকাশ কর।"],
 "ক) −2\nখ) (x − 1)(x² + x + 1); x² + x + 1 এর নিশ্চায়ক 1 − 4 = −3 < 0\nগ) 1/(x − 1) − (x + 2)/(x² + x + 1)"),
('কঠিন',"f(x) = x² − 5x + 6 এবং g(x) = x³ + 1",
 ["f(x) কে উৎপাদকে বিশ্লেষণ কর।","g(x) কে f(x) দ্বারা ভাগ করে ভাগফল ও ভাগশেষ নির্ণয় কর।","g(x)/f(x) কে আংশিক ভগ্নাংশে প্রকাশ কর।"],
 "ক) (x − 2)(x − 3)\nখ) ভাগফল x + 5, ভাগশেষ 19x − 29\nগ) x + 5 − 9/(x − 2) + 28/(x − 3)"),
('কঠিন',"x + y + z = 2, xy + yz + zx = −5 এবং xyz = −6",
 ["x² + y² + z² এর মান নির্ণয় কর।","x³ + y³ + z³ এর মান নির্ণয় কর।","x, y, z যে সমীকরণ t³ − 2t² − 5t + 6 = 0 এর মূল, তা ব্যবহার করে (7t − 1)/(t³ − 2t² − 5t + 6) কে আংশিক ভগ্নাংশে প্রকাশ কর।"],
 "ক) 14\nখ) 20\nগ) 2/(t − 3) − 1/(t − 1) − 1/(t + 2)"),
]
items=[]
for i,(lv,st,p_,a_) in enumerate(CQ):
    assert len(p_)==3 and a_.count('ক)')==1 and a_.count('খ)')==1 and a_.count('গ)')==1, i
    assert 'আংশিক ভগ্নাংশ' in p_[2], i
    items.append({'n':f'b{i+1}','ex':'সমন্বিত','stem':st,'p':p_,'a':a_,'lv':lv})
assert len(items)==8
json.dump(items,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'cq_c10h_2.json'),'w'),ensure_ascii=False,indent=1); print('cq_c10h_2',len(items))
