from random import randint
import os

class EnemyShip(object):
    """This class represents an opposing star ship."""
    def __init__(self, name, ship):
        self.name = name
        self.ship = ship
        self.frequencies = ['Alpha', 'Beta', 'Delta', 'Gamma', 'Omega']
        self.find_shield()
        self.find_phaser()


    def find_shield(self):
        self.current_shield = self.frequencies[randint(0, len(self.frequencies) - 1)]


    def find_phaser(self):
        self.current_phaser = self.frequencies[randint(0, len(self.frequencies) - 1)]


    def ship_combat(self):
        print("The %s engages in combat." % name)
