import random as r
from compatants.data import dino_species as ds
from compatants.dinosaurs.t_rex import TRex
from compatants.dinosaurs.stegosurus import Stegosurus as Steg
from compatants.dinosaurs.pterodactyl import Pterodactyl as Ptero

class Herd:
    def __init__(self, team_size) -> None:
        self.herd = []
        while True:
            user_input = input('Would you like to pick your herd? or shall we choose at random? [pick, random] : ')
            if user_input.lower() == 'pick':
                self.pick(team_size)
                break
            if user_input.lower() == 'random':
                self.random(team_size)
                break
            print(f'Sorry "{user_input}" was not a valid input.')

    def pick(self, team_size):
        self.dino_details()
        while len(self.herd) != team_size:
            user_input = input('\nWhich dino species would you like to add to the team? [1,2,3] : ')
            self.selection(user_input)
            print(f'Herd has now has {len(self.herd)}/{team_size} dinosaurs. {f"pick {team_size-len(self.herd)} more" if len(self.herd) != team_size else ""}')
        self.display_herd()

    def random(self, team_size):
        self.dino_details()
        while len(self.herd) != team_size:
            selection = r.choice['1','2','3']
            self.selection(selection)
        self.display_herd()

    def dino_details(self):
        print('---------- Dinosaur Species ----------')
        print(f"1) T-Rex:\n\t-Bite attack does x{ds['T-Rex']['mods']['bite']} more damage\n\t-Has a +{ds['T-Rex']['mods']['initative']} to initiative")
        print(f"2) Stegosurus:\n\t-Tail slap attack does x{ds['Stegosurus']['mods']['tail']} more damage\n\t-Has {ds['Stegosurus']['mods']['health']} addition health\n\t-Has armor plating that reduces damage by {int((ds['Stegosurus']['mods']['plating'])*100)}%")
        print(f"3) Pterodactyl:\n\t-Base evasiveness is {int((ds['Pterodactyl']['mods']['base evasion'])*100)}%\n\t-The Evade move increases to {int((ds['Pterodactyl']['mods']['evasion move'])*100)}% for an extra {'turn' if ds['Pterodactyl']['mods']['evasion turns'] == 1 else str(ds['Pterodactyl']['mods']['evasion turns'],' turns')}\n\t-Has {ds['Pterodactyl']['mods']['health'][1:]} reduced health")

    def selection(self, selection):
        while True:
            if selection == '1':
                self.herd.append(TRex())
                break
            elif selection == '2':
                self.herd.append(Steg())
                break
            elif selection == '3':
                self.herd.append(Ptero())
                break
            else:
                input(f'{selection} was an invalid entry. Valid entries [1,2,3] : ')

    def display_herd(self):
        print('---------- Your Herd ----------')
        for dino in self.herd:
            count = 1
            print(f'{count}) {dino.name} the {dino.species}')
            count += 1