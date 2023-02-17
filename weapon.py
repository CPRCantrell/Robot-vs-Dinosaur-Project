class Weapon:
    def __init__(self, name, attack_power, accuracy) -> None:
        self.name = name
        self.attack_power = attack_power
        self.accuracy = accuracy

    def to_hit(self):
        pass