def split(str):
    result=[]
    counta=0
    countb=0
    str2=""
    for char in str:
        if char=='A':
            counta+=1
            str2+=char
        elif char=='B':
            countb+=1
            str2+=char

        if counta==countb:
            result.append(str2)
            str2=""
    
    print(result)
a=input("Enter a string")
split(a)
    
   


