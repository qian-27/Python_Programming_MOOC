# write your solution here
# if False:
#    student_information = input("Student information: ")
#    exercise_points_file = input("Exercises completed: ")
#    exam_points_file = input("Exam points: ")
# else:
#    student_information = "students1.csv"
#    exercise_points_file = "exercises1.csv"
#    exam_points_file = "exam_points1.csv"

student_information = input("Student information: ")
exercise_points_file = input("Exercises completed: ")
exam_points_file = input("Exam points: ")

names = {}
with open(student_information) as new_file:
   for line in new_file:
      parts = line.split(";")
      if parts[0] == "id":
         continue
      names[parts[0]] = parts[1].strip() + " " + parts[2].strip()
# print(names)

exer_points = {}
with open(exercise_points_file) as new_file:
   for line in new_file:
      parts = line.split(";")
      if parts[0] == "id":
         continue
      exer_points_result = int((int(parts[1]) + int(parts[2]) + int(parts[3]) + int(parts[4]) + int(parts[5]) + int(parts[6]) + int(parts[7])) / 40 * 10)
      exer_points[parts[0]] = exer_points_result
# print(exer_points)

exam_points = {}
with open(exam_points_file) as new_file:
   for line in new_file:
      parts = line.split(";")
      if parts[0] == "id":
         continue
      exam_points[parts[0]] = int(parts[1]) + int(parts[2]) + int(parts[3])

for id, name in names.items():
   if id in exer_points:
      point = exer_points[id]
      if id in exam_points:
         point += exam_points[id]
         if point < 15:
            grade = 0
         elif point < 18:
            grade = 1
         elif point < 21:
            grade = 2
         elif point < 24:
            grade = 3
         elif point < 28:
            grade = 4
         else:
            grade = 5
         
         print(f"{name} {grade}")