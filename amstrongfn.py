def armstrong(number):
    sum=0
    rem=0
    num=number
    while num>0:
        rem=num%10
        sum=sum+rem**3
        num//=10
    if sum==number:
        print("It is an amstrong number")
    else:
        print("It is not an amstrong")
a=int(input("Enter a number"))
armstrong(a)