####################################
# Jessica Meng, jmeng1, Section B
# Lights Out
# 15-112 Term Project 
# game1
# this is the first game in the series of puzzles the user has to solve
# the game is called "CyberMove", where randomly drawn and sized dots will appear and move and the user has to click within the dots to reach a certain score. When the user clicks a dot, a random fact about cybersecurity will pop up. 
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
# Facts class
# this contains all the facts that will be displayed
# facts from: https://www.usatoday.com/story/tech/columnist/komando/2013/07/19/hacker-attack-trojan-horse-drive-by-downloads-passwords/2518053/, https://www.floridatechonline.com/blog/information-technology/interesting-facts-on-cybersecurity/ 
####################################

class Facts(object):
    facts = ['''One popular hacker strategy is\nphishing scams, where hackers try to\nget you to send in personal or\nbanking information.''', '''Many hackers want to slip a virus\non your computer. Once installed,\na virus can record everything\nyou type and can send out spam\ne-mail or attack other computers.''', '''Programs on your computer might\nhave weaknesses that hackers can\nuse to bypass security software. To\nstay safe, you have to keep your\nprograms up-to-date.''', '''It is important that you use a\ndifferent password for every account.\nIf a hacker discovers one,\nat least they can't get into every\none of your accounts.''', '''Be careful in using open Wi-Fi as\nhackers can connect to your\nnetwork from outside. Take a few\nminutes and secure your network.''', '''The prevalence of cyber crime has\nskyrocketed over the past several\nyears to include cyber espionage,\nmalware and phishing schemes.''', '''The United States loses $100 billion\nannually as a result of cyber crime,\nwhich targets over 594 million victims\nper year.''', '''As consumers expand their tech use\nto new outlets, cyber criminals follow\nthem.''', '''Apple users should take caution, as\nMacs have become an attractive target\nfor cybercrime as the company gains\nmore market share.''']

####################################
# init
# to initialize needed variables
#################################### 

def init(data):
    # initial mode is "startGame1"
    data.mode = "startGame1"
    data.dotsize = 10 
    data.score = 0 
    data.timeLeft = 30
    data.time = 0
    data.isPaused = False 
    data.isFactOnScreen = False
    data.facts = Facts.facts 
    data.message = 0
    data.dots = [ ]
    data.colors = ["misty rose", "tomato", "gold", "dark turquoise", "medium purple", "chartreuse"]
    
####################################
# mode dispatcher
# learned from 15-112 notes
####################################

# goes to individual mode mousePressed functions
def mousePressed(event, data):
    if (data.mode == "startGame1"): 
        startGame1MousePressed(event, data)
    elif (data.mode == "helpScreen"):   
        helpScreenMousePressed(event, data)
    elif (data.mode == "playGame1"):   
        playGame1MousePressed(event, data)
    elif (data.mode == "winGame1"):   
        winGame1MousePressed(event, data)
    elif (data.mode == "restartGame1"):   
        restartGame1MousePressed(event, data)

# goes to individual mode keyPressed functions
def keyPressed(event, data):
    if (data.mode == "startGame1"): 
        startGame1KeyPressed(event, data)
    elif (data.mode == "helpScreen"):   
        helpScreenKeyPressed(event, data)
    elif (data.mode == "playGame1"):
        playGame1KeyPressed(event, data)
    elif (data.mode == "winGame1"):   
        winGame1KeyPressed(event, data)
    elif (data.mode == "restartGame1"):   
        restartGame1KeyPressed(event, data)

# goes to individual mode timerFired functions
def timerFired(data):
    if (data.mode == "startGame1"): 
        startGame1TimerFired(data)
    elif (data.mode == "helpScreen"):   
        helpScreenTimerFired(data)
    elif (data.mode == "playGame1"):   
        playGame1TimerFired(data)
    elif (data.mode == "winGame1"):   
        winGame1TimerFired(data)
    elif (data.mode == "restartGame1"):   
        restartGame1TimerFired(data)

