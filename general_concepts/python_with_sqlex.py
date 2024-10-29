import mysql.connector
config = {
    'user': 'root',
    'password': 'suresh',
    'host': 'localhost',
    'database': 'python'
}
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

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

mysql=f"insert into student_python values({id},'{name}',{mark1},{mark2},{mark3},{total},{average},'{grade}')"
cursor.execute(mysql)

cnx.commit()

cursor.close()