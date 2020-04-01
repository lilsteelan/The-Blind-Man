Version = 1.2
#Importations
import time
import turtle
import random
import datetime
import sys

"""DEFINITIONS"""
def animate(var):
    for x in var:
        sys.stdout.write(x)
        time.sleep(0.045)
        sys.stdout.flush()

animate("is this fluent? Test hello world")
