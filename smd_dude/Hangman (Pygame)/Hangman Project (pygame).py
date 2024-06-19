#Anna He
#Pygame Hangman

import pygame, sys, random, time
pygame.init()

SCREENWIDTH, SCREENHEIGHT= 1200, 800
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("Anna He, Hangman Pygame Project")
CLOCK = pygame.time.Clock()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 200)
RED = (255, 0, 0)
SPLASHSCREENMILLISECONDS = 1000
pygame.font.init()

#------------sound effects-----------------
DIRECTORY = 'C:/Users/Eric/Desktop/FunnyPrograms/exp-1/smd_dude/Hangman (Pygame)/'
LOSESOUND = pygame.mixer.Sound(DIRECTORY + "laugh.wav")
WINSOUND = pygame.mixer.Sound(DIRECTORY + "sheesh.wav")
INCORRECTSOUND = pygame.mixer.Sound(DIRECTORY + "shocked.wav")
CORRECTSOUND = pygame.mixer.Sound(DIRECTORY + "good.wav")
INTROSCREENSOUND = pygame.mixer.Sound(DIRECTORY + "start.wav")
BGMUSIC = pygame.mixer.Sound(DIRECTORY + "BgMusic.wav")
BGMUSIC.play()

#Classes go here
class SplashScreen:
    INTROSCREENSOUND.play()
    def __init__(self):
        #pre:
        #post: Initializes splash screen

        self.image = pygame.image.load(DIRECTORY + "Introscreen.jpg")
        self.startTime = pygame.time.get_ticks()
        self.show = True
    
    def draw(self):
        #pre:
        #post: draws splashscreen

        if pygame.time.get_ticks() - self.startTime <= SPLASHSCREENMILLISECONDS:
            SCREEN.blit(self.image, (0, 0))
        else:
            self.show = False

class InstructionsScreen:
    def __init__(self):
        #pre:
        #post:Initializes the InstructionsScreen

        self.image = pygame.image.load(DIRECTORY + "Instructions.jpg")
        self.show = False

    def draw(self):
        #pre:
        #post:Draws the InstructionsScreen

        SCREEN.blit(self.image, (0, 0))

class LoseScreen:
    def __init__(self):
        #pre:
        #post: Initializes the LoseScreen

        self.image = pygame.image.load(DIRECTORY + "Loser.jpg")
        self.show = False

    def draw(self):
        #pre:
        #post: Draws the LoseScreen image on the screen

        SCREEN.blit(self.image, (0, 0))

class WinScreen:
    def __init__(self):
        #pre:
        #post: Initializes the WinScreen with necessary attributes

        self.image = pygame.image.load(DIRECTORY + "Winner.jpg")
        self.show = False

    def draw(self):
        #pre:
        #post: Draws the WinScreen image

        SCREEN.blit(self.image, (0, 0))

class Word:
    def __init__(self, level):
        #pre: needs a string representing the difficulty level
        #post: Chooses a word from the dictionary 

        Words = open(DIRECTORY + "Dictionary.txt").read().split("\n")
        self.SecretWord = random.choice(Words)
        self.iLow = 0
        self.iHigh = 0
        
        if level == "Easy":
            self.iLow = 8 
            self.iHigh = 100
        elif level == "Medium":
            self.iLow = 5
            self.iHigh = 7
        elif level == "Hard":
            self.iLow = 3
            self.iHigh = 4
        
        while len(self.SecretWord) < self.iLow or len(self.SecretWord) > self.iHigh:
            self.SecretWord = random.choice(Words)
        
        self.x = 750
        self.y = 400
        self.LettersGuessed = ""
        self.CorrectLetters = ""
        self.Reveal = ""
        self.letter = ""
        self.rect = (self.x, self.y, len(self.SecretWord) * 30, 30)
        self.font = pygame.font.SysFont("arial", 30)

        #print(self.SecretWord) note: include this to test

    def RevealWord(self):
        #pre:
        #post: Updates the Reveal attribute with revealed letters

        self.Reveal = ""
        for letter in self.SecretWord:
            if letter in self.LettersGuessed:
                self.Reveal += letter

            else:
                self.Reveal += "_"

        return self.Reveal

    def Draw(self):
        #pre:
        #post: Draws the word on the screen

        position = 0
        for character in self.Reveal:
            position += 1
            start_pos = (self.x + position * 30, self.y)
            end_pos = (self.x + position * 30 + 15, self.y)
            dest = (self.x + position * 30 + 2, self.y - 30)

            if character == "_":
                pygame.draw.line(SCREEN, WHITE, start_pos, end_pos)

            else:
                self.letter = self.font.render(character, True, WHITE)
                SCREEN.blit(self.letter, dest)
            

