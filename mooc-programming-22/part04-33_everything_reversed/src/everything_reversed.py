# Write your solution here
def everything_reversed(my_list: list):
   reversed_list = reversed(my_list)
   new = []

   for item in reversed_list:
      new_item = item[::-1]
      new.append(new_item)
   
   return new

# Note, that at this time the main program should not be written inside
if __name__ == "__main__":
   my_list = ["Steve", "Jean", "Katherine", "Paul"]
   print(everything_reversed(my_list))