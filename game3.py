####################################
# Jessica Meng, jmeng1, Section B
# Lights Out
# 15-112 Term Project 
# game3
# this is the third game in the series of puzzles the user has to solve
# the game is called "Cyber Attack" and has 2 symbols, one good and one bad, that fall from random locations. The user has to catch the good symbols for points and avoid the bad symbols, which track the player's position. If the player hits a bad symbol, a random "Cyber Fact" will pop up to educate the user about cybersecurity. 
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
# facts from: https://heimdalsecurity.com/blog/10-surprising-cyber-security-facts-that-may-affect-your-online-safety/  
####################################

class Facts(object):
    facts = ['''The most expensive computer virus\nin the world and in cyber security\nhistory caused an estimated\nfinancial damage of $38.5 billion.\nThis virus was called MyDoom.''', '''Cyber attackers love social media\n(just as much as we do!),\nbecause users that spend a lot\nof time on social networks are\nvery likely to click links\nposted by their friends, which\nhackers use to their advantage.''', '''Oracle Java, Adobe Reader, or\nAdobe Flash is present on 99% of\ncomputers, which means that 99%\nof computer users are vulnerable\nto exploit kits (software\nvulnerabilities).''', '''Vulnerabilities that software often\npresent are extremely critical:\nall it takes is one click\non an infected advertising banner\nto give a hacker full access to\nyour computer.''', '''Psychological manipulation of\nvictims is also another way cyber\nattackers manipulate their targets.\nThey use social engineering, or the\ntricking of people into performing\nactions or divulging confidential\ninformation.''', '''Your government is actually making\nyou vulnerable. Governments around\nthe world are creating malware and\nusing it as digital weapons or\nin espionage programs.''', '''Hacktivism, or a subversive use of\ncomputers and computer networks\nto promote a political agenda,\naccounts for half of the cyber\nattacks launched in the world.''', '''The average time to detect a\nmalicious or criminal attack, as\nfounded by a global study\nsample of organizations, is 170\ndays.''']
    
####################################
# init
# to initialize needed variables
####################################

def init(data):
   # initial mode is "startGame3"
   data.mode = "startGame3"
   
   # for startGame3 and endGame3 mode 
   data.timerDelay = 100
   
   # for the light (good) symbol 
   data.lightX = 50
   data.lightY = 30
   data.lightSize = 25
   data.lightHeadRight, data.lightHeadDown = True, True
   
   # for lock (bad) symbol
   data.lockX = 450
   data.lockY = 20
   data.lockSize = 15
   data.lockHeadRight, data.lockHeadDown = True, True
   data.pop = None
   
   # for playGame3 mode 
   data.symbols = [] 
   data.powerUps = []
   
   # list of facts
   data.facts = Facts.facts 
   
   # for the score and timeLeft 
   data.score = 0
   data.timeLeft = 60
   
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
   data.isLockSymbol = False
   data.message = 0
    
####################################
# mode dispatcher
# learned from 15-112 notes
####################################

# goes to individual mode mousePressed functions
def mousePressed(event, data):
   if (data.mode == "startGame3"): 
      startGame3MousePressed(event, data)
   elif (data.mode == "playGame3"):   
      playGame3MousePressed(event, data)
   elif (data.mode == "instructionScreen"):   
      instructionScreenMousePressed(event, data)
   elif (data.mode == "winGame3"):   
      winGame3MousePressed(event, data)
   elif (data.mode == "restartGame3"):   
      restartGame3MousePressed(event, data)

# goes to individual mode keyPressed functions
def keyPressed(event, data):
   if (data.mode == "startGame3"): 
      startGame3KeyPressed(event, data)
   elif (data.mode == "playGame3"):
      playGame3KeyPressed(event, data)
   elif (data.mode == "instructionScreen"):   
      instructionScreenKeyPressed(event, data)
   elif (data.mode == "winGame3"):   
      winGame3KeyPressed(event, data)
   elif (data.mode == "restartGame3"):   
      restartGame3KeyPressed(event, data)

