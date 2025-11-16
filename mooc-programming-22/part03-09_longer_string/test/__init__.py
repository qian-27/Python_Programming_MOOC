# Write your solution here
str1 = input("Please type in string 1: ")
str2 = input("Please type in string 2: ")

length_str1 = len(str1)
length_str2 = len(str2)

if length_str1 > length_str2:
    print(f"{str1} is longer")
elif length_str1 < length_str2:
    print(f"{str2} is longer")
else:
    print("The strings are equally long")