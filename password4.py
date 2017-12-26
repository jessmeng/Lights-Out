####################################
# Jessica Meng, jmeng1, Section B
# Lights Out
# 15-112 Term Project 
# password4
# this is the fourth and final "crack the password" puzzle the user has to solve
# tkinter "Entry" box feature learned from: http://effbot.org/tkinterbook/entry.htm (used this tutorial to write the code) 
# tkinter "Button" feature learned from: https://www.tutorialspoint.com/python/tk_button.htm (used this tutorial to write the code) 
# all colors used from: https://wiki.tcl.tk/37701
# root.geometry learned from: https://www.python-course.eu/tkinter_layout_management.php
####################################

####################################
# imports
#################################### 

import tkinter 
from tkinter import *
import random

####################################
# function and main
# necessary to run program
####################################

# password4 will be the most difficult to crack
# Jess is trying to create the ultimate password. She decides it has to have EVERYTHING: a symbol in the exact middle of the passcode, letters surrounding the symbol, with the letters being the first letters of significant people in her life: Helen, Tina, Mitzi, Mohini, Jack, Aldrich, a combination of uppercase and lowercase letters, and finally, 2 numbers in the beginning, in consecutive decreasing order. 
# password3 strength is very strong

root = Tk()
canvas = Canvas(root, width = 500, height = 500)
  
# creates the starting background and instruction screen
canvas.create_rectangle(5, 5, 500, 500, fill = "black", outline = "yellow2", width = 15)
canvas.create_text(500/2, 500/3 - 20, text = "Welcome!", fill = "cyan", font = "Courier 60 bold")
canvas.create_text(500/2, 500/3 + 60, text = "Type in the box above", fill = "green2", font = "Courier 30 bold")
canvas.create_text(500/2, 500/3 + 100, text = "to guess Jess' password.", fill = "green2", font = "Courier 30 bold")
canvas.create_text(500/2, 2.9*500/4, text = "Type \'h\' for help.", fill = "magenta", font = "Courier 30 bold")

# uses backtracking to see if user input is the correct password 
def getPassword(input, answer):
    input = inputFromUser.get()
    def solve(input, answer):
        if (len(input) == len(answer)):
            return input 
        else:
            for item in answer:
                input += str(item)
                # if input is legal, then create solution
                if (isLegal(input, answer)):
                    solution = solve(input, answer)
                    if (solution != None):
                        return solution
            return None
    return solve(input, answer)

# isLegal function for backtracking
def isLegal(input, answer):
    # input has to be the same length and match every item in answer
    if (len(input) != len(answer)):
        return False
    for item in input:
        if (item not in answer): 
            return False
    if (input != answer): 
        return False
    return True 

