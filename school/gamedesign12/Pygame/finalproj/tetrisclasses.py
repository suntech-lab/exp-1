'''
GameDesign 12 - Pygame Final Project
Tetris
Eric Liu
20/06/2025
bug:
if a block is slammed instantly after restart, there is a chance that the block does not fully reach the bottom
(^^i tried using ai to fix but it couldnt find the problem)
'''

import random, time, pygame, sys
from pygame.locals import *
pygame.mixer.init()

#important constants
FPS = 60
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
BOXSIZE = 20
BOARDWIDTH = 10
BOARDHEIGHT = 20
EMPTY = '.'

#sounds
TETRISTHEME = pygame.mixer.Sound('C:\\Users\\ericl\\Documents\\lab\\school\\gamedesign12\\Pygame\\finalproj\\Tetris.mp3')
TETRISTHEME.set_volume(0.5)
LOCKPIECESOUND = pygame.mixer.Sound('C:\\Users\\ericl\\Documents\\lab\\school\\gamedesign12\\Pygame\\finalproj\\TetrisSlam.mp3')
LOCKPIECESOUND.set_volume(0.5)
PAUSEMUSIC = pygame.mixer.Sound('C:\\Users\\ericl\\Documents\\lab\\school\\gamedesign12\\Pygame\\finalproj\\PauseMusic.mp3')
PAUSEMUSIC.set_volume(0.5)
LOSESOUND = pygame.mixer.Sound('C:\\Users\\ericl\\Documents\\lab\\school\\gamedesign12\\Pygame\\finalproj\\LoseEffect.mp3')
LOSESOUND.set_volume(0.5)

#time in seconds * seconds to nanoseconds
#nanoseconds is used for more accurate timing
#i switched from seconds because time.time() uses seconds since the epoch
#and this makes the lock time delay vary depending on when the game started and how many seconds have passed
#this is a problem because the lock time delay is supposed to be constant
MOVESIDEWAYSFREQ = 0.13 * 1000000000
MOVEDOWNFREQ = 0.3 * 1000000000

#figuring out how to center the board
XMARGIN = int((WINDOWWIDTH - BOARDWIDTH * BOXSIZE) / 2)
TOPMARGIN = WINDOWHEIGHT - (BOARDHEIGHT * BOXSIZE) - 5

#neat colours
WHITE       = (255, 255, 255)
GRAY        = (185, 185, 185)
BLACK       = ( 10,  10,  10)
RED         = (135,   0,   0)
LIGHTRED    = (175,  40,  40)
GREEN       = (  0, 135,   0)
LIGHTGREEN  = ( 40, 175,  40)
BLUE        = ( 40,  40, 135)
LIGHTBLUE   = ( 80,  80, 175)
YELLOW      = (135, 135,   0)
LIGHTYELLOW = (175, 175,  40)

#set colours
BORDERCOLOUR = (  70,  70, 175)
BGCOLOUR = BLACK
TEXTCOLOUR = WHITE
TEXTSHADOWCOLOUR = GRAY
COLOURS      = (BLUE, GREEN, RED, YELLOW)
LIGHTCOLOURS = (LIGHTBLUE, LIGHTGREEN, LIGHTRED, LIGHTYELLOW)

#piece template dimensions
#line piece is weird but thats just how it is
TEMPLATEWIDTH = 5
TEMPLATEHEIGHT = 5

