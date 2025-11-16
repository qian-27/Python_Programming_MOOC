# Write your solution here

num = int(input("Please type in a number: "))

i = 1

if num > 1:
    if num % 2 == 0:
        while i <= num:
            print(i + 1)
            print(i)
            i += 2
    else:
        while i < num:
            print(i + 1)
            print(i)
            i += 2
        print(num)

elif num == 1:
    print(num)