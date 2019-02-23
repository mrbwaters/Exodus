from random import randint
import os

class Ship(object):
    """This class represents a star ship."""
    def __init__(self, name, captain):
        self.name = name
        self.captain_name = captain
        self.fuel = 5
        self.money = 1000
        self.crew = [captain, 'Argus Fenstrom', 'Nadia Zelossian', 'Sid Corvin', 'Miranda Delos']
        self.weapons = ['Phaser Cannon']
        self.firepower = 1
        self.frequencies = ['Alpha', 'Beta', 'Delta', 'Gamma', 'Omega']
        self.current_location = 'Nibiru'
        self.coord = self.find_coord()


    def find_coord(self):
        if self.current_location == 'Nibiru':
            self.coord = [0, 0]
        elif self.current_location == 'Aurum':
            self.coord = [2, 2]
        elif self.current_location == 'Cephia IV':
            self.coord = [2, 0]
        elif self.current_location == 'Outpost 31':
            self.coord = [3, -5]


    def calculate_firepower(self):
        self.firepower = 1
        if self.weapons.count('Photon Torpedo'):
            self.firepower += 6
        if self.crew.count('Punch Jackson'):
            self.firepower += 3


    def combat_odds(self, oppforce):
        self.calculate_firepower()
        if self.firepower == 0:
            chance_to_win = 0
        else:
            chance_to_win = (1 - (oppforce / self.firepower)) * 100
            if chance_to_win < 0:
                chance_to_win = 0
        print("Your chance of defeating the enemy is %i%%." % chance_to_win)


    def retreat_attempt(self):
        if self.fuel < 3:
            print("Insufficient fuel for escape maneuvers.")
            print("You are unable to escape and must engage the enemy.")
            input("Press Enter to continue...")
            os.system('clear')
            return False
        else:
            if (randint(1,10) > 40):
                print("You escape!")
                input("Press Enter to continue...")
                os.system('clear')
                return True
            else:
                print("You are unable to escape and must engage the enemy.")
                input("Press Enter to continue...")
                os.system('clear')
                return False
