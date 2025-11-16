# Write your solution here
from random import choice, randint
from string import ascii_lowercase

def generate_strong_password(length_of_password: int, second_argument = True, third_argument = True):
   letters = ascii_lowercase
   numbers = "0123456789"
   characters = "!?=+-()#"

   password = choice(letters)

   if second_argument != True and third_argument != True:
      while len(password) < int(length_of_password):
         i = choice(letters)
         password += i

   elif second_argument == True and third_argument == True:
      password += choice(numbers)
      password += choice(characters)
      while len(password) < int(length_of_password):
         i = choice(letters + numbers + characters)
         password += i

   elif second_argument != True and third_argument == True:
      password += choice(characters)
      while len(password) < int(length_of_password):
         i = choice(letters + characters)
         password += i

   elif second_argument == True and third_argument != True:
      password += choice(numbers)
      while len(password) < int(length_of_password):
         i = choice(letters + numbers)
         password += i

   return password



# You can test your function by calling it within the following block
if __name__ == "__main__":
   print(generate_strong_password(2, False, False))


# from random import choice, randint
# from string import ascii_lowercase, digits
 
# def generate_strong_password(length: int, numbers: bool, special_characters: bool):
#     special_chars = "!?=+-()#"
#     # One letter at beginning of the password
#     passwd = choice(ascii_lowercase)
#     choice_set = ascii_lowercase
 
#     # If numbers is wanted, add at least one number
#     if numbers:
#         passwd = add_character(passwd, digits)
#         choice_set += digits
 
#     # same for special characters
#     if special_characters:
#         passwd = add_character(passwd, special_chars)
#         choice_set += special_chars
 
#     # build the rest of the password from the whole set
#     while (len(passwd) < length):
#         passwd = add_character(passwd, choice_set)
 
#     return passwd
 
# # Add a random character from the given set either
# # at the beginning or end of the string
# def add_character(passwd: str, characters):
#     character = choice(characters)
#     if randint(1,2) == 1:
#         return character + passwd
#     else:
#         return passwd + character