# goes to individual mode redrawAll functions
def redrawAll(canvas, data):
    if (data.mode == "startGame1"): 
        startGame1RedrawAll(canvas, data)
    elif (data.mode == "helpScreen"):   
        helpScreenRedrawAll(canvas, data)
    elif (data.mode == "playGame1"):   
        playGame1RedrawAll(canvas, data)
    elif (data.mode == "winGame1"):   
        winGame1RedrawAll(canvas, data)
    elif (data.mode == "restartGame1"):   
        restartGame1RedrawAll(canvas, data)

####################################
# startGame1 mode
####################################

# draws the starting background 
def drawStartBackground(canvas, data):
    canvas.create_rectangle(5, 5, data.width, data.height, fill = "orange2", outline = "yellow2", width = 15)
    canvas.create_rectangle(25, 25, data.width - 17, data.height - 17, fill = "black", width = 0)
    canvas.create_text(data.width/2, data.height/3, text = "CYBER", fill = "lawn green", font = "Courier 75 bold")
    canvas.create_text(data.width/2, data.height/2, text = "MOVE", fill = "cyan", font = "Georgia 80 bold")

# draws the buttons going to "help" and "play"
def drawStartButtons(canvas, data):
    canvas.create_rectangle(data.width/4 - 40, data.height*3/4, data.width/4 + 100, data.height*3/4 + 50, fill = "magenta", outline = "white", width = 3)
    canvas.create_rectangle(data.width/3 + 115, data.height*3/4, data.width/3 + 255, data.height*3/4 + 50, fill = "firebrick2", outline = "white", width = 3)
 
# draws the buttons' text for "help" and "play"
def drawStartButtonsText(canvas, data):
    canvas.create_text(data.width/4 + 30, data.height*3/4 + 25, text = "HELP", fill = "black", font = "Courier 30 bold")
    canvas.create_text(data.width/3 + 185, data.height*3/4 + 25, text = "PLAY", fill = "black", font = "Courier 30 bold")
  
# game goes to helpScreen mode or playGame1 mode 
def startGame1MousePressed(event, data):
    # user's mouse x-coordinate and y-coordinate 
    userX = event.x
    userY = event.y
    # splash screen to helpScreen mode
    helpLeftX = data.width/4 - 40
    helpRightX = data.width/4 + 100
    helpTopY = data.height*3/4
    helpBottomY = data.height*3/4 + 50
    if (userX > helpLeftX and userX < helpRightX and userY > helpTopY and userY < helpBottomY):
        data.mode = "helpScreen"
    # splash screen to playGame1 mode
    playLeftX = data.width/3 + 115
    playRightX = data.width/3 + 255
    playTopY = data.height*3/4
    playBottomY = data.height*3/4 + 50
    if (userX > playLeftX and userX < playRightX and userY > playTopY and userY < playBottomY):
        data.mode = "playGame1"
    
def startGame1KeyPressed(event, data):
    pass
    
def startGame1TimerFired(data):
    pass

# draws the starting screen background and "help" and "play" buttons 
def startGame1RedrawAll(canvas, data):
    drawStartBackground(canvas, data)
    drawStartButtons(canvas, data)
    drawStartButtonsText(canvas, data)
    
####################################
# helpScreen mode
####################################

# draws the help screen background
def drawHelpBackground(canvas, data):
    canvas.create_rectangle(5, 5, data.width, data.height, fill = "black", outline = "yellow2", width = 15)
    canvas.create_text(data.width/2, data.height/7 + 30, text = "The goal of this game is", fill = "lawn green", font = "Courier 23 bold")
    canvas.create_text(data.width/2, data.height/7 + 60, text = "to click inside the circles.", fill = "cyan", font = "Courier 23 bold")
    canvas.create_text(data.width/2, data.height/7 + 90, text = "Every time you click, you will", fill = "magenta", font = "Courier 23 bold")
    canvas.create_text(data.width/2, data.height/7 + 120, text = "receive a point and a fact", fill = "yellow", font = "Courier 23 bold")
    canvas.create_text(data.width/2, data.height/7 + 150, text = "about cybersecurity will pop up,", fill = "firebrick1", font = "Courier 23 bold")
    canvas.create_text(data.width/2, data.height/7 + 180, text = "allowing you to learn about", fill = "hot pink", font = "Courier 23 bold")
    canvas.create_text(data.width/2, data.height/7 + 210, text = "your safety on the Internet.", fill = "chocolate1", font = "Courier 23 bold")
    
