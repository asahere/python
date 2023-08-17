import re
txt="The quick brown frog jumps over the lazy dog"
x=re.findall("^The.*dog$",txt)
print(x)