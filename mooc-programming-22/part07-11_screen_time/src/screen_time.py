# # Write your solution here
from datetime import datetime, timedelta

# if False:
#    file_name = input("Filename:")
#    input_start_date = input("Starting date:")
#    input_days = int(input("How many days:"))
# if True:
#    file_name = "late_june.txt"
#    input_start_date = "30.3.2020"
#    input_days = 3

file_name = input("Filename: ")
input_start_date = input("Starting date: ")
input_days = int(input("How many days:"))

start_date = datetime.strptime(input_start_date,"%d.%m.%Y")
screen_date = start_date.strftime("%d.%m.%Y")
# print(input_start_date)
# print(start_date)
# print(screen_date)

print("Please type in screen time in minutes on each day (TV computer mobile): ")


screen_time_dict = {}
add_one_day = 1
for i in range(input_days):
   screen_time = input(f"Screen time {screen_date}: ")
   screen_time = screen_time.split(" ")
   screen_time_dict[screen_date] = screen_time

   one_day = timedelta(days=add_one_day)
   screen_date = (start_date + one_day).strftime("%d.%m.%Y")
   add_one_day += 1
print(screen_time_dict)

start_format = start_date.strftime("%d.%m.%Y")
end_format = (start_date + timedelta(days=(input_days-1))).strftime("%d.%m.%Y")
time_period = f'{start_format}-{end_format}'
print(start_format)
print(end_format)
print(time_period)

total_min = 0 
for key,value in screen_time_dict.items():
    for item in value:
        total_min += int(item)
average_min = round(total_min / input_days, 1)
print(total_min)
print(average_min)

# 24.06.2020: 60/120/0

with open(file_name,"w") as my_file:
    my_file.write(f"Time period: {time_period}\n")
    my_file.write(f"Total minutes: {total_min}\n")
    my_file.write(f"Average minutes: {average_min}\n")
    for key,value in screen_time_dict.items():
      # my_file.write(f"{key}: {value}\n")
      number = ""
      for item in range(len(value)):
         if item == len(value) -1:
            number += value[item] 
         else:
            number += value[item] +"/"
      my_file.write(f"{key}: {number}\n")

print(f"Data stored in file {file_name}")






# Answer
# from datetime import datetime, timedelta
 
# week = timedelta(days=7)
 
# def format(aika):
#     return aika.strftime("%d.%m.%Y")
 
# file = input("Filename: ")
# start = input("Starting date: ").split('.')
# days = int(input("How many days: "))
# print("Please type in screen time in minutes on each day (TV computer mobile):")
 
# screen_times = []
# total = 0
# start = datetime(int(start[2]), int(start[1]), int(start[0]))
 
# for i in range(days):
#     day = start + timedelta(days=i)
#     times = input(f"Screen time {format(day)}: ").split(' ')
#     tv = int(times[0])
#     pc = int(times[1])
#     mobile = int(times[2])
#     total += tv + pc + mobile
#     screen_times.append((day, tv, pc, mobile) )
 
# with open(file, "w") as tdsto:
#     tdsto.write(f"Time period: {format(start)}-{format(start + timedelta(days=(days-1)))}\n")
#     tdsto.write(f"Total minutes: {total}\n")
#     tdsto.write(f"Average minutes: {total/days:.1f}\n")
#     for pv, tv, pc, mob in screen_times:
#         tdsto.write(f"{format(pv)}: {tv}/{pc}/{mob}\n")
 
# print(f"Data stored in file {file}")


 

 



