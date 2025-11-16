# WRITE YOUR SOLUTION HERE:
def lengths(lists: list):
   return [len(list) for list in lists]



# You can test your function by calling it within the following block
if __name__ == "__main__":
   lists = [[1,2,3,4,5], [324, -1, 31, 7],[]]
   print(lengths(lists))