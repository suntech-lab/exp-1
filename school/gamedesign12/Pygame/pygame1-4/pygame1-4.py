'''
Pygame 1-4 GameDesign12 Assignment
Eric Liu
31/03/2025
'''

import pygame
import os
import sys

class Background():
    def __init__(self, sSurface, tPos, iWidth, iHeight, fImage):
        self.sSurface = sSurface
        self.tPos = tPos
        self.iWidth = iWidth
        self.iHeight = iHeight
        self.fImage = fImage

    def fDrawBackground(self):
        #pre: needs the image
        #post: draws the background image on the sSurface
        self.sSurface.blit(self.fImage, (self.tPos[0], self.tPos[1]))

class Alien():
    def __init__(self, sSurface, tPos, iWidth, iHeight, fImage):
        self.sSurface = sSurface
        self.tPos = tPos
        self.iWidth = iWidth
        self.iHeight = iHeight
        self.fImage = fImage

    def fDrawAlien(self):
        #pre: needs the image
        #post: draws the alien image on the sSurface
        self.sSurface.blit(self.fImage, (self.tPos[0], self.tPos[1]))

    def fMoveAlien(self):
        #pre: needs the position of the alien
        #post: moves the alien to the new position
        self.tPos = self.tPos[0] + 1, self.tPos[1]
        self.fDrawAlien()
        

if __name__ == "__main__":

    #initialize pygame
    pygame.init()

    #set up all the required technical stuff
    cClock = pygame.time.Clock()
    sScreen = pygame.display.set_mode((800, 600))
    pygame.display.set_caption("Background Test")

    #get the directory of the images
    sDirectory = os.path.dirname(os.path.abspath(__file__))

    #set up the background
    fBackground = pygame.image.load(os.path.join(sDirectory, 'background.jpg'))
    fBackground = pygame.transform.scale(fBackground, (1100, 600))
    fBackgroundRect = fBackground.get_rect(center=(400, 300))
    fBackground = Background(sScreen, (0, 0), 800, 600, fBackground)

    #set up the alien
    fAlien = pygame.image.load(os.path.join(sDirectory, 'spaceship.png'))
    fAlien = pygame.transform.scale(fAlien, (50, 50))
    fAlienRect = fAlien.get_rect(center=(400, 300))
    fAlien = Alien(sScreen, (0, 300), 50, 50, fAlien)

    #set up the "score"
    fFont = pygame.font.Font(None, 36)
    fText = fFont.render('Score: 1234', 1, (255, 255, 255))
    fTextRect = fText.get_rect()
    fTextRect.center = (400, 50)

    #get the spaceship sound ready for the alien
    pygame.mixer.music.load(os.path.join(sDirectory, 'spaceshipsound.mp3'))
    pygame.mixer.music.play(loops=-1, start=0.0)

    #main loop
    while True:

        #exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

        #draw the background and alien
        sScreen.fill((255, 255, 255))
        fBackground.fDrawBackground()
        fAlien.fDrawAlien()
        fAlien.fMoveAlien()
        sScreen.blit(fText, fTextRect)

        cClock.tick(60)
        pygame.display.flip()