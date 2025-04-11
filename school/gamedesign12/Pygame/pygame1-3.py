'''
Pygame 1-3 GameDesign12 Assignment
Eric Liu
13/03/2025
'''

import pygame

class ProgressBar():
    def __init__(self, sSurface, tColor, tPos, iWidth, iHeight, iProgress, tBGColor):
        self.sSurface = sSurface
        self.tColor = tColor
        self.tBGColor = tBGColor
        self.tPos = tPos
        self.iWidth = iWidth
        self.iHeight = iHeight
        self.iProgress = iProgress

    def fDrawProgressBar(self, iProgress):
        #pre: needs the progress of the progress bar
        #post: draws a progress bar on the sSurface with HP% text and a coloured background
        self.iProgress = iProgress
        pygame.draw.rect(self.sSurface, self.tBGColor, (self.tPos[0] - 2, self.tPos[1] - 2, self.iWidth + 4, self.iHeight + 4))
        pygame.draw.rect(self.sSurface, self.tColor, (self.tPos[0], self.tPos[1], self.iProgress, self.iHeight))
        fFont = pygame.font.Font(None, 20)
        fText = fFont.render('HP: ' + str(iProgress) + '%', 1, (0, 0, 0))
        rTextRect = fText.get_rect()
        rTextRect.center = (self.tPos[0] + self.iWidth // 2, self.tPos[1] + self.iHeight // 2)
        self.sSurface.blit(fText, rTextRect)

if __name__ == "__main__":
    pygame.init()
    sScreen = pygame.display.set_mode((200, 100))
    pygame.display.set_caption("ProgressBar")
    cClock = pygame.time.Clock()
    bGameLoop = True
    tColor = (0, 255, 0)
    tPos = (50, 50)
    iWidth = 100
    iHeight = 20
    iProgress = 80
    tBGColor = (255, 0, 0)
    ProgressBar1 = ProgressBar(sScreen, tColor, tPos, iWidth, iHeight, iProgress, tBGColor)
    
    while bGameLoop:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                bGameLoop = False

        sScreen.fill((255, 255, 255))
        ProgressBar1.fDrawProgressBar(iProgress)
        pygame.display.flip()
        cClock.tick(60)

    pygame.quit()
