# Write your solution here
def palindromes(word: str):
   reversed = word[::-1]
   if word == reversed:
      return True
   else:
      return False

def main():
    while True:
      words = input("Please type in a palindrome: ")
      if palindromes(words):
         print(f"{words} is a palindrome!")
         break
      else:
         print("that wasn't a palindrome")


# Note, that at this time the main program should not be written inside
# if __name__ == "__main__":
#    block
main()