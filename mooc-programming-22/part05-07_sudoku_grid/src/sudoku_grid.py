# Write your solution here
def row_correct(sudoku: list):
   x = 0

   while x < len(sudoku):
      y = 0
      row_list = []
      while y < len(sudoku):
         number = sudoku[x][y]
         if number > 0 and number in row_list:
            return False
         row_list.append(number)
         y += 1
      # print(sorted(row_list))
      x += 1
   
   return True

def column_correct(sudoku: list):

   y = 0

   while y < len(sudoku):
      x = 0
      column_list = []
      while x < len(sudoku):
         number = sudoku[x][y]
         if number > 0 and number in column_list:
            return False
         column_list.append(number)
         x += 1
      print(sorted(column_list))
      y += 1
   
   return True

def grid_correct(sudoku: list):
   column = 0
   while column < len(sudoku):
      row = 0
      while row < len(sudoku):
         numbers = []
 
         for r in range(row, row+3):
            for c in range(column, column+3):
               number = sudoku[r][c]
               if number > 0 and number in numbers:
                  return False
               numbers.append(number)
               print(numbers)
         row += 3
      
      column += 3
 
   return True

def sudoku_grid_correct(sudoku: list):

   row_cor = row_correct(sudoku)
   if row_cor == False:
      return False
   
   column_cor = column_correct(sudoku)
   if column_cor == False:
      return False

   grid_cor = grid_correct(sudoku)
   if grid_cor == False:
      return False
   
   
   return True


# You can test your function by calling it within the following block
# if __name__ == "__main__":
#    sudoku1 = [
#      [9, 0, 0, 0, 8, 0, 3, 0, 0],
#      [2, 0, 0, 2, 5, 0, 7, 0, 0],
#      [0, 2, 0, 3, 0, 0, 0, 0, 4],
#      [2, 9, 4, 0, 0, 0, 0, 0, 0],
#      [0, 0, 0, 7, 3, 0, 5, 6, 0],
#      [7, 0, 5, 0, 6, 0, 4, 0, 0],
#      [0, 0, 7, 8, 0, 3, 9, 0, 0],
#      [0, 0, 1, 0, 0, 0, 0, 0, 3],
#      [3, 0, 0, 0, 0, 0, 0, 0, 2]
#    ]

#    sudoku2 = [
#      [2, 6, 7, 8, 3, 9, 5, 0, 4],
#      [9, 0, 3, 5, 1, 0, 6, 0, 0],
#      [0, 5, 1, 6, 0, 0, 8, 3, 9],
#      [5, 1, 9, 0, 4, 6, 3, 2, 8],
#      [8, 0, 2, 1, 0, 5, 7, 0, 6],
#      [6, 7, 4, 3, 2, 0, 0, 0, 5],
#      [0, 0, 0, 4, 5, 7, 2, 6, 3],
#      [3, 2, 0, 0, 8, 0, 0, 5, 7],
#      [7, 4, 5, 0, 0, 3, 9, 0, 1]
#    ]

#    sudoku3 = [
#      [ 6, 4, 9, 2, 8, 3, 1, 5, 7 ],
#      [ 0, 5, 0, 6, 4, 9, 2, 3, 8 ],
#      [ 2, 3, 8, 1, 5, 7, 6, 4, 9 ],
#      [ 9, 2, 3, 8, 1, 5, 0, 6, 4 ],
#      [ 7, 6, 4, 9, 2, 3, 8, 1, 5 ],
#      [ 8, 1, 5, 7, 0, 4, 9, 2, 0 ],
#      [ 5, 7, 6, 4, 9, 2, 3, 2, 1 ],
#      [ 4, 0, 2, 3, 8, 1, 5, 0, 6 ],
#      [ 3, 0, 1, 5, 0, 6, 4, 9, 0 ],
#    ]


   # print(row_correct(sudoku1))
   # print(column_correct(sudoku3))
   # print(grid_correct(sudoku1))
   # print(sudoku_grid_correct(sudoku3))