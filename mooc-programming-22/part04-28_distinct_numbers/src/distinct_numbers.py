# Write your solution here
def distinct_numbers(myList: list):
   sorted_list = sorted(myList)
   new = []
   new.append(sorted_list[0])
   i = 1
   while i < len(sorted_list):
      if sorted_list[i] != sorted_list[i-1]:
         new_word = sorted_list[i]
         new.append(new_word)
      
      i += 1
   
   return new

# Note, that at this time the main program should not be written inside
if __name__ == "__main__":
   block

# def distinct_numbers(my_list: list):
#     results = []
#     for item in my_list:
#         if item not in results:
#             results.append(item)
 
#     results.sort()
#     return results
# Write your solution here
