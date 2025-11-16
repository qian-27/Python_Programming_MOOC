# Write your solution here
def check_week_number(week: str):
   try:
      week_number = int(week[5:])
      return True
   except:
      return False


def check_amount_of_numbers(numbers: list):
   if len(numbers) != 7:
      return False
   else:
      return True


def check_numbers_range(numbers: list):
   try: 
      for number in numbers:
         number = int(number)
         if number < 1 or number > 39:
            # number not in correct range
            return False
      # All numbers are correct
      return True
   except:
      # number is not a int
      return False


def check_repeated_numbers(numbers: list):
   for number in numbers:
      if numbers.count(number) > 1:
         return False
      else:
         return True


def check_everything(week: str, numbers_list: list):
   if check_week_number(week) and check_amount_of_numbers(numbers_list) and check_numbers_range(numbers_list) and check_repeated_numbers(numbers_list):
      return True


def filter_incorrect():
   correct_dict = {}
   with open("lottery_numbers.csv") as file:
      for line in file:
         line = line.replace("\n", "")
         parts = line.split(";")
         week = parts[0]
         numbers = parts[1]
         numbers_list = numbers.split(",")

         try:
            if check_everything(week, numbers_list) == True:
               if week not in correct_dict:
                  correct_dict[week] = numbers
         except:
            return False    


   with open("correct_numbers.csv", "w") as new_file:
      for week, numbers in correct_dict.items():
         new_file.write(f'{week};')
         new_file.write(numbers)
         new_file.write(f'\n') 



# You can test your function by calling it within the following block
if __name__ == "__main__":
   filter_incorrect()



# def filter_incorrect():
#     with open("lottery_numbers.csv") as input_file, open("correct_numbers.csv", "w") as result_file:
#         for row in input_file:
#             parts = row.strip().split(";")
#             if len(parts) != 2:
#                 continue
#             week = parts[0].split(" ")
#             error = False
#             if len(week) != 2 or week[0] != "week":
#                 error = True
#             try:
#                 mika = int(week[1])
#             except:
#                 error = True
#             number_list = parts[1].split(",")
#             if len(number_list) != 7:
#                 error = True
 
#             # numbers already listed --> to find out duplicates
#             listed = []
#             for item in number_list:
#                 try:
#                     number = int(item)
#                     if number < 1 or number > 39 or number in listed:
#                         error = True
#                     listed.append(number)
#                 except:
#                     error = True
#             if not error:
#                 result_file.write(row)
