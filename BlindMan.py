
Version = 1.6
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
        winsound.PlaySound("silentkeyshort.wav", winsound.SND_ASYNC)
        time.sleep(0.045)
        sys.stdout.flush()
        #9
        #time.sleep(0.023)

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
		#Ask the user what color they want to be
		userColor = input("What color would you like to be: ")
		#Then asign that color
		turtle.color = (str(userColor.lower()))

	#If they do not wish to continue
	if cont == "n" or cont == " n":
		animate("Smart choice, leaving the game")
		#sys.exit() makes the program end
		sys.exit()
	#If it did not match what we intended
	else:
		animate("Invalid answer, try again")
		pass

