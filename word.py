import re
s = "Ameen ticca aabab"
x= re.findall(r'\ba\w.*b\b',s)
print(x)