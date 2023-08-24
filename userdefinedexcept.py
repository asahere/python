class InvalidRange(Exception):
        pass
try:
    marks=input('Enter the Numerator')
    result = int(marks)
    if(marks<0 or marks>100):
         raise InvalidRange
    print('Result=',marks)
except ValueError:
    print('Main Block:Invalid Input')
except InvalidRange:
    print('Main Block:Divide by Zero error')
