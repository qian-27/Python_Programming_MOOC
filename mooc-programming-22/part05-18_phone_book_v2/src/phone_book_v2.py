# Write your solution here
my_dictionary = {}
while True:

   input_num = int(input("command (1 search, 2 add, 3 quit): "))

   if input_num == 2:
      input_name = input("name: ")
      input_number = input("number: ")
      if input_name not in my_dictionary:
         my_dictionary[input_name] = [input_number]
      else:
         my_dictionary[input_name].append(input_number)
      print("ok!")
   elif input_num == 1:
      input_name = input("name: ")
      if input_name not in my_dictionary:
         print("no number")
      if input_name in my_dictionary:
         for item in range(len(my_dictionary[input_name])):
            print(my_dictionary[input_name][item])
   elif input_num == 3:
      print("quitting...")
      break

# def search(persons):
#     name = input("name: ")
#     if name in persons:
#         for number in persons[name]:
#             print(number)
#     else:
#         print("no number")
 
# def add(persons):
#     name = input("name: ")
#     number = input("number: ")
#     if name not in persons:
#         persons[name] = []
#     persons[name].append(number)
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