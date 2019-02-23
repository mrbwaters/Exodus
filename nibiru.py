import ship
import os
from random import randint

class Nibiru(object):
    """This class represents the system of Nibiru."""
    def __init__(self):
        self.coord = [0, 0]

    def visit(self, ship):
        self.ship = ship
        self.ship.current_location = 'Nibiru'
        self.ship.find_coord()
        os.system('clear')
        while True:
            print("----------NIBIRU----------")
            print("Welcome to the colonial capital of Nibiru.")
            print("Where would you like to go?")
            print("1. Merchant District")
            print("2. Return to RNS %s" % self.ship.name)
            choice = input("> ")
            if choice == '1':
                self.torpedo_sale()
            elif choice == '2':
                return True
            else:
                print("I do not recognize that command. Enter menu number.")
                input("Press Enter to continue...")
                os.system('clear')
        return True


    def torpedo_sale(self):
        if not self.ship.weapons.count('Photon Torpedo'):
            while True:
                print("As you enter the merchant district, an Ornathian approaches you.")
                print('"That is a fine vessel, but it is awfully undefended."')
                print('"Of course I can help. Would you like to purchase a photon torpedo for the low price of 500 credits?"')
                print("You have: %i credits." % self.ship.money)
                print("1. Yes \n2. No")
                choice = input("> ")

                if choice == '1' and self.ship.money >= 500:
                    print('"Excellent choice!"')
                    print('"I will get that installed aboard your vessel immediately!"')
                    self.ship.money -= 500
                    self.ship.weapons.append('Photon Torpedo')
                    input("Press Enter to continue...")
                    os.system('clear')
                    return True
                elif choice == '1' and self.ship.money < 500:
                    print('"Looks like you don\'t have the money right now."')
                    print('"Come back if your fortunes improve."')
                    input("Press Enter to continue...")
                    os.system('clear')
                    return True
                elif choice == '2':
                    print("The merchant seems annoyed at your dismissal.")
                    print('"Suit yourself. Good luck when the Confederates track you down."')
                    input("Press Enter to continue...")
                    os.system('clear')
                    return True
                else:
                    print("I do not recognize that command.")
        else:
            print("There are many shops but none selling anything of interest.")
            input("Press Enter to continue...")
            os.system('clear')
            return True
