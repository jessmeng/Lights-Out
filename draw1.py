####################################
# Jessica Meng, jmeng1, Section B
# Lights Out
# 15-112 Term Project 
# draw1
# this is called "Cyber Draw" and it is a drawing puzzle that is for fun for the user. 
# all colors used from: https://wiki.tcl.tk/37701 
# root.geometry learned from: https://www.python-course.eu/tkinter_layout_management.php
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
    # initial mode is "startDraw1"
    data.mode = "startDraw1"
    data.timeLeft = 15
    data.time = 0
    
####################################
# mode dispatcher
# learned from 15-112 notes
####################################

# goes to individual mode mousePressed functions
def mousePressed(event, data):
    if (data.mode == "startDraw1"): 
        startDraw1MousePressed(event, data)
    elif (data.mode == "helpScreen"):   
        helpScreenMousePressed(event, data)
    elif (data.mode == "playDraw1"):   
        playDraw1MousePressed(event, data)
    elif (data.mode == "winDraw1"):   
        winDraw1MousePressed(event, data)

# goes to individual mode keyPressed functions
def keyPressed(event, data):
    if (data.mode == "startDraw1"): 
        startDraw1KeyPressed(event, data)
    elif (data.mode == "helpScreen"):   
        helpScreenKeyPressed(event, data)
    elif (data.mode == "playDraw1"):
        playDraw1KeyPressed(event, data)
    elif (data.mode == "winDraw1"):   
        winDraw1KeyPressed(event, data)

# goes to individual mode timerFired functions
def timerFired(data):
    if (data.mode == "startDraw1"): 
        startDraw1TimerFired(data)
    elif (data.mode == "helpScreen"):   
        helpScreenTimerFired(data)
    elif (data.mode == "playDraw1"):   
        playDraw1TimerFired(data)
    elif (data.mode == "winDraw1"):   
        winDraw1TimerFired(data)

# goes to individual mode redrawAll functions
def redrawAll(canvas, data):
    if (data.mode == "startDraw1"): 
        startDraw1RedrawAll(canvas, data)
    elif (data.mode == "helpScreen"):   
        helpScreenRedrawAll(canvas, data)
    elif (data.mode == "playDraw1"):   
        playDraw1RedrawAll(canvas, data)
    elif (data.mode == "winDraw1"):   
        winDraw1RedrawAll(canvas, data)

####################################
# startDraw1 mode
####################################

# draws the starting background 
def drawStartBackground(canvas, data):
    canvas.create_rectangle(5, 5, data.width, data.height, fill = "black", outline = "yellow2", width = 15)
    canvas.create_text(data.width/2, data.height/3, text = "CYBER", fill = "lawn green", font = "Courier 60 bold")
    canvas.create_text(data.width/2, data.height/2, text = "DRAW", fill = "cyan", font = "Georgia 65 bold")

# draws the buttons going to "help" and "start"
def drawStartButtons(canvas, data):
    canvas.create_rectangle(data.width/4 - 30, data.height*3/4, data.width/4 + 70, data.height*3/4 + 50, fill = "magenta", outline = "white", width = 3)
    canvas.create_rectangle(data.width/3 + 100, data.height*3/4, data.width/3 + 200, data.height*3/4 + 50, fill = "firebrick2", outline = "white", width = 3)
 
# draws the buttons' text for "help" and "start"
def drawStartButtonsText(canvas, data):
    canvas.create_text(data.width/4 + 20, data.height*3/4 + 25, text = "HELP", fill = "black", font = "Courier 25 bold")
    canvas.create_text(data.width/3 + 150, data.height*3/4 + 25, text = "START", fill = "black", font = "Courier 25 bold")
  
# game goes to helpScreen mode or playDraw1 mode 
def startDraw1MousePressed(event, data):
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
    # splash screen to playDraw1 mode
    startLeftX = data.width/3 + 100
    startRightX = data.width/3 + 200
    startTopY = data.height*3/4
    startBottomY = data.height*3/4 + 50
    if (userX > startLeftX and userX < startRightX and userY > startTopY and userY < startBottomY):
        data.mode = "playDraw1"
        import drawing
        
def startDraw1KeyPressed(event, data):
    pass
    
def startDraw1TimerFired(data):
    pass

# draws the starting screen background and "help" and "start" buttons 
def startDraw1RedrawAll(canvas, data):
    drawStartBackground(canvas, data)
    drawStartButtons(canvas, data)
    drawStartButtonsText(canvas, data)

####################################
# helpScreen mode
####################################

# draws the help screen background
def drawHelpBackground(canvas, data):
    canvas.create_rectangle(5, 5, data.width, data.height, fill = "black", outline = "yellow2", width = 15)
    canvas.create_text(data.width/2, data.height/7 + 60, text = "The goal of this game is", fill = "lawn green", font = "Courier 23 bold")
    canvas.create_text(data.width/2, data.height/7 + 90, text = "to enjoy the beauty of", fill = "cyan", font = "Courier 23 bold")
    canvas.create_text(data.width/2, data.height/7 + 120, text = "the Internet! Just have", fill = "magenta", font = "Courier 23 bold")
    canvas.create_text(data.width/2, data.height/7 + 150, text = "fun and cyber draw!", fill = "yellow", font = "Courier 23 bold")
    
