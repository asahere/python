def palindrome(s):
    return s == s[::-1]
def rep_palindrome(text):
    w=text.split()
    m=[]
    for w in w:
        if palindrome(w):
            m.append("@@@@@@@@@")
        else:
            m.append(w)
    return" ".join(m)
x="malayalam is my mother tounge"
output=rep_palindrome(x)
print(output)