# Write your solution here
def row_sums(my_matrix: list):
   for list in my_matrix:
      sum = 0
      for item in list:
         sum += item
      list.append(sum)


# You can test your function by calling it within the following block
if __name__ == "__main__":
   my_matrix = [[1, 2], [3, 4]]
   row_sums(my_matrix)
   print(my_matrix)




# def row_sums(matrix: list):
#     for row in matrix:
#         row.append(sum(row))