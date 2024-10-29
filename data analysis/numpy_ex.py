import numpy as np
'''l=[1,2,3,4,5] # single dimensional array
print(l)
a=np.array(l)
print(a)
o=[]
for i in range(len(l)):
    print(l[i])
    o.append(l[i]+1)
print(o)
print(a+1)
print(a*2)
#two dimesional array
l=[[1,2,3],[4,5,6],[7,8,9]] # two dimensional array
print(l)
b=np.array(l)
print(b)
print(b+2)
#three dimensional array
l=[[[1,2],[3,4],[5,6]],[[44,55],[66,77],[88,77]],[[40,20],[30,10],[70,80]]] # three dimensional array
print(l)
c=np.array(l)
print(c)

sl=[]
for b in range(5):
    n=int(input("enter the register number:"))
    sl.append(n)
print(sl)
d=np.array(sl)
print(d)

w=[]
for a in range(1,4):
    t=[]
    for b in range(1,4):
        n=int(input(f"enter the {a}row and {b}column value"))
        t.append(n)
    w.append(t)
print(w)

st_list=[]
avg_list=[]
sum_list=[]
for a in range(1,6):
    sum=0
    t=[]
    for b in range(1,6):
        n=int(input(f"enter the {a}row and {b}column value"))
        t.append(n)
        sum+=n
    st_list.append(t)
    avg_list.append(sum)
    sum_list.append(sum/5)
print(st_list)
print(avg_list)
print(sum_list)
l=[8,9,17,22,24,27,12]
a=np.array(l)
print(a[6])
print(a[3:6])

print(np.arange(17))#if it is an negative value oit will print only empty array

print(np.linspace(0,10,5))#linspace
print(np.linspace(10,100,20))
print(np.zeros(5))
print(np.zeros((3,5)))
print()
print(np.zeros((2,4,5)))
print(np.ones((2,4,6)))

print(np.full((4,2,3),0))#it is used to print the given numbers
print(np.random.random((4,3,3)))

print(np.empty(5))#it will print the scientific values
print(np.empty((2,3)))
print(np.empty(((2,3,4))))

print(np.eye(3))#it will print identical matrix like it was used in matrix and data analysis
print(np.diag([3]))
print(np.diag([11,12,13]))

l1=[[2,4,5],[6,7,8]]
print(l1)
a=np.array(l1)
print(a)
a[0,0]=12
a[1,2]=20
print(a)'''
l=[[89,78,21],[11,121,4]]
c=np.array(l)
print(c)
print(c[::-1])
print(c[::-1,::-1])
print(c.ndim)# it will print the dimesional
print(c.size)# it will print the size
print(c.itemsize)#it will print the bit
print(c.nbytes)#it will print the bytes
print(c.shape)#it will print how many rows and columns



'''l1=[[2,4,5],[6,7,8],[111,121,131]]
print(l1)
a=np.array(l1)
print(a)
print()
a[::-1]
print(a)
'''
a=[[12,3,4],[2,3,4],[4,5,6]]
b=np.array(a)
print(a)
print(b)
arr1=np.random.randint(0,5,size=20)
print(arr1)
c=np.unique(arr1)
print(c)
c,count=np.unique(arr1,return_counts=True)
print(c)
print(count)