PIECES = {
    'S': [['.....',
           '.....',
           '..OO.',
           '.OO..',
           '.....'],
          ['.....',
           '..O..',
           '..OO.',
           '...O.',
           '.....']],
    'Z': [['.....',
           '.....',
           '.OO..',
           '..OO.',
           '.....'],
          ['.....',
           '..O..',
           '.OO..',
           '.O...',
           '.....']],
    'I': [['..O..',
           '..O..',
           '..O..',
           '..O..',
           '.....'],
          ['.....',
           '.....',
           'OOOO.',
           '.....',
           '.....']],
    'O': [['.....',
           '.....',
           '.OO..',
           '.OO..',
           '.....']],
    'J': [['.....',
           '.O...',
           '.OOO.',
           '.....',
           '.....'],
          ['.....',
           '..OO.',
           '..O..',
           '..O..',
           '.....'],
          ['.....',
           '.....',
           '.OOO.',
           '...O.',
           '.....'],
          ['.....',
           '..O..',
           '..O..',
           '.OO..',
           '.....']],
    'L': [['.....',
           '...O.',
           '.OOO.',
           '.....',
           '.....'],
          ['.....',
           '..O..',
           '..O..',
           '..OO.',
           '.....'],
          ['.....',
           '.....',
           '.OOO.',
           '.O...',
           '.....'],
          ['.....',
           '.OO..',
           '..O..',
           '..O..',
           '.....']],
    'T': [['.....',
           '..O..',
           '.OOO.',
           '.....',
           '.....'],
          ['.....',
           '..O..',
           '..OO.',
           '..O..',
           '.....'],
          ['.....',
           '.....',
           '.OOO.',
           '..O..',
           '.....'],
          ['.....',
           '..O..',
           '.OO..',
           '..O..',
           '.....']]
}

class CPiece:
    def __init__(self, sShape, iRotation, iX, iY, iColour):
        self.sShape = sShape
        self.iRotation = iRotation
        self.iX = iX
        self.iY = iY
        self.iColour = iColour

    def copy(self):
        #pre: its own attributes
        #post: a new object with the same attributes
        return CPiece(self.sShape, self.iRotation, self.iX, self.iY, self.iColour)

class CBoard:
    def __init__(self):
        self.iWidth = BOARDWIDTH
        self.iHeight = BOARDHEIGHT
        self.lGrid = [[EMPTY] * self.iHeight for _ in range(self.iWidth)] #its easier to move the parts of the pieces through a single list instead of across multiple lists

    def isOnBoard(self, iX, iY):
        #pre: iX and iY are the coordinates of the piece
        #post: returns true if the piece is on the board
        return iX >= 0 and iX < self.iWidth and iY < self.iHeight

    def isValidPosition(self, oPiece, iAdjX=0, iAdjY=0):
        if oPiece is None:
            return False
        #pre: needs info on the piece
        #post: returns true if the piece is in a valid position (board, other pieces)
        if oPiece.iY is None:
            oPiece.iY = 0 #if the piece is None, set it to 0 so it doesn't crash
        for iXTemplate in range(TEMPLATEWIDTH):
            for iYTemplate in range(TEMPLATEHEIGHT):
                bIsAboveBoard = iYTemplate + oPiece.iY + iAdjY < 0

                if bIsAboveBoard or PIECES[oPiece.sShape][oPiece.iRotation][iYTemplate][iXTemplate] == EMPTY:
                    continue #skip empty spaces in the template

                if not self.isOnBoard((iXTemplate + oPiece.iX + iAdjX), (iYTemplate + oPiece.iY + iAdjY)): #brackets inside the argument arent needed here but there for clarity (iX and iY)
                    return False #out of bounds

                if self.lGrid[iXTemplate + oPiece.iX + iAdjX][iYTemplate + oPiece.iY + iAdjY] != EMPTY: #checks if the block in the grid is empty/EMPTY
                    return False #collides with another piece
        return True

    def addPiece(self, oPiece):
        #pre: needs info on the piece
        #post: for each cell in the template, check if its not EMPTY, then add the cells to the grid
        for iXTemplate in range(TEMPLATEWIDTH):
            for iYTemplate in range(TEMPLATEHEIGHT):
                if PIECES[oPiece.sShape][oPiece.iRotation][iYTemplate][iXTemplate] != EMPTY:
                    self.lGrid[iXTemplate + oPiece.iX][iYTemplate + oPiece.iY] = oPiece.iColour

    def isCompleteLine(self, iY):
        #pre: needs the y coordinate of the line
        #post: returns true if the line is complete
        for iX in range(self.iWidth):
            if self.lGrid[iX][iY] == EMPTY:
                return False
        return True

    def removeCompleteLines(self):
        #pre: the board info
        #post: removes complete lines and returns the number of lines removed from bottom to top
        iLinesRemoved = 0
        iY = self.iHeight - 1
        while iY >= 0: #check from bottom
            if self.isCompleteLine(iY):

                for iPullDownY in range(iY, 0, -1):
                    for iX in range(self.iWidth):
                        self.lGrid[iX][iPullDownY] = self.lGrid[iX][iPullDownY-1] #pull row above (iPullDownY-1) down

                for iX in range(self.iWidth):
                    self.lGrid[iX][0] = EMPTY
                iLinesRemoved += 1 #clear top row

            else:
                iY -= 1 #decrement here because we pulled a row down, allowing us to check the same row again
        return iLinesRemoved

    def getBlankBoard(self):
        #pre: needs the board info
        #post: makes a EMPTY board
        self.lGrid = [[EMPTY] * self.iHeight for _ in range(self.iWidth)]

