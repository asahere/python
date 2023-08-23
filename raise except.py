def divide(a,b):
    try:
        res=a/b
        return res
    except ZeroDivisionError:
        print('Divide Function:Divide by Zero Error')
        return 0
try:
    a=int(input('Enter the Numerator'))
    b=int(input('Enter the Denominator'))

    result = divide(a,b)
    print('Result=',result)
except ValueError:
    print('Main Block:Invalid Input')
except ZeroDivisionError:
    print('Main Block:Divide by Zero error')

print('End of Program')


