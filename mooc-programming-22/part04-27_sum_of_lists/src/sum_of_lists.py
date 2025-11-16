# Write your solution here
def list_sum(a: list, b:list):
   new = []
   i = 0
   if len(a) == len(b):
      while i < len(a):
         new.append(a[i] + b[i])
         i += 1
   
   return new

# Note, that at this time the main program should not be written inside
if __name__ == "__main__":
   block

# def list_sum(list1: list, list2: list):
#     results = []
#     for i in range(len(list1)):
#         results.append(list1[i] + list2[i])
 
#     return results

# Another solution would be use zip-function,
# which creates new list by combining items in two or more lists
# for item1, item2 in zip(list1, list2):
#   results.append(item1 + item2)