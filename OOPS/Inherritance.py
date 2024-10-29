'''#single inheritance

class father():
    def __init__(self,fname,fage,flocation):
        self.fname=fname
        self.fage=fage
        self.flocation=flocation
    def printfather(self):
        return f"Fathername {self.fname}and is age {self.fage}and is from {self.flocation}"

class son(father):
    def __init__(self,fname,fage,flocation,sname,sage,slocation):
        father.__init__(self,fname,fage,flocation)
        self.sname=sname
        self.sage=sage
        self.slocation=slocation
    def printson(self):
        return f"Sonname {self.sname} and is age {self.sage} and is from {self.slocation}"
f=father('Raja','55','kovilpatti')
o=f.printfather()
s=son('Raja','55','kovilpatti')
p=s.printson()
print(o)
print(p)
s1=son('Raja','55','kovilpatti','Alwin','22','kovilpatti')
o1=s1.printfather()
o2=s1.printson()
print(o1)
print(o2)'''

#multilevel inheritance
'''class gfather():
    def __init__(self,gfname,gfage,gflocation):
        self.gfname=gfname
        self.gfage=gfage
        self.gflocation=gflocation
    def gfatherprint(self):
        return f"grandFathername {self.gfname}and is age {self.gfage}and is from {self.gflocation}"

class father(gfather):
    def __init__(self,gfname,gfage,gflocation,fname,fage,flocation):
        gfather.__init__(self,gfname,gfage,gflocation)
        self.fname=fname
        self.fage=fage
        self.flocation=flocation
    def printfather(self):
        return f"Fathername {self.fname}and is age {self.fage}and is from {self.flocation}"

class son(father):
    def __init__(self,gfname,gfage,gflocation,fname,fage,flocation,sname,sage,slocation):
        father.__init__(self,gfname,gfage,gflocation,fname,fage,flocation)
        self.sname=sname
        self.sage=sage
        self.slocation=slocation

    def sonprint(self):
        return f"sonname {self.sname}and is age {self.sage}and is from {self.slocation}"
s2=son('sarangan',82,'vandlaur','kumar',52,'tambaram','suresh',21,'vandalur')
o3=s2.gfatherprint()
print(o3)
o3=s2.printfather()
print(o3)
o4=s2.sonprint()
print(o4)
'''
#multiple inheritance
'''class father():
    def __init__(self,fname,fage,flocation):
        self.fname=fname
        self.fage=fage
        self.flocation=flocation
    def printfather(self):
        return f"Fathername {self.fname}and is age {self.fage}and is from {self.flocation}"
class mother():
    def __init__(self,mname,mage,mlocation):
        self.mname=mname
        self.mage=mage
        self.mlocation=mlocation
    def printmother(self):
        return f"mothername {self.mname}and is age {self.mage}and is from {self.mlocation}"

class son(father,mother):
    def __init__(self,fname,fage,flocation,mname,mage,mlocation,sname,sage,slocation):
        father.__init__(self, fname, fage, flocation)
        mother.__init__(self, mname, mage, mlocation)
        self.sname=sname
        self.sage=sage
        self.slocation=slocation
    def printson(self):
        return f"sonname {self.sname}and is age {self.sage}and is from {self.slocation}"

c1=son('kumar',52,'vandalur','prabha',38,'meenambakkam','suresh',21,'vandalur')
a=c1.printson()
a1=c1.printfather()
a2=c1.printmother()
print(a)
print(a1)
print(a2)

#hierachical inheritance
class family():
    def __init__(self,fname,surname,origin):
        self.fname=fname
        self.surname=surname
        self.origin=origin
    def printfamily(self):
        return f"Familyname {self.fname}and surname is {self.surname}and origin is from {self.origin}"

class son1(family):
    def __init__(self,fname,surname,origin,s1name,s1age,s1location):
        family.__init__(self,fname,surname,origin)
        self.s1name=s1name
        self.s1age=s1age
        self.s1location=s1location
    def printson1(self):
        return f"son1name {self.s1name}and is age {self.s1age}and is from {self.s1location}"

class son2(family):
    def __init__(self,fname,surname,origin,s2name,s2age,s2location):
        family.__init__(self, fname, surname, origin)
        self.s2name=s2name
        self.s2age=s2age
        self.s2location=s2location
    def printson2(self):
        return f"son2name {self.s2name}and is age {self.s2age}and is from {self.s2location}"
f=son1('abc',60,'tambaram','xyz',40,'vandalur')
f1=son2('harish',76,'chennai','vani',39,'salem')
p=f.printfamily()
p1=f.printson1()
b=f1.printfamily()
b2=f1.printson2()
print(b)
print(b2)
print(p)
print(p1)
'''
#hybrid inheritan:
class gfather():
    def __init__(self,gfname,gfage,gflocation):
        self.gfname=gfname
        self.gfage=gfage
        self.gflocation=gflocation
    def printgfather(self):
        return f"grandFathername {self.gfname}and is age {self.gfage}and is from {self.gflocation}"

class father(gfather):
    def __init__(self,gfname,gfage,gflocation,fname,fage,flocation):
        gfather.__init__(self,gfname,gfage,gflocation)
        self.fname=fname
        self.fage=fage
        self.flocation=flocation
    def printfather(self):
        return f"Fathername {self.fname}and is age {self.fage}and is from {self.flocation}"

class mother():
    def __init__(self,mname,mage,mlocation):
        self.mname=mname
        self.mage=mage
        self.mlocation=mlocation
    def printmother(self):
        return f"mother is {self.mname} and is age ={self.mage} and is from={self.mlocation}"

class son(father,mother):
    def __init__(self,gfname,gfage,gflocation,fname,fage,flocation,mname,mage,mlocation,sname,sage,slocation):
        father.__init__(self, gfname,gfage,gflocation,fname, fage, flocation)
        #gfname.__init__(self,gfname,gfage,gflocation)
        mother.__init__(self, mname, mage, mlocation)
        self.sname=sname
        self.sage=sage
        self.slocation=slocation
    def printson(self):
        return f"soname is={self.sname}and is age={self.sage}and is from={self.slocation}"
x=son('saragan',82,'saidapet','kumar',52,'tambaram','prabha',40,'madurai','dhoni',21,'jaipur')
p=x.printgfather()
p1=x.printfather()
p2=x.printmother()
p3=x.printson()
print(p)
print(p1)
print(p2)
print(p3)







