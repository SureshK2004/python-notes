# n=int(input("enter the number:"))
# for a in range(1,n):
#     print(a,end=" ")
#     n+=1
# print() #output: 1 2 3 4 5 ...........

# n=int(input("enter the number:"))
# for a in range(1,n):
#     print("*"*a)
#     n+=1
# print() 
 #output:
                #  *
                #  **
                #  ***

# n=int(input("enter the number:"))
# for a in range(1,n):
#     print(str(a)*a)
#     n+=1
# print()

#output:
# enter the number:7
# 1
# 22
# 333
# 4444
# 55555
# 666666

n=int(input("enter ther number:"))
for a in range(n,0,-1):
    print("*"*a)
print()
#output
# *****
# ****
# ***
# **
# *

n=int(input("enter:"))
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()
#output:
# enter:5
# 1 
# 1 2
# 1 2 3
# 1 2 3 4
# 1 2 3 4 5