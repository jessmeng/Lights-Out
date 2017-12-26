####################################
# Jessica Meng, jmeng1, Section B
# Lights Out
# 15-112 Term Project 
# customizationPart2
# after the user escapes "Lights Out", they will get the option to build and customize their own game - a type of puzzle in "Lights Out"
# this is the second part of customization
# all colors used from: https://wiki.tcl.tk/37701
# root.geometry learned from: https://www.python-course.eu/tkinter_layout_management.php
####################################

####################################
# imports
# necessary to run program
#################################### 

from tkinter import *
import tkinter 
import copy
import math
import random 

####################################
# Facts class
# this contains all the facts that will be displayed
# user has the option to choose the number of facts they want 
# facts from: https://heimdalsecurity.com/blog/10-surprising-cyber-security-facts-that-may-affect-your-online-safety/  
####################################

#1 fact
class Facts1(object):
    facts = ['''The most expensive computer virus\nin the world and in cyber security\nhistory caused an estimated\nfinancial damage of $38.5 billion.\nThis virus was called MyDoom.''']

# 4 facts
class Facts2(object):
    facts = ['''The most expensive computer virus\nin the world and in cyber security\nhistory caused an estimated\nfinancial damage of $38.5 billion.\nThis virus was called MyDoom.''', '''Cyber attackers love social media\n(just as much as we do!),\nbecause users that spend a lot\nof time on social networks are\nvery likely to click links\nposted by their friends, which\nhackers use to their advantage.''', '''Oracle Java, Adobe Reader, or\nAdobe Flash is present on 99% of\ncomputers, which means that 99%\nof computer users are vulnerable\nto exploit kits (software\nvulnerabilities).''', '''Vulnerabilities that software often\npresent are extremely critical:\nall it takes is one click\non an infected advertising banner\nto give a hacker full access to\nyour computer.''']
  
# 8 facts
class Facts3(object):
    facts = ['''The most expensive computer virus\nin the world and in cyber security\nhistory caused an estimated\nfinancial damage of $38.5 billion.\nThis virus was called MyDoom.''', '''Cyber attackers love social media\n(just as much as we do!),\nbecause users that spend a lot\nof time on social networks are\nvery likely to click links\nposted by their friends, which\nhackers use to their advantage.''', '''Oracle Java, Adobe Reader, or\nAdobe Flash is present on 99% of\ncomputers, which means that 99%\nof computer users are vulnerable\nto exploit kits (software\nvulnerabilities).''', '''Vulnerabilities that software often\npresent are extremely critical:\nall it takes is one click\non an infected advertising banner\nto give a hacker full access to\nyour computer.''', '''Psychological manipulation of\nvictims is also another way cyber\nattackers manipulate their targets.\nThey use social engineering, or the\ntricking of people into performing\nactions or divulging confidential\ninformation.''', '''Your government is actually making\nyou vulnerable. Governments around\nthe world are creating malware and\nusing it as digital weapons or\nin espionage programs.''', '''Hacktivism, or a subversive use of\ncomputers and computer networks\nto promote a political agenda,\naccounts for half of the cyber\nattacks launched in the world.''', '''The average time to detect a\nmalicious or criminal attack, as\nfounded by a global study\nsample of organizations, is 170\ndays.''']
    
####################################
# init
# to initialize needed variables
####################################

def init(data):
   # initial mode is "startUserGame"
   data.mode = "startUserGame"
   
   # for the symbols
   data.pieceSize = 15
   data.enemySize = 15
   
   # for the game name
   data.nameArrowPressed = False
   data.numNameArrowClicks = 0
   data.gameName1 = False
   data.gameName2 = False
   data.gameName3 = False
   
   # for customizationScreen mode 
   # for the player
   data.playerArrowPressed = False
   data.numPlayerArrowClicks = 0
   data.player1 = True
   data.player2 = False 
   # for the piece
   data.pieceArrowPressed = False
   data.numPieceArrowClicks = 0
   data.piece1 = True
   data.piece2 = False 
   # for the enemy 
   data.enemyArrowPressed = False
   data.numEnemyArrowClicks = 0
   data.enemy1 = True
   data.enemy2 = False 
   # for the power up
   data.powerUpArrowPressed = False
   data.numPowerUpArrowClicks = 0
   data.powerUp1 = True
   data.powerUp2 = False
   # for the display/background
   data.displayArrowPressed = False
   data.numDisplayArrowClicks = 0
   data.display1 = True
   data.display2 = False
   # for the timeLeft
   data.timeArrowPressed = False
   data.numTimeArrowClicks = 0
   data.time1 = True
   data.time2 = False
   data.time3 = False
   data.time4 = False
   # for the number of facts
   data.factArrowPressed = False
   data.numFactArrowClicks = 0
   data.fact1 = True
   data.fact2 = False
   data.fact3 = False
   
   # for playUserGame mode
   data.symbols = [] 
   data.powerUps = []
   # list of facts
   data.facts = Facts1.facts 
   # for the score and timeLeft 
   data.score = 0 
   data.timeLeft = 20
   # for the player
   data.playX = data.width/2
   data.playY = data.height - 80
   data.playSize = 40
   data.playSpeed = 0
   data.time = 0 
   # for the power up
   data.powerX = 20
   data.powerY = 20
   data.powerSize = 20
   data.speed = 1
   data.isSpedUp = False
   # pauses/unpauses the game
   data.isPaused = False 
   # for the fact screen that pops up with the fact/message 
   data.isFactOnScreen = False
   data.isEnemy = False
   data.message = 0
   
   # for endUserGame mode
   # for the next object
   data.objectArrowPressed = False
   data.numObjectArrowClicks = 0
   data.object1 = True
   data.object2 = False
   data.object3 = False
   # for the room 
   data.roomArrowPressed = False
   data.numRoomArrowClicks = 0
   data.room1 = True
   data.room2 = False
   data.room3 = False
    
####################################
# mode dispatcher
# learned from 15-112 notes
####################################

# goes to individual mode mousePressed functions
def mousePressed(event, data):
   if (data.mode == "startUserGame"): 
      startUserGameMousePressed(event, data)
   elif (data.mode == "playUserGame"):   
      playUserGameMousePressed(event, data)
   elif (data.mode == "helpScreen"):   
      helpScreenMousePressed(event, data)
   elif (data.mode == "customizationScreen"):   
      customizationScreenMousePressed(event, data)
   elif (data.mode == "endUserGame"):   
      endUserGameMousePressed(event, data)
   elif (data.mode == "restartUserGame"):   
      restartUserGameMousePressed(event, data)

# goes to individual mode keyPressed functions
def keyPressed(event, data):
   if (data.mode == "startUserGame"): 
      startUserGameKeyPressed(event, data)
   elif (data.mode == "playUserGame"):
      playUserGameKeyPressed(event, data)
   elif (data.mode == "helpScreen"):   
      helpScreenKeyPressed(event, data)
   elif (data.mode == "customizationScreen"):   
      customizationScreenKeyPressed(event, data)
   elif (data.mode == "endUserGame"):   
      endUserGameKeyPressed(event, data)
   elif (data.mode == "restartUserGame"):   
      restartUserGameKeyPressed(event, data)

# goes to individual mode timerFired functions
def timerFired(data):
   if (data.mode == "startUserGame"): 
      startUserGameTimerFired(data)
   elif (data.mode == "playUserGame"):   
      playUserGameTimerFired(data)
   elif (data.mode == "helpScreen"):   
      helpScreenTimerFired(data)
   elif (data.mode == "customizationScreen"):   
      customizationScreenTimerFired(data)
   elif (data.mode == "endUserGame"):   
      endUserGameTimerFired(data)
   elif (data.mode == "restartUserGame"):   
      restartUserGameTimerFired(data)

# goes to individual mode redrawAll functions
def redrawAll(canvas, data):
   if (data.mode == "startUserGame"): 
      startUserGameRedrawAll(canvas, data)
   elif (data.mode == "playUserGame"):   
      playUserGameRedrawAll(canvas, data)
   elif (data.mode == "helpScreen"):   
      helpScreenRedrawAll(canvas, data)
   elif (data.mode == "customizationScreen"):   
      customizationScreenRedrawAll(canvas, data)
   elif (data.mode == "endUserGame"):   
      endUserGameRedrawAll(canvas, data)
   elif (data.mode == "restartUserGame"):   
      restartUserGameRedrawAll(canvas, data)

