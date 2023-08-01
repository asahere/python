
class calc:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b
    def add(self):
        self.sum=self.num1+self.num2
        return self.sum
    def sub(self):
        self.min=self.num1-self.num2
        return self.min
    def mul(self):
        self.multi=self.num1*self.num2
        return self.multi
    def div(self):
        self.division=self.num1/self.num2
        return self.division
n=int(input("Enter a choice:"))
if(n==0):
    a=calc(20,10)
    print(a.add())
elif(n==1):
    sub1=calc(20,10)
    print("Substraction=",sub1.sub())
elif(n==2):
    mul1=calc(20,10)
    print("Multiplication=",mul1.mul())
elif(n==3):
    div1=calc(20,10)
    print("Division=",div1.div())
else:
    print("Wrong choice vro")


