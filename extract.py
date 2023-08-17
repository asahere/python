import re
url="https://www.adithya sreejith25.com/hsf/hys/up/2003/10/02"
x=re.findall(r'\d\d\d\d/\d+/\d+',url)
print(x)