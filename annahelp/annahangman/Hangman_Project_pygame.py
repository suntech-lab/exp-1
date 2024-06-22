'''
Anna He
Hangman Pygame Version
6/20/2024
'''
import pygame, sys, random, time
pygame.init()

SCREENWIDTH, SCREENHEIGHT= 1200, 800
SCREEN = pygame.display.set_mode((SCREENWIDTH, SCREENHEIGHT))
pygame.display.set_caption("Hangman Pygame Project, Anna He")
CLOCK = pygame.time.Clock()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
BLUE = (0, 0, 200)
RED = (255, 0, 0)
SPLASHSCREENMILLISECONDS = 3000
pygame.font.init()

# Sounds
DIRECTORY = 'C:/Users/Eric/Desktop/FunnyPrograms/exp-1/smd_dude/annahangman/' # Need to get rid of all the directories or blake is gonna beat my ass
LOSESOUND = pygame.mixer.Sound(DIRECTORY + "losesound_laugh.wav")
WINSOUND = pygame.mixer.Sound(DIRECTORY + "winsound_oh.wav")
INCORRECTSOUND = pygame.mixer.Sound(DIRECTORY + "wrongsound_bones.wav")
CORRECTSOUND = pygame.mixer.Sound(DIRECTORY + "correctsound_spring.wav")
INTROSCREENMUSIC = pygame.mixer.Sound(DIRECTORY + "intromusic.wav")
BACKGROUNDMUSIC = pygame.mixer.Sound(DIRECTORY + "backgroundmusic.wav")
BACKGROUNDMUSIC.play()

# Splashscreens
class SplashScreen:
    INTROSCREENMUSIC.play()
    def __init__(self):
        #pre:
        #post: initialises splash screen attributes
        self.image = pygame.image.load(DIRECTORY + "introscreen.jpg")
        self.image = pygame.transform.scale(self.image, (SCREENWIDTH, SCREENHEIGHT))
        self.startTime = pygame.time.get_ticks()
        self.show = True
    
    def draw(self):
        #pre: self attributes
        #post: blits the screen on to the screen
        if pygame.time.get_ticks() - self.startTime <= SPLASHSCREENMILLISECONDS:
            SCREEN.blit(self.image, (0, 0))
        else:
            self.show = False

class InstructionsScreen:
    def __init__(self):
        #pre:
        #post: initialises the instructions screen attributes
        self.image = pygame.image.load(DIRECTORY + "instructionsscreen.jpg")
        self.image = pygame.transform.scale(self.image, (SCREENWIDTH, SCREENHEIGHT))
        self.show = False

    def draw(self):
        #pre: self attributes
        #post: blits the screen on to the screen
        SCREEN.blit(self.image, (0, 0))

class LosingScreen:
    def __init__(self):
        #pre:
        #post: initialises the lose screen attributes
        self.image = pygame.image.load(DIRECTORY + "losescreen.jpg")
        self.image = pygame.transform.scale(self.image, (SCREENWIDTH, SCREENHEIGHT))
        self.show = False

    def draw(self):
        #pre: self attributes
        #post: blits the screen on to the screen
        SCREEN.blit(self.image, (0, 0))

class WinScreen:
    def __init__(self):
        #pre:
        #post: initialises the win screen attributes
        self.image = pygame.image.load(DIRECTORY + "winscreen.jpg")
        self.image = pygame.transform.scale(self.image, (SCREENWIDTH, SCREENHEIGHT))
        self.show = False

    def draw(self):
        #pre: self attributes
        #post: blits the screen on to the screen
        SCREEN.blit(self.image, (0, 0))

# Classes
class Word:
    def __init__(self, level):
        #pre: the difficulty level string from seleclevel
        #post: finds a word in the dictionary 
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

    def RevealWord(self):
        #pre: self attributes
        #post: changes the reveal blanks with the letters
        self.Reveal = ""
        for letter in self.SecretWord:
            if letter in self.LettersGuessed:
                self.Reveal += letter
            else:
                self.Reveal += "_"
        return self.Reveal

    def Draw(self):
        #pre: self attributes
        #post: blits the letters on the screen
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
        #post: initialises the hangingman attributes
        self.x = 0
        self.y = 0
        
        self.imagelist = []
        for x in range(0, 10):
            self.image = pygame.image.load(DIRECTORY + 'guess'+ str(x) +".jpg")
            self.image = pygame.transform.scale(self.image, (SCREENWIDTH, SCREENHEIGHT))
            self.imagelist.append(self.image)

    def draw(self, errors):
        #pre: self attributes, the number of errors made in integers
        #post: blits the unfortunate person onto the screen
        SCREEN.blit(self.imagelist[errors], (self.x, self.y))

    
class Button:
    def __init__(self, x, y, width, height, text):
        #pre: position, dimensions, and content
        #post: inits the button attributes
        self.rect = pygame.Rect(x, y, width, height)
        self.text = text
        self.font = pygame.font.Font(None, 36)
        self.clicked = False

    def draw(self):
        #pre: self attributes
        #post: blits onto the screen with the content of button
        pygame.draw.rect(SCREEN, WHITE, self.rect)
        pygame.draw.rect(SCREEN, BLACK, self.rect, 2)

        TextSurface = self.font.render(self.text, True, BLACK)
        TextRect = TextSurface.get_rect(center=self.rect.center)
        SCREEN.blit(TextSurface, TextRect)
        
    def isClicked(self, mousePos):
        #pre: self attributes, coordinate of cursor
        #post: returns bool value to signal if button is pressed or not
        return self.rect.collidepoint(mousePos)