# goes to individual mode timerFired functions
def timerFired(data):
   if (data.mode == "startGame3"): 
      startGame3TimerFired(data)
   elif (data.mode == "playGame3"):   
      playGame3TimerFired(data)
   elif (data.mode == "instructionScreen"):   
      instructionScreenTimerFired(data)
   elif (data.mode == "winGame3"):   
      winGame3TimerFired(data)
   elif (data.mode == "restartGame3"):   
      restartGame3TimerFired(data)

# goes to individual mode redrawAll functions
def redrawAll(canvas, data):
   if (data.mode == "startGame3"): 
      startGame3RedrawAll(canvas, data)
   elif (data.mode == "playGame3"):   
      playGame3RedrawAll(canvas, data)
   elif (data.mode == "instructionScreen"):   
      instructionScreenRedrawAll(canvas, data)
   elif (data.mode == "winGame3"):   
      winGame3RedrawAll(canvas, data)
   elif (data.mode == "restartGame3"):   
      restartGame3RedrawAll(canvas, data)

####################################
# startGame3 mode
####################################

# draws the starting board
def drawStart(canvas, data):
   canvas.create_rectangle(5, 5, data.width, data.height, fill = "black", outline = "yellow2", width = 15)
   canvas.create_text(data.width/2, data.height/3, text = "CYBER", fill = "lawn green", font = "Courier 70 bold")
   canvas.create_text(data.width/2, data.height/2.2, text = "ATTACK", fill = "cyan", font = "Georgia 75 bold")
   canvas.create_text(data.width/2, data.height*2.7/4, text = "Press \'i\' for instructions!", fill = "magenta", font = "Courier 25 bold")
   canvas.create_text(data.width/2, data.height*3/4, text = "Press \'p\' to play!", fill = "firebrick1", font = "Courier 25 bold")

# draws the bouncing light symbol in the beginning
def drawLight(canvas, data):
   canvas.create_polygon(data.lightX, data.lightY, data.lightX + data.lightSize, data.lightY + data.lightSize, data.lightX, data.lightY - data.lightSize, data.lightX + data.lightSize, data.lightY, fill = "yellow2", outline = "khaki2", width = 2)
    
# draws the bouncing lock symbol in the beginning
def drawLock(canvas,data):
   canvas.create_rectangle(data.lockX, data.lockY, data.lockX + 2*data.lockSize, data.lockY + 2*data.lockSize, fill = "thistle3", outline = "white", width = 2)
   canvas.create_oval(data.lockX + data.lockSize/2, data.lockY + data.lockSize/2, data.lockX + 1.4*data.lockSize, data.lockY + 1.4*data.lockSize, fill = "gray9", width = 0)

# move functions for animating the light symbol; symbol moves random amount
def moveLightLeft(data):
   data.lightX -= random.randint(1, 10)
    
def moveLightRight(data):
   data.lightX += random.randint(1, 10)
    
def moveLightUp(data):
   data.lightY -= random.randint(1, 10)
    
def moveLightDown(data):
   data.lightY += random.randint(1, 10)
    
# move functions for animating the lock symbol; symbol moves random amount 
def moveLockLeft(data):
   data.lockX -= random.randint(1, 10)
    
def moveLockRight(data):
   data.lockX += random.randint(1, 10)
   
def moveLockUp(data):
   data.lockY -= random.randint(1, 10)
   
def moveLockDown(data):
   data.lockY += random.randint(1, 10)

# moves the light symbol, allows it to bounce around
def moveLight(data):
   if (data.lightHeadRight == True):
      if (data.width - 40 <= data.lightX + data.lightSize):
         data.lightHeadRight = False
      moveLightRight(data)
   else:
      if (data.lightX <= 40):
         data.lightHeadRight = True
      moveLightLeft(data)
   if (data.lightHeadDown == True):
      if (data.height - 40 <= data.lightY + data.lightSize):
         data.lightHeadDown = False
      moveLightDown(data)
   else:
      if (data.lightY <= 40):
         data.lightHeadDown = True
      moveLightUp(data)
        
# moves the lock symbol, allows it to bounce around
def moveLock(data):
   if (data.lockHeadRight == True):
      if (data.width - 40 <= data.lockX + data.lockSize):
         data.lockHeadRight = False
      moveLockRight(data)
   else:
      if (data.lockX <= 40):
         data.lockHeadRight = True
      moveLockLeft(data)
   if (data.lockHeadDown == True):
      if (data.height - 40 <= data.lockY + data.lockSize):
         data.lockHeadDown = False
      moveLockDown(data)
   else:
      if (data.lockY <= 40):
         data.lockHeadDown = True
      moveLockUp(data)

