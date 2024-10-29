'''num=int(input("enter the value:"))
if num<=10:
    print("below 10 or 10")
elif num<=100:
    print("below 100 or 100")
elif num<=1000:
    print("below 1000 or 1000")
else:
    print("above 1000")'''
id=int(input("enter the id:"))
name=input("enter the name:")
m1=int(input("enter the m1:"))
m2=int(input("enter the m2:"))
m3=int(input("enter the m3:"))
if m1<35 or m2<35 or m3<35:
    if m1 < 35 and m2 < 35 and m3 < 35:
        print("failed in all the subject")
    elif m1<35 and  m2<35:
        print("failed in 1 &2 subject")
    elif m2<35 and  m3<35:
        print("falied in 2 & 3 subject")
    elif m1<35 and m3<35:
        print("failed in 1 & 3 subject")
    elif m1<35:
        print("failed in m1")
    elif m2<35:
        print("failed in the m2")
    else:
        print("failed in m3")
else:
    total=m1+m2+m3
    avg=total/3
    print(avg)

