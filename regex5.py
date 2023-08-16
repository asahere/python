import re
s="abd abcd abccd abcccd"
x=re.findall("abc*d",s)
print(x)