def startGame3MousePressed(event, data):
   pass

# game goes to instructionScreen mode or playGame3 mode
def startGame3KeyPressed(event, data):
   # splash screen to instructionScreen mode
   if (event.keysym == "i"):
      data.mode = "instructionScreen"
   # splash screen to playGame3 mode
   elif (event.keysym == "p"):
      data.mode = "playGame3"

# moves the light symbol and lock symbol around 
def startGame3TimerFired(data):
   moveLight(data)
   moveLock(data)

# draws the starting screen, moving light symbol, and moving lock symbol 
def startGame3RedrawAll(canvas, data):
   drawStart(canvas, data)
   drawLight(canvas, data)
   drawLock(canvas, data)
    
####################################
# instructionScreen mode
####################################

# draws the instruction screen
def drawInstructions(canvas, data):
   canvas.create_rectangle(5, 5, data.width, data.height, fill = "black", outline = "yellow2", width = 15)
   canvas.create_text(data.width/2, data.height/6 - 20, text = "Instructions:", fill = "turquoise1", font = "Georgia 45 bold")
   canvas.create_text(data.width/2, data.height/6 + 17, text = "Use left and right arrow keys to move player", fill = "hot pink", font = "Courier 16 bold")
   # for the light symbol and instructions
   lightX = 80
   lightY = 160
   canvas.create_polygon(lightX, lightY, lightX + data.lightSize, lightY + data.lightSize, lightX, lightY - data.lightSize, lightX + data.lightSize, lightY, fill = "yellow2", outline = "khaki2", width = 2)
   canvas.create_text(data.width/2 + 40, data.height/3 - 7, text = "Lightning Symbol (Retrieve)", fill = "white", font = "Courier 18 bold")
   canvas.create_text(data.width/2 + 30, data.height/3 + 20, text = "+10 points", fill = "goldenrod1", font = "Courier 20 bold")
   # draws the lock symbol and instructions 
   lockX = 80
   lockY = 250
   canvas.create_rectangle(lockX, lockY, lockX + 2*data.lockSize, lockY + 2*data.lockSize, fill = "thistle3", outline = "white", width = 2)
   canvas.create_oval(lockX + data.lockSize/2, lockY + data.lockSize/2, lockX + 1.4*data.lockSize, lockY + 1.4*data.lockSize, fill = "gray9", width = 0)
   canvas.create_text(data.width/2 + 30, data.height/3 + 85, text = "Lock Symbol (Avoid)", fill = "white", font = "Courier 18 bold")
   canvas.create_text(data.width/2 + 25, data.height/3 + 108, text = "-5 points", fill = "firebrick1", font = "Courier 20 bold")
   # draws a star for the power up (template taken from lab4) 
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
      pointX = 95 + (pointRad*math.cos(angleOfPoint))
      pointY = 350 - (pointRad*math.sin(angleOfPoint))
      allPoints += (pointX, pointY)
   canvas.create_polygon(allPoints, fill = "LightPink1", outline = "green2", width = 2)
   canvas.create_text(data.width/2 + 30, data.height/3 + 175, text = "Power Up!", fill = "white", font = "Courier 20 bold")
   canvas.create_text(data.width/2 + 40, data.height/3 + 198, text = "2x speed for 5 seconds (+20 points)", fill = "magenta", font = "Courier 15 bold")
   # for going back to startGame3 or playGame3
   canvas.create_text(data.width/2, data.height*3.75/5 + 50, text = "Press \'s\' to go back to the Start Screen", fill = "LightBlue1", font = "Courier 18 bold")
   canvas.create_text(data.width/2, data.height*4.1/5 + 45, text = "Press \'r\' to start/resume play", fill = "Cadet Blue", font = "Courier 20 bold")
    
def instructionScreenMousePressed(event, data):
   pass

