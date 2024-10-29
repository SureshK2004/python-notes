l=[1,4,2,9,10]
l1=lambda a:a**2
print(l1(2))
print(l1(9))
o=list(map(l1,l))
print(o)

r=[1,4,2,9,10]
s=[2,4,5,6,7]
l2=lambda a,b:(a**2)+(b**2)+(2*a*b)
o2=list(map(l2,r,s))
print(o2)

'''def tempcheck(t):
    temp=t
    for a in range(len(temp)):
        print(temp[a])
tempcheck([11,12,13,14,15])'''

'''def tempcheck(t):
    o=[]
    temp=t
    for a  in range(len(temp)):
        if temp[a]<0:
            o.append('cold')
        elif temp[a]>=0 and temp[a]<=15:
            o.append('medium cold')
        elif temp[a]>=16 and temp[a]<=25:
            o.append('hot')
        else:
            o.append('extreme hot')
    return o'''
'''tempv=tempcheck([11,12,55,-11,-7,4])
print(tempv)'''

'''i=list(map(tempcheck([11,12,55,-11,-7,4])))
print(i)'''
def tempcheck(a):
    o=[]
    if a < 0:
        o.append('cold')
    elif a >= 0 and a <= 15:
        o.append('medium cold')
    elif a >= 16 and a <= 25:
        o.append('medium hot')
    elif a >= 26 and a <= 35:
        o.append('hot')
    else:
        o.append('extreme hot')

    return o
inp=[11,12,34,45,67,-3,3,-4]
o3=list(map(tempcheck,inp))
print(o3)
zippedoutput=dict(zip(inp,o3))
print(zippedoutput)


