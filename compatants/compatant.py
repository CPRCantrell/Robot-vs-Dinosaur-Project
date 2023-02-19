import random as r
class Compatant:
    def __init__(self, name, health, accuracy, initiative) -> None:
        self.name = name
        self.health = health
        self.accuracy = accuracy
        self.initiative = initiative
        self.attack_dmg = 0

    def attack(self, compatant):
        compatant.health -= self.attack_dmg
        if compatant.health < 0:
            compatant.health = 0
        print(f'{self.name} has dealt {self.attack_dmg} damage to {compatant.name}')
        print(f'{compatant.name} as {compatant.health} left')