# Write your solution here
def shortest(myList: list):
   result = myList[0]
   for item in myList:
      if len(item) < len(result):
         result = item

   return result

# Note, that at this time the main program should not be written inside
if __name__ == "__main__":
   block