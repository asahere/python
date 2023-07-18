def character(str, char_find):
    count=0
    for char in str:
        if char == char_find:
            count += 1
    return count
str1 =  input("enter a string: " )
char1  = input("enter the character to find occurrences for: ")
count=character(str1,char1)
print("the character",char1,"has",count,"appearences in the string")
 