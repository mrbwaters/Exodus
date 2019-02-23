import ship
import os
from random import randint

class Cephia(object):
    """This class represents the system of Cephia."""
    def __init__(self):
        self.coord = [2, 0]

    def visit(self, ship):
        self.ship = ship
        self.ship.current_location = 'Cephia IV'
        self.ship.find_coord()
        os.system('clear')
        while True:
            print("----------CEPHIA IV----------")
            print("Welcome to the Ceph homeworld, Cephia IV.")
            print("Where would you like to go?")
            print("1. Fuel Depot")
            print("2. Return to RNS %s" % self.ship.name)
            choice = input("> ")
            if choice == '1':
                self.fuel_sale()
            elif choice == '2':
                return True
            else:
                print("I do not recognize that command. Enter menu number.")
                input("Press Enter to continue...")
                os.system('clear')
        return True


    def fuel_sale(self):
        print("A robotic attendant approaches you.")
        print('"Welcome to the Automated Fuel Distributor."')
        while True:
            print('"Fuel costs 50 credits per unit. How much would you like to purchase?"')
            print("You have %i credits." % self.ship.money)
            ask = input("Enter a positive integer: ")
            if ask.isdigit():
                if int(ask) == 0:
                    print('"Ah. I understand. Perhaps another time."')
                    input("Press Enter to continue...")
                    os.system('clear')
                    return True
                elif int(ask) * 50 <= self.ship.money:
                    self.ship.money -= int(ask) * 50
                    self.ship.fuel += int(ask)
                    print('"%s units of fuel will be delivered to your ship."' % ask)
                    print('"Thank you for your purchase."')
                    input("Press Enter to continue...")
                    os.system('clear')
                    return True
                elif int(ask) * 50 > self.ship.money:
                    print('"You do not have enough credits for that amount of fuel."')
            else:
                print("Fuel is ordered in positive integer values.")
