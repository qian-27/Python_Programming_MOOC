# Write your solution here
def longest(strings: list):
   longest_word = strings[0]

   for item in strings:
      if len(item) > len(longest_word):
         longest_word = item
   
   return longest_word



# You can test your function by calling it within the following block
if __name__ == "__main__":
    strings = ["hi", "hiya", "hello", "howdydoody", "hi there"]
    print(longest(strings))