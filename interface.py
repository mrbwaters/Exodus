import nibiru
import cephia
import outpost
import aurum
import ship
import os
from math import sqrt

class Interface(object):
    """This class represents the Interface."""
    def __init__(self,ship):
        self.nib = nibiru.Nibiru()
        self.ceph = cephia.Cephia()
        self.aur = aurum.Aurum()
        self.out = outpost.Outpost()
        self.ship = ship
        print("Welcome aboard the RNS %s, Captain %s." % (self.ship.name, self.ship.captain_name))
        print("Your ship represents the primary defense effort of the Republic of Nibiru.")
        print("Your mission is to stop the Confederate incursion in the Local Cluster.")
        print("You must navigate the local cluster, acquire resources,")
        print("and destroy the Confederate threat before it comes to Nibiru.")
        input("Press Enter to continue...")
        os.system('clear')
        self.bridge()


    def bridge(self):
        repeat = True
        while repeat:
            os.system('clear')
            print("----------COMMAND BRIDGE----------")
            print("You are currently orbiting:", self.ship.current_location)
            print("You have %i fuel." % (self.ship.fuel))
            print("You have %i credits." % self.ship.money)
            print("Choose a command console:")
            print("1. Galaxy Map \n2. Crew Manifest \n3. Weapons Manifest")
            choice = input("> ")

            if choice == '1':
                repeat = self.galaxy_map()
            elif choice == '2':
                repeat = self.crew_manifest()
            elif choice == '3':
                repeat = self.weap_manifest()
            elif choice == 'exit':
                repeat = False
            else:
                print("I do not recognize that command. Enter menu number.")
                input("Press Enter to continue...")
                os.system('clear')


    def galaxy_map(self):
        while True:
            os.system('clear')
            print("----------GALAXY MAP----------")
            print("You are currently orbiting:", self.ship.current_location)
            print("You have %i fuel." % (self.ship.fuel))
            print("Where would you like to go?")
            print("1. Nibiru \n2. Cephia IV \n3. Aurum \n4. Outpost 31")
            print("5. Return to command bridge.")
            choice = input("> ")
            if choice == '1':
                if self.within_range(self.nib):
                    if not self.nib.visit(self.ship):
                        return False
            elif choice == '2':
                if self.within_range(self.ceph):
                    if not self.ceph.visit(self.ship):
                        return False
            elif choice == '3':
                if self.within_range(self.aur):
                    if not self.aur.visit(self.ship):
                        return False
            elif choice == '4':
                if self.within_range(self.out):
                    if not self.out.visit(self.ship):
                        return False
            elif choice == '5':
                return True
            else:
                print("I do not recognize that command. Enter menu number.")
                input("Press Enter to continue...")
                os.system('clear')
        return False


    def crew_manifest(self):
        os.system('clear')
        print("----------CREW MANIFEST----------")
        print("The following is a list of crew members aboard the RNS %s:" % self.ship.name)
        for i in self.ship.crew:
            print(i)
        input("Press Enter to continue...")
        os.system('clear')
        return True


    def weap_manifest(self):
        os.system('clear')
        print("----------WEAPONS MANIFEST----------")
        print("The following is a list of weapon systems installed on the RNS %s:" % self.ship.name)
        for i in self.ship.weapons:
            print(i)
        self.ship.calculate_firepower()
        print("The total power level of your weapons systems is: %s" % self.ship.firepower)
        input("Press Enter to continue...")
        os.system('clear')
        return True


    def within_range(self, destination):
        self.ship.find_coord()
        a = self.ship.coord[0] - destination.coord[0]
        b = self.ship.coord[1] - destination.coord[1]
        dist = sqrt(a ** 2 + b ** 2)
        if dist <= self.ship.fuel:
            self.ship.fuel = int(self.ship.fuel - dist)
            return True
        else:
            print("Your destination is %i light years away. You have only %i units of fuel." % (dist + 1, self.ship.fuel))
            print("Acquire more fuel to travel to this destination.")
            input("Press Enter to continue...")
            os.system('clear')
            return False
