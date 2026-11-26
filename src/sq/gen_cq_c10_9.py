# এসএসসি সাধারণ গণিত অধ্যায় ৯ (ত্রিকোণমিতিক অনুপাত): ব্যবহারকারীর দেওয়া ১০টি সৃজনশীল প্রশ্ন (শুধু উত্তর; প্রমাণে "প্রমাণিত")
# ক (২), খ (৪), গ (৪)। নিচে সব উত্তর সংখ্যাগতভাবে যাচাই করা।
import json, os, math
from math import sin, cos, tan, radians as R, sqrt, isclose
sec=lambda x:1/cos(x); csc=lambda x:1/sin(x); cot=lambda x:1/tan(x)

# ---------- যাচাই ----------
A=math.atan(3/4); assert isclose(sin(A),3/5) and isclose(cos(A),4/5)
assert isclose((cos(A)+sin(A))/(cos(A)-sin(A)),7) and isclose((csc(A)+cot(A))/(csc(A)-cot(A)),9)
t=math.asin(21/29); assert isclose(sec(t)+tan(t),5/2) and isclose(sec(t)-tan(t),2/5) and isclose(cot(t)+csc(t),7/3)
a,b=R(60),R(30); assert isclose(sin(a)*cos(b)+cos(a)*sin(b),1) and isclose(cos(a)*cos(b)+sin(a)*sin(b),sqrt(3)/2) and isclose((tan(a)-tan(b))/(1+tan(a)*tan(b)),1/sqrt(3))
assert isclose(tan(R(60))**2,3)
for th in (0,60): assert abs(2*cos(R(th))**2-3*cos(R(th))+1)<1e-12
assert isclose(tan(R(45))+cot(R(45)),2)
assert isclose(sqrt(3+1),2) and isclose(math.degrees(math.atan(1/sqrt(3))),30) and isclose((tan(R(60))-tan(R(30)))/(1+tan(R(60))*tan(R(30))),tan(R(30)))
assert isclose(sec(R(45))+tan(R(45)),sqrt(2)+1)
for (aa,bb,th) in ((2,1,R(60)),(3,5,R(20))):
    x=aa*sec(th)+bb*tan(th); y=aa*tan(th)+bb*sec(th); assert isclose(x*x-y*y,aa*aa-bb*bb)
th=R(60); assert isclose(2*sec(th)+tan(th)+2*tan(th)+sec(th),6+3*sqrt(3))
for th in (R(30),R(50)): assert isclose(1/(1+sin(th))+1/(1-sin(th)),2*sec(th)**2) and isclose(sqrt((1-sin(th))/(1+sin(th))),sec(th)-tan(th))
assert isclose(2*sec(R(30))**2,8/3)
aa,bb=2.0,3.0; th=math.atan(aa/bb); assert isclose(sin(th),aa/sqrt(aa*aa+bb*bb)) and isclose((aa*sin(th)-bb*cos(th))/(aa*sin(th)+bb*cos(th)),(aa*aa-bb*bb)/(aa*aa+bb*bb))
assert isclose(cot(R(30)),sqrt(3)) and isclose(cos(R(60)),0.5)
for th in (R(30),R(70)):
    P=sec(th)+tan(th); assert isclose(P*(sec(th)-tan(th)),1) and isclose((P*P-1)/(P*P+1),sin(th))
assert isclose(sec(R(30))+tan(R(30)),sqrt(3))
th=R(45); assert isclose(sin(th)+cos(th),sqrt(2)) and isclose(sin(th)*cos(th),.5) and isclose(tan(th)+cot(th),2) and isclose(sin(th)**4+cos(th)**4,.5)

