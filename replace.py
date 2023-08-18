import re
text = """ keep the blue flag\nflying high"""
x= re.sub("\n"," ",text)
print(x)