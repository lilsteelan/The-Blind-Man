
Version = 1.3
#Importations
import time
from turtle import *
import random
import datetime
import sys


"""DEFINITIONS"""
def animate(var):
    for x in var:
        sys.stdout.write(x)
        time.sleep(0.045)
        sys.stdout.flush()
"""VARIABLES"""
coins = 100
GameIsRunning = True
while GameIsRunning:
	animate("Welcome to the blind man run,\n")
	animate("enter the maze at YOUR OWN Risk\n")
	animate("btw, c = yes, and x = no\n")
	cont = input("Continue: ")
	print(cont)
	#Check the users response
	if cont == "c" or cont == " c":
		animate("Very well then, as you wish\n")

	#If it did not match what we intended
	else:
		animate("Invalid answer, try again")
		pass
