# Write your solution here
limit = int(input("Limit: "))

num = 1
next_num = 2
text = "1"

while num < limit:
    text += f" + {next_num}"
    num += next_num
    next_num += 1

print(f"The consecutive sum: {text} = {num}")