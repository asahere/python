import re
x=r"^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9.+_-]+\.[a-zA-Z]{2,}$"
email="asa.arsha@gmail.com"
match=re.match(x,email)

if match:
    print(email," is valid.")
else:
    print(email," is not valid.")