# write your solution here
def largest():
   with open("numbers.txt") as new_file:
      largest_number = 0

      for line in new_file:
         line = line.replace("\n", "")
         if int(line) > largest_number:
            largest_number = int(line)
   
   return largest_number


   # with open("numbers.txt") as new_file:
   #    contents = new_file.read()
   #    print(contents)


# You can test your function by calling it within the following block
if __name__ == "__main__":
   print(largest())

