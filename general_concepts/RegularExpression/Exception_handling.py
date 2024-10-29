#try(yes)->except->else(yes)->finally(yes)
#try(no)->except(yes)->else(no)->finally(yes)
#exceptional handling are mainly used to handle exception which occured in the program
#exception handling are mainly used for smoother execution
'''
various exception handling types
1.ZeroDivisionError
2.NameError
3.IndexError
4.ModuleNotFoundError
5.KeyError
6.TypeError
7.AttributeError
8.FileNotFoundError

a=10
b=0
l=[1,2,3,4,5]
d={"name":'suresh','age':21}
name="abc"
d=5
open('xyz.txt')'''
try:
    a=10
    b=20
    print(a/b)
except ZeroDivisionError:
    print('number cannot be divisible by zero')
else:
    print("i will print only when try executed successfully")
finally:
    print("i will always print the statement")
print()

try:
    a=20
    b='hello'
    print(a+5)
    print(str(a)+b)
except(NameError,TypeError):
    print("either variable is not defiend or two different data types are used together")
else:
    print("i will print only when try executed successfully")
finally:
    print("i will always print the statement")

