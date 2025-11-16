# TEE RATKAISUSI TÄHÄN:
class Money:
    def __init__(self, euros: int, cents: int):
        self.__euros = euros
        self.__cents = cents
    
    # Equal to
    def __eq__(self, another):
        return self.__euros + self.__cents == another.__euros + another.__cents

    # Not equal to
    def __ne__(self, another):
        return self.__euros + self.__cents != another.__euros + another.__cents

    # Less than
    def __lt__(self, another):
        return self.__euros + self.__cents < another.__euros + another.__cents

    # Greater than
    def __gt__(self, another):
        return self.__euros + self.__cents > another.__euros + another.__cents
  
    # Addition
    def __add__(self, another):
        euross = self.__euros + another.__euros
        cents = self.__cents + another.__cents
        if  cents >= 100:
            euross += 1
            cents = cents - 100
        return Money(euross, cents)

    # Subtraction
    def __sub__(self, another):
        euros = self.__euros - another.__euros
        if euros >= 0:
            cents = self.__cents - another.__cents
            if cents < 0:
                euros -= 1
                cents += 100
                if euros < 0:
                    raise ValueError("a negative result is not allowed")
            return Money(euros, cents)

        else:
            raise ValueError("a negative result is not allowed")
    
    def __str__(self):
        # f-string has a handy feature for adding leading zeros:
        # :02d for example means, that output has at least 2 digit
        return f"{self.__euros}.{self.__cents:02d} eur"




# You can test your function by calling it within the following block
if __name__ == "__main__":
    e1 = Money(4, 5)
    e2 = Money(2, 95)

    e3 = e1 + e2
    # e4 = e1 - e2

    # print(e3)
    # print(e4)

    e5 = e2-e1




# Answers!!!
# class Money:
#     def __init__(self, euros: int, cents: int):
#         self.__euros = euros
#         self.__cents = cents
 
#     def __str__(self):
#         # f-string has a handy feature for adding leading zeros:
#         # :02d for example means, that output has at least 2 digit
#         return f"{self.__euros}.{self.__cents:02d} eur"
 
#     # Helper method for returning the value in cents
#     # --> makes the comparisons easier
#     def __value(self):
#         return self.__euros * 100 + self.__cents
 
#     # Another helper method which converts cents to value
#     def __set_value(self, cents: int):
#         self.__euros = cents // 100
#         self.__cents = cents - self.__euros * 100
 
#     def __eq__(self, other: "Money"):
#         return self.__value() == other.__value()
 
#     def __lt__(self, other: "Money"):
#         return self.__value() < other.__value()
 
#     def __gt__(self, other: "Money"):
#         return self.__value() > other.__value()
 
#     def __ne__(self, other: "Money"):
#         return self.__value() != other.__value()
 
#     def __add__(self, other: "Money"):
#         msum = Money(0,0)
#         msum.__set_value(self.__value() + other.__value())
#         return msum
 
#     def __sub__(self, other: "Money"):
#         difference = self.__value() - other.__value()
#         if difference < 0:
#             raise ValueError("a negative result is not allowed")
#         dmoney = Money(0,0)
#         dmoney.__set_value(self.__value() - other.__value())
#         return dmoney