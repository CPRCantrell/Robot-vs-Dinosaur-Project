from compatant import Compatant

class Dinosaur(Compatant):
    def __init__(self, name, health, attack_power) -> None:
        # self.species =  species -- later addition
        super().__init__(name, health, attack_power)