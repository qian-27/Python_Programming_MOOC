# Write your solution here
print("Please type in integer numbers. Type in 0 to finish.")
count = 0
total = 0
positive = 0
negative = 0
while True:
    integer = int(input("Number: "))
    count += 1
    total += integer
    if integer > 0:
        positive += 1
    elif integer < 0:
        negative += 1
        
    if integer == 0:
        break
print(f"Numbers typed in {count - 1}")
print(f"The sum of the numbers is {total}")
print(f"The mean of the numbers is {total / (count - 1)}")
print(f"Positive numbers {positive}")
print(f"Negative numbers {negative}")
