'''
Pygame 1-1 GameDesign12 Assignment
Eric Liu
12/03/2025
'''

import pygame

class Circle():
    def __init__(self, surface, color, center, radius, width):
        self.surface = surface
        self.color = color
        self.center = center
        self.radius = radius
        self.width = width

    def draw(self, surface):
        #pre: needs the surface to draw on
        #post: draws a cCircle on the surface
        pygame.draw.circle(surface, self.color, self.center, self.radius, self.width)

class Ellipse():
    def __init__(self, surface, color, rect, width):
        self.surface = surface
        self.color = color
        self.rect = rect
        self.width = width

    def draw(self, surface):
        #pre: needs the surface to draw on
        #post: draws an eEllipse on the surface
        pygame.draw.ellipse(surface, self.color, self.rect, self.width)

class Rect():
    def __init__(self, surface, color, rect, width):
        self.surface = surface
        self.color = color
        self.rect = rect
        self.width = width

    def draw(self, surface):
        #pre: needs the surface to draw on
        #post: draws a rectangle (or rSquare) on the surface
        pygame.draw.rect(surface, self.color, self.rect, self.width)

class Line():
    def __init__(self, surface, color, start_pos, end_pos, width):
        self.surface = surface
        self.color = color
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.width = width

    def draw(self, surface):
        #pre: needs the surface to draw on
        #post: draws a lLine on the surface
        pygame.draw.line(surface, self.color, self.start_pos, self.end_pos, self.width)

class Polygon():
    def __init__(self, surface, color, points, width):
        self.surface = surface
        self.color = color
        self.points = points
        self.width = width

    def draw(self, surface):
        #pre: needs the surface to draw on
        #post: draws a polygon on the surface
        pygame.draw.polygon(surface, self.color, self.points, self.width)
        

if __name__ == "__main__":
    pygame.init()
    tBlack = (0, 0, 0)
    tGreen = (0, 255, 0)
    tBlue = (0, 0, 255)
    tWhite = (255, 255, 255)

    iScreenWidth = 400
    iScreenHeight = 400

    dScreen = pygame.display.set_mode((iScreenWidth, iScreenHeight))
    bRunning = True
    pPentagon = Polygon(dScreen, tBlue, [(200, 0), (400, 150), (350, 400), (50, 400), (0, 150)], 5)
    cCircle = Circle(dScreen, tBlack, (200, 205), 50, 5)
    eEllipse = Ellipse(dScreen, tBlue, ((20, 150), (300, 160)), 5)
    rSquare = Rect(dScreen, tGreen, ((230, 60), (80, 80)), 5)
    lLine = Line(dScreen, tBlack, (230, 100), (310, 100), 5)
    cClock = pygame.time.Clock()

    while bRunning:
        dScreen.fill(tWhite)

        for event in pygame.event.get():
            if event == pygame.QUIT:
                bRunning = False

        cCircle.draw(dScreen)
        rSquare.draw(dScreen)
        eEllipse.draw(dScreen)
        lLine.draw(dScreen)
        pPentagon.draw(dScreen)

        pygame.display.flip()
        cClock.tick(60)
    
    pygame.quit()

    quit()

        