####################################
# startUserGame mode
####################################

# draws the starting background 
def drawStartBackground(canvas, data):
    canvas.create_rectangle(5, 5, data.width, data.height, fill = "orange2", outline = "yellow2", width = 15)
    canvas.create_rectangle(25, 25, data.width - 17, data.height - 17, fill = "black", width = 0)
    canvas.create_text(data.width/2, data.height/3 - 30, text = "CYBER", fill = "lawn green", font = "Courier 75 bold")
    canvas.create_polygon(100, 200, 70, 220, 100, 240, fill = "salmon1", outline = "DeepPink4", width = 2)
    canvas.create_polygon(400, 200, 430, 220, 400, 240, fill = "salmon1", outline = "DeepPink4", width = 2)
    canvas.create_text(data.width/2, data.height/2 - 30, text = "MOVE", fill = "cyan", font = "Georgia 80 bold")

# draws the buttons going to "customize", "help", and "play"
def drawStartButtons(canvas, data):
    canvas.create_rectangle(data.width/2 - 90, data.height*3/4 - 60, data.width/2 + 90, data.height*3/4 - 10, fill = "khaki1", outline = "white", width = 3)
    canvas.create_rectangle(data.width/4 - 40, data.height*3/4 + 20, data.width/4 + 100, data.height*3/4 + 70, fill = "magenta", outline = "white", width = 3)
    canvas.create_rectangle(data.width/3 + 115, data.height*3/4 + 20, data.width/3 + 255, data.height*3/4 + 70, fill = "firebrick2", outline = "white", width = 3)
 
# draws the buttons' text for "customize", "help", and "play"
def drawStartButtonsText(canvas, data):
    canvas.create_text(data.width/2, data.height*3/4 - 35, text = "CUSTOMIZE", fill = "red", font = "Courier 30 bold")
    canvas.create_text(data.width/4 + 30, data.height*3/4 + 45, text = "HELP", fill = "black", font = "Courier 30 bold")
    canvas.create_text(data.width/3 + 185, data.height*3/4 + 45, text = "PLAY", fill = "black", font = "Courier 30 bold")
    
# for the first name of the game
def drawGameName1(canvas, data):
    canvas.create_rectangle(105, 180, 395, 260, fill = "black")
    canvas.create_text(data.width/2, data.height/2 - 30, text = "MOVE", fill = "cyan", font = "Georgia 80 bold")
    
# for the second name of the game
def drawGameName2(canvas, data):
    canvas.create_rectangle(105, 180, 395, 260, fill = "black")
    canvas.create_text(data.width/2, data.height/2 - 30, text = "JUMP", fill = "cyan", font = "Georgia 80 bold")

# for the third name of the game
def drawGameName3(canvas, data):
    canvas.create_rectangle(105, 180, 395, 260, fill = "black")
    canvas.create_text(data.width/2, data.height/2 - 30, text = "LOCK", fill = "cyan", font = "Georgia 80 bold")
  
# game goes to helpScreen mode or playUserGame mode 
def startUserGameMousePressed(event, data):
    # user's mouse x-coordinate and y-coordinate 
    userX = event.x
    userY = event.y
    # for nameArrow left arrow
    nameLeftArrowLeftX = 70
    nameLeftArrowRightX = 100
    nameLeftArrowTopY = 200
    nameLeftArrowBottomY = 240
    if (userX > nameLeftArrowLeftX and userX < nameLeftArrowRightX and userY > nameLeftArrowTopY and userY < nameLeftArrowBottomY):
        data.nameArrowPressed = True 
        # keeps track of the number of nameArrow clicks and depending on that number, changes the game name
        data.numNameArrowClicks += 1
        if (data.numNameArrowClicks % 2 == 0 or data.numNameArrowClicks % 2 == 1):
            data.gameName2 = True
            data.gameName1 = False
            data.gameName3 = False
        if (data.numNameArrowClicks % 3 == 1): 
            data.gameName1 = True
            data.gameName2 = False
            data.gameName3 = False
        if (data.numNameArrowClicks % 3 == 0): 
            data.gameName3 = True
            data.gameName1 = False
            data.gameName2 = False
    # for nameArrow right arrow
    nameRightArrowLeftX = 400
    nameRightArrowRightX = 430
    nameRightArrowTopY = 200
    nameRightArrowBottomY = 240
    if (userX > nameRightArrowLeftX and userX < nameRightArrowRightX and userY > nameRightArrowTopY and userY < nameRightArrowBottomY):
        data.nameArrowPressed = True 
        # keeps track of the number of nameArrow clicks and depending on that number, changes the game name
        data.numNameArrowClicks += 1
        if (data.numNameArrowClicks % 2 == 0 or data.numNameArrowClicks % 2 == 1):
            data.gameName2 = True
            data.gameName1 = False
            data.gameName3 = False
        if (data.numNameArrowClicks % 3 == 1): 
            data.gameName1 = True
            data.gameName2 = False
            data.gameName3 = False
        if (data.numNameArrowClicks % 3 == 0): 
            data.gameName3 = True
            data.gameName1 = False
            data.gameName2 = False
    # splash screen to customizationScreen mode
    customLeftX = data.width/2 - 90
    customRightX = data.width/2 + 90
    customTopY = data.height*3/4 - 60
    customBottomY = data.height*3/4 - 10
    if (userX > customLeftX and userX < customRightX and userY > customTopY and userY < customBottomY):
        data.mode = "customizationScreen"
    # splash screen to helpScreen mode
    helpLeftX = data.width/4 - 40
    helpRightX = data.width/4 + 100
    helpTopY = data.height*3/4 + 20
    helpBottomY = data.height*3/4 + 70
    if (userX > helpLeftX and userX < helpRightX and userY > helpTopY and userY < helpBottomY):
        data.mode = "helpScreen"
    # splash screen to playUserGame mode
    playLeftX = data.width/3 + 115
    playRightX = data.width/3 + 255
    playTopY = data.height*3/4 + 20
    playBottomY = data.height*3/4 + 70
    if (userX > playLeftX and userX < playRightX and userY > playTopY and userY < playBottomY):
        data.mode = "playUserGame"
    
def startUserGameKeyPressed(event, data):
    pass
    
def startUserGameTimerFired(data):
    pass

# draws the starting screen background and "help" and "play" buttons and possible game names
def startUserGameRedrawAll(canvas, data):
    drawStartBackground(canvas, data)
    drawStartButtons(canvas, data)
    drawStartButtonsText(canvas, data)
    if (data.gameName1 == True):
        drawGameName1(canvas, data)
    if (data.gameName2 == True):
        drawGameName2(canvas, data)
    if (data.gameName3 == True):
        drawGameName3(canvas, data)

####################################
# customizationScreen mode
####################################

# draws the starting background 
def drawCustomBackground(canvas, data):
    canvas.create_rectangle(5, 5, data.width, data.height, fill = "black", outline = "yellow2", width = 15)
    canvas.create_text(data.width/2, data.height/6 - 30, text = "CREATE YOUR GAME:", fill = "turquoise1", font = "Georgia 35 bold")
    canvas.create_text(data.width/4 + 10, data.height/6 + 20, text = "PLAYER:", fill = "green2", font = "Courier 25 bold")
    canvas.create_polygon(60, 155, 40, 165, 60, 175, fill = "salmon1", outline = "DeepPink4", width = 2)
    canvas.create_polygon(200, 155, 220, 165, 200, 175, fill = "salmon1", outline = "DeepPink4", width = 2)
    canvas.create_text(data.width*3/4, data.height/6 + 20, text = "PIECE:", fill = "red2", font = "Courier 25 bold")
    canvas.create_polygon(300, 155, 280, 165, 300, 175, fill = "salmon1", outline = "DeepPink4", width = 2)
    canvas.create_polygon(440, 155, 460, 165, 440, 175, fill = "salmon1", outline = "DeepPink4", width = 2)
    canvas.create_text(data.width/4 + 10, data.height/2 - 20, text = "ENEMY:", fill = "orange", font = "Courier 25 bold")
    canvas.create_polygon(60, 280, 40, 290, 60, 300, fill = "salmon1", outline = "DeepPink4", width = 2)
    canvas.create_polygon(200, 280, 220, 290, 200, 300, fill = "salmon1", outline = "DeepPink4", width = 2)
    canvas.create_text(data.width*3/4, data.height/2 - 20, text = "POWER UP:", fill = "hot pink", font = "Courier 25 bold")
    canvas.create_polygon(300, 280, 280, 290, 300, 300, fill = "salmon1", outline = "DeepPink4", width = 2)
    canvas.create_polygon(440, 280, 460, 290, 440, 300, fill = "salmon1", outline = "DeepPink4", width = 2)
    canvas.create_text(data.width/4 - 20, data.height/2 + 90, text = "TIME:", fill = "violet", font = "Courier 25 bold")
    canvas.create_polygon(60, 375, 50, 385, 60, 395, fill = "salmon1", outline = "DeepPink4", width = 2)
    canvas.create_polygon(140, 375, 150, 385, 140, 395, fill = "salmon1", outline = "DeepPink4", width = 2)
    canvas.create_text(data.width/2, data.height/2 + 90, text = "DISPLAY:", fill = "turquoise3", font = "Courier 25 bold")
    canvas.create_polygon(240, 375, 250, 365, 260, 375, fill = "salmon1", outline = "DeepPink4", width = 2)
    canvas.create_polygon(240, 455, 250, 465, 260, 455, fill = "salmon1", outline = "DeepPink4", width = 2)
    canvas.create_text(data.width*3/4 + 20, data.height/2 + 90, text = "# FACTS:", fill = "NavajoWhite", font = "Courier 25 bold")
    canvas.create_polygon(350, 375, 340, 385, 350, 395, fill = "salmon1", outline = "DeepPink4", width = 2)
    canvas.create_polygon(450, 375, 460, 385, 450, 395, fill = "salmon1", outline = "DeepPink4", width = 2)

