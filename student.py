class student():
    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def display(self):
        print("Name=",self.name)
        print("Age=",self.age)
        print("Roll Number=",self.rollno)
        print("Mark=",self.mark)
    def set_age(self,age):
        self.age=age
    def set_marks(self,mark):
        self.mark=mark
name=input("Enter student name:")
rollno=int(input("Enter the Roll Number:"))
stud1=student(name,rollno)
age=int(input("Enter the age:"))
marks=float(input("Enter the total marks obtained:"))
stud1.set_age(age)
stud1.set_marks(marks)
stud1.display()



