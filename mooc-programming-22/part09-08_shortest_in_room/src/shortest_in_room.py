# WRITE YOUR SOLUTION HERE:
class Person:
    def __init__(self, name: str, height: int):
        self.name = name
        self.height = height

    def __str__(self):
        return self.name

class Room:
    def __init__(self):
        self.persons = []

    def add(self, person: Person):
        self.persons.append(person)
    
    def is_empty(self):
        return len(self.persons) == 0
    
    def shortest(self):
        if self.is_empty():
            return None
        else:
            shortest_height = self.persons[0].height
            for person in self.persons:
                if person.height <= shortest_height:
                    shortest_height = person.height
                    shortest_person = person
            return shortest_person
        
    def remove_shortest(self):
        if self.is_empty():
            return None
        else:
            the_shortest_removed = self.shortest()
            self.persons.remove(self.shortest())
            return the_shortest_removed

    def print_contents(self):
        total_height = 0
        for person in self.persons:
            total_height += person.height
        print(f"There are {len(self.persons)} persons in the room, and their combined height is {total_height} cm")
        for person in self.persons:
            print(f'{person.name} ({person.height} cm)')


# You can test your function by calling it within the following block
if __name__ == "__main__":
    room = Room()

    room.add(Person("Lea", 183))
    room.add(Person("Kenya", 172))
    room.add(Person("Nina", 162))
    room.add(Person("Ally", 166))
    room.print_contents()

    print()

    removed = room.remove_shortest()
    print(f"Removed from room: {removed.name}")

    print()

    room.print_contents()


# Answers!!!
# class Person:
#     def __init__(self, name: str, height: int):
#         self.name = name
#         self.height = height
 
#     def __str__(self):
#         return self.name
 
# class Room:
#     def __init__(self):
#         self.persons = []
 
#     def add(self, person: Person):
#         self.persons.append(person)
 
#     def is_empty(self):
#         return len(self.persons) == 0
 
#     def print_contents(self):
#         total_height = 0
#         for person in self.persons:
#             total_height += person.height
#         print(f"There are {len(self.persons)} persons in the room, and their combined height is {total_height} cm")
#         for person in self.persons:
#             print(f'{person.name} ({person.height} cm)')
 
#     def shortest(self):
#         shortest_person = None
#         height_of_shortest = 0
#         for person in self.persons:
#             if shortest_person is None or person.height < height_of_shortest:
#                 shortest_person = person
#                 height_of_shortest = person.height
 
#         return shortest_person
 
#     def remove_shortest(self):
#         # Utilizing the previous method
#         shortest_person = self.shortest()
#         # equals to conditon shortest person is not None
#         if shortest_person:
#             self.persons.remove(shortest_person)
 
#         return shortest_person