# draws the buttons going to "customize", "help", and "play"
def drawCustomButtons(canvas, data):
    canvas.create_rectangle(data.width/10 - 20, data.height*7/8, data.width/10 + 60, data.height*7/8 + 35, fill = "magenta", outline = "white", width = 3)
    canvas.create_rectangle(data.width*6/7 - 35, data.height*7/8, data.width*6/7 + 45, data.height*7/8 + 35, fill = "firebrick2", outline = "white", width = 3)
 
# draws the buttons' text for "customize", "help", and "play"
def drawCustomButtonsText(canvas, data):
    canvas.create_text(data.width/10 + 20, data.height*7/8 + 17.5, text = "HELP", fill = "white", font = "Courier 20 bold")
    canvas.create_text(data.width*6/7 + 5, data.height*7/8 + 17.5, text = "PLAY", fill = "white", font = "Courier 20 bold") 
  
# draws player 1
def drawPlayer1(canvas, data):
    canvas.create_rectangle(65, 135, 195, 185, fill = "black")
    canvas.create_rectangle(115, 145, 145, 185, fill = "light blue", outline = "maroon", width = 2)

# draws player 2
def drawPlayer2(canvas, data):
    canvas.create_rectangle(65, 135, 195, 185, fill = "black")
    canvas.create_polygon(110, 145, 130, 185, 150, 145, fill = "pale green", outline = "maroon", width = 2)

# draws piece 1
def drawPiece1(canvas, data):
    canvas.create_rectangle(305, 135, 435, 185, fill = "black")
    canvas.create_oval(355, 150, 385, 180, outline = "pink", width = 3)

# draws piece 2
def drawPiece2(canvas, data):
    canvas.create_rectangle(305, 135, 435, 185, fill = "black")
    canvas.create_oval(355, 150, 385, 180, fill = "medium spring green", outline = "plum", width = 2)
    canvas.create_oval(365, 140, 375, 150, fill = "medium spring green", outline = "plum", width = 2)

# draws enemy 1
def drawEnemy1(canvas, data):
    canvas.create_rectangle(65, 260, 195, 300, fill = "black")
    canvas.create_rectangle(115, 275, 145, 305, fill = "violet", outline = "cyan", width = 2)

# draws enemy 2
def drawEnemy2(canvas, data):
    canvas.create_rectangle(65, 260, 195, 300, fill = "black")
    canvas.create_rectangle(115, 275, 145, 305, fill = "bisque2", outline = "coral", width = 2)
    canvas.create_rectangle(125, 285, 135, 295, outline = "tan4", width = 3)

# draws power up 1
def drawPowerUp1(canvas, data):
    canvas.create_rectangle(305, 260, 435, 300, fill = "black")
    # draws a star (template taken from lab4) 
    outRad = 20
    inOut = 0.382
    inRad = (outRad * inOut)
    allPoints = []
    for point in range(2 * 5):
        angleOfPoint = math.pi/2 - (2*math.pi)*(point/(5*2))
        # if point is even, use the outer radius 
        if (point % 2 == 0):
            pointRad = outRad
        # if point is odd, use the inner radius
        if (point % 2 == 1):
            pointRad = inRad
        pointX = 370 + (pointRad*math.cos(angleOfPoint))
        pointY = 290 - (pointRad*math.sin(angleOfPoint))
        allPoints += (pointX, pointY)
    canvas.create_polygon(allPoints, fill = "LightPink1", outline = "green2", width = 2)
    
# draws power up 2
def drawPowerUp2(canvas, data):
    canvas.create_rectangle(305, 260, 435, 300, fill = "black")
    # draws a star (template taken from lab4) 
    outRad = 20
    inOut = 0.382
    inRad = (outRad * inOut)
    allPoints = []
    for point in range(2 * 5):
        angleOfPoint = math.pi/2 - (2*math.pi)*(point/(5*2))
        # if point is even, use the outer radius 
        if (point % 2 == 0):
            pointRad = outRad
        # if point is odd, use the inner radius
        if (point % 2 == 1):
            pointRad = inRad
        pointX = 370 + (pointRad*math.cos(angleOfPoint))
        pointY = 290 - (pointRad*math.sin(angleOfPoint))
        allPoints += (pointX, pointY)
    canvas.create_polygon(allPoints, fill = "IndianRed1", outline = "CadetBlue1", width = 2)

# draws time left 1
def drawTime1(canvas, data):
    canvas.create_rectangle(65, 365, 135, 400, fill = "black")
    canvas.create_text(100, 385, text = "20", fill = "white", font = "Courier 30 bold")

# draws time left 2
def drawTime2(canvas, data):
    canvas.create_rectangle(65, 365, 135, 400, fill = "black")
    canvas.create_text(100, 385, text = "30", fill = "white", font = "Courier 30 bold")
    
# draws time left 3
def drawTime3(canvas, data):
    canvas.create_rectangle(65, 365, 135, 400, fill = "black")
    canvas.create_text(100, 385, text = "40", fill = "white", font = "Courier 30 bold")
    
# draws display/background 1
def drawDisplay1(canvas, data):
    canvas.create_rectangle(200, 380, 300, 450, fill = "black")
    canvas.create_rectangle(220, 385, 280, 445, fill = "midnight blue", outline = "white", width = 2)
    canvas.create_text(240, 415, text = "1", fill = "royal blue", font = "Courier 22 bold")
    canvas.create_text(260, 415, text = "0", fill = "slategray", font = "Courier 22 bold")

# draws display/background 2
def drawDisplay2(canvas, data):
    canvas.create_rectangle(200, 380, 300, 450, fill = "black")
    canvas.create_rectangle(220, 385, 280, 445, fill = "purple4", outline = "white", width = 2)
    canvas.create_text(240, 410, text = ".", fill = "MediumOrchid3", font = "Courier 25 bold")
    canvas.create_text(260, 415, text = "1", fill = "MediumPurple3", font = "Courier 22 bold")

# draws number of facts 1 (1 fact)
def drawFact1(canvas, data):
    canvas.create_rectangle(355, 365, 445, 400, fill = "black")
    canvas.create_text(400, 385, text = "1", fill = "white", font = "Courier 30 bold")

# draws number of facts 2 (4 facts)
def drawFact2(canvas, data):
    canvas.create_rectangle(355, 365, 445, 400, fill = "black")
    canvas.create_text(400, 385, text = "4", fill = "white", font = "Courier 30 bold")
    
# draws number of facts 3 (8 facts)
def drawFact3(canvas, data):
    canvas.create_rectangle(355, 365, 445, 400, fill = "black")
    canvas.create_text(400, 385, text = "8", fill = "white", font = "Courier 30 bold")
    
