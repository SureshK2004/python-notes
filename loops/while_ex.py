'''#while loop vs for loop
1 Iterattive
2 for endpoint shared know first travel for first 100 kilometres
#while
    * Run until conditon get satisy
    *Travel until destination is reached.
    *for--->while its possible conversion.
    *while-->for its not possible conversion.
    '''
'''i=1
while(i<=10):
    print(i)
    i+=1'''
#while
'''a=1
while(a<=9):
    b=1
    while(b<=9):
        print(a*b,end=" ")
        b+=1
    print()
    a+=1'''
'''a=1
while(a<=5):
    b=1
    while(b<a+1):
        print(b,end=" ")
        b+=1
    print()
    a+=1'''
from new_symbols import *
flag=True
while(flag):
    n=int(input("enter the no to guess"))
    if n==numbertoguess:
        print("u have identify number to guess")
        flag=False
    elif n<numbertoguess:
        print(" u have enter samll number")
    else:
        print("u have entered bigger number")