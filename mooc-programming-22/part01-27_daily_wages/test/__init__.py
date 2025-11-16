# Write your solution here
hourly_wage = float(input("Hourly wage: "))
work_hours = float(input("Hours worked: "))
day = input("Day of the week: ")
 
if day != "Sunday":
    print(f"Daily wages: {hourly_wage * work_hours} euros")
 
else:
    print(f"Daily wages: {hourly_wage * work_hours * 2} euros")