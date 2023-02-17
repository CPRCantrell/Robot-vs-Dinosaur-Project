from compatant import Compatant

class Dinosaur(Compatant):
    def __init__(self, name, species, health, attack_power) -> None:
        self.species =  species
        self.attack_power = attack_power