# game goes to helpScreen mode or playUserGame mode 
def customizationScreenMousePressed(event, data):
    # user's mouse x-coordinate and y-coordinate 
    userX = event.x
    userY = event.y
    # for playerArrow left arrow
    playerLeftArrowLeftX = 40
    playerLeftArrowRightX = 60
    playerLeftArrowTopY = 155
    playerLeftArrowBottomY = 175
    if (userX > playerLeftArrowLeftX and userX < playerLeftArrowRightX and userY > playerLeftArrowTopY and userY < playerLeftArrowBottomY):
        data.playerArrowPressed = True 
        # keeps track of the number of playerArrow clicks and depending on that number, changes the player
        data.numPlayerArrowClicks += 1
        if (data.numPlayerArrowClicks % 2 == 1):
            data.player2 = True
            data.player1 = False
        if (data.numPlayerArrowClicks % 2 == 0): 
            data.player1 = True
            data.player2 = False
    # for playerArrow right arrow
    playerRightArrowLeftX = 200
    playerRightArrowRightX = 220
    playerRightArrowTopY = 155
    playerRightArrowBottomY = 175
    if (userX > playerRightArrowLeftX and userX < playerRightArrowRightX and userY > playerRightArrowTopY and userY < playerRightArrowBottomY):
        data.playerArrowPressed = True 
        # keeps track of the number of playerArrow clicks and depending on that number, changes the player
        data.numPlayerArrowClicks += 1
        if (data.numPlayerArrowClicks % 2 == 1):
            data.player2 = True
            data.player1 = False
        if (data.numPlayerArrowClicks % 2 == 0): 
            data.player1 = True
            data.player2 = False
    # for pieceArrow left arrow
    pieceLeftArrrowLeftX = 280
    pieceLeftArrrowRightX = 300
    pieceLeftArrrowTopY = 155
    pieceLeftArrrowBottomY = 175
    if (userX > pieceLeftArrrowLeftX and userX < pieceLeftArrrowRightX and userY > pieceLeftArrrowTopY and userY < pieceLeftArrrowBottomY):
        data.pieceArrowPressed = True 
        # keeps track of the number of pieceArrow clicks and depending on that number, changes the piece
        data.numPieceArrowClicks += 1
        if (data.numPieceArrowClicks % 2 == 1):
            data.piece2 = True
            data.piece1 = False
        if (data.numPieceArrowClicks % 2 == 0): 
            data.piece1 = True
            data.piece2 = False
    # for pieceArrow right arrow 
    pieceRightArrowLeftX = 440
    pieceRightArrowRightX = 460
    pieceRightArrowTopY = 155
    pieceRightArrowBottomY = 175
    if (userX > pieceRightArrowLeftX and userX < pieceRightArrowRightX and userY > pieceRightArrowTopY and userY < pieceRightArrowBottomY):
        data.pieceArrowPressed = True 
        # keeps track of the number of pieceArrow clicks and depending on that number, changes the piece
        data.numPieceArrowClicks += 1
        if (data.numPieceArrowClicks % 2 == 1):
            data.piece2 = True
            data.piece1 = False
        if (data.numPieceArrowClicks % 2 == 0): 
            data.piece1 = True
            data.piece2 = False
    # for enemyArrow left arrow
    enemyLeftArrowLeftX = 40
    enemyLeftArrowRightX = 60
    enemyLeftArrowTopY = 280
    enemyLeftArrowBottomY = 300
    if (userX > enemyLeftArrowLeftX and userX < enemyLeftArrowRightX and userY > enemyLeftArrowTopY and userY < enemyLeftArrowBottomY):
        data.enemyArrowPressed = True 
        # keeps track of the number of enemyArrow clicks and depending on that number, changes the enemy
        data.numEnemyArrowClicks += 1
        if (data.numEnemyArrowClicks % 2 == 1):
            data.enemy2 = True
            data.enemy1 = False
        if (data.numEnemyArrowClicks % 2 == 0): 
            data.enemy1 = True
            data.enemy2 = False
    # for enemyArrow right arrow 
    enemyRightArrowLeftX = 200
    enemyRightArrowRightX = 220
    enemyRightArrowTopY = 280
    enemyRightArrowBottomY = 300
    if (userX > enemyRightArrowLeftX and userX < enemyRightArrowRightX and userY > enemyRightArrowTopY and userY < enemyRightArrowBottomY):
        data.enemyArrowPressed = True 
        # keeps track of the number of enemyArrow clicks and depending on that number, changes the enemy
        data.numEnemyArrowClicks += 1
        if (data.numEnemyArrowClicks % 2 == 1):
            data.enemy2 = True
            data.enemy1 = False
        if (data.numEnemyArrowClicks % 2 == 0): 
            data.enemy1 = True
            data.enemy2 = False
    # for powerUpArrow left arrow
    powerUpLeftArrowLeftX = 280
    powerUpLeftArrowRightX = 300
    powerUpLeftArrowTopY = 280
    powerUpLeftArrowBottomY = 300
    if (userX > powerUpLeftArrowLeftX and userX < powerUpLeftArrowRightX and userY > powerUpLeftArrowTopY and userY < powerUpLeftArrowBottomY):
        data.powerUpArrowPressed = True 
        # keeps track of the number of powerUpArrow clicks and depending on that number, changes the power up 
        data.numPowerUpArrowClicks += 1
        if (data.numPowerUpArrowClicks % 2 == 1):
            data.powerUp2 = True
            data.powerUp1 = False
        if (data.numPowerUpArrowClicks % 2 == 0): 
            data.powerUp1 = True
            data.powerUp2 = False
    # for powerUpArrow right arrow 
    powerUpRightArrowLeftX = 440
    powerUpRightArrowRightX = 460
    powerUpRightArrowTopY = 280
    powerUpRightArrowBottomY = 300
    if (userX > powerUpRightArrowLeftX and userX < powerUpRightArrowRightX and userY > powerUpRightArrowTopY and userY < powerUpRightArrowBottomY):
        data.powerUpArrowPressed = True 
        # keeps track of the number of powerUpArrow clicks and depending on that number, changes the power up
        data.numPowerUpArrowClicks += 1
        if (data.numPowerUpArrowClicks % 2 == 1):
            data.powerUp2 = True
            data.powerUp1 = False
        if (data.numPowerUpArrowClicks % 2 == 0): 
            data.powerUp1 = True
            data.powerUp2 = False
    # for timeArrow left arrow
    timeLeftArrowLeftX = 50
    timeLeftArrowRightX = 60
    timeLeftArrowTopY = 375
    timeLeftArrowBottomY = 395
    if (userX > timeLeftArrowLeftX and userX < timeLeftArrowRightX and userY > timeLeftArrowTopY and userY < timeLeftArrowBottomY):
        data.timeArrowPressed = True 
        # keeps track of the number of timeArrow clicks and depending on that number, changes the time left
        data.numTimeArrowClicks += 1
        if (data.numTimeArrowClicks % 2 == 0 or data.numTimeArrowClicks % 2 == 1):
            data.time2 = True
            data.time1 = False
            data.time3 = False
            data.timeLeft = 30
        if (data.numTimeArrowClicks % 3 == 1): 
            data.time1 = True
            data.time2 = False
            data.time3 = False
            data.timeLeft = 20
        if (data.numTimeArrowClicks % 3 == 0): 
            data.time3 = True
            data.time1 = False
            data.time2 = False
            data.timeLeft = 40
    # for timeArrow right arrow
    timeRightArrowLeftX = 140
    timeRightArrowRightX = 150
    timeRightArrowTopY = 375
    timeRightArrowBottomY = 395
    if (userX > timeRightArrowLeftX and userX < timeRightArrowRightX and userY > timeRightArrowTopY and userY < timeRightArrowBottomY):
        data.timeArrowPressed = True 
        # keeps track of the number of timeArrow clicks and depending on that number, changes the time left
        data.numTimeArrowClicks += 1
        if (data.numTimeArrowClicks % 2 == 0 or data.numTimeArrowClicks % 2 == 1):
            data.time2 = True
            data.time1 = False
            data.time3 = False
            data.timeLeft = 30
        if (data.numTimeArrowClicks % 3 == 1): 
            data.time1 = True
            data.time2 = False
            data.time3 = False
            data.timeLeft = 20
        if (data.numTimeArrowClicks % 3 == 0): 
            data.time3 = True
            data.time1 = False
            data.time2 = False
            data.timeLeft = 40
    # for displayArrow left arrow
    displayLeftArrowLeftX = 240
    displayLeftArrowRightX = 260
    displayLeftArrowTopY = 365
    displayLeftArrowBottomY = 375
    if (userX > displayLeftArrowLeftX and userX < displayLeftArrowRightX and userY > displayLeftArrowTopY and userY < displayLeftArrowBottomY):
        data.displayArrowPressed = True 
        # keeps track of the number of displayArrow clicks and depending on that number, changes the display
        data.numDisplayArrowClicks += 1
        if (data.numDisplayArrowClicks % 2 == 1):
            data.display2 = True
            data.display1 = False
        if (data.numDisplayArrowClicks % 2 == 0): 
            data.display1 = True
            data.display2 = False
    # for displayArrow right arrow 
    displayRightArrowLeftX = 240
    displayRightArrowRightX = 260
    displayRightArrowTopY = 455
    displayRightArrowBottomY = 465
    if (userX > displayRightArrowLeftX and userX < displayRightArrowRightX and userY > displayRightArrowTopY and userY < displayRightArrowBottomY):
        data.displayArrowPressed = True 
        # keeps track of the number of displayArrow clicks and depending on that number, changes the display
        data.numDisplayArrowClicks += 1
        if (data.numDisplayArrowClicks % 2 == 1):
            data.display2 = True
            data.display1 = False
        if (data.numDisplayArrowClicks % 2 == 0): 
            data.display1 = True
            data.display2 = False
    # for factArrow left arrow
    factLeftArrowLeftX = 340
    factLeftArrowRightX = 350
    factLeftArrowTopY = 375
    factLeftArrowBottomY = 395
    if (userX > factLeftArrowLeftX and userX < factLeftArrowRightX and userY > factLeftArrowTopY and userY < factLeftArrowBottomY):
        data.timeArrowPressed = True 
        # keeps track of the number of factArrow clicks and depending on that number, changes the number of facts
        data.numFactArrowClicks += 1
        if (data.numFactArrowClicks % 2 == 0 or data.numFactArrowClicks % 2 == 1):
            data.fact2 = True
            data.fact1 = False
            data.fact3 = False
            data.facts = Facts2.facts
        if (data.numFactArrowClicks % 3 == 1): 
            data.fact1 = True
            data.fact2 = False
            data.fact3 = False
            data.facts = Facts1.facts
        if (data.numFactArrowClicks % 3 == 0): 
            data.fact3 = True
            data.fact1 = False
            data.fact2 = False
            data.facts = Facts3.facts
    # for factArrow right arrow
    factRightArrowLeftX = 450
    factRightArrowRightX = 460
    factRightArrowTopY = 375
    factRightArrowBottomY = 395
    if (userX > factRightArrowLeftX and userX < factRightArrowRightX and userY > factRightArrowTopY and userY < factRightArrowBottomY):
        data.factArrowPressed = True 
        # keeps track of the number of factArrow clicks and depending on that number, changes the number of facts
        data.numFactArrowClicks += 1
        if (data.numFactArrowClicks % 2 == 0 or data.numFactArrowClicks % 2 == 1):
            data.fact2 = True
            data.fact1 = False
            data.fact3 = False
            data.facts = Facts2.facts
        if (data.numFactArrowClicks % 3 == 1): 
            data.fact1 = True
            data.fact2 = False
            data.fact3 = False
            data.facts = Facts1.facts
        if (data.numFactArrowClicks % 3 == 0): 
            data.fact3 = True
            data.fact1 = False
            data.fact2 = False
            data.facts = Facts3.facts
    # splash screen to helpScreen mode
    helpLeftX = data.width/10 - 20
    helpRightX = data.width/10 + 60
    helpTopY = data.height*7/8
    helpBottomY = data.height*7/8 + 35
    if (userX > helpLeftX and userX < helpRightX and userY > helpTopY and userY < helpBottomY):
        data.mode = "helpScreen" 
    # splash screen to helpScreen mode
    playLeftX = data.width*6/7 - 35 
    playRightX = data.width*6/7 + 45
    playTopY = data.height*7/8
    playBottomY = data.height*7/8 + 35
    if (userX > playLeftX and userX < playRightX and userY > playTopY and userY < playBottomY):
        data.mode = "playUserGame" 
    
