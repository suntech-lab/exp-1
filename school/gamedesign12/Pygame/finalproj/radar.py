'''
Pygame 1-7 GameDesign12 Assignment
Eric Liu
03/04/2025

note:
the rectangles that the radar detects are called black rectangles, because they are black by default
and turn red when detected

15/04/2025
improved physics of rects
added a jumpscare video that plays when the player loses
added a sound that plays when the player loses

16/04/2025
made it so that when the player loses the screen becomes a lose screen
and the jumpscare instantly pops up like a bait and switch
made screen larger
added radar width
sorted code


'''
import math
import pygame
import sys
import random
import itertools
import cv2
import numpy as np
import os
import time

class VideoPlayer:
    def __init__(self, filePath, screenWidth, screenHeight):
        self.cap = cv2.VideoCapture(filePath)
        if not self.cap.isOpened():
            print(f"Error: Could not open video file {filePath}")
            self.valid = False
            return
        
        self.valid = True
        self.playing = False
        self.screenWidth = screenWidth
        self.screenHeight = screenHeight
        self.fadeAlpha = 128  # Set transparency level (128 = 50% transparent)
        self.fadeSurface = pygame.Surface((screenWidth, screenHeight))
        
    def play(self):
        #pre: needs to know if the video's good to go, and if it is, it plays the video
        #post: plays the video

        if self.valid:
            self.playing = True
            self.fadeAlpha = 50
            self.cap.set(cv2.CAP_PROP_POS_FRAMES, 0)  # Rewind to start
        
    def update(self, screen):
        #pre: needs to know if the video is playing or valid
        #post: sets up the video to be played

        if not self.valid or not self.playing:
            return False

        ret, frame = self.cap.read()
        if not ret:
            self.playing = False
            return False

        # Convert and resize video frame
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        frame = cv2.resize(frame, (self.screenWidth, self.screenHeight))
        frame = np.rot90(frame)

        # Convert to pygame surface and display
        videoSurface = pygame.surfarray.make_surface(frame)

        self.fadeSurface.fill((0, 0, 0))
        self.fadeSurface.blit(videoSurface, (0, 0))
        self.fadeSurface.set_alpha(self.fadeAlpha)  # Set transparency level (0 = fully transparent, 255 = fully opaque)

        # Blit the fade surface onto the screen
        screen.blit(self.fadeSurface, (0, 0))
        time.sleep(0.026)
        return True

class Player():
    def __init__(self, sSurface, tColour, iWidth, iHeight):
        self.sSurface = sSurface
        self.tColour = tColour
        self.iWidth = iWidth
        self.iHeight = iHeight
        self.tPos = ((iScreenWidth/2) - iWidth/2, (iScreenHeight/2) - iHeight/2)
        self.fVelX = 0
        self.fVelY = 0
        self.bRect = pygame.Rect(self.tPos[0], self.tPos[1], iWidth, iHeight)

    def fHandleInput(self):
        #pre: needs the keyboard input
        #post: sets the velocity of the player based on the keyboard input
        keys = pygame.key.get_pressed()
        self.fVelX = 0
        self.fVelY = 0
        
        if keys[pygame.K_LEFT]:
            self.fVelX = -2
        if keys[pygame.K_RIGHT]:
            self.fVelX = 2
        if keys[pygame.K_UP]:
            self.fVelY = -2
        if keys[pygame.K_DOWN]:
            self.fVelY = 2
    
    def fMove(self):
        #pre: needs the velocity and position of the player
        #post: moves the player based on the velocity and position
        x, y = self.tPos
        x += self.fVelX
        y += self.fVelY
        
        x = max(0, min(iScreenWidth - self.iWidth, x))
        y = max(0, min(iScreenHeight - self.iHeight, y))
        
        self.tPos = (x, y)
        self.bRect.x = x
        self.bRect.y = y

    def fCheckCollision(self, rRect):
        #pre: needs the position and size of the rectangle
        #post: returns a rectangle object
        if self.bRect.colliderect(rRect.bRect):
            print("boo")
            return True
        return False
    
    def fPlacePlayer(self, sSurface, tColour, iWidth, iHeight):
        #pre: needs the position of the blue rectangle
        #post: draws the blue rectangle on the sSurface
        self.bRect.x = self.tPos[0]
        self.bRect.y = self.tPos[1]

        pygame.draw.rect(sSurface, tColour, (self.tPos[0], self.tPos[1], iWidth, iHeight))

        #get the numbers ready to put on the rectangles
        fNumberText = fPlayerFont.render("DONT TOUCH RED", True, WHITE)
        rTextRect = fNumberText.get_rect(center=(self.tPos[0] + iWidth/2, self.tPos[1] - iHeight/2))

        sSurface.blit(fNumberText, rTextRect)

