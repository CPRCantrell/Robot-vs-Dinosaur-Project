from weapon import Weapon as w
from compatant import Compatant

class Robot(Compatant):
    def __init__(self, name, model, health, weapon) -> None:
        self.model =  model
        self.equiped_weapon = weapon