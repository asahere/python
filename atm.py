bal=100 
def withdraw():
    bal=bal-a
    print("Current balance=",bal)
def deposit():
    bal=bal+b
    print("Current balance=",bal)
       
# bal=float(input("Enter the balance"))
while True:
 
    x=int(input("Enter a choice"))
    if x==0:
            a=int(input("Please enter the amount"))
            withdraw(bal,a)
    elif x==1:
            b=int(input("Please enter the amount"))
            deposit(bal,b)
    else:
        print("Wrong input")
        break

    




    
