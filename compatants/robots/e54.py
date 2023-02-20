from .robot import Robot
from compatants.data import *

class E54(Robot):
    def __init__(self) -> None:
        self.model = 'E54'
        self.modifiers = robots_models[self.model]['mods']
        self.cooldown = 0
        super().__init__()

    def self_repair(self):
        self.attack_dmg = 0
        self.repaired = self.max_health * self.modifiers['self repair']
        self.health += self.repaired
        if self.health > self.max_health:
            self.health = self.max_health

    def set_multi_attack(self, wep_amount):
        if self.cooldown == 0:
            print(f'{self.name} has activated Sentry Mode')
            self.cooldown = self.modifiers['sentry mode cd']
            self.accuracy *= (1-self.modifiers['sentry mode accuracy penalty'])
            self.equiped_weapon.addition_attacks = self.modifiers['sentry mode multi']
            super().set_multi_attack(self.equiped_weapon.addition_attacks-1)
        else:
            self.cooldown -= 1
            super().set_multi_attack(wep_amount)