from compatants.compatant import Compatant as com
from compatants.dinosaurs.herd import Herd
from compatants.robots.fleet import Fleet
from compatants.robots.robot import Robot
from compatants.dinosaurs.dinosaur import Dinosaur as Dino
import random as r

class Battlefield:
    def __init__(self) -> None:
        even_teams = input('\nWould you like to make even teams? [y,n] : ')
        if even_teams.lower() == 'y':
            team_size = input('Would you like set the team size? or at random between 3 to 5? [#, random] : ')
            if team_size.lower() == 'random':
                team_size = r.randrange(3,6)
                self.herd = Herd(team_size)
                self.fleet = Fleet(team_size)
            else:
                self.herd = Herd(int(team_size))
                self.fleet = Fleet(int(team_size))
        elif even_teams.lower() == 'n':
            team_size = input('Would you like set the team size? or at random between 3 to 5? [set, random] : ')
            if team_size.lower() == 'random':
                self.herd = Herd(r.randrange(3,6))
                self.fleet = Fleet(r.randrange(3,6))
            else:
                self.herd = Herd(int(input('Dino Team: ')))
                self.fleet = Fleet(int(input('Robot Team: ')))
        self.battle_order = com.in_order_group(self, self.herd.herd, self.fleet.fleet)
        self.round = 1

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print('\nWelcome to an epic battle for the ages!\nOnly one side can win!')

    def battle_phase(self):
        while len(self.herd.herd) != 0 and len(self.fleet.fleet) != 0:
            print(f'---------- Round {self.round} ----------')
            for compatant in self.battle_order:
                if isinstance(compatant, Robot):
                    opponent = r.choice(self.herd.herd)
                    compatant.attack(opponent)
                    if opponent.health <= 0:
                        self.herd.herd.remove(opponent)
                        self.battle_order.remove(opponent)
                        if len(self.herd.herd) == 0:
                            break
                elif isinstance(compatant, Dino):
                    opponent = r.choice(self.fleet.fleet)
                    compatant.attack(opponent)
                    if opponent.health <= 0:
                        self.fleet.fleet.remove(opponent)
                        self.battle_order.remove(opponent)
                        if len(self.fleet.fleet) == 0:
                            break
                print()
            self.round += 1

    def display_winner(self):
        print(f'\n{"The Herd" if len(self.herd.herd) != 0 else "The Fleet"} as executed {"the Herd" if len(self.herd.herd) != 0 else "the Fleet"}!')
        for survivor in self.herd.herd if len(self.herd.herd) != 0 else self.fleet.fleet:
            print(f'{survivor.name} the {survivor.species if isinstance(survivor, Dino) else survivor.model} with {survivor.health} health left')
        print(f'These survivors are your winners Won!')