# draws the buttons going to "start" and "play" 
def drawHelpButtons(canvas, data):
    canvas.create_rectangle(data.width/4 - 40, data.height*3/4, data.width/4 + 100, data.height*3/4 + 50, fill = "magenta", outline = "white", width = 3)
    canvas.create_rectangle(data.width/3 + 115, data.height*3/4, data.width/3 + 255, data.height*3/4 + 50, fill = "firebrick2", outline = "white", width = 3)
    
# draws the buttons' text for "start" and "play"
def drawHelpButtonsText(canvas, data):
    canvas.create_text(data.width/4 + 30, data.height*3/4 + 25, text = "START", fill = "black", font = "Courier 30 bold")
    canvas.create_text(data.width/3 + 185, data.height*3/4 + 25, text = "PLAY", fill = "black", font = "Courier 30 bold") 
    
# game goes to startGame1 mode or playGame1 mode     
def helpScreenMousePressed(event, data):
    # user's mouse x-coordinate and y-coordinate 
    userX = event.x
    userY = event.y
    # splash screen to startGame1 mode
    startLeftX = data.width/4 - 40
    startRightX = data.width/4 + 100
    startTopY = data.height*3/4
    startBottomY = data.height*3/4 + 50
    if (userX > startLeftX and userX < startRightX and userY > startTopY and userY < startBottomY):
        data.mode = "startGame1"
    # splash screen to playGame1 mode
    playLeftX = data.width/3 + 115
    playRightX = data.width/3 + 255
    playTopY = data.height*3/4
    playBottomY = data.height*3/4 + 50
    if (userX > playLeftX and userX < playRightX and userY > playTopY and userY < playBottomY):
        data.mode = "playGame1"
    
def helpScreenKeyPressed(event, data):
    pass

def helpScreenTimerFired(data):
    pass

# draws the help screen background and "start" and "play" buttons
def helpScreenRedrawAll(canvas, data):
    drawHelpBackground(canvas, data)
    drawHelpButtons(canvas, data)
    drawHelpButtonsText(canvas, data)
    
####################################
# playGame1 mode
####################################
    
# draws the background (black screen)
def drawPlayBackground(canvas, data):
    canvas.create_rectangle(5, 5, data.width, data.height, fill = "black", width = 0)

# creates dots that are added to the set data.dots 
def createDot(data):
    # each dot has an x-coordinate, y-coordinate, and radius
    x = 0
    y = random.randint(50, 450)
    r = random.randint(20, 40)
    data.dots.append([x, y, r])

# draws the dots that are a part of the set data.dots 
def drawDot(canvas, data):
    for element in range(len(data.dots)):
        x = data.dots[element][0]
        y = data.dots[element][1]
        r = data.dots[element][2]
        # to choose a random color from data.colors list
        randomIndex = random.randint(0, len(data.colors) - 1)
        color = data.colors[randomIndex]
        canvas.create_oval(x - r + data.dotsize, y - r + data.dotsize, x + r + data.dotsize, y + r + data.dotsize, fill = color, width = 3)

# draws the time left in the upper left corner
def drawTimeLeft(canvas, data):
    score = "Time Left: " + str(data.timeLeft)
    xPosition = data.width/4 - 10
    yPosition = 30
    canvas.create_text(xPosition, yPosition, text = score, fill = "white", font = "Georgia 25 bold") 
     
# draws the score in the upper right corner
def drawScore(canvas, data):
    score = "Score: " + str(data.score)
    xPosition = data.width*4/5 + 20
    yPosition = 30
    canvas.create_text(xPosition, yPosition, text = score, fill = "white", font = "Georgia 25 bold")

# draws the buttons for "pause" and "help"
def drawPlayButtons(canvas, data):
    canvas.create_rectangle(data.width/10 - 20, data.height*7/8, data.width/10 + 60, data.height*7/8 + 35, fill = "magenta", outline = "yellow", width = 3)
    canvas.create_rectangle(data.width*6/7 - 35, data.height*7/8, data.width*6/7 + 45, data.height*7/8 + 35, fill = "firebrick2", outline = "yellow", width = 3)
    