class Hangingman:
    def __init__(self):
        #pre:
        #post: Initializes the Hangingman object

        self.x = 0
        self.y = 0
        self.image = []
        for x in range(0, 10):
            self.image.append(pygame.image.load(DIRECTORY + 'img'+str(x)+".jpg")) #image name is like imgx.png

    def draw(self, errors):
        #pre: needs an integer representing the number of errors
        #post: Draws the hanging man image on the screen

        SCREEN.blit(self.image[errors], (self.x, self.y))

    
class Button:
    def __init__(self, x, y, width, height, text):
        #pre:x: An integer representing the x-coordinate of the button.
        #- y: An integer representing the y-coordinate of the button.
        #- width: An integer representing the width of the button.
        #- height: An integer representing the height of the button.
        #- text: A string representing the text on the button.
        #post: Initializes the Button with necessary attributes

        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(None, 36)
        self.clicked = False

    def draw(self):
        #pre:
        #post: Draws the button on the screen with the specified text
    
        pygame.draw.rect(SCREEN, WHITE, self.rect)
        pygame.draw.rect(SCREEN, BLACK, self.rect, 2)

        TextSurface = self.font.render(self.text, True, BLACK)
        TextRect = TextSurface.get_rect(center=self.rect.center)
        SCREEN.blit(TextSurface, TextRect)
        
    def isClicked(self, mousePos):
        #pre: mousePos: A tuple representing the mouse position (x, y)
        #post: Returns True if the button is clicked, False otherwise

        return self.rect.collidepoint(mousePos)


class LetterButton:
    def __init__(self, letter, position):
        #pre: letter: A string representing the letter on the button.
        #- position: An integer representing the position of the button.
        #post: Initializes the LetterButton

        self.GreenInk = (0, 200, 0)
        self.BlackInk = (0, 0, 0)
        self.BlueInk = (160, 225, 255)
        self.size = 40
        self.name = letter
        if self.name >= "a" and self.name <= 'g':
            self.x = 440 + position*40
            self.y = 640
        elif self.name >= 'h' and self.name <= 'n':
            self.x = 160 + position*40
            self.y = 680
        elif self.name >= 'o' and self.name <= 'u':
            self.x = -120 + position*40
            self.y = 720
        elif self.name >= 'v':
            self.x = -360 + position*40
            self.y = 760
        self.font = pygame.font.SysFont('arial', 40)
        self.mouse = False
        self.show = True
        self.letter = self.font.render(self.name, True, self.BlackInk)
        self.clicked = False  # Add a clicked attribute to track whether the button is clicked

    def draw(self):
        #pre:
        #post: Draws the letter button on the screen based on its state (clicked or not clicked)

        if not self.clicked and self.show:
            if self.mouse:
                pygame.draw.rect(SCREEN, self.BlueInk, (self.x, self.y, self.size, self.size))
            else:
                pygame.draw.rect(SCREEN, self.GreenInk, (self.x, self.y, self.size, self.size))

            SCREEN.blit(self.letter, (self.x + 8, self.y))

    def mouseover(self):
        #pre:
        #post:

        x, y = pygame.mouse.get_pos()
        if self.x <= x < self.x + self.size and self.y < y < self.y + self.size:
            self.mouse = True

        else:
            self.mouse = False

    def click(self):
        #pre:
        #post: Returns the letter if the button is clicked and updates it

        global Alphabet
        x, y = pygame.mouse.get_pos()
        if self.x <= x < self.x + self.size and self.y <= y < self.y + self.size and self.show:
            self.show = False  # Hide the button after it's clicked

            if self.name in Alphabet:
                Alphabetlist = list(Alphabet)  # Convert to list
                Alphabetlist.remove(self.name)  # Remove the clicked letter from qlphabet so it cant be clicked again
                Alphabet = ''.join(Alphabetlist)  # Convert back to string
                
            return self.name


class ScoreBoard:
    def __init__(self):
        #pre:
        #post: Initializes the ScoreBoard

        self.Score = 0
        self.BlackRect = None
        self.font = pygame.font.SysFont('Times New Roman', 50)
    
    def IncreaseScore(self):
        #pre:
        #post: Increases the score attribute by 1

        self.Score +=1
    
    def draw(self, screen):
        #pre: Needs the Pygame screen object
        #post: Draws the score on the screen within a black rectangle

        ScoreText = self.font.render(f"SCORE: {self.Score}", True, RED)
        RectWidth = ScoreText.get_width() + 20
        RectHeight = ScoreText.get_height() + 20
        RectX = (SCREENWIDTH - RectWidth) // 2
        RectY = 10
        self.BlackRect = pygame.Rect(RectX, RectY, RectWidth, RectHeight)
        pygame.draw.rect(screen, BLACK, self.BlackRect)
        screen.blit(ScoreText, (RectX + 10, RectY + 10))