# gets the user input 
def userInput():
    input = inputFromUser.get()
    # if user presses "h", generate a random hint
    if (input == "h"):
        hintsList = ['''  The length of this\npassword should be 10.''', '''The starting\nnumber is 5.''', '''The first letter\n  is lowercase.''', '''The first person\n    is Tina.''', '''The second letter\n  is uppercase.''', '''The second person\n   is Aldrich.''', '''The third letter\n  is lowercase.''', '''The third person\n    is Mitzi.''', '''The symbol is the\n 6th character.''', '''The fourth letter\n  is uppercase.''', '''The fourth person\n    is Mohini.''', '''The fifth letter\n  is lowercase.''', '''The fifth person\n    is Jack.''', '''The sixth and final\nletter is lowercase.''', '''The sixth and final\n  person is Helen.''']
        randomHint = random.choice(hintsList)
        canvas.create_rectangle(5, 5, 500, 500, fill = "black", outline = "yellow2", width = 15)
        canvas.create_text(500/2, 500/3 - 30, text = "Hint:", fill = "firebrick2", font = "Courier 60 bold")
        canvas.create_text(500/2, 500/2 - 20, text = randomHint, fill = "green2", font = "Courier 30 bold")
        canvas.create_text(500/2, 2.9*500/4 - 30, text = "Try Again!", fill = "magenta", font = "Courier 30 bold")
    elif (input != "h"):      
        # if input does not match the answer, return a "Try Again" screen
        # if input does match the answer, return a screen that tells the user the next object
        if (getPassword(input, "54tAm@MjH") != "54tAm@MjH" or len(input) <= 0):
            canvas.create_rectangle(5, 5, 500, 500, fill = "black", outline = "yellow2", width = 15)
            canvas.create_text(500/2, 500/3, text = "Try Again!", fill = "firebrick2", font = "Courier 60 bold")
            canvas.create_text(500/2, 500/2 - 10, text = "Incorrect Password :(", fill = "green2", font = "Courier 30 bold")
            canvas.create_text(500/2, 2.9*500/4 - 30, text = "Try a different password.", fill = "magenta", font = "Courier 25 bold")
            canvas.create_text(500/2, 2.9*500/4, text = "Type \'h\' for help.", fill = "magenta", font = "Courier 25 bold")
        else:
            canvas.create_rectangle(5, 5, 500, 500, fill = "black", outline = "yellow2", width = 15)
            canvas.create_text(500/2, 500/3 - 30, text = "Good Work!", fill = "cyan", font = "Courier 60 bold")
            canvas.create_text(500/2, 500/2 - 40, text = "The next object is", fill = "green2", font = "Courier 30 bold")
            canvas.create_text(500/2, 500/2, text = "the DRAWER in room 1.", fill = "green2", font = "Courier 30 bold")
            canvas.create_text(500/2, 2.9*500/4 - 40, text = "Exit this window and press", fill = "magenta", font = "Courier 25 bold")
            canvas.create_text(500/2, 2.9*500/4 - 10, text = "\'1\' to return to rooms.", fill = "magenta", font = "Courier 25 bold")
            canvas.create_text(500/2, 2.9*500/4 + 30, text = "Click TEST PASSWORD to", fill = "magenta", font = "Courier 25 bold")
            canvas.create_text(500/2, 2.9*500/4 + 60, text = "test this password!", fill = "magenta", font = "Courier 25 bold")
    print(input)

