from .dinosaur import Dinosaur
from compatants.data import dino

class TRex(Dinosaur):
    def __init__(self, name, health, initiative) -> None:
        self.species = 'T-Rex'
        self.modifiers = dino[self.species]['mods']
        super().__init__(name, health, initiative, self.species)

    def bite(self):
        self.attack_dmg = self.bite_power


    def stats(self):
        self.bite_power = self.modifiers['Bite'] * self.power