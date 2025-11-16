# Write your solution here
import string
def change_case(orig_string: str):
   new_string = ""
   for character in orig_string:
      if character in string.ascii_uppercase:
         new_string += character.lower()
      elif character in string.ascii_lowercase:
         new_string += character.upper()
      else:
         new_string += character
   
   return new_string


def split_in_half(orig_string: str):
   length_of_string = len(orig_string)
   half = length_of_string // 2
   p1 = orig_string[0:half]
   p2 = orig_string[half:length_of_string]
   return p1, p2


def remove_special_characters(orig_string: str):
   new_string = ""
   for character in orig_string:
      if character in string.ascii_letters:
         new_string += character
      elif character in string.digits:
         new_string += character
      elif character == " ":
         new_string += character
   
   return new_string


# You can test your function by calling it within the following block
if __name__ == "__main__":
   p1, p2 = split_in_half("Well hello there!")
   print(p1)
   print(p2)


 
# from string import ascii_letters, digits
 
# def change_case(orig_string: str):
#     new_string = ""
#     for character in orig_string:
#         if character.isupper():
#             new_string += character.lower()
#         elif character.islower():
#             new_string += character.upper()
#         else:
#             new_string += character
 
#     return new_string
 
# def split_in_half(orig_string: str):
#     return orig_string[:len(orig_string) // 2], orig_string[len(orig_string) // 2:]
 
# def remove_special_characters(orig_string: str):
#     allowed = ascii_letters + digits + ' '
#     new_string = ""
#     for character in orig_string:
#         if character in allowed:
#             new_string += character
 
#     return new_string