class CTetrisGame:
    def __init__(self):
            self.oBoard = CBoard()
            self.iScore = 0
            self.iLevel = 1
            self.fFallFreq = MOVEDOWNFREQ
            self.fLockDelay = 0.5 * 1000000000
            self.fLockStartTime = None
            self.fLastMoveDownTime = time.time_ns()
            self.fLastMoveSidewaysTime = time.time_ns()
            self.fLastFallTime = time.time_ns()
            self.bMovingDown = False
            self.bMovingLeft = False
            self.bMovingRight = False
            self.oFallingPiece = self.getNewPiece()
            self.oNextPiece = self.getNewPiece()
            self.hardDropping = False
            self.softDropFreq = 0.3 * 1000000000  # Default soft drop interval (nanoseconds)
    
    def resetGame(self):
        self.oBoard = CBoard()
        self.iScore = 0
        self.iLevel = 1
        self.fFallFreq = MOVEDOWNFREQ
        self.fLockDelay = 0.5 * 1000000000
        self.fLockStartTime = None
        self.fLastMoveDownTime = time.time_ns()
        self.fLastMoveSidewaysTime = time.time_ns()
        self.fLastFallTime = time.time_ns()
        self.bMovingDown = False
        self.bMovingLeft = False
        self.bMovingRight = False
        self.oFallingPiece = self.getNewPiece()
        self.oNextPiece = self.getNewPiece()
        self.hardDropping = False
        self.softDropFreq = 0.3 * 1000000000  # Default soft drop interval (nanoseconds)

    def runGame(self):
        return _runGame(self) #added here cause the function is HUGE

    def getNewPiece(self):
        #pre: needs info on the game
        #post: returns a new piece with a random shape, a random rotation, and x and y coordinates so that it spawns in the middle of the board at the top
        sShape = random.choice(list(PIECES.keys()))
        iRotation = random.randint(0, len(PIECES[sShape]) - 1)
        iX = int(BOARDWIDTH / 2) - int(TEMPLATEWIDTH / 2)
        iY = -2
        iColour = random.randint(0, len(COLOURS)-1) #random colour too
        return CPiece(sShape, iRotation, iX, iY, iColour)

    def calculateLevelAndFallFreq(self):
        #pre: needs info on the game
        #post: changes the level and fall frequency based on the score
        self.iLevel = int(self.iScore / 10) + 1
        self.fFallFreq = 0.27 - (self.iLevel * 0.02)

    def hardDrop(self):
        #pre: needs info on the game
        #post: SLAMS IT DOWN
        self.hardDropping = True
        while self.oBoard.isValidPosition(self.oFallingPiece, iAdjY=1):
            self.oFallingPiece.iY += 1
        self.lockPiece()

    def lockPiece(self):
        #pre: needs info on the game
        #post: locks the piece in place and removes complete lines and resets the falling piece
        self.oBoard.addPiece(self.oFallingPiece)
        self.iScore += self.oBoard.removeCompleteLines()
        self.calculateLevelAndFallFreq()
        self.fLockStartTime = None
        self.oFallingPiece = None
        LOCKPIECESOUND.play() #play the sound
        return True

    def moveLeft(self):
        #pre: game info
        #post: moves the piece
        if self.oBoard.isValidPosition(self.oFallingPiece, iAdjX=-1):
            self.oFallingPiece.iX -= 1

    def moveRight(self):
        #pre: game info
        #post: moves the piece
        if self.oBoard.isValidPosition(self.oFallingPiece, iAdjX=1):
            self.oFallingPiece.iX += 1

    def moveDown(self):
        #pre: game info
        #post: moves the piece, returns true if it moved
        #if the piece is at the bottom, lock it
        if self.oBoard.isValidPosition(self.oFallingPiece, iAdjY=1):
            self.oFallingPiece.iY += 1
            return True
        return False

    def rotate(self):
        #pre: game info
        #post: rotates the piece (selects next rotation) and kicks it if it is in an invalid position
        iOldRotation = self.oFallingPiece.iRotation
        iOldX = self.oFallingPiece.iX
        self.oFallingPiece.iRotation = (self.oFallingPiece.iRotation + 1) % len(PIECES[self.oFallingPiece.sShape]) #rotates the piece
        
        if self.oFallingPiece.sShape == 'I':
            # Try a sequence of wall kicks for the I piece
            for offset in [0, -1, 1, -2, 2, -3, 3]:
                self.oFallingPiece.iX = iOldX + offset
                if self.oBoard.isValidPosition(self.oFallingPiece):
                    return
            # If none work, revert
            self.oFallingPiece.iX = iOldX
            self.oFallingPiece.iRotation = iOldRotation
        else:
            if not self.oBoard.isValidPosition(self.oFallingPiece):
                self.oFallingPiece.iX -= 1 #try moving it if the rotation is invalid
                if not self.oBoard.isValidPosition(self.oFallingPiece):
                    self.oFallingPiece.iX += 2 #if the move is invalid, move it the other way
                    if not self.oBoard.isValidPosition(self.oFallingPiece):
                        self.oFallingPiece.iX -= 1
                        self.oFallingPiece.iRotation = iOldRotation

    def rotateCCW(self): #same thing, except chooses the rotation before
        #pre: game info
        #post: rotates the piece (selects next rotation) and kicks it if it is in an invalid position
        iOldRotation = self.oFallingPiece.iRotation
        iOldX = self.oFallingPiece.iX
        self.oFallingPiece.iRotation = (self.oFallingPiece.iRotation - 1) % len(PIECES[self.oFallingPiece.sShape]) #rotates the piece
        
        if self.oFallingPiece.sShape == 'I':
            # Try a sequence of wall kicks for the I piece
            for offset in [0, -1, 1, -2, 2, -3, 3]:
                self.oFallingPiece.iX = iOldX + offset
                if self.oBoard.isValidPosition(self.oFallingPiece):
                    return
            # If none work, revert
            self.oFallingPiece.iX = iOldX
            self.oFallingPiece.iRotation = iOldRotation
        else:
            if not self.oBoard.isValidPosition(self.oFallingPiece):
                self.oFallingPiece.iX -= 1 #try moving it if the rotation is invalid
                if not self.oBoard.isValidPosition(self.oFallingPiece):
                    self.oFallingPiece.iX += 2 #if the move is invalid, move it the other way
                    if not self.oBoard.isValidPosition(self.oFallingPiece):
                        self.oFallingPiece.iX -= 1
                        self.oFallingPiece.iRotation = iOldRotation

    def getGhostPiece(self):
        #pre: game info
        #post: returns a ghost piece that is the same shape and colour as the falling piece, but at the bottom of the board
        oGhost = self.oFallingPiece.copy()
        while self.oBoard.isValidPosition(oGhost, iAdjY=1):
            oGhost.iY += 1
        return oGhost

