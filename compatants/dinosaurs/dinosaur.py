from compatants.compatant import Compatant
import random as r
from compatants.data import *

class Dinosaur(Compatant):
    def __init__(self, additional_initiative=0) -> None:
        self.name = r.choice(dino_names)
        self.health = dino_base_stats['health']
        self.power = dino_base_stats['power']
        self.accuracy = dino_base_stats['accuracy']
        self.evasion = dino_base_stats['evassion']
        self.stats()
        self.evaded = False
        super().__init__(additional_initiative)

    def attack(self, compatant):
        if self.evaded:
            attack = r.choice(['Bite','Tail Slap'])
        else:
            attack = r.choice(['Bite','Tail Slap','Evade'])
        if attack == 'Bite':
            self.bite()
            print(f'{self.name} : {self.species} : is going to bite {compatant.name}')
        elif attack == 'Tail Slap':
            self.tail_slap()
            print(f'{self.name} : {self.species} : is going to tail slap {compatant.name}')
        else:
            self.evade()
            print(f'{self.name} : {self.species} : increased there evasivness by {int(self.evasion*100)}% for the next {self.evade_ends} attacks')
        super().attack(compatant)

    def bite(self):
        self.attack_dmg = self.power

    def tail_slap(self):
        self.attack_dmg = self.power

    def evade(self):
        self.attack_dmg = 0
        self.evaded = True
        self.evade_ends = dino_base_stats['evade turns']
        self.evasion = dino_base_stats['evade move']

    def reset_evasion(self):
        self.evasion = 0

    def hit_me(self, compatant):
        if self.evaded:
            self.evade_ends -= 1
            if self.evade_ends == 0:
                self.evaded = False
                self.reset_evasion()
        return ((compatant.accuracy * (1-self.evasion)) * 100)

    def take_dmg(self, compatant):
        self.health -= compatant.attack_dmg