#qarakusayin python
import math
def qarakusayin(a,b,c):
    if(b>=0):
        b1=f"+{b}"
    if(c>=0):
        c1=f"+{c}"
    print(f"qarakusayin havasarumn e  {a}X^2{b1}X{c1}=0")
    d=b*b-4*a*c
    if(d>0):
        print(f"X1 = {(-b+math.sqrt(d))/(2*a)}")
        print(f"x2 = {(-b-math.sqrt(d))/(2*a)}")
    elif(d==0):
        print(f"X = {-b/(2*a)}")
    else:
        print("havasarumy lucum chuni")

a = float(input("grel havasarman a-i gorcakicy  "))
b = float(input("grel havasarman b-i gorcakicy  "))
c = float(input("grel havasarman c-i gorcakicy  "))

qarakusayin(a,b,c)


