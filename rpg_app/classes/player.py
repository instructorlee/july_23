
class Player:
    def __init__(self, name, strength = 100 ) -> None:
        
        self.name = name
        self.strength = strength

    def walk(self):
        self.strength -= 5
        return self.strength
