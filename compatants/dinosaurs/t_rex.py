from .dinosaur import Dinosaur
from compatants.data import *

class TRex(Dinosaur):
    def __init__(self) -> None:
        self.species = 'T-Rex'
        self.modifiers = dino_species[self.species]['mods']
        self.additional_initiative = self.modifiers['initiative']
        super().__init__(self.additional_initiative)

    def bite(self):
        self.attack_dmg = self.bite_power


    def stats(self):
        self.bite_power = self.modifiers['bite'] * self.power