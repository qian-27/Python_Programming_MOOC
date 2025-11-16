# Write your solution here
def even_numbers(my_list: list):
   new_list = []
   for i in my_list:
      if i % 2 == 0:
         new_list.append(i)
   return new_list


# Note, that at this time the main program should not be written inside
if __name__ == "__main__":
   block