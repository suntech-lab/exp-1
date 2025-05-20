import random, time, pygame, sys
from pygame.locals import *

FPS = 60
WINDOWWIDTH = 640
WINDOWHEIGHT = 480
BOXSIZE = 20
BOARDWIDTH = 10
BOARDHEIGHT = 20
BLANK = '.'

MOVESIDEWAYSFREQ = 0.13
MOVEDOWNFREQ = 0.1

XMARGIN = int((WINDOWWIDTH - BOARDWIDTH * BOXSIZE) / 2)
TOPMARGIN = WINDOWHEIGHT - (BOARDHEIGHT * BOXSIZE) - 5

#               R    G    B
WHITE       = (255, 255, 255)
GRAY        = (185, 185, 185)
BLACK       = (  0,   0,   0)
RED         = (155,   0,   0)
LIGHTRED    = (175,  20,  20)
GREEN       = (  0, 155,   0)
LIGHTGREEN  = ( 20, 175,  20)
BLUE        = (  0,   0, 155)
LIGHTBLUE   = ( 20,  20, 175)
YELLOW      = (155, 155,   0)
LIGHTYELLOW = (175, 175,  20)

BORDERCOLOR = LIGHTBLUE
BGCOLOR = GRAY
TEXTCOLOR = WHITE
TEXTSHADOWCOLOR = GRAY
COLORS      = (     BLUE,      GREEN,      RED,      YELLOW)
LIGHTCOLORS = (LIGHTBLUE, LIGHTGREEN, LIGHTRED, LIGHTYELLOW)
assert len(COLORS) == len(LIGHTCOLORS) #each color must have light color

TEMPLATEWIDTH = 5
TEMPLATEHEIGHT = 5

S_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '..OO.',
                     '.OO..',
                     '.....'],
                    ['.....',
                     '..O..',
                     '..OO.',
                     '...O.',
                     '.....']]

Z_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '.OO..',
                     '..OO.',
                     '.....'],
                    ['.....',
                     '..O..',
                     '.OO..',
                     '.O...',
                     '.....']]

I_SHAPE_TEMPLATE = [['..O..',
                     '..O..',
                     '..O..',
                     '..O..',
                     '.....'],
                    ['.....',
                     '.....',
                     'OOOO.',
                     '.....',
                     '.....']]

O_SHAPE_TEMPLATE = [['.....',
                     '.....',
                     '.OO..',
                     '.OO..',
                     '.....']]

J_SHAPE_TEMPLATE = [['.....',
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
                     '.....']]

L_SHAPE_TEMPLATE = [['.....',
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
                     '.....']]

