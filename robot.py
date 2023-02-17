from weapon import Weapon as w
from compatant import Compatant

class Robot(Compatant):
    def __init__(self, name, health) -> None:
        #self.model =  model -- later addition
        self.equiped_weapon = w()
        super().__init__(name, health)

    def attack(self, compatant):
        wep = self.equiped_weapon.select_weapon()
        self.equiped_weapon = w(wep['name'],wep['power'])
        self.attack_power = self.equiped_weapon.attack_power
        print(f'\n{self.name} has select a {wep["name"]} as their weapon',end='')
        super().attack(compatant)