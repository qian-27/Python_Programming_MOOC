# WRITE YOUR SOLUTION HERE:
class SimpleDate:
   def __init__(self, day: int, month: int, year: int):
      self.__day = day
      self.__month = month
      self.__year = year

   def __value(self):
      return self.__year * 12 * 30 + self.__month * 30 + self.__day

   def __set_value(self, days: int):
      self.__year = days // 30 // 12
      self.__month = (days - self.__year * 30 * 12) // 30
      self.__day = days - self.__year * 30 * 12 - self.__month * 30
   
   def __eq__(self, other: "SimpleDate"):
      return self.__value() == other.__value()
   
   def __ne__(self, other: "SimpleDate"):
      return self.__value() != other.__value()
   
   def __gt__(self, other: "SimpleDate"):
      return self.__value() > other.__value()
 
   def __lt__(self, other: "SimpleDate"):
      return self.__value() < other.__value()
   
   def __add__(self, other: int):
      dmy = SimpleDate(0, 0 , 0)
      days = self.__value() + other
      dmy.__set_value(days)
      return dmy

   def __sub__(self, other: "SimpleDate"):
      days = abs(self.__value() - other.__value())
      return days
   
   def __str__(self):
      return f"{self.__day}.{self.__month}.{self.__year}"
      

# You can test your function by calling it within the following block
if __name__ == "__main__":
   d1 = SimpleDate(4, 10, 2020)
   d2 = SimpleDate(2, 11, 2020)
   d3 = SimpleDate(28, 12, 1985)

   print(d2-d1)
   print(d1-d2)
   print(d1-d3)



# Answers!!!
# class SimpleDate:
#     def __init__(self, pv: int, month: int, year: int):
#         self.__pv = pv
#         self.__month = month
#         self.__year = year
 
#     def __str__(self):
#         return f'{self.__pv}.{self.__month}.{self.__year}'
 
#     # Comparisons are easier, when date is converted to days
#     def __value(self):
#         return self.__year * 360 + self.__month * 30 + self.__pv
 
#     # Converst days back to date
#     def __to_date(self, days: int):
#         months = days // 30
#         years = months // 12
#         days -= months * 30
#         months -= years * 12
#         return SimpleDate(days, months, years)
 
#     def __lt__(self, other: "SimpleDate"):
#         return self.__value() < other.__value()
 
#     def __gt__(self, other: "SimpleDate"):
#         return self.__value() > other.__value()
 
#     def __eq__(self, other: "SimpleDate"):
#         return self.__value() == other.__value()
        
#     def __ne__(self, other: "SimpleDate"):
#         return self.__value() != other.__value()
 
#     def __add__(self, days_to_add: int):
#         return self.__to_date(self.__value() + days_to_add)
 
#     def __sub__(self, other: "SimpleDate"):
#         # abs(x) returns the absolute value of x
#         return abs(self.__value() - other.__value())