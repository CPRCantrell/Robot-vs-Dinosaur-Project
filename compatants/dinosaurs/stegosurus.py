from .dinosaur import Dinosaur
from compatants.data import *

class Stegosurus(Dinosaur):
    def __init__(self,) -> None:
        self.species = 'Stegosurus'
        self.modifiers = dino_species[self.species]['mods']
        super().__init__()

    def tail_slap(self):
        self.attack_dmg = self.tail_slap_power


    def stats(self):
        self.tail_slap_power = self.modifiers['tail'] * self.power
        self.plating = self.modifiers['plating']
        self.health += self.modifiers['health']

    def take_dmg(self, compatant):
        dmg = compatant.attack_dmg
        provented_dmg =(dmg*self.plating)
        compatant.attack_dmg = dmg - provented_dmg
        print(f'-{self.name}\'s plating has provented {provented_dmg} damage-')
        super().take_dmg(compatant)