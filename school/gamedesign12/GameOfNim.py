'''
Game Of Nim GameDesign12
Eric Liu
30/01/2025

NOTE: the game is designed to be played in a terminal that is
very tall so you can see the whole pile of stones, otherwise,
the terminal may not be fully cleared before the next turn.
'''

import random
import time
import os

#functions
def prRed(sRedText):
    print("\033[91m {}\033[00m" .format(sRedText))

def prGreen(sGreenText):
    print("\033[92m {}\033[00m" .format(sGreenText))

def prPurple(sPurpleText):
    print("\033[95m {}\033[00m" .format(sPurpleText))

def prHighlightText(sHightlightedText):
    print("\033[41m {}\033[0m" .format(sHightlightedText))


def turnOrder():

    #Pre: needs the random module and needs to be placed at the start of the game
    #Post: determines the turn order of the game

    iPlayerOrComputer = random.randint(0, 1)

    if iPlayerOrComputer == 1:
        print('You go first!')
        
        return True
    
    else:
        print('The computer goes first!')
        
        return False


def makeComputerTakeStones(iStonesLeft, lPileOfStones, iStonesTaken):

    #Pre: needs to know how many stones are left, the pile of stones,
    #how many stones have been taken, and the time module
    #Post: the computer will take stones from the pile

    time.sleep(3)

    iStonesComputerWillTake = (iStonesLeft % 4) - 1

    #this will make the computer take three stones only if it's not on the winning track
    if iStonesComputerWillTake <= 0:
        iStonesComputerWillTake = 3

    iStonesLeft -= iStonesComputerWillTake

    while iStonesComputerWillTake > 0:
        lPileOfStones[iStonesTaken] = ['[STONE]', '       ', '       ']
        
        iStonesTaken += 1
        
        iStonesComputerWillTake -= 1

    return lPileOfStones, iStonesLeft, iStonesTaken


def stoneTakingPrompt(iStonesLeft, lPileOfStones, iStonesTaken):

    #Pre: needs to know how many stones are left, the pile of stones, and how many stones have been taken
    #Post: will ask the user to take stones from the pile

    iStonesUserTakes = 0
    
    try:
        iStonesUserTakes = int(input('How many stones do you want to take? (1-3 stones only): '))
        
        if int(iStonesUserTakes) < 1 or int(iStonesUserTakes) > 3:
            print("Your integer is out of range. Try again.")
        
            stoneTakingPrompt(iStonesLeft, lPileOfStones, iStonesTaken)

    except:
        print("Don't put any letters or special characters. Try again.")
        
        stoneTakingPrompt(iStonesLeft, lPileOfStones, iStonesTaken)

    iStonesLeft -= iStonesUserTakes

    while iStonesUserTakes > 0:
        lPileOfStones[iStonesTaken] = ['       ', '       ', '[STONE]']
        
        iStonesTaken += 1
        
        iStonesUserTakes -= 1

    return lPileOfStones, iStonesLeft, iStonesTaken


def showPile(lPileOfStones, iStonesLeft):

    #Pre: needs to have the pile of stones and know how many stones are left
    #Post: will display the pile of stones and how many stones are left

    for i in lPileOfStones:
        print(i[0], i[1], i[2])

    prRed(f'{iStonesLeft} stone(s) left.')


def determineWinner(iStonesLeft, lPileOfStones):

    #Pre: needs to know whose turn it is, how many stones are left, and the pile of stones
    #Post: will determine the winner of the game

    if iStonesLeft <= 1:
        if bPlayerTurn: #this will print a message depending on whose turn it is when the game ends
            showPile(lPileOfStones, iStonesLeft)
            
            prRed("""
     You take the last stone...
.    __                         __.
.   / /   ____  ________  _____/ /.
.  / /   / __ \/ ___/ _ \/ ___/ / .
. / /___/ /_/ (__  )  __/ /  /_/  .
./_____/\____/____/\___/_/  (_)   .
                  """)
            
            exit()
        
        else:
            showPile(lPileOfStones, iStonesLeft)
            
            prGreen("""
   The computer takes the last stone...
.__  __                        _       __.
.\ \/ /___  __  __   _      __(_)___  / /.
. \  / __ \/ / / /  | | /| / / / __ \/ / .
. / / /_/ / /_/ /   | |/ |/ / / / / /_/  .
./_/\____/\____/    |__/|__/_/_/ /_(_)   .
                  """)
            
            exit()
    

def beginGame():

    #Pre: it doesn't need anything except being put at the initial start of the game
    #Post: will start the game if the player wants to play, otherwise exits the program

    sBeginQuery = input('Would you like to play? (y/n): ')
    
    if sBeginQuery == 'y':
        return True
    
    elif sBeginQuery == 'n':
        print('Goodbye!')
        
        exit()
    
    else:
        print('Invalid input. Try again.')
        
        beginGame()
    

def printTitle():
    
    #Pre: doesn't need anything
    #Post: will print the title of the game

    prPurple("""
.   ______                        ____  ____   _   ___         .
.  / ____/___ _____ ___  ___     / __ \/ __/  / | / (_)___ ___ .
. / / __/ __ `/ __ `__ \/ _ \   / / / / /_   /  |/ / / __ `__ \.
./ /_/ / /_/ / / / / / /  __/  / /_/ / __/  / /|  / / / / / / /.
.\____/\__,_/_/ /_/ /_/\___/   \____/_/    /_/ |_/_/_/ /_/ /_/ .
          
   AI      vs     YOU
      """)


#initializing the game
printTitle()
prGreen("""
Welcome to the Game of Nim! The rules are simple:
Take turns taking 1-3 stones from the pile
The player who takes the last stone loses! Good luck!
(make sure your terminal really tall so you can see the whole pile)
""")
iStonesLeft = random.randint(22, 32)
lPileOfStones = []
for i in range(iStonesLeft):
    lPileOfStones.append(['       ', '[STONE]', '       '])

iStonesTaken = 0
bPlayerTurn = turnOrder()
beginGame()

#main loop
while True:

    os.system('cls')

    printTitle()

    determineWinner(iStonesLeft, lPileOfStones)

    showPile(lPileOfStones, iStonesLeft)
    
    if not bPlayerTurn:
        prHighlightText('The computer takes a stone or two... or three...')

    if bPlayerTurn:
        lPileOfStones, iStonesLeft, iStonesTaken = stoneTakingPrompt(iStonesLeft, lPileOfStones, iStonesTaken)

    else:
        lPileOfStones, iStonesLeft, iStonesTaken = makeComputerTakeStones(iStonesLeft, lPileOfStones, iStonesTaken)

    bPlayerTurn = not bPlayerTurn