# tracks the characters the user has entered to generate messages that lets user know if they are close
def trackUserInput(keyPressed):
    print("User Input So Far: {}".format(keyPressed))
    if (keyPressed == "h"):
        hintsList = ['''  The length of this\npassword should be 10.''', '''The starting\nnumber is 5.''', '''The first letter\n  is lowercase.''', '''The first person\n    is Tina.''', '''The second letter\n  is uppercase.''', '''The second person\n   is Aldrich.''', '''The third letter\n  is lowercase.''', '''The third person\n    is Mitzi.''', '''The symbol is the\n 6th character.''', '''The fourth letter\n  is uppercase.''', '''The fourth person\n    is Mohini.''', '''The fifth letter\n  is lowercase.''', '''The fifth person\n    is Jack.''', '''The sixth and final\nletter is lowercase.''', '''The sixth and final\n  person is Helen.''']
        randomHint = random.choice(hintsList)
        canvas.create_rectangle(5, 5, 500, 500, fill = "black", outline = "yellow2", width = 15)
        canvas.create_text(500/2, 500/3 - 30, text = "Hint:", fill = "firebrick2", font = "Courier 60 bold")
        canvas.create_text(500/2, 500/2 - 20, text = randomHint, fill = "green2", font = "Courier 30 bold")
        canvas.create_text(500/2, 2.9*500/4 - 30, text = "Try Again!", fill = "magenta", font = "Courier 30 bold")
    elif (keyPressed == "5"):
        canvas.create_rectangle(5, 5, 500, 500, fill = "black", outline = "yellow2", width = 15)
        canvas.create_text(500/2, 500/3, text = "Getting There!", fill = "cyan", font = "Courier 50 bold")
        canvas.create_text(500/2, 500/2 - 10, text = "You got the first", fill = "green2", font = "Courier 30 bold")
        canvas.create_text(500/2, 500/2 + 30, text = "character of the password!", fill = "green2", font = "Courier 25 bold")
        canvas.create_text(500/2, 2.9*500/4, text = "Keep Going!", fill = "magenta", font = "Courier 40 bold")
        canvas.create_text(500/2, 2.9*500/4 + 50, text = "Type \'h\' for help.", fill = "magenta", font = "Courier 25 bold")
    elif (keyPressed == "54"):
        canvas.create_rectangle(5, 5, 500, 500, fill = "black", outline = "yellow2", width = 15)
        canvas.create_text(500/2, 500/3, text = "Getting There!", fill = "cyan", font = "Courier 50 bold")
        canvas.create_text(500/2, 500/2 - 10, text = "You got the second", fill = "green2", font = "Courier 30 bold")
        canvas.create_text(500/2, 500/2 + 30, text = "character of the password!", fill = "green2", font = "Courier 25 bold")
        canvas.create_text(500/2, 2.9*500/4, text = "Keep Going!", fill = "magenta", font = "Courier 40 bold")
        canvas.create_text(500/2, 2.9*500/4 + 50, text = "Type \'h\' for help.", fill = "magenta", font = "Courier 25 bold")
    elif (keyPressed == "54t"):
        canvas.create_rectangle(5, 5, 500, 500, fill = "black", outline = "yellow2", width = 15)
        canvas.create_text(500/2, 500/3, text = "Getting There!", fill = "cyan", font = "Courier 50 bold")
        canvas.create_text(500/2, 500/2 - 10, text = "You got the third", fill = "green2", font = "Courier 30 bold")
        canvas.create_text(500/2, 500/2 + 30, text = "character of the password!", fill = "green2", font = "Courier 25 bold")
        canvas.create_text(500/2, 2.9*500/4, text = "Keep Going!", fill = "magenta", font = "Courier 40 bold")
        canvas.create_text(500/2, 2.9*500/4 + 50, text = "Type \'h\' for help.", fill = "magenta", font = "Courier 25 bold")
    elif (keyPressed == "54tA"):
        canvas.create_rectangle(5, 5, 500, 500, fill = "black", outline = "yellow2", width = 15)
        canvas.create_text(500/2, 500/3, text = "Getting There!", fill = "cyan", font = "Courier 50 bold")
        canvas.create_text(500/2, 500/2 - 10, text = "You got the fourth", fill = "green2", font = "Courier 30 bold")
        canvas.create_text(500/2, 500/2 + 30, text = "character of the password!", fill = "green2", font = "Courier 25 bold")
        canvas.create_text(500/2, 2.9*500/4, text = "Keep Going!", fill = "magenta", font = "Courier 40 bold")
        canvas.create_text(500/2, 2.9*500/4 + 50, text = "Type \'h\' for help.", fill = "magenta", font = "Courier 25 bold")
    elif (keyPressed == "54tAm"):
        canvas.create_rectangle(5, 5, 500, 500, fill = "black", outline = "yellow2", width = 15)
        canvas.create_text(500/2, 500/3, text = "Getting There!", fill = "cyan", font = "Courier 50 bold")
        canvas.create_text(500/2, 500/2 - 10, text = "You got the fifth", fill = "green2", font = "Courier 30 bold")
        canvas.create_text(500/2, 500/2 + 30, text = "character of the password!", fill = "green2", font = "Courier 25 bold")
        canvas.create_text(500/2, 2.9*500/4, text = "Keep Going!", fill = "magenta", font = "Courier 40 bold")
        canvas.create_text(500/2, 2.9*500/4 + 50, text = "Type \'h\' for help.", fill = "magenta", font = "Courier 25 bold")
    elif (keyPressed == "54tAm@"):
        canvas.create_rectangle(5, 5, 500, 500, fill = "black", outline = "yellow2", width = 15)
        canvas.create_text(500/2, 500/3, text = "Getting There!", fill = "cyan", font = "Courier 50 bold")
        canvas.create_text(500/2, 500/2 - 10, text = "You got the sixth", fill = "green2", font = "Courier 30 bold")
        canvas.create_text(500/2, 500/2 + 30, text = "character of the password!", fill = "green2", font = "Courier 25 bold")
        canvas.create_text(500/2, 2.9*500/4, text = "Keep Going!", fill = "magenta", font = "Courier 40 bold")
        canvas.create_text(500/2, 2.9*500/4 + 50, text = "Type \'h\' for help.", fill = "magenta", font = "Courier 25 bold")
    elif (keyPressed == "54tAm@M"):
        canvas.create_rectangle(5, 5, 500, 500, fill = "black", outline = "yellow2", width = 15)
        canvas.create_text(500/2, 500/3, text = "Getting There!", fill = "cyan", font = "Courier 50 bold")
        canvas.create_text(500/2, 500/2 - 10, text = "You got the seventh", fill = "green2", font = "Courier 30 bold")
        canvas.create_text(500/2, 500/2 + 30, text = "character of the password!", fill = "green2", font = "Courier 25 bold")
        canvas.create_text(500/2, 2.9*500/4, text = "Keep Going!", fill = "magenta", font = "Courier 40 bold")
        canvas.create_text(500/2, 2.9*500/4 + 50, text = "Type \'h\' for help.", fill = "magenta", font = "Courier 25 bold")
    elif (keyPressed == "54tAm@Mj"):
        canvas.create_rectangle(5, 5, 500, 500, fill = "black", outline = "yellow2", width = 15)
        canvas.create_text(500/2, 500/3, text = "Getting There!", fill = "cyan", font = "Courier 50 bold")
        canvas.create_text(500/2, 500/2 - 10, text = "You got the eighth", fill = "green2", font = "Courier 30 bold")
        canvas.create_text(500/2, 500/2 + 30, text = "character of the password!", fill = "green2", font = "Courier 25 bold")
        canvas.create_text(500/2, 2.9*500/4, text = "Keep Going!", fill = "magenta", font = "Courier 40 bold")
        canvas.create_text(500/2, 2.9*500/4 + 50, text = "Type \'h\' for help.", fill = "magenta", font = "Courier 25 bold")
    elif (keyPressed == "54tAm@MjH"):
        canvas.create_rectangle(5, 5, 500, 500, fill = "black", outline = "yellow2", width = 15)
        canvas.create_text(500/2, 500/3 - 30, text = "Correct", fill = "cyan", font = "Courier 60 bold")
        canvas.create_text(500/2, 500/3 + 20, text = "Password!", fill = "cyan", font = "Courier 60 bold")
        canvas.create_text(500/2, 500/2 + 10, text = "You guessed", fill = "green2", font = "Courier 30 bold")
        canvas.create_text(500/2, 500/2 + 40, text = "Jess' password!", fill = "green2", font = "Courier 30 bold")
        canvas.create_text(500/2, 2.9*500/4, text = "Click ENTER!", fill = "magenta", font = "Courier 40 bold")
    else:
        canvas.create_rectangle(5, 5, 500, 500, fill = "black", outline = "yellow2", width = 15)
        canvas.create_text(500/2, 500/3, text = "Backtrack!", fill = "firebrick2", font = "Courier 60 bold")
        canvas.create_text(500/2, 500/2 - 10, text = "You have the wrong", fill = "green2", font = "Courier 30 bold")
        canvas.create_text(500/2, 500/2 + 30, text = "next character.", fill = "green2", font = "Courier 30 bold")
        canvas.create_text(500/2, 2.9*500/4, text = "Try Again!", fill = "magenta", font = "Courier 40 bold")
        canvas.create_text(500/2, 2.9*500/4 + 50, text = "Type \'h\' for help.", fill = "magenta", font = "Courier 25 bold")
    return True
