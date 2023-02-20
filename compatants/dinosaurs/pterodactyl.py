from .dinosaur import Dinosaur
from compatants.data import *

class Pterodactyl(Dinosaur):
    def __init__(self) -> None:
        self.species = 'Pterodactyl'
        self.modifiers = dino_species[self.species]['mods']
        super().__init__()

    def evade(self):
        self.evaded = True
        self.attack_dmg = 0
        self.evade_ends = (dino_base_stats['evade turns'] + self.modifiers['evade turns'])
        self.evasion = self.modifiers['evade move']


    def stats(self):
        self.health += self.modifiers['health']
        self.evasion = self.modifiers['base evasion']

    def reset_evasion(self):
        self.evasion = self.modifiers['base evasion']