# game goes back to startGame3 mode or to playGame3 mode
def instructionScreenKeyPressed(event, data):
   # splash screen to startGame3 mode
   if (event.keysym == "s"):
      data.mode = "startGame3"
   # splash screen to playGame3 mode
   elif (event.keysym == "r"):
      data.mode = "playGame3"

def instructionScreenTimerFired(data):
   pass 
    
# draws the instruction screen 
def instructionScreenRedrawAll(canvas, data):
   drawInstructions(canvas, data)
    
####################################
# playGame3 mode
####################################

# draws the game background
def drawGameBackground(canvas, data):
   canvas.create_rectangle(0, 0, data.width, data.height, fill = "midnight blue")
   # for the binary in the background (1s and 0s)
   for first in range(30, 481, 90): 
      canvas.create_text(250, first, text = "1 0 1 0 1 0 1 0 1 0 1 0 1 0", fill = "blue", font = "Courier 30")
   for second in range(60, 481, 90): 
      canvas.create_text(250, second, text = "1 0 1 0 1 0 1 0 1 0 1 0 1 0", fill = "royal blue", font = "Courier 30")
   for last in range(90, 481, 90): 
      canvas.create_text(250, last, text = "1 0 1 0 1 0 1 0 1 0 1 0 1 0", fill = "slategray", font = "Courier 30")
   canvas.create_rectangle(0, 470, data.width, data.height, fill = "blue4", width = 0)

# draws the time left, score, "h" for help, and "p" to pause/unpause displayed during the game 
def drawMenu(canvas, data):
   timeLeft = "Time Left: " + str(data.timeLeft)
   canvas.create_text(100, data.height/16, text = timeLeft, fill = "orange", font = "Courier 20 bold")
   score = "Score: " + str(data.score)
   canvas.create_text(75, data.height/9, text = score, fill = "yellow2", font = "Courier 20 bold")
   canvas.create_text(data.width*3.75/5, data.height/16, text = "Press \'h\' for help", fill = "white", font = "Courier 16 bold")
   canvas.create_text(data.width*3.4/5, data.height/9, text = "Press \'p\' to pause/unpause", fill = "white", font = "Courier 16 bold")

# draws the player    
def drawPlayer(canvas,data):
   canvas.create_rectangle(data.playX, data.playY, data.playX + data.playSize, data.playY + data.playSize + 10, fill = "light blue", outline = "maroon", width = 3)

# creates a new symbol (either light or lock) and adds to list data.symbols
def createSymbol(data):
   # each symbol has an x-coordinate, y-coordinate, and is either a good or bad symbol (1 or 0)
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
      # if symbol is 0 (bad), then draw the lock symbol
      if (symbol == 0):
         canvas.create_rectangle(x, y, x + 2*data.lockSize, y + 2*data.lockSize, fill = "thistle3", outline = "white", width = 2)
         canvas.create_oval(x + data.lockSize/2, y + data.lockSize/2, x + 1.4*data.lockSize, y + 1.4*data.lockSize, fill = "gray9", width = 0)
      # if symbol is 1 (good), then draw the light symbol
      elif (symbol == 1):
         canvas.create_polygon(x, y, x + data.lightSize, y + data.lightSize, x, y - data.lightSize, x + data.lightSize, y, fill = "yellow2", outline = "khaki2", width = 2)
            
# creates new power up to list data.powerUps
def createPowerUp(data):
   x = random.randint(50, 450)
   y = 0
   data.powerUps.append([x, y])  
    
# draws the power up (star) 
def drawPowerUp(canvas, data):
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
    
# checks for collisions between player and symbols and power ups 
def collision(data):
   # for the symbols
   for element in range(len(data.symbols)):
      x = data.symbols[element][0]
      y = data.symbols[element][1]
      symbol = data.symbols[element][2] 
      # collision with lock symbol
      if (symbol == 0):
         if ((data.playX - 30 <= x + data.lockSize and data.playX + 50 >= x) and (data.playY <= y + data.lockSize and data.playY + 10 >= y)):
               data.pop = element
               data.score -= 5
               data.isPaused = True
               data.isLockSymbol = True 
               data.isFactOnScreen = True
               data.message = random.randint(0, 7)
               break
      # collision with light symbol 
      elif (symbol == 1):
         if ((data.playX - 25 <= x + data.lightSize and data.playX + 20 >= x) and (data.playY - 1 <= y + data.lightSize and data.playY + 6 >= y)):
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
                
