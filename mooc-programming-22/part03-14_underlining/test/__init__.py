# Write your solution here
text = input("Please type in a string: ")

while text != "":
    print(text)
    print("-"*len(text))

    text = input("Please type in a string: ")
    if text == "":
        break