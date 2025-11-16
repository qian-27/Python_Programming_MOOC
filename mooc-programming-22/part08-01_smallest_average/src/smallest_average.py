# Write your solution here
from unittest import result


def smallest_average(person1: dict, person2: dict, person3: dict):
   person1_average = (person1["result1"] + person1["result2"] + person1["result3"]) / 3
   person2_average = (person2["result1"] + person2["result2"] + person2["result3"]) / 3
   person3_average = (person3["result1"] + person3["result2"] + person3["result3"]) / 3

   if person1_average < person2_average and person1_average < person3_average:
      return person1
   elif person2_average < person1_average and person2_average < person3_average:
      return person2
   else:
      return person3


# You can test your function by calling it within the following block
if __name__ == "__main__":
   person1 = {"name": "Mary", "result1": 2, "result2": 3, "result3": 3}
   person2 = {"name": "Gary", "result1": 5, "result2": 1, "result3": 8}
   person3 = {"name": "Larry", "result1": 3, "result2": 1, "result3": 1}

   print(smallest_average(person1, person2, person3))




# # Helper function for one average
# def average(person: dict):
#     ex_sum = person["result1"]+person["result2"]+person["result3"]
#     return ex_sum/3
 
# def smallest_average(person1: dict, person2: dict, person3: dict):
#     smallest = person1
 
#     if average(person2) < average(smallest):
#         smallest = person2
 
#     if average(person3) < average(smallest):
#         smallest = person3
 
#     return smallest