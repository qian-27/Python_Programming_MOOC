# Exercise 2
class Driver:
   def __init__(self, name: str, year_of_birth: int,
           height: int, weight: int):
      self.name = name
      self.year_of_birth = year_of_birth
      self.height = height
      self.weight = weight
   def __str__(self):
      return (f"Driver(name = {self.name}, " +
         f"year_of_birth = {self.year_of_birth}, " +
         f"height = {self.height}, weight = {self.weight})")

class RallyCar:
   def __init__(self, make: str, top_speed: int, driver: Driver):
      self.make = make
      self.top_speed = top_speed
      self.driver = driver

   def __str__(self):
      return (f"RallyCar(make = {self.make}, " +
         f"top_speed = {self.top_speed}, " +
         f"driver = {self.driver})")


def fastest_cars(cars: list, speed: int):
   return [car.make for car in cars if car.top_speed > speed]

def drivers_of_make(cars: list, make: str):
   return [car.driver.name for car in cars if car.make == make]

def youngest_and_oldest_driver(drivers: list):
   def order_by_year(driver: Driver):
      return driver.year_of_birth
   new_list = sorted(drivers, key=order_by_year, reverse=True)
   youngest = new_list[0].name
   oldest = new_list[-1].name
   return (youngest, oldest)

def by_speed(cars: list):
   def order_by_speed(car: RallyCar):
      return car.top_speed
   return sorted(cars, key=order_by_speed)



# You can test your function by calling it within the following block
if __name__ == "__main__":
   d1 = Driver("Bob", 1990, 179, 50)
   d2 = Driver("John", 1993, 179, 50)
   d3 = Driver("Miky", 1880, 179, 50)
   d4 = Driver("Lee", 2000, 179, 50)
   d5 = Driver("Tom", 2021, 179, 50)

   drivers = [d1, d2, d3, d4, d5]


   car1 = RallyCar("Toyota", 150, d1)
   car2 = RallyCar("Toyota", 180, d2)
   car3 = RallyCar("Ford", 200, d3)
   car4 = RallyCar("Tesla", 190, d4)
   car5 = RallyCar("BMW", 210, d5)

   cars = [car1, car2, car3, car4, car5]

   print("Part a print out")
   print(fastest_cars(cars, 200))

   print("Part b print out")
   print(drivers_of_make(cars, "Toyota"))

   print("Part c print out")
   print(youngest_and_oldest_driver(drivers))

   print("Part d print out")
   for car in by_speed(cars):
      print(car)
