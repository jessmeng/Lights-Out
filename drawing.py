####################################
# Jessica Meng, jmeng1, Section B
# Lights Out
# 15-112 Term Project 
# drawing
# this is the drawing interface
# this is called "Cyber Draw" and it is a drawing puzzle that is for fun for the user.
# tkinter painting learned from: https://canvascanvascanvas.python-course.eu/tkinter_canvas.php
# tkinter "Canvas" feature learned from: http://effbot.org/tkinterbook/canvas.htm (used this to write code)
# tkinter "Label" feature learned from: http://effbot.org/tkinterbook/label.htm (used this to write code)
# root.geometry learned from: https://www.python-course.eu/tkinter_layout_management.php
####################################

####################################
# imports
# necessary to run program
#################################### 

from tkinter import *
import tkinter
import time

####################################
# functions
#################################### 

width = 500
height = 300

# user draws using small ovals to represent pixels
def draw(event):
   x1 = event.x - 1
   y1 = event.y - 1
   x2 = event.x + 1
   y2 = event.y + 1
   canvas.create_oval(x1, y1, x2, y2, fill = "black")

# to display the canvas 
root = Tk()
root.resizable(False, False)
root.title("Cyber Draw Canvas")
root.geometry("+{}+{}".format(805, 450))
canvas = Canvas(root, width = width, height = height)
canvas.pack(expand = YES, fill = BOTH)
canvas.bind("<B1-Motion>", draw)

# instructions for the user 
# learned from: http://effbot.org/tkinterbook/label.htm
instructions = Label(root, text = "Press and drag mouse to draw!", font = "Courier 20")
instructions.pack(side = BOTTOM)
    
####################################
# run function
# to run the above functions
#################################### 

def drawing():
    mainloop()

drawing()