# draws the buttons' text for "pause" and "help"
def drawPlayButtonsText(canvas, data):
    canvas.create_text(data.width/10 + 20, data.height*7/8 + 17.5, text = "PAUSE", fill = "white", font = "Courier 20 bold")
    canvas.create_text(data.width*6/7 + 5, data.height*7/8 + 17.5, text = "HELP", fill = "white", font = "Courier 20 bold") 
    
# pops up a fact screen every time the player clicks on a dot
def factScreen(canvas, data):
    canvas.create_rectangle(data.width/6, data.height/6, data.width*5/6, data.height*5/6, fill = "LightBlue1", outline = "DeepSkyBlue4", width = 3)
    canvas.create_text(data.width/6 + 65, data.height/6 + 10, text = "Cyber Fact!", fill = "DodgerBlue3", anchor = "nw", font = "Courier 30 bold")
    canvas.create_text(data.width/6 + 10, data.height/6 + 60, text = data.facts[data.message], fill = "black", anchor = "nw", font = "Georgia 15 bold")
    canvas.create_text(data.width/6 + 22, data.height/6 + 310, text = "Press \'p\' to continue playing", fill = "medium blue", anchor = "nw", font = "Courier 16 bold")
        
# distance formula from the Internet: http://www.teacherschoice.com.au/maths_library/analytical%20geometry/alg_15.htm
def distance(data, x1, y1, x2, y2):
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    
def playGame1MousePressed(event, data):
    # user's mouse x-coordinate and y-coordinate 
    userX = event.x
    userY = event.y
    # pauses the game
    pauseLeftX = data.width/10 - 20
    pauseRightX = data.width/10 + 60
    pauseTopY = data.height*7/8
    pauseBottomY = data.height*7/8 + 35
    if (userX > pauseLeftX and userX < pauseRightX and userY > pauseTopY and userY < pauseBottomY):
        data.isPaused = not data.isPaused
    # splash screen to helpScreen mode
    helpLeftX = data.width*6/7 - 35 
    helpRightX = data.width*6/7 + 45
    helpTopY = data.height*7/8
    helpBottomY = data.height*7/8 + 35
    if (userX > helpLeftX and userX < helpRightX and userY > helpTopY and userY < helpBottomY):
        data.mode = "helpScreen" 
    # adds to the score every time the user clicks within a dot
    for dot in data.dots:
        userX, userY = event.x, event.y
        dotX, dotY = dot[0], dot[1]
        dotR = dot[2]
        if (distance(data, userX, userY, dotX, dotY) < dotR):
            data.score += 1
            data.isPaused = True
            data.isFactOnScreen = True
            # picks a random fact from Facts fact
            data.message = random.randint(0, 8)

# to pause/unpause the game and for when the fact screen is displayed
def playGame1KeyPressed(event, data):
    if event.keysym == "p":
        data.isPaused = not data.isPaused  
        if (data.isFactOnScreen):
            data.isFactOnScreen = False
            
# for the time left, score, time, and creating dots
def playGame1TimerFired(data):
    data.timerDelay = 100
    if (data.timeLeft == -1 and data.score < 20):
        data.mode = "restartGame1"
    if (data.score >= 20 and data.timeLeft != 0):
        data.mode = "winGame1"
    if (not data.isPaused):
        data.time += 1
        # for data.timeLeft (the timer) 
        if (data.time % 10 == 0):
            data.timeLeft -= 1
        # if the user retrieves 20 or more points and there's still time left, then splash screen to winGame1
        # if the user doesn't retrieve 20 points and there's no time left, then splash screen to restartGame1
        if (data.timeLeft != 0 and data.score == 10):
            data.mode = "winGame1"
        if (data.timeLeft <= 0 and data.score < 10):
            data.mode = "restartGame1"
        # creates dots every increment of time 
        if (data.time % 20 == 0):
            createDot(data)
        # moves the dots to the right 
        if (data.time % 2 == 0):
            for element in range(len(data.dots)):
                data.dots[element][0] += 10
            
