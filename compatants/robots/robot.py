from .weapon import Weapon as w
from compatants.compatant import Compatant
from compatants.data import *
import random as r

class Robot(Compatant):
    def __init__(self, additional_initiative = 0) -> None:
        self.name = r.choice(robot_names)
        self.health = robo_base_stats['health']
        self.equiped_weapon = w()
        super().__init__(additional_initiative)

    def attack(self, compatant):
        wep = self.equiped_weapon.select_weapon()
        self.equiped_weapon = w(wep['name'],wep['power'],wep['accuracy'])
        self.attack_dmg = self.equiped_weapon.power
        self.accuracy = self.equiped_weapon.accuracy
        print(f'{self.name} has select a {wep["name"]} as their weapon')
        super().attack(compatant)

    def hit_me(self, compatant):
        return compatant.accuracy * 100

    def take_dmg(self, compatant):
        self.health -= compatant.attack_dmg