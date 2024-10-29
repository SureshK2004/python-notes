class header():
    def __init__(self):
        print("""
        -------------------------------------------------------------
        --------------welcome to electricity board-------------------
        -------------------------------------------------------------
        """)
class footer():
    def __init__(self):
        print("""
        -------------------------------------------------------------
        -------------------------Thank you---------------------------
        ------------------pay on time to get connection--------------
        -------------------------------------------------------------
        """)
class billcalculation:
    def __init__(self,unit):
        self.unit=unit
    def billcal(self):
        print(f"number of units consumed={self.unit}")
        if self.unit<=100:
            charges=0.0
        elif self.unit<=200:
            charges=((100*0)+(self.unit-100)*2.25)
        elif self.unit<=400:
            charges=((100*0)+(100*2.25)+(self.unit-200)*4.50)
        elif self.unit<=500:
            charges=((100*0)+(100*2.25)+(200*4.5)+(self.unit-400)*6.00)
        else:
            charges=((100*0)+(300*4.5)+(100*6.00)+(self.unit-500)*8)
        print(f"bill amount ={charges}")
u=int(input("enter the no of units:"))
h=header()
b=billcalculation(u)
b.billcal()
f=footer()
