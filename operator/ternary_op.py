a=7
b=13
print("a is bigger" if a>b else"b is bigger")

a=10
print("even" if a%2==0 else"odd")

a=20
print("divisible by 2 and 3"if a%2==0 and a%3==0 else "divisible by3")

a=21
print("divisible by 2 and 3"if a%2==0 and a%3==0 else "divisible by 3" if a%3==0 else "non divisible by 3")