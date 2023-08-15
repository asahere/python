def words(num):
    word=num.split()
    return len(word)
x=input("Enter a Sentence:")
obj=words(x)
print("Number of words:",obj)
