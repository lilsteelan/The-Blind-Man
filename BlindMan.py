
Version = 1.75
#Importations
import time
from turtle import *
import random
import datetime
import sys
import winsound
import os


"""DEFINITIONS"""
def wall():
	pd()
	fd(75)
	pu()
	fd(50)
	pd()
	fd(75)
	rt(90)

def room():
	
	pu()
	fd(100)
	lt(90)
	fd(100)
	rt(180)
	wall()
	wall()
	wall()
	wall()

def animate(var):
    for x in var:
        sys.stdout.write(x)
        time.sleep(0.045)
        sys.stdout.flush()
        #9
        #time.sleep(0.023)

"""VARIABLES"""
coins = 100
GameIsRunning = True

window = Screen()
while GameIsRunning:



	animate("Welcome to the blind man run,\n")
	animate("enter the maze at YOUR OWN Risk\n")
	animate("btw, c = yes, and x = no\n")
	cont = input("Continue: ")
	print(cont)
	#Check the users response
	if cont == "c" or cont == " c" or cont.lower() == "yes" or cont.lower == "y":
		animate("Very well then, as you wish\n")
		#Ask the user what color they want to be
		userColor = input("What color would you like to be: ")
		#Then asign that color

		#Try to set that color
		try:
			turtle.color = (str(userColor.lower()))

		#If it fails we inform the user that it failed
		except:
			animate("that color was invalid! \n")
		
	#If they do not wish to continue
	if cont == "n" or cont == " n":
		animate("Smart choice, leaving the game\n")
		#sys.exit() makes the program end
		sys.exit()
	#If it did not match what we intended
	else:
		animate("Please try again!\n")
		pass

