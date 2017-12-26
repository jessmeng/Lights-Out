####################################
# Jessica Meng, jmeng1, Section B
# Lights Out
# 15-112 Term Project 
# main
# all visuals were created and designed using Adobe Illustrator
# visuals were created and designed by Jessica Meng with basic templates courtesy of Google Images
# tkinter "PhotoImage" feature learned from: http://effbot.org/tkinterbook/photoimage.htm, https://www.python-course.eu/tkinter_canvas.php
# this is the main file for the start screen and the rooms 
####################################

####################################
# imports
# necessary to run program
####################################

from tkinter import *
import tkinter
import math
import random

####################################
# main part of the project; runs all the other .py files
####################################
 
# to initialize the needed variables 
def init(canvas):
    # tkinter "PhotoImage" feature learned from: http://effbot.org/tkinterbook/photoimage.htm, https://www.python-course.eu/tkinter_canvas.php
    image = PhotoImage(file = "assets/introPartOne.gif")
    canvas.data["image"] = image
    canvas.data["started"] = False
    # there are total of 10 objects
    # all the objects "clicked" start off as False, because they have not been clicked
    canvas.data["magnifyingGlassClicked"] = False
    canvas.data["vaseClicked"] = False
    canvas.data["keyClicked"] = False
    canvas.data["clothClicked"] = False
    canvas.data["hatClicked"] = False
    canvas.data["symbols2Clicked"] = False
    canvas.data["paintingClicked"] = False
    canvas.data["frameClicked"] = False
    canvas.data["symbols1Clicked"] = False
    canvas.data["drawerClicked"] = False
    
# for when the objects are clicked
def mousePressed(event):
    # canvas = event.widget.canvas from 15-112 notes
    canvas = event.widget.canvas
    # user's mouse x-coordinate and y-coordinate 
    userX = event.x
    userY = event.y
    # for the starting introduction screen to display the cyber attack message
    if (event.x < 800 and event.y < 600 and canvas.data["started"] == False):
        canvas.data["image"] = PhotoImage(file = "assets/room1.gif")
        redrawAll(canvas)
        canvas.data["started"] = True
        import cyberAttackMessage
        redrawAll(canvas)
    elif (userX >= 25 and userY >= 550 and userX <= 99 and userY <= 584):
        canvas.data["image"] = PhotoImage(file = "assets/helpScreen.gif")
        redrawAll(canvas)
    elif (userX >= 239 and userY >= 352 and userX <= 291 and userY <= 383 and canvas.data["magnifyingGlassClicked"] == False):
        canvas.data["image"] = PhotoImage(file = "assets/magnifyingGlass.gif")
        redrawAll(canvas)
    elif (userX >= 70 and userY >= 369 and userX <= 161 and userY <= 523 and canvas.data["vaseClicked"] == False and canvas.data["magnifyingGlassClicked"] == True):
        canvas.data["image"] = PhotoImage(file = "assets/vase.gif")
        redrawAll(canvas)
    elif (userX >= 130 and userY >= 386 and userX <= 170 and userY <= 418 and canvas.data["keyClicked"] == False and canvas.data["vaseClicked"] == True):
        canvas.data["image"] = PhotoImage(file = "assets/key.gif")
        redrawAll(canvas)
    elif (userX >= 362 and userY >= 527 and userX <= 493 and userY <= 570 and canvas.data["clothClicked"] == False and canvas.data["keyClicked"] == True):
        canvas.data["image"] = PhotoImage(file = "assets/cloth.gif")
        redrawAll(canvas)
    elif (userX >= 80 and userY >= 191 and userX <= 145 and userY <= 240 and canvas.data["hatClicked"] == False):
        canvas.data["image"] = PhotoImage(file = "assets/hat.gif")
        redrawAll(canvas)
    elif (userX >= 51 and userY >= 173 and userX <= 130 and userY <= 221 and canvas.data["symbols2Clicked"] == False and canvas.data["hatClicked"] == True):
        canvas.data["image"] = PhotoImage(file = "assets/symbols2.gif")
        redrawAll(canvas)
    elif (userX >= 577 and userY >= 422 and userX <= 726 and userY <= 528 and canvas.data["paintingClicked"] == False and canvas.data["symbols2Clicked"] == True):
        canvas.data["image"] = PhotoImage(file = "assets/painting.gif")
        redrawAll(canvas)
    elif (userX >= 534 and userY >= 152 and userX <= 675 and userY <= 307 and canvas.data["frameClicked"] == False and canvas.data["paintingClicked"] == True):
        canvas.data["image"] = PhotoImage(file = "assets/frame.gif")
        redrawAll(canvas)
    elif (userX >= 595 and userY >= 235 and userX <= 689 and userY <= 282 and canvas.data["symbols1Clicked"] == False and canvas.data["frameClicked"] == True):
        canvas.data["image"] = PhotoImage(file = "assets/symbols1.gif")
        redrawAll(canvas)
    elif (userX >= 323 and userY >= 274 and userX <= 400 and userY <= 311 and canvas.data["drawerClicked"] == False and canvas.data["symbols1Clicked"] == True):
        canvas.data["image"] = PhotoImage(file = "assets/drawer.gif")
        redrawAll(canvas)

