'''
Anna He
Hangman Project (Text)
5/12/2024
'''
import random, os, time, pygame
from HMGraphics import HangingMan

# Sound
pygame.init()
pygame.mixer.init()

# Splash Screen
def IntroScreen():
    #pre: nothing
    #post: prints the hangman 'logo', instructions, the prompt to start, and plays a sound
    os.system("CLS")
    IntroSound = pygame.mixer.Sound("start.wav")
    IntroSound.play()
    print('''
  _   _                                         
 | | | | __ _ _ __   __ _ _ __ ___   __ _ _ __  
 | |_| |/ _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
 |  _  | (_| | | | | (_| | | | | | | (_| | | | |
 |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    |___/                       ''')
    
    time.sleep(3)
    os.system('CLS')

    #Instructions Screen
    print("Instructions:\n1. Selecting a difficulty: Easy, Medium, Hard\n2. Guess the word letter by letter\n3. Underscores stand for letters that have not yet been guessed\n4. Correctly guessed letters will replace the underscores\n5. You have 9 tries in total")
    input("\nPress enter when you are ready!: ")
    os.system("CLS")

def WinningScreen(iScore):
    #pre: fnreveal's final score
    #post: prints win screen
    os.system('CLS')
    IntroSound = pygame.mixer.Sound("sheesh.wav")
    IntroSound.play ()
    print('''
 __   __           __        ___       _ 
 \ \ / /__  _   _  \ \      / (_)_ __ | |
  \ V / _ \| | | |  \ \ /\ / /| | '_ \| |
   | | (_) | |_| |   \ V  V / | | | | |_|
   |_|\___/ \__,_|    \_/\_/  |_|_| |_(_)
                                          ''')

    time.sleep(3)
    os.system("CLS")
    print("Your final score is:", iScore, ".\n")
    print("You win!!")

def fnLoseScreen(iScore):
    #pre: fnreveal's final score
    #post: prints lose screen
    os.system("CLS")
    IntroSound = pygame.mixer.Sound("laugh.wav")
    IntroSound.play ()
    time.sleep(2.5)    
    print('''
 __   __            ____             _        
 \ \ / /__  _   _  / ___| _   _  ___| | __    
  \ V / _ \| | | | \___ \| | | |/ __| |/ /    
   | | (_) | |_| |  ___) | |_| | (__|   < _ _ 
   |_|\___/ \__,_| |____/ \__,_|\___|_|\_(_|_)
                                                ''')
    time.sleep(3)
    os.system("CLS")
    print('The word was "' + ChosenWord + '".\nYour score is:', iScore, "\n")

# Gamemode
def GameMode(difficulty, words): 
    #pre: difficulty result from prompt and dictionary
    #post: gives a word that is suitable for the difficulty level
    iLow = 0
    iHigh = 0
    sAnswer = ''

    if difficulty == 'easy':
        iLow = 10
        iHigh = 69420
    elif difficulty == 'medium':
        iLow = 6
        iHigh = 9
    elif difficulty == 'hard':
        iLow = 1
        iHigh = 5

    sValidWord = '' 

    while len(sAnswer) < iLow or len(sAnswer) > iHigh:
        sAnswer = random.choice(words)
        if len(sAnswer) >= iLow and len(sAnswer) <= iHigh:
            sValidWord = sAnswer
    return sValidWord

def fnReveal(WordToGuess):
    #pre: suitable word from gamemode function
    #post: hosts the game, keeps track of score and such, main loop here, sees if the player won or not
    iErrors = 0
    sLetterGuessed = '' 
    iMaxAttempts = 9
    iScore = 0
    while iErrors < iMaxAttempts:
        os.system("CLS")
        print(HangingMan[iErrors])
        sReveal = ''

        for char in WordToGuess:
            if char in sLetterGuessed:
                sReveal += char + " "
            else:
                sReveal += "_ "
        print(sReveal)
        
        print("Already Guessed Letters:", ', '.join(sLetterGuessed))

        print("Your Score Is:", iScore) 

        # Player Won
        if sReveal.replace(' ', '') == WordToGuess:
            time.sleep(2.2)
            WinningScreen(iScore) 
            break  

        sGuessedLetter = input("Enter a letter to guess: ").lower()
        if sGuessedLetter in sLetterGuessed:
            IntroSound = pygame.mixer.Sound("shocked.wav")
            IntroSound.play()
            print("You guessed", sGuessedLetter, "already...")  
        else:
            IntroSound = pygame.mixer.Sound("good.wav")
            IntroSound.play()
            sLetterGuessed += sGuessedLetter 
            if sGuessedLetter not in WordToGuess:
                iErrors += 1
                IntroSound = pygame.mixer.Sound("shocked.wav")
                IntroSound.play ()
            else:
                iScore += 1 

    if iErrors == iMaxAttempts:
        time.sleep(0.5) 
        fnLoseScreen(iScore)

IntroScreen()
words = open("C:/Users/annah/OneDrive/Desktop/Programming 11/Hangman (Text)/Dictionary.txt").read().split("\n") # Just writing Dictionary.txt did not work on my pc so I had to change it to this
sGameMode = '' 

gamemodes = ['easy','medium','hard']
while sGameMode not in gamemodes:
    sGameMode = input("Which game mode do you want to play (easy/medium/hard)? ").lower() 
    IntroSound = pygame.mixer.Sound("ugh.wav")
    IntroSound.play ()
    if sGameMode not in gamemodes: 
        print("Not a valid choice!")
        time.sleep(1) 
        os.system("CLS")

ChosenWord = GameMode(sGameMode, words) 
fnReveal(ChosenWord)