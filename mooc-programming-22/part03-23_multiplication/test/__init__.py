# Write your solution here
num = int(input("Please type in a number: "))

i = 1

while num > 0 and i <= num:
    k = 1
    
    while k <= num:
        print(f'{i} x {k} = {i * k}')
        k += 1
    
    i += 1