def main():
    #pre: nothing
    #post: sets up and runs the game
    pygame.init()
    pygame.mixer.init()
    global FPSCLOCK, DISPLAYSURF, BASICFONT, BIGFONT
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 13)
    BIGFONT = pygame.font.Font('freesansbold.ttf', 100)
    pygame.display.set_caption('Tetris (OOP)')
    showStartScreen('Tetris')
    while True:
        CTetrisGame().runGame()
        showStartScreen('Game Over')

def showStartScreen(text):
    #pre: text to display
    #post: displays the text on the screen and waits for a key press
    titleSurf, titleRect = makeTextObjs(text, BIGFONT, TEXTCOLOUR)
    titleRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2))
    DISPLAYSURF.blit(titleSurf, titleRect)
    titleSurf, titleRect = makeTextObjs(text, BIGFONT, TEXTSHADOWCOLOUR)
    titleRect.center = (int(WINDOWWIDTH / 2) - 3, int(WINDOWHEIGHT / 2) - 3)
    DISPLAYSURF.blit(titleSurf, titleRect)
    pressKeySurf, pressKeyRect = makeTextObjs('Press any key to start. Press ESC to quit. During the game, press p to pause.', BASICFONT, TEXTCOLOUR)
    pressKeyRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2) + 100)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)
    while checkForKeyPress() == None:
        pygame.display.update()
        FPSCLOCK.tick()

