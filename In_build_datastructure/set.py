#point to remember
#duplicate value not printed
#o/p order will not same a input
#(so that indexing,slicing,will not work)
set={1,2,3,4,5,3}
print(set)
print(dir(set))
s1=set.copy()
print(s1)
s1.clear()
print(s1)
s1.add(7)
s1.add(4)
s1.add(7)
print(s1)
#intersection
n={1,2,3,4,5}
n1={2,3,5,6,7,4}
n2={1,3,5,7,4}
intersection=n.intersection(n1,n2)
print(intersection)
#symbol intersection
x=n1&n2
print(x)
#union
unionout=n.union(n1,n2)
print(unionout)
#union symbol
x=n1|n2
print(x)
#diiference symbol
difference=n-n1
print(difference)
#difference
diff=n.difference(n2)
print(diff)
#symmetric difference
symetric=n1.symmetric_difference(n2)
print(symetric)
#symmetic symbol
sy_diff=n^n2
print(sy_diff)
#pop
print(n)
n.pop()
print(n)
#difference b/w discard(different value kudutha output varum) and remove(different value kudutha error varum)
m={1,2,3,4,6,7}
print(m)
m.discard(9)
print(m)
m.remove(3)
print(m)
#issubset
a={'a','b','c'}
b={'a,b'}
print(a)
print(b)
print(a.issubset(b))
#issuperset
d={'d','e','f'}
f={'d','e'}
print(d)
print(f)
print(d.issuperset(f))
print(f.isdisjoint(d))
print(n)
print(n1)
n1.difference_update(n)
print(n1)
n1.intersection_update(n)
print(n1)
n1.symmetric_difference_update(n)
print(n1)
s4={1,2,2,3,4}
s5={7,8}
s4.update(s5)
print(s4)
print(s5)