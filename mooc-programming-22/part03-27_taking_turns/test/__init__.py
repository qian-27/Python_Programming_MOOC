# Write your solution here
num = int(input("Please type in a number: "))

i = 1
half = num // 2

if num % 2 == 0:
    while i <= half:
        print(i)
        print(num - i + 1)
        i += 1
else:
    while i <= half:
        print(i)
        print(num - i + 1)
        i += 1
    print(num - i + 1)