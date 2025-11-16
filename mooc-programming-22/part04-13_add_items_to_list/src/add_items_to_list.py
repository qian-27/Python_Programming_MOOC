# Write your solution here
number_of_items = int(input("How many items: "))
my_list = []
num = 1

while True:
   if num > number_of_items:
      break
   new_item = int(input(f"Item {num}: "))
   my_list.append(new_item)
   num += 1

print(my_list)
