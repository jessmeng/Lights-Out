####################################
# Jessica Meng, jmeng1, Section B
# Lights Out
# 15-112 Term Project 
# game2
# this is the second game in the series of puzzles the user has to solve
# this is the easier version of the game, where the AI is not as "smart"
# this game is called "Tic Tac Virus", where the player is the "X" and the opponenet (also known as the "virus") is the "V". The "virus" is the computer, who will play the player. The goal of the game is for the player to beat the "virus", so it does not infect their computer. 
# uses the Minimax decision rule: https://en.wikipedia.org/wiki/Minimax, https://stackoverflow.com/questions/31928352/python-tic-tac-toe-using-minimax-does-not-make-best-move, https://cwoebker.com/posts/tic-tac-toe, http://www.sarathlakshman.com/2011/04/29/writing-a-tic-tac
# idea for the game from Internet
# the computer tries to find the best place to move depending on where the player has placed their "X" and loops through all the possible solutions that can result in a win for the virus and a loss for the player or a tie for the next best possible option 
# tkinter "Button" feature learned from: https://www.tutorialspoint.com/python/tk_button.htm (used this tutorial to write the code) 
# tkinter "grid" feature learned from: http://effbot.org/tkinterbook/grid.htm (used this to write code)
# all colors used from: https://wiki.tcl.tk/37701
# root.geometry learned from: https://www.python-course.eu/tkinter_layout_management.php
####################################

####################################
# imports
# necessary to run program
#################################### 

import tkinter
from tkinter import *
from tkinter import Tk
from tkinter import Button
from tkinter import ttk 
from copy import deepcopy

####################################
# Minimax Class
# learned from: https://en.wikipedia.org/wiki/Minimax, https://stackoverflow.com/questions/31928352/python-tic-tac-toe-using-minimax-does-not-make-best-move 
# the computer "minimizes the possible loss in a worst case scenario" or tries to make the next best move. It iterates through all the possibilities and sees whether a certain series of steps leads to a win, tie, or a loss: https://cwoebker.com/posts/tic-tac-toe
####################################  

class Minimax(object):
   
   #init to initialize all the variables needed 
   def __init__(self, other = 0):
      self.dict = { }
      self.size = 3
      self.emptyCell = ' '
      # sets Tic Tac Virus board to empty cells initially 
      for col in range(self.size):
         for row in range(self.size):
            self.dict[row, col] = self.emptyCell
      self.player = 'X'
      self.virus = 'V'
      if (other):
         # deepcopy of dict learned from: https://stackoverflow.com/questions/5105517/deep-copy-of-a-dict-in-python
         self.__dict__ = deepcopy(other.__dict__)
   
   # repr function to display "X"s and "V"s
   def __repr__(self):
      letters = ""
      for col in range(self.size):
         for row in range(self.size):
            letters += self.dict[row, col]
         letters += "\n"
      return letters
      
   # basic minimax template from https://en.wikipedia.org/wiki/Minimax
   # learned minimax from: https://stackoverflow.com/questions/31928352/python-tic-tac-toe-using-minimax-does-not-make-best-move, https://cwoebker.com/posts/tic-tac-toe, http://www.sarathlakshman.com/2011/04/29/writing-a-tic-tac
   # method to implement AI for the virus to find where to place "V"; tries to find the place that is best for computer and worst for player
   # maximizes winning chances and minimizes losing chances
   def minimax(self, player):
      # sees if there is already a winner
      if (self.gameOver()):
         # -1 means player wins, which is the best case for the player
         # 1 means virus wins, which the best case for virus 
         if (player != True):
            firstBest = 1
            secondBest = 0
            bestOption = (firstBest, secondBest)
            return bestOption
         elif (player == True):
            firstBest = -1
            secondBest = 0
            bestOption = (firstBest, secondBest)
            return bestOption
      # sees if there is no winner (tie)
      # 0 means that there is no winner
      elif (self.tieGame()):
         firstBest = 0
         secondBest = 0
         bestOption = (firstBest, secondBest)
         return bestOption
      # finds the next best move for the virus and the best next move for the player (opponent) 
      elif (player != True):
         firstBest = 2
         secondBest = 0
         bestOption = (firstBest, secondBest)
         for row, col in self.dict:
            # if cell is empty, a possible new option would be to move to empty cell 
            if (self.dict[row,col] == self.emptyCell):
               # recurisve call at each level to see all available moves
               newOption = self.move(row, col).minimax(not player)[0]
               if (newOption < bestOption[0]):
                  bestOption = (newOption, (row, col))
         return bestOption
      elif (player == True):
         firstBest = -2
         secondBest = 0
         bestOption = (firstBest, secondBest)
         for row, col in self.dict:
            # if cell is empty, a possible new option would be to move to empty cell 
            if (self.dict[row, col] == self.emptyCell):
               # recurisve call at each level to see all available moves
               newOption = self.move(row, col).minimax(not player)[0]
               if (newOption > bestOption[0]):
                  bestOption = (newOption, (row, col))
         return bestOption
         