class BlackRects():
    def __init__(self, sSurface, tBlackPos, tColour, iWidth, iHeight, iNumber):
        self.sSurface = sSurface
        self.tBlackPos = tBlackPos
        self.tColour = tColour
        self.iWidth = iWidth
        self.iHeight = iHeight
        self.iNumber = iNumber
        self.fVelX = random.uniform(-1.5, 1.5)
        self.fVelY = random.uniform(-1.5, 1.5)
        self.bRect = pygame.Rect(tBlackPos[0], tBlackPos[1], iWidth, iHeight)
        self.bLastDetected = 0
        self.bDetectionDuration = 1000
        self.iMaxAlpha = 255

    def fPlaceRect(self, sSurface, tColour, iWidth, iHeight, iNumber, iCurrentTime):
        #pre: needs the position of the blue rectangle
        #post: draws the blue rectangle on the sSurface
        # If recently detected, keep showing as red
        self.bRect.x = self.tBlackPos[0]
        self.bRect.y = self.tBlackPos[1]

        if iCurrentTime - self.bLastDetected < self.bDetectionDuration:
            elapsed = iCurrentTime - self.bLastDetected
            iBlackRectTransparency = int(self.iMaxAlpha * (1 - elapsed / self.bDetectionDuration))

            sRectSurface = pygame.Surface((iWidth, iHeight), pygame.SRCALPHA)
            pygame.draw.rect(sRectSurface, (*RED, iBlackRectTransparency), (0, 0, iWidth, iHeight))
            sSurface.blit(sRectSurface, (self.tBlackPos[0], self.tBlackPos[1]))
        else:
            pygame.draw.rect(sSurface, tColour, (self.tBlackPos[0], self.tBlackPos[1], iWidth, iHeight))
        
        #get the numbers ready to put on the rectangles
        fNumberText = fPlayerFont.render(str(iNumber), True, WHITE)
        rTextRect = fNumberText.get_rect(center=(self.tBlackPos[0] + iWidth/2, self.tBlackPos[1] + iHeight/2))

        #sSurface.blit(fNumberText, rTextRect)

    def fGetRect(self):
        #pre: needs the position and tSize of the rectangle
        #post: returns a rectangle object
        return pygame.Rect(self.tBlackPos[0], self.tBlackPos[1], self.iWidth, self.iHeight)

    def fMove(self, iScreenWidth, iScreenHeight):
        #pre: needs the screen iWidth and height
        #post: makes the square bounce off the walls when it detects that the square is touching the walls
        x, y = self.tBlackPos
        x += self.fVelX
        y += self.fVelY

        if x <= 0 or x >= iScreenWidth - self.iWidth:
            self.fVelX *= -1
        if y <= 0 or y >= iScreenHeight - self.iHeight:
            self.fVelY *= -1

        self.tBlackPos = (x, y)

    def fCheckCollision(rRect1, rRect2):
        #pre: needs two square objects
        #post: checks if the two squares are touching each other, and if they are, it makes them bounce off each other
        if rRect1.fGetRect().colliderect(rRect2.fGetRect()):
        # Calculate overlap amounts
            iOverlapX = min(rRect1.bRect.right - rRect2.bRect.left, 
                        rRect2.bRect.right - rRect1.bRect.left)
            
            iOverlapY = min(rRect1.bRect.bottom - rRect2.bRect.top,
                        rRect2.bRect.bottom - rRect1.bRect.top)

            # Determine primary collision axis (which overlap is smaller)
            if abs(iOverlapX) < abs(iOverlapY):
                # Horizontal collision - change X velocities
                total_mass = 2  # Assuming equal mass
                fNewVel1 = (rRect1.fVelX*(1-1) + 2*1*rRect2.fVelX)/total_mass
                fNewVel2 = (rRect2.fVelX*(1-1) + 2*1*rRect1.fVelX)/total_mass
                rRect1.fVelX, rRect2.fVelX = fNewVel1, fNewVel2
                
                # Separate along X axis by full overlap amount
                if rRect1.bRect.centerx < rRect2.bRect.centerx:
                    rRect1.tBlackPos = (rRect1.tBlackPos[0] - iOverlapX/2, rRect1.tBlackPos[1])
                    rRect2.tBlackPos = (rRect2.tBlackPos[0] + iOverlapX/2, rRect2.tBlackPos[1])
                else:
                    rRect1.tBlackPos = (rRect1.tBlackPos[0] + iOverlapX/2, rRect1.tBlackPos[1])
                    rRect2.tBlackPos = (rRect2.tBlackPos[0] - iOverlapX/2, rRect2.tBlackPos[1])
            else:
                # Vertical collision - change Y velocities
                total_mass = 2  # Assuming equal mass
                fNewVel1 = (rRect1.fVelY*(1-1) + 2*1*rRect2.fVelY)/total_mass
                fNewVel2 = (rRect2.fVelY*(1-1) + 2*1*rRect1.fVelY)/total_mass
                rRect1.fVelY, rRect2.fVelY = fNewVel1, fNewVel2
                
                # Separate along Y axis
                if rRect1.bRect.centery < rRect2.bRect.centery:
                    rRect1.tBlackPos = (rRect1.tBlackPos[0], rRect1.tBlackPos[1] - iOverlapY/2)
                    rRect2.tBlackPos = (rRect2.tBlackPos[0], rRect2.tBlackPos[1] + iOverlapY/2)
                else:
                    rRect1.tBlackPos = (rRect1.tBlackPos[0], rRect1.tBlackPos[1] + iOverlapY/2)
                    rRect2.tBlackPos = (rRect2.tBlackPos[0], rRect2.tBlackPos[1] - iOverlapY/2)

            # Update rectangle positions
            rRect1.bRect.x = rRect1.tBlackPos[0]
            rRect1.bRect.y = rRect1.tBlackPos[1]
            rRect2.bRect.x = rRect2.tBlackPos[0]
            rRect2.bRect.y = rRect2.tBlackPos[1]

