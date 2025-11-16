# WRITE YOUR SOLUTION HERE:
class ListHelper:
   
   @classmethod
   def greatest_frequency(cls, my_list: list):
      frequency = 0
      most_frequency_number = 0
      for item in my_list:
         if my_list.count(item) > frequency:
            frequency = my_list.count(item)
            most_frequency_number = item
      return most_frequency_number

   @classmethod
   def doubles(cls, my_list: list):
      new_list = []
      for item in my_list:
         if my_list.count(item) >= 2 and item not in new_list:
            new_list.append(item)
      return len(new_list)



# You can test your function by calling it within the following block
if __name__ == "__main__":
   numbers = [1, 1, 2, 1, 3, 3, 4, 5, 5, 5, 6, 5, 5, 5]
   print(ListHelper.greatest_frequency(numbers))
   # print(ListHelper.doubles(numbers))