####################################
# TicTacVirusBoard Class
# inherits from Minimax Class for the method of AI 
#################################### 

class TicTacVirusBoard(Minimax):
   
   # init function for key variables
   def __init__(self, other = 0):
      self.dict = { }
      self.size = 3
      self.emptyCell = ' '
      # sets Tic Tac Virus board to empty cells initially 
      for col in range(self.size):
         for row in range(self.size):
            self.dict[row, col] = self.emptyCell
      self.player = 'X'
      self.virus = 'V'
      if (other):
         self.__dict__ = deepcopy(other.__dict__)
   
   # repr function inherited from Minimax class
   def __repr__(self):
      super().__repr__(self)
 
   # this is to know where to move next  
   def move(self, row, col):
      board = TicTacVirusBoard(self)
      board.dict[row,col] = board.player
      (board.player, board.virus) = (board.virus, board.player)
      return board
 
   # finds the best option for moving the virus based on the minimax method 
   def bestOption(self):
      option = self.minimax(True)[1]
      return option
   
   # if the game is tied (no winner aka no one row of all the same letter) 
   def tieGame(self):
      for (row,col) in self.dict:
         if (self.dict[row, col] == self.emptyCell):
            return False
      return True
   
   # game over when either player or virus wins or board is full
   # the AI for the "easy" version of the game only places a "V" in the next available empty cell
   def gameOver(self):
      board = TicTacVirusBoard(self)
      # checks the rows to see if they are all of the same letter
      for col in range(self.size):
         winner = []
         for row in range(self.size):
            # if player in cell, then virus avoids the player
            if (self.dict[row, col] == self.player):
               winner.append((row, col))
               if (self.size == len(winner)):
                  # if one of the cells in the row is a "V" then virus is the winner
                  # if one of the cells in the row in an "X" then the player is the winner
                  if (board.dict[winner[0]] == self.virus):
                     winner = self.virus 
                  elif (board.dict[winner[0]] == self.player):
                     winner = self.player
                  return winner
      # checks the columns to see if they are all of the same letter
      for row in range(self.size):
         winner = []
         for col in range(self.size):
            if (self.dict[row, col] == self.player):
               winner.append((row, col))
               if (self.size == len(winner)):
                  # if one of the cells in the row is a "V" then virus is the winner
                  # if one of the cells in the row in an "X" then the player is the winner
                  if (board.dict[winner[0]] == self.virus):
                     winner = self.virus 
                  elif (board.dict[winner[0]] == self.player):
                     winner = self.player
                  return winner
      # checks the first diagonal to see if they are all of the same letter
      winner = []
      for col in range(self.size):
         if (self.dict[col, col] == self.player):
            winner.append((col, col))
            if (self.size == len(winner)):
               # if one of the cells in the row is a "V" then virus is the winner
               # if one of the cells in the row in an "X" then the player is the winner
               if (board.dict[winner[0]] == self.virus):
                  winner = self.virus 
               elif (board.dict[winner[0]] == self.player):
                  winner = self.player
               return winner
      # checks the second diagonal to see if they are all of the same letter
      winner = []
      for col in range(self.size):
         if (self.dict[self.size - col - 1, col] == self.player):
            winner.append((self.size - col - 1, col))
            if (self.size == len(winner)):
               # if one of the cells in the row is a "V" then virus is the winner
               # if one of the cells in the row in an "X" then the player is the winner
               if (board.dict[winner[0]] == self.virus):
                  winner = self.virus 
               elif (board.dict[winner[0]] == self.player):
                  winner = self.player
               return winner
      # if 0 of them have the same letter all in one, return 0
      return 0
         
####################################
# DisplayTicTacVirusBoard Class
# this displays the Tic Tac Virus board 
# tkinter "Button" feature learned from: https://www.tutorialspoint.com/python/tk_button.htm (used this tutorial to write the code) 
####################################  

