# Write your solution here:
class SuperHero:
    def __init__(self, name: str, superpowers: str):
        self.name = name
        self.superpowers = superpowers

    def __str__(self):
        return f'{self.name}, superpowers: {self.superpowers}'

class SuperGroup:
    def __init__(self, name: str, location: str):
        self._name = name
        self._location = location
        self._members = []
    
    # A getter method of name
    @property
    def name(self):
        return self._name

    # A getter method of location
    @property
    def location(self):
        return self._location

    def add_member(self, hero: SuperHero):
        self._members.append(hero)
    
    def print_group(self):
        print(f"{self.name}, {self.location}")
        print("Members:")
        for member in self._members:
            print(member)


# You can test your function by calling it within the following block
if __name__ == "__main__":
    superperson = SuperHero("SuperPerson", "Superspeed, superstrength")
    invisible = SuperHero("Invisible Inca", "Invisibility")
    revengers = SuperGroup("Revengers", "Emerald City")

    revengers.add_member(superperson)
    revengers.add_member(invisible)
    revengers.print_group()