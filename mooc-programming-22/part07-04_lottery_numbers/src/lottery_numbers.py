# Write your solution here
from calendar import week
from random import sample

def lottery_numbers(amount: int, lower: int, upper: int):
   number_pool = list(range(lower, upper+1))
   draw = sample(number_pool, amount)
   number_in_order = sorted(draw)

   return number_in_order



# You can test your function by calling it within the following block
if __name__ == "__main__":
   for number in lottery_numbers(7, 1, 40):
      print(number)



# from random import randint
 
# def lottery_numbers(amount: int, lower: int, upper: int):
#     numbers = []
#     while len(numbers) < amount:
#         number = randint(lower, upper)
#         if number not in numbers:
#             numbers.append(number)
 
#     return sorted(numbers)