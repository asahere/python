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
l=[]
while True:
    print("1.Create\n2.Deposit\n3.Withdraw\n4.Show balance\n5.Exit")
    name=input("Please enter your name:")
    account_number=int(input("Please enter your account number:"))
    balance=int(input("Please enter your current balance:"))
    amt1=bank(name,account_number,balance)
    ch=int(input("Enter the choice"))
    if ch==1:
        account=create.accnt()
        l.append(account)
    elif ch==2:
        pin=int(input("Enter pin:"))
        for i in l:
             if i.m==pin:
                 amt=int(input("enter amount:"))
                 i.deposit(amt)

    