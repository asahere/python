def extract_uppercase_words(sentence):
    words = sentence.split()
    uppercase_words= [word for word in words if word[0].isupper()]
    return uppercase_words

user_input = input("enter a sentence: ")
uppercase_words = extract_uppercase_words(user_input)
print("words starting with an uppercase character:", uppercase_words)
