# WRITE YOUR SOLUTION HERE:
class BankAccount:
   def __init__(self, name: str, account_num: str, balance: float):
      self.__name = name
      self.__account_num = account_num
      self.__balance = balance
   
   def deposit(self, amount: float):
      if amount > 0:
         self.__balance += amount
         self.__service_charge()
      else:
         raise ValueError
   
   def withdraw(self, amount: float):
      if amount <= self.__balance:
         self.__balance -= amount
         self.__service_charge()
      else:
         raise ValueError  

   # A getter method
   @property
   def balance(self):
      return self.__balance

   def __service_charge(self):
      self.__balance *= 0.99



# You can test your function by calling it within the following block
if __name__ == "__main__":
   account = BankAccount("Randy Riches", "12345-6789", 1000)
   account.withdraw(100)
   print(account.balance)
   account.deposit(100)
   print(account.balance)




# Answers!!!
# class BankAccount:
#     def __init__(self, owner: str, account_number: str, balance: float):
#         self.__owner = owner
#         self.__account_number = account_number
#         self.__balance = balance
 
#     def __service_charge(self):
#         self.__balance *= 0.99
 
#     def deposit(self, amount: float):
#         self.__balance += amount
#         self.__service_charge()
 
#     def withdraw(self, amount: float):
#         self.__balance -= amount
#         self.__service_charge()
 
#     @property
#     def balance(self):
#         return self.__balance