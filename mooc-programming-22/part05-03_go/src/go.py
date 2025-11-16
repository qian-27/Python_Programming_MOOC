# Write your solution here
def who_won(game_board: list):
   piece_1 = 0
   piece_2 = 0

   for row in game_board:
         piece_1 += row.count(1)
         piece_2 += row.count(2)

   if piece_1 > piece_2:
      return 1
   elif piece_2 > piece_1:
      return 2
   else:
      return 0

# You can test your function by calling it within the following block
# if __name__ == "__main__":
#    block