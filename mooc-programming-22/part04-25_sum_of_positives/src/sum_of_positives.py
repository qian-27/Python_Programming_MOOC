# Write your solution here
def sum_of_positives(my_list: list):
   result = 0
   i = 0

   while i < len(my_list):
      if my_list[i] > 0:
         result += my_list[i]
      i += 1
   
   return result


# Note, that at this time the main program should not be written inside
if __name__ == "__main__":
   block