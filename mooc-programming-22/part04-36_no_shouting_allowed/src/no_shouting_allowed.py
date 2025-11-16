# Write your solution here
from curses.ascii import isupper
from operator import ne


def no_shouting(my_list: list):
   new = []

   for item in my_list:
      if item.isupper() == False:
      # if not item.isupper():
         new.append(item)
   
   return new


# Note, that at this time the main program should not be written inside
if __name__ == "__main__":
   my_list = ["ABC", "def", "UPPER", "ANOTHERUPPER", "lower", "another lower", "Capitalized"]
   pruned_list = no_shouting(my_list)
   print(pruned_list)