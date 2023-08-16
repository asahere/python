import re

s="cat bat sat pat mat rat"
x=re.findall("[scr]at",s)
print(x)