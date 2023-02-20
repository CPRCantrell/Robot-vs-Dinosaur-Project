from .weapons.weapon import Weapon as w
from compatants.compatant import Compatant
from compatants.data import *
import random as r

class Robot(Compatant):
    def __init__(self, additional_initiative = 0) -> None:
        self.name = r.choice(robot_names)
        self.health = robo_base_stats['health']
        self.max_health = self.health
        super().__init__(additional_initiative)

    def attack(self, compatant):
        if self.health == self.max_health:
            attack = 'Use Weapon'
        else:
            attack = r.choice(['Use Weapon','Self Repair'])

        if attack == 'Use Weapon':
            self.select_weapon()
            print(f'{self.name} : {self.model} : is going to use {self.equiped_weapon.name} as their weapon')
        else:
            self.self_repair()
            print(f'{self.name} : {self.model} : is going to repair themselves for {self.repaired} health')
            print(f'{self.name} as {self.health} left')
        super().attack(compatant)

    def select_weapon(self):
        name = w.select_weapon(self)
        wep = weapons[name]
        self.equiped_weapon = w(name, wep['power'], wep['accuracy'], wep['multi'])
        self.weapon_stats()

    def weapon_stats(self):
        self.attack_dmg = self.equiped_weapon.power
        self.accuracy = self.equiped_weapon.accuracy
        self.set_multi_attack(self.equiped_weapon.additional_attacks)

    def set_multi_attack(self, attack_number):
        if attack_number > 0:
            self.m_attack = True
            self.addition_amount = attack_number
        else:
            self.m_attack = False

    def multi_attack(self):
        if self.addition_amount > 0:
            self.addition_amount -= 1
        else:
            self.m_attack = False
        return self.m_attack

    def self_repair(self):
        self.attack_dmg = 0
        self.repaired = self.max_health * robo_base_stats['self repair']
        self.health += self.repaired
        if self.health > self.max_health:
            self.health = self.max_health

    def hit_me(self, compatant):
        return compatant.accuracy * 100

    def take_dmg(self, compatant):
        self.health -= compatant.attack_dmg