class LetterButton:
    def __init__(self, letter, position):
        #pre: the letter on the button as a string, the position of the button
        #post: inits letterbutton attributes
        self.GreenInk = (0, 200, 0)
        self.BlackInk = (0, 0, 0)
        self.BlueInk = (160, 225, 255)
        self.size = 40
        self.name = letter

        if self.name >= "a" and self.name <= 'g':
            self.x = 700 + position*40
            self.y = 600
        elif self.name >= 'h' and self.name <= 'n':
            self.x = 420 + position*40
            self.y = 640
        elif self.name >= 'o' and self.name <= 'u':
            self.x = 140 + position*40
            self.y = 680
        elif self.name >= 'v':
            self.x = -100 + position*40
            self.y = 720

        self.font = pygame.font.SysFont('arial', 30)
        self.mouse = False
        self.show = True
        self.letter = self.font.render(self.name, True, self.BlackInk)
        self.clicked = False  # Add a clicked attribute to track whether the button is clicked

    def draw(self):
        #pre: self attributes
        #post: blits button on screen depending on pos of cursor
        if not self.clicked and self.show:
            if self.mouse:
                pygame.draw.rect(SCREEN, self.BlueInk, (self.x, self.y, self.size, self.size))
            else:
                pygame.draw.rect(SCREEN, self.GreenInk, (self.x, self.y, self.size, self.size))

            SCREEN.blit(self.letter, (self.x + 8, self.y))

    def mouseover(self):
        #pre: self attributes
        #post: detects if the mouse is on the button (letter)
        x, y = pygame.mouse.get_pos()
       
        if self.x <= x < self.x + self.size and self.y < y < self.y + self.size:
            self.mouse = True
        else:
            self.mouse = False

    def click(self):
        #pre: self attributes
        #post: updates the button and then returns letter on the button
        global Alphabet
        x, y = pygame.mouse.get_pos()
        
        if self.x <= x < self.x + self.size and self.y <= y < self.y + self.size and self.show:
            self.show = False 

            if self.name in Alphabet:
                Alphabetlist = list(Alphabet) 
                Alphabetlist.remove(self.name) 
                Alphabet = ''.join(Alphabetlist)  

            return self.name


class ScoreBoard:
    def __init__(self):
        #pre:
        #post: inits scoreboard attributes
        self.Score = 0
        self.BlackRect = None
        self.font = pygame.font.SysFont('Times New Roman', 50)
    
    def IncreaseScore(self):
        #pre: self attributes
        #post: adds one to score
        self.Score +=1
    
    def draw(self, screen):
        #pre: self attributes, the pygame screen object
        #post: blits score onto black rectangle
        ScoreText = self.font.render(f"SCORE: {self.Score}", True, RED)
        RectWidth = ScoreText.get_width() + 20
        RectHeight = ScoreText.get_height() + 20
        RectX = (SCREENWIDTH - RectWidth) // 2
        RectY = 10
        self.BlackRect = pygame.Rect(RectX, RectY, RectWidth, RectHeight)
        pygame.draw.rect(screen, BLACK, self.BlackRect)
        screen.blit(ScoreText, (RectX + 10, RectY + 10))

# Selecting difficulty 
def SelectLevel():
    #pre:
    #post: looks at which button is clicked and changes the difficulty to it
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


# Starting up
Splash = SplashScreen()
Instructions = InstructionsScreen()
showInstructions = False
easyButton = Button(SCREENWIDTH/2-50, SCREENHEIGHT-200, 100, 50, "Easy")
mediumButton = Button(SCREENWIDTH/2-50, SCREENHEIGHT-150, 100, 50, "Medium")
hardButton = Button(SCREENWIDTH/2-50, SCREENHEIGHT-100, 100, 50, "Hard")

Alphabet = "abcdefghijklmnopqrstuvwxyz"
Keyboard = []
index = 0

for letter in Alphabet:
    Keyboard.append(LetterButton(letter, index))
    index += 1

HangMan = Hangingman()
iErrors = 0
WordToGuess = None
DisplayLoseScreen = False
WinScreenShown = False
LoseScreen = LosingScreen()
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

                        if iErrors == 9 and not DisplayLoseScreen:
                            SCREEN.blit(HangMan.imagelist[9], (HangMan.x, HangMan.y))
                            pygame.display.update()
                            BACKGROUNDMUSIC.stop()
                            LOSESOUND.play()
                            time.sleep(2)  
                            DisplayLoseScreen = True

                        # Varifying that player won
                        if set(WordToGuess.CorrectLetters.lower()) == set(WordToGuess.SecretWord.lower()):
                            WinScreenShown = True       
                            SCREEN.blit(HangMan.imagelist[iErrors], (HangMan.x, HangMan.y))
                            pygame.display.update()    
                            time.sleep(2)
                            BACKGROUNDMUSIC.stop()
                            WINSOUND.play()      

                        Keyboard[letter].clicked = True 

    SCREEN.fill((0, 0, 0))

    if Splash.show:
        Splash.draw()
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

    if DisplayLoseScreen:
        LoseScreen.draw()

    if WordToGuess is not None: 
        scoreboard.draw(SCREEN)
        

    pygame.display.update()
    CLOCK.tick(30)