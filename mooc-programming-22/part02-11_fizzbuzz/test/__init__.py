# Write your solution here
num = int(input("Number:"))
remainder1 = num % 15
remainder2 = num % 3
remainder3 = num % 5

if remainder1 == 0:
    print("FizzBuzz")
elif remainder2 == 0:
    print("Fizz")
elif remainder3 == 0:
    print("Buzz")