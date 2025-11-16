# Write your solution here
from cgitb import small


def remove_smallest(numbers: list):
   smallest = numbers[0]
   for item in numbers:
      if item < smallest:
         smallest = item
   
   numbers.remove(smallest)

# def remove_smallest(numbers: list):
#     smallest = min(numbers)
#     numbers.remove(smallest)