'''
2048 GameDesign12 Project
Eric Liu
30/01/2025
'''

import random
import os
from colorama import Fore
import time

#create a 4x4 grid
board = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]


def AddRandomTwo(board):

    #pre: needs to know which cells on the board are empty
    #post: fills an empty cell with a two or a four

    emptyCells = [(i, j) for i in range(4)for j in range(4) if board[i][j] == 0]
    
    if emptyCells:
        i, j = random.choice(emptyCells)        
        inject = random.randint(1,8) #2048 has a 1/8 chance of putting a four instead of a two
        if inject < 8:
            board[i][j] = 2
        else:
            board[i][j] = 4

def FlipBoard(board):

    #pre: needs the board
    #post: reverses every row in the board so that it is flipped about the y axis

    return[row[::-1] for row in board]

def TransposeBoard(board):

    #pre: needs the board
    #post: zips the board and puts it back into a list
    #(zip reassigns every first element to every other first element, every second to every second,
    #and so on)
    #map uses the operator passed into the first position on every element in the argument passed in the second

    return list(map(list, zip(*board)))

def MergeRowLeft(row):

    #pre: one row from the board, and it needs to have something in it
    #post: puts all the non-empty units on the left,
    #combines them, and moves them to the left again

    for num in row:
        if num == 0:
            row.remove(num) #remove one zero from the row
            row.append(0) #add a zero to the end
        
    for i in range(3):
        if row[i] == row[i + 1] and row[i] != 0:
            row[i], row[i + 1] = row[i + 1], row[i]
            row[i] *= 2
            row[i + 1] = 0

    for num in row:
        if num == 0:
            row.remove(num)
            row.append(0)

    return row

def MergeLeft(board):

    #pre: the board
    #post: merges every row in the board to the left

    for row in board:
        MergeRowLeft(row)
    return board

def MergeRight(board):

    #pre: the board
    #post: merges every row in the board to the right
    #by flipping it, merging to the left, and flipping it again
    #this is because there is no need to remake an algorithm to
    #specifically merge it to the right

    board = FlipBoard(board)
    MergeLeft(board)
    board = FlipBoard(board)
    return board

def MergeUp(board):

    #pre: the board
    #post: merges every column in the board up
    #by flipping it about it's diagonal/transposing it

    board = TransposeBoard(board)
    MergeLeft(board)
    board = TransposeBoard(board)
    return board

def MergeDown(board):

    #pre: the board
    #post: merges every column in the board down
    #by flipping it about its y axis AND transposing it

    board = TransposeBoard(board)
    board = FlipBoard(board)
    MergeLeft(board)
    board = FlipBoard(board)
    board = TransposeBoard(board)
    return board

def PrintTitle():

    #pre: it needs to be put at the start of the main loop or before cls is used
    #post: prints the title in yellow at the top of the screen

    print(Fore.LIGHTYELLOW_EX + """
 ___ ___ ___ ___ 
|_  |   | | | . |
|  _| | |_  | . |
|___|___| |_|___|
""" + Fore.WHITE)

def DetectWin(board):

    #pre: the board
    #post: detects whether there is a cell with 2048 inside, and prints
    #"You Win!" in big letters and ends the game if there is

    for row in board:
        for num in row:
            if num == 2048:
                print(Fore.GREEN + """
                              __ 
 __ __            _ _ _ _    |  |
|  |  |___ _ _   | | | |_|___|  |
|_   _| . | | |  | | | | |   |__|
  |_| |___|___|  |_____|_|_|_|__|            
""" + Fore.WHITE)
                exit()
                
def DetectLoss(board):

    #pre: the board
    #post: detects if the elements in the board and the elements adjacent to them are similar or not
    #if there are no similar elements adjacent to each other, column or row, the game ends and the
    #player loses

    possibleMerges = 0

    for row in board:
        for num in range(3):
            if row[num] == row[num + 1]:
                possibleMerges += 1
    
    tBoardReference = TransposeBoard(board)

    for row in tBoardReference:
        for num in range(3):
            if row[num] == row[num + 1]:
                possibleMerges += 1

    for row in board:
        if 0 in row:
            return
    
    if possibleMerges == 0:
        print(Fore.RED + """
                                    __ 
 __ __            __               |  |
|  |  |___ _ _   |  |   ___ ___ ___|  |
|_   _| . | | |  |  |__| . |_ -| -_|__|
  |_| |___|___|  |_____|___|___|___|__|
""" + Fore.WHITE)
        exit()


def PrintBoard(board):

    #pre: the board
    #post: prints the board onto the terminal in a fancy way

    for row in board:
        print('+------' * 4 + '+')
        for cell in row:
            print(f'| {cell if cell != 0 else "":4}', end=' ') #fit the number in the cell regardless of space
        print('|')
    print('+------' * 4 + '+')

def Introduction():

    #pre: it needs to be put at the beginning
    #post: it introduces the player to the game and asks the player if they want to play

    PrintTitle()
    print(Fore.LIGHTGREEN_EX + 
"""
Welcome to 2048!
The goal of the game is to add similar numbers together, starting from 2, until you reach 2048.
However, if no new moves can be made, you lose.
""" + Fore.LIGHTYELLOW_EX + 
"""
If you would like a simple AI to play, input "ai" (not case sensitive) as a move when the game asks you to enter a movement.
"""
+ Fore.LIGHTGREEN_EX + 
"""
Good luck!
""" + Fore.WHITE)
    
    playGame = input('Would you like to play? (y/n): ')

    if playGame == 'y':
        os.system('cls')
        PrintTitle()
        MainGameLoop(board)
    elif playGame == 'n':
        print('Okay, goodbye.')
        exit()
    else:
        os.system('cls')
        Introduction()

def BestMove(board):

    #pre: looks at the board
    #post: determines the move that gives the most empty tiles on the board

    moves = {
        'a': MergeLeft([row[:] for row in board]),
        'd': MergeRight([row[:] for row in board]),
        'w': MergeUp([row[:] for row in board]),
        's': MergeDown([row[:] for row in board])
    }

    bestMove = None
    maxEmpty = -1

    for move, new_board in moves.items(): #.items() puts the key-value pairs in the moves dictionary in tuples in a list
        empty_cells = sum(row.count(0) for row in new_board)
        if new_board != board and empty_cells > maxEmpty:
            maxEmpty = empty_cells
            bestMove = move

    return bestMove if bestMove else 'a' #if theres no best move then go left

def MainGameLoop(board, AIMode = False):

    #pre: the board
    #post: moves the tiles on the board based on user input

    AddRandomTwo(board)
    while True:
        PrintBoard(board)
        DetectLoss(board)
        DetectWin(board)

        oldBoard = [row[:] for row in board]

        if AIMode:
            movement = BestMove(board)
            time.sleep(0.2) #sleep so that the screen doesnt flash too much
            print(f'AI chose: {movement.upper()}')
        else:
            movement = input("Enter a movement (WASD): ").lower()
            if movement == 'ai':
                AIMode = True
                continue
    
        if movement == 'a':
            board = MergeLeft(board)
        elif movement == 'd':
            board = MergeRight(board)
        elif movement == 'w':
            board = MergeUp(board)
        elif movement == 's':
            board = MergeDown(board)
        os.system('cls')
        PrintTitle()

        if board != oldBoard:
            AddRandomTwo(board)

Introduction()
