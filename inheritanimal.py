class Animal:
    def __init__(self,name):
        self.name=name
class speak(Animal):
    def __init__(self,name):
        super().__init__(name)
    def sound(self):
        if self.name=='cat':
            print("meow...meow")
        elif self.name=='dog':
            print("bow...bow")
        elif self.name=='horse':
            print("neigh....neigh")
        else:
            print("wrong input")
n=input("Enter the name of the animal:")
s=speak(n)
s.sound()