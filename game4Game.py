####################################
# Jessica Meng, jmeng1, Section B
# Lights Out
# 15-112 Term Project 
# game4
# this is the fourth and final game in the series of puzzles the user has to solve
# uses messagebox for pop up's 
# tkinter "messagebox" feature learned from: https://pythonspot.com/tk-message-box/ (used this to write code)
# tkinter "Label" feature learned from: http://effbot.org/tkinterbook/label.htm (used this to write code)
# tkinter "Frame" feature learned from: http://effbot.org/tkinterbook/frame.htm (used this to write code)
# tkinter "grid" feature learned from: http://effbot.org/tkinterbook/grid.htm (used this to write code)
# this game is called "CyberBot", where the user must play the computer, who will be "CyberBot" (uses AI). The goal of the game is to have more blue squares than green squares. The squares change color based on where they are placed and also change the squares surrounding the clicked square to that color. 
# "Greedy algorithm" learned from: https://en.wikipedia.org/wiki/Greedy_algorithm - makes the choice that seems to be the best at the moment (finding a cell that has the most blue neighbors), but may not be the best in the future (further into the game)
# has some randomness so the game is not impossible 
# all colors used from: https://wiki.tcl.tk/37701
####################################

####################################
# imports
# necessary to run program
#################################### 

from tkinter import *
from tkinter import messagebox
import random 
import time
import sys
import os

####################################
# functions
#################################### 

# creates the empty board in the beginning
rows = 10
cols = 10
board = [[None]*10 for cell in range(rows)]
cross = [[None]*10 for cell in range(rows)]
count = 0
message = False
initialCyberBotCell = 0
emptyCellCount = 100
greenCellCount = 0
blueCellCount = 0
previousCellX = 0
previousCellY = 0

root = Tk()
root.title("CyberBot")

# checks the current board and cells and sees if there is a winner if there are no more empty cells
def updateBoard():
    # uses global variables because emptyCellCount, greenCellCount, and blueCellCount get called on in other functions and throughout the code
    global emptyCellCount
    global greenCellCount
    global blueCellCount
    emptyCellCount = 100
    greenCellCount = 0
    blueCellCount = 0
    # changes the respective cell count if a cell is a certain color 
    for i, row in enumerate(board):
        for j, column in enumerate(row):
            if (board[i][j] == "green"):
                greenCellCount += 1
                emptyCellCount -= 1
            elif (board[i][j] == "blue"):
                blueCellCount += 1
                emptyCellCount -= 1
    # if there are no more empty cells, checks to see if there is a winner or a tie
    if (emptyCellCount == 0):
        # if there are more green cells than blue cells, then the winner is "CyberBot"
        # if there are more blue cells than green cells, then the winner is the user 
        if (blueCellCount < greenCellCount):
            winner = "CyberBot"
        elif (greenCellCount < blueCellCount):
            winner = "Player"
        else:
            winner = "Tie"
        if (winner != "Tie"):
            messagebox.showinfo("Game Over!", winner + " wins!")
            # if user is winner, the user gets the location of the next object in "Lights Out"
            if (winner == "Player"):
                messagebox.showinfo("Congrats!", "The next object is the SYMBOLS in room 2.")
                root.quit()
            elif (winner == "CyberBot"):
                messagebox.showinfo("Good Try!", "This game is hard, so here's the next object in reward for your effort: the SYMBOLS in room 2.")
                root.quit()
                
        else:
            messagebox.showinfo("Game Over!", "Tied Game! This game is hard, so here's the next object in reward for your effort: the SYMBOLS in room 2.")
            root.quit()

# function for when a cell is clicked 
def clickedCell(row, col, event):
    # uses global variables because these variables get called on in other functions and throughout the code
    global message
    message = True
    global count
    global greenCellCount
    global blueCellCount
    # total number of cells is 100
    numCells = 100
    if (count < numCells):
        if (board[row][col] == None):
            # if count is even, then it is the "CyberBot"'s turn; if count is odd, then it is the user's turn
            if (count % 2 == 0):
                color = "green"
                user = "CyberBot"
                otherColor = "blue"
                otherUser = "Player"
            else:
                color = "blue" 
                user = "Player"
                otherColor = "green"
                otherUser = "CyberBot"
            event.widget.config(bg = color)
            board[row][col] = color
            # changes the surrounding cells to the clicked cell to the color of the current turn 
            start = -1
            end = 2
            for cell1 in range(start, end):
                for cell2 in range(start, end):
                    try:
                        if (board[row + cell1][col + cell2] == otherColor):
                            board[row + cell1][col + cell2] = color
                    except IndexError:
                        break
            count += 1
            global gameFrame
            gameFrame.destroy()
            main()
        # if cell is alreay occupied, a message pops up to let user know
        else:
            messagebox.showinfo("Filled Cell!", "This cell is already occupied! Please find an empty cell.")

