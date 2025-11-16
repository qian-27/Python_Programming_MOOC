# Write your solution here
text = input("Please type in a string: ")
len_text = len(text)

index = len_text - 1

while index >= 0:
    print(text[index:])
    index -= 1
