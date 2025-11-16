# write your solution here
def read_fruits():
   fruit_dict = {}
   with open("fruits.csv") as new_file:
      for line in new_file:
         line = line.replace("\n", "")
         parts = line.split(";")
         fruit_name = parts[0]
         fruit_price = float(parts[1])
         fruit_dict[fruit_name] = fruit_price
   
   return fruit_dict

# You can test your function by calling it within the following block
if __name__ == "__main__":
   print(read_fruits())


