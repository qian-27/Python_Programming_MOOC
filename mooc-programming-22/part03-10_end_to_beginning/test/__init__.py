# Write your solution here
input_string = input("Please type in a string: ")
length_of_input_string = len(input_string)

if length_of_input_string > 0:
    index = length_of_input_string - 1
    while index < length_of_input_string and index >= 0:
        print(input_string[index])
        index -= 1 
else:
    print("The input string is empty. There is no first character.")