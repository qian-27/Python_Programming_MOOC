# Write your solution here
text = input("Please type in a string: ")
len_text = len(text)
second_char = text[1]
last_char = text[len_text - 2]

if len_text > 1 and second_char == last_char:
    print(f"The second and the second to last characters are {second_char}")
else:
    print(f"The second and the second to last characters are different")