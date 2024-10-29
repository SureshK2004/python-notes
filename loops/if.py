'''if 2:
    print('hello ')
if 7:
    print(14)
if -4:
    print(5)
if False:
    print(12)
if True:
    print(15)
if 0:
    print(8)#(0 and false )should not go inside the loop  because ''they are invalid key'''
'''a=int(input("enter the value:"))
b=int(input("enter the value:"))
if a>b:
    print(f"{a} is bigger than {b}")
else:
    print(f"{b} is bigger than {a}")'''
username=input("enter the username:")
password=input("enter the password:")
if username=="admin" and password== "admin":
    print("successful login")
elif username=="admin" and password!="admin":
    print("incorrect password")
elif username!="admin" and password=="admin":
    print("username incorrecet")
else:
    print("both are incorrect")