def makeTextObjs(text, font, colour):
    #pre: text, font, and colour
    #post: returns a surface and a rect for the text
    surf = font.render(text, True, colour)
    return surf, surf.get_rect()

def checkForKeyPress():
    #pre: nothing
    #post: returns the key that was pressed, or None if no key was pressed
    checkForQuit()
    for event in pygame.event.get([KEYDOWN, KEYUP]):
        if event.type == KEYDOWN:
            continue
        return event.key
    return None

def checkForQuit():
    #pre: nothing
    #post: checks for quit events and exits the game if necessary
    for event in pygame.event.get(QUIT):
        pygame.quit()
        sys.exit()
    for event in pygame.event.get(KEYUP):
        if event.key == K_ESCAPE:
            pygame.quit()
            sys.exit()
        pygame.event.post(event)

def convertToPixelCoords(iBoxX, iBoxY):
    #pre: iBoxX and iBoxY are the coordinates of the box
    #post: returns the pixel coordinates of the box
    return (XMARGIN + (iBoxX * BOXSIZE)), (TOPMARGIN + (iBoxY * BOXSIZE))

def drawBox(iBoxX, iBoxY, iColour, pixelX=None, pixelY=None, ghost=False):
    #pre: iBoxX and iBoxY are the coordinates of the box, the colour of the box, pixel coordinates of the box (optional), whether the box is a ghost piece
    #post: draws the box on the screen
    if iColour == EMPTY:
        return
    if pixelX is None and pixelY is None:
        pixelX, pixelY = convertToPixelCoords(iBoxX, iBoxY)
    if ghost:
        surf = pygame.Surface((BOXSIZE - 1, BOXSIZE - 1), pygame.SRCALPHA) #alpha for fade
        surf.fill((*COLOURS[iColour], 80))
        DISPLAYSURF.blit(surf, (pixelX + 1, pixelY + 1))
    else:
        pygame.draw.rect(DISPLAYSURF, COLOURS[iColour], (pixelX + 1, pixelY + 1, BOXSIZE - 1, BOXSIZE - 1))
        pygame.draw.rect(DISPLAYSURF, LIGHTCOLOURS[iColour], (pixelX + 1, pixelY + 1, BOXSIZE - 4, BOXSIZE - 4))

