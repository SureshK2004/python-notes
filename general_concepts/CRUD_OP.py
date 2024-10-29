import mysql.connector
config = {
    'user': 'root',
    'password': 'suresh',
    'host': 'localhost',
    'database': 'python'
}
cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()


def readallstudent():
    sql="select * from student_python"
    cursor.execute(sql)
    output=cursor.fetchall()
    for a in output:
        print(a)

#readallstudent()

#value=int(input("enter the id:"))

def readsinglestudent(student_id):
    sql=f"select * from student_python where id={student_id}"
    cursor.execute(sql)
    output=cursor.fetchall()
    for a in output:
        print(a)
#readsinglestudent(value)

#value=int(input("enter the id:"))

def deletestuendt(student_id):
    sql=f"delete from student_python where id={student_id}"
    cursor.execute(sql)
    cnx.commit()
    cursor.close()

#deletestuendt(value)'''

def insertstuendt(id,name,mark1,mark2,mark3,gender,dob,location,coursetaken):

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
    print(id, name, mark1, mark2, mark3, total, average, grade)

    mysql = f"insert into student_python values({id},'{name}',{mark1},{mark2},{mark3},{total},{average},'{grade}','{gender}','{dob}','{location}','{coursetaken}')"
    cursor.execute(mysql)
    cnx.commit()
'''id=int(input("student_id"))
name= input("enter the name")
mark1=int(input("enter mark1"))
mark2=int(input("enter mark2"))
mark3= int(input("enter mark3"))
insertstuendt(id,name,mark1,mark2,mark3)'''

#update
def updatestuendt(id,name,mark1,mark2,mark3):

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
    #print(id, name, mark1, mark2, mark3, total, average, grade)

    mysql = f"update student_python set name='{name}',mark1={mark1} where id={id}"
    cursor.execute(mysql)# it is  used to insert,delete,update....
    cnx.commit()# it is  used to insert,delete,update....
'''id=int(input("student_id"))
name= input("enter the name")
mark1=int(input("enter mark1"))
mark2=int(input("enter mark2"))
mark3= int(input("enter mark3"))
updatestuendt(id,name,mark1,mark2,mark3)
'''



