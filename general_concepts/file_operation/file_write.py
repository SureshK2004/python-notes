#file modes write-w,read-r,append-a
import csv
import os# to check a file in this folder
f=os.path.isfile('student_out.csv')
print(f)
id=int(input("student_id"))
name= input("enter the name")
mark1=int(input("enter mark1"))
mark2=int(input("enter mark2"))
mark3= int(input("enter mark3"))
total = mark1+mark2+mark3
average=total/3
if total>=290:
    grade='a'
elif total <290 and total>=275:
    grade='b'
elif total<275 and total>=250:
    grade='c'
elif total<250 and total>=200:
    grade='d'
else:
    grade='e'
print(id,name,mark1,mark2,mark3,total,average,grade)
with open('student_out.csv','a',newline='') as file:
    if f:
        writer=csv.writer(file)
        #writer.writerow(['id','name','mark1','mark2','mark3','total','average','grade'])
        writer.writerow([id,name,mark1,mark2,mark3,total,average,grade])
    else:
        writer = csv.writer(file)
        writer.writerow(['id','name','mark1','mark2','mark3','total','average','grade'])
        writer.writerow([id, name, mark1, mark2, mark3, total, average, grade])
