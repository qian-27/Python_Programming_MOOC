# Write your solution here
from fractions import Fraction

def fractionate(amount: int):
   my_list = []
   i = 0
   while i < amount:
      my_list.append(Fraction(1, amount))
      i += 1
   return my_list


# You can test your function by calling it within the following block
if __name__ == "__main__":
   print(fractionate(5))



# from fractions import Fraction
 
# def fractionate(amount: int):
#     # numerator, denominator
#     fraction = Fraction(1, amount)
 
#     return [fraction] * amount