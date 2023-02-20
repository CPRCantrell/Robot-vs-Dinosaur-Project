from .robot import Robot
from compatants.data import *

class E54(Robot):
    def __init__(self) -> None:
        self.model = 'E54'
        self.modifiers = robots_models[self.model]['mods']
        self.cooldown == 0
        super().__init__()

    def self_repair(self):
        self.attack_dmg = 0
        self.repaired = self.max_health * self.modifiers['self repair']
        self.health += self.repaired
        if self.health > self.max_health:
            self.health = self.max_health

    def set_multi_attack(self, wep_amount):
        if self.cooldown == 0:
            self.cooldown = self.modifiers['sentry mode cd']
            self.sentry_mode()
        else:
            self.cooldown -= 1
        super().set_multi_attack(wep_amount)

    def sentry_mode(self):
        self.accuracy *= (1-self.modifiers['sentry mode accuracy penalty'])
        super().set_multi_attack(self.modifiers['sentry mode multi']-1)