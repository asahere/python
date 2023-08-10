class shape:
    def __init__(self,color):
        self.color = color

class circle(shape):
    def __init__(self,color,radius):
        super().__init__(color)
        print("Area of circle=",3.14*radius**2)
    
class square(shape):
    def __init__(self,color,side_length):
        super().__init__(color)
        print("Area of square=",side_length**2)
obj1=circle("Red",5)
obj2=square("Blue",4)

