import random as r
from data import weapons

class Weapon:
    def __init__(self, name=None, attack_power=None) -> None:
        self.name = name
        self.attack_power = attack_power
        # self.accuracy = accuracy -- later addition

    # def to_hit(self): -- later addition
    def select_weapon(self):
        return weapons[r.choice(list(weapons.keys()))]