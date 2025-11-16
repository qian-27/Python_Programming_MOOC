# Write your solution here:
def word_generator(characters: str, length: int, amount: int):
   return (characters[i: i+length] for i in range(amount))


# You can test your function by calling it within the following block
if __name__ == "__main__":
   wordgen = word_generator("abcdefg", 3, 5)
   for word in wordgen:
      print(word)



# Answers!!!
# from random import choice
 
# def word_generator(letters: str, length: int, amount:int):
#     return ("".join([choice(letters ) for i in range(length)]) for j in range(amount))