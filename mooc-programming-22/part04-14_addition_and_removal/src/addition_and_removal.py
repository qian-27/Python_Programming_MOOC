# Write your solution here
my_list = []

while True:
   print(f"The list is now {my_list}")
   answer = input("a(d)d, (r)emove or e(x)it: ")
   len_of_list = int(len(my_list))
   num = len_of_list + 1
   if answer == "x":
      break
   if answer == "d":
      my_list.append(num)
   elif answer == "r" and len_of_list > 0:
      my_list.pop(-1)

print("Bye!")