#draws the background, time left, score, buttons, and the dots 
def playGame1RedrawAll(canvas, data):
    drawPlayBackground(canvas, data)
    drawTimeLeft(canvas, data) 
    drawScore(canvas, data)
    drawPlayButtons(canvas, data)
    drawPlayButtonsText(canvas, data)
    drawDot(canvas, data)
    # if data.isFactOnScreen is True, then draw/display the fact screen
    if (data.isFactOnScreen == True):
        factScreen(canvas, data)
    
####################################
# winGame1 mode
####################################

# draws the win screen that tells the user the next object
def drawWinBackground(canvas, data):
    canvas.create_rectangle(5, 5, data.width, data.height, fill = "black", outline = "yellow2", width = 15)
    canvas.create_text(data.width/2, data.height/3 - 20, text = "Congrats!", fill = "cyan", font = "Courier 60 bold")
    canvas.create_text(500/2, 500/2 - 30, text = "The next object is", fill = "green2", font = "Courier 30 bold")
    canvas.create_text(500/2, 500/2, text = "the UMBRELLA VASE", fill = "green2", font = "Courier 30 bold")
    canvas.create_text(500/2, 500/2 + 30, text = "in room 2.", fill = "green2", font = "Courier 30 bold")
    canvas.create_text(data.width/2, 2.9*data.height/4, text = "Exit this window and press", fill = "magenta", font = "Courier 25 bold")
    canvas.create_text(data.width/2, 2.9*data.height/4 + 30, text = "\'1\' to return to rooms.", fill = "magenta", font = "Courier 25 bold")

def winGame1MousePressed(event, data):
    pass
    
def winGame1KeyPressed(event, data):
    pass
    
def winGame1TimerFired(data):
    pass

# draws the winning screen background
def winGame1RedrawAll(canvas, data):
    drawWinBackground(canvas, data)

####################################
# restartGame1 mode
####################################

# draws the restart screen that tells the user to play again
def drawRestartBackground(canvas, data):
    canvas.create_rectangle(5, 5, data.width, data.height, fill = "black", outline = "yellow2", width = 15)
    canvas.create_text(data.width/2, data.height/3 - 20, text = "Times Out!", fill = "cyan", font = "Courier 60 bold")
    canvas.create_text(data.width/2, data.height/3 + 50, text = "Looks like you didn't", fill = "lawn green", font = "Courier 23 bold")
    canvas.create_text(data.width/2, data.height/3 + 80, text = "complete the puzzle in time.", fill = "lawn green", font = "Courier 22 bold")
    canvas.create_text(data.width/2, data.height/3 + 130, text = "Try again!", fill = "magenta", font = "Courier 32 bold")

def drawPlayAgainButton(canvas, data):
    canvas.create_rectangle(data.width/2 - 75, data.height*3/4, data.width/2 + 75, data.height*3/4 + 50, fill = "firebrick2", outline = "white", width = 3)

def drawPlayAgainButtonText(canvas, data):
    canvas.create_text(data.width/2, data.height*3/4 + 25, text = "PLAY AGAIN", fill = "black", font = "Courier 22 bold")

def restartGame1MousePressed(event, data):
    # user's mouse x-coordinate and y-coordinate 
    userX = event.x
    userY = event.y
    # goes back to the beginning (init)
    playAgainLeftX = data.width/2 - 75
    playAgainRightX = data.width/2 + 75
    playAgainTopY = data.height*3/4
    playAgainBottomY = data.height*3/4 + 50
    if (userX > playAgainLeftX and userX < playAgainRightX and userY > playAgainTopY and userY < playAgainBottomY):
        init(data)
    
def restartGame1KeyPressed(event, data):
    pass
    
def restartGame1TimerFired(data):
    pass

# draws the restart screen background and "play again" button 
def restartGame1RedrawAll(canvas, data):
    drawRestartBackground(canvas, data)
    drawPlayAgainButton(canvas, data) 
    drawPlayAgainButtonText(canvas, data)
    
####################################
# runGame1 function 
# general run function template from 15-112 notes
####################################

def runGame1(width = 300, height = 300):
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
    root.title("Cyber Move")
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
    
runGame1(500, 500)