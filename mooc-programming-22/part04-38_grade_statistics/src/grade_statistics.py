# Write your solution here
total_points_list = []
grade_list = []

while True:
   exam_and_exercises = input("Exam points and exercises completed: ")
   
   if exam_and_exercises == "":
      break
   
   input_list = exam_and_exercises.split() 
   exam_points = int(input_list[0])
   exercises_completed = int(input_list[1])
   result = int(exam_points + exercises_completed / 10)

   total_points_list.append(result)

   if result < 15 or exam_points < 10:
      grade = 0
   elif result < 18:
      grade = 1
   elif result < 21:
      grade = 2
   elif result < 24:
      grade = 3
   elif result < 28:
      grade = 4
   else:
      grade = 5
   
   grade_list.append(grade)



num_5 = grade_list.count(5)
num_4 = grade_list.count(4)
num_3 = grade_list.count(3)
num_2 = grade_list.count(2)
num_1 = grade_list.count(1)
num_0 = grade_list.count(0)

len_list = len(grade_list)
average_point = sum(total_points_list) / len_list
pass_percentage = (len_list - grade_list.count(0)) / len_list * 100

print("Statistics:")
print(f"Points average: {average_point}")
print(f"Pass percentage: {round(pass_percentage, 1)}")
print(f"Grade distribution:")
print(f'5: {"*" * num_5}')
print(f'4: {"*" * num_4}')
print(f'3: {"*" * num_3}')
print(f'2: {"*" * num_2}')
print(f'1: {"*" * num_1}')
print(f'0: {"*" * num_0}')