# pops up a fact screen every time the player hits a lock symbol 
def factScreen(canvas, data):
   if (data.isLockSymbol == True):
      canvas.create_rectangle(data.width/6, data.height/6, data.width*5/6, data.height*5/6, fill = "lightSalmon2", outline = "OrangeRed4", width = 3)
      canvas.create_text(data.width/6 + 120, data.height/6 + 10, text = "Uh-Oh!", fill = "red3", anchor = "nw", font = "Courier 30 bold")
      canvas.create_text(data.width/6 + 10, data.height/6 + 50, text = "Cyber Fact:", fill = "brown", anchor = "nw", font = "Courier 20 bold")
      canvas.create_text(data.width/6 + 10, data.height/6 + 80, text = data.facts[data.message], fill = "black", anchor = "nw", font = "Courier 15 bold")
      canvas.create_text(data.width/6 + 22, data.height/6 + 310, text = "Press \'p\' to continue playing", fill = "brown", anchor = "nw", font = "Courier 16 bold")

# draws the text for when power ups are retrieved 
def isSpedUpText(canvas, data):
   canvas.create_text(data.width/2, data.height/4, text = "Power Up!", fill = "spring green", anchor = "center", font = "Courier 30 bold") 
        
def playGame3MousePressed(event, data):
   pass
    
# moves player based on key pressed and splashes screens
def playGame3KeyPressed(event, data):
   # splash screen to instructionScreen mode
   if (event.keysym == "h"):
      data.mode = "instructionScreen"
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
def playGame3KeyReleased(event,data):
   if (event.keysym == "Left"):
      data.playSpeed = 0
   elif (event.keysym == "Right"):
      data.playSpeed = 0

# when timer starts, timeLeft decreases by 1 until it gets to 0
def playGame3TimerFired(data):
   data.timerDelay = 50
   if (not data.isPaused):
      data.time += 1
      if (data.time % 20 == 0):
         data.timeLeft -= 1
      # if the player reaches score of 60 or more, they win and receives the next object
      # if timeLeft becomes 0 (out of time) and the player's score is less than 60, the player must play again 
      if (data.timeLeft == -1 and data.score < 60):
         data.mode = "restartGame3"
      if (data.score >= 60 and data.timeLeft != 0):
         data.mode = "winGame3"
      data.playX += data.playSpeed
      # adds new symbols and new power ups every increment of time
      if (data.time % 50 == 0):
         createSymbol(data)
      if (data.time % 100 == 0):
         createPowerUp(data)
      if (data.time % 2 == 0):
         for element in range(len(data.symbols)):
               # if symbol is a lock symbol, follow the player
               # if player is to the right of the symbol, symbol moves down and right depending on distance between the        
               # player's x-coordinate and the symbol's x-coordinate (when symbol gets closer, it will slow down)
               if (data.playX >= data.symbols[element][0] and data.symbols[element][2] == 0):
                  data.symbols[element][1] += 10
                  # track the player based off player's coordinates and distance from lock (bad) symbol
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

# draws the background, players, symbols, power ups, time left, score, "h" for help, "p" to pause/unpause, and power up message/fact screen/message (if applicable)
def playGame3RedrawAll(canvas, data):
   drawGameBackground(canvas, data)
   drawMenu(canvas, data)
   drawPlayer(canvas,data)
   drawSymbols(canvas, data)
   drawPowerUp(canvas, data)
   # if power up is retrieved
   if (data.isSpedUp):
      isSpedUpText(canvas, data)
   # to display fact if lock symbol is retrieved  
   if (data.isFactOnScreen):
      factScreen(canvas, data)

####################################
# winGame3 mode
####################################

