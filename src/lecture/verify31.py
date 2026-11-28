from sympy import *
a,b,c,x,y,z,p,q,r,m,n=symbols('a b c x y z p q r m n')
E=lambda l,rr: expand(l-rr)==0
# পাঠ্যবই অনুশীলনী ৩.১
assert E((2*a+3*b)**2,4*a**2+12*a*b+9*b**2) and E((x**2+2/y**2)**2,x**4+4*x**2/y**2+4/y**4) and E((4*y-5*x)**2,16*y**2-40*x*y+25*x**2)
assert E((5*x**2-y)**2,25*x**4-10*x**2*y+y**2) and E((3*b-5*c-2*a)**2,9*b**2+25*c**2+4*a**2-30*b*c+20*c*a-12*a*b)
assert E((a*x-b*y-c*z)**2,a**2*x**2+b**2*y**2+c**2*z**2-2*a*b*x*y+2*b*c*y*z-2*a*c*x*z) and 1007**2==1014049
A=7*p+3*q-5*r; B=8*p-4*q-5*r; assert E(A**2-2*A*B+B**2,(7*q-p)**2) and expand(A-B)==-p+7*q
A=2*m+3*n-p; B=2*m-3*n+p; assert E(A**2+B**2-2*A*B,(6*n-2*p)**2)
assert abs(6.35*6.35+2*6.35*3.65+3.65*3.65-100)<1e-9 and (2345*2345-759*759)//(2345-759)==3104
assert 16+240==256 and 81-72==9 and (4**2+2)**2-2==322 and Rational(9,4)-2==Rational(1,4)
s7,s5=sqrt(7),sqrt(5); ab=(7-5)/Integer(4); a2b2=(7+5)/Integer(2); assert ab==Rational(1,2) and a2b2==6 and 8*ab*a2b2==24
assert 81-62==19 and 9+16==25 and 2*14-2*11==6 and (3*3-4*4+2*5)**2==9
assert E((3*x-4*y+2*z)**2,9*x**2+16*y**2+4*z**2-24*x*y-16*y*z+12*z*x)
assert E((a+2*b)*(3*a+2*c),(2*a+b+c)**2-(b-c-a)**2) and E(x**2+10*x+24,(x+5)**2-1)
assert E((a**2+a*b+b**2)*(a**2-a*b+b**2),a**4+a**2*b**2+b**4)
# কাজ
assert E((4*x+3*y)**2+2*(4*x+3*y)*(4*x-3*y)+(4*x-3*y)**2,64*x**2) and 2*50-2*(144-50)//2==6
assert E((2*x+3*y)*(4*x-5*y),(3*x-y)**2-(4*y-x)**2)
# অনুশীলনী (নতুন)
assert E((3*x+2*y)**2,9*x**2+12*x*y+4*y**2) and E((2*a-5*b)**2,4*a**2-20*a*b+25*b**2) and E((x-3/x)**2,x**2-6+9/x**2)
assert E((2*x-y+3*z)**2,4*x**2+y**2+9*z**2-4*x*y-6*y*z+12*z*x) and 998**2==996004 and E((x+7)*(x-4),x**2+3*x-28)
assert 64-60==4 and 25+96==121 and 25-2==23 and 4+2==6 and (49-21)//2==14 and E((3*x+2*y)**2+2*(3*x+2*y)*(x-2*y)+(x-2*y)**2,16*x**2)
assert abs(5.75**2-2*5.75*0.75+0.75**2-25)<1e-9
assert (9+2)**2-2==119 and (11-7)/4==1 and (11+7)/2==9 and 4*1*9==36
assert E((2*x-3*y-z)**2,4*x**2+9*y**2+z**2-12*x*y+6*y*z-4*z*x) and (4-9-4)**2==81
assert E(x**2+8*x+15,(x+4)**2-1) and E((x+3*y)*(x-5*y),(x-y)**2-(4*y)**2) and 21//7==3 and (7+3)//2==5 and (7-3)//2==2
# MCQ / self test
assert 25-8==17 and 101**2==10201 and 9+16==25 and E(x**2-6*x+9,(x-3)**2) and 53*47==2491 and 9-4==5 and 9-8==1 and 9+1==10
assert E((3*x-4*y)**2,9*x**2-24*x*y+16*y**2) and 36-16==20 and 25+2==27 and 1003**2==1006009 and 36-22==14
X=sqrt(3)+sqrt(2); assert simplify(X+1/X-2*sqrt(3))==0 and simplify(X**2+1/X**2-10)==0
print('ok')
