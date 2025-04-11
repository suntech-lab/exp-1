'''
Pygame 1-7 GameDesign12 Assignment
Eric Liu
03/04/2025
'''

import math
import pygame
import sys
import random
import time

class BlackRects():
    def __init__(self, sSurface, tBlackPos, tColour, iWidth, iHeight, iNumber):
        self.sSurface = sSurface
        self.tBlackPos = tBlackPos
        self.tColour = tColour
        self.iWidth = iWidth
        self.iHeight = iHeight
        self.iNumber = iNumber
        self.bRect = pygame.Rect(tBlackPos[0], tBlackPos[1], iWidth, iHeight)

    def fPlaceRect(self, sSurface, tColour, iWidth, iHeight, iNumber):
        #pre: needs the position of the blue rectangle
        #post: draws the blue rectangle on the sSurface
        pygame.draw.rect(sSurface, tColour, (self.tBlackPos[0], self.tBlackPos[1], iWidth, iHeight))
        
        #get the numbers ready to put on the rectangles
        fNumberText = font.render(str(iNumber), True, (255, 255, 255))
        rTextRect = fNumberText.get_rect(center=(self.tBlackPos[0] + iWidth/2, self.tBlackPos[1] + iHeight/2))
        
        #draw the text on the rectangle
        sSurface.blit(fNumberText, rTextRect)

if __name__ == "__main__":

    #initialize pygame
    pygame.init()

    iScreenWidth = 600
    iScreenHeight = 600

    #initialize black squares
    iBlackWidth = 20
    iBlackHeight = 20

    #initialize the font
    pygame.font.init()
    font = pygame.font.SysFont(None, 20)

    #set up the clock and screen
    cClock = pygame.time.Clock()
    sScreen = pygame.display.set_mode((iScreenWidth, iScreenHeight))
    pygame.display.set_caption("Collision Test")

    #set up the colours
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)

    #set up the circle motion
    iRadius = 500
    angle = 0
    fSpeed = 0.05

    #set up the blue rectangles
    lBlackRects = []
    for i in range(10):
        tBlackPos = (random.randint(0, iScreenWidth - iBlackWidth), random.randint(0, iScreenWidth - iBlackHeight))
        lBlackRects.append(BlackRects(sScreen, tBlackPos, BLACK, iBlackWidth, iBlackHeight, i + 1))

    #set up the exit
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #fill the bg
        sScreen.fill((0, 0, 0))

        #update angle
        angle += fSpeed

        #calculate new position
        x = iScreenWidth/2 + iRadius * math.cos(angle)
        y = iScreenHeight/2 + iRadius * math.sin(angle)

        #draw the line from the center of the screen to the mouse cursor
        pygame.draw.line(sScreen, WHITE, (iScreenWidth/2, iScreenHeight/2), (x, y), 2)

        #detect collisions with mouse cursor location
        for rect in lBlackRects:
            lineCollision = rect.bRect.clipline((iScreenWidth/2, iScreenHeight/2), (x, y))
            if lineCollision:
                rect.fPlaceRect(sScreen, RED, iBlackWidth, iBlackHeight, rect.iNumber)
            else:
                rect.fPlaceRect(sScreen, BLACK, iBlackWidth, iBlackHeight, rect.iNumber)

        #draw the rectangles and update the display
        pygame.display.flip()
        cClock.tick(60)