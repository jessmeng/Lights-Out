####################################
# Jessica Meng, jmeng1, Section B
# Lights Out
# 15-112 Term Project 
# passwordStrengthDetector1
# this is the password strength detector tool used to help the user understand what a strong password should look like and can generate random strong passwords for the user to use
# tkinter "Text" box feature learned from: http://effbot.org/tkinterbook/text.htm
# tkinter "Button" feature learned from: https://www.tutorialspoint.com/python/tk_button.htm (used this tutorial to write the code) 
# root.geometry learned from: https://www.python-course.eu/tkinter_layout_management.php
####################################

####################################
# imports
# necessary to run program
#################################### 

from tkinter import *
import tkinter 
import math
import random 
# webbrowser for web links
import webbrowser

####################################
# functions
#################################### 

# a strong password should have at least one special symbol, uppercase letter, lowercase letter, and number 
# start screen 
root = Tk()
canvas = Canvas(root, width = 500, height = 500)
canvas.create_rectangle(5, 5, 500, 500, fill = "black", outline = "yellow2", width = 15)
canvas.create_text(500/2, 500/3 - 40, text = "Welcome!", fill = "cyan", font = "Courier 60 bold")
canvas.create_text(500/2, 500/3 + 30, text = "Type in the box above", fill = "hot pink", font = "Courier 30 bold")
canvas.create_text(500/2, 500/3 + 70, text = "to test a password!", fill = "hot pink", font = "Courier 30 bold")
canvas.create_text(500/2, 500/3 + 150, text = "Excellent", fill = "firebrick2", font = "Courier 20 bold")
canvas.create_text(500/2, 500/3 + 180, text = "Good", fill = "orange", font = "Courier 20 bold")
canvas.create_text(500/2, 500/3 + 210, text = "Average", fill = "lawn green", font = "Courier 20 bold")
canvas.create_text(500/2, 500/3 + 240, text = "Poor", fill = "cyan", font = "Courier 20 bold")
canvas.create_text(500/2, 500/3 + 270, text = "Very Poor", fill = "magenta", font = "Courier 20 bold")

