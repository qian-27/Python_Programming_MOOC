# Write your solution here
def counter(max: int):
   list = []
   i = 2
   while i < max:
      list.append(i)
      i += 1
   return list

def prime_numbers():
   prime = 2
   while prime < 120:
      if prime < 4:
         yield prime
      else:
         list = counter(prime)
         wrong = 0
         for i in list:
            if prime % i == 0:
               wrong += 1
         if wrong == 0:
            yield prime

      prime += 1


# You can test your function by calling it within the following block
if __name__ == "__main__":
   numbers = prime_numbers()
   for i in range(8):
      print(next(numbers))



# Answers!!!
# def prime_numbers():
#     number = 1
#     while True:
#         if is_prime(number):
#             yield number
#         number += 1
 
# # Helper method for checking if number is prime
# def is_prime(number: int):
#     if number < 2:
#         return False
#     # Possible divisor is between 2 and number-1
#     for i in range(2, number):
#         if number % i == 0:
#             return False
#     return True