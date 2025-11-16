# Write your solution here
while True:
   print("1 - add an entry, 2 - read entries, 0 - quit")
   input_num = int(input("Function: "))
   if input_num == 0:
      break

   if input_num == 1:
      input_diary = input("Diary entry: ")
      with open("diary.txt", "a") as my_file:
         my_file.write(input_diary)
         my_file.write("\n")
      print("Diary saved")

   if input_num == 2:
      print("Entries: ")
      with open("diary.txt") as my_file:
         for line in my_file:
            print(line)
   
print("Bye now!")