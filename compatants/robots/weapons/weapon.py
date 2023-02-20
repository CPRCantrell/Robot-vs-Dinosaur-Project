import random as r
from compatants.data import weapons

class Weapon:
    def __init__(self, name=None, power=None, accuracy=None, multi=None) -> None:
        self.name = name
        self.power = power
        self.accuracy = accuracy
        self.addition_attacks = multi

    def select_weapon(self):
        return r.choice(list(weapons.keys()))

    def blast(self, robot):
        robot.attack_dmg = 100