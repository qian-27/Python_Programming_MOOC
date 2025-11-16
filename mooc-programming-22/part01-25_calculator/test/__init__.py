# Write your solution here
num_1 = int(input("Number 1:"))
num_2 = int(input("Number 2:"))
operation = input("Operation:")
 
if operation == "add":
    result = num_1 + num_2
    print(f"{num_1} + {num_2} = {result}")
 
if operation == "multiply":
    result = num_1 * num_2
    print(f"{num_1} * {num_2} = {result}")
 
if operation == "subtract":
    result = num_1 - num_2
    print(f"{num_1} - {num_2} = {result}")s