class DisplayTicTacVirusBoard(object):
 
   # init function for important variables to display board
   def __init__(self):
      self.root = Tk()
      self.root.resizable(width = 1000, height = 1000)
      self.root.title('Tic Tac Virus')
      self.board = TicTacVirusBoard()
      self.buttonsDict = { }
      # draws the "Play Again" button
      # tkinter "Button" feature learned from: https://www.tutorialspoint.com/python/tk_button.htm (used this tutorial to write the code) 
      playAgainButton = Button(self.root, width = 10, height = 2, text = 'Play Again', font = "Courier 12", highlightbackground = "pink", command = lambda: self.playAgain())
      playAgainButton.grid(row = 3, column = 1)
      # draws the initial empty board
      for row, col in self.board.dict:
         draw = (lambda row = row, col = col: self.move(row, col))
         button = Button(self.root, width = 5, height = 3, font = "Courier 25", highlightbackground = "black", state = "normal", command = (lambda row = row, col = col: self.move(row, col)))
         button.grid(row = col, column = row) 
         self.buttonsDict[row,col] = button
      self.update()
   
   # to reset the board back to empty (game back to beginning)
   def playAgain(self):
      self.board = TicTacVirusBoard()
      newBoard = self.update()
      return newBoard
   
   # to move the virus so it knows where to place its "V" 
   def move(self,row,col):
      # cursors learned from: http://infohost.nmt.edu/tcc/help/pubs/tkinter/web/cursors.html
      self.root.config(cursor = "pencil")
      self.root.update()
      self.board = self.board.move(row, col)
      self.update()
      # to find the best option
      nextMove = self.board.bestOption()
      if (nextMove):
         self.board = self.board.move(*nextMove)
         self.update()
      self.root.config(cursor = "")
 
   # to update the board every time a button is pressed 
   def update(self):
      for (row,col) in self.board.dict:
         text = self.board.dict[row, col]
         self.buttonsDict[row, col]["text"] = text
         # if button already pressed, then disable it from being pressed again
         if (text != self.board.emptyCell):
            # button state learned from: https://www.tutorialspoint.com/python/tk_button.htm
            self.buttonsDict[row, col]["state"] = "disabled"
         else:
            self.buttonsDict[row, col]["state"] = "normal"
      # if the game is a tie, the user must play again until it beats the virus 
      if (self.board.tieGame()):
         for row, col in self.buttonsDict:
            self.buttonsDict[row, col]["state"] = "disabled"
         root = Tk()
         root.title("Tied Game!")
         root.geometry("+{}+{}".format(902, 350))
         canvas = Canvas(root, width = 300, height = 300)
         canvas.create_rectangle(5, 5, 300, 300, fill = "black", outline = "yellow2", width = 5)
         canvas.create_text(150, 80, text = "Tied Game!", fill = "cyan", font = "Courier 40 bold")
         canvas.create_text(150, 130, text = "Looks like neither you", fill = "lawn green", font = "Courier 20 bold")
         canvas.create_text(150, 150, text = "or the virus won ...", fill = "lawn green", font = "Courier 20 bold")
         canvas.create_text(150, 200, text = "Play again!", fill = "firebrick2", font = "Courier 30 bold")
         canvas.pack()
      winner = self.board.gameOver()
      # if the winner is the player ("X"), then the user gets the next object 
      if (winner == self.board.player):
         for row, col in self.buttonsDict:
            self.buttonsDict[row, col]["state"] = "disabled"
         root = Tk()
         root.title("You Win!")
         root.geometry("+{}+{}".format(902, 350))
         canvas = Canvas(root, width = 300, height = 300)
         canvas.create_rectangle(5, 5, 300, 300, fill = "black", outline = "yellow2", width = 5)
         canvas.create_text(150, 75, text = "Congrats!", fill = "cyan", font = "Courier 40 bold")
         canvas.create_text(150, 110, text = "You survived the virus!", fill = "hot pink", font = "Courier 20 bold")
         canvas.create_text(150, 150, text = "The next object is", fill = "lawn green", font = "Courier 20 bold")
         canvas.create_text(150, 170, text = "the HAT in room 2.", fill = "lawn green", font = "Courier 20 bold")
         canvas.create_text(150, 230, text = "Exit these windows and press", fill = "firebrick2", font = "Courier 15 bold")
         canvas.create_text(150, 250, text = "\'1\' to return to rooms.", fill = "firebrick2", font = "Courier 17 bold")
         canvas.pack()
      # if the winner is the virus ("V"), then the user must play again 
      elif (winner == self.board.virus):
         for row, col in self.buttonsDict:
            self.buttonsDict[row, col]["state"] = "disabled"
         root = Tk()
         root.title("Virus!")
         root.geometry("+{}+{}".format(902, 350))
         canvas = Canvas(root, width = 300, height = 300)
         canvas.create_rectangle(5, 5, 300, 300, fill = "black", outline = "yellow2", width = 5)
         canvas.create_text(150, 70, text = "Oh no!", fill = "cyan", font = "Courier 40 bold")
         canvas.create_text(150, 115, text = "The virus has taken", fill = "lawn green", font = "Courier 22 bold")
         canvas.create_text(150, 140, text = "over your computer!", fill = "lawn green", font = "Courier 22 bold")
         canvas.create_text(150, 200, text = "Play again!", fill = "firebrick2", font = "Courier 30 bold")
         canvas.pack()
      # keeps updating for each cell in the board
      for (row, col) in self.board.dict:
         self.buttonsDict[row, col].update()
         
   # main function to run the above functions
   def mainloop(self):
      self.root.geometry("+{}+{}".format(900, 0))
      self.root.mainloop()
 
DisplayTicTacVirusBoard().mainloop()