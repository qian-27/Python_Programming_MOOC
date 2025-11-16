# Tee ratkaisusi tähän:
class DecreasingCounter:
    def __init__(self, initial_value: int):
        self.value = initial_value
        self.store_original_value = initial_value

    def print_value(self):
        print("value:", self.value)

    def decrease(self):
        if 1 <= self.value:
            self.value -= 1
            return True

        return False
    
    def set_to_zero(self):
        self.value = 0

    def reset_original_value(self):
        self.value = self.store_original_value



# You can test your function by calling it within the following block
if __name__ == "__main__":
    counter = DecreasingCounter(55)
    counter.decrease()
    counter.decrease()
    counter.decrease()
    counter.decrease()
    counter.print_value()
    counter.reset_original_value()
    counter.print_value()



# class DecreasingCounter:
#     def __init__(self, initial_value: int):
#         self.value = initial_value
#         self.original_value = initial_value
 
#     def print_value(self):
#         print("value:", self.value)
 
#     def decrease(self):
#         if self.value > 0:
#             self.value -= 1
 
#     def set_to_zero(self):
#         self.value = 0
 
#     def reset_original_value(self):
#         self.value = self.original_value

