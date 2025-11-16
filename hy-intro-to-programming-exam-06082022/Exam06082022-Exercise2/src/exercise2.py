# Write your solution to exercise 2 here
def palindromes(my_list: list):
   new_list = []
   for string in my_list:
      if string == string[::-1]:
         new_list.append(string)
   return new_list

def word_counts(my_list: list):
   my_dict = {}
   for string in my_list:
      if string not in my_dict:
         my_dict[string] = my_list.count(string)
   return my_dict

def most_repeated_palindrome(my_list: list):
   palindromes_list = palindromes(my_list)
   word_dict = word_counts(palindromes_list)

   most_occurs_palindrome = max(word_dict, key=word_dict.get)

   return most_occurs_palindrome



# if __name__ == "__main__":
#    my_list = ["my", "jacket", "pan", "kayak", "deified", "rotator", "repaper", "deed", "jacket", "trousers", "malayalam", "kayak"]
#    print("part1")
#    print(palindromes(my_list))
#    print("part2")
#    print(word_counts(my_list))
#    print("part3")
#    print(most_repeated_palindrome(my_list))