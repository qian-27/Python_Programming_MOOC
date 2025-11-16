# Write your solution here
students_num = int(input("How many students on the course?"))
group_size = int(input("Desired group size?"))
 
number_of_groups = students_num / group_size
number_of_groups2 = students_num // group_size
 
if number_of_groups2 == number_of_groups:
    print(f"Number of groups formed: {int(number_of_groups2)}")
 
elif number_of_groups2 != number_of_groups:
    print(f"Number of groups formed: {int(number_of_groups2 + 1)}")
