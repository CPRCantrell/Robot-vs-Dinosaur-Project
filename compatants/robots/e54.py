from .robot import Robot
from compatants.data import *

class E54(Robot):
    def __init__(self) -> None:
        self.model = 'E54'
        self.modifiers = robots_models[self.model]['mods']
        super().__init__()

    def self_repair(self):
        self.attack_dmg = 0
        self.repaired = self.max_health * self.modifiers['self repair']
        self.health += self.repaired
        if self.health > self.max_health:
            self.health = self.max_health