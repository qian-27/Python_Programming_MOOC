# Write your solution here!
class  NumberStats:
    def __init__(self):
        self.numbers = 0
        self.count = 0
        self.sum = 0
        self.sum_even = 0
        self.sum_odd = 0

    def add_number(self, number:int):
        self.number = number
        self.count += 1
        self.sum += number
        if number % 2 == 0:
            self.sum_even += number
        else:
            self.sum_odd += number

    def count_numbers(self):
        return self.count
    
    def get_sum(self):
        return self.sum

    def average(self):
        the_sum = self.sum
        the_length = self.count
        if self.count > 0:
            the_average = the_sum / the_length
            return the_average
        else:
            return 0
    
    def sum_of_even(self):
        return self.sum_even
    
    def sum_of_odd(self):
        return self.sum_odd

# def main():
# Part3 User input
stats = NumberStats()
input_num = int(input("Please type in integer numbers: \n"))
while input_num >= 0:
    stats.add_number(input_num)
    input_num = int(input())
print(f"Sum of numbers: {stats.get_sum()}")
print(f"Mean of numbers: {stats.average()}")
# Part 4 Multiple sums
print(f"Sum of even numbers: {stats.sum_of_even()}")
print(f"Sum of odd numbers: {stats.sum_of_odd()}")


# Delete "if block" While Testing In The Mooc 
# You can test your function by calling it within the following block
# if __name__ == "__main__":
#     main()
    # stats = NumberStats()
    # stats.add_number(3)
    # stats.add_number(-1)
    # stats.add_number(-2)
    # stats.add_number(-2)
    # print("Numbers added:", stats.count_numbers())
    # print("Sum of numbers:", stats.get_sum())
    # print("Mean of numbers:", stats.average())



# Answers
# class  NumberStats:
#     def __init__(self):
#         self.numbers = []
 
#     def add_number(self, number:int):
#         self.numbers.append(number)
 
#     def count_numbers(self):
#         return len(self.numbers)
 
#     def get_sum(self):
#         return sum(self.numbers)
 
#     def average(self):
#         if not self.numbers:
#             return 0.0
#         else:
#             return self.get_sum() / self.count_numbers()
 
# stats = NumberStats()
# even = NumberStats()
# odd = NumberStats()
# while True:
#     number = int(input("Give a number: "))
#     if number == -1:
#         break
 
#     stats.add_number(number)
#     if number % 2 == 0:
#         even.add_number(number)
#     else:
#         odd.add_number(number)
 
# print("Sum of numbers:", stats.get_sum())
# print("Mean of numbers:", stats.average())
# print("Sum of even numbers:", even.get_sum())
# print("Sum of odd numbers:", odd.get_sum())
