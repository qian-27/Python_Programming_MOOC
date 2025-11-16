# Write your solution here
def factorials(n: int):
   results = {}
   fact = 1
   for i in range (1, n + 1):
      fact *= i
      results[i] = fact
      
   return results

   # def factorials(n: int):
   #  result = {}
   #  result[1] = 1
   #  for i in range(2, n + 1):
   #      result[i] = result[i-1] * i
   #  return result

# # You can test your function by calling it within the following block
if __name__ == "__main__":
   k = factorials(5)
   print(k[1])
   print(k[3])
   print(k[5])