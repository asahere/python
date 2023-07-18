def length():
    l=["asa","here","asahere"]
    l2=[]
    x=len(l)
    for i in range(len(l)):
        a=l[i]
        k=''
        for j in range(0,len(a)):
            if a[j] not in k:
                k+=a[j]
        l2.append(k)
    print(l2)
    t=l2[0]
    for p in range(0,len(l2)):
        if len(t)<=len(l2[p]):
            t=l2[p]
      print(t)
length()
        
            

                  
     

        