# draws the button going to "start"
def drawHelpButton(canvas, data):
    canvas.create_rectangle(data.width/3 + 20, data.height*3/4, data.width/3 + 120, data.height*3/4 + 50, fill = "firebrick2", outline = "white", width = 3)
    
# draws the button's text for "start"
def drawHelpButtonText(canvas, data):
    canvas.create_text(data.width/3 + 70, data.height*3/4 + 25, text = "START", fill = "black", font = "Courier 25 bold")
    
# game goes to startDraw1 mode
def helpScreenMousePressed(event, data):
    # user's mouse x-coordinate and y-coordinate 
    userX = event.x
    userY = event.y
    # splash screen to startDraw1 mode
    startLeftX = data.width/3 + 20
    startRightX = data.width/3 + 120
    startTopY = data.height*3/4
    startBottomY = data.height*3/4 + 50
    if (userX > startLeftX and userX < startRightX and userY > startTopY and userY < startBottomY):
        data.mode = "startDraw1"
    
def helpScreenKeyPressed(event, data):
    pass

def helpScreenTimerFired(data):
    pass

# draws the help screen background and "start" button
def helpScreenRedrawAll(canvas, data):
    drawHelpBackground(canvas, data)
    drawHelpButton(canvas, data)
    drawHelpButtonText(canvas, data)
    
####################################
# playDraw1 mode
####################################
    
# draws the background (black screen)
def drawPlayBackground(canvas, data):
    canvas.create_rectangle(5, 5, data.width, data.height, fill = "black", width = 0)

# draws the time left in the upper left corner
def drawTimeLeft(canvas, data):
    score = "Time Left: " + str(data.timeLeft)
    canvas.create_text(data.width/2, data.height/2, text = score, fill = "white", font = "Courier 40 bold") 

# draws the button going to "help"
def drawPlayButton(canvas, data):
    canvas.create_rectangle(data.width*6/7 - 35, data.height*7/8, data.width*6/7 + 45, data.height*7/8 + 35, fill = "firebrick2", outline = "yellow", width = 3)
    
# draws the button's text for "help"
def drawPlayButtonText(canvas, data):
    canvas.create_text(data.width*6/7 + 5, data.height*7/8 + 17.5, text = "HELP", fill = "white", font = "Courier 20 bold") 
    
def playDraw1MousePressed(event, data):
    # user's mouse x-coordinate and y-coordinate 
    userX = event.x
    userY = event.y
    # splash screen to helpScreen mode
    helpLeftX = data.width*6/7 - 35 
    helpRightX = data.width*6/7 + 45
    helpTopY = data.height*7/8
    helpBottomY = data.height*7/8 + 35
    if (userX > helpLeftX and userX < helpRightX and userY > helpTopY and userY < helpBottomY):
        data.mode = "helpScreen" 

def playDraw1KeyPressed(event, data):
    pass

def playDraw1TimerFired(data):
    data.timerDelay = 100
    data.time += 1
    # for data.timeLeft (the timer) 
    if (data.time % 10 == 0):
        data.timeLeft -= 1
    # when time left gets to 0, the user gets the next object
    if (data.timeLeft == 0):
        data.mode = "winDraw1"
            
#draws the background, time left, and "help" button 
def playDraw1RedrawAll(canvas, data):
    drawPlayBackground(canvas, data)
    drawTimeLeft(canvas, data) 
    drawPlayButton(canvas, data)
    drawPlayButtonText(canvas, data)
    
####################################
# winDraw1 mode
####################################

# draws the win screen that tells the user the next object
def drawWinBackground(canvas, data):
    canvas.create_rectangle(5, 5, data.width, data.height, fill = "black", outline = "yellow2", width = 15)
    canvas.create_text(data.width/2, data.height/3, text = "Congrats!", fill = "cyan", font = "Courier 55 bold")
    canvas.create_text(data.width/2, data.height/2 - 5, text = "The next object is", fill = "green2", font = "Courier 25 bold")
    canvas.create_text(data.width/2, data.height/2 + 30, text = "the CLOTH in room 3.", fill = "green2", font = "Courier 25 bold")
    canvas.create_text(data.width/2, 2.9*data.height/4, text = "Exit this window and press", fill = "magenta", font = "Courier 20 bold")
    canvas.create_text(data.width/2, 2.9*data.height/4 + 30, text = "\'1\' to return to rooms.", fill = "magenta", font = "Courier 22 bold")

def winDraw1MousePressed(event, data):
    pass
    
def winDraw1KeyPressed(event, data):
    pass
    
def winDraw1TimerFired(data):
    pass

# draws the winning screen background
def winDraw1RedrawAll(canvas, data):
    drawWinBackground(canvas, data)

####################################
# runDraw1 function 
# general run function template from 15-112 notes
####################################

def runDraw1(width = 300, height = 300):
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
    root.title("Cyber Draw")
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
    
runDraw1(400, 400)