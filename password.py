import re
s=input("Enter a password(min 8 characters):")
x=re.search(r'^[a-z A-Z]+[0-9]+[_!@#$%^&*(),.?":{}|<>$]?',s)
if len(s)>=8:
    print("Your password is valid")
else:
    print("Invalid Password!!!")
