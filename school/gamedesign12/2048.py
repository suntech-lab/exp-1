'''
2048 GameDesign12 Project
Eric Liu
30/01/2025
'''

import random

# Create a 4x4 game grid to store the current state of the game board. All values start at 0
board = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]

# Generate a single 2 at a random position
def AddRandomTwo(board):
    emptyCells = [(i, j) for i in range(4) for j in range(4) if board[i][j] == 0]
    if emptyCells:
        i, j = random.choice(emptyCells)
        board[i][j] = 2

def Swap(value1, value2):
    return value2, value1

def MergeRowLeft(row):
    for i in range(3):
        if row[i] == row[i + 1]:
            row[i], row[i + 1] = Swap(row[i], row[i + 1])
            row[i] *= 2
            row[i + 1] = 0

        
    return row

def CompactRow(row):
    for i in range(3):
        if row[i] == 0:
            if row[i + 1] != 0:
                row[i], row[i + 1] = Swap(row[i], row[i + 1])

def PrintBoard(board):
    # Pre: needs the board to be passed in
    # Post: will print the board to the console

    for row in board:
        print('+------' * 4 + '+')
        for cell in row:
            print(f'| {cell if cell != 0 else "":4}', end=' ')
        print('|')
    print('+------' * 4 + '+')


AddRandomTwo(board)
AddRandomTwo(board)
AddRandomTwo(board)
AddRandomTwo(board)
AddRandomTwo(board)
AddRandomTwo(board)
AddRandomTwo(board)
AddRandomTwo(board)
AddRandomTwo(board)
AddRandomTwo(board)
AddRandomTwo(board)
AddRandomTwo(board)

PrintBoard(board)
MergeRowLeft(board[0])
PrintBoard(board)