# for "CyberBot" to find the next best cell to beat user aka for the computer to find the cell that has the most blue cells surrounding it so it can change them to green
def findBestCell():
    # max starts at 0 
    maxBlueNeighbors = 0
    maxX = 0
    maxY = 0
    # finds the number of blue neighbors for each empty cell (checks the possible cells for "CyberBot" to move to)
    for curRow, row in enumerate(board):
        for curCol, column in enumerate(row):
            if (board[curRow][curCol] == None):
                curBlueNeighbors = 0;
                start = -1
                end = 2
                for i in range(start, end):
                    for j in range(start, end):
                        try:
                            if (board[curRow + i][curCol + j] == "blue"):
                                curBlueNeighbors += 1
                        except IndexError:
                            break
                # if current number of blue neighbors around that cell is greater than the current max number of blue neighbors
                # set the max number of blue neighbors to current number of blue neighbors and the maxX and maxY to current row and current column
                if (curBlueNeighbors >= maxBlueNeighbors):
                    maxBlueNeighbors = curBlueNeighbors
                    maxX = curRow
                    maxY = curCol
    # returns the best X position and the best Y position (row and column)
    return (maxX, maxY)

# main function
def main():
    global gameFrame
    # tkinter "Frame" feature learned from: http://effbot.org/tkinterbook/frame.htm
    gameFrame = Frame(root)
    gameFrame.pack()
    global count
    global initialCyberBotCell
    global previousCellX
    global previousCellY
    # if the initialCyberBotCell is 0 (empty), then "CyberBot" makes its initial move
    if (initialCyberBotCell == 0):
        # CyberBot Starts in the an initial position of the sixth row and sixth column
        board[5][5] = 'green'
        cross[5][5] = 'C'
        cross[previousCellX][previousCellY] = None
        previousCellX = 5
        previousCellY = 5
        count += 1
        initialCyberBotCell = 1
        updateBoard()
        # to display who's turn it is, and the score
        root.wm_title("Player's Turn, Score: Player - " + str(blueCellCount) + ", CyberBot - " + str(greenCellCount))
    elif (count % 2 == 0):
        # use greedy method to find a good square: https://en.wikipedia.org/wiki/Greedy_algorithm
        (x, y) = findBestCell()
        board[x][y] = 'green'
        cross[x][y] = 'C'
        # for testing/debugging row, col position
        #print("x = ", x, "   y = ", y)
        cross[previousCellX][previousCellY] = None
        previousCellX = x
        previousCellY = y
        # to change the color of the surrounding cells of the current cell 
        # uses the try, except method - idea from 15-112 "Exceptions" notes: https://www.cs.cmu.edu/~112/notes/notes-exceptions.html
        start = -1
        end = 2
        for i in range(start, end):
            for j in range(start, end):
                try:
                    # if the surrounding cells are of the other color, change it to the current color 
                    # e.g. if the surrounding cells are blue, and it's "CyberBot"'s turn, then change them to green
                    if (board[x + i][y + j] == 'blue'):
                        board[x + i][y + j] = 'green'
                except IndexError:
                    break
        count += 1
        updateBoard()
        # to display who's turn it is, and the score
        root.wm_title("Player's Turn, Score: Player - " + str(blueCellCount) + ", CyberBot - " + str(greenCellCount))
    for i, row in enumerate(board):
        for j, column in enumerate(row):
            # empty cells are a grey color 
            if (board[i][j] == None):
                color = "azure3"
            else: 
                color = board[i][j]
            if (cross[i][j] == None):
                L = Label(gameFrame, text = "    ", bg = color)
            # to track the CyberBot's current position with a "C"
            else:
                L = Label(gameFrame, text = " C ", bg = color)
            # creates the grid and each cell (each cell is a button)
            L.grid(row = i, column = j, padx = '8', pady = '8')
            L.bind('<Button-1>', lambda e, row = i, col = j: clickedCell(row, col, e))
    
####################################
# run function 
# runs the above functions
####################################

def runGame4Game():
    main()
    root.geometry("+{}+{}".format(825, 450))
    root.mainloop()
    
runGame4Game()