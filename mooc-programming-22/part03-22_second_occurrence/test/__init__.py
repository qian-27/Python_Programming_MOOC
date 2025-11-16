# Write your solution here
string = input("Please type in a string: ")
substring = input("Please type in a substring: ")

index1 = string.find(substring)

word = string[index1 + len(substring):]
index2 = word.find(substring)

index = index2 + index1 + len(substring)

if index2 < 0:
    print("The substring does not occur twice in the string.")
else:
    print(f"The second occurrence of the substring is at index {index}.")

# print(index1)
# print(word)
# print(index2)
# print(index)