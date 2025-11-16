# write your solution here
def matrix_sum():
   sum = 0
   with open("matrix.txt") as new_file:
      for row in new_file:
         row = row.replace("\n", "")
         numbers = row.split(",")
         for number in numbers:
            print(int(number))
            sum += int(number)

   return sum


def matrix_max():
   with open("matrix.txt") as new_file:
      max = 0
      for row in new_file:
         row = row.replace("\n", "")
         numbers = row.split(",")
         for number in numbers:
            if int(number) > max:
               max = int(number)

   return max


def row_sums():
   list_of_sum = []
   with open("matrix.txt") as new_file:
      for row in new_file:
         row = row.replace("\n", "")
         numbers = row.split(",")

         sum = 0
         for number in numbers:
            sum += int(number)

         list_of_sum.append(sum)

   return list_of_sum


# You can test your function by calling it within the following block
if __name__ == "__main__":
   print(matrix_sum())
   print(matrix_max())
   print(row_sums())


# Answer from Helsinki University
# def read_matrix():
#     with open("matrix.txt") as file:
#         m = []
#         for row in file:
#             mrow = []
#             items = row.split(",")
#             for item in items:
#                 mrow.append(int(item))
#             m.append(mrow)
 
#     return m
 
# # Yhdistää matriisin rivit yhdeksi listaksi
# def combine(matriisi: list):
#     mlist = []
#     for row in matriisi:
#         mlist += row
    
#     return mlist
 
# def matrix_sum():
#     mlist = combine(read_matrix())
#     return sum(mlist)
 
# def matrix_max():
#     mlist = combine(read_matrix())
#     return max(mlist)
 
# def row_sums():
#     matrix = read_matrix()
#     sums = []
#     for row in matrix:
#         sums.append(sum(row))
#     return sums

# if __name__ == "__main__":
#    print(read_matrix())



