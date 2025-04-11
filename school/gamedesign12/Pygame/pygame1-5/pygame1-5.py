'''
Pygame 1-5 GameDesign12 Assignment
Eric Liu
01/04/2025
'''

import pygame
import sys
import os
import random

class BlueRects():
    def __init__(self, sSurface, tPos, tColour, iWidth, iHeight, iNumber):
        self.sSurface = sSurface
        self.tPos = tPos
        self.tColour = tColour
        self.iWidth = iWidth
        self.iHeight = iHeight
        self.iNumber = iNumber

    def fPlaceBlueRect(self):
        #pre: needs the position of the blue rectangle
        #post: draws the blue rectangle on the sSurface
        pygame.draw.rect(self.sSurface, self.tColour, (self.tPos[0], self.tPos[1], self.iWidth, self.iHeight))
        fNumberText = font.render(str(self.iNumber), True, (255, 255, 255))
        rTextRect = fNumberText.get_rect(center=(self.tPos[0] + self.iWidth/2, self.tPos[1] + self.iHeight/2))
        self.sSurface.blit(fNumberText, rTextRect)

class CursorTrackingRect():
    def __init__(self, sSurface, tPos, tColour, iWidth, iHeight, iSpeed):
        self.sSurface = sSurface
        self.tPos = tPos
        self.tColour = tColour
        self.iWidth = iWidth
        self.iHeight = iHeight
        self.iSpeed = iSpeed
        self.iCollidedNumber = None
        self.tColour = tColour

    def fMoveRect(self):
        #pre: needs the position of the cursor
        #post: moves the rectangle to the new position (cursor position)
        self.tPos = (pygame.mouse.get_pos()[0]-self.iWidth/2, pygame.mouse.get_pos()[1]-self.iHeight/2)
        if self.tPos[0] < 0:
            self.tPos = (0, self.tPos[1])
        if self.tPos[0] > 800 - self.iWidth:
            self.tPos = (800 - self.iWidth, self.tPos[1])
        pygame.draw.rect(self.sSurface, self.tColour, (self.tPos[0], self.tPos[1], self.iWidth, self.iHeight))

    def fDetectCollision(self, lBlueRects):
        #pre: needs the position of the blue rectangle and the cursor rectangle
        #post: detects if there is a collision between the two rectangles
        cCursorRect = pygame.Rect(self.tPos, (self.iWidth, self.iHeight))
        
        for rect in lBlueRects:
            bBlueRect = pygame.Rect(rect.tPos, (rect.iWidth, rect.iHeight))
            if cCursorRect.colliderect(bBlueRect):
                self.iCollidedNumber = rect.iNumber
                pygame.mixer.music.play(loops=0, start=0.0)
                self.tColour = (
                    random.randint(10, 255),
                    random.randint(10, 255),
                    random.randint(10, 255))
                return True
        return False

if __name__ == "__main__":

    #initialize pygame
    pygame.init()
    pygame.font.init()
    font = pygame.font.SysFont(None, 20)

    #set up the technical stuff
    cClock = pygame.time.Clock()
    sScreen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Collision Test")

    #get directory and load sound
    sDirectory = os.path.dirname(os.path.abspath(__file__))
    pygame.mixer.music.load(os.path.join(sDirectory, 'ping.mp3'))

    #set up the blue rectangles
    lBlueRects = []
    for i in range(10):
        tPos = (random.randint(0, 750), random.randint(0, 550))
        lBlueRects.append(BlueRects(sScreen, tPos, (0, 0, 255), 50, 50, i + 1))

    #set up the cursor tracking rectangle
    fCursorRect = CursorTrackingRect(sScreen, (0, 0), (255, 0, 0), 50, 50, 5)

    #set up the text that tells you which rectangle you hit
    sInfoText = ""
    tInfoTextPos = (10, 10)

    #main loop
    while True:

        #exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #background
        sScreen.fill((0, 0, 0))

        #place blue rects
        for rect in lBlueRects:
            rect.fPlaceBlueRect()

        #draw the cursor tracking rectangle
        fCursorRect.fMoveRect()

        #detect collision
        if fCursorRect.fDetectCollision(lBlueRects):

            #change window text
            sInfoText = f"Collision with {fCursorRect.iCollidedNumber}"

            #print to terminal
            print(sInfoText)

            #remove the collided rectangle from the list
            lBlueRects = [rect for rect in lBlueRects if rect.iNumber != fCursorRect.iCollidedNumber]

        #put the text on the screen
        if sInfoText:
            sTextSurface = font.render(sInfoText, True, (255, 255, 255))
            sScreen.blit(sTextSurface, tInfoTextPos)

        pygame.display.flip()
        cClock.tick(60)