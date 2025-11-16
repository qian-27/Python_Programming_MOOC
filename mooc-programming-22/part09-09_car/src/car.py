# WRITE YOUR SOLUTION HERE:
class Car:
   def __init__(self):
      self.__petrol = 0
      self.__odometer = 0
   
   def fill_up(self):
      self.__petrol = 60
   
   def drive(self, km: int):
      if km < self.__petrol:
         self.__petrol -= km
         self.__odometer += km
      elif km >= self.__petrol:
         self.__odometer += self.__petrol
         self.__petrol = 0

   def __str__(self):
      return f"Car: odometer reading {self.__odometer} km, petrol remaining {self.__petrol} litres"



# You can test your function by calling it within the following block
if __name__ == "__main__":
   car = Car()
   print(car)
   car.fill_up()
   print(car)
   car.drive(20)
   print(car)
   car.drive(50)
   print(car)
   car.drive(10)
   print(car)
   car.fill_up()
   car.fill_up()
   print(car)


# Answers!!!
# class Car:
#     def __init__(self):
#         self.__petrol = 0
#         self.__driven = 0
 
#     def fill_up(self):
#         self.__petrol = 60
 
#     def drive(self, km: int):
#         if km > self.__petrol:
#             km = self.__petrol
 
#         self.__driven += km
#         self.__petrol -= km
 
#     def __str__(self):
#         return f"Car: odometer reading {self.__driven} km, petrol remaining {self.__petrol} litres"