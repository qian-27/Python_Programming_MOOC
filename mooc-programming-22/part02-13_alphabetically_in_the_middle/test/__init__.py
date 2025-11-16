# Write your solution here
num1 = input("1st letter:")
num2 = input("2nd letter:")
num3 = input("3rd letter:")

if num1 > num2 and num1 < num3:
    print(f"The letter in the middle is {num1}")
elif num1 > num3 and num1 < num2:
    print(f"The letter in the middle is {num1}")
elif num2 > num1 and num2 < num3:
    print(f"The letter in the middle is {num2}")
elif num2 > num3 and num2 < num1:
    print(f"The letter in the middle is {num2}")
else:
    print(f"The letter in the middle is {num3}")
