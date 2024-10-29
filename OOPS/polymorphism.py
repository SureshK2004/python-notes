#in build polymorphism
import math
a=5
b=4
print(a+b)
a='hello'
b='world'
print(a+b)
l=[1,2,3,4]
print(len(l))
l='welcome to programing'
print(len(l))
a=8
b=7
print(a*b)
a='suresh'
b=6
print(a*b)

#polymorphism  with function
def add(x,y):
    return x+y
c=add(7,6)
print(c)
def sumofno(*args):
    sum=0
    for a in args:
        sum+=a
    return sum
a=sumofno(3,4,5,6)
print(a)
b=sumofno(1,4,6)
print(b)

#class with polymorphism
class india():
    def population(self):
        print('India is my country')
    def type(self):
        print('developing country')
class US():
    def population(self):
        print('US is my country')
    def type(self):
        print('developing country')
class UAE():
    def population(self):
        print('UAE is my country')
    def type(self):
        print('developing country')
'''i=india()
i.population()
i.type()
u=US()
u.population()
u.type()
d=UAE()
d.population()
d.type()'''
i=india()
u=US()
d=UAE()
for a in(i,u,d):
    a.population()
    a.type()

#inheritance with polymorphism
class shape():
    def __init__(self):
        print(" I am a parent class for all shapes")
        print("-------------------------------------")
    def volume(self):
        raise NotImplementedError("subclass must defined volume")
class square(shape):
    def __init__(self,a):
        self.a=a
    def volume(self):
        print(f"volume of square={self.a*self.a}")
class circle(shape):
    def __init__(self,r):
        self.r=r
    def volume(self):
        print(f"volume of circle={math.pi*(self.r**2)}")
class rectangle(shape):
    def __init__(self,l,b):
        self.l=l
        self.b=b
    def volume(self):
        print(f"volume of rectangle={self.l*self.b}")
s=square(4)
c=circle(4)
r=rectangle(3,6)
for a in (s,c,r):
    a.volume()


