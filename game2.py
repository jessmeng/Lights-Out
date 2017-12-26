####################################
# Jessica Meng, jmeng1, Section B
# Lights Out
# 15-112 Term Project 
# game2
# this is the second game in the series of puzzles the user has to solve
# this game is called "Tic Tac Virus", where the player is the "X" and the opponenet (also known as the "virus") is the "V". The "virus" is the computer, who will play the player. The goal of the game is for the player to beat the "virus", so it does not infect their computer.  
# idea for the game from Internet
# all colors used from: https://wiki.tcl.tk/37701 
# root.geometry learned from: https://www.python-course.eu/tkinter_layout_management.php
####################################

####################################
# imports
# necessary to run program
#################################### 

from tkinter import *
import random
import math

####################################
# init
# to initialize needed variables
#################################### 

def init(data):
    # initial mode is "startGame2"
    data.mode = "startGame2"
    
####################################
# mode dispatcher
# learned from 15-112 notes
####################################

# goes to individual mode mousePressed functions
def mousePressed(event, data):
    if (data.mode == "startGame2"): 
        startGame2MousePressed(event, data)
    elif (data.mode == "helpScreen"):   
        helpScreenMousePressed(event, data)

# goes to individual mode keyPressed functions
def keyPressed(event, data):
    if (data.mode == "startGame2"): 
        startGame2KeyPressed(event, data)
    elif (data.mode == "helpScreen"):   
        helpScreenKeyPressed(event, data)

# goes to individual mode timerFired functions
def timerFired(data):
    if (data.mode == "startGame2"): 
        startGame2TimerFired(data)
    elif (data.mode == "helpScreen"):   
        helpScreenTimerFired(data)

# goes to individual mode redrawAll functions
def redrawAll(canvas, data):
    if (data.mode == "startGame2"): 
        startGame2RedrawAll(canvas, data)
    elif (data.mode == "helpScreen"):   
        helpScreenRedrawAll(canvas, data)

####################################
# startGame2 mode
####################################

# draws the starting background 
def drawStartBackground(canvas, data):
    canvas.create_rectangle(5, 5, data.width, data.height, fill = "black", outline = "yellow2", width = 15)
    canvas.create_rectangle(25, 25, data.width - 17, data.height - 17, fill = "black", width = 0)
    canvas.create_text(data.width/2, data.height/3, text = "TIC TAC", fill = "lawn green", font = "Courier 75 bold")
    canvas.create_text(data.width/2, data.height/2, text = "VIRUS", fill = "cyan", font = "Georgia 80 bold")

# draws the buttons going to instructions and "easy" and "hard"
def drawStartButtons(canvas, data):
    canvas.create_oval(data.width/10 - 10, data.height/10 - 10, data.width/10 + 30, data.height/10 + 30, fill = "RoyalBlue4", outline = "white", width = 2)
    canvas.create_rectangle(data.width/4 - 40, data.height*3/4, data.width/4 + 100, data.height*3/4 + 50, fill = "magenta", outline = "white", width = 3)
    canvas.create_rectangle(data.width/3 + 115, data.height*3/4, data.width/3 + 255, data.height*3/4 + 50, fill = "firebrick2", outline = "white", width = 3)
 
# draws the buttons' text for instructions and "easy" and "hard"
def drawStartButtonsText(canvas, data):
    canvas.create_text(data.width/10 + 10, data.height/10 + 10, text = "i", fill = "white", font = "Courier 25 bold")
    canvas.create_text(data.width/4 + 30, data.height*3/4 + 25, text = "EASY", fill = "black", font = "Courier 30 bold")
    canvas.create_text(data.width/3 + 185, data.height*3/4 + 25, text = "HARD", fill = "black", font = "Courier 30 bold")

