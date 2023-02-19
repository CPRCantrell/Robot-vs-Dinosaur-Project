from compatants.compatant import Compatant
import random as r

class Dinosaur(Compatant):
    def __init__(self, name, health, initiative, species) -> None:
        self.species = species
        self.power = 50
        self.natural_accuracy = .9
        self.evassion = 1
        self.stats()
        super().__init__(name, health, self.natural_accuracy, initiative)

    def attack(self, compatant):
        attack = r.choice(['Bite','Tail Slap','Evade'])
        print()
        if attack == 'Bite':
            self.bite()
            print(f'{self.name} : {self.species} : is going to bite {compatant.name}')
        elif attack == 'Tail Slap':
            self.tail_slap()
            print(f'{self.name} : {self.species} : is going to tail slap {compatant.name}')
        else:
            self.evade()
            print(f'{self.name} : {self.species} : increased there evasivness by {int(self.evassion*100)}%')
        super().attack(compatant)

    def bite(self):
        self.attack_dmg = self.power

    def tail_slap(self):
        self.attack_dmg = self.power

    def evade(self):
        self.evassion = .3

    def hit(self):
        return self.evassion