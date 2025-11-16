# Write your solution here
def row_correct(sudoku: list, row_no: int):
   results = 0
   for item in sudoku[row_no]:
      if item >= 1 and item <= 9:
         x = sudoku[row_no].count(item)
         if x > results:
            results = x
   
   if results == 1:
      return True
   else:
      return False

# def row_correct(sudoku: list, row_no: int):
#     numbers = []
#     for number in sudoku[row_no]:
#         if number > 0 and number in numbers:
#             return False
#         numbers.append(number)
 
#     return True


# You can test your function by calling it within the following block
if __name__ == "__main__":
   sudoku = [
     [9, 0, 0, 0, 8, 0, 3, 0, 0],
     [2, 0, 0, 2, 5, 0, 7, 0, 0],
     [0, 2, 0, 3, 0, 0, 0, 0, 4],
     [2, 9, 4, 0, 0, 0, 0, 0, 0],
     [0, 0, 0, 7, 3, 0, 5, 6, 0],
     [7, 0, 5, 0, 6, 0, 4, 0, 0],
     [0, 0, 7, 8, 0, 3, 9, 0, 0],
     [0, 0, 1, 0, 0, 0, 0, 0, 3],
     [3, 0, 0, 0, 0, 0, 0, 0, 2]
   ]

   print(row_correct(sudoku, 0))
   print(row_correct(sudoku, 1))