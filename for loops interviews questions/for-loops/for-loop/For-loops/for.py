#for loop print in the same line
# n=int(input("enter:"))
# for i in range(n):
#     print(i,end=" ")

#box model pattern in for loop
# n=int(input("enter the number:"))
# for i in range(n):
#         print(str(n)* n)
        
#box middle space pattern
# n=int(input("enter the no:"))
# for a in range(n):
#         for  b in range(n):
#                 if a==0 or a==n-1 or b==0 or b==n-1:
#                         print("*",end=" ")
#                 else:
#                         print(" ",end=" ")
#         print()

#triangle pattern
# n=int(input("enter the no:"))
# for i in range(n):
#         print(str(i)*i)

# star triangle pattern
# n=int(input("enter the no:"))
# for i in range(n+1):
#         print("*"*i)
        
#reverse triangle


#star patter between space
# n=int(input("enter the number:"))
# for i in range(n):
#     for h in range(i+1):
#         if h==0 or i==h or i==n-1:
#             print("X",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#pattern between space in string
# n=int(input("enter the number:"))
# for i in range(n):
#     for h in range(i+1):
#         if h==0 or i==h or i==n-1:
#             print(str(i),end=" ")
#         else:
#             print(" ",end=" ")
#     print()

#straight triangle
# n=9
# for a in range(1,n+1):
#     print(" "*(n-a)+"* "*a)


#to print the left triangle alphabets in loop:
# n=int(input("enter the number:"))
# for i in range(n,0,-1):
#     print(" "*(n-1),end=" ")
#     for j in range(i):
#         print(chr(65+j),end=" ")
#     print()

# to print my loop 1010101 in loop:
# n=int(input("enter the number:"))
# for i in range(1,n+1):
#     for j in range(i):
#         print((i+j)%2,end=" ")
#     print()

#to print the rights triangle alphabets in loop:
# n=int(input("enter:"))
# for i in range(1,n+1):
#     for j in range(i):
#         print(chr(65+j),end=" ")
#     print()
      
#to print a right triangle i
# increment methods in the loop 
# n=int(input("enter:"))
n=6
for i in range(1,n+1):
    for j in range(1,i+1):
        print(j,end=" ")
    print()    
     
