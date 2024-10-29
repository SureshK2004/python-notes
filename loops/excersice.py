'''n=int(input("enter the  amstrong number:"))
sumofdigit=0
for a in str(n):
    sumofdigit+=int(a)**(len(str(n)))
if n== sumofdigit:
    print("its a amsytrong number")
else:
    print("its not a amstrong number")'''
#palindrome
'''a=input("enter the string to chenck :")
print(a)
reverse_string=(a[::-1])
if a==reverse_string:
    print("its a palindrom")
else:
    print("its not  a palindrome")'''

'''a=int(input("enter the value:"))
sum_of_digit=0
for x in str(a):
    sum_of_digit+=int(x)
    #print(sum_of_digit)
print(sum_of_digit)'''
c=int(input("enter the number :"))
if c>1:
   for i in range(2,(c//2)+1):
       if(c%i)==0:
           print(c,"is not a prime number")
           break
   else:
           print(c,'is  a prime number')
else:
    print("its not a prime number")
