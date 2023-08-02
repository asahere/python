class circle():
    def __init__(self,radius):
        self.radius=radius
    def getarea(self):
        return 3.14 * self.radius **2
    def getcircumference(self):
        return 2 * 3.14 * self.radius
radius=float(input("enter the radius "))
circle=circle(radius)
print("area is =",circle.getarea())
print("circumference is =",circle.getcircumference())


        