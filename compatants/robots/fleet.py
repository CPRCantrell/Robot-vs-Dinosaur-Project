import random as r
from compatants.data import robots_models as rm
from compatants.robots.gen2_sparring_bot import Gen2SparingBot as G2
from compatants.robots.b1_268 import B1_268 as B1
from compatants.robots.e54 import E54

class Fleet:
    def __init__(self, team_size) -> None:
        self.fleet = []
        while True:
            user_input = input('\nWould you like to pick your fleet? or shall we choose at random? [pick, random] : ')
            if user_input.lower() == 'pick':
                self.pick(team_size)
                break
            if user_input.lower() == 'random':
                self.random(team_size)
                break
            print(f'Sorry "{user_input}" was not a valid input.')

    def pick(self, team_size):
        self.robo_details()
        while len(self.fleet) != team_size:
            user_input = input('\nWhich robot model would you like to add to the team? [1,2,3] : ')
            self.selection(user_input)
            print(f'Fleet has now has {len(self.fleet)}/{team_size} robots. {f"pick {team_size-len(self.fleet)} more" if len(self.fleet) != team_size else ""}')
        self.display_fleet()

    def random(self, team_size):
        self.robo_details()
        while len(self.fleet) != team_size:
            selection = r.choice(['1','2','3'])
            self.selection(selection)
        self.display_fleet()

    def robo_details(self):
        print('---------- Robot Models ----------')
        print(f"1) 2nd Gen Sparring Bot:\n\t-Can only use fist as a weapon but deals x{rm['2nd Gen Sparring Bot']['mods']['fist']} more damage with them\n\t-Has a base evasivness of {int(rm['2nd Gen Sparring Bot']['mods']['evade']*100)}%")
        print(f"2) B1-268:\n\t-Deals x{rm['B1-268']['mods']['power']} more damage with all weapons\n\t-Has {int((1-rm['B1-268']['mods']['accuracy'])*100)}% reduced accuracy")
        print(f"3) E54:\n\t-When self repairing heals for {int((rm['E54']['mods']['self repair'])*100)}% of max health")

    def selection(self, selection):
        while True:
            if selection == '1':
                self.fleet.append(G2())
                break
            elif selection == '2':
                self.fleet.append(B1())
                break
            elif selection == '3':
                self.fleet.append(E54())
                break
            else:
                input(f'{selection} was an invalid entry. Valid entries [1,2,3] : ')

    def display_fleet(self):
        print('---------- Your Fleet ----------')
        count = 1
        for robot in self.fleet:
            print(f'{count}) {robot.name} the {robot.model}')
            count += 1