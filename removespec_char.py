def special(str):
    str2=""
    list=[",",".","/",";",":","<",">","?","!","@","#","$","%","^","&","*"]
    for i in range(len(str)):
        if str[i] not in list:
            str2+=str[i]
    print("The output is:",str2)
name=input("Enter string with special characters:")
special(name)