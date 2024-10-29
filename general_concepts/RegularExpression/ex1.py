import re #re in the regular expression
'''text='hello hi tata bye'
print(text)
a=re.findall("t",text)
print(a)
if len(a)==0:
    print("the letter is not  in the string")
else:
    print(f"the letter is  present number of times={len(a)}")
txt=" the python session starts at 10 am and end with 11am"
numberofnumber=re.findall("[0-9]",txt)
print(numberofnumber)
v=len(numberofnumber)
print(v)
phone="4379991294"
valid=re.findall("[6-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9][0-9]",phone)
print(valid)
if len(valid)==0:
    print('invallid')
else:
    print('valid no')

time="10 hi 23 and 73"
val=re.findall("[0-7][0-5]",time)
print(val)
c="SURESH K suresh k"
print(c)
numberofsmallalphabets=re.findall("[a-z]",c)
numberofcapalphabets=re.findall("[A-Z]",c)
print(numberofsmallalphabets)
print(numberofcapalphabets)
bothcapsmallalphabets=re.findall("[a-z]|[A-Z]",c)
print(bothcapsmallalphabets)'''
'''txt="Welcome come to my programming  world"
print(txt)
numberofword=re.split(" ",txt)
print(numberofword)

text="raining in spain"
firstspace=re.search("i",text)
print(firstspace)
print(firstspace.start())
print(firstspace.Match)'''
'''n='welcome to my world'
numbertosplit=re.split(' ',n,2)
print(numbertosplit)
'''
'''#replace
s='box is bigger and heaviear'
print(s)
replaceds=re.sub("box","fox",s)
print(replaceds)

t="The Welcome to Regular Expressionsis xyz"
print(t)
r=re.search(r"\bE\w+",t)
print(r.span())
print(r.string)
print(r.group())
print(t)
startingcheck=re.search("^The",t)
print(startingcheck)
endingcheck=re.search("The.* xyz$",t)
print(endingcheck)'''

st="hello world"
output=re.findall("he..o",st)
print(output)
output1=re.findall("he.*o",st)
print(output1)

output2=re.findall("he.{2}o",st)
print(output2)

output3=re.findall("a|e|i|o|u",st)#counting vowels in the words
print(output3)

str="the course starts at 9 am and end at as 11 am"
numberofdigits=re.findall("\d",str)
print(numberofdigits)

str="the course starts at 9 am and end at as 11 am"
numberofdigits=re.findall("\D",str)
print(numberofdigits)

#\b=find the word begining
#\w=to find untill need space is there
#\D=to find non-digit is the sentences
#^=beginning sentences
#$=ending sentences.