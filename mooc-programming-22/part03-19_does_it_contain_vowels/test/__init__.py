# Write your solution here
letter1 = "a"
letter2 = "e"
letter3 = "o"

while True:
    input_text = input("What are you looking for? ")
    if letter1 in input_text:
        print("a found")
    else:
        print("a not found")

    if letter2 in input_text:
        print("e found")
    else:
        print("e not found")

    if letter3 in input_text:
        print("o found")
    else:
        print("o not found")
    break