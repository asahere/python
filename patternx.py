n=int(input("Enter a limit:"))
a="*"
print(a)
for i in range(1,n+1):
    print(a,end="")
    for j in range(1,i+1):
        print(j,end="")
    for j in range(i-1,0,-1):
        print(j,end="")
    print(a,end="")
    print()
for i in range(n-1,0,-1):
    print(a,end="")
    for j in range(1,i+1):
        print(j,end="")
    for j in range(i-1,0,-1):
        print(j,end="")
    print(a,end="")
    print()
print(a)

    
