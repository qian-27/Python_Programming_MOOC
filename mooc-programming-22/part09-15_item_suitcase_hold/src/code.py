# Write your solution here:
class Item:
   def __init__(self, name: str, weight: int):
      self.__name = name
      self.__weight = weight
   
   def name(self):
      return self.__name
   
   def weight(self):
      return self.__weight
   
   def __str__(self):
      return f"{self.name()} ({self.weight()} kg)"


class Suitcase:
   def __init__(self, max_weight: int):
      self.max_weight = max_weight
      self.__items = []

   def weight(self):
      w = 0
      for item in self.__items:
         w += item.weight()
      return w
   
   def add_item(self, item: Item):
      if self.weight() + item.weight() <= self.max_weight:
         self.__items.append(item)

   def heaviest_item(self):
      heaviest_item = None
      heaviest_weight = 0
      for item in self.__items:
         if item.weight() > heaviest_weight:
            heaviest_weight = item.weight()
            heaviest_item = item
      return heaviest_item
   
   def print_items(self):
      for item in self.__items:
         # print(f'{item.name()} ({item.weight()} kg)')
         print(item)

   def __str__(self):
      if len(self.__items) == 1:
         return f"{len(self.__items)} item ({self.weight()} kg)"
      else:
         return f"{len(self.__items)} items ({self.weight()} kg)"


class CargoHold:
   def __init__(self, max_weight: int):
      self.__max_weight = max_weight
      self.cargo_weight = 0
      self.suitcases = []
   
   def add_suitcase(self, suitcase: Suitcase):
      if suitcase.weight() + self.cargo_weight <= self.__max_weight:
         self.cargo_weight += suitcase.weight()
         self.suitcases.append(suitcase)
   
   def __str__(self):
      if len(self.suitcases) == 1:
         return f"{len(self.suitcases)} suitcase, space for {self.__max_weight - self.cargo_weight} kg"
      else:
         return f"{len(self.suitcases)} suitcases, space for {self.__max_weight - self.cargo_weight} kg"

   def print_items(self):
      for suitcase in self.suitcases:
         suitcase.print_items()
      


# You can test your function by calling it within the following block
if __name__ == "__main__":
   book = Item("ABC Book", 2)
   phone = Item("Nokia 3210", 1)
   brick = Item("Brick", 4)

   adas_suitcase = Suitcase(10)
   adas_suitcase.add_item(book)
   adas_suitcase.add_item(phone)

   peters_suitcase = Suitcase(10)
   peters_suitcase.add_item(brick)

   cargo_hold = CargoHold(1000)
   cargo_hold.add_suitcase(adas_suitcase)
   cargo_hold.add_suitcase(peters_suitcase)

   print("The suitcases in the cargo hold contain the following items:")
   cargo_hold.print_items()



# Answers!!!
# class Item:
#     def __init__(self, name: str, weight: int):
#         self.__name = name
#         self.__weight = weight
 
#     def __str__(self):
#         return f"{self.__name} ({self.__weight} kg)"
 
#     def weight(self):
#         return self.__weight
 
#     def name(self):
#         return self.__name
 
# class Suitcase:
#     def __init__(self, max_weight: int):
#         self.__max_weight = max_weight
#         self.__items = []
 
#     def weight(self):
#         p = 0
#         for item in self.__items:
#             p += item.weight()
#         return p
 
#     def __str__(self):
#         # Use the one-line condition introduced at the end of part 7
#         end_s = "s" if len(self.__items) != 1 else ""
 
#         return f"{len(self.__items)} item{end_s} ({self.weight()} kg)"
 
#     def add_item(self, item):
#         if self.weight() + item.weight() > self.__max_weight:
#             return
 
#         self.__items.append(item)
 
#     def print_items(self):
#         for item in self.__items:
#             print(item)
 
#     def heaviest_item(self):
#         heaviest = self.__items[0]
#         for item in self.__items:
#             if item.weight() > heaviest.weight():
#                 heaviest = item
#         return heaviest
 
# class CargoHold:
#     def __init__(self, max_weight: int):
#         self.__max_weight = max_weight
#         self.__suitcases = []
 
   #  def __str__(self):
   #      word = "suitcases"
   #      if len(self.__suitcases) == 1:
   #          word = "suitcase"
 
   #      return f"{len(self.__suitcases)} {word}, space for {self.__max_weight-self.weight()} kg"
 
   #  def weight(self):
   #      p = 0
   #      for suitcase in self.__suitcases:
   #          p += suitcase.weight()
   #      return p
 
   #  def add_suitcase(self, suitcase):
   #      if self.weight() + suitcase.weight() > self.__max_weight:
   #          return
   #      self.__suitcases.append(suitcase)
 
   #  def print_items(self):
   #      for suitcase in self.__suitcases:
   #          suitcase.print_items()