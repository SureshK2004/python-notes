'''comphersion-----------
* converting multiple line of code into single line
* always run faster than normal code
* list,dict,set'''
l=[]
for a in range(1,11):
    l.append(a**2)
print(l)
print('_________________')

o=[a**2 for a in range(1,11)]
print(o)
print('_________________')

ol={a:a**2 for a in range(1,11)}
print(ol)
print('_________________')

os={a**2 for a in range(1,11)}
print(os)

v=[]
for a in range(1,15):
    if a%2:
        v.append(a)
print(v)

print([a for a in range(1,20) if a%2])

d=dict()
for a in range(1,15):
    if a%2:
        d[a]='odd'
print(d)

print({a:'odd' for a in range(1,15) if a%2})
#two range for comphrension
c=[]
for a  in range(1,5):
    for b in range(1,5):
        c.append(a*b)
    print()
print(c)

print([a*b for a in range(1,5) for b in range(1,5)])

o=[]
for a in range(1,5):
    if a%2:
        o.append('odd')
    else:
        o.append('even')
print(o)

print(['odd' if a%2 else 'even' for a in range(1,10)])

d=dict()
for i in range(1,10):
    if a%2:
        d[a]='odd'
    else:
        d[a]='even'
print(d)

print({a:'odd' if a%2 else 'even' for i in range(1,10)})#for dictionary comphrension