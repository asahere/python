import re
s="asdas DFDSF trfhf hello_dEA_nDFSs"
x=re.findall(r'[a-z,A-Z,_]+$',s)
print(x)