def customizationScreenKeyPressed(event, data):
    pass
    
def customizationScreenTimerFired(data):
    pass

# draws the custom screen background and "help" and "play" buttons and possible customization options
def customizationScreenRedrawAll(canvas, data):
    drawCustomBackground(canvas, data)
    drawCustomButtons(canvas, data)
    drawCustomButtonsText(canvas, data)
    # for the player
    if (data.player1 == True):
        drawPlayer1(canvas, data)
    if (data.player2 == True):
        drawPlayer2(canvas, data)
    # for the piece
    if (data.piece1 == True):
        drawPiece1(canvas, data)
    if (data.piece2 == True):
        drawPiece2(canvas, data)
    # for the enemy
    if (data.enemy1 == True):
        drawEnemy1(canvas, data)
    if (data.enemy2 == True):
        drawEnemy2(canvas, data)
    # for the power up
    if (data.powerUp1 == True):
        drawPowerUp1(canvas, data)
    if (data.powerUp2 == True):
        drawPowerUp2(canvas, data)
    # for the display/background
    if (data.display1 == True):
        drawDisplay1(canvas, data)
    if (data.display2 == True):
        drawDisplay2(canvas, data)
    # for the time left
    if (data.time1 == True):
        drawTime1(canvas, data)
    if (data.time2 == True):
        drawTime2(canvas, data)
    if (data.time3 == True):
        drawTime3(canvas, data)
    # for the number of facts
    if (data.fact1 == True):
        drawFact1(canvas, data)
    if (data.fact2 == True):
        drawFact2(canvas, data)
    if (data.fact3 == True):
        drawFact3(canvas, data)
        
####################################
# helpScreen mode
####################################

# draws the instruction screen
def drawInstructions(canvas, data):
    canvas.create_rectangle(5, 5, data.width, data.height, fill = "black", outline = "yellow2", width = 15)
    canvas.create_text(data.width/2, data.height/7, text = "The goal of this game is", fill = "lawn green", font = "Courier 23 bold")
    canvas.create_text(data.width/2, data.height/7 + 30, text = "retrieve pieces and power ups", fill = "cyan", font = "Courier 23 bold")
    canvas.create_text(data.width/2, data.height/7 + 60, text = "for points and to avoid", fill = "magenta", font = "Courier 23 bold")
    canvas.create_text(data.width/2, data.height/7 + 90, text = "the enemies. Everytime you", fill = "yellow", font = "Courier 23 bold")
    canvas.create_text(data.width/2, data.height/7 + 120, text = "hit an enemy, a fact about", fill = "SeaGreen1", font = "Courier 23 bold")
    canvas.create_text(data.width/2, data.height/7 + 150, text = "cybersecurity will pop up,", fill = "firebrick1", font = "Courier 23 bold")
    canvas.create_text(data.width/2, data.height/7 + 180, text = "allowing you to learn about", fill = "hot pink", font = "Courier 23 bold")
    canvas.create_text(data.width/2, data.height/7 + 210, text = "your safety on the Internet.", fill = "chocolate1", font = "Courier 23 bold")
 
# draws the buttons going to "customize", "start", and "play" 
def drawInstructionButtons(canvas, data):
    canvas.create_rectangle(data.width/2 - 90, data.height*3/4 - 40, data.width/2 + 90, data.height*3/4 + 10, fill = "khaki1", outline = "white", width = 3)
    canvas.create_rectangle(data.width/4 - 40, data.height*3/4 + 35, data.width/4 + 100, data.height*3/4 + 85, fill = "magenta", outline = "white", width = 3)
    canvas.create_rectangle(data.width/3 + 115, data.height*3/4 + 35, data.width/3 + 255, data.height*3/4 + 85, fill = "firebrick2", outline = "white", width = 3)
    
# draws the buttons' text for "customize", "help", and "play"
def drawInstructionButtonsText(canvas, data):
    canvas.create_text(data.width/2, data.height*3/4 - 15, text = "CUSTOMIZE", fill = "red", font = "Courier 30 bold")
    canvas.create_text(data.width/4 + 30, data.height*3/4 + 60, text = "START", fill = "black", font = "Courier 30 bold")
    canvas.create_text(data.width/3 + 185, data.height*3/4 + 60, text = "PLAY", fill = "black", font = "Courier 30 bold")
    