T_SHAPE_TEMPLATE = [['.....',
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

PIECES = {'S': S_SHAPE_TEMPLATE,
          'Z': Z_SHAPE_TEMPLATE,
          'J': J_SHAPE_TEMPLATE,
          'L': L_SHAPE_TEMPLATE,
          'I': I_SHAPE_TEMPLATE,
          'O': O_SHAPE_TEMPLATE,
          'T': T_SHAPE_TEMPLATE}

def main():
    #pre: doesnt need any arguments
    #post: gives runGame() the stuff it needs to run
    global FPSCLOCK, DISPLAYSURF, BASICFONT, BIGFONT
    pygame.init()
    FPSCLOCK = pygame.time.Clock()
    DISPLAYSURF = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
    BASICFONT = pygame.font.Font('freesansbold.ttf', 18)
    BIGFONT = pygame.font.Font('freesansbold.ttf', 100)
    pygame.display.set_caption('Tetris')

    showTextScreen('Tetris')
    while True:
        runGame()
        showTextScreen('Game Over')

def runGame():
    #pre: needs the stuff from main()
    #post: runs the game/is the game

    #setup variables for the start of the game
    board = getBlankBoard()
    fLastMoveDownTime = time.time()
    fLastMoveSidewaysTime = time.time()
    fLastFallTime = time.time()
    bMovingDown = False #there is no movingUp variable
    bMovingLeft = False
    bMovingRight = False
    iScore = 0
    iLevel, fFallFreq = calculateLevelAndFallFreq(iScore)
    fLockDelay = 0.5
    fLockStartTime = None

    pFallingPiece = getNewPiece()
    pNextPiece = getNewPiece()

    while True: #game loop
        if pFallingPiece == None:
            #no falling piece in play, so start a new piece at the top
            pFallingPiece = pNextPiece
            pNextPiece = getNewPiece()
            fLastFallTime = time.time() # reset fLastFallTime

            if not isValidPosition(board, pFallingPiece):
                return #cant fit a new piece on the board, so game over

        checkForQuit()
        for event in pygame.event.get(): #event handling loop
            if event.type == KEYUP:
                if (event.key == K_p):
                    # Pausing the game
                    DISPLAYSURF.fill(BGCOLOR)
                    showTextScreen('Paused') #pause until a key press
                    fLastFallTime = time.time()
                    fLastMoveDownTime = time.time()
                    fLastMoveSidewaysTime = time.time()
                elif (event.key == K_LEFT or event.key == K_a):
                    bMovingLeft = False
                elif (event.key == K_RIGHT or event.key == K_d):
                    bMovingRight = False
                elif (event.key == K_DOWN or event.key == K_s):
                    bMovingDown = False

            elif event.type == KEYDOWN:
                #moving the piece sideways
                if (event.key == K_LEFT or event.key == K_a) and isValidPosition(board, pFallingPiece, adjX=-1):
                    pFallingPiece['x'] -= 1
                    bMovingLeft = True
                    bMovingRight = False
                    fLastMoveSidewaysTime = time.time()

                elif (event.key == K_RIGHT or event.key == K_d) and isValidPosition(board, pFallingPiece, adjX=1):
                    pFallingPiece['x'] += 1
                    bMovingRight = True
                    bMovingLeft = False
                    fLastMoveSidewaysTime = time.time()

                #rotating the piece (if there is room to rotate)
                elif (event.key == K_UP or event.key == K_w):
                    pFallingPiece['rotation'] = (pFallingPiece['rotation'] + 1) % len(PIECES[pFallingPiece['shape']])
                    if not isValidPosition(board, pFallingPiece):
                        pFallingPiece['x'] -= 1
                        if not isValidPosition(board, pFallingPiece):
                            pFallingPiece['x'] += 2
                elif (event.key == K_q): #rotate the other direction
                    pFallingPiece['rotation'] = (pFallingPiece['rotation'] - 1) % len(PIECES[pFallingPiece['shape']])
                    if not isValidPosition(board, pFallingPiece):
                        pFallingPiece['x'] -= 1
                        if not isValidPosition(board, pFallingPiece):
                            pFallingPiece['x'] += 2
                            
                #making the piece fall faster with the down key
                elif (event.key == K_DOWN or event.key == K_s):
                    bMovingDown = True
                    if isValidPosition(board, pFallingPiece, adjY=1):
                        pFallingPiece['y'] += 1
                    fLastMoveDownTime = time.time()

                #move the current piece all the way down
                elif event.key == K_SPACE:
                    bMovingDown = False
                    bMovingLeft = False
                    bMovingRight = False
                    fLockDelay = 0
                    for i in range(1, BOARDHEIGHT):
                        if not isValidPosition(board, pFallingPiece, adjY=i):
                            break
                    pFallingPiece['y'] += i - 1

        #handle moving the piece because of user input
        if (bMovingLeft or bMovingRight) and time.time() - fLastMoveSidewaysTime > MOVESIDEWAYSFREQ:
            if bMovingLeft and isValidPosition(board, pFallingPiece, adjX=-1):
                pFallingPiece['x'] -= 1
            elif bMovingRight and isValidPosition(board, pFallingPiece, adjX=1):
                pFallingPiece['x'] += 1
            fLastMoveSidewaysTime = time.time()

        if bMovingDown and time.time() - fLastMoveDownTime > MOVEDOWNFREQ and isValidPosition(board, pFallingPiece, adjY=1):
            pFallingPiece['y'] += 1
            fLastMoveDownTime = time.time()

        #let the piece fall if it is time to fall
        if time.time() - fLastFallTime > fFallFreq:
            #see if the piece has landed
            if not isValidPosition(board, pFallingPiece, adjY=1):
                if fLockStartTime == None:
                    fLockStartTime = time.time()
                elif time.time() - fLockStartTime >= fLockDelay:
                    #falling piece has landed, set it on the board
                    addToBoard(board, pFallingPiece)
                    iScore += removeCompleteLines(board)
                    iLevel, fFallFreq = calculateLevelAndFallFreq(iScore)
                    pFallingPiece = None
                    fLockStartTime = None
            else:
                #piece did not land, just move the piece down
                pFallingPiece['y'] += 1
                fLastFallTime = time.time()

        #drawing everything on the screen
        DISPLAYSURF.fill(BGCOLOR)
        drawBoard(board)
        drawStatus(iScore, iLevel)
        drawNextPiece(pNextPiece)
        if pFallingPiece != None:
            ghostPiece = getGhostPiecePosition(board, pFallingPiece.copy())
            drawPiece(ghostPiece, ghost=True)    
            drawPiece(pFallingPiece)

        pygame.display.update()
        FPSCLOCK.tick(FPS)

def makeTextObjs(text, font, color):
    surf = font.render(text, True, color)
    return surf, surf.get_rect()

def terminate():
    pygame.quit()
    sys.exit()

def checkForKeyPress():
    #Go through event queue looking for a KEYUP event.
    #Grab KEYDOWN events to remove them from the event queue.
    checkForQuit()

    for event in pygame.event.get([KEYDOWN, KEYUP]):
        if event.type == KEYDOWN:
            continue
        return event.key
    return None

def showTextScreen(text):
    #This function displays large text in the
    #center of the screen until a key is pressed.
    #Draw the text drop shadow
    titleSurf, titleRect = makeTextObjs(text, BIGFONT, TEXTSHADOWCOLOR)
    titleRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2))
    DISPLAYSURF.blit(titleSurf, titleRect)

    #Draw the text
    titleSurf, titleRect = makeTextObjs(text, BIGFONT, TEXTCOLOR)
    titleRect.center = (int(WINDOWWIDTH / 2) - 3, int(WINDOWHEIGHT / 2) - 3)
    DISPLAYSURF.blit(titleSurf, titleRect)

    #Draw the additional "Press a key to play." text.
    pressKeySurf, pressKeyRect = makeTextObjs('Press any key to start. During the game, press p to pause.', BASICFONT, TEXTCOLOR)
    pressKeyRect.center = (int(WINDOWWIDTH / 2), int(WINDOWHEIGHT / 2) + 100)
    DISPLAYSURF.blit(pressKeySurf, pressKeyRect)

    while checkForKeyPress() == None:
        pygame.display.update()
        FPSCLOCK.tick()

