'''#lambda to function possible
#function to lambda not possible
def hello():
    print('welcome to function')
hello()
#return
def helo():
    return "world"
a=helo()
print(a)
#args
def addtion(num1,num2):
    return num1//num2
b=addtion(94,3)
print(b)
#three args
def arithmaticop(symbol,num1,num2):
    if symbol  in['//','**','%']:
        return 'invalid operation'
    else:
        if symbol=='+':
            return f"addition of {num1}and{num2}={num1+num2}"
        elif symbol=='-':
            return f"subtraction of {num1}and{num2}={num1-num2}"
        elif symbol == '*':
            return f"multiplication of {num1}and{num2}={num1 *num2}"
        else:
            return f"division of {num1} and{num2 }={num1/num2} "
num1=int(input("enter the value:"))
num2=int(input("enter the value:"))
symbol=input("enter the symbol:")
c=arithmaticop(symbol,num1,num2)
print(c)'''
'''def sum(*nums):#non keyworc args(
    sum=0
    for a in nums:
        sum-=a
    return sum
b=sum('hello','world')
c=sum(20,3,9,5,4,3,2,6,8,9,18)
print(c)
print(b)'''
'''def str(*word):
    output=" "
    for a in word:
        output+=a
        output+="-"
    return output
a=str('hello','world','welcome','to','python')
print(a)'''
#-,--,---......
'''def str1(*word):
    output=" "
    c=1
    for a in word:
        output+=a
        if c==1:
            temp="-"*c
            output+=temp
            c+=1
        else:
            temp = "*" * c
            output += temp
            c += 1
    return output
a=str1('hello','world','welcome','to','python')
print(a)'''
'''def printmessage(**args):
    for a in args:
        print(a,args[a])
printmessage(id=1,name='suresh')'''
#function()
#(*args)-non-keywords
a2b=8888888

