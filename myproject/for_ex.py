'''for a in range(1,6):
    if a in[4,5]:
        for b in range(1,6):
            if b in[1,5]:
                print("*",end=" ")
            else:
                print(" ",end=" ")
        print()
    elif a in[3]:
        for b in range(1,6):
            if b in[1,2,3,4,5]:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    elif a in[2]:
        for b in range(1,6):
            if b in[1,5]:
                print("*",end=" ")
            else:
                print(" ",end=' ')
        print()
    elif a in[1]:
        for b in range(1,6):
            if b in[3]:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()'''
for a in range(1,7):
    if a in[1,3]:
        for b in range(1,5):
            if b in[1,2,3,4]:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
    elif a in[1,2,3,4,5,6]:
        for b in range(1,5):
            if b in[1]:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()
