class temperature():
    def __init__(self,temp):
        self.temp=temp
    def confahrenheit(self):
        self.fah=(self.temp-32)*5/9
        return self.fah
    def concelsius(self):
        self.cel=(self.temp*9/5)+32
        return self.cel
temp=float(input("enter the temp "))
temperature=temperature(temp)
print("Fahrenheit is =",temperature.confahrenheit())
print("Celsius is =",temperature.concelsius())