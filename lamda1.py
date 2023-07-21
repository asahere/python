def factorial(n):
    if n<0:
        return None
    elif n==0:
        return 1
    else:
        return reduce(lambda x,y:x*y,range(1,n+1))

num=int(input("Enter a number to calculate its factorial:"))
result=factorial(num)
 