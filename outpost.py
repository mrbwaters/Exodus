import ship
import os
from random import randint
from time import sleep

class Outpost(object):
    """This class represents the system of Outpost 31."""
    def __init__(self,):
        self.coord = [3, -5]


    def visit(self, ship):
        self.ship = ship
        self.ship.current_location = 'Outpost 31'
        self.ship.find_coord()
        os.system('clear')
        print("----------OUTPOST 31----------")
        print("Welcome to Outpost 31, the Confederate military's forward base.")
        input("Press Enter to continue...")
        return self.outpost_combat()


    def outpost_combat(self):
        oppforce = 3
        print("You are surrounded by Confederate battlecruisers.")
        self.ship.combat_odds(oppforce)
        print("You must engage or retreat.")
        print("1. Engage \n2. Retreat")
        choice = input("> ")
        while True:
            if choice == '1':
                print("You fire!")
                sleep(2)
                if randint(0, self.ship.firepower) > oppforce:
                    print("The Confederate ships are destroyed.")
                    print("You win!")
                    return False
                else:
                    print("Your weapons do not phase the Confederate ships.")
                    print("The enemy returns fire.")
                    print("The RNS %s is destroyed with no hands surviving." % self.ship.name)
                    print("GAME OVER")
                    return False
            elif choice == '2':
                print("You attempt a daring escape!")
                sleep(2)
                if self.ship.retreat_attempt():
                    return True
                else:
                    choice = '1'
            else:
                print("I do not recognize that command.")
                input("Press Enter to continue...")
                os.system('clear')
