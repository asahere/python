def initials(name):
    words = name.split()
    words = [word.capitalize() for word in words]
    cap_name = " ".join(words)
    return cap_name


name = input("enter your name: ")
cap_name = initials(name)
print("Name with initials:", cap_name)