def drawBoard(oBoard):
    #pre: the board object
    #post: draws the board on the screen
    pygame.draw.rect(DISPLAYSURF, BORDERCOLOUR, (XMARGIN - 3, TOPMARGIN - 7, (BOARDWIDTH * BOXSIZE) + 8, (BOARDHEIGHT * BOXSIZE) + 12), 5)
    for iX in range(BOARDWIDTH):
        for iY in range(BOARDHEIGHT):
            drawBox(iX, iY, oBoard.lGrid[iX][iY])

def drawStatus(iScore, iLevel):
    #pre: the score and level
    #post: draws them on the screen
    scoreSurf = BASICFONT.render('Score: %s' % iScore, True, TEXTCOLOUR) #%s is a placeholder for the string representation of the score
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 150, 20)
    DISPLAYSURF.blit(scoreSurf, scoreRect)
    levelSurf = BASICFONT.render('Level: %s' % iLevel, True, TEXTCOLOUR)
    levelRect = levelSurf.get_rect()
    levelRect.topleft = (WINDOWWIDTH - 150, 50)
    DISPLAYSURF.blit(levelSurf, levelRect)

def drawPiece(oPiece, pixelX=None, pixelY=None, ghost=False):
    #pre: the piece object, whether the piece is a ghost piece
    #post: draws the piece on the screen
    shapeToDraw = PIECES[oPiece.sShape][oPiece.iRotation]
    if pixelX is None and pixelY is None:
        pixelX, pixelY = convertToPixelCoords(oPiece.iX, oPiece.iY)
    for iX in range(TEMPLATEWIDTH):
        for iY in range(TEMPLATEHEIGHT):
            if shapeToDraw[iY][iX] != EMPTY:
                iColour = oPiece.iColour
                if ghost:
                    drawBox(None, None, iColour, pixelX + (iX * BOXSIZE), pixelY + (iY * BOXSIZE), ghost=True)
                else:
                    drawBox(None, None, iColour, pixelX + (iX * BOXSIZE), pixelY + (iY * BOXSIZE))

def drawNextPiece(oPiece):
    #pre: the next piece object
    #post: draws the "next piece" on the screen (next piece is in quotes because it is not actually next, it is the piece that will spawn after the current one)
    nextSurf = BASICFONT.render('Next:', True, TEXTCOLOUR)
    nextRect = nextSurf.get_rect()
    nextRect.topleft = (WINDOWWIDTH - 120, 80)
    DISPLAYSURF.blit(nextSurf, nextRect)
    drawPiece(oPiece, pixelX=WINDOWWIDTH-120, pixelY=100)

