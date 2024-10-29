'''l=[1,2,3,4,5,6,]
l1=['a','b','c','d','e','f']
print(l)
print(l1)
o=zip(l,l1)
print(o)
#print(list(o))
#print(set(o))
print(dict(o))#tuple can't work in thse zip'''
'''________________________________________________
day=[0,1,2,3,4]
name=['sunday','monday','tuesday','wednesday','thursday']
s_name=['eng','mat','tamil','science','socail']
a=set(zip(day,name,s_name))#------------suppose dict can use pairs only output.it because as an key value pair.
# it can't three values paris---------')
print(a)
#unzip
statepincode=[('tnagar',600010),('kknagar',600031),('cnagar',600091)]
print(statepincode)
state,pincode=zip(*statepincode)
print(state)
print(pincode)
day,name,s_name=zip(*a)
print(day)
print(name)
print(s_name)'''
from function import *
print(a2b)