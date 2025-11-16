# Write your solution here
def add_student(database: dict, student_name: str):
   courses_dict = {}
   database[student_name] = courses_dict
   return database


def add_course(database: dict, student_name: str, course_info: tuple):
   if student_name in database:
      if course_info[1] == 0:
         return database
      else:
         if course_info[0] not in database[student_name]:
            database[student_name][course_info[0]] = course_info[1]
         elif course_info[0] in database[student_name] and course_info[1] > database[student_name][course_info[0]]:
            database[student_name][course_info[0]] = course_info[1]
   return database
   

def print_student(database: dict, student_name: str):
   if student_name in database:
      print(f"{student_name}:")
      if len(database[student_name]) == 0:
         print(" no completed courses")
      else:
         print(f" {len(database[student_name])} completed courses:")
         grade = 0
         for key, value in database[student_name].items():
            x = " "
            print(x, key, value)
            grade += value
         average_grade = grade / (len(database[student_name]))
         print(f" average grade {round(average_grade, 1)}")
   else:
      print(f"{student_name}: no such person in the database")


def summary(database: dict):
   student_number = len(database)
   print(f"students {student_number}")

   most_courses = 0
   most_completed_student = ""
   for student in database:
      if len(database[student]) > most_courses:
         most_courses = len(database[student])
         most_completed_student = student
   print(f"most courses completed {most_courses} {most_completed_student}")

   # Following code is about best average grade with it's student
   average_grade_dict = {}
   for student_name in database:
      grade = 0
      for key, value in database[student_name].items():
         # print(key, value)
         grade += value
      average_grade = round(grade / (len(database[student_name])), 1)
      average_grade_dict[student_name] = average_grade
      # print(f" average grade {average_grade}")

   # print(average_grade_dict)
   better_grade = 0
   better_student = " "
   for student_name in average_grade_dict:
      if average_grade_dict[student_name] > better_grade:
         better_grade = average_grade_dict[student_name]
         better_student = student_name
   print(f"best average grade {better_grade} {better_student}")

   
   


# You can test your function by calling it within the following block
if __name__ == "__main__":
   students = {}
   add_student(students, "Emily")
   add_student(students, "Peter")
   add_course(students, "Emily", ("Software Development Methods", 4))
   add_course(students, "Emily", ("Software Development Methods", 5))
   add_course(students, "Peter", ("Data Structures and Algorithms", 3))
   add_course(students, "Peter", ("Models of Computation", 0))
   add_course(students, "Peter", ("Data Structures and Algorithms", 2))
   add_course(students, "Peter", ("Introduction to Computer Science", 1))
   add_course(students, "Peter", ("Software Engineering", 3))
   summary(students)


