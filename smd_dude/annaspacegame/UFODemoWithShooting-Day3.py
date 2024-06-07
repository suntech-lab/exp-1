# Pygame Demo - Keyboard Events
# GrumpyOgre Pygame Demo

import pygame
from pygame.locals import *
import sys

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
SCREEN_DIMENSIONS = (SCREEN_WIDTH, SCREEN_HEIGHT)
FPS = 60

# define window parameters
pygame.init()
winScreen = pygame.display.set_mode(SCREEN_DIMENSIONS, 0, 32)
pygame.display.set_caption("Hello, Alien World!")
FPSspeed = pygame.time.Clock()
imgBGImage = 'space.jpg'
BG = pygame.image.load('C:/Users/annah/OneDrive/Desktop/Programming 11/UFO' + imgBGImage).convert()
pygame.mixer.pre_init(44100, -16, 2, 2048)


class MyShip():
	def __init__(self):
		self.image = pygame.image.load('C:/Users/annah/OneDrive/Desktop/Programming 11/UFO' + 'Player.png').convert_alpha()
		self.x = 557 # start player in approximate middle of x axis
		self.y = 600 # start player near the bottom of window
		self.xDirection = 0
		self.laser = pygame.mixer.Sound('C:/Users/annah/OneDrive/Desktop/Programming 11/UFO' + 'blaster.wav') 
		
		# Step 1: add this variable to your class
		# down = no shield
		# up = shield
		self.shieldstate = "down" 
		

	
	def update(self):
		# our xDirection variable will contain either a - or a + value
		# if it is a - value, adding a - value moves us to the left
		# if it is a + value, adding a + value moves us to the right
		self.x += self.xDirection
			
	def collision(self):
		# yesterday's collision stuff
		# why do you think we use < and > instead of == kinds of checks?
		'''
		the ship might skip past the value that it's x coordinate is being compared to
		this is because the ship does not move one pixel at a time
		'''
		# also, why do we check "right side" collision with 940?
		'''
		right side collision is 934 because (0, 0) in a Pygame sprite is it's very top left corner
		934 is the difference between the width of the window and the width of the sprite
		'''
		# it seems like an odd value right? Can you figure out why?
		if self.x < 0:
			self.xDirection *= -1
			self.xDirection = 0
		elif self.x > 934:
			self.xDirection *= -1
			self.xDirection = 0
			
	def draw(self):
		# pretty straight forward, draw the ship to the screen
		winScreen.blit(self.image, (self.x, self.y))
		# Step 3: add the code here to draw a circle around our ship
		# use pygame.draw.circle() and make sure you place it so that
		# the ship is in the middle and the shield moves with the
		# movement of our ship
		if self.shieldstate == "up":
			pygame.draw.circle(winScreen, color=(173, 216, 230), center=((self.x + 45), (self.y + 71.5)), radius=70)

		
class Alien():
	def __init__(self):
		self.image = pygame.image.load('C:/Users/annah/OneDrive/Desktop/Programming 11/UFO' + 'alien.png').convert_alpha()
		self.x = 50
		self.y = 50
		self.xDirection = 4  # speed and direction of horizontal movement
		self.yDirection = 20  # distance to move down when changing direction

	def update(self):
		self.x += self.xDirection
		if self.x > 925.5 or self.x < 0:  # hit the right or left wall
			self.xDirection *= -1  # change direction
			self.y += self.yDirection  # move down

	def draw(self):
		winScreen.blit(self.image, (self.x, self.y))

	
Player = MyShip()
Coolguy = Alien()
print(Coolguy.image.get_rect())

RunGame = True
while RunGame==True:
	
	
#~-~-~-~-~-~-~-~-~-~-~-~-~-EVENT PUMP-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			RunGame = False
			pygame.quit()
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_d:
				Player.xDirection = 6
			elif event.key == pygame.K_a:
				Player.xDirection = -6
			# Step 2: add another key constant to the event pump
			# this time we are looking for the right side ctrl button
			# but you could use K_SPACE or K_RSHIFT or look up your own
			# so while the right control key is down, shieldstate will 
			# be set to "up"  
			elif event.key == pygame.K_SPACE:
				Player.shieldstate = "up"
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_d or pygame.K_a:
				Player.xDirection = 0
			if event.key == pygame.K_SPACE:
				Player.shieldstate = "down" # on the release of the key turn this off
			
			
		

#~-~-~-~-~-~-~-~-~-~-~-~-~-UPDATES~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-	
	
	Player.update()
	Player.collision() 
	Coolguy.update()
	
#~-~-~-~-~-~-~-~-~-~-~-~-~-DRAWING~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-	
	winScreen.blit(BG, (0,0))
	Player.draw()	
	Coolguy.draw()
	pygame.display.update()
	FPSspeed.tick(60) # this limits our game speed to 32 fps
	




	
