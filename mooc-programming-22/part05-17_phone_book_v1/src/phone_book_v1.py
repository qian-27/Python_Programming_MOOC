# Write your solution here
my_dictionary = {}
while True:

   input_num = int(input("command (1 search, 2 add, 3 quit): "))

   if input_num == 2:
      input_name = input("name: ")
      input_number = input("number: ")
      my_dictionary[input_name] = input_number
      print("ok!")
   elif input_num == 1:
      input_name = input("name: ")
      if input_name not in my_dictionary:
         print("no number")
      if input_name in my_dictionary:
         print(my_dictionary[input_name])
   elif input_num == 3:
      print("quitting...")
      break


# def search(persons):
#     name = input("name: ")
#     if name in persons:
#         print(persons[name])
#     else:
#         print("no number")
 
# def add(persons):
#     name = input("name: ")
#     number = input("number: ")
#     persons[name] = number
#     print("ok!")
 
# def main():
#     persons = {}
#     while True:
#         cmd = input("command (1 search, 2 add, 3 quit): ")
#         if cmd == "1":
#             search(persons)
#         if cmd == "2":
#             add(persons)
#         if cmd == "3":
#             break
#     print("quitting...")
 
# main()

            
      





