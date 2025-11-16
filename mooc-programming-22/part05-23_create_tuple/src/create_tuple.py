# Write your solution here
from unittest import result


def create_tuple(x: int, y: int, z: int):
   my_list = [x, y, z]
   mini = min(my_list)
   maxi = max(my_list)
   intotal = sum(my_list)
   result = (mini, maxi, intotal)
   return result

# def create_tuple(x: int, y: int, z: int):
#     """ The function returns a tuple formed from the parameters (smallest, greatest, sum) """
#     smallest = min([x, y, z])
#     greatest = max([x, y, z])
#     sum = x + y + z # sum([x, y, z]) also works
 
#     return (smallest, greatest, sum)

# You can test your function by calling it within the following block
if __name__ == "__main__":
   print(create_tuple(5, 3, -1))