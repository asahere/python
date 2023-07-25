def sum_list():
    num=[]
    n=int(input("Enter number:"))
    for i in range(3):
        num.append(n)
    
    sum_sqr=0
    for n in num:
        sum_sqr+=n**2

    print(f"The sum of squaresis",sum_sqr)
sum_list()