# draws the win screen 
def drawWinScreen(canvas, data):
   canvas.create_rectangle(5, 5, data.width, data.height, fill = "black", outline = "yellow2", width = 15)
   canvas.create_text(data.width/2, data.height/3, text = "Congrats!", fill = "cyan", font = "Courier 60 bold")
   canvas.create_text(data.width/2, data.height/2 - 10, text = "The next object is", fill = "green2", font = "Courier 25 bold")
   canvas.create_text(data.width/2, data.height/2 + 30, text = "the PAINTING in room 1.", fill = "green2", font = "Courier 30 bold")
   canvas.create_text(data.width/2, 2.9*data.height/4, text = "Exit this window and press", fill = "magenta", font = "Courier 25 bold")
   canvas.create_text(data.width/2, 2.9*data.height/4 + 30, text = "\'1\' to return to rooms.", fill = "magenta", font = "Courier 25 bold")
    
# draws the bouncing light symbol in the end
def drawLight(canvas, data):
   canvas.create_polygon(data.lightX, data.lightY, data.lightX + data.lightSize, data.lightY + data.lightSize, data.lightX, data.lightY - data.lightSize, data.lightX + data.lightSize, data.lightY, fill = "yellow2", outline = "khaki2", width = 2)
    
# draws the bouncing lock symbol in the end
def drawLock(canvas,data):
   canvas.create_rectangle(data.lockX, data.lockY, data.lockX + 2*data.lockSize, data.lockY + 2*data.lockSize, fill = "thistle3", outline = "white", width = 2)
   canvas.create_oval(data.lockX + data.lockSize/2, data.lockY + data.lockSize/2, data.lockX + 1.4*data.lockSize, data.lockY + 1.4*data.lockSize, fill = "gray9", width = 0)

# move functions for animating the light symbol; symbol moves random amount
def moveLightLeft(data):
   data.lightX -= random.randint(1, 10)
   
def moveLightRight(data):
   data.lightX += random.randint(1, 10)
   
def moveLightUp(data):
   data.lightY -= random.randint(1, 10)
   
def moveLightDown(data):
   data.lightY += random.randint(1, 10)
    
# move functions for animating the lock symbol; symbol moves random amount
def moveLockLeft(data):
   data.lockX -= random.randint(1, 10)
   
def moveLockRight(data):
   data.lockX += random.randint(1, 10)
   
def moveLockUp(data):
   data.lockY -= random.randint(1, 10)
   
def moveLockDown(data):
   data.lockY += random.randint(1, 10)

# moves the light symbol, allows it to bounce around
def moveLight(data):
   data.timerDelay = 100
   if (data.lightHeadRight == True):
      if (data.width - 40 <= data.lightX + data.lightSize):
         data.lightHeadRight = False
      moveLightRight(data)
   else:
      if (data.lightX <= 40):
         data.lightHeadRight = True
      moveLightLeft(data)
   if (data.lightHeadDown == True):
      if (data.height - 40 <= data.lightY + data.lightSize):
         data.lightHeadDown = False
      moveLightDown(data)
   else:
      if (data.lightY <= 40):
         data.lightHeadDown = True
      moveLightUp(data)
        
# moves the lock symbol, allows it to bounce around
def moveLock(data):
   data.timerDelay = 100
   if (data.lockHeadRight == True):
      if (data.width - 40 <= data.lockX + data.lockSize):
         data.lockHeadRight = False
      moveLockRight(data)
   else:
      if (data.lockX <= 40):
         data.lockHeadRight = True
      moveLockLeft(data)
   if (data.lockHeadDown == True):
      if (data.height - 40 <= data.lockY + data.lockSize):
         data.lockHeadDown = False
      moveLockDown(data)
   else:
      if (data.lockY <= 40):
         data.lockHeadDown = True
      moveLockUp(data)
        
def winGame3MousePressed(event, data):
   pass

def winGame3KeyPressed(event, data):
   pass
    
# to move the light symbol and lock symbol around
def winGame3TimerFired(data):
   moveLight(data)
   moveLock(data)
   
# draws the winning screen and bouncing symbols 
def winGame3RedrawAll(canvas, data):
   drawWinScreen(canvas, data)
   drawLight(canvas, data)
   drawLock(canvas, data)
    
####################################
# restartGame3 mode
####################################

