l=["a","e","i","o","u"]
k,a=" "
l2=[]
def remove_vowels():
    for i in range(0,len(l)):
        a=l[i]
        for j in range(0,len(a)):
            if a[j] not in "aeiou":
                k+=a[j]
        l2.append(k)
print(remove_vowels())
        
      