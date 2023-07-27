list=[3,8,12,7,6,10,21,15]
c=int(len(list))
for i in range(c):
    for n in range(i+1,c):
        sum=list[i]+list[n]
        if(sum==18):
            print(list[i],list[n],"is a pair whose sum is 18")
    
        



    