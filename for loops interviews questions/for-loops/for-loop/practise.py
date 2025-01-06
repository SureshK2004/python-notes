#star patter between space
# n=int(input("enter the number:"))
# for i in range(n):
#     for h in range(i+1):
#         if h==0 or i==h or i==n-1:
#             print("X",end=" ")
#         else:
#             print(" ",end=" ")
#     print()

# n=5
# for i in range(1,n+1):
#     print(" "*(n-i)+"* "*i)

# for j in range(20):
#     print(chr(65+j),end=" ")

n=6
for i in range(n,0,-1):
    print(" "*(n-i),end=" ")
    for j in range(i):
        print(chr(j+1),end=" ")
    print()
#output
#  ☺ ☻ ♥ ♦ ♣ ♠ 
#   ☺ ☻ ♥ ♦ ♣ 
#    ☺ ☻ ♥ ♦
#     ☺ ☻ ♥
#      ☺ ☻
#       ☺
n=5
for i in range(n,0,-1):
    print(" "*(n-i),end=" ")
    for j in range(i):
        print(chr(65+j),end=" ")
    print()