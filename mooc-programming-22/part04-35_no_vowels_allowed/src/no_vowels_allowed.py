# Write your solution here
def no_vowels(my_string: str):
   new = my_string.replace("a", "")
   new = new.replace("o", "")
   new = new.replace("e", "")
   new = new.replace("i", "")
   new = new.replace("u", "")

   return new



# Note, that at this time the main program should not be written inside
if __name__ == "__main__":
   my_string = "this is an example"
   print(no_vowels(my_string))