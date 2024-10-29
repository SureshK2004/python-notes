'''always key with some name in there means it will print only
lastest key'''
aadhar={'name':'suresh','phone':6379991294,'phone':9789848324}
print(aadhar)
print(dir(aadhar))
details=aadhar.copy()
print(details)
details.clear()
print(details)
print(aadhar.keys())
print(aadhar.values())
print(aadhar.items())
#nested dictionary
stud={'id':1,'name':'suresh','phone':9245799769,'location':'chennai',
      'course_taken':{
    'course_no1':1,'course_name1':'python','course_no2':2,'course_name2':'sql','status':'completed'
}
}
print(stud)
print(stud['course_taken'])
print(stud['course_taken']['course_name1'])
print(stud['course_taken']['status'])
print(stud.get('name'))
print(stud)
stud.popitem()
print(stud)
stud.pop('phone')
print(stud)
stud['phone']=989789667
print(stud)
#fromkeys
a=['a','e','i','o','u']
v=0
o=dict.fromkeys(a,v)
print(o)
#update
d={'id':1,'name':'suresh','salary':50000}
d1={'id':1,'name':'suresh','salary':45000,'phone':6379991294,'location':'mumbai'}
print(d)
print(d1)
d.update(d1)
print(d)
#set default
d1.setdefault('location','chennai')
print(d1)