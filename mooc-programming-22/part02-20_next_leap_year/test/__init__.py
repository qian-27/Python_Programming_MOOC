# Write your solution here
year = int(input("Year: "))

leap_year = year + 1
while True:
    if leap_year % 100 == 0 and leap_year % 400 != 0:
        leap_year += 1
    elif leap_year % 400 == 0:
        break
    elif leap_year % 4 == 0:
        break
    else:
        leap_year += 1

print(f"The next leap year after {year} is {leap_year}")
