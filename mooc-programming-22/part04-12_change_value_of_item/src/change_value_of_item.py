# Write your solution here
my_list = [1, 2, 3, 4, 5]

while True:
   index = int(input("Index: "))
   if index == -1:
      break
   if index < 0 or index >= len(my_list):
      print("Index is outside of the range of the list")
      continue

   new_value = int(input("New value: "))
   my_list[index] = new_value
   print(my_list)
