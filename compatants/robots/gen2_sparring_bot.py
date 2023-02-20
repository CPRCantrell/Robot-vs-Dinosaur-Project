from .weapons.weapon import Weapon as w
from .robot import Robot
from compatants.data import *
import random as r

class Gen2SparingBot(Robot):
    def __init__(self) -> None:
        self.model = '2nd Gen Sparring bot'
        self.modifiers = robots_models[self.model]['mods']
        self.evasion = self.modifiers['evade']
        super().__init__()

    def select_weapon(self):
        name = 'Fist'
        wep = weapons[name]
        self.equiped_weapon = w(name, wep['power'], wep['accuracy'])
        self.attack_dmg = self.equiped_weapon.power * self.modifiers['fist']
        self.accuracy = self.equiped_weapon.accuracy

    def  hit_me(self, compatant):
        return ((compatant.accuracy * (1-self.evasion)) * 100)