def checkForQuit():
    for event in pygame.event.get(QUIT): # get all the QUIT events
        terminate() # terminate if any QUIT events are present
    for event in pygame.event.get(KEYUP): # get all the KEYUP events
        if event.key == K_ESCAPE:
            terminate() # terminate if the KEYUP event was for the Esc key
        pygame.event.post(event) # put the other KEYUP event objects back

def calculateLevelAndFallFreq(iScore):
    #Based on the iScore, return the iLevel the player is on and
    #how many seconds pass until a falling piece falls one space.
    iLevel = int(iScore / 10) + 1
    fFallFreq = 0.27 - (iLevel * 0.02)
    return iLevel, fFallFreq

def getNewPiece():
    # return a random new piece in a random rotation and color
    shape = random.choice(list(PIECES.keys()))
    newPiece = {'shape': shape,
                'rotation': random.randint(0, len(PIECES[shape]) - 1),
                'x': int(BOARDWIDTH / 2) - int(TEMPLATEWIDTH / 2),
                'y': -2, # start it above the board (i.e. less than 0)
                'color': random.randint(0, len(COLORS)-1)}
    return newPiece

def addToBoard(board, piece):
    # fill in the board based on piece's location, shape, and rotation
    for x in range(TEMPLATEWIDTH):
        for y in range(TEMPLATEHEIGHT):
            if PIECES[piece['shape']][piece['rotation']][y][x] != BLANK:
                board[x + piece['x']][y + piece['y']] = piece['color']

def getBlankBoard():
    # create and return a new blank board data structure
    board = []
    for i in range(BOARDWIDTH):
        board.append([BLANK] * BOARDHEIGHT)
        print(board)
    return board

def isOnBoard(x, y):
    return x >= 0 and x < BOARDWIDTH and y < BOARDHEIGHT

def isValidPosition(board, piece, adjX=0, adjY=0):
    # Return True if the piece is within the board and not colliding
    for x in range(TEMPLATEWIDTH):
        for y in range(TEMPLATEHEIGHT):
            isAboveBoard = y + piece['y'] + adjY < 0
            if isAboveBoard or PIECES[piece['shape']][piece['rotation']][y][x] == BLANK:
                continue
            if not isOnBoard(x + piece['x'] + adjX, y + piece['y'] + adjY):
                return False
            if board[x + piece['x'] + adjX][y + piece['y'] + adjY] != BLANK:
                return False
    return True

def isCompleteLine(board, y):
    # Return True if the line filled with boxes with no gaps.
    for x in range(BOARDWIDTH):
        if board[x][y] == BLANK:
            return False
    return True

