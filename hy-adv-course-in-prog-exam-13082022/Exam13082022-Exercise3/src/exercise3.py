# Exercise 3
class FileHandler():
   def __init__(self, filename):
      self.__filename = filename
   
   def read_line(self):
      with open(self.__filename, 'r') as new_file:
         x = len(new_file.readlines())
         return x
      

   def add_history(self, list):
      with open(self.__filename, "a") as new_file:
         new_file.write(";".join(list) + "\n")

   def show_history(self):
      with open(self.__filename) as new_file:
         for line in new_file:
            parts = line.strip().split(';')
            print(f"{parts[0]} {parts[1]} {parts[2]} {parts[3]} {parts[4]}")
   
   def clear_history(self):
      with open(self.__filename, "w") as new_file:
         new_file.close()



class CalculatorApplication:
   def __init__(self):
      self.__filehandler = FileHandler("history.txt")

   def help(self):
      print("Commands: ")
      print("0 - end program")
      print("1 - calculate addition (+)")
      print("2 - calculate subtraction (-)")
      print("3 - calculate multiplication (*)")
      print("4 - calculate division (/)")
      print("5 - show history")
      print("6 - empty history")
      print("7 - show commands")

   # Calculating addition
   def add(self, x, y):
       return x + y
   # Calculating subtraction
   def subtract(self, x, y):
       return x - y
   # Calculating multiplication
   def multiply(self, x, y):
       return x * y
   # Calculating division
   def divide(self, x, y):
       return x / y

   def execute(self):
      print("Calculator")
      x = self.__filehandler.read_line()
      print(f"{x} calculations stored in history")
      self.help()
      while True:
         command = input("Select command: ")
         if command == "0":
            print("Shutting down program...")
            break

         if command in ["1", "2", "3", "4"]:
            if command == "1":
               print("Addition (+)")
               x = float(input("Input number: "))
               y = float(input("Input number: "))
               result = self.add(x, y)
               list = [str(x), "+", str(y), "=", str(result)]
               self.__filehandler.add_history(list)

            elif command == "2":
               print("Subtraction (-)")
               x = float(input("Input number: "))
               y = float(input("Input number: "))
               result = self.subtract(x, y)
               list = [str(x), "-", str(y), "=", str(result)]
               self.__filehandler.add_history(list)

            elif command == "3":
               print("Multiplication (*)")
               x = float(input("Input number: "))
               y = float(input("Input number: "))
               result = self.multiply(x, y)
               list = [str(x), "*", str(y), "=", str(result)]
               self.__filehandler.add_history(list)

            elif command == "4":
               print("Division (/)")
               x = float(input("Input number: "))
               y = float(input("Input number: "))
               result = self.divide(x, y)
               list = [str(x), "/", str(y), "=", str(result)]
               self.__filehandler.add_history(list)

            print(f"Result: {result}")

         elif command == "5":
            # x = len((self.__filehandler.show_history()).readlines())
            # print(len(self.__filehandler.show_history()))
            print(f"{int(x)} calculations stored in history")
            self.__filehandler.show_history()
         elif command == "6":
            self.__filehandler.clear_history()
            print("History cleared.")

         elif command == "7":
            self.help()


# store calculations in the file named history.txt.
# The program should create the file history.txt at runtime, 


# You can test your function by calling it within the following block
if __name__ == "__main__":
   application = CalculatorApplication()
   application.execute()