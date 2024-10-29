
def sumofnumber(n):
    sum=0
    for a in str(n):
        sum+=int(a)
    return sum
'''o=sumofnumber(487)
print(o)'''
l1=[1234,136,14,15,16]
b=list(map(sumofnumber,l1))
print(b)
combine=dict(zip(l1,b))
print(combine)
