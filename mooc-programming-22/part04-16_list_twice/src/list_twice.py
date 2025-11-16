# Write your solution here
the_list = []

while True:
   new_item = int(input("New item: "))
   if new_item == 0:
      break
   the_list.append(new_item)
   print(f'The list now: {the_list}')
   print(f'The list in order: {sorted(the_list)}')

print("Bye!")
