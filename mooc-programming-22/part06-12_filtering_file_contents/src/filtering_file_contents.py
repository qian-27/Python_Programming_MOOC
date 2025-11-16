# Write your solution here
def filter_solutions():
   right_list = []
   wrong_list = []

   with open("solutions.csv") as new_file:
      for line in new_file:
         parts = line.split(";")
         name = parts[0]
         calculation = parts[1]
         result = int(parts[2])

         if "+" in calculation:
            numbers = calculation.split("+")
            real_result = int(numbers[0]) + int(numbers[1])
            if real_result == result:
               right_list.append([name, calculation, result])
            elif real_result != result:
               wrong_list.append([name, calculation, result])

         elif "-" in calculation:
            numbers = calculation.split("-")
            real_result = int(numbers[0]) - int(numbers[1])
            if real_result == result:
               right_list.append([name, calculation, result])
            elif real_result != result:
               wrong_list.append([name, calculation, result])
   
   with open("correct.csv", "w") as correct_file:
      for item in right_list:
         correct_file.write(f"{item[0]};{item[1]};{item[2]}\n")

   with open("incorrect.csv", "w") as incorrect_file:
      for item in wrong_list:
         incorrect_file.write(f"{item[0]};{item[1]};{item[2]}\n")


# You can test your function by calling it within the following block
# if __name__ == "__main__":
#    filter_solutions()


# def filter_solutions():
#     # Open all lines
#     with open("solutions.csv") as source, open("correct.csv", "w") as correct_file, open("incorrect.csv", "w") as incorrect_file:
#         for row in source:
#             # Split into pieces
#             pieces = row.split(";")
 
#             calculation = pieces[1]
#             result = pieces[2]
 
#             # Addition or subtraction?
#             if "+" in calculation:
#                 operands = calculation.split("+")
#                 # correct is True or False based on whether the calculation was correct or not
#                 correct = int(operands[0]) + int(operands[1]) == int(result)
#             else:
#                 operands = calculation.split("-")
#                 # correct is True or False based on whether the calculation was correct or not
#                 correct = int(operands[0]) - int(operands[1]) == int(result)
 
#             # Write to file
#             if correct:
#                 correct_file.write(row)
#             else:
#                 incorrect_file.write(row)
               