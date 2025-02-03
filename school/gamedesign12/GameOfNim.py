'''
Game Of Nim GameDesign12
Eric Liu
30/01/2025
'''
#imports
import random
import time

#nobody wants to play a game where the turn order is the same EVERY TIME
def turnOrder():

    #coin flip to determine who goes first
    playerOrComputer = random.randint(0, 1)

    if playerOrComputer == 1:
        print('You go first!')
        return True
    
    else:
        print('The computer goes first!')
        return False

#the computer needs to take 1-3 stones to progress the game
def stonesComputerWillTake(stonesLeft, pileOfStones, stonesTaken):

    #this is here to make sure the game doesn't flash when the computer takes stones
    time.sleep(2)

    #this is the computer's strategy to win the game
    stonesComputerTakes = (stonesLeft % 4) - 1

    #this will make the computer take one stone only if it's not on the winning track
    if stonesComputerTakes <= 0:
        stonesComputerTakes = 3

    #this tells the program how many stones are available for taking
    stonesLeft -= stonesComputerTakes

    #the pile needs to update when the computer takes stones
    while stonesComputerTakes > 0:
        pileOfStones[stonesTaken] = ['[STONE]', '       ', '       ']
        stonesTaken += 1
        stonesComputerTakes -= 1

    return pileOfStones, stonesLeft, stonesTaken

#the user needs to take 1-3 stones to progress the game
def stoneTakingPrompt(stonesLeft, pileOfStones, stonesTaken):
    stonesUserTakes = 0
    
    #stonesUserTakes starts at zero, so this loop will run at least once
    while stonesUserTakes < 1 or stonesUserTakes > 3:

        #this try except block is here to catch any strings or special characters that the user might input
        try:
            stonesUserTakes = int(input('How many stones do you want to take? (1-3 stones only): '))

            #if the user's input is out of range, this will tell the user to try again
            if int(stonesUserTakes) < 1 or int(stonesUserTakes) > 3:
                print("Your integer is out of range. Try again.")

        except:
            print("Don't put any letters or special characters. Try again.")


    #this tells the program how many stones are available for taking
    stonesLeft -= stonesUserTakes

    #this updates the pile when the user takes stones
    while stonesUserTakes > 0:
        pileOfStones[stonesTaken] = ['       ', '       ', '[STONE]']
        stonesTaken += 1
        stonesUserTakes -= 1

    #this returns all the needed variables for the game to continue
    return pileOfStones, stonesLeft, stonesTaken

#this is what actually prints the pile of stones and tells the user how many stones are left
def showPile(pileOfStones, stonesLeft):
    for i in pileOfStones:
        print(i[0], i[1], i[2])

    print(stonesLeft, 'stone(s) left.')

#this determines if the player has lost
def determineWinner(stonesLeft, pileOfStones):
    if stonesLeft <= 1:
        
        #this will print a message depending on whose turn it is when the game ends
        if playerTurn:
            showPile(pileOfStones, stonesLeft)
            print("""
.    __                         __.
.   / /   ____  ________  _____/ /.
.  / /   / __ \/ ___/ _ \/ ___/ / .
. / /___/ /_/ (__  )  __/ /  /_/  .
./_____/\____/____/\___/_/  (_)   .
                  """)
            exit()
        
        else:
            showPile(pileOfStones, stonesLeft)
            print("""
.__  __                        _       __.
.\ \/ /___  __  __   _      __(_)___  / /.
. \  / __ \/ / / /  | | /| / / / __ \/ / .
. / / /_/ / /_/ /   | |/ |/ / / / / /_/  .
./_/\____/\____/    |__/|__/_/_/ /_(_)   .
                  """)
            exit()
    
#this makes sure the game doesn't jumpscare the user when they run the program
def beginGame():
    beginQuery = input('Would you like to play? (y/n): ')
    
    #this if else block will handle both easier than a while loop because there's only two options
    if beginQuery == 'y':
        return True
    
    elif beginQuery == 'n':
        print('Goodbye!')
        exit()
    
    else:
        print('Invalid input. Try again.')
        beginGame()

#initialize how many stones are in the pile
stonesLeft = random.randint(18, 26)

#initialize the pile of stones
pileOfStones = []

for i in range(stonesLeft):
    pileOfStones.append(['       ', '[STONE]', '       '])

stonesTaken = 0

#introduce the player to the game
print("""
.   ______                        ____  ____   _   ___         .
.  / ____/___ _____ ___  ___     / __ \/ __/  / | / (_)___ ___ .
. / / __/ __ `/ __ `__ \/ _ \   / / / / /_   /  |/ / / __ `__ \.
./ /_/ / /_/ / / / / / /  __/  / /_/ / __/  / /|  / / / / / / /.
.\____/\__,_/_/ /_/ /_/\___/   \____/_/    /_/ |_/_/_/ /_/ /_/ .
      """)
print("""
Welcome to the Game of Nim! The rules are simple:
Take turns taking 1-3 stones from the pile
The player who takes the last stone loses! Good luck!
""")

#ask the user to play the game
beginGame()

#turnOrder() returns true or false on a coin flip, telling the program 
playerTurn = turnOrder()

#main loop
while True:

    #determineWinner() will end the game if the player has lost, so there isn't a turn after the game ends
    determineWinner(stonesLeft, pileOfStones)

    #showPile() is here because it's the first thing the user sees when it's their turn or the computer's turn
    showPile(pileOfStones, stonesLeft)

    #this switches depending on playerTurn
    if playerTurn:
        pileOfStones, stonesLeft, stonesTaken = stoneTakingPrompt(stonesLeft, pileOfStones, stonesTaken)

    else:
        pileOfStones, stonesLeft, stonesTaken = stonesComputerWillTake(stonesLeft, pileOfStones, stonesTaken)
        print('The computer takes a stone or two... or three...')

    #switch the actual turn
    playerTurn = not playerTurn