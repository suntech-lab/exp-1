'''
Game Of Nim GameDesign12
Eric Liu
30/01/2025
'''

import random
import time
import os

#functions
def prRed(redText):
    print("\033[91m {}\033[00m" .format(redText))

def prGreen(greenText):
    print("\033[92m {}\033[00m" .format(greenText))

def prPurple(purpleText):
    print("\033[95m {}\033[00m" .format(purpleText))

def prHighlightText(hightlightedText):
    print("\033[41m {}\033[0m" .format(hightlightedText))


def turnOrder():

    #Pre: needs the random module and needs to be placed at the start of the game
    #Post: determines the turn order of the game

    playerOrComputer = random.randint(0, 1)

    if playerOrComputer == 1:
        print('You go first!')
        
        return True
    
    else:
        print('The computer goes first!')
        
        return False


def makeComputerTakeStones(stonesLeft, pileOfStones, stonesTaken):

    #Pre: needs to know how many stones are left, the pile of stones,
    #how many stones have been taken, and the time module
    #Post: the computer will take stones from the pile

    time.sleep(3)

    stonesComputerWillTake = (stonesLeft % 4) - 1

    #this will make the computer take three stones only if it's not on the winning track
    if stonesComputerWillTake <= 0:
        stonesComputerWillTake = 3

    stonesLeft -= stonesComputerWillTake

    while stonesComputerWillTake > 0:
        pileOfStones[stonesTaken] = ['[STONE]', '       ', '       ']
        
        stonesTaken += 1
        
        stonesComputerWillTake -= 1

    return pileOfStones, stonesLeft, stonesTaken


def stoneTakingPrompt(stonesLeft, pileOfStones, stonesTaken):

    #Pre: needs to know how many stones are left, the pile of stones, and how many stones have been taken
    #Post: will ask the user to take stones from the pile

    stonesUserTakes = 0
    
    try:
        stonesUserTakes = int(input('How many stones do you want to take? (1-3 stones only): '))
        
        if int(stonesUserTakes) < 1 or int(stonesUserTakes) > 3:
            print("Your integer is out of range. Try again.")
        
            stoneTakingPrompt(stonesLeft, pileOfStones, stonesTaken)

    except:
        print("Don't put any letters or special characters. Try again.")
        
        stoneTakingPrompt(stonesLeft, pileOfStones, stonesTaken)

    stonesLeft -= stonesUserTakes

    while stonesUserTakes > 0:
        pileOfStones[stonesTaken] = ['       ', '       ', '[STONE]']
        
        stonesTaken += 1
        
        stonesUserTakes -= 1

    return pileOfStones, stonesLeft, stonesTaken


def showPile(pileOfStones, stonesLeft):

    #Pre: needs to have the pile of stones and know how many stones are left
    #Post: will display the pile of stones and how many stones are left

    for i in pileOfStones:
        print(i[0], i[1], i[2])

    prRed(f'{stonesLeft} stone(s) left.')


def determineWinner(stonesLeft, pileOfStones):

    #Pre: needs to know whose turn it is, how many stones are left, and the pile of stones
    #Post: will determine the winner of the game

    if stonesLeft <= 1:
        if playerTurn: #this will print a message depending on whose turn it is when the game ends
            showPile(pileOfStones, stonesLeft)
            
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
            showPile(pileOfStones, stonesLeft)
            
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

    beginQuery = input('Would you like to play? (y/n): ')
    
    if beginQuery == 'y':
        return True
    
    elif beginQuery == 'n':
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
stonesLeft = random.randint(18, 26)
pileOfStones = []
for i in range(stonesLeft):
    pileOfStones.append(['       ', '[STONE]', '       '])

stonesTaken = 0
playerTurn = turnOrder()
beginGame()

#main loop
while True:

    os.system('cls')

    printTitle()

    determineWinner(stonesLeft, pileOfStones)

    showPile(pileOfStones, stonesLeft)
    
    if not playerTurn:
        prHighlightText('The computer takes a stone or two... or three...')

    if playerTurn:
        pileOfStones, stonesLeft, stonesTaken = stoneTakingPrompt(stonesLeft, pileOfStones, stonesTaken)

    else:
        pileOfStones, stonesLeft, stonesTaken = makeComputerTakeStones(stonesLeft, pileOfStones, stonesTaken)

    playerTurn = not playerTurn