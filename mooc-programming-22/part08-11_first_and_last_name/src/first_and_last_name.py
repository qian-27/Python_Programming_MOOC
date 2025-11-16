# Write your solution here:
class Person:
   def __init__(self, full_name: str):
      self.full_name = full_name.split(" ")
   
   def return_first_name(self):
      return self.full_name[0]

   def return_last_name(self):
      return self.full_name[1]


# You can test your function by calling it within the following block
if __name__ == "__main__":
   peter = Person("Peter Pythons")
   print(peter.return_first_name())
   print(peter.return_last_name())

   paula = Person("Paula Pythonnen")
   print(paula.return_first_name())
   print(paula.return_last_name())



# class Person:
#     def __init__(self, name: str):
#         self.name = name
 
#     def return_first_name(self):
#         names = self.name.split(" ")
#         return names[0]
 
#     def return_last_name(self):
#         names = self.name.split(" ")
#         return names[-1]