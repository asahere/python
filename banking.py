class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

class employee(person):
    def __init__(self,name,age,department):
        super().__init__(name,age)
        self.department = department

    def emp(self):
        print("Employee name is", self.name,"with age of",self.age,"and department is",self.department,"department" )

class customer(person):
    def __init__(self, name, age,des):
        super().__init__(name, age)
        self.des = des

    def cust(self):
        print ("customer Name is", self.name,"Age is",self.age,"and a", self.des,"customer")

x=employee('pyari', 45 , 'finance')
x.emp()
y=customer('bhavani', 40 , 'regular')
y.cust()