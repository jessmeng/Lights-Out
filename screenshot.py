####################################
# Jessica Meng, jmeng1, Section B
# Lights Out
# 15-112 Term Project 
# screenshot
# this is used to "take a picture" of the user's customized escape room
# uses pyscreenshot, learned from: https://pypi.python.org/pypi/pyscreenshot/0.1.4
####################################

####################################
# imports
# necessary to run program
#################################### 

import tkinter
from tkinter import *
import pyscreenshot as ImageGrab
from pyscreenshot import grab

####################################
# screenshot function
#################################### 

def screenshot():
    roomX1 = 300
    roomY1 = 50
    roomX2 = 1200
    roomY2 = 800
    screen = ImageGrab.grab(bbox = (roomX1, roomY1, roomX2, roomY2))
    screen.show()
    ImageGrab.grab_to_file("EscapeRoom.png")

screenshot()