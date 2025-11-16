# Write your solution here
from random import choice

def roll(die: str):
   die_A = [3, 3, 3, 3, 3, 6]
   die_B = [2, 2, 2, 5, 5, 5]
   die_C = [1, 4, 4, 4, 4, 4]

   result = 0
   if die == "A":
      result = choice(die_A)
   elif die == "B":
      result = choice(die_B)
   elif die == "C":
      result = choice(die_C)
   return result


def play(die1: str, die2: str, times: int):
   a_win = 0
   b_win = 0
   a_equal_b = 0
   sum_wins = 0

   if die1 == die2:
      for i in range(0, times):
         if roll(die1) > roll(die2):
            a_win += 1
         elif roll(die1) < roll(die2):
            b_win += 1
         else:
            a_equal_b += 1
   
   elif die1 != die2:
      while sum_wins < times:
         if roll(die1) > roll(die2):
            print(roll(die1), end = " ")
            print(roll(die2))
            a_win += 1
         elif roll(die1) < roll(die2):
            print(roll(die1), end = " ")
            print(roll(die2))
            b_win += 1
         sum_wins = a_win + b_win
   return (a_win, b_win, a_equal_b)



# You can test your function by calling it within the following block
if __name__ == "__main__":
   result = play("A", "C", 10)
   print(result)



# from random import sample
# def roll(die: str):
#     dices = {
#         "A": [3, 3, 3, 3, 3, 6],
#         "B": [2, 2, 2, 5, 5, 5],
#         "C": [1, 4, 4, 4, 4, 4]
#     }
 
#     return sample(dices[die], 1)[0]
 
# def play(die1: str, die2: str, times: int):
#     v1 = 0
#     v2 = 0
#     t = 0
#     for i in range(times):
#         n1 = roll(die1)
#         n2 = roll(die2)
#         if n1>n2:
#             v1 += 1
#         elif n1<n2:
#             v2 += 1
#         else:
#             t += 1
#     return v1, v2, t
