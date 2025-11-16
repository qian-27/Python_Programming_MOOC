# Write your solution here
while True:
    num = int(input("Please type in a number: "))
    if num <= 0:
        break

    index = 1
    fac = 1

    while index <= num:
        fac *= index
        index += 1
    
    print(f"The factorial of the number {num} is {fac}")

print("Thanks and bye!")