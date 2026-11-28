from sympy import *
a,b,c,x,y,m,n,z,p,q=symbols('a b c x y m n z p q')
E=lambda l,r: expand(l-r)==0
# পাঠ্যবইয়ের উদাহরণ ও কাজ
assert E((2*x+3*y)**3,8*x**3+36*x**2*y+54*x*y**2+27*y**3) and E((2*x-y)**3,8*x**3-12*x**2*y+6*x*y**2-y**3) and (2*37+6)**3==512000
assert E(8*x**3+72*x**2+216*x+216,(2*x+6)**3)
assert E((3*x+2*y)**3,27*x**3+54*x**2*y+36*x*y**2+8*y**3) and E((3*x-4*y)**3,27*x**3-108*x**2*y+144*x*y**2-64*y**3) and 397**3==62570773
assert E(27*x**3-54*x**2+36*x-8,(3*x-2)**3) and (3*-2-2)**3==-512 and (125-90)+4*(25-24)==39
X=sqrt(5)+sqrt(3); assert simplify(X**3+8/X**3-28*sqrt(5))==0
# অনুশীলনী ৩.২
assert E((2*x**2+3*y**2)**3,8*x**6+36*x**4*y**2+54*x**2*y**4+27*y**6) and E((7*m**2-2*n)**3,343*m**6-294*m**4*n+84*m**2*n**2-8*n**3)
assert E((2*a-b-3*c)**3,8*a**3-12*a**2*b-36*a**2*c+6*a*b**2+36*a*b*c+54*a*c**2-b**3-9*b**2*c-27*b*c**2-27*c**3)
assert E((7*x+3*b)**3-(5*x+3*b)**3-6*x*(7*x+3*b)*(5*x+3*b),8*x**3)
assert E((a+b+c)**3-(a-b-c)**3-6*(b+c)*(a**2-(b+c)**2),8*(b+c)**3)
assert E((m+n)**6-(m-n)**6-12*m*n*(m**2-n**2)**2,64*m**3*n**3)
assert E((x+y)*(x**2-x*y+y**2)+(y+z)*(y**2-y*z+z**2)+(z+x)*(z**2-z*x+x**2),2*(x**3+y**3+z**3))
assert E((2*x+3*y-4*z)**3+(2*x-3*y+4*z)**3+12*x*(4*x**2-(3*y-4*z)**2),64*x**3)
assert 125+3*36*5==665 and (513-27)/9==54 and (2*19+3*-12)**3==8 and (2*15+5)**3+5==42880 and E(8*a**3+60*a**2+150*a+130,(2*a+5)**3+5)
mm,nn=symbols('mm nn'); AB=(mm**2-nn)/2; P3=mm**3-3*AB*mm; assert E(mm**3+2*P3,3*mm*nn)
assert 9-2*2-2==3 and 3*3==9 and 25+2*36+36==133 and 5*133==665
assert 1+3==4
cc=-a-b; assert simplify(a**3+b**3+cc**3-3*a*b*cc)==0 and simplify((b+cc)**2/(3*b*cc)+(cc+a)**2/(3*cc*a)+(a+b)**2/(3*a*b)-1)==0
assert E((q+p-q)**3-q**3-(p-q)**3,3*p*q*(p-q))
t=Rational(3,2); assert t**3+3*t==Rational(63,8) and 8*Rational(63,8)==63
A=sqrt(6)+sqrt(5); assert simplify(1/A-(sqrt(6)-sqrt(5)))==0 and simplify((A**6-1)/A**3-46*sqrt(5))==0
s=sqrt(3); assert s**2+2==5 and 25-2==23 and 23*5==5*23 and 125-15==110
xx=(s+sqrt(7))/2; assert simplify(xx-1/xx-s)==0 and simplify(xx**6+1/xx**6-110)==0 and simplify(xx**2-s*xx-1)==0
# নতুন অনুশীলনী
assert E((x+3)**3,x**3+9*x**2+27*x+27) and E((2*a-3*b)**3,8*a**3-36*a**2*b+54*a*b**2-27*b**3) and E((3*x**2+2*y)**3,27*x**6+54*x**4*y+36*x**2*y**2+8*y**3)
assert 103**3==1092727 and 99**3==970299 and E((a+2)*(a**2-2*a+4),a**3+8)
assert 64-36==28 and 8+90==98 and (512-152)/24==15 and (3*3+2)**3==1331 and E(27*x**3+54*x**2+36*x+8,(3*x+2)**3) and 27-9==18 and 8+6==14
assert E((5*x+2)**3-(3*x+2)**3-6*x*(5*x+2)*(3*x+2),8*x**3)
A=sqrt(3)+sqrt(2); assert simplify((A**6+1)/A**3-18*sqrt(3))==0 and simplify(a**2/(b*cc)+b**2/(cc*a)+cc**2/(a*b)-3)==0
t=Rational(4,3); assert 27*(t**3+3*t)==172
r5=sqrt(5); assert simplify(r5**2-2-3)==0 and simplify(r5**3-3*r5-2*r5)==0 and 27-9==18
# MCQ / self test
assert 27-18==9 and 8+18==26 and 8-6==2 and expand((x-2)**3).coeff(x,2)==-6 and E(8*x**3+12*x**2+6*x+1,(2*x+1)**3) and 1+3==4 and 8-6==2 and 4-3==1
assert E((x-3*y)**3,x**3-9*x**2*y+27*x*y**2-27*y**3) and 125-60==65 and 27+9==36 and 101**3==1030301 and (8+2)**3==1000
A=sqrt(2)+1; assert simplify(A**3+1/A**3-10*sqrt(2))==0
print('ok')
