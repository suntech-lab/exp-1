'''
Pygame 1-7 GameDesign12 Assignment
Eric Liu
03/04/2025
'''

import pygame
import sys
import random

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

    #initialize the font
    pygame.font.init()
    font = pygame.font.SysFont(None, 20)

    #set up the clock and screen
    cClock = pygame.time.Clock()
    sScreen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Collision Test")

    #set up the colours
    BLACK = (0, 0, 0)
    RED = (255, 0, 0)
    WHITE = (255, 255, 255)

    #set up the blue rectangles
    lBlackRects = []
    for i in range(10):
        tBlackPos = (random.randint(0, 750), random.randint(0, 550))
        lBlackRects.append(BlackRects(sScreen, tBlackPos, BLACK, 50, 50, i + 1))

    #set up the exit
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #fill the bg
        sScreen.fill((0, 0, 0))

        #draw the line from the center of the screen to the mouse cursor
        pygame.draw.line(sScreen, WHITE, (400, 300), pygame.mouse.get_pos(), 2)

        #detect collisions with mouse cursor location
        for rect in lBlackRects:
            lineCollision = rect.bRect.clipline((400, 300), pygame.mouse.get_pos())
            if lineCollision:
                rect.fPlaceRect(sScreen, RED, 50, 50, rect.iNumber)
            else:
                rect.fPlaceRect(sScreen, BLACK, 50, 50, rect.iNumber)

        #draw the rectangles and update the display
        pygame.display.flip()
        cClock.tick(60)