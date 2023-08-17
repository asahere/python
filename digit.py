import re
s="1 12 123 1567 14321"
x=re.findall(r'\d\d\d+',s)
print(x)