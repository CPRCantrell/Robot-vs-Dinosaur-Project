import random as r
class Compatant:

    def __init__(self, additional_initiative = 0) -> None:
        self.attack_dmg = 0
        self.initiative = r.randrange(1,11) + additional_initiative

    def attack(self, compatant):
        hit_chance = compatant.hit_me(self)
        if r.randrange(1,101) > hit_chance:
            print(f'{self.name} has missed {compatant.name} and has dealt no damage ({hit_chance}% chance to hit)')
            print(f'{compatant.name} as {compatant.health} left')
        else:
            if self.attack_dmg != 0:
                compatant.take_dmg(self)
                if compatant.health < 0:
                    compatant.health = int(0)
                print(f'{self.name} has dealt {self.attack_dmg} damage to {compatant.name}')
                print(f'{compatant.name} as {compatant.health} left')
            else:
                print(f'{compatant.name} as {compatant.health} left')