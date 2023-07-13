"""
    Classses -
        - Like a blueprint
        - Encapsulates related data and functionality

    Instantiation -
        - Creates an instance of the class
"""


class Animal:  # PascalCase

    # class level data
    animals = []

    map = [ #multidimensional array
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
        [None, None, None, None, None, None, None, None, None, None],
    ]

    def __init__(self, name, species, age, energy=100): # self = instance level data
        self.name = name
        self.species = species
        self.age = age

        self.energy = energy
        self.location = {'x': 0, 'y': 0}

        Animal.add_animal(self)

    def get_description(self):
        return f"{self.name} is a {self.species} and is {self.age} years old."

    def walk(self, distance):
        self.energy -= distance
        return f"{self.name} walked {distance} kilometers and lost {distance} energy!"

    def eat(self, food, energy):
        self.energy += energy
        return f"{self.name} ate {food} and gained {energy} energy!"
    
    @classmethod
    def pass_time(cls):
        for animal in cls.animals:
            animal.energy -= 1

        return True
    
    @classmethod
    def add_animal(cls, animal):
        cls.animals.append(animal)

        """
            Challenge:
                - add_animal
                    - add animal to animals list
                    - add to map
                        - randomly place animal on map
                            - update animal's location
                        - cannot be placed on top of another animal

        """
    
    @staticmethod # functionality related to the class, but does not use any data from the class
    def calculate_distance_between_animals(animal_1, animal_2):
        x_distance = animal_1.location["x"] - animal_2.location["x"]
        y_distance = animal_1.location["y"] - animal_2.location["y"]

        return (x_distance**2 + y_distance**2) ** 0.5


kitty = Animal("Kitty", "Cat", 3)
print(kitty.name)  # dictionary['key'] list[0]
print(kitty.get_description())
print(kitty.walk(5))
print(kitty.eat("fish", 10))
print(kitty.energy)

rover = Animal("Rover", "Dog", 5)

Animal.pass_time()


class Owl(Animal):

    def __init__(self, name, age):
        super().__init__(name, "Owl", age)

    def fly(self, distance):
        self.energy -= distance * 3
        return f"{self.name} flew {distance} kilometers and lost {distance * 3} energy!"
    
    #overriding
    def eat(self, food, energy):
        self.energy += energy
        return f"The Owl, {self.name} ate {food} and gained {energy} energy!"

ollie = Owl("Ollie", 5)
print(ollie.get_description())
print(ollie.eat("leaves", 10))
print(ollie.walk(5))
print(ollie.fly(3))


