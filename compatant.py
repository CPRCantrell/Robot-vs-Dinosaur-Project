class Compatant:
    def __init__(self, name, health, attack_power=0) -> None:
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, compatant):
        compatant.health -= self.attack_power
        if compatant.health < 0:
            compatant.health = 0
        print(f'\n{self.name} has attacked {compatant.name} and has dealt {self.attack_power}')
        print(f'{compatant.name} as {compatant.health} remaining!')