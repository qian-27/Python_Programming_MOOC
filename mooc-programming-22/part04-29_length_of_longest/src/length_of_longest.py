# Write your solution here
def length_of_longest(myList: list):
   length_of_result = 0
   for item in myList:
      if len(item) > length_of_result:
         length_of_result = len(item)

   return length_of_result

# Note, that at this time the main program should not be written inside
if __name__ == "__main__":
   block