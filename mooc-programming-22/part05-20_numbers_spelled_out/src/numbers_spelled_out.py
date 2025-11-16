# Write your solution here


def dict_of_numbers():
   less_than_20 = ["", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"]
   tens = ["","ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"]
   numbers = {}
   for key in range(0, 100):
      if key == 0:
         numbers[key] = "zero"
      elif key < 20:
         numbers[key] = less_than_20[key]
      elif key >= 20 and key % 10 == 0:
         numbers[key] = tens[key//10]
      elif key >= 20 and key % 10 != 0:
         numbers[key] = tens[key // 10] + "-" + less_than_20[key % 10]
   return numbers

# You can test your function by calling it within the following block
if __name__ == "__main__":
   numbers = dict_of_numbers()
   print(numbers[2])
   print(numbers[11])
   print(numbers[45])
   print(numbers[99])
   print(numbers[0])