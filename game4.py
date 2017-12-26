####################################
# Jessica Meng, jmeng1, Section B
# Lights Out
# 15-112 Term Project 
# game4
# this is the fourth and final game in the series of puzzles the user has to solve
# this game is called "CyberBot", where the user must play the computer, who will be "CyberBot" (uses AI). The goal of the game is to have more blue squares than green squares. The squares change color based on where they are placed and also change the squares surrounding the clicked square to that color. 
# all colors used from: https://wiki.tcl.tk/37701
####################################

####################################
# imports
# necessary to run program
#################################### 

from tkinter import *
import tkinter
import tkinter
import random
import math

####################################
# init
# to initialize needed variables
#################################### 

def init(data):
   data.mode = "startGame4"
   data.timeLeft = 15
   data.time = 0
    
####################################
# mode dispatcher
# learned from 15-112 notes
####################################

# goes to individual mode mousePressed functions
def mousePressed(event, data):
   if (data.mode == "startGame4"): 
      startGame4MousePressed(event, data)
   elif (data.mode == "helpScreen"):   
      helpScreenMousePressed(event, data)

# goes to individual mode keyPressed functions
def keyPressed(event, data):
   if (data.mode == "startGame4"): 
      startGame4KeyPressed(event, data)
   elif (data.mode == "helpScreen"):   
      helpScreenKeyPressed(event, data)

# goes to individual mode timerFired functions
def timerFired(data):
   if (data.mode == "startGame4"): 
      startGame4TimerFired(data)
   elif (data.mode == "helpScreen"):   
      helpScreenTimerFired(data)

# goes to individual mode redrawAll functions
def redrawAll(canvas, data):
   if (data.mode == "startGame4"): 
      startGame4RedrawAll(canvas, data)
   elif (data.mode == "helpScreen"):   
      helpScreenRedrawAll(canvas, data)

####################################
# startGame4 mode
####################################

# draws the starting background 
def drawStartBackground(canvas, data):
   canvas.create_rectangle(5, 5, data.width, data.height, fill = "black", outline = "yellow2", width = 15)
   canvas.create_text(data.width/2, data.height/3 - 10, text = "CYBER", fill = "lawn green", font = "Courier 70 bold")
   canvas.create_text(data.width/2, data.height/2 - 10, text = "BOT", fill = "cyan", font = "Georgia 75 bold")

# draws the buttons going to "help" and "start"
def drawStartButtons(canvas, data):
   canvas.create_rectangle(data.width/4 - 30, data.height*3/4, data.width/4 + 70, data.height*3/4 + 50, fill = "magenta", outline = "white", width = 3)
   canvas.create_rectangle(data.width/3 + 100, data.height*3/4, data.width/3 + 200, data.height*3/4 + 50, fill = "firebrick2", outline = "white", width = 3)

# draws the buttons' text for "help" and "start"
def drawStartButtonsText(canvas, data):
   canvas.create_text(data.width/4 + 20, data.height*3/4 + 25, text = "HELP", fill = "black", font = "Courier 25 bold")
   canvas.create_text(data.width/3 + 150, data.height*3/4 + 25, text = "START", fill = "black", font = "Courier 25 bold")

# game goes to helpScreen mode or to game4Game
def startGame4MousePressed(event, data):
   # user's mouse x-coordinate and y-coordinate 
   userX = event.x
   userY = event.y
   # splash screen to helpScreen mode
   helpLeftX = data.width/4 - 30
   helpRightX = data.width/4 + 70
   helpTopY = data.height*3/4
   helpBottomY = data.height*3/4 + 50
   if (userX > helpLeftX and userX < helpRightX and userY > helpTopY and userY < helpBottomY):
      data.mode = "helpScreen"
   # go to game4Game
   startLeftX = data.width/3 + 100
   startRightX = data.width/3 + 200
   startTopY = data.height*3/4
   startBottomY = data.height*3/4 + 50
   if (userX > startLeftX and userX < startRightX and userY > startTopY and userY < startBottomY):
      import game4Game
      
def startGame4KeyPressed(event, data):
   pass
   
def startGame4TimerFired(data):
   pass

# draws the starting screen background and "help" and "start" buttons 
def startGame4RedrawAll(canvas, data):
   drawStartBackground(canvas, data)
   drawStartButtons(canvas, data)
   drawStartButtonsText(canvas, data)

####################################
# helpScreen mode
####################################