def _runGame(self):
    #pre: literally everything
    #post: runs the game loop
    TETRISTHEME.play(-1)
    while True:
        LOSESOUND.stop() #stop the lose sound if it is playing
        if self.oFallingPiece == None:
            self.oFallingPiece = self.oNextPiece
            self.oNextPiece = self.getNewPiece()
            self.fLastFallTime = time.time_ns()
            self.fLockDelay = 0.5 * 1000000000
            if not self.oBoard.isValidPosition(self.oFallingPiece):
                self.oFallingPiece.iY += 1
                TETRISTHEME.stop()
                LOSESOUND.play()
                showStartScreen('Game Over')
                return
        checkForQuit()
        for event in pygame.event.get():
            if event.type == KEYUP:

                if (event.key == K_p):
                    PAUSEMUSIC.play(-1)
                    TETRISTHEME.stop()
                    DISPLAYSURF.fill(BGCOLOUR)
                    showStartScreen('Paused')
                    self.fLastFallTime = time.time_ns() #reset movement timer
                    self.fLastMoveDownTime = time.time_ns() #reset movement timer
                    self.fLastMoveSidewaysTime = time.time_ns() #reset movement timer
                    TETRISTHEME.play(-1) #resume the music
                    PAUSEMUSIC.stop() #stop the pause music

                elif (event.key == K_LEFT or event.key == K_a):
                    self.bMovingLeft = False
                elif (event.key == K_RIGHT or event.key == K_d):
                    self.bMovingRight = False
                elif (event.key == K_DOWN or event.key == K_s):
                    self.bMovingDown = False
                    self.softDropFreq = 0.3 * 1000000000  # Reset to normal soft drop speed

            elif event.type == KEYDOWN:
                if (event.key == K_LEFT or event.key == K_a) and self.oBoard.isValidPosition(self.oFallingPiece, iAdjX=-1):
                    self.oFallingPiece.iX -= 1
                    self.bMovingLeft = True
                    self.bMovingRight = False
                    self.fLastMoveSidewaysTime = time.time_ns() #reset movement timer

                elif (event.key == K_RIGHT or event.key == K_d) and self.oBoard.isValidPosition(self.oFallingPiece, iAdjX=1):
                    self.oFallingPiece.iX += 1
                    self.bMovingRight = True
                    self.bMovingLeft = False
                    self.fLastMoveSidewaysTime = time.time_ns() #reset movement timer

                elif (event.key == K_UP or event.key == K_w):
                    self.rotate()

                elif (event.key == K_q):
                    self.rotateCCW()

                elif (event.key == K_DOWN or event.key == K_s):
                    self.bMovingDown = True
                    self.softDropFreq = 0.06 * 1000000000  # Fast soft drop speed

                elif event.key == K_SPACE:
                    if self.oFallingPiece is not None: #make sure the player doesn't lock a nonexistent piece
                        self.bMovingDown = False
                        self.bMovingLeft = False
                        self.bMovingRight = False
                        self.fLockDelay = 0
                        for i in range(1, BOARDHEIGHT):
                            if not self.oBoard.isValidPosition(self.oFallingPiece, iAdjY=i):
                                break
                        self.oFallingPiece.iY += i - 1 #move the piece to the bottom
                        self.lockPiece() #force it to lock here. if locked naturally, it will take some time
                        continue

        if (self.bMovingLeft or self.bMovingRight) and time.time_ns() - self.fLastMoveSidewaysTime > MOVESIDEWAYSFREQ:
            if self.bMovingLeft and self.oBoard.isValidPosition(self.oFallingPiece, iAdjX=-1):
                self.oFallingPiece.iX -= 1 #move left continuously
            elif self.bMovingRight and self.oBoard.isValidPosition(self.oFallingPiece, iAdjX=1):
                self.oFallingPiece.iX += 1 #move right continuously
            self.fLastMoveSidewaysTime = time.time_ns() #reset movement timer

        if self.bMovingDown and time.time_ns() - self.fLastMoveDownTime > self.softDropFreq and self.oBoard.isValidPosition(self.oFallingPiece, iAdjY=1):
            self.oFallingPiece.iY += 1 #soft drop faster
            self.fLastMoveDownTime = time.time_ns() #reset movement timer

        if not self.hardDropping:
            if time.time_ns() - self.fLastFallTime > MOVEDOWNFREQ:
                if not self.oBoard.isValidPosition(self.oFallingPiece, iAdjY=1):
                    if self.fLockStartTime is None: #if the piece is not moving down, start the lock timer
                        self.fLockStartTime = time.time_ns() #start it
                    elif time.time_ns() - self.fLockStartTime >= self.fLockDelay:
                        self.lockPiece() #lock it
                        self.fLockStartTime = None
                else:
                    self.oFallingPiece.iY += 1 #otherwise, move it down naturally
                    self.fLastFallTime = time.time_ns() #reset movement timer

        #drawing and displaying stuff
        DISPLAYSURF.fill(BGCOLOUR)
        drawBoard(self.oBoard)
        drawStatus(self.iScore, self.iLevel)
        drawNextPiece(self.oNextPiece)
        if self.oFallingPiece is not None:
            ghostPiece = self.getGhostPiece()
            drawPiece(ghostPiece, ghost=True)
            drawPiece(self.oFallingPiece)
        pygame.display.update()
        FPSCLOCK.tick(FPS)

if __name__ == '__main__':
    main()