# draws the restart screen to tell user to restart the game
def drawRestartScreen(canvas, data):
   canvas.create_rectangle(5, 5, data.width, data.height, fill = "black", outline = "yellow2", width = 15)
   canvas.create_text(data.width/2, data.height/3, text = "Times Out!", fill = "cyan", font = "Courier 60 bold")
   canvas.create_text(data.width/2, data.height/2, text = "Looks like you didn't", fill = "lawn green", font = "Courier 23 bold")
   canvas.create_text(data.width/2, data.height/2 + 30, text = "complete the puzzle in time.", fill = "lawn green", font = "Courier 22 bold")
   canvas.create_text(data.width/2, 2.3*data.height/3, text = "Press \'r\' to restart and try again!", fill = "DeepPink2", font = "Courier 18 bold")
    
# draws the bouncing light symbol in the end
def drawLight(canvas, data):
   canvas.create_polygon(data.lightX, data.lightY, data.lightX + data.lightSize, data.lightY + data.lightSize, data.lightX, data.lightY - data.lightSize, data.lightX + data.lightSize, data.lightY, fill = "yellow2", outline = "khaki2", width = 2)
    
# draws the bouncing lock symbol in the end
def drawLock(canvas,data):
   canvas.create_rectangle(data.lockX, data.lockY, data.lockX + 2*data.lockSize, data.lockY + 2*data.lockSize, fill = "thistle3", outline = "white", width = 2)
   canvas.create_oval(data.lockX + data.lockSize/2, data.lockY + data.lockSize/2, data.lockX + 1.4*data.lockSize, data.lockY + 1.4*data.lockSize, fill = "gray9", width = 0)

# move functions for animating the light symbol; symbol moves random amount
def moveLightLeft(data):
   data.lightX -= random.randint(1, 10)
   
def moveLightRight(data):
   data.lightX += random.randint(1, 10)
   
def moveLightUp(data):
   data.lightY -= random.randint(1, 10)
   
def moveLightDown(data):
   data.lightY += random.randint(1, 10)
   
# move functions for animating the lock symbol; symbol moves random amount
def moveLockLeft(data):
   data.lockX -= random.randint(1, 10)
   
def moveLockRight(data):
   data.lockX += random.randint(1, 10)
   
def moveLockUp(data):
   data.lockY -= random.randint(1, 10)
   
def moveLockDown(data):
   data.lockY += random.randint(1, 10)

# moves the light symbol, allows it to bounce around
def moveLight(data):
   data.timerDelay = 100
   if (data.lightHeadRight == True):
      if (data.width - 40 <= data.lightX + data.lightSize):
         data.lightHeadRight = False
      moveLightRight(data)
   else:
      if (data.lightX <= 40):
         data.lightHeadRight = True
      moveLightLeft(data)
   if (data.lightHeadDown == True):
      if (data.height - 40 <= data.lightY + data.lightSize):
         data.lightHeadDown = False
      moveLightDown(data)
   else:
      if (data.lightY <= 40):
         data.lightHeadDown = True
      moveLightUp(data)
        
# moves the lock symbol, allows it to bounce around
def moveLock(data):
   data.timerDelay = 100
   if (data.lockHeadRight == True):
      if (data.width - 40 <= data.lockX + data.lockSize):
         data.lockHeadRight = False
      moveLockRight(data)
   else:
      if (data.lockX <= 40):
         data.lockHeadRight = True
      moveLockLeft(data)
   if (data.lockHeadDown == True):
      if (data.height - 40 <= data.lockY + data.lockSize):
         data.lockHeadDown = False
      moveLockDown(data)
   else:
      if (data.lockY <= 40):
         data.lockHeadDown = True
      moveLockUp(data)
        
def restartGame3MousePressed(event, data):
   pass

def restartGame3KeyPressed(event, data):
   # sets everything back to init function (beginning) 
   if (event.keysym == "r"):
      init(data)
   
# to move the light symbol and lock symbol around
def restartGame3TimerFired(data):
   moveLight(data)
   moveLock(data)
   
# draws the restart screen and bouncing symbols 
def restartGame3RedrawAll(canvas, data):
   drawRestartScreen(canvas, data)
   drawLight(canvas, data)
   drawLock(canvas, data)

####################################
# runGame3 function 
# general run function template from 15-112 notes
####################################

def runGame3(width = 300, height = 300):
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
      playGame3KeyReleased(event, data)
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
   root.title("Cyber Attack")
   root.geometry("+{}+{}".format(805, 0))
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

runGame3(500, 500)