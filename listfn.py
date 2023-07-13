l=[]
print("Operations: \n1.Create a list \n2.Insert an element \n3.Delete an element \n4.Sort \n5.Exit")
ch=int(input("Enter the choice:"))
while True:
    if ch==1:
        create()
    elif ch==2:
        insert()
    elif ch==3:
        delete()
    elif ch==4:
        sort()
    else:
        Exit()
