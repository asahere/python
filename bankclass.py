class bank:
    def __init__(self,a,b,c):
        self.name=a
        self.account_number=b
        self.balance=c
    def deposit(self,amt):
        self.amount=amt
        self.amt=self.balance+self.amount
    def withdraw(self,amt2):
        if amt2>self.balance:
            print("Insufficient Balance!!!")
        else:
            self.amount2=amt2
            self.amt2=self.balance-self.amt2
    def bal(self):
        print("Balance=",self.balance)
name=input("Please enter your name:")
account_number=int(input("Please enter your account number:"))
balance=int(input("Please enter your current balance:"))
n=int(input("Please select your choice:"))
if n==0:
    amt=int(input("Enter the amount:"))
    amt1=bank(name,account_number,balance)
    print("Your current balance=",amt1.deposit(amt))
elif n==1:
    amt2=int(input("Enter the amount:"))
    amt3=bank(name,account_number,balance)
    print("Your current balance=",amt3.withdraw(amt2))
elif n==3:
    print("Your current balance=",bal())
else:
    print("Wrong choice!!!")

