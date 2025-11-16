# Write your solution here
from datetime import datetime, timedelta

eve_millennium = datetime(1999, 12, 31)

day = int(input("Day: "))
month = int(input("Month: "))
year = int(input("Year: "))

birthday = datetime(year, month, day)

difference = eve_millennium - birthday

if difference.days < 0:
   print("You weren't born yet on the eve of the new millennium.")
else:
   print(f"You were {difference.days} days old on the eve of the new millennium.")



# from datetime import datetime
 
# day = int(input("Day: "))
# month = int(input("Month: "))
# year = int(input("Year: "))
 
# time = datetime(year, month, day)
# millenium = datetime(1999, 12, 31)
 
# if time > millenium:
#     print ("You weren't born yet on the eve of the new millennium.")
# else:
#     ika = millenium - time
#     print (f"You were {ika.days} days old on the eve of the new millennium.")