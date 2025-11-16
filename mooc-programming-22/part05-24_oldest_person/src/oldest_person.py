# Write your solution here
from unittest import result


def oldest_person(people: list):
   oldest = people[0][1]
   index = 0
   for i in range(len(people)):
      if people[i][1] < oldest:
         oldest = people[i][1]
         index = i
   result = people[index][0]
   return result

# def oldest_person(people: list):
#    oldest = people[0]
#    for person in people:
#       # comparing the year of birth of the oldest known person and the person in turn
#       if person[1] < oldest[1]:
#          oldest = person
 
#    return oldest[0]



# You can test your function by calling it within the following block
if __name__ == "__main__":
   p1 = ("Adam", 1977)
   p2 = ("Ellen", 1985)
   p3 = ("Mary", 1953)
   p4 = ("Ernest", 1997)
   people = [p1, p2, p3, p4]

   print(oldest_person(people))