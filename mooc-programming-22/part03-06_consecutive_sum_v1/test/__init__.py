# Write your solution here
limit = int(input("Limit: "))

num = 1
loop_time = 0
while num < limit:
    loop_time += 1
    num += (loop_time + 1)

print(num)