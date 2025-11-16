# Write your solution here
def formatted(my_list: list):
   new = []
   for item in my_list:
      new.append(f"{item:.2f}")
   
   return new

# Note, that at this time the main program should not be written inside
if __name__ == "__main__":
   block