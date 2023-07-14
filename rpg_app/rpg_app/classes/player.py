
class Player:
    def __init__(self, name, strength = 100 ) -> None:
        
        self.name = name
        self.strength = strength

        self.weapons = []

    def walk(self) -> bool:
        self.strength -= 1
        return self.strength
    
    def add_weapon(self, weapon) -> object:
        self.weapons.append(weapon)
        return weapon
