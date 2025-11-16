# Write your solution here
def invert(my_dictionary: dict):
   tem = {}
   tem = {v: k for k, v in my_dictionary.items()}
   my_dictionary.clear()
   for key, value in tem.items():
      my_dictionary[key] = value

# def invert(dictionary: dict):
# 	copy = {}
# 	for key in dictionary:
# 		copy[key] = dictionary[key]
# 	for key in copy:
# 		del dictionary[key]
# 	for key in copy:
# 		dictionary[copy[key]] = key

# You can test your function by calling it within the following block
if __name__ == "__main__":
   s = {1: "first", 2: "second", 3: "third", 4: "fourth"}
   invert(s)
   print(s)