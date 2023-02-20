import random as r
class Compatant:

    def __init__(self, additional_initiative = 0) -> None:
        self.attack_dmg = 0
        self.initiative = r.randrange(1,11) + additional_initiative

    def attack(self, compatant):
        try:
            hit_chance = int(compatant.hit_me(self))
        except: hit_chance = 0
        if self.attack_dmg != 0:
            hit = 0
            while True:
                if r.randrange(1,101) > hit_chance:
                    print(f'{self.name} has missed {compatant.name} and has dealt no damage ({hit_chance}% chance to hit)')
                else:
                    compatant.take_dmg(self)
                    if compatant.health < 0:
                        compatant.health = int(0)
                    print(f'{self.name} has dealt {self.attack_dmg} damage to {compatant.name}')
                    hit += 1
                print(f'{compatant.name} as {compatant.health} left')

                try:
                    if self.multi_attack():
                        continue
                    else:
                        if hit == 3:
                            if self.equiped_weapon.name == "Needle Gun":
                                self.equiped_weapon.blast(self)
                                hit_chance = 100
                                continue
                            else:
                                break
                        else:
                            break
                except:
                    break
        else:
            print(f'{compatant.name} as {compatant.health} left')

    def in_order_group(self, herd, fleet):
        in_order = []
        in_order.extend(herd)
        in_order.extend(fleet)
        for position in range(len(in_order)):
            for sort in range(position,len(in_order)):
                if in_order[position].initiative < in_order[sort].initiative:
                    temp = in_order[position]
                    in_order[position] = in_order[sort]
                    in_order[sort] = temp
                elif in_order[position].initiative == in_order[sort].initiative:
                    in_order[position].initiative += r.choice([-1,1])
                    if in_order[position].initiative < in_order[sort].initiative:
                        temp = in_order[position]
                        in_order[position] = in_order[sort]
                        in_order[sort] = temp
        return in_order