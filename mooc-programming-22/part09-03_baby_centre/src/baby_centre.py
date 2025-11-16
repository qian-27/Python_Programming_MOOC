# WRITE YOUR SOLUTION HERE:
#Note! Do not change the class Person!

class Person:
    def __init__(self, name: str, age: int, height: int, weight: int):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight


class BabyCentre:
    def __init__(self):
        self.number_of_weigh_ins = 0
        self.input_times = 0

    def weigh(self, person: Person):
        self.number_of_weigh_ins = person.weight
        self.input_times += 1
        return self.number_of_weigh_ins
    
    def feed(self, person: Person):
        self.number_of_weigh_ins = person.weight
        person.weight = self.number_of_weigh_ins + 1
        return self.number_of_weigh_ins
    
    def weigh_ins(self):
        return self.input_times


# You can test your function by calling it within the following block
if __name__ == "__main__":
    baby_centre = BabyCentre()

    eric = Person("Eric", 1, 110, 7)
    peter = Person("Peter", 33, 176, 85)

    print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")

    baby_centre.weigh(eric)
    baby_centre.weigh(eric)

    print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")

    baby_centre.weigh(eric)
    baby_centre.weigh(eric)
    baby_centre.weigh(eric)
    baby_centre.weigh(eric)

    print(f"Total number of weigh-ins is {baby_centre.weigh_ins()}")



# Answers!!!
# class Person:
#     def __init__(self, name: str, age: int, height: int, weight: int):
#         self.name = name
#         self.age = age
#         self.height = height
#         self.weight = weight
 
# class BabyCentre:
#     def __init__(self):
#         self.number_of_weigh_ins = 0
 
#     def weigh(self, person: Person):
#         # return the weight of the person passed as an argument
#         self.number_of_weigh_ins += 1
#         return person.weight
 
#     def feed(self, person: Person):
#         person.weight += 1
 
#     def weigh_ins(self):
#         return self.number_of_weigh_ins