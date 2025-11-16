# Write your solution here
def new_person(name: str, age: int):
   input_name_list = name.split()
   if len(name) > 40:
      raise ValueError
   if age < 0 or age > 150:
      raise ValueError
   if len(input_name_list) < 2:
      raise ValueError
   else:
      return (name, age)
      
# You can test your function by calling it within the following block
if __name__ == "__main__":
   print(new_person('James', 32))


# def new_person(name: str, age: int):
#     # Validate name
#     if name == "" or (" " not in name) or len(name) > 40:
#         raise ValueError("Invalid argument value for name: " + name)
 
#     # Validate age
#     if age < 0 or age > 150:
#         raise ValueError("Invalid argument value for age:" + str(age))
 
#     # Both ok
#     return (name, age)