class Button:
    def __init__(self, xPos, yPos, width, height, text, colour, hoverColour):
        self.rect = pygame.Rect(xPos, yPos, width, height)
        self.text = text
        self.colour = colour
        self.hoverColour = hoverColour
        self.isHovered = False
        
    def draw(self, surface):
        colour = self.hoverColour if self.isHovered else self.colour
        pygame.draw.rect(surface, colour, self.rect)
        pygame.draw.rect(surface, WHITE, self.rect, 2)  # Border
        
        textSurf = font.render(self.text, True, WHITE)
        textRect = textSurf.get_rect(center=self.rect.center)
        surface.blit(textSurf, textRect)
        
    def check_hover(self, pos):
        self.isHovered = self.rect.collidepoint(pos)
        return self.isHovered
        
    def is_clicked(self, pos, event):
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            return self.rect.collidepoint(pos)
        return False
    
class Obstacle():
    def __init__(self, sSurface, tColour, iWidth, iHeight, tPos):
        self.sSurface = sSurface
        self.tColour = tColour
        self.iWidth = iWidth
        self.iHeight = iHeight
        self.tPos = tPos
        self.bRect = pygame.Rect(tPos[0], tPos[1], iWidth, iHeight)

    def fPlaceObstacle(self, sSurface, tColour, iWidth, iHeight):
        #pre: needs the position of the obstacle
        #post: draws the obstacle on the sSurface
        self.bRect.x = self.tPos[0]
        self.bRect.y = self.tPos[1]

        pygame.draw.rect(sSurface, tColour, (self.tPos[0], self.tPos[1], iWidth, iHeight))

