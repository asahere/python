a=[]
print("Enter an integer")
while True:
    list1=input()
    if list1:
        a.append(list1)
    else:
        break
print(a)
b=a[0]
for i in range(len(a)):
    if b<=a[i]:
        b=a[i]
print("The largest integer is:",b)
