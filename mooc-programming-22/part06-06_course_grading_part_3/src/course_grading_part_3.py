# if False:
#    student_file = input("Student information: ")
#    exercise_file = input("Exercises completed: ")
#    exam_file = input("Exam points: ")
# else:
#    student_file = "students1.csv"
#    exercise_file = "exercises1.csv"
#    exam_file = "exam_points1.csv"

student_file = input("Student information: ")
exercise_file = input("Exercises completed: ")
exam_file = input("Exam points: ")

names = {}
with open(student_file) as new_file:
   for line in new_file:
      parts = line.split(";")
      if parts[0] == "id":
         continue
      names[parts[0]] = parts[1].strip() + " " + parts[2].strip()
# print(names)


exercise_total_points_dict = {}
with open(exercise_file) as new_file:
   for line in new_file:
      parts = line.split(";")
      if parts[0] == "id":
         continue
      exercise_total_points = int(parts[1]) + int(parts[2]) + int(parts[3]) + int(parts[4]) + int(parts[5]) + int(parts[6]) + int(parts[7])
      exercise_total_points_dict[parts[0]] = exercise_total_points
# print(exercise_total_points_dict)

exercise_award_points = {}
for student_id in names:
   exercise_award_points[student_id] = exercise_total_points_dict[student_id] // 4
# print(exercise_award_points)


exam_points = {}
with open(exam_file ) as new_file:
   for line in new_file:
      parts = line.split(";")
      if parts[0] == "id":
         continue
      exam_points[parts[0]] = int(parts[1]) + int(parts[2]) + int(parts[3])
# print(exam_points)


total_points = {}
for student_id in names:
   total_points[student_id] = exercise_award_points[student_id] + exam_points[student_id]
# print(total_points)

def grade(points):
   i = 0
   limits = [15, 18, 21, 24, 28]
   while i < 5 and points >= limits[i]:
       i += 1

   return i


print(f'{"name":30}{"exec_nbr":<9} {"exec_pts.":<10}{"exm_pts.":10}{"tot_pts.":10}{"grade":10}')
for student_id, name in names.items():
   print(f"{name:30}", end="")
   print(f"{exercise_total_points_dict[student_id]:<10}", end="")
   print(f"{exercise_award_points[student_id]:<10}", end="")
   print(f"{exam_points[student_id]:<10}", end="")
   print(f"{total_points[student_id]:<10}", end="")
   print(f"{grade(total_points[student_id])}")
