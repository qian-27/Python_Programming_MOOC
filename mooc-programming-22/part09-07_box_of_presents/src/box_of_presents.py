# WRITE YOUR SOLUTION HERE:
class Present:
   def __init__(self, name: str, weight: int):
      self.name = name
      self.weight = weight
   
   def __str__(self):
      return f"{self.name} Book ({self.weight} kg)"


class Box:
   def __init__(self):
      self.weights = 0

   def  add_present(self, present: Present):
      self.present = present
      self.weights += self.present.weight
   
   def total_weight(self):
      return self.weights


# You can test your function by calling it within the following block
if __name__ == "__main__":
   book = Present("ABC Book", 2)

   box = Box()
   box.add_present(book)
   print(box.total_weight())

   cd = Present("Pink Floyd: Dark Side of the Moon", 1)
   box.add_present(cd)
   print(box.total_weight())




# Answers!!!
# class Present:
#     def __init__(self, name: str, weight: int):
#         self.name = name
#         self.weight = weight
 
#     def __str__(self):
#         return f'Present (name: {self.name}, weight: {self.weight})'
 
# class Box:
#     def __init__(self):
#         self.presents = []
 
#     def add_present(self, present: Present):
#         self.presents.append(present)
 
#     def total_weight(self):
#         weight = 0
#         for present in self.presents:
#             weight += present.weight
#         return weight