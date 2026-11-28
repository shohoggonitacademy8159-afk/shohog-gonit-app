from sympy import *
a,b,c,x,y=symbols('a b c x y')
E=lambda l,r: expand(l-r)==0
assert E((3*x+5*y)**2,9*x**2+30*x*y+25*y**2) and 105**2==11025 and E((2*a-3*b)**2,4*a**2-12*a*b+9*b**2)
assert 7**2-2*12==25 and 7**2-4*12==1
assert 3**2+2==11 and 11**2-2==119
assert 81-2*26==29
assert E((2*x+3)**3,8*x**3+36*x**2+54*x+27) and 4**3-3*4==52 and 5**3+3*36*5==665
assert E((5*x-4)**2+(4-3*x)**2+2*(5*x-4)*(4-3*x),4*x**2)
A=sqrt(3)+sqrt(2); assert simplify(1/A-(sqrt(3)-sqrt(2)))==0 and simplify(A**3+1/A**3-18*sqrt(3))==0
assert simplify(((a+b)**3+(-(a+b))**3)) == 0 and expand(a**3+b**3+(-a-b)**3-3*a*b*(-a-b))==0
X=2+sqrt(3); assert simplify(X+1/X-4)==0 and simplify(X**2+1/X**2-14)==0 and simplify(X**3+1/X**3-52)==0
# L1
assert E((2*x+5)**2,4*x**2+20*x+25) and E((3*a-4*b)**2,9*a**2-24*a*b+16*b**2) and 98**2==9604 and E((x+5)*(x-3),x**2+2*x-15)
assert E((a+b-c)**2,a**2+b**2+c**2+2*a*b-2*b*c-2*c*a) and E((x-2*y)**3,x**3-6*x**2*y+12*x*y**2-8*y**3)
# L2
assert 25-12==13 and 125-90==35 and 9-2==7 and 27-9==18 and 9+20==29 and 9+40==49 and (100-38)/2==31
assert E((2*a+3*b)**2-(2*a-3*b)**2,24*a*b) and 997**2==994009
# L3
X=sqrt(5)+2; assert simplify(1/X-(sqrt(5)-2))==0 and simplify(X+1/X-2*sqrt(5))==0 and simplify(X**3+1/X**3-34*sqrt(5))==0
assert 64+12==76
cc=-a-b; assert simplify(a**2/(b*cc)+b**2/(cc*a)+cc**2/(a*b)-3)==0
assert 16-2==14 and 14**2-2==194
# MCQ
assert 25-8==17 and 4-2==2 and expand((x-2)**3).coeff(x,1)==12 and 101**2==10201 and 16+20==36 and 1+3==4 and (9-4==5 and 9-8==1 and 27-18==9)
# Self test
assert E((4*x-3*y)**2,16*x**2-24*x*y+9*y**2) and 36-2*8==20 and 25+2==27 and 125-3*5==110 and 1003**2==1006009
print('ok')
