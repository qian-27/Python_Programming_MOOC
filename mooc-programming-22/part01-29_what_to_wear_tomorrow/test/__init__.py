# Write your solution here
temperature = int(input("Temperature: "))
rain = input("Will it rain (yes/no): ")
 
if temperature > 20:
    print("Wear jeans and a T-shirt")
elif temperature > 10:
    print("Wear jeans and a T-shirt\nI recommend a jumper as well")
elif temperature > 5:
    print("Wear jeans and a T-shirt\nI recommend a jumper as well\nTake a jacket with you")
else:
    print("Wear jeans and a T-shirt\nI recommend a jumper as well\nTake a jacket with you\nMake it a warm coat, actually\nI think gloves are in order")
 
if rain == "yes":
    print("Don't forget your umbrella!")