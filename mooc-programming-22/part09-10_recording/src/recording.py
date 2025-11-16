# WRITE YOUR SOLUTION HERE:
class Recording:
   def __init__(self, length: int):
      if length >= 0:
         self.__length = length
      else:
         raise ValueError
   
   # A getter method
   @property
   def length(self):
      return self.__length

   # A setter method
   @length.setter
   def length(self, length):
      if length >= 0:
         self.__length = length
      else:
         raise ValueError



# You can test your function by calling it within the following block
if __name__ == "__main__":
   the_wall = Recording(-1)
   print(the_wall.length)
   the_wall.length = 44
   print(the_wall.length)
   the_wall.length = -1
   print(the_wall.length)




# Answers!!！
# class Recording:
   #  def __init__(self, length: int):
   #      if length >= 0:
   #          self.__length = length
   #      else:
   #          raise ValueError("Negative length is not possible")
 
   #  @property
   #  def length(self):
   #      return self.__length
 
   #  @length.setter 
   #  def length(self, length):
   #      if length >= 0:
   #          self.__length = length
   #      else:
   #          raise ValueError("Negative length is not possible")
