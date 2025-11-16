# Write your solution here
def count_matching_elements(my_matrix: list, element: int):
   results = 0
   for row in my_matrix:
         x = row.count(element)
         results += x

   return results




# You can test your function by calling it within the following block
if __name__ == "__main__":
   m = [[1, 2, 1], [0, 3, 4], [1, 0, 0]]
   print(count_matching_elements(m, 4))