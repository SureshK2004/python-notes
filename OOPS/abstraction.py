from abc import ABC,abstractmethod
class shape(ABC):
    @abstractmethod
    def volume(self):
        pass
class square(shape):
    def __init__(self,a):
            self.a=a
    def volume(self):
            print(f"volume of the square {self.a**2}")
class rectangle(shape):
    def __init__(self,l,b):
            self.l=l
            self.b=b
    def volume(self):
            print(f"volume of the rectangel{self.l*self.b}")
s=square(4)
r=rectangle(2,4)
for a in (s,r):
    a.volume()

