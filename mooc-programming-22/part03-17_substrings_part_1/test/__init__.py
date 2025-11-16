# Write your solution here
text = input("Please type in a string: ")
len_text = len(text)

index = 1

while index <= len_text:
    print(text[0:index])
    index += 1
