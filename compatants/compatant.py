import random as r
class Compatant:

    def __init__(self, additional_initiative = 0) -> None:
        self.attack_dmg = 0
        self.initiative = r.randrange(1,11) + additional_initiative

    def attack(self, compatant):
        hit_chance = int(compatant.hit_me(self))
        if self.attack_dmg != 0:
            if r.randrange(1,101) > hit_chance:
                print(f'{self.name} has missed {compatant.name} and has dealt no damage ({hit_chance}% chance to hit)')
            else:
                compatant.take_dmg(self)
                if compatant.health < 0:
                    compatant.health = int(0)
                print(f'{self.name} has dealt {self.attack_dmg} damage to {compatant.name}')
        print(f'{compatant.name} as {compatant.health} left')

    def in_order_group(self, herd, fleet):
        in_order = []
        in_order.extend(herd)
        in_order.extend(fleet)
        for compatants in in_order:
            for position in range(len(in_order)-1):
                compare_position = position+1
                compare = in_order[compare_position]
                if compatants.initiative < compare.initiative:
                    temp = in_order[position]
                    in_order[position] = in_order[compare_position]
                    in_order[compare_position] = temp
        return in_order