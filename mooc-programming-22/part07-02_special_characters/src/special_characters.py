# Write your solution here
import string

def separate_characters(my_string: str):
   letters = string.ascii_letters
   punctuations = string.punctuation

   part1 = ""
   part2 = ""
   part3 = ""

   for letter in my_string:
      if letter in letters:
         part1 += letter
      elif letter in punctuations:
         part2 += letter
      else:
         part3 += letter
   
   tuple = (part1, part2, part3)
   return tuple
   # part2 = string.punctuation(my_string)
   # part3 = string.printabble(my_string)
   # part4 = string.whitespace(my_string)

   # ascii_letters
   # punctuation
   # other characters (including whitespace)


# You can test your function by calling it within the following block
if __name__ == "__main__":
   parts = separate_characters("Olé!!! Hey, are ümläüts wörking?")
   print(parts)
   print(parts[0])
   print(parts[1])
   print(parts[2])



# from string import ascii_letters, punctuation
 
# def separate_characters(my_string: str):
#     letters = ""
#     special_characters = ""
#     other_characters = ""
 
#     for character in my_string:
#         if character in ascii_letters:
#             letters += character
#         elif character in punctuation:
#             special_characters += character
#         else:
#             other_characters += character
 
#     return (letters, special_characters, other_characters)