import re
s = "altaza,zedone,orane,track"
x=re.findall("[z]\w*",s)
print(x)