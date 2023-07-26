x=int(input("Please enter a number:"))
n1=0
n2=1
sum=0
count=0
while True:
    if x>0:
        while (count<x+2):
            print(sum)
            count+=1
            n1=n2
            n2=sum
            sum=n1+n2
    else:
        print("Please enter a positive input!")
    break
