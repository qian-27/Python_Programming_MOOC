# Write your solution to exercise 1 here
strings = []
long_string = ""

total_length = 0

repeat_times = 0
the_character = ""

while True:
   input_text = input("Type in a string: ")
   if input_text == "":
      break
   strings.append(input_text)
   long_string += input_text
   total_length += len(input_text)

for letter in long_string:
   if long_string.count(letter) > repeat_times:
      repeat_times = long_string.count(letter)
      the_character = letter


print(f"Total number of strings: {len(strings)}")
print(f"The average length of the strings: {round(total_length / len(strings), 1)}")
print(f"The most common character in strings: {the_character}")