if __name__ == "__main__":
    #initialize pygame
    pygame.init()
    pygame.font.init()

    #variables (screen size, rect size, colours, radar)
    iScreenWidth = 800
    iScreenHeight = 600

    iBlackWidth = 30
    iBlackHeight = 30
    iPlayerWidth = 20
    iPlayerHeight = 20

    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    DARKRED = (200, 0, 0)
    TITLECOLOUR = (153, 0, 76)
    BUTTONGREEN = (0, 180, 0)
    HOVERGREEN = (0, 220, 0)

    iRadarRadius = int(math.sqrt((iScreenWidth/2)**2 + (iScreenHeight/2)**2))
    iRadarStartAngle = 0
    fRadarSpeed = 0.03
    lRadarHistory = []
    iHistoryDuration = 2000

    SAFEZONEX = iPlayerWidth * 5
    SAFEZONEY = iPlayerHeight * 5
    playerCenterX = iScreenWidth / 2
    playerCenterY = iScreenHeight / 2

    pygame.font.init()
    fPlayerFont = pygame.font.SysFont(None, 20)
    fLoseTextFont = pygame.font.SysFont(None, 50)
    font = pygame.font.SysFont(None, 40)

    fps = 60

    #set up the clock and screen
    cClock = pygame.time.Clock()
    sScreen = pygame.display.set_mode((iScreenWidth, iScreenHeight))
    pygame.display.set_caption("game")

    #media prep (directory, sound, video, font)
    sDirectory = os.path.dirname(os.path.abspath(__file__))

    pygame.mixer.music.load(os.path.join(sDirectory, 'locust.mp3'))

    videoPlayer = VideoPlayer((os.path.join(sDirectory, "locust.mp4")), iScreenWidth, iScreenHeight)  # Make sure file is in same directory
    if not videoPlayer.valid:
        print("video player initialization fail")
    
    #set up player
    cPlayer = Player(sScreen, WHITE, iPlayerWidth, iPlayerHeight)

    #set up the black rectangles
    lBlackRects = []
    for i in range(10):
        while True:
            tBlackPos = (random.randint(0, iScreenWidth - iBlackWidth), 
                        random.randint(0, iScreenHeight - iBlackHeight))
            # Check if position is outside safe zone
            if not (abs(tBlackPos[0] - playerCenterX) < SAFEZONEX) and (abs(tBlackPos[1] - playerCenterY) < SAFEZONEY):
                break
        lBlackRects.append(BlackRects(sScreen, tBlackPos, BLACK, iBlackWidth, iBlackHeight, i + 1))

    #set up obstacles
    lObstacles = []
    for i in range(20):
        while True:
            tPos = (random.randint(0, iScreenWidth - iBlackWidth), random.randint(0, iScreenHeight - iBlackHeight))
            # Check if position is outside safe zone
            if not (abs(tPos[0] - playerCenterX) < SAFEZONEX) and (abs(tPos[1] - playerCenterY) < SAFEZONEY):
                break
        lObstacles.append(Obstacle(sScreen, BLACK, iBlackWidth, iBlackHeight, tPos))

    #game states
    MENU = 0
    PLAYING = 1
    GAME_OVER = 2

    gameState = MENU

    #buttons
    playButton = Button(iScreenWidth//2 - 100, iScreenHeight//2 - 25, 200, 50, "PLAY", BUTTONGREEN, HOVERGREEN)
    quitButton = Button(iScreenWidth//2 - 100, iScreenHeight//2 + 50, 200, 50, "QUIT", RED, DARKRED)
    
    while True:
        #find mouse
        mouse_pos = pygame.mouse.get_pos()

        #keep track of the time
        iCurrentTime = pygame.time.get_ticks()

        #exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if gameState == MENU:
                if playButton.is_clicked(mouse_pos, event):
                    gameState = PLAYING
                    cPlayer.tPos = ((iScreenWidth/2) - iPlayerWidth/2, (iScreenHeight/2) - iPlayerHeight/2)
                    pygame.mixer.music.stop()
                    
                if quitButton.is_clicked(mouse_pos, event):
                    pygame.quit()
                    sys.exit()

        #fill the bg
        sScreen.fill(BLACK)

        if gameState == MENU:
            # Draw title
            title_text = pygame.font.SysFont(None, 80).render("THE LOCUSTS", True, TITLECOLOUR)
            title_rect = title_text.get_rect(center=(iScreenWidth//2, iScreenHeight//4))
            sScreen.blit(title_text, title_rect)
            
            # Update and draw buttons
            playButton.check_hover(mouse_pos)
            quitButton.check_hover(mouse_pos)
            playButton.draw(sScreen)
            quitButton.draw(sScreen)
        
        elif gameState == PLAYING:
            # Gameplay logic
            for rect in lBlackRects:    
                rect.fPlaceRect(sScreen, BLACK, iBlackWidth, iBlackHeight, rect.iNumber, iCurrentTime)

            cPlayer.fPlacePlayer(sScreen, WHITE, iPlayerWidth, iPlayerHeight)
            
            # Update radar angle
            iRadarStartAngle += fRadarSpeed

            #place black rects
            for rect in lBlackRects:    
                rect.fPlaceRect(sScreen, BLACK, iBlackWidth, iBlackHeight, rect.iNumber, iCurrentTime)

            #place obstacles
            for rect in lObstacles:
                rect.fPlaceObstacle(sScreen, WHITE, iBlackWidth, iBlackHeight)

            #place player
            cPlayer.fPlacePlayer(sScreen, WHITE, iPlayerWidth, iPlayerHeight)

            #update iRadarStartAngle
            iRadarStartAngle += fRadarSpeed

            #calculate new position
            x = iScreenWidth/2 + iRadarRadius * math.cos(iRadarStartAngle)
            y = iScreenHeight/2 + iRadarRadius * math.sin(iRadarStartAngle)

            #draw the line from the center of the screen to the x, y of the radar ^^^
            pygame.draw.line(sScreen, WHITE, ((cPlayer.tPos[0] + cPlayer.iWidth/2),(cPlayer.tPos[1] + cPlayer.iHeight/2)), (x - 14, y - 14), 2)
            pygame.draw.line(sScreen, WHITE, ((cPlayer.tPos[0] + cPlayer.iWidth/2),(cPlayer.tPos[1] + cPlayer.iHeight/2)), (x + 14, y + 14), 2)

            #check for collisions between black rectangles
            for rRect1, rRect2 in itertools.combinations(lBlackRects, 2):
                BlackRects.fCheckCollision(rRect1, rRect2)

            #check for collisions between player and black rectangles
            for rRect in lBlackRects:
                if cPlayer.fCheckCollision(rRect):
                    sScreen.fill(BLACK)

                    #lose screen text
                    fYouLose = fLoseTextFont.render("you lose!", True, RED)
                    rRectYouLose = fYouLose.get_rect(center=(iScreenWidth/2, iScreenHeight/4))

                    fPlayAgain = fLoseTextFont.render("play again?", True, RED)
                    rRectPlayAgain = fPlayAgain.get_rect(center=(iScreenWidth/4, iScreenHeight/2))

                    sScreen.blit(fYouLose, rRectYouLose)
                    sScreen.blit(fPlayAgain, rRectPlayAgain)

                    pygame.display.flip()
                    time.sleep(3)
                    videoPlayer.play()
                    pygame.mixer.music.play(loops=-1, start=0.0)
                    gameState = GAME_OVER

            #player movement
            cPlayer.fHandleInput()
            cPlayer.fMove()

            #black rect movement
            for rect in lBlackRects:
                rect.fMove(iScreenWidth, iScreenHeight)

            #detect and execute collisions with radar and black rects
            for rect in lBlackRects:
                for i in range(100): #the detects in a 100 pixel gap
                    lineCollision = rect.bRect.clipline((
                        (cPlayer.tPos[0] + cPlayer.iWidth/2),
                        (cPlayer.tPos[1] + cPlayer.iHeight/2)),
                        (x + i, y + i))
                
                    if lineCollision:
                        rect.bLastDetected = iCurrentTime
                        tCollisionPoint = lineCollision[0]
                        lRadarHistory.append((tCollisionPoint, iCurrentTime))

            #remove old points from radar history, update transparency
            for point, timestamp in lRadarHistory[:]:
                age = iCurrentTime - timestamp
                if age > iHistoryDuration:
                    lRadarHistory.remove((point, timestamp))
                    continue

                iBlackRectTransparency = 255 - int(255 * (age / iHistoryDuration))

        elif gameState == GAME_OVER:
            if not videoPlayer.update(sScreen):
                gameState = MENU
        
        pygame.display.flip()
        cClock.tick(fps)