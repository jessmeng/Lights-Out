####################################
# Jessica Meng, jmeng1, Section B
# Lights Out
# 15-112 Term Project 
# cyberAttackMessage
# this is for the initial message that tells the user that they have been cyber attacked 
# tkinter "Text" box feature learned from: https://www.tutorialspoint.com/python/tk_text.htm (used this tutorial to write the code) 
# all colors used from: https://wiki.tcl.tk/37701
# root.geometry learned from: https://www.python-course.eu/tkinter_layout_management.php
####################################

####################################
# imports
# necessary to run program
####################################

from tkinter import *
import tkinter
import random

####################################
# functions
####################################

# this function creates the appearance that the message is typing out itself 
# this is the first function for the cyber attacker
def writeOut1(display, index, message):
   # base case 
   if (len(message) > 0):
      first = message[0]
      display.insert(index, first)
   # recursive case 
   if (len(message) > 1):
      # finds the index of the next character in the message, learned from: http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/text-index.html
      nextIndex = display.index("%s + 1 char" % index)
      # uses recursion to type out the next character in the message by slicing the message string
      speed = 80
      newMessage = message[1:]
      display.after(speed, writeOut1, display, nextIndex, newMessage)

# this function creates the "typewriter effect", where the message appears to be typing out itself 
# this is the second function for the instructions for the user 
def writeOut2(display, index, message):
   # base case 
   if (len(message) > 0):
      first = message[0]
      display.insert(index, first)
   # recursive case 
   if (len(message) > 1):
      # finds the index of the next character in the message, learned from: http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/text-index.html
      nextIndex = display.index("%s + 1 char" % index)
      # uses recursion to type out the next character in the message by slicing the message string
      speed = 80
      newMessage = message[1:]
      display.after(speed, writeOut2, display, nextIndex, newMessage)

root = Tk()
root.title("Cyber Attack Message")

# creates the "text" boxes that the messages will be typed out in
text1 = Text(root, width = 33, height = 10, bg = "black", fg = "chartreuse3", relief = SUNKEN, font = "Courier 25 bold")
text1.pack(fill = "both", expand = True)
text2 = Text(root, width = 33, height = 18, bg = "black", fg = "red", relief = SUNKEN, font = "Courier 25 bold")
text2.pack(fill = "both", expand = True)

# to choose a random symbol for the beginning of the cyber attack message
def randomSymbol():
   time = 60
   symbols = "¡™£¢∞§¶•ªºœ∑´®†¥¨ˆøπåß∂ƒ©˙∆˚¬Ω≈ç√∫˜µ"
   while time > 0:
      return random.choice(symbols)
      time -= 1

# calls both writeOut1 and writeOut2 in order to display the messages
writeOut1(text1, "2.0", "  " + randomSymbol() + "¢£™§ª•πºª¬¶§∞¢™øƒ˙˚©ç√ƒ∂˜∆ˆ†∂ \n  √ƒ∂˜•πºª¬¶§∞¢™∆˙˚ˆ†∂¢£™§øª©çƒ \n  •πºª£™§øª©¬¶§∞√ƒ∂˜¢π™∆˙˚ˆ†∂¢ç \n  ˙˚ˆ†∂√ƒ∂˜•π¢™∆¢£™§øª˜∫©ºª¬¶§∞ \n  ƒˆ†øª©ç£™§√¶∂˜•πºª˜∫¬∂¢∞µ¢™∆˙˚ \n  •π™§øª©çƒºª¬¶§√ƒ∂˜∞¢™∆˙˚ˆ†∂¢£ \n  ∫∂˚ˆ†∂¢£√ƒ∂˜•π∆™§øª©ºª¬©¶§∞¢™ \n  ™§øª©çƒ∂¢™∆˙˚˜ß•∞¨πºª√¬¶§ˆ∂¢† \n  ºª¬¶§∞√˜•π¢™∆¢£ƒ∂™§øª©çƒ˙˚ˆ†∂ \n  √∂™§øª©çƒ˜ºª¬¶§∞•¢£ƒ˙˚ˆ†∂π¢™∆")
writeOut2(text2, "2.0", "                    \n Hmm ... it seems like something \n is up with your computer.\n                            \n Maybe more than something ... \n You may be under cyber attack. \n            \n In today's digital age, \n         no one is safe. \n            \n           \n Can you escape ...?           \n Exit this window to start. \n \n Hint: start with the magnifying \n glass.")

####################################
# run function
# to run the writeOut functions
####################################

def runCyberAttackMessage():
   root.geometry("+{}+{}".format(805, 0))
   root.mainloop()
    
runCyberAttackMessage()