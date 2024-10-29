#find the unique among both list
l1=[1,4,2,3,7]
l2=[4,2,19,7,1]
s=set(l1)
s1=set(l2)
s2=s.union(s1)
print(s2)
s3=list(s.union(s1))
print(s3)
#intercahnge the element in the list
l3=[[1,2,3,4],[7,8,9,10],[11,12,13,14]]
print(l3)
a=l3[0][1]
b=l3[0][2]
c=a
l3[0][1]=b
l3[0][2]=c
print(l3)
a=l3[1][1]
b=l3[1][2]
c=a
l3[1][1]=b
l3[1][2]=c
a=l3[2][1]
b=l3[2][2]
c=a
l3[2][1]=b
l3[2][2]=c
#changing in the inside the value in the list
l3[2][3]=100
print(l3)
#how to append the inside the list
l3[1].append(121)
l3.append([11,12,13,14,15])
print(l3)
#append in the dictionary
stud={'id':1,'name':'suresh','phone':9245799769,'location':'chennai',
      'course_taken':{
    'course_no1':1,'course_name1':'python','course_no2':2,'course_name2':'sql','status':'completed'
}}
stud['course_taken']['course_name1']='django'
stud['course_taken']['course_n04']=45
print(stud)
l4=[22,3,4,5,55,44,33,66,77,88,99,100,11,12,13]
print(l4[1])
print(l4[-5])#indexing values
print(l4[:])
print(l4[2:])
print(l4[:5])
print(l4[0:8])
print(l4[0:8:3])#third colon is the setvalues
print(l4)
print(l4[::-1])#reverse
l4.sort(reverse=True)
print(l4)