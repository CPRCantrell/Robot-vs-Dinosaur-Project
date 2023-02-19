from .weapon import Weapon as w
from compatants.compatant import Compatant

class Robot(Compatant):
    def __init__(self, name, health) -> None:
        self.equiped_weapon = w()
        super().__init__(name,health, None, None)

    def attack(self, compatant):
        wep = self.equiped_weapon.select_weapon()
        self.equiped_weapon = w(wep['name'],wep['power'])
        self.attack_dmg = self.equiped_weapon.power
        print(f'\n{self.name} has select a {wep["name"]} as their weapon')
        super().attack(compatant)