# game goes to startUserGame mode or playUserGame mode     
def helpScreenMousePressed(event, data):
    userX = event.x
    userY = event.y
    # splash screen to customizationScreen mode
    customLeftX = data.width/2 - 90
    customRightX = data.width/2 + 90
    customTopY = data.height*3/4 - 40
    customBottomY = data.height*3/4 + 10
    if (userX > customLeftX and userX < customRightX and userY > customTopY and userY < customBottomY):
        data.mode = "customizationScreen"
    # splash screen to helpScreen mode
    startLeftX = data.width/4 - 40
    startRightX = data.width/4 + 100
    startTopY = data.height*3/4 + 35
    startBottomY = data.height*3/4 + 85
    if (userX > startLeftX and userX < startRightX and userY > startTopY and userY < startBottomY):
        data.mode = "startUserGame"
    # splash screen to playUserGame mode
    playLeftX = data.width/3 + 115
    playRightX = data.width/3 + 255
    playTopY = data.height*3/4 + 35
    playBottomY = data.height*3/4 + 85
    if (userX > playLeftX and userX < playRightX and userY > playTopY and userY < playBottomY):
        data.mode = "playUserGame"

def helpScreenKeyPressed(event, data):
    pass

def helpScreenTimerFired(data):
    pass 
    
# creates the instruction screen 
def helpScreenRedrawAll(canvas, data):
    drawInstructions(canvas, data)
    drawInstructionButtons(canvas ,data)
    drawInstructionButtonsText(canvas, data)
    
####################################
# playUserGame mode
####################################

# draws the game background
def drawGameBackground(canvas, data):
    if (data.display1 == True):
        canvas.create_rectangle(5, 5, data.width, data.height, fill = "midnight blue", width = 0)
        # for the binary in the background (1s and 0s)
        for first in range(30, 401, 90): 
            canvas.create_text(250, first, text = "1 0 1 0 1 0 1 0 1 0 1 0 1 0", fill = "blue", font = "Courier 30")
        for second in range(60, 481, 90): 
            canvas.create_text(250, second, text = "1 0 1 0 1 0 1 0 1 0 1 0 1 0", fill = "royal blue", font = "Courier 30")
        for last in range(90, 481, 90): 
            canvas.create_text(250, last, text = "1 0 1 0 1 0 1 0 1 0 1 0 1 0", fill = "slategray", font = "Courier 30")
        canvas.create_rectangle(0, 470, data.width, data.height, fill = "blue4", width = 0)
    if (data.display2 == True):
        canvas.create_rectangle(5, 5, data.width, data.height, fill = "purple4", width = 0)
        # for the dots and binary in the background
        for first in range(30, 481, 90): 
            canvas.create_text(250, first, text = ". . . . . . . . . . . . . .", fill = "MediumOrchid3", font = "Courier 30")
        for second in range(60, 481, 90): 
            canvas.create_text(250, second, text = ". . . . . . . . . . . . . .", fill = "MediumPurple3", font = "Courier 30")
        for last in range(90, 481, 90): 
            canvas.create_text(250, last, text = "1 0 1 0 1 0 1 0 1 0 1 0 1 0", fill = "purple2", font = "Courier 30")
        canvas.create_rectangle(0, 470, data.width, data.height, fill = "HotPink3", width = 0)

# draws the time left, score, "h" for help, "c" to customize, and "p" to pause/unpause displayed during the game 
def drawTimeAndScore(canvas, data):
    timeLeft = "Time Left: " + str(data.timeLeft)
    canvas.create_text(100, data.height/16, text = timeLeft, fill = "orange", font = "Courier 20 bold")
    score = "Score: " + str(data.score)
    canvas.create_text(75, data.height/9, text = score, fill = "yellow2", font = "Courier 20 bold")
    canvas.create_text(data.width*3.75/5 + 13, data.height/16, text = "Press \'h\' for help", fill = "white", font = "Courier 16 bold")
    canvas.create_text(data.width*3.4/5 + 28, data.height/16 + 20, text = "Press \'c\' to customize", fill = "white", font = "Courier 16 bold")
    canvas.create_text(data.width*3.4/5 + 10, data.height/16 + 40, text = "Press \'p\' to pause/unpause", fill = "white", font = "Courier 16 bold")

# draws the player    
def drawPlayer(canvas,data):
    if (data.player1 == True):
        canvas.create_rectangle(data.playX, data.playY, data.playX + data.playSize, data.playY + data.playSize + 10, fill = "light blue", outline = "maroon", width = 3)
    if (data.player2 == True):
        canvas.create_polygon(data.playX, data.playY - data.playSize/200, data.playX + data.playSize, data.playY - data.playSize/200, data.playX + data.playSize/2, data.playY + 2.4*data.playSize/2, fill = "pale green", outline = "maroon", width = 2)

# creates a new symbol (either piece or enemy) and adds to list data.symbols
def createSymbol(data):
    x = random.randint(50, 450)
    y = 0
    symbol = random.randint(0, 1) 
    data.symbols.append([x, y, symbol])   
    
# draws a random symbol based on list data.symbols
def drawSymbols(canvas, data):
    for element in range(len(data.symbols)):
        x = data.symbols[element][0]
        y = data.symbols[element][1]
        symbol = data.symbols[element][2]
        # if symbol is 0 (bad), then draw the enemy symbol depending on user's choice
        if (symbol == 0):
            if (data.enemy1 == True):
                canvas.create_rectangle(x, y, x + 2*data.enemySize, y + 2*data.enemySize, fill = "violet", outline = "cyan", width = 2) 
            if (data.enemy2 == True):
                canvas.create_rectangle(x, y, x + 2*data.enemySize, y + 2*data.enemySize, fill = "bisque2", outline = "coral", width = 2)
                canvas.create_rectangle(x + 1.2*data.enemySize/2, y + 1.2*data.enemySize/2, x + 2.6*data.enemySize/2, y + 2.5*data.enemySize/2, outline = "tan4", width = 3)
        # if symbol is 1 (good), then draw the piece symbol depending on user's choice
        elif (symbol == 1):
            if (data.piece1 == True):
                canvas.create_oval(x - data.pieceSize, y - data.pieceSize, x + data.pieceSize, y + data.pieceSize, outline = "pink", width = 3)
            if (data.piece2 == True):
                canvas.create_oval(x - data.pieceSize, y - data.pieceSize, x + data.pieceSize, y + data.pieceSize, fill = "medium spring green", outline = "plum", width = 2)
                canvas.create_oval(x - data.pieceSize/4, y - 1.6*data.pieceSize, x + data.pieceSize/4, y - data.pieceSize, fill = "medium spring green", outline = "plum", width = 2)
            
# creates new power up to list data.powerUps
def createPowerUp(data):
    x = random.randint(50, 450)
    y = 0
    data.powerUps.append([x, y])  
    
# draws the power up depending on the user's choice
def drawPowerUp(canvas, data):
    if (data.powerUp1 == True):
        # drawing star template taken from lab4
        for element in range(len(data.powerUps)):
            centerX = data.powerUps[element][0]
            centerY = data.powerUps[element][1]
            outRad = data.powerSize
            inOut = 0.382
            inRad = (outRad * inOut)
            allPoints = []
            for point in range(2 * 5):
                angleOfPoint = math.pi/2 - (2*math.pi)*(point/(5*2))
                # if point is even, use the outer radius 
                if (point % 2 == 0):
                    pointRad = outRad
                # if point is odd, use the inner radius
                if (point % 2 == 1):
                    pointRad = inRad
                pointX = centerX + (pointRad*math.cos(angleOfPoint))
                pointY = centerY - (pointRad*math.sin(angleOfPoint))
                allPoints += (pointX, pointY)
            canvas.create_polygon(allPoints, fill = "LightPink1", outline = "green2", width = 2)
    if (data.powerUp2 == True):
        # drawing star template taken from lab4
        for element in range(len(data.powerUps)):
            centerX = data.powerUps[element][0]
            centerY = data.powerUps[element][1]
            outRad = data.powerSize
            inOut = 0.382
            inRad = (outRad * inOut)
            allPoints = []
            for point in range(2 * 5):
                angleOfPoint = math.pi/2 - (2*math.pi)*(point/(5*2))
                # if point is even, use the outer radius 
                if (point % 2 == 0):
                    pointRad = outRad
                # if point is odd, use the inner radius
                if (point % 2 == 1):
                    pointRad = inRad
                pointX = centerX + (pointRad*math.cos(angleOfPoint))
                pointY = centerY - (pointRad*math.sin(angleOfPoint))
                allPoints += (pointX, pointY)
            canvas.create_polygon(allPoints, fill = "IndianRed1", outline = "CadetBlue1", width = 2)
    
