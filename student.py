class student():
    def __init__(self,name,age,rollnumber,mark):
        self.name=name
        self.rollnumber=rollnumber 
        self.age=age
        self.mark=mark
    def display(self):
        print("Name=",self.name)
        print("Age=",self.age)
        print("Roll Number=",self.rollnumber)
        print("Mark=",self.mark)
    def student_age(self):
