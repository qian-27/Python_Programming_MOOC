# Write your solution here
from cgitb import text
import json

def print_persons(filename: str):
   with open(filename) as my_file:
      data = my_file.read()
   
   info = json.loads(data)
   text = ""
   for student in info:
      # print(f'{info[name]} {info[age]} years ({info[hobbies]})')
      print(f"{student['name']} {student['age']} years (", end = "")
      print(', '.join(student['hobbies']), end = "")
      print(f")")

   
   return text


# You can test your function by calling it within the following block
if __name__ == "__main__":
   print_persons("file1.json")




# import json
# def print_persons(filename: str):
#     with open(filename) as f:
#         content = f.read()
#     persons = json.loads(content)
#     for person in persons:
#         name = person['name']
#         age = person['age']
#         hobbies = ", ".join(person['hobbies'])
#         print(f"{name} {age} years ({hobbies})")
 