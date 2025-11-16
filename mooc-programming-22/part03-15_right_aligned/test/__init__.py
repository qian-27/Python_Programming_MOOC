# Write your solution here
text = input("Please type in a string: ")
len_text = len(text)
len_symbol = 20 - len_text

print("*" * len_symbol + text)