'''they are three types of encapsulation:
1.public =eg.self.balance=balance
2.private=eg.__
3.protect=eg._'''
'''class encapsulation:
    def __init__(self,account_holder,balance=0):
        self.account_holder=account_holder
        self.__balance=balance #its a private variables
    def getbalance(self):
        return self.__balance
    def amountdepostie(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"deposited ₹{amount},new balance=₹{self.__balance}")
        else:
            print(f"amount cannot be an negative value")
    def withdraw(self,amount):
        if 0<amount<=self.__balance:
            self.__balance-=amount
            print(f"withdraw ₹{amount},new balance ₹={self.__balance}")
        else:
            print("Insufficient balance")
account=encapsulation('suresh',3000)
print(account.account_holder)
print(account.getbalance())
account.amountdepostie(500)
print(account.getbalance())
account.withdraw(100)
account.withdraw(1000)
print(account.getbalance())
account.withdraw(3500)'''

#protected examples
'''class encapsulation:
    def __init__(self,account_holder,balance=0):
        self._account_holder=account_holder #it is an protected variables
        self.__balance=balance #its a private variables
    def getbalance(self):
        return self.__balance
    def amountdepostie(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"deposited ₹{amount},new balance=₹{self.__balance}")
        else:
            print(f"amount cannot be an negative value")
    def withdraw(self,amount):
        if 0<amount<=self.__balance:
            self.__balance-=amount
            print(f"withdraw ₹{amount},new balance ₹={self.__balance}")
        else:
            print("Insufficient balance")
    def setaccountholder(self,new_accountholder):
        if new_accountholder:
            self._account_holder=new_accountholder
            print(f"accountholder changged to{self._account_holder}")
        else:
            print("Invalid account holder")
    def getaccountholder(self):
        return self._account_holder

account=encapsulation('suresh',3000)
print(account.account_holder)
print(account.getbalance())
account.amountdepostie(500)
print(account.getbalance())
account.withdraw(100)
account.withdraw(1000)
print(account.getbalance())
account.withdraw(3500)'''

class encapsulation:
    def __init__(self,accountholder,balance=0):
        self._accountholder=accountholder #it is a protected variable
        self.__balance=balance #it is a private variable
    def getbalance(self):
        return self.__balance
    def amountdeposit(self,amount):
        if amount>0:
            self.__balance+=amount
            print(f"deposited ${amount},newbalance=${self.__balance}")
        else:
            print(f"amount cannot be negative")

    def withdraw(self,amount):
        if 0<amount<=self.__balance:
            self.__balance-=amount
            print(f"withdraw ${amount},newbalance=${self.__balance}")
        else:
            print("insufficient fund")

    def setaccountholder(self,new_accountholder):
        if new_accountholder:
            self._accountholder=new_accountholder
            print(f"accountholder changed to {self._accountholder}")
        else:
            print("invaliad accountholder name")

    def getaccountholder(self):
        return self._accountholder

account=encapsulation('abc',70000)
a=account.getaccountholder()
print(a)
print(account.getbalance())
account.amountdeposit(500)
print(account.getbalance())
account.withdraw(100)
account.withdraw(1000)
print(account.getbalance())
account.withdraw(69000)
print(account.getbalance())
print("-----------------------")
account._accountholder='suresh'
o=account.getaccountholder()
print(o)
account.setaccountholder('VIP')
a=account.getaccountholder()
print(a)