def removeCompleteLines(board):
    # Remove any completed lines on the board, move everything above them down, and return the number of complete lines.
    iLinesRemoved = 0
    y = BOARDHEIGHT - 1 # start y at the bottom of the board
    while y >= 0:
        if isCompleteLine(board, y):
            # Remove the line and pull boxes down by one line.
            for pullDownY in range(y, 0, -1):
                for x in range(BOARDWIDTH):
                    board[x][pullDownY] = board[x][pullDownY-1]
            # Set very top line to blank.
            for x in range(BOARDWIDTH):
                board[x][0] = BLANK
            iLinesRemoved += 1
            # Note on the next iteration of the loop, y is the same.
            # This is so that if the line that was pulled down is also
            # complete, it will be removed.
        else:
            y -= 1 # move on to check next row up
    return iLinesRemoved

def convertToPixelCoords(boxX, boxY):
    # Convert the given xy coordinates of the board to xy
    # coordinates of the location on the screen.
    return (XMARGIN + (boxX * BOXSIZE)), (TOPMARGIN + (boxY * BOXSIZE))

def drawBox(boxX, boxY, color, pixelX=None, pixelY=None, ghost=False):
    if color == BLANK:
        return
    if pixelX == None and pixelY == None:
        pixelX, pixelY = convertToPixelCoords(boxX, boxY)
    if ghost:
        # Draw with a lighter color or transparency
        surf = pygame.Surface((BOXSIZE - 1, BOXSIZE - 1), pygame.SRCALPHA)
        surf.fill((*COLORS[color], 80))  # 80 is alpha for transparency
        DISPLAYSURF.blit(surf, (pixelX + 1, pixelY + 1))
    else:
        pygame.draw.rect(DISPLAYSURF, COLORS[color], (pixelX + 1, pixelY + 1, BOXSIZE - 1, BOXSIZE - 1))
        pygame.draw.rect(DISPLAYSURF, LIGHTCOLORS[color], (pixelX + 1, pixelY + 1, BOXSIZE - 4, BOXSIZE - 4))

def drawBoard(board):
    # draw the border around the board
    pygame.draw.rect(DISPLAYSURF, BORDERCOLOR, (XMARGIN - 3, TOPMARGIN - 7, (BOARDWIDTH * BOXSIZE) + 8, (BOARDHEIGHT * BOXSIZE) + 8), 5)

    # fill the background of the board
    pygame.draw.rect(DISPLAYSURF, BGCOLOR, (XMARGIN, TOPMARGIN, BOXSIZE * BOARDWIDTH, BOXSIZE * BOARDHEIGHT))
    # draw the individual boxes on the board
    for x in range(BOARDWIDTH):
        for y in range(BOARDHEIGHT):
            drawBox(x, y, board[x][y])

def drawStatus(iScore, iLevel):
    # draw the iScore text
    scoreSurf = BASICFONT.render('Score: %s' % iScore, True, TEXTCOLOR)
    scoreRect = scoreSurf.get_rect()
    scoreRect.topleft = (WINDOWWIDTH - 150, 20)
    DISPLAYSURF.blit(scoreSurf, scoreRect)

    # draw the iLevel text
    levelSurf = BASICFONT.render('Level: %s' % iLevel, True, TEXTCOLOR)
    levelRect = levelSurf.get_rect()
    levelRect.topleft = (WINDOWWIDTH - 150, 50)
    DISPLAYSURF.blit(levelSurf, levelRect)

def drawPiece(piece, pixelX=None, pixelY=None, ghost=False):
    shapeToDraw = PIECES[piece['shape']][piece['rotation']]
    if pixelX == None and pixelY == None:
        # if pixelX & pixelY hasn't been specified, use the location stored in the piece data structure
        pixelX, pixelY = convertToPixelCoords(piece['x'], piece['y'])

    # draw each of the boxes that make up the piece
    for x in range(TEMPLATEWIDTH):
        for y in range(TEMPLATEHEIGHT):
            if shapeToDraw[y][x] != BLANK:
                color = piece['color']
                if ghost:
                    color = color
                    drawBox(None, None, color, pixelX + (x * BOXSIZE), pixelY + (y * BOXSIZE), ghost=True)
                else:
                    drawBox(None, None, color, pixelX + (x * BOXSIZE), pixelY + (y * BOXSIZE))

def drawNextPiece(piece):
    # draw the "next" text
    nextSurf = BASICFONT.render('Next:', True, TEXTCOLOR)
    nextRect = nextSurf.get_rect()
    nextRect.topleft = (WINDOWWIDTH - 120, 80)
    DISPLAYSURF.blit(nextSurf, nextRect)
    # draw the "next" piece
    drawPiece(piece, pixelX=WINDOWWIDTH-120, pixelY=100)

def getGhostPiecePosition(board, piece):
    # Copy the piece to avoid modifying the original
    ghostPiece = piece.copy()
    while isValidPosition(board, ghostPiece, adjY=1):
        ghostPiece['y'] += 1
    return ghostPiece

if __name__ == '__main__':
    main()