userInputTracked = root.register(trackUserInput)

# keeps track of which key the user presses
def keyPressed(event):
    print("Key Pressed: {}".format(event.char))

# keeps track of what the user has inputted so far (which keys)
def userInputSoFar(*args):
    print("User Input So Far: {}".format(soFar.get(), args))
soFar = StringVar()

# creates the text box for the user's input
# learned from: http://effbot.org/tkinterbook/entry.htm
inputFromUser = Entry(root, width = 20, bg = "blue4", fg = "white", font = "Courier 20", textvariable = soFar, validate = "key", validatecommand = (userInputTracked, "%P"), cursor = "pencil")
inputFromUser.bind('<Key>', keyPressed)
inputFromUser.pack(ipady = 30)
canvas.pack()

# creates the "Enter" button that records the user's input/response
# tkinter "Button" feature learned from: https://www.tutorialspoint.com/python/tk_button.htm
enter = lambda: userInput()
enterButton = Button(root, width = 10, height = 2, text = "ENTER", font = "Courier 18", highlightbackground = "LightBlue1", command = enter)
enterButton.pack()

# creates the "TEST PASSWORD" button that brings the user to the passwordStrengthDetector 
def importPasswordStrengthDetector():
    import passwordStrengthDetector
    
test = lambda: importPasswordStrengthDetector()
testButton = Button(root, width = 20, height = 2, text = "TEST PASSWORD", font = "Courier 18", highlightbackground = "light pink", command = test)
testButton.pack()

####################################
# run function
# runs the above functions
####################################

def runPassword4():
    canvas.pack()
    root.title("Password 4")
    root.geometry("+{}+{}".format(805, 0))
    mainloop()
    
runPassword4()