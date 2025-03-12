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
lBoard = [[0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0],
         [0, 0, 0, 0]]


def AddRandomTwo(lBoard):

    #pre: needs to know which cells on the lBoard are empty
    #post: fills an empty iCell with a two or a four

    lEmptyCells = [(i, j) for i in range(4)for j in range(4) if lBoard[i][j] == 0]
    
    if lEmptyCells:
        i, j = random.choice(lEmptyCells)        
        iInject = random.randint(1,8) #2048 has a 1/8 chance of putting a four instead of a two
        if iInject < 8:
            lBoard[i][j] = 2
        else:
            lBoard[i][j] = 4

def FlipBoard(lBoard):

    #pre: needs the lBoard
    #post: reverses every lRow in the lBoard so that it is flipped about the y axis

    return[lRow[::-1] for lRow in lBoard]

def TransposeBoard(lBoard):

    #pre: needs the lBoard
    #post: zips the lBoard and puts it back into a list
    #(zip reassigns every first element to every other first element, every second to every second,
    #and so on)
    #map uses the operator passed into the first position on every element in the argument passed in the second

    return list(map(list, zip(*lBoard)))

def MergeRowLeft(lRow):

    #pre: one lRow from the lBoard, and it needs to have something in it
    #post: puts all the non-empty units on the left,
    #combines them, and dMoves them to the left again

    for iNum in lRow:
        if iNum == 0:
            lRow.remove(iNum) #remove one zero from the lRow
            lRow.append(0) #add a zero to the end
        
    for i in range(3):
        if lRow[i] == lRow[i + 1] and lRow[i] != 0:
            lRow[i], lRow[i + 1] = lRow[i + 1], lRow[i]
            lRow[i] *= 2
            lRow[i + 1] = 0

    for iNum in lRow:
        if iNum == 0:
            lRow.remove(iNum)
            lRow.append(0)

    return lRow

def MergeLeft(lBoard):

    #pre: the lBoard
    #post: merges every lRow in the lBoard to the left

    for lRow in lBoard:
        MergeRowLeft(lRow)
    return lBoard

def MergeRight(lBoard):

    #pre: the lBoard
    #post: merges every lRow in the lBoard to the right
    #by flipping it, merging to the left, and flipping it again
    #this is because there is no need to remake an algorithm to
    #specifically merge it to the right

    lBoard = FlipBoard(lBoard)
    MergeLeft(lBoard)
    lBoard = FlipBoard(lBoard)
    return lBoard

def MergeUp(lBoard):

    #pre: the lBoard
    #post: merges every column in the lBoard up
    #by flipping it about it's diagonal/transposing it

    lBoard = TransposeBoard(lBoard)
    MergeLeft(lBoard)
    lBoard = TransposeBoard(lBoard)
    return lBoard

def MergeDown(lBoard):

    #pre: the lBoard
    #post: merges every column in the lBoard down
    #by flipping it about its y axis AND transposing it

    lBoard = TransposeBoard(lBoard)
    lBoard = FlipBoard(lBoard)
    MergeLeft(lBoard)
    lBoard = FlipBoard(lBoard)
    lBoard = TransposeBoard(lBoard)
    return lBoard

def PrintTitle():

    #pre: it needs to be put at the start of the main loop or before cls is used
    #post: prints the title in yellow at the top of the screen

    print(Fore.LIGHTYELLOW_EX + """
 ___ ___ ___ ___ 
|_  |   | | | . |
|  _| | |_  | . |
|___|___| |_|___|
""" + Fore.WHITE)

def DetectWin(lBoard):

    #pre: the lBoard
    #post: detects whether there is a iCell with 2048 inside, and prints
    #"You Win!" in big letters and ends the game if there is

    for lRow in lBoard:
        for iNum in lRow:
            if iNum == 2048:
                print(Fore.GREEN + """
                              __ 
 __ __            _ _ _ _    |  |
|  |  |___ _ _   | | | |_|___|  |
|_   _| . | | |  | | | | |   |__|
  |_| |___|___|  |_____|_|_|_|__|            
""" + Fore.WHITE)
                exit()
                
