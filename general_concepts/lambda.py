#what is called lambda ?
#lambda are called as anonymous function means function without an name mostly used for
#single line operation(code)
#syntax for lambda:
#-----------a=lambda args(optional):expression---------
import math
c=lambda :'------------------'
a=lambda :'hello'
print(a())
print(c())
b=lambda d:d**2
print(b(27))
print(c())
m=lambda a,b:(a**2)+(2*a*b)+(b**2)
print(m(2,5))
print(c())
print(m(4,6))
print(c())
v=lambda a=3,b=3:(a**2)+(2*a*b)+(b**2)
print(v(2))
print(math.pi)
avg=lambda r:math.pi*(r**2)
for a in range(0,11):
    print(c())
    print(f"area of circle for radius{a}={avg(a)}")

