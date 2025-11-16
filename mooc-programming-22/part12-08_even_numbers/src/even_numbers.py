# Write your solution here
def even_numbers(beginning: int, maximum: int):
   if beginning % 2 == 0:
      number = beginning
   else:
      number = beginning + 1
   while number <= maximum:
      yield number
      number += 2



# You can test your function by calling it within the following block
if __name__ == "__main__":
   numbers = even_numbers(2, 10)
   for number in numbers:
      print(number)



# Answers!!!
# def even_numbers(beginning: int, maximum: int):
#     if beginning % 2 != 0:
#         beginning += 1
#     while beginning <= maximum:
#         yield beginning
#         beginning += 2