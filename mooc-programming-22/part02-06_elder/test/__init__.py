# Write your solution here
name1 = input("Name:")
age1 = int(input("Age:"))

name2 = input("Name:")
age2 = int(input("Age:"))

# print(f"Person 1:\nName: {name1}\nAge: {age1}")
# print(f"Person 2:\nName: {name2}\nAge: {age2}")

if age1 != age2:
    if age1 > age2:
        print(f"The elder is {name1}")
    else:
        print(f"The elder is {name2}")
else:
    print(f"{name1} and {name2} are the same age")