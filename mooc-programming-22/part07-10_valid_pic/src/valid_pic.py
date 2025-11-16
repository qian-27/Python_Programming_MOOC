# Write your solution here
from datetime import datetime

def is_date_valid(year: int, month: int, day: int):
   try:
      datetime(year, month, day)
      return True
   except ValueError:
      return False


def is_it_valid(pic: str):
   day = int(pic[0:2])
   month = int(pic[2:4])
   yy = int(pic[4:6])
   century_marker = pic[6]

   year = 0
   if century_marker == "+":
      year = 1800 + yy
   elif century_marker == "-":
      year = 1900 + yy
   elif century_marker == "A":
      year = 2000 + yy
   
   

   control_character = pic[10]
   digits = int(pic[0:6] + pic[7:10])
   print(day,month,yy,century_marker,year,control_character,digits)
   characters = "0123456789ABCDEFHJKLMNPRSTUVWXY"
   remainder = digits % 31
   real_control_character = characters[remainder]

   if len(pic) == 11:
      if control_character == real_control_character:
         if is_date_valid(year, month, day) == True:
            return True
         else:
            return False
      else:
         return False
   else:
      return False
   




# You can test your function by calling it within the following block
if __name__ == "__main__":
   # is_it_valid("080842-720N")
   print(is_date_valid(2022, 2, 30))





# from datetime import datetime
 
# def is_it_valid(pic: str):
#     if len(pic) != 11:
#         return False
#     numbers = pic[:6]+pic[7:10]
#     for x in numbers:
#         if x not in "0123456789":
#             return False
#     century_marker = pic[6]
#     if century_marker not in "+-A":
#         return False
#     day = int(pic[:2])
#     month = int(pic[2:4])
#     year = int(pic[4:6])
#     if century_marker == "+":
#         year += 1800
#     if century_marker == "-":
#         year += 1900
#     if century_marker == "A":
#         year += 2000
#     try:
#         test = datetime(year, month, day)
#     except:
#         return False
#     characters = "0123456789ABCDEFHJKLMNPRSTUVWXYZ"
#     index = int(numbers)%31
#     return characters[index] == pic[-1]