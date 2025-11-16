# Write your solution here
input_num = int(input("Please type in a number:"))
 
if input_num < 0:
    input_num *= -1
    print(f"The absolute value of this number is {input_num}")
else:
    print(f"The absolute value of this number is {input_num}")
