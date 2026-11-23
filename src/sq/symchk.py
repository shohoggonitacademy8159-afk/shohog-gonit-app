# বীজগাণিতিক উত্তর যাচাই: eq('lhs','rhs') — বাংলা/ইউনিকোড প্রতীক বদলে sympy দিয়ে মেলায়
import sympy as sp, re
from sympy.parsing.sympy_parser import parse_expr, standard_transformations, implicit_multiplication_application, convert_xor
T=standard_transformations+(implicit_multiplication_application,convert_xor)
SUP={'²':'^2','³':'^3','⁴':'^4','⁶':'^6','⁵':'^5','⁻¹':'^(-1)'}
def P(s):
    s=s.replace('−','-').replace('×','*').replace('÷','/')
    for k,v in SUP.items(): s=s.replace(k,v)
    s=re.sub(r'√\(',r'sqrt(',s); s=re.sub(r'√(\d+|[a-z])',r'sqrt(\1)',s)
    return parse_expr(s,transformations=T)
def eq(a,b): d=sp.simplify(sp.expand(P(a)-P(b))); assert d==0,(a,b,d)
def val(a,**kw): return sp.nsimplify(sp.simplify(P(a).subs({sp.Symbol(k):v for k,v in kw.items()})))
