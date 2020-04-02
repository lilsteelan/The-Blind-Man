Version = 1.3
#Importations
import time
import turtle as *
import random
import datetime
import sys

"""DEFINITIONS"""
def animate(var):
    for x in var:
        sys.stdout.write(x)
        time.sleep(0.045)
        sys.stdout.flush()

animate("Welcome to the blind man run,\n")
animate("enter the maze at YOUR OWN Risk\n")
animate("btw, c = yes, and x = no\n")
cont = input("Continue?: ")

if cont == c:
	animate("Very well then, as you wish\n")
