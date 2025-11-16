# Write your solution here
import random

def words(n: int, beginning: str):
   my_list = []

   with open("words.txt") as file:
      for line in file:
         line = line.replace("\n", "")
         if line.find(beginning) == 0:
            my_list.append(line)

   # print(my_list)
   if len(my_list) < n:
      raise ValueError

   another_list = []
   while len(another_list) < n:
      word = random.choice(my_list)
      if word not in another_list:
         another_list.append(word)
   
   return another_list


# You can test your function by calling it within the following block
if __name__ == "__main__":
   word_list = words(3, "ca")
   for word in word_list:
      print(word)


# import random
 
# def words(n: int, beginning: str):
#     word_list = []
#     with open("words.txt") as file:
#         for word in file:
#             word = word.replace("\n","")
#             if word.startswith(beginning):
#                 word_list.append(word)
#     if len(word_list) < n:
#         raise ValueError("Not enough suitable words can be found!")
#     return random.sample(word_list, n)