# takes in user's input 
# uses wrapper functions
def userpasswordInput():
    input = textBox.get("1.0", "end-1c")
    def checkpasswordStrength(password):
        # password strength starts off at 0 and builds up 
        passwordStrength = 0
        passwordLength = int()
        specialSymbols = int()
        lowerLetters = int()
        upperLetters = int()
        numberDigits = int()
        # a strong password consists of at least 6 characters, special symbols, lowercase letters, uppercase letters, and numbers
        # learned from: https://www.webopedia.com/TERM/S/strong_password.html
        if (len(password) >= 6):
            passwordLength = True
        # special symbols, lowercase letters, uppercase letters, and numbers
        specialCharacters = [' ', '!', '#', '$', '%', '&', '"', '(', ')', '*', '+', ',', '-', '.', '/', ':', ';', '<', '=', '>', '?', '@', '[', '\\', ']', '^', '_', '`', '{', '|', '}', '~',"'"]
        for symbol in specialCharacters:
            if (symbol in password):
                specialSymbols = True
        lowercaseLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
        for letter in lowercaseLetters:
            if (letter in password):
                lowerLetters = True
        uppercaseLetters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
        for letter in uppercaseLetters:
            if (letter in password):
                upperLetters = True
        numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
        for number in numbers:
            if (number in password):
                numberDigits = True
        if (passwordLength == True):
            passwordStrength += 1 
        if (specialSymbols == True):
            passwordStrength += 2
        if (lowerLetters == True):
            passwordStrength += 1 
        if (upperLetters == True):
            passwordStrength += 1 
        if (numberDigits == True):
            passwordStrength += 1
        passwordStrengthResult = str()
        # rankings for password strength 
        if (passwordStrength >= 5):
            passwordStrengthResult = "Excellent"
        if (passwordStrength == 4):
            passwordStrengthResult = "Good"
        if (passwordStrength == 3):
            passwordStrengthResult = "Average"
        if (passwordStrength == 2):
            passwordStrengthResult = "Poor"
        if (passwordStrength <= 1):
            passwordStrengthResult = "Very Poor"
        # different possible issues for user's password
        passwordIssues = [passwordLength, specialSymbols, lowerLetters, upperLetters, numberDigits]
        canvas.create_rectangle(5, 5, 500, 500, fill = "black", outline = "yellow2", width = 15)
        canvas.create_text(500/2, 500/3 - 50, text = "Password", fill = "firebrick2", font = "Courier 50 bold")
        canvas.create_text(500/2, 500/3, text = "Results", fill = "firebrick2", font = "Courier 50 bold")
        canvas.create_text(500/2, 500/2 - 10, text = "Your password is ...", fill = "green2", font = "Courier 37 bold")
        canvas.create_text(500/2, 500/2 + 50, text = passwordStrengthResult, fill = "cyan", font = "Courier 50 bold")
        canvas.create_text(500/2, 500/2 + 120, text = "To receive password info, type \'info\'.", fill = "magenta", font = "Courier 20 bold")
        canvas.create_text(500/2, 500/2 + 150, text = "To generate a password, type \'random\'.", fill = "magenta", font = "Courier 20 bold")
        canvas.create_text(500/2, 500/2 + 180, text = "To see easy passwords, type \'easy\'.", fill = "magenta", font = "Courier 20 bold")
        
        # displays the issues for the password entered depending on strength ranking
        if (input != "info" and input != "random" and input != "easy" and input != "special" and input != "lower" and input != "upper" and input != "number"):
            root = Tk()
            root.title("Password Issues :(")
            root.geometry("+{}+{}".format(305, 0))
            newCanvas = Canvas(root, width = 500, height = 500)
            newCanvas.create_rectangle(5, 5, 500, 500, fill = "black", outline = "yellow2", width = 15)
            newCanvas.create_text(500/2, 500/3 - 80, text = "Password Issues:", fill = "firebrick2", font = "Courier 40 bold")
            if (passwordIssues[0] != True):
                newCanvas.create_text(500/2, 500/3 - 20, text = "Your password is too short.", fill = "yellow2", font = "Courier 25 bold")
            if (passwordIssues[1] != True):
                newCanvas.create_text(500/2, 500/3 + 20, text = "Your password is missing", fill = "orange", font = "Courier 25 bold")
                newCanvas.create_text(500/2, 500/3 + 40, text = "a special symbol.", fill = "orange", font = "Courier 25 bold")
                newCanvas.create_text(500/2, 500/3 + 60, text = "What's a special symbol? Type \'special\'.", fill = "lavender", font = "Courier 18 bold")
            if (passwordIssues[2] != True):
                newCanvas.create_text(500/2, 500/3 + 100, text = "Your password is missing", fill = "lawn green", font = "Courier 25 bold")
                newCanvas.create_text(500/2, 500/3 + 120, text = "a lowercase letter.", fill = "lawn green", font = "Courier 25 bold")
                newCanvas.create_text(500/2, 500/3 + 140, text = "What's a lowercase letter? Type \'lower\'.", fill = "lavender", font = "Courier 16 bold")
            if (passwordIssues[3] != True):
                newCanvas.create_text(500/2, 500/3 + 180, text = "Your password is missing", fill = "cyan", font = "Courier 25 bold")
                newCanvas.create_text(500/2, 500/3 + 200, text = "an uppercase letter.", fill = "cyan", font = "Courier 25 bold")
                newCanvas.create_text(500/2, 500/3 + 220, text = "What's an uppercase letter? Type \'upper\'.", fill = "lavender", font = "Courier 16 bold")
            if (passwordIssues[4] != True):
                newCanvas.create_text(500/2, 500/3 + 260, text = "Your password is missing a number.", fill = "magenta", font = "Courier 22 bold")
                newCanvas.create_text(500/2, 500/3 + 280, text = "What's a number? Type \'number\'.", fill = "lavender", font = "Courier 18 bold")
            newCanvas.pack()
       
        # displays information about passwords and links to an article about creating strong passwords 
        if (input == "info"):
            canvas.create_rectangle(5, 5, 500, 500, fill = "black", outline = "yellow2", width = 15)
            canvas.create_text(500/2, 500/3 - 100, text = "What's in a", fill = "firebrick2", font = "Courier 50 bold")
            canvas.create_text(500/2, 500/3 - 50, text = "Strong Password?", fill = "firebrick2", font = "Courier 40 bold")
            canvas.create_text(500/2, 500/3 + 20, text = "- at least 6 characters", fill = "orange", font = "Courier 30 bold")
            canvas.create_text(500/2, 500/3 + 70, text = "- have a combination of", fill = "green2", font = "Courier 25 bold")
            canvas.create_text(500/2, 500/3 + 100, text = "special symbols, lowercase and", fill = "green2", font = "Courier 25 bold")
            canvas.create_text(500/2, 500/3 + 130, text = "uppercase letters, and numbers", fill = "green2", font = "Courier 25 bold")
            canvas.create_text(500/2, 500/3 + 180, text = "- not easy to guess", fill = "cyan", font = "Courier 30 bold")
            canvas.create_text(500/2, 500/3 + 230, text = "- different for each account", fill = "magenta", font = "Courier 27 bold")
            # for the web link for more information on passwords
            # learned from: http://effbot.org/zone/tkinter-text-hyperlink.htm
            def webLink(event):
                webbrowser.open_new(r"https://www.sagedatasecurity.com/blog/what-makes-a-strong-password-and-six-steps-to-create-one")
            root = Tk()
            root.title("Bonus: More Info!")
            root.geometry("+{}+{}".format(440, 0))
            # creates the label with the link
            # tkinter "Label" feature learned from: http://effbot.org/tkinterbook/label.htm
            link = Label(root, width = 30, height = 5, text = "Click for more \ninformation on passwords!", fg = "blue", bg = "lavender", font = "Courier 20 bold", cursor = "hand1")
            link.pack()
            link.bind("<Button-1>", webLink)
        
        elif (input == "random"):
            # creates a random password that meets the requirements of being a strong password
            randompassword = ""
            passwordLength = 8
            specialSymbols = "!#$%&()*+,-./:;<=>?@[\\]^_`{|}~"
            lowercaseLetters = "abcdefghijklmnopqrstuvwxyz"
            uppercaseLetters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            numbers = "0123456789"
            for element in range(passwordLength):
                nextIndex = random.randrange(len(lowercaseLetters))
                randompassword += lowercaseLetters[nextIndex]
            # replace 1 or 2 letters with a special symbol
            for num in range(random.randrange(1, 3)):
                replacedIndex = random.randrange(len(randompassword)//2, len(randompassword))
                randompassword = randompassword[0:replacedIndex] + str(specialSymbols[replacedIndex]) + randompassword[replacedIndex+1:]
            # replace 1 or 2 letters with an uppercase letter
            for num in range(random.randrange(1,3)):
                replacedIndex = random.randrange(len(randompassword)//2, len(randompassword))
                randompassword = randompassword[0:replacedIndex] + str(uppercaseLetters[replacedIndex]) + randompassword[replacedIndex+1:]
            # replace 1 or 2 characters with a number
            for num in range(random.randrange(1, 3)):
                replacedIndex = random.randrange(len(randompassword)//2)
                randompassword = randompassword[0:replacedIndex] + str(numbers[replacedIndex]) + randompassword[replacedIndex+1:]
            canvas.create_rectangle(5, 5, 500, 500, fill = "black", outline = "yellow2", width = 15)
            canvas.create_text(500/2, 500/3 - 50, text = "Here is your", fill = "firebrick2", font = "Courier 45 bold")
            canvas.create_text(500/2, 500/3, text = "Random Password:", fill = "orange", font = "Courier 43 bold")
            canvas.create_rectangle(500/3 - 60, 500/3 + 100, 500/2 + 140, 500/3 + 180, fill = "LightSkyBlue1", outline = "RoyalBlue1", width = 3)
            canvas.create_text(500/2, 500/3 + 140, text = randompassword, fill = "black", font = "Courier 50")
        
        elif (input == "easy"):
            # uses backtracking to generate "common" passwords
            def commonPassword(digits):
                passList = ["password", "123456", "sunshine", "123abc", "abc123"] 
                numbers = range(1, 10)
                def solve(new, digits):
                    if (len(str(new)) == digits):
                        return new
                    else:
                        for num in numbers:
                            new = new*10 + num
                            # if new password isLegal, then create a solution
                            if (isLegal(new)):
                                solution = solve(new, digits)
                                passList.append(new)
                                choice = random.choice(passList)
                                print(choice)
                                if (solution != None):
                                    return choice
                            new //= 10
                        return None
                return solve(0, digits)
            # isLegal function for the backtracking function commonPassword
            def isLegal(new):
                new = str(new)
                setsOf2 = set()
                for start in range(0, len(new) - 3):
                    end = start + 1
                    curSet = new[start:end]
                    if (curSet in setsOf2):
                        return False
                    else: 
                        setsOf2.add(curSet)
                print(setsOf2)
                return True 
            canvas.create_rectangle(5, 5, 500, 500, fill = "black", outline = "yellow2", width = 15)
            canvas.create_text(500/2, 500/3 - 50, text = "Here is a", fill = "firebrick2", font = "Courier 45 bold")
            canvas.create_text(500/2, 500/3, text = "Common Password:", fill = "orange", font = "Courier 43 bold")
            canvas.create_rectangle(500/3 - 100, 500/3 + 100, 500/2 + 180, 500/3 + 180, fill = "LightSkyBlue1", outline = "RoyalBlue1", width = 3)
            canvas.create_text(500/2, 500/3 + 140, text = commonPassword(6), fill = "black", font = "Courier 50")
            # for the web link for more information on passwords
            # learned from: http://effbot.org/zone/tkinter-text-hyperlink.htm
            def webLink(event):
                webbrowser.open_new(r"https://nakedsecurity.sophos.com/2010/12/15/the-top-50-passwords-you-should-never-use/")
            root = Tk()
            root.title("Bonus: More Info!")
            root.geometry("+{}+{}".format(415, 0))
            # creates the label with the link
            # tkinter "Label" feature learned from: http://effbot.org/tkinterbook/label.htm
            link = Label(root, width = 35, height = 5, text = "Click to see the top 50 \npasswords you should never use!", fg = "blue", bg = "lavender", font = "Courier 18 bold", cursor = "hand1")
            link.pack()
            link.bind("<Button-1>", webLink)
            
        # displays the special symbols
        elif (input == "special"):
            canvas.create_rectangle(5, 5, 500, 500, fill = "black", outline = "yellow2", width = 15)
            canvas.create_text(500/2, 500/3 - 50, text = "Special", fill = "firebrick2", font = "Courier 50 bold")
            canvas.create_text(500/2, 500/3, text = "Symbols", fill = "firebrick2", font = "Courier 50 bold")
            quotes1 = '"'
            quotes2 = "'"
            canvas.create_text(500/2, 500/3 + 80, text = "! # $ % & " + quotes1 + " ( ) * + ,", fill = "orange", font = "Courier 30 bold")
            canvas.create_text(500/2, 500/3 + 120, text = "- . / : ; " + quotes2 + " < = > ? @", fill = "lawn green", font = "Courier 30 bold")
            canvas.create_text(500/2, 500/3 + 160, text = "[ \\ ] ^ _ ` { | } ~", fill = "cyan", font = "Courier 30 bold")
        
        # displays the lowercase letters a-z
        elif (input == "lower"):
            canvas.create_rectangle(5, 5, 500, 500, fill = "black", outline = "yellow2", width = 15)
            canvas.create_text(500/2, 500/3 - 50, text = "Lowercase", fill = "firebrick2", font = "Courier 50 bold")
            canvas.create_text(500/2, 500/3, text = "Letters", fill = "firebrick2", font = "Courier 50 bold")
            canvas.create_text(500/2, 500/3 + 80, text = "a b c d e f g h i", fill = "orange", font = "Courier 30 bold")
            canvas.create_text(500/2, 500/3 + 120, text = "j k l m n o p q r", fill = "lawn green", font = "Courier 30 bold")
            canvas.create_text(500/2, 500/3 + 160, text = "s t u v w x y z", fill = "cyan", font = "Courier 30 bold")
        
        # displays the uppercase letters A-Z
        elif (input == "upper"):
            canvas.create_rectangle(5, 5, 500, 500, fill = "black", outline = "yellow2", width = 15)
            canvas.create_text(500/2, 500/3 - 50, text = "Uppercase", fill = "firebrick2", font = "Courier 50 bold")
            canvas.create_text(500/2, 500/3, text = "Letters", fill = "firebrick2", font = "Courier 50 bold")
            canvas.create_text(500/2, 500/3 + 80, text = "A B C D E F G H I", fill = "orange", font = "Courier 30 bold")
            canvas.create_text(500/2, 500/3 + 120, text = "J K L M N O P Q R", fill = "lawn green", font = "Courier 30 bold")
            canvas.create_text(500/2, 500/3 + 160, text = "S T U V W X Y Z", fill = "cyan", font = "Courier 30 bold")
        
        # displays the numbers 0-9
        elif (input == "number"):
            canvas.create_rectangle(5, 5, 500, 500, fill = "black", outline = "yellow2", width = 15)
            canvas.create_text(500/2, 500/3 - 30, text = "Numbers", fill = "firebrick2", font = "Courier 55 bold")
            canvas.create_text(500/2, 500/3 + 80, text = "0 1 2 3 4", fill = "lawn green", font = "Courier 40 bold")
            canvas.create_text(500/2, 500/3 + 120, text = "5 6 7 8 9", fill = "cyan", font = "Courier 40 bold")
            
    checkpasswordStrength(input)  
    print(input)

# creates the text box for the user to type input
# tkinter "Text" box feature learned from: http://effbot.org/tkinterbook/text.htm
textBox = Text(root, width = 20, height = 5, bg = "blue4", fg = "white", relief = SUNKEN, font = "Courier 20")
textBox.pack()

# creates the "Enter" button that records the user's input/response
# tkinter "Button" feature learned from: https://www.tutorialspoint.com/python/tk_button.htm (used this tutorial to write the code) 
enter = lambda: userpasswordInput()
enterButton = Button(root, width = 10, height = 2, text = "Enter", font = "Courier 18", highlightbackground = "LightBlue1", command = enter)
enterButton.pack()

####################################
# run function
# runs the above functions
####################################
   
def runPasswordStrengthDetector():
    canvas.pack()
    root.title("Password Strength Detector")
    root.geometry("+{}+{}".format(805, 0))
    mainloop()

runPasswordStrengthDetector()