# for when a key is pressed
def keyPressed(event):
    # canvas = event.widget.canvas from 15-112 notes
    canvas = event.widget.canvas
    # the "1", "2", "3" keys control which room the user is in
    if (event.keysym == "1"):
        canvas.data["image"] = PhotoImage(file = "assets/room1.gif")
        redrawAll(canvas)
    elif (event.keysym == "2"):
        canvas.data["image"] = PhotoImage(file = "assets/room2.gif")
        redrawAll(canvas)
    elif (event.keysym == "3"):
        canvas.data["image"] = PhotoImage(file = "assets/room3.gif")
        redrawAll(canvas)
    # the user must press keys to start the puzzle for each respective object
    elif (event.keysym == "a" and canvas.data["magnifyingGlassClicked"] == False):
        canvas.data["magnifyingGlassClicked"] = True
        import game1
        redrawAll(canvas)
    elif (event.keysym == "j" and canvas.data["vaseClicked"] == False):
        canvas.data["vaseClicked"] = True
        import password1
        redrawAll(canvas)
    elif (event.keysym == "b" and canvas.data["keyClicked"] == False):
        canvas.data["keyClicked"] = True
        import draw1
        redrawAll(canvas)
    elif (event.keysym == "n" and canvas.data["clothClicked"] == False):
        import game2
        redrawAll(canvas)
    elif (event.keysym == "e" and canvas.data["hatClicked"] == False):
        canvas.data["hatClicked"] = True
        import password2
        redrawAll(canvas)
    elif (event.keysym == "o" and canvas.data["symbols2Clicked"] == False):
        canvas.data["symbols2Clicked"] = True
        import game3
        redrawAll(canvas)
    elif (event.keysym == "i" and canvas.data["paintingClicked"] == False):
        canvas.data["paintingClicked"] = True
        import password3
        redrawAll(canvas)
    elif (event.keysym == "q" and canvas.data["frameClicked"] == False):
        canvas.data["frameClicked"] = True
        import game4
        redrawAll(canvas)
    elif (event.keysym == "c" and canvas.data["symbols1Clicked"] == False):
        canvas.data["symbols1Clicked"] = True
        import password4
        redrawAll(canvas)
 
# for when a key is released
def keyReleased(event):
    # canvas = event.widget.canvas from 15-112 notes
    canvas = event.widget.canvas
    # the "1", "2", "3" keys control which room the user is in
    if (event.keysym == "1"):
        canvas.data["image"] = PhotoImage(file = "assets/room1.gif")
        redrawAll(canvas)
    elif (event.keysym == "2"):
        canvas.data["image"] = PhotoImage(file = "assets/room2.gif")
        redrawAll(canvas)
    elif (event.keysym == "3"):
        canvas.data["image"] = PhotoImage(file = "assets/room3.gif")
        redrawAll(canvas)
    # the user must press keys to start the puzzle for each respective object
    elif (event.keysym == "a" and canvas.data["magnifyingGlassClicked"] == False):
        canvas.data["magnifyingGlassClicked"] = True
        import game1
        redrawAll(canvas)
    elif (event.keysym == "j" and canvas.data["vaseClicked"] == False):
        canvas.data["vaseClicked"] = True
        import password1
        redrawAll(canvas)
    elif (event.keysym == "b" and canvas.data["keyClicked"] == False):
        canvas.data["keyClicked"] = True
        import draw1
        redrawAll(canvas)
    elif (event.keysym == "n" and canvas.data["clothClicked"] == False):
        import game2
        redrawAll(canvas)
    elif (event.keysym == "e" and canvas.data["hatClicked"] == False):
        canvas.data["hatClicked"] = True
        import password2
        redrawAll(canvas)
    elif (event.keysym == "o" and canvas.data["symbols2Clicked"] == False):
        canvas.data["symbols2Clicked"] = True
        import game3
        redrawAll(canvas)
    elif (event.keysym == "i" and canvas.data["paintingClicked"] == False):
        canvas.data["paintingClicked"] = True
        import password3
        redrawAll(canvas)
    elif (event.keysym == "q" and canvas.data["frameClicked"] == False):
        canvas.data["frameClicked"] = True
        import game4
        redrawAll(canvas)
    elif (event.keysym == "c" and canvas.data["symbols1Clicked"] == False):
        canvas.data["symbols1Clicked"] = True
        import password4
        redrawAll(canvas)

# draws the images
def redrawAll(canvas):
    image = canvas.data["image"]
    canvas.create_image(400, 0, anchor = N, image = image)

####################################
# start function
# general run function template from 15-112 notes
# root.geometry learned from: https://www.python-course.eu/tkinter_layout_management.php
####################################

def startLightsOut():
    # for the music
    import music
    # create the root and the canvas
    root = Tk()
    root.resizable(False, False)
    root.title("Lights Out")
    root.geometry("+{}+{}".format(0, 0))
    canvas = Canvas(root, width = 800, height = 600)
    # starts with the first image of "Lights Out" 
    image = PhotoImage(file = "assets/introPartOne.gif")
    canvas.create_image(400, 0, anchor = N, image = image)
    canvas.pack()
    # store canvas in root and in canvas itself for callbacks
    root.canvas = canvas.canvas = canvas
    # set up canvas data and call init
    canvas.data = { }
    init(canvas)
    # set up events
    root.bind("<Button-1>", mousePressed)
    root.bind("<KeyPress>", keyPressed)
    root.bind("<KeyRelease>", keyReleased)
    # launch the app
    root.mainloop() 
    # for customization portion where user can design their own escape room
    import customizationPart1
    import customizationPart2 

def main():
    startLightsOut()

if (__name__ == '__main__'):
    main()