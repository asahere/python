def prime(num):#function declaration
#function definition
    count=0
    if num<=1:
        print ("not prime")
    for i in range(2,num+1):
        if num%i==0:
            count+=1
    if(count==1):
        return("prime")
    else:
        return("not prime")
n=int(input("enter a number:"))
print(prime(n))


