print("1.Create\n2.Deposit\n3.Withdraw\n4.Show balance\n5.Exit")
l=[]
ch==int(input("Enter the choice"))
while True:
    if ch==1:
        account=create.accnt()
        l.append(account)
    elif ch==2:
        pin=int(input("Enter pin:"))
        for i in l:
             if i.m==pin:
                 amt=int(input("enter amount:"))
                 i.deposit(amt)
    def create_accnt():
        
    class bank:
        def __init__(self,n,m,bal):
            self.name=n
            self.accno=m
            self.bal=bal

    