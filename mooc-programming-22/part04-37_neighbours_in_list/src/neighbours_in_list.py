# Write your solution here
def longest_series_of_neighbours(my_list: list):
   longest = 0
   new = []

   for i in range(len(my_list) - 1):
      result = abs(my_list[i] - my_list[i + 1])

      if result == 1:
         longest += 1         
         new.append(longest)
      elif result != 1:
         longest = 0

   result = max(new) + 1

   return result

# def longest_series_of_neighbours(my_list: list):
#     longest = 1
#     result = 1
#     for i in range(1, len(my_list)):
#         # function abs calculates the absolute value
#         if abs(my_list[i-1]-my_list[i]) == 1:
#             result += 1
#         else:
#             result = 1
#         # function max returns the highest of the parameters
#         longest = max(longest, result)
#     return longest



# Note, that at this time the main program should not be written inside
if __name__ == "__main__":
   my_list = [1, 2, 5, 7, 6, 5, 6, 3, 4, 1, 0]
   print(longest_series_of_neighbours(my_list))