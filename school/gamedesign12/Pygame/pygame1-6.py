'''
Pygame 1-6 GameDesign12 Assignment
Eric Liu
02/04/2025
'''

import pygame
import sys
import random

class BlueRects():
    def __init__(self, sSurface, tBluePos, tColour, iWidth, iHeight, iNumber):
        self.sSurface = sSurface
        self.tBluePos = tBluePos
        self.tColour = tColour
        self.iWidth = iWidth
        self.iHeight = iHeight
        self.iNumber = iNumber
        self.bRect = pygame.Rect(tBluePos[0], tBluePos[1], iWidth, iHeight)

    def fPlaceRect(self, sSurface, tColour, iWidth, iHeight, iNumber):
        #pre: needs the position of the blue rectangle
        #post: draws the blue rectangle on the sSurface
        pygame.draw.rect(sSurface, tColour, (self.tBluePos[0], self.tBluePos[1], iWidth, iHeight))
        
        #get the numbers ready to put on the rectangles
        fNumberText = font.render(str(iNumber), True, (255, 255, 255))
        rTextRect = fNumberText.get_rect(center=(self.tBluePos[0] + iWidth/2, self.tBluePos[1] + iHeight/2))
        
        #draw the text on the rectangle
        sSurface.blit(fNumberText, rTextRect)

if __name__ == "__main__":

    #initialize pygame
    pygame.init()

    #initialize the font
    pygame.font.init()
    font = pygame.font.SysFont(None, 20)

    #set up the clock and screen
    cClock = pygame.time.Clock()
    sScreen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Collision Test")

    #set up the colours
    BLUE = (0, 0, 255)
    RED = (255, 0, 0)

    #set up the blue rectangles
    lBlueRects = []
    for i in range(10):
        tBluePos = (random.randint(0, 750), random.randint(0, 550))
        lBlueRects.append(BlueRects(sScreen, tBluePos, BLUE, 50, 50, i + 1))

    #set up the exit
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #get the cursor position and fill the bg
        tCursorPos = pygame.mouse.get_pos()
        sScreen.fill((0, 0, 0))

        #detect collisions with mouse cursor location
        for rect in lBlueRects:
            if rect.bRect.collidepoint(tCursorPos):
                rect.fPlaceRect(sScreen, RED, 50, 50, rect.iNumber)
            else:
                rect.fPlaceRect(sScreen, BLUE, 50, 50, rect.iNumber)

        #draw the rectangles and update the display
        pygame.display.flip()
        cClock.tick(60)

#03/04/2025
#changed the variable names so that there is no longer "rect.rect" in line 70