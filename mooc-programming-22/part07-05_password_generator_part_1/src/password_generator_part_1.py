# Write your solution here
from string import ascii_lowercase
from random import choice

def generate_password(num_of_characters: int):
   lower_letters = ascii_lowercase
   password = ""

   while len(password) < num_of_characters:
      letter = choice(lower_letters)
      password += letter

   return password




# You can test your function by calling it within the following block
if __name__ == "__main__":
   for i in range(10):
      print(generate_password(2))


 
# from random import choice
# from string import ascii_lowercase
 
# def generate_password(length: int):
#     passwd = ""
#     for i in range(length):
#         passwd += choice(ascii_lowercase)
 
#     return passwd