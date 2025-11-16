# Write your solution here
def most_common_character(my_stirng: str):
   letter_list = []
   max = 0

   for letter in my_stirng:
      if letter not in letter_list:
         letter_list.append(letter)
   
   for item in letter_list:
      x = my_stirng.count(item)
      if x > max:
         max = x
   
   for letter in my_stirng:
      if my_stirng.count(letter) == max:
         return letter
      

# Note, that at this time the main program should not be written inside
if __name__ == "__main__":
   my_stirng = "abcdbde"
   print(most_common_character(my_stirng))