# Write your solution here
import copy

def copy_and_add(sudoku: list, row_no: int, column_no: int, number: int):
   sudoku_copy_list = copy.deepcopy(sudoku)

   sudoku_copy_list[row_no][column_no] = number
   
   return sudoku_copy_list

# def copy_and_add(sudoku: list, row_no: int, column_no: int, number:int):
#     new_list = []
#     for r in sudoku:
#         new_list.append(r[:])
 
#     new_list[row_no][column_no] = number
#     return new_list


# You can test your function by calling it within the following block
if __name__ == "__main__":
   sudoku  = [
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0]
   ]

   sudoku2 = copy_and_add(sudoku, 0, 0, 2)
   print("Original:")
   print_sudoku(sudoku)
   print()
   print("Copy:")
   print_sudoku(sudoku2)