from dinosaur import Dinosaur as dr
from robot import Robot as rt

class Battlefield:
    def __init__(self) -> None:
        self.robot = rt('Sam', 200)
        self.dinosaur = dr('Jo', 200, 30)

    def run_game(self):
        self.display_welcome()
        self.battle_phase()
        self.display_winner()

    def display_welcome(self):
        print('\nWelcom to an epic battle for the ages!\nOnly one side can win!')

    def battle_phase(self):
        while self.robot.health != 0 or self.dinosaur.health != 0:
            self.robot.attack(self.dinosaur)
            if self.dinosaur.health == 0:
                break
            self.dinosaur.attack(self.robot)

    def display_winner(self):
        print(f'\n{self.dinosaur.name if self.dinosaur != 0 else self.robot.name} as exicuted {self.dinosaur.name if self.dinosaur == 0 else self.robot.name}!')
        print(f'\n{self.dinosaur.name if self.dinosaur != 0 else self.robot.name} Won!\n')