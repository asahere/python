try:
    a=int(input('enter the first number'))
    b=int(input('enter the second number'))
    try:
        result=a/b
        print('result=',result)
    except:
        print('Divide by zero error')
except:
    print('Invalid Input')
finally:
    print("This code will run no matter what")
print("End of Program")