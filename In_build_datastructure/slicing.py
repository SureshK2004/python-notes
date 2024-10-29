a=[12,233,34,45,56]
print(a)
print(a[3])
print(a[:4])
print(a[2:])
print(a[2:4])
print(a[2:-2])
print(a[-2:-2])

#inbuild function
print(sum(a))
print(max(a))
print(min(a))
print(len(a))
print(dir(a))#To find the function in the list (dir is used to all the function)

l4=[]
l4.append(24)
l4.append(12)
l4.insert(0,111)
l3=[1,2,3]
l4.extend(l3)
print(l4)
l4.pop()
l4.remove(111)
print(l4)
l3=l4.copy()
print(l3)
l3.clear()
print(l3)
l5=[11,12,11,13,14,11,12,15]
print(l5.count(11))
print(l5.count(12))
l2=[2,3,5,7,8]
l2.sort()
print(l2)
l2.reverse()
print(l2)
print(l2[2])
print(l2.index(3))

b=['apple','grapes',"orange","bllueberry"]
print(max(b))
print(min(b))