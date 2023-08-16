import re
s="abd abcd abccd abcccd"
x=re.findall("ab.{3}d",s)
print(x)