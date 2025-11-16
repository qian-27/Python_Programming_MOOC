# Write your solution here
def all_the_longest(my_list: list):
   longest = 0
   new = []
   
   for item in my_list:
      if len(item) > longest:
         longest = len(item)
   
   for item in my_list:
      if len(item) == longest:
         new.append(item)

   return new

# Note, that at this time the main program should not be written inside
if __name__ == "__main__":
   block