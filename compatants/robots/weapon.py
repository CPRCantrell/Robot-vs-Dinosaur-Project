import random as r
from compatants.data import weapons

class Weapon:
    def __init__(self, name=None, power=None) -> None:
        self.name = name
        self.power = power
        #self.accuracy =

    # def to_hit(self): -- later addition
    def select_weapon(self):
        return weapons[r.choice(list(weapons.keys()))]