def SelectLevel(): #i kinda removed it from the main game loop or else it would be too long
    #pre: Handles the selection of the game difficulty level
    #post: Returns the selected difficulty level or None if no level is chosen

    if event.type == pygame.MOUSEBUTTONDOWN:
        mousePos = pygame.mouse.get_pos()

        if easyButton.isClicked(mousePos):
            easyButton.clicked = True

            Instructions.show = False
            mediumButton.clicked = False
            hardButton.clicked = False
            return "Easy"
        
        elif mediumButton.isClicked(mousePos):
            mediumButton.clicked = True

            Instructions.show = False
            easyButton.clicked = False
            hardButton.clicked = False
            return "Medium"
        
        elif hardButton.isClicked(mousePos):
            hardButton.clicked = True

            Instructions.show = False
            easyButton.clicked = False
            mediumButton.clicked = False
            return "Hard"

    return None  # Return None if no level is chosen


#-----------Setup Stuffs-------------------
splash = SplashScreen()
Instructions = InstructionsScreen()
showInstructions = False
easyButton = Button(1000, 50, 100, 50, "Easy")
mediumButton = Button(1000, 125, 100, 50, "Medium")
hardButton = Button(1000, 200, 100, 50, "Hard")

Alphabet = "abcdefghijklmnopqrstuvwxyz"
Keyboard = []
index = 0

for letter in Alphabet:
    Keyboard.append(LetterButton(letter, index))
    index += 1

HangMan = Hangingman()
iErrors = 0
WordToGuess = None
LoseScreenShown = False
WinScreenShown = False
losescreen = LoseScreen()
winscreen = WinScreen()
scoreboard = ScoreBoard()

RunGame = True
while RunGame:

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            RunGame = False
            pygame.quit()
            sys.exit()

        elif event.type == pygame.MOUSEBUTTONDOWN:

            for letter in range(len(Keyboard)):
                result = Keyboard[letter].click()
                SelectLevel()

                if iErrors <= 9:

                    if result is not None and WordToGuess is not None:

                        if result not in WordToGuess.SecretWord:
                            iErrors += 1
                            INCORRECTSOUND.play()
                            WordToGuess.LettersGuessed += result

                        if result in WordToGuess.SecretWord:
                            WordToGuess.CorrectLetters += result
                            WordToGuess.LettersGuessed += result
                            scoreboard.IncreaseScore()
                            CORRECTSOUND.play()

                        if iErrors == 9 and not LoseScreenShown:
                            # Draw img9.jpg before displaying the lose screen
                            SCREEN.blit(HangMan.image[9], (HangMan.x, HangMan.y))
                            pygame.display.update()
                            BGMUSIC.stop()
                            LOSESOUND.play()
                            time.sleep(2)  # You can adjust the sleep time if needed
                            LoseScreenShown = True

                        # Check for win condition
                        if set(WordToGuess.CorrectLetters.lower()) == set(WordToGuess.SecretWord.lower()):
                            WinScreenShown = True       
                            SCREEN.blit(HangMan.image[iErrors], (HangMan.x, HangMan.y))
                            pygame.display.update()    
                            time.sleep(2)
                            BGMUSIC.stop()
                            WINSOUND.play()      

                        Keyboard[letter].clicked = True  # Set the clicked attribute to True

    SCREEN.fill((0, 0, 0))

    if splash.show:

        splash.draw()
        Instructions.show = True

    elif Instructions.show:

        Instructions.draw()

        if not easyButton.clicked:
            easyButton.draw()

        if not mediumButton.clicked:
            mediumButton.draw()

        if not hardButton.clicked:
            hardButton.draw()

    if easyButton.clicked or mediumButton.clicked or hardButton.clicked and WordToGuess is not None:

        HangMan.draw(iErrors)

        if iErrors < 10:

            for letter in range(len(Keyboard)):

                Keyboard[letter].draw()
                Keyboard[letter].mouseover()

    if WordToGuess is None:

        if easyButton.clicked:
            WordToGuess = Word("Easy")

        elif mediumButton.clicked:
            WordToGuess = Word("Medium")

        elif hardButton.clicked:
            WordToGuess = Word("Hard")

    if WordToGuess is not None:

        WordToGuess.RevealWord()
        WordToGuess.Draw()

    if WinScreenShown:
        winscreen.draw()

    if LoseScreenShown:
        losescreen.draw()

    if WordToGuess is not None: 
        scoreboard.draw(SCREEN)
        
    pygame.display.update()
    CLOCK.tick(30)