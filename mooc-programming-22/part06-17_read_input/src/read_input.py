# Write your solution here
def read_input(text, small_num, big_num):
   while True:
      try:
         input_num = (input(text))
         number = int(input_num)
         if number >= small_num and number <= big_num:
            return number
      except ValueError:
         pass
      
      print(f"You must type in an integer between {small_num} and {big_num}")

# You can test your function by calling it within the following block
if __name__ == "__main__":
   number = read_input('Enter a number', 5, 10)


# def read_input(prompt: str, lower_limit: int, upper_limit: int):
#     while True:
#         error = False
#         try:
#             number = int(input(prompt))
#             if number < lower_limit or number > upper_limit:
#                 error = True
#         except:
#             error = True
#         if error:
#             print(f"You must type in an integer between {lower_limit} and {upper_limit}")
#         else:
#             return number