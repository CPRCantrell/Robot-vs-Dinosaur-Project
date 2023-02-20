from compatants.dinosaurs.t_rex import TRex
from compatants.dinosaurs.stegosurus import Stegosurus as Steg
from compatants.dinosaurs.pterodactyl import Pterodactyl as ptero
from compatants.robots.gen2_sparring_bot import Gen2SparingBot as G2
from compatants.robots.e54 import E54

class Battlefield:
    def __init__(self) -> None:
        self.robot = E54()
        self.dinosaur = Steg()
        self.round = 1

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print('\nWelcome to an epic battle for the ages!\nOnly one side can win!')

    def battle_phase(self):
        while self.robot.health != 0 and self.dinosaur.health != 0:
            print(f'---------- Round {self.round} ----------')
            self.robot.attack(self.dinosaur)
            if self.dinosaur.health == 0:
                break
            print()
            self.dinosaur.attack(self.robot)
            self.round += 1

    def display_winner(self):
        print(f'\n{self.dinosaur.name if self.dinosaur.health != 0 else self.robot.name} as executed {self.dinosaur.name if self.dinosaur.health == 0 else self.robot.name}!')
        print(f'{self.dinosaur.name if self.dinosaur.health != 0 else self.robot.name} Won!')