def DetectLoss(lBoard):

    #pre: the lBoard
    #post: detects if the elements in the lBoard and the elements adjacent to them are similar or not
    #if there are no similar elements adjacent to each other, column or lRow, the game ends and the
    #player loses

    iPossibleMerges = 0

    for lRow in lBoard:
        for iNum in range(3):
            if lRow[iNum] == lRow[iNum + 1]:
                iPossibleMerges += 1
    
    lBoardReference = TransposeBoard(lBoard)

    for lRow in lBoardReference:
        for iNum in range(3):
            if lRow[iNum] == lRow[iNum + 1]:
                iPossibleMerges += 1

    for lRow in lBoard:
        if 0 in lRow:
            return
    
    if iPossibleMerges == 0:
        print(Fore.RED + """
                                    __ 
 __ __            __               |  |
|  |  |___ _ _   |  |   ___ ___ ___|  |
|_   _| . | | |  |  |__| . |_ -| -_|__|
  |_| |___|___|  |_____|___|___|___|__|
""" + Fore.WHITE)
        exit()


def PrintBoard(lBoard):

    #pre: the lBoard
    #post: prints the lBoard onto the terminal in a fancy way

    for lRow in lBoard:
        print('+------' * 4 + '+')
        for iCell in lRow:
            print(f'| {iCell if iCell != 0 else "":4}', end=' ') #fit the number in the cell regardless of space
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
However, if no new dMoves can be made, you lose.
""" + Fore.LIGHTYELLOW_EX + 
"""
If you would like a simple AI to play, input "ai" (not case sensitive) as a sMove when the game asks you to enter a sMovement.
"""
+ Fore.LIGHTGREEN_EX + 
"""
Good luck!
""" + Fore.WHITE)
    
    sPlayGame = input('Would you like to play? (y/n): ')

    if sPlayGame == 'y':
        os.system('cls')
        PrintTitle()
        MainGameLoop(lBoard)
    elif sPlayGame == 'n':
        print('Okay, goodbye.')
        exit()
    else:
        os.system('cls')
        Introduction()

def BestMove(lBoard):

    #pre: looks at the lBoard
    #post: determines the move that gives the most empty tiles on the lBoard

    dMoves = {
        'a': MergeLeft([lRow[:] for lRow in lBoard]),
        'd': MergeRight([lRow[:] for lRow in lBoard]),
        'w': MergeUp([lRow[:] for lRow in lBoard]),
        's': MergeDown([lRow[:] for lRow in lBoard])
    }

    sBestMove = None
    iMaxEmpty = -1

    for sMove, lNewBoard in dMoves.items(): #.items() puts the key-value pairs in the dMoves dictionary in tuples in a list
        iEmptyCells = sum(lRow.count(0) for lRow in lNewBoard)
        if lNewBoard != lBoard and iEmptyCells > iMaxEmpty:
            iMaxEmpty = iEmptyCells
            sBestMove = sMove

    return sBestMove if sBestMove else 'a' #if theres no best sMove then go left

def MainGameLoop(lBoard, bAIMode = False):

    #pre: the lBoard
    #post: dMoves the tiles on the lBoard based on user input

    AddRandomTwo(lBoard)
    while True:
        PrintBoard(lBoard)
        DetectLoss(lBoard)
        DetectWin(lBoard)

        lOldBoard = [lRow[:] for lRow in lBoard]

        if bAIMode:
            sMovement = BestMove(lBoard)
            time.sleep(0.2) #sleep so that the screen doesnt flash too much
            print(f'AI chose: {sMovement.upper()}')
        else:
            sMovement = input("Enter a sMovement (WASD): ").lower()
            if sMovement == 'ai':
                bAIMode = True
                continue
    
        if sMovement == 'a':
            lBoard = MergeLeft(lBoard)
        elif sMovement == 'd':
            lBoard = MergeRight(lBoard)
        elif sMovement == 'w':
            lBoard = MergeUp(lBoard)
        elif sMovement == 's':
            lBoard = MergeDown(lBoard)
        os.system('cls')
        PrintTitle()

        if lBoard != lOldBoard:
            AddRandomTwo(lBoard)

Introduction()
