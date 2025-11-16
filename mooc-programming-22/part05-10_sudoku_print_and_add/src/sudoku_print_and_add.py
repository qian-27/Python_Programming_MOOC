# Write your solution here
def print_sudoku(sudoku: list):
   row = 0

   while row < len(sudoku):
      column = 0

      while column < len(sudoku):
         number = sudoku[row][column]

         if column == len(sudoku) - 1:
            if row == 2 or row == 5:
               if number == 0:
                  print("_ \n")
               else:
                  print(f'{number} \n')
            else:
               if number == 0:
                  print("_ ")
               else:
                  print(f'{number} ')

         elif column == 3 or column == 6:
            if number == 0:
               print(" _ ", end = "")
            else:
               print(f' {number} ', end = "")
         else:
            if number == 0:
               print("_ ", end = "")
            else:
               print(f'{number} ', end = "")

         column += 1

      row += 1


def add_number(sudoku: list, row_no: int, column_no: int, number:int):
   sudoku[row_no][column_no] = number

   

# def print_sudoku(sudoku: list):
#     r = 0
#     for row in sudoku:
#         s = 0
#         for character in row:
#             s += 1
#             if character == 0:
#                 character = "_"
#             m = f"{character} "
#             if s%3 == 0 and s < 8:
#                 m += " "
#             print(m, end="")
 
#         print()
#         r += 1
#         if r%3 == 0 and r < 8:
#             print()
 
# def add_number(sudoku: list, row_no: int, column_no: int, number: int):
#     sudoku[row_no][column_no] = number

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

   print_sudoku(sudoku)
   add_number(sudoku, 0, 0, 2)
   add_number(sudoku, 1, 2, 7)
   add_number(sudoku, 5, 7, 3)
   print()
   print("Three numbers added:")
   print()
   print_sudoku(sudoku)
