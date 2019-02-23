import ship
import os
from random import randint

class Aurum(object):
    """This class represents the system of Aurum, the CWA governing system
    within the Local Cluster"""
    def __init__(self):
        self.coord = [2, 2]
        self.punch_here = True

    def visit(self, ship):
        self.ship = ship
        self.ship.current_location = 'Aurum'
        self.ship.find_coord()
        os.system('clear')
        while True:
            print("----------AURUM----------")
            print("Welcome to Aurum, the Core World Alliance's administrative center in Region 47A.")
            print("Where would you like to go?")
            print("1. Cantina")
            print("2. Return to RNS %s" % self.ship.name)
            choice = input("> ")
            if choice == '1':
                self.cantina()
            elif choice == '2':
                return True
            else:
                print("I do not recognize that command. Enter menu number.")
                input("Press Enter to continue...")
                os.system('clear')
        return True


    def cantina(self):
        print("This place is full of scum and villainy!")
        while self.punch_here:
            print("A tall, handsome rogue sits alone in the corner.")
            print("Rumor has it that he is Punch Jackson, a skilled weapons expert.")
            print("He would be a welcome addition to the crew.")
            while True:
                print("Attempt to recruit the stranger. How will you approach?")
                print("1. Flatter \n2. Challenge \n3. Leave cantina")
                choice = input("> ")
                if choice == '1':
                    print("You cross the room to the man.")
                    while True:
                        print("What do you say?")
                        print('1. "You are very handsome. Will you join my crew?"')
                        print('2. "You are the greatest gunner in the galaxy!"')
                        choice2 = input("> ")
                        if choice2 == '1':
                            print('"You are very handsome. Will you join my crew?"')
                            print("Punch stands up and moves toward the door.")
                            print('"Hey now. You just keep your distance, buddy."')
                            self.punch_here = False
                            input("Press Enter to continue...")
                            os.system('clear')
                            return True
                        elif choice2 == '2':
                            print('"You are the greatest gunner in the galaxy!"')
                            print("Punch smiles to himself.")
                            print('"No autographs right now. I am just here to drink."')
                            input("Press Enter to continue...")
                            os.system('clear')
                            return True
                        else:
                            print("I do not recognize that command.")
                elif choice == '2':
                    print("You defeat Punch Jackson in a drinking contest!")
                    print("He agrees to join your crew.")
                    print("He will have sobered up by the time you are ready to depart.")
                    self.ship.crew.append('Punch Jackson')
                    self.punch_here = False
                    input("Press Enter to continue...")
                    os.system('clear')
                    return True
                elif choice == '3':
                    print("You leave the cantina.")
                    input("Press Enter to continue...")
                    os.system('clear')
                    return True
                else:
                    print("I do not recognize that command.")
        print("But there is not much else to see.")
        input("Press Enter to continue...")
        os.system('clear')
        return True