# draws the help screen background
def drawHelpBackground(canvas, data):
   canvas.create_rectangle(5, 5, data.width, data.height, fill = "black", outline = "yellow2", width = 15)
   canvas.create_text(data.width/2, data.height/7, text = "The goal of this game is", fill = "lawn green", font = "Courier 20 bold")
   canvas.create_text(data.width/2, data.height/7 + 20, text = 'to beat "CyberBot" (aka', fill = "cyan", font = "Courier 20 bold")
   canvas.create_text(data.width/2, data.height/7 + 40, text = "the computer). You want", fill = "magenta", font = "Courier 20 bold")
   canvas.create_text(data.width/2, data.height/7 + 60, text = "to have more blue cells", fill = "yellow", font = "Courier 20 bold")
   canvas.create_text(data.width/2, data.height/7 + 80, text = "than green cells. Every", fill = "red", font = "Courier 20 bold")
   canvas.create_text(data.width/2, data.height/7 + 100, text = "time a cell is clicked,", fill = "orange", font = "Courier 20 bold")
   canvas.create_text(data.width/2, data.height/7 + 120, text = "the surrounding cells change", fill = "SeaGreen1", font = "Courier 20 bold")
   canvas.create_text(data.width/2, data.height/7 + 140, text = "to the current color.", fill = "Hot Pink", font = "Courier 20 bold")
   canvas.create_rectangle(80, 220, 100, 240, fill = "blue", outline = "snow2", width = 2)
   canvas.create_text(200, 230, text = "You - BLUE", fill = "white", font = "Courier 25 bold")
   canvas.create_rectangle(80, 260, 100, 280, fill = "green", outline = "snow2", width = 2)
   canvas.create_text(220, 270, text = "CyberBot - GREEN", fill = "white", font = "Courier 22 bold")
   
# draws the buttons going to "back" and "play" 
def drawHelpButtons(canvas, data):
   canvas.create_rectangle(data.width/4 - 30, data.height*3/4 + 20, data.width/4 + 70, data.height*3/4 + 70, fill = "magenta", outline = "white", width = 3)
   canvas.create_rectangle(data.width/3 + 100, data.height*3/4 + 20, data.width/3 + 200, data.height*3/4 + 70, fill = "firebrick2", outline = "white", width = 3)
    
# draws the buttons' text for "back" and "play"
def drawHelpButtonsText(canvas, data):
   canvas.create_text(data.width/4 + 20, data.height*3/4 + 45, text = "BACK", fill = "black", font = "Courier 25 bold")
   canvas.create_text(data.width/3 + 150, data.height*3/4 + 45, text = "PLAY", fill = "black", font = "Courier 25 bold") 
   
# game goes to startGame4 mode or to game4Game     
def helpScreenMousePressed(event, data):
   # user's mouse x-coordinate and y-coordinate 
   userX = event.x
   userY = event.y
   # splash screen to startGame4 mode
   startLeftX = data.width/4 - 30
   startRightX = data.width/4 + 70
   startTopY = data.height*3/4 + 20
   startBottomY = data.height*3/4 + 70
   if (userX > startLeftX and userX < startRightX and userY > startTopY and userY < startBottomY):
      data.mode = "startGame4"
   # go to game4Game
   resumeLeftX = data.width/3 + 100
   resumeRightX = data.width/3 + 200
   resumeTopY = data.height*3/4 + 20
   resumeBottomY = data.height*3/4 + 70
   if (userX > resumeLeftX and userX < resumeRightX and userY > resumeTopY and userY < resumeBottomY):
      import game4Game

def helpScreenKeyPressed(event, data):
   pass

def helpScreenTimerFired(data):
   pass

# draws the help screen background and "back" and "play" buttons 
def helpScreenRedrawAll(canvas, data):
   drawHelpBackground(canvas, data)
   drawHelpButtons(canvas, data)
   drawHelpButtonsText(canvas, data)

####################################
# runGame4 function 
# general run function template from 15-112 notes
####################################

def runGame4(width = 300, height = 300):
   def redrawAllWrapper(canvas, data):
      canvas.delete(ALL)
      canvas.create_rectangle(0, 0, data.width, data.height, fill = 'white', width = 0)
      redrawAll(canvas, data)
      canvas.update()    

   def mousePressedWrapper(event, canvas, data):
      mousePressed(event, data)
      redrawAllWrapper(canvas, data)

   def keyPressedWrapper(event, canvas, data):
      keyPressed(event, data)
      redrawAllWrapper(canvas, data)

   def timerFiredWrapper(canvas, data):
      timerFired(data)
      redrawAllWrapper(canvas, data)
      # pause, then call timerFired again
      canvas.after(data.timerDelay, timerFiredWrapper, canvas, data)
      
   # set up data and call init
   class Struct(object): pass
   data = Struct()
   data.width = width
   data.height = height
   data.timerDelay = 100 # milliseconds
   init(data)
   # create the root and the canvas
   root = Tk()
   root.resizable(False, False)
   root.title("CyberBot")
   root.geometry("+{}+{}".format(805, 0))
   canvas = Canvas(root, width = data.width, height = data.height)
   data.canvas = canvas
   canvas.pack()
   # set up events
   root.bind("<Button-1>", lambda event:
                           mousePressedWrapper(event, canvas, data))
   root.bind("<KeyPress>", lambda event:
                           keyPressedWrapper(event, canvas, data))
   timerFiredWrapper(canvas, data)
   # launch the app
   root.mainloop()
   
runGame4(400, 400)