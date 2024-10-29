'''square_dict = dict()
for num in range(1, 11):
    square_dict[num] = num*num
print(square_dict)
# dictionary comprehension example
square_dict = {num: num*num for num in range(1, 11)}
print(square_dict)

 #item price in dollars
old_price = {'milk': 1.02, 'coffee': 2.5, 'bread': 2.5}

dollar_to_pound = 0.76
new_price = {item: value*dollar_to_pound for (item, value) in old_price.items()}
print(new_price)
print('_________________________________________')

d={}
for (item,value) in old_price.items():
    d[item]=value*dollar_to_pound
print(d)
print('_________________________________________')


original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}

even_dict = {k: v for (k, v) in original_dict.items() if v % 2 == 0}
print(even_dict)
print('_________________________________________')
d={}
for (k,v) in original_dict.items():
    if v % 2==0:
        d[k]=v
print(d)
print('_________________________________________')
original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}

new_dict = {k: v for (k, v) in original_dict.items() if v % 2 != 0 if v < 40}
print(new_dict)
original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}
print('_________________________________________')
b={}
for (k,v) in original_dict.items:
    if v%2!=0:
        if v<40:
            b[k]=v
print(b)
print('_________________________________________')
original_dict = {'jack': 38, 'michael': 48, 'guido': 57, 'john': 33}

new_dict_1 = {k: ('old' if v > 40 else 'young')
    for (k, v) in original_dict.items()}
print(new_dict_1)

print('_________________________________________')
c={}
for (k,v) in original_dict.items():
    if v>40:
        print('old')
    else:
        print('young')
print(c)
print('_________________________________________')
dictionary = {
    k1: {k2: k1 * k2 for k2 in range(1, 6)} for k1 in range(2, 5)
}
print(dictionary)
'''
print('_________________________________________')
'''o={}
for k1 in range(2,5):
    u={}
    for k2 in range(1,6):
        u[k2]=k1*k2
    o[k1]=u
print(o)
print('_________________________________________')

print=({ k1: {k2: k1 * k2 for k2 in range(1, 6)} for k1 in range(1,11)})
'''
#anonymous function
a=int(input("enter the number:"))
b=int(input("enter the number:"))
c=int(input("enter the number:"))
d=int(input("enter the number:"))
sum=a+b+c+d
average=sum/4
print(f"the average of {a},{b},{c},{d} is {average}")
