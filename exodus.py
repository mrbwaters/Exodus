import interface
import ship
import os
import enemy_ship
from time import sleep

os.system('clear')
captain_name = input("What is your name? ")
name = input("What is the name of your ship? ")
ship1 = ship.Ship(name, captain_name)
a_game = interface.Interface(ship1)
sleep(2)