CQ=[  # (ex, মান, উদ্দীপক, [ক, খ, গ], উত্তর)
('9.1','সহজ',"ABC সমকোণী ত্রিভুজে ∠B = 90° এবং tanA = 3/4",
 ["sinA ও cosA এর মান নির্ণয় কর।","(cosA + sinA)/(cosA − sinA) এর মান নির্ণয় কর।","দেখাও যে, (cosecA + cotA)/(cosecA − cotA) = 9"],
 "ক) sinA = 3/5, cosA = 4/5\nখ) 7\nগ) প্রমাণিত"),
('9.1','মধ্যম',"secθ + tanθ = 5/2",
 ["secθ − tanθ এর মান নির্ণয় কর।","sinθ এর মান নির্ণয় কর।","দেখাও যে, cotθ + cosecθ = 7/3"],
 "ক) 2/5\nখ) 21/29\nগ) প্রমাণিত"),
('9.2','সহজ',"A = 60° এবং B = 30°",
 ["sinA·cosB + cosA·sinB এর মান নির্ণয় কর।","দেখাও যে, cosA·cosB + sinA·sinB = cos(A − B)","দেখাও যে, tan(A − B) = (tanA − tanB)/(1 + tanA·tanB)"],
 "ক) 1\nখ) প্রমাণিত (উভয় পক্ষ = √3/2)\nগ) প্রমাণিত (উভয় পক্ষ = 1/√3)"),
('9.2','মধ্যম',"(i) 2cos²θ − 3cosθ + 1 = 0\n(ii) tanθ + cotθ = 2   [0° ≤ θ ≤ 90°]",
 ["cosθ = 1/2 হলে tan²θ এর মান নির্ণয় কর।","(i) নং সমীকরণটি সমাধান কর।","(ii) নং সমীকরণটি সমাধান কর।"],
 "ক) 3\nখ) θ = 0° অথবা 60°\nগ) θ = 45°"),
('9.2','সহজ',"PQR সমকোণী ত্রিভুজে ∠Q = 90°, PQ = √3 একক এবং QR = 1 একক।",
 ["PR এর দৈর্ঘ্য নির্ণয় কর।","∠P ও ∠R এর মান নির্ণয় কর।","দেখাও যে, (tanR − tanP)/(1 + tanR·tanP) = tanP"],
 "ক) 2 একক\nখ) ∠P = 30°, ∠R = 60°\nগ) প্রমাণিত"),
('9.1','মধ্যম',"x = a secθ + b tanθ এবং y = a tanθ + b secθ",
 ["a = b = 1 এবং θ = 45° হলে x এর মান নির্ণয় কর।","প্রমাণ কর যে, x² − y² = a² − b²","a = 2, b = 1 এবং θ = 60° হলে x + y এর মান নির্ণয় কর।"],
 "ক) √2 + 1\nখ) প্রমাণিত\nগ) 6 + 3√3"),
('9.1','মধ্যম',"A = 1/(1 + sinθ) + 1/(1 − sinθ)",
 ["দেখাও যে, A = 2sec²θ","θ = 30° হলে A এর মান নির্ণয় কর।","প্রমাণ কর যে, √((1 − sinθ)/(1 + sinθ)) = secθ − tanθ"],
 "ক) প্রমাণিত\nখ) 8/3\nগ) প্রমাণিত"),
('সমন্বিত','মধ্যম',"cotθ = b/a",
 ["sinθ এর মান a ও b এর মাধ্যমে প্রকাশ কর।","প্রমাণ কর যে, (a sinθ − b cosθ)/(a sinθ + b cosθ) = (a² − b²)/(a² + b²)","a = 1, b = √3 হলে θ এবং cos2θ এর মান নির্ণয় কর।"],
 "ক) a/√(a² + b²)\nখ) প্রমাণিত\nগ) θ = 30°, cos2θ = 1/2"),
('সমন্বিত','মধ্যম',"P = secθ + tanθ",
 ["দেখাও যে, P(secθ − tanθ) = 1","প্রমাণ কর যে, (P² − 1)/(P² + 1) = sinθ","P = √3 হলে θ এর মান নির্ণয় কর।"],
 "ক) প্রমাণিত\nখ) প্রমাণিত\nগ) θ = 30°"),
('সমন্বিত','সহজ',"sinθ + cosθ = √2   (θ সূক্ষ্মকোণ)",
 ["sinθ·cosθ এর মান নির্ণয় কর।","tanθ + cotθ এর মান নির্ণয় কর।","θ এবং sin⁴θ + cos⁴θ এর মান নির্ণয় কর।"],
 "ক) 1/2\nখ) 2\nগ) θ = 45°, sin⁴θ + cos⁴θ = 1/2"),
]
items=[]
for i,(ex,lv,st,p_,a_) in enumerate(CQ):
    assert len(p_)==3 and a_.count('ক)')==1 and a_.count('খ)')==1 and a_.count('গ)')==1, i
    assert not any(ch in st+''.join(p_)+a_ for ch in '০১২৩৪৫৬৭৮৯'), i   # সংখ্যা ইংরেজি
    items.append({'n':f'b{i+1}','ex':ex,'stem':st,'p':p_,'a':a_,'lv':lv})
assert len(items)==10
json.dump(items,open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'cq_c10_9.json'),'w'),ensure_ascii=False,indent=1); print('cq_c10_9',len(items))
