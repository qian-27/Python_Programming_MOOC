# Write your solution here
attempts = 0

while True:
    pin_code = input("PIN: ")
    attempts += 1
    if pin_code == "4321":
        break
    print("Wrong")

if attempts == 1:
    print("Correct! It only took you one single attempt!")
else:
    print(f"Correct! It took you {attempts} attempts")