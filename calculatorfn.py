print("Menu\n1.Add\n2.Subtraction\n3.Multiplication\n4.Division")
def sum(a,b):
    A=a
    B=b
print(sum)
def sub(a,b):
    A=a
    B=b
print(sub)
def mul(a,b):
    A=a
    B=b
print(mul)
def div(a,b):
    A=a
    B=b
print(div)
while True:
    ch=int(input("Enter the choice"))
    a=int(input("Enter the 1st number"))
    b=int(input("Enter the 2nd number"))
    if ch==1:
        sum(a+b)
    elif ch==2:
        sub(a-b)
    elif ch==3:
        mul(a*b)
    elif ch==4:
        div(a/b)
    elif ch==5:
        print("invalid choice")
        break


