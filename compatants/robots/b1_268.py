from .weapons.weapon import Weapon as w
from .robot import Robot
from compatants.data import *
import random as r

class B1_268(Robot):
    def __init__(self) -> None:
        self.model = 'B1-268'
        self.modifiers = robots_models[self.model]['mods']
        self.evasion = self.modifiers['evade']
        super().__init__()

    def select_weapon(self):
        name = w.select_weapon(self)
        wep = weapons[name]
        self.equiped_weapon = w(name, wep['power'], wep['accuracy'])
        self.attack_dmg = self.equiped_weapon.power * self.modifiers['power']
        self.accuracy = self.equiped_weapon.accuracy * self.modifiers['accuracy']