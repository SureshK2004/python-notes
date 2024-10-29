#how to ceate a empty class
class ab:
    pass
#if there is print statement inside class it will print all those statement.
class a:
    print('hello hi  tata bye')
    print('hello')
    b=-10
    print(b)

#how to print the dtatmember and class methods or member function
class sub:
    trainer="babu"
    course='python'
    def welcome_to_oops(self):
        print('Welcome')
a=sub()
print(a.trainer)#print(sub.trainer)
print(a.course)
a.welcome_to_oops()#sub.welcome_to_oops()


'''class Employee:
    company = 'Tutorial Gateway'

    def func_message(self):
        print('Welcome to Programming')


class Employee:
    company = 'Tutorial Gateway'


emp = Employee()
print(emp.company)

print("-------------")
print(Employee.company)

emp = Employee()
print(emp.company)
emp.func_message()

print("-------------")
print(Employee.company)
#print(Employee.func_message)'''


class Employee:
    company = 'Tutorial Gateway'

    def __init__(self):
        print('Hello World')

    def func_message(self):
        print('Welcome to Python Programming')


emp1 = Employee()  # Created an Instance

print(emp1.company)
emp1.func_message()


class Employee:
    company = 'Tutorial Gateway'

    def __init__(self, name, age, gender):
        print('hi')
        self.name = name
        self.age = age
        self.gender = gender

    def func_message(self):
        print('Welcome to Programming')

    def printmsg(self):
        print(f"{self.name},welcome to oops class and is age was={self.age} and gender was={self.gender}")


emp1 = Employee('Jack', 25, 'Male')
emp2 = Employee('Rose', 23, 'FeMale')

print(emp1.company)
emp1.func_message()
print(emp1.name)
print(emp1.age)
print(emp1.gender)
emp1.printmsg()
emp2.printmsg()
emp2.age=20
emp2.printmsg()