####################################
# Jessica Meng, jmeng1, Section B
# Lights Out
# 15-112 Term Project 
# customizationPart1
# after the user escapes "Lights Out", they will get the option to build their own escape room
# this is the first part of customization
# tkinter "PhotoImage" feature learned from: http://effbot.org/tkinterbook/photoimage.htm
# tkinter "Frame" feature learned from: https://www.tutorialspoint.com/python/tk_frame.htm
# python "Frame" class learned from: https://stackoverflow.com/questions/34371088/how-does-class-applicationframe-works
# all colors used from: https://wiki.tcl.tk/37701
# root.geometry learned from: https://www.python-course.eu/tkinter_layout_management.php
####################################

####################################
# imports
# necessary to run program
####################################
 
import tkinter
from tkinter import * 
import math
import random 

####################################
# ObjectFunction class
# this is used to define the object (image) and keep track of whether it has been clicked, dragged, and placed by the user
####################################
 
class ObjectFunction(object):
    
    # init function to initialize needed variables
    def __init__(self, canvas, imageX, imageY, image):
        self.objectMoved = False
        self.canvas = canvas
        self.imageX = imageX
        self.imageY = imageY
        self.image = image
        # tkinter "PhotoImage" feature learned from: http://effbot.org/tkinterbook/photoimage.htm
        self.getImage = PhotoImage(file = self.image)
        self.drawImage = canvas.create_image(self.imageX, self.imageY, image = self.getImage)
        self.dragObject = self.move
        # tag_bind learned from: https://stackoverflow.com/questions/2786877/how-do-i-attach-event-bindings-to-items-on-a-canvas-using-tkinter
        # for the user to interact with objects contained in a Canvas object
        self.canvas.tag_bind(self.drawImage, '<Button1-Motion>', self.dragObject)
        self.canvas.tag_bind(self.drawImage, '<ButtonRelease-1>', self.dropObject)
         
    # keeps track of mousePressed 
    def move(self, event):
        # if the object is being moved, then recursively call the move function and redraw the object depending on coordinates moved to
        if (self.objectMoved == True):
            newImageX = event.x
            newImageY = event.y
            self.canvas.move(self.drawImage, newImageX - self.mouseX, newImageY - self.mouseY)
            # new coordinates are of where the user moved the image to
            self.mouseX = newImageX
            self.mouseY = newImageY
        # if the object is picked up, then objectMoved is set to true and becomes in the process of being moved
        elif (self.objectMoved == False):
            self.objectMoved = True
            # tag_raise learned from: https://stackoverflow.com/questions/10959858/tkinter-canvas-move-item-to-top-level
            # to move an item to the top level; everytime an object is picked up, it is moved to the top level
            self.canvas.tag_raise(self.drawImage)
            self.mouseX = event.x
            self.mouseY = event.y
    
    # when the object is dropped and placed, set objectMoved back to False 
    def dropObject(self, event):
        self.objectMoved = False

####################################
# Display class
# this is used to display the user interface for the user to see the objects/backgrounds
# tkinter "Frame" feature learned from: https://www.tutorialspoint.com/python/tk_frame.htm
# python "Frame" class learned from: https://stackoverflow.com/questions/34371088/how-does-class-applicationframe-works
####################################

