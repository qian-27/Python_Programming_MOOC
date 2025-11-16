# write your solution here
# if False:
#     student_info_file = input("Student information: ")
#     student_exercises_file = input("Exercises completed: ")
# else:
#     # now this is the False branch, and is never executed
#     student_info_file = "students2.csv"
#     student_exercises_file = "exercises2.csv"

student_info_file = input("Student information: ")
student_exercises_file = input("Exercises completed: ")

names = {}
with open(student_info_file) as new_file:
   for line in new_file:
      parts = line.split(";")
      if parts[0] == "id":
         continue
      names[parts[0]] = parts[1].strip() + " " + parts[2].strip()
# print(names)

points = {}
with open(student_exercises_file) as new_file:
   for line in new_file:
      parts = line.split(";")
      if parts[0] == "id":
         continue
      points[parts[0]] = int(parts[1]) + int(parts[2]) + int(parts[3]) + int(parts[4]) + int(parts[5]) + int(parts[6]) + int(parts[7])
# print(points)

for id, name in names.items():
   if id in points:
      point = points[id]
      print(f"{name} {point}")