def long_word(num):
    words=num.split()
    lw=max(words,key=len)
    return lw
x=input("Enter a Sentence:")
obj=long_word(x)
print("Longest word:",obj)