# Write your solution here
my_list = []
times = 0
while True:
   words = input("Word: ")
   if words in my_list:
      break
   my_list.append(words)
   times += 1


print(f"You typed in {times} different words")