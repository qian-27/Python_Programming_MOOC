# Write your solution here
def histogram(word: str):
   letters = {}
   for i in word:
      if i not in letters:
         letters[i] = word.count(i)
         print(f"{i} {'*' * word.count(i)}")

# def histogram(my_str: str):
#     characters = {}
#     for character in my_str:
#         if not character in characters:
#             characters[character] = 0
#         characters[character] += 1
 
#     for character, lkm in characters.items():
#         stars = "*"*lkm
#         print(f"{character} {stars}")



# # You can test your function by calling it within the following block
if __name__ == "__main__":
   histogram("abba")