class Display(Frame):
 
    # init function to initialize needed variables
    def __init__(self, root):
        self.root = root
        Frame.__init__(self, root)
        
        self.width = 1200
        self.height = 800
        self.canvas = Canvas(self, width = self.width, height = self.height)
        self.canvas.pack()
        
        # creates the background for the menu bar
        self.canvas.create_rectangle(0, 0, 300, 800, fill = "SlateGray1", width = 0)
        self.canvas.create_text(150, 23, text = "FURNITURE:", fill = "black", font = "Courier 40")
        self.canvas.create_text(150, 50, text = "(Drag and Drop)", fill = "black", font = "Courier 20")
        self.canvas.create_text(150, 470, text = "OBJECTS:", fill = "black", font = "Courier 40")
        self.canvas.create_text(150, 497, text = "(Drag and Drop)", fill = "black", font = "Courier 20")
        self.canvas.create_text(150, 610, text = "EFFECTS:", fill = "black", font = "Courier 40")
        self.canvas.create_text(150, 637, text = "(Drag and Drop)", fill = "black", font = "Courier 20")
        self.canvas.create_rectangle(220, 760, 280, 790, fill = "white", outline = "black", width = 2)
        self.canvas.create_rectangle(240, 770, 260, 783, fill = "black", outline = "grey", width = 1)
        self.canvas.create_rectangle(253, 767, 258, 770, fill = "red", width = 0)
        self.canvas.create_oval(248, 774, 253, 779, outline = "grey", width = 2)
        
        # calls the menu for the furniture, objects, and effects
        
        # for the empty room backgrounds 
        self.room1 = ObjectFunction(self.canvas, 750, 400, "assets/emptyRoom1.gif")
        self.room2 = ObjectFunction(self.canvas, 750, 400, "assets/emptyRoom2.gif")
        self.room3 = ObjectFunction(self.canvas, 750, 400, "assets/emptyRoom3.gif")
        
        # for the furniture 
        self.furniture1 = ObjectFunction(self.canvas, 120, 130, "assets/couch1.gif")
        self.furniture2 = ObjectFunction(self.canvas, 100, 130, "assets/couch2.gif")
        self.furniture3 = ObjectFunction(self.canvas, 150, 270, "assets/dresser.gif")
        self.furniture4 = ObjectFunction(self.canvas, 150, 270, "assets/desk1.gif")
        self.furniture5 = ObjectFunction(self.canvas, 150, 290, "assets/desk2.gif")
        self.furniture6 = ObjectFunction(self.canvas, 150, 230, "assets/chair1.gif")
        self.furniture7 = ObjectFunction(self.canvas, 150, 230, "assets/chair2.gif")
        self.furniture8 = ObjectFunction(self.canvas, 120, 360, "assets/painting1.gif")
        self.furniture9 = ObjectFunction(self.canvas, 130, 360, "assets/painting2.gif")
        self.furniture10 = ObjectFunction(self.canvas, 140, 360, "assets/painting3.gif")
        self.furniture11 = ObjectFunction(self.canvas, 150, 360, "assets/painting4.gif")
        
        # for the objects 
        self.object1 = ObjectFunction(self.canvas, 200, 550, "assets/key1.gif")
        self.object2 = ObjectFunction(self.canvas, 220, 550, "assets/key2.gif")
        self.object3 = ObjectFunction(self.canvas, 240, 550, "assets/key3.gif")
        self.object4 = ObjectFunction(self.canvas, 40, 550, "assets/puzzlePiece1.gif")
        self.object5 = ObjectFunction(self.canvas, 60, 550, "assets/puzzlePiece2.gif")
        self.object6 = ObjectFunction(self.canvas, 80, 550, "assets/puzzlePiece3.gif")
        self.object7 = ObjectFunction(self.canvas, 100, 550, "assets/apple.gif")
        self.object8 = ObjectFunction(self.canvas, 140, 550, "assets/pen.gif")
        self.object8 = ObjectFunction(self.canvas, 140, 550, "assets/magGlass.gif")
        
        # for the effects (extra)
        self.effect1 = ObjectFunction(self.canvas, -150, 650, "assets/lights1.gif")
        self.effect2 = ObjectFunction(self.canvas, -130, 730, "assets/lights2.gif")
        self.effect3 = ObjectFunction(self.canvas, -150, 720, "assets/lights3.gif")
        self.effect4 = ObjectFunction(self.canvas, -130, 750, "assets/lights4.gif")

####################################
# mousePressed function to detect if user clicks the camera button
####################################

def mousePressed(event):
    # user's mouse x-coordinate and y-coordinate 
    userX = event.x
    userY = event.y
    if (userX > 220 and userX < 280 and userY > 760 and userY < 790):
        import screenshot
        
####################################
# run function
# runs the program
# general run function template from 15-112 notes
####################################

def runCustomization():
    def mousePressedWrapper(event):
        mousePressed(event)
    root = Tk()
    root.resizable(False, False)
    root.title("User Custom Escape Room")    
    root.geometry("+{}+{}".format(0, 0))
    root.bind("<Button-1>", lambda event: mousePressedWrapper(event))
    Display(root).pack(fill = 'both')
    root.mainloop()
  
runCustomization()