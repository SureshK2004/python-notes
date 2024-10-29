import csv
import os
b=os.path.isfile('student_mul.csv')
print(b)
n=int(input("enter the no of the student: "))
student_list=[]
for a in range(n):
    tempst=[]
    id = int(input("student_id"))
    name = input("enter the name")
    mark1 = int(input("enter mark1"))
    mark2 = int(input("enter mark2"))
    mark3 = int(input("enter mark3"))
    total = mark1 + mark2 + mark3
    average = total / 3
    if total >= 290:
        grade = 'a'
    elif total < 290 and total >= 275:
        grade = 'b'
    elif total < 275 and total >= 250:
        grade = 'c'
    elif total < 250 and total >= 200:
        grade = 'd'
    else:
        grade = 'e'
    tempst.append(id)
    tempst.append(name)
    tempst.append(mark1)
    tempst.append(mark2)
    tempst.append(mark3)
    tempst.append(total)
    tempst.append(average)
    tempst.append(grade)
    student_list.append(tempst)
    print(student_list)
with open('student_mul.csv','a',newline='') as file:
    if b:
        writer=csv.writer(file)
        writer.writerows(student_list)
    else:
        writer=csv.writer(file)
        writer.writerow(['id','name','mark1','mark2','mark3','total','average','grade'])
        writer.writerows(student_list)


