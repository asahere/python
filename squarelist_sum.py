def sum_list():
    num=[]
    for i in range(3):
        n=int(input(f"Enter number{i+1}:"))
        num.append(n)
    
    sum_sqr=0
    for n in num:
        sum_sqr+=n**2

    print("The sum of squaresis",sum_sqr)
sum_list()