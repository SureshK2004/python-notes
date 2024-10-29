import re

txt="Python is an interpreted, object-oriented, high-level programming language with dynamic semantics. Its high-level built in data structures, combined with dynamic typing and dynamic binding, make it very attractive for Rapid Application Development, as well as for use as a scripting or glue language to connect existing components together."
print(txt)
numberofwords=re.split(" ",txt)
print(numberofwords)
v=len(numberofwords)
print(v)
unique=set(numberofwords)
print(unique)
s=len(unique)
print(s)
output=dict()
for a in numberofwords:
    if a in output:
        output[a]+=1
    else:
        output[a]=1
    print(output)
print(output)