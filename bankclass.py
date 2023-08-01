class bank:
    def __init__(self,a,b,c):
        self.name=a
        self.account_number=b
        self.balance=c
    def deposit(self,amt):
        self.amount=amt
        self.amt=self.balance+self.amount
        return self.amt
    def withdraw(self,amt):
        if amt>self.balance:
            print("Sorry,insufficient Balance!!!")
        else:
            self.amount2=amt
            self.amt=self.balance-self.amount2
            return self.amt
    def bal(self):
        print("Balance=",self.balance)
name=input("Please enter your name:")
account_number=int(input("Please enter your account number:"))
balance=int(input("Please enter your current balance:"))
amt1=bank(name,account_number,balance)
n=int(input("Please select your choice:"))
if n==0:
    amt=int(input("Enter the amount:"))
    amt1.deposit(amt)
elif n==1:
    amt=int(input("Enter the amount:"))
    #amt3=bank(name,account_number,balance)
    amt1.withdraw(amt)
elif n==3:
    amt1.bal()
else:
    print("Wrong choice!!!")