# game goes to helpScreen mode and gets game2Easy and game2Hard
def startGame2MousePressed(event, data):
    # user's mouse x-coordinate and y-coordinate 
    userX = event.x
    userY = event.y
    # splash screen to helpScreen mode
    helpLeftX = data.width/10 - 10
    helpRightX = data.width/10 + 30
    helpTopY = data.height/10 - 10
    helpBottomY = data.height/10 + 30
    if (userX > helpLeftX and userX < helpRightX and userY > helpTopY and userY < helpBottomY):
        data.mode = "helpScreen"
    # go to game4Easy
    easyLeftX = data.width/4 - 40
    easyRightX = data.width/4 + 100
    easyTopY = data.height*3/4
    easyBottomY = data.height*3/4 + 50
    if (userX > easyLeftX and userX < easyRightX and userY > easyTopY and userY < easyBottomY):
        import game2Easy
    # go to game4Hard
    hardLeftX = data.width/3 + 115
    hardRightX = data.width/3 + 255
    hardTopY = data.height*3/4
    hardBottomY = data.height*3/4 + 50
    if (userX > hardLeftX and userX < hardRightX and userY > hardTopY and userY < hardBottomY):
        import game2Hard
   
def startGame2KeyPressed(event, data):
    pass
   
def startGame2TimerFired(data):
    pass

# draws the starting screen background and buttons 
def startGame2RedrawAll(canvas, data):
    drawStartBackground(canvas, data)
    drawStartButtons(canvas, data)
    drawStartButtonsText(canvas, data)

####################################
# helpScreen mode
####################################

# draws the help screen background
def drawHelpBackground(canvas, data):
    canvas.create_rectangle(5, 5, data.width, data.height, fill = "black", outline = "yellow2", width = 15)
    canvas.create_text(data.width/2, data.height/7 + 10, text = "The goal of this game is", fill = "lawn green", font = "Courier 28 bold")
    canvas.create_text(data.width/2, data.height/7 + 50, text = 'to beat "Virus" (aka', fill = "cyan", font = "Courier 28 bold")
    canvas.create_text(data.width/2, data.height/7 + 90, text = "the computer). This is", fill = "magenta", font = "Courier 28 bold")
    canvas.create_text(data.width/2, data.height/7 + 130, text = "the same as Tic Tac Toe", fill = "yellow", font = "Courier 28 bold")
    canvas.create_text(data.width/2, data.height/7 + 170, text = "(3 in a row).", fill = "red", font = "Courier 28 bold")
    canvas.create_text(data.width/2, data.height/7 + 230, text = "You - \'X\'", fill = "white", font = "Courier 30 bold")
    canvas.create_text(data.width/2, data.height/7 + 260, text = "Virus - \'V\'", fill = "white", font = "Courier 30 bold")
    
# draws the buttons going to "back"
def drawHelpButton(canvas, data):
    canvas.create_rectangle(data.width/3 + 30, data.height*3/4 + 20, data.width/3 + 130, data.height*3/4 + 70, fill = "firebrick2", outline = "white", width = 3)
    
# draws the buttons' text for "back"
def drawHelpButtonText(canvas, data):
    canvas.create_text(data.width/3 + 80, data.height*3/4 + 45, text = "BACK", fill = "black", font = "Courier 25 bold") 
    
# game goes to startGame2 mode 
def helpScreenMousePressed(event, data):
    # user's mouse x-coordinate and y-coordinate 
    userX = event.x
    userY = event.y
    # splash screen to startGame4 mode
    startLeftX = data.width/3 + 30
    startRightX = data.width/3 + 130
    startTopY = data.height*3/4 + 20
    startBottomY = data.height*3/4 + 70
    if (userX > startLeftX and userX < startRightX and userY > startTopY and userY < startBottomY):
        data.mode = "startGame2"
    
def helpScreenKeyPressed(event, data):
    pass

def helpScreenTimerFired(data):
    pass

# draws the help screen background and "back" button
def helpScreenRedrawAll(canvas, data):
    drawHelpBackground(canvas, data)
    drawHelpButton(canvas, data)
    drawHelpButtonText(canvas, data)
    
####################################
# runGame2 function 
# general run function template from 15-112 notes
####################################

def runGame2(width = 300, height = 300):
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
   root.title("Tic Tac Virus")
   root.geometry("+{}+{}".format(805, 0))
   root.resizable(False, False)
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

runGame2(500, 500)