# checks for collisions between player and symbols and power ups 
def collision(data):
    # for the symbols
    for element in range(len(data.symbols)):
        x = data.symbols[element][0]
        y = data.symbols[element][1]
        symbol = data.symbols[element][2] 
        # collision with enemy
        if (symbol == 0):
            if ((data.playX - 30 <= x + data.enemySize and data.playX + 50 >= x) and (data.playY <= y + data.enemySize and data.playY + 10 >= y)):
                data.pop = element
                data.score -= 5
                data.isPaused = True
                data.isEnemy = True 
                data.isFactOnScreen = True
                if (data.fact1 == True):
                    data.message = 0
                if (data.fact2 == True):
                    data.message = random.randint(0, 4)
                if (data.fact3 == True):
                    data.message = random.randint(0, 8)
                break
        # collision with piece 
        elif (symbol == 1):
            if ((data.playX <= x + data.pieceSize and data.playX + 50 >= x) and (data.playY <= y + data.pieceSize and data.playY + 6 >= y)):
                data.pop = element
                data.symbols.pop(element)
                data.score += 10
                break
    # for the power ups
    for item in range(len(data.powerUps)):
        x = data.powerUps[item][0]
        y = data.powerUps[item][1]
        if ((data.playX - 25 <= x + data.powerSize and data.playX + 25 >= x) and (data.playY - 1 <= y + data.powerSize and data.playY + 6 >= y)):
            data.powerUps.pop(item)
            data.score += 20
            data.isSpedUp = True
            data.t1 = data.time
            break
                
# pops up a fact screen every time the player hits a enemy symbol 
def factScreen(canvas, data):
    if (data.isEnemy == True):
        canvas.create_rectangle(data.width/6, data.height/6, data.width*5/6, data.height*5/6, fill = "lightSalmon2", outline = "OrangeRed4", width = 3)
        canvas.create_text(data.width/6 + 120, data.height/6 + 10, text = "Uh-Oh!", fill = "red3", anchor = "nw", font = "Courier 30 bold")
        canvas.create_text(data.width/6 + 10, data.height/6 + 50, text = "Cyber Fact:", fill = "brown", anchor = "nw", font = "Courier 20 bold")
        canvas.create_text(data.width/6 + 10, data.height/6 + 80, text = data.facts[data.message], fill = "black", anchor = "nw", font = "Courier 15 bold")
        canvas.create_text(data.width/6 + 22, data.height/6 + 310, text = "Press \'p\' to continue playing", fill = "brown", anchor = "nw", font = "Courier 16 bold")

# draws the text for when power ups are retrieved 
def isSpedUpText(canvas, data):
    canvas.create_text(data.width/2, data.height/4, text = "Power Up!", fill = "spring green", anchor = "center", font = "Courier 30 bold") 
        
def playUserGameMousePressed(event, data):
    pass
    
# moves player based on key pressed and splashes screens
def playUserGameKeyPressed(event, data):
    # splash screen to helpScreen mode
    if (event.keysym == "h"):
        data.mode = "helpScreen"
    # splash screen to customizationScreen mode
    if (event.keysym == "c"):
        data.mode = "customizationScreen"
    # pauses/unpauses the game
    elif (event.keysym == "p"):
        data.isPaused = not data.isPaused
        if (data.isFactOnScreen):
            data.isFactOnScreen = False
            data.symbols.pop(data.pop)
    # moves the player left and right if game is not paused 
    elif (not data.isPaused) and (event.keysym == "Left"):
        data.playSpeed = -10*data.speed
    elif (not data.isPaused) and (event.keysym == "Right"):
        data.playSpeed = 10*data.speed

# makes player stop when key is released
def playUserGameKeyReleased(event,data):
    if (event.keysym == "Left"):
        data.playSpeed = 0
    elif (event.keysym == "Right"):
        data.playSpeed = 0

# when timer starts, timeLeft decreases by 1 until it gets to 0
def playUserGameTimerFired(data):
    data.timerDelay = 50
    if (not data.isPaused):
        data.time += 1
        if (data.time % 20 == 0):
            data.timeLeft -= 1
        # if timeLeft becomes 0 (out of time) and splash screen to "endUserGame" 
        if (data.timeLeft <= 0):
            data.mode = "endUserGame"
        data.playX += data.playSpeed
        # adds new symbols and new power ups during a given increment of time
        if (data.time % 50 == 0):
            createSymbol(data)
        if (data.time % 100 == 0):
            createPowerUp(data)
        if (data.time % 2 == 0):
            for element in range(len(data.symbols)):
                # if symbol is a enemy symbol, follow the player
                # if player is to the right of the symbol, symbol moves down and right depending on distance between the        
                # player's x-coordinate and the symbol's x-coordinate (when symbol gets closer, it will slow down)
                if (data.playX >= data.symbols[element][0] and data.symbols[element][2] == 0):
                    data.symbols[element][1] += 10
                    # track the player based off player's coordinates and distance from enemy symbol
                    data.symbols[element][0] -= (data.symbols[element][0] - data.playX)/15
                # if player is to the left of the symbol, symbol moves down and left depending on distance between the        
                # player's x-coordinate and the symbol's x-coordinate (when symbol gets closer, it will slow down)
                elif (data.playX <= data.symbols[element][0] and data.symbols[element][2] == 0):
                    data.symbols[element][1] += 10
                    data.symbols[element][0] -= (data.symbols[element][0] - data.playX)/15
                data.symbols[element][1] += 10
            for item in range(len(data.powerUps)):
                data.powerUps[item][1] += 5
        # bounds for the movement for the player so the player does not move off screen
        if (data.playX <= 10):
            data.playSpeed = 0
            data.playX = 10
        if (data.playX >= data.width - 45):
            data.playSpeed = 0
            data.playX = data.width - 45
        collision(data)
        # for the power up to increase player speed when retrieved
        if (data.isSpedUp):
            if(data.time - data.t1 < 100):
                data.speed = 2
            else:
                data.speed = 1
                data.isSpedUp = False

# draws the background, players, symbols, power ups, time left, score, "h" for help, "c" to customize, "p" to pause/unpause, and power up message/fact screen/message (if applicable)
def playUserGameRedrawAll(canvas, data):
    drawGameBackground(canvas, data)
    drawTimeAndScore(canvas, data)
    drawPlayer(canvas,data)
    drawSymbols(canvas, data)
    drawPowerUp(canvas, data)
    # if power up is retrieved
    if (data.isSpedUp):
        isSpedUpText(canvas, data)
    # to displace fact if lock symbol is retrieved  
    if (data.isFactOnScreen):
        factScreen(canvas, data)

####################################
# endUserGame mode
####################################

# draws the win screen 
def drawWinScreen(canvas, data):
    canvas.create_rectangle(5, 5, data.width, data.height, fill = "black", outline = "yellow2", width = 15)
    canvas.create_text(data.width/2, data.height/4 - 40, text = "Congrats!", fill = "cyan", font = "Courier 60 bold")
    canvas.create_text(data.width/2, data.height/2 - 100, text = "The next object is the", fill = "green2", font = "Courier 25 bold")
    canvas.create_text(data.width/2, data.height/2 - 35, text = "CHAIR", fill = "firebrick2", font = "Courier 50 bold")
    canvas.create_polygon(120, 200, 95, 215, 120, 230, fill = "salmon1", outline = "DeepPink4", width = 2)
    canvas.create_polygon(380, 200, 405, 215, 380, 230, fill = "salmon1", outline = "DeepPink4", width = 2)
    canvas.create_text(data.width/2, data.height/2 + 20, text = "in", fill = "green2", font = "Courier 25 bold")
    canvas.create_text(data.width/2, data.height/2 + 75, text = "ROOM 1", fill = "orange", font = "Courier 50 bold")
    canvas.create_polygon(120, 310, 95, 325, 120, 340, fill = "salmon1", outline = "DeepPink4", width = 2)
    canvas.create_polygon(380, 310, 405, 325, 380, 340, fill = "salmon1", outline = "DeepPink4", width = 2)
    canvas.create_text(data.width/2, 2.9*data.height/4 + 50, text = "Exit this window to", fill = "magenta", font = "Courier 25 bold")
    canvas.create_text(data.width/2, 2.9*data.height/4 + 80, text = "return to rooms.", fill = "magenta", font = "Courier 25 bold")

