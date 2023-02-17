from weapon import Weapon as w
from compatant import Compatant

class Robot(Compatant):
    def __init__(self, name, health) -> None:
        #self.model =  model -- later addition
        self.equiped_weapon = w('Pea-Shooter', 35)
        super().__init__(name, health, self.equiped_weapon.attack_power)