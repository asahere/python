class shape:
    def __init__(self,color):
        self.color = color

class circle(shape):
    def __init__(self,color):
        super().__init__(color)
        self.radius = radius

    def calculate_area(self):
        return 3.14*self.radius*self.radius
    
class square(shape):
    def __init__(self,color,side):
        super().__init__(color)
        self.side = side

    def calculate_area(self):
        return self.side * self.side
circle=shape.circle("Red",5)
square=shape.square("Blue",4)
print("Circle Area:",circle.calculate_area())
print("Square Area:",square.calculate_area())