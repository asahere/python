import os
while True:
    ch=input("Enter a choice from c=create,r=read,w=write,a=append,d=delete:")
    if ch=='c':
        n=input("Enter a name of the file to be created:")
        f=open(n,"x")
        print("File created successfull")
    elif ch=='w':
        c=input("Enter the content:")
        f=open(n,"w")
        f.write(c)
    elif ch=='r':
        f=open(n,"r")
        print(f.read())
    elif ch=='a':
        c=input("Enter the content you want to add:")
        f=open(n,"a")
        f.write(c)
    elif ch=='d':
        f.close()
        if os.path.exists(n):
            os.remove(n)
            print("File Successfully deleted")
            break
        else:
            print("The file does not exist!!!")
    else:
        print("Please choose from the above given options!!")
  
