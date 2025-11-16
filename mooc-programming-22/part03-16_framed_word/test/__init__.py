# Write your solution here
text = input("Word: ")
len_text = len(text)


print("*" * 30)

if len_text % 2 == 0:
    space = int(30 - 2 - len_text) // 2
    print("*" + " " * space + text + " " * space + "*")
else:
    space = int(30 - 2 - len_text - 1) // 2
    print("*" + " " * space + text + " " * (space + 1) + "*")
    
print("*" * 30)