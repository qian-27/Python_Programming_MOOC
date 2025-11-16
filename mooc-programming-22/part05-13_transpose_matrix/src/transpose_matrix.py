# Write your solution here
def transpose(matrix: list):
   l = len(matrix)
 
   for i in range(l):
      for j in range(i+1, l):
         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

# def transpose(matrix: list):
#     n = len(matrix)
#     for i in range(n):
#         for j in range(i, n):
#             temp = matrix[i][j]
#             matrix[i][j] = matrix[j][i]
#             matrix[j][i] = temp
 

# # You can test your function by calling it within the following block
if __name__ == "__main__":
   matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
   # game_board = [[1, 2],[1, 2]]
   print(transpose(matrix))
   print(matrix)