# draws the first object
def drawObject1(canvas, data):
    canvas.create_rectangle(125, 180, 375, 235, fill = "black")
    canvas.create_text(data.width/2, data.height/2 - 35, text = "CHAIR", fill = "firebrick2", font = "Courier 50 bold")
    
# draws the second object
def drawObject2(canvas, data):
    canvas.create_rectangle(125, 180, 375, 235, fill = "black")
    canvas.create_text(data.width/2, data.height/2 - 35, text = "CLOTH", fill = "firebrick2", font = "Courier 50 bold")

# draws the third object
def drawObject3(canvas, data):
    canvas.create_rectangle(125, 180, 375, 235, fill = "black")
    canvas.create_text(data.width/2, data.height/2 - 35, text = "PAPER", fill = "firebrick2", font = "Courier 50 bold")
    
# draws the first room
def drawRoom1(canvas, data):
    canvas.create_rectangle(125, 290, 375, 345, fill = "black")
    canvas.create_text(data.width/2, data.height/2 + 75, text = "ROOM 1", fill = "orange", font = "Courier 50 bold")
    
# draws the second room
def drawRoom2(canvas, data):
    canvas.create_rectangle(125, 290, 375, 345, fill = "black")
    canvas.create_text(data.width/2, data.height/2 + 75, text = "ROOM 2", fill = "orange", font = "Courier 50 bold")

# draws the third room
def drawRoom3(canvas, data):
    canvas.create_rectangle(125, 290, 375, 345, fill = "black")
    canvas.create_text(data.width/2, data.height/2 + 75, text = "ROOM 3", fill = "orange", font = "Courier 50 bold")
    
def endUserGameMousePressed(event, data):
    # user's mouse x-coordinate and y-coordinate 
    userX = event.x
    userY = event.y
    # for objectArrow left arrow
    objectLeftArrowLeftX = 95
    objectLeftArrowRightX = 120
    objectLeftArrowTopY = 200
    objectLeftArrowBottomY = 230
    if (userX > objectLeftArrowLeftX and userX < objectLeftArrowRightX and userY > objectLeftArrowTopY and userY < objectLeftArrowBottomY):
        data.objectArrowPressed = True 
        # keeps track of the number of objectArrow clicks and depending on that number, changes the object
        data.numObjectArrowClicks += 1
        if (data.numObjectArrowClicks % 2 == 0 or data.numObjectArrowClicks % 2 == 1):
            data.object2 = True
            data.object1 = False
            data.object3 = False
        if (data.numObjectArrowClicks % 3 == 1): 
            data.object1 = True
            data.object2 = False
            data.object3 = False
        if (data.numObjectArrowClicks % 3 == 0): 
            data.object3 = True
            data.object1 = False
            data.object2 = False
    # for objectArrow right arrow
    nameRightArrowLeftX = 380
    nameRightArrowRightX = 405
    nameRightArrowTopY = 200
    nameRightArrowBottomY = 230
    if (userX > nameRightArrowLeftX and userX < nameRightArrowRightX and userY > nameRightArrowTopY and userY < nameRightArrowBottomY):
        data.objectArrowPressed = True 
        # keeps track of the number of objectArrow clicks and depending on that number, changes the object
        data.numObjectArrowClicks += 1
        if (data.numObjectArrowClicks % 2 == 0 or data.numObjectArrowClicks % 2 == 1):
            data.object2 = True
            data.object1 = False
            data.object3 = False
        if (data.numObjectArrowClicks % 3 == 1): 
            data.object1 = True
            data.object2 = False
            data.object3 = False
        if (data.numObjectArrowClicks % 3 == 0): 
            data.object3 = True
            data.object1 = False
            data.object2 = False
    # for roomArrow left arrow
    roomLeftArrowLeftX = 95
    roomLeftArrowRightX = 120
    roomLeftArrowTopY = 310
    roomLeftArrowBottomY = 340
    if (userX > roomLeftArrowLeftX and userX < roomLeftArrowRightX and userY > roomLeftArrowTopY and userY < roomLeftArrowBottomY):
        data.roomArrowPressed = True 
        # keeps track of the number of roomArrow clicks and depending on that number, changes the room
        data.numRoomArrowClicks += 1
        if (data.numRoomArrowClicks % 2 == 0 or data.numRoomArrowClicks % 2 == 1):
            data.room2 = True
            data.room1 = False
            data.room3 = False
        if (data.numRoomArrowClicks % 3 == 1): 
            data.room1 = True
            data.room2 = False
            data.room3 = False
        if (data.numRoomArrowClicks % 3 == 0): 
            data.room3 = True
            data.room1 = False
            data.room2 = False
    # for roomArrow right arrow
    roomRightArrowLeftX = 380
    roomRightArrowRightX = 405
    roomRightArrowTopY = 310
    roomRightArrowBottomY = 340
    if (userX > roomRightArrowLeftX and userX < roomRightArrowRightX and userY > roomRightArrowTopY and userY < roomRightArrowBottomY):
        data.roomArrowPressed = True 
        # keeps track of the number of roomArrow clicks and depending on that number, changes the room
        data.numRoomArrowClicks += 1
        if (data.numRoomArrowClicks % 2 == 0 or data.numRoomArrowClicks % 2 == 1):
            data.room2 = True
            data.room1 = False
            data.room3 = False
        if (data.numRoomArrowClicks % 3 == 1): 
            data.room1 = True
            data.room2 = False
            data.room3 = False
        if (data.numRoomArrowClicks % 3 == 0): 
            data.room3 = True
            data.room1 = False
            data.room2 = False

def endUserGameKeyPressed(event, data):
    pass
    
# to move the light symbol and lock symbol around
def endUserGameTimerFired(data):
    pass
    
# creates the winning screen and bouncing symbols 
def endUserGameRedrawAll(canvas, data):
    drawWinScreen(canvas, data)
    if (data.object1 == True):
        drawObject1(canvas, data)
    if (data.object2 == True):
        drawObject2(canvas, data)
    if (data.object3 == True):
        drawObject3(canvas, data)
    if (data.room1 == True):
        drawRoom1(canvas, data)
    if (data.room2 == True):
        drawRoom2(canvas, data)
    if (data.room3 == True):
        drawRoom3(canvas, data)
    
####################################
# restartUserGame mode
####################################

# draws the restart screen 
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

def restartUserGameMousePressed(event, data):
    userX = event.x
    userY = event.y
    # splash screen to startUserGame mode
    playAgainLeftX = data.width/2 - 75
    playAgainRightX = data.width/2 + 75
    playAgainTopY = data.height*3/4
    playAgainBottomY = data.height*3/4 + 50
    # restarts the game with init
    if (userX > playAgainLeftX and userX < playAgainRightX and userY > playAgainTopY and userY < playAgainBottomY):
        init(data)
    
def restartUserGameKeyPressed(event, data):
    pass
    
def restartUserGameTimerFired(data):
    pass

# draws the restart screen background and "play again" button 
def restartUserGameRedrawAll(canvas, data):
    drawRestartBackground(canvas, data)
    drawPlayAgainButton(canvas, data) 
    drawPlayAgainButtonText(canvas, data)

####################################
# runUserGame function 
# general run function template from 15-112 notes
####################################

def runUserGame(width = 300, height = 300):
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
        
    def keyReleasedWrapper(event, canvas, data):
        playUserGameKeyReleased(event, data)
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
    root.title("User Custom Puzzle/Game")
    if (data.gameName1 == True):
        root.title("Cyber Move")
    elif (data.gameName2 == True):
        root.title("Cyber Jump")
    elif (data.gameName3 == True):
        root.title("Cyber Lock")
    root.geometry("+{}+{}".format(0, 0))
    canvas = Canvas(root, width = data.width, height = data.height)
    data.canvas = canvas
    canvas.pack()
    # set up events
    root.bind("<Button-1>", lambda event:
                            mousePressedWrapper(event, canvas, data))
    root.bind("<KeyPress>", lambda event:
                            keyPressedWrapper(event, canvas, data))
    root.bind("<KeyRelease>", lambda event:
                            keyReleasedWrapper(event,canvas,data))
    timerFiredWrapper(canvas, data)
    # launch the app
    root.mainloop()

runUserGame(500, 500)