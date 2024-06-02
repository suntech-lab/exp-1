# Pygame Demo - Keyboard Events
# GrumpyOgre Pygame Demo

import pygame, random
from pygame.locals import *
import sys

SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
SCREEN_DIMENSIONS = (SCREEN_WIDTH, SCREEN_HEIGHT)
FPS = 60

# define window parameters
# the only new things in this section are the 
# image load, and the sound mixer stuff
# External Images "must be" in the same folder as your .py file
#.convert() changes pixel format to that of the surface you are drawing to
#.convert_alpha() as above but retains transparency in image file
# IF YOU WANT TRANSPARENCY USE A PNG FILE FORMAT. 

pygame.init()
winScreen = pygame.display.set_mode(SCREEN_DIMENSIONS, 0, 32)
pygame.display.set_caption("SPACE INVADERS!!!")
FPSspeed = pygame.time.Clock()
imgBGImage = 'space.jpg'
BG = pygame.image.load('C:/Users/Eric/Desktop/FunnyPrograms/exp-1/smd_dude/annaspacegame/' + imgBGImage).convert()
pygame.mixer.pre_init(44100, -16, 2, 2048)




class MyShip():
	def __init__(self):

		self.image = pygame.image.load('C:/Users/Eric/Desktop/FunnyPrograms/exp-1/smd_dude/annaspacegame/' + 'Player.png').convert_alpha()
		self.x = 470 # start player in approximate middle of x axis
		self.y = 600 # start player near the bottom of window
		self.xDirection = 0
		self.laser = pygame.mixer.Sound('C:/Users/Eric/Desktop/FunnyPrograms/exp-1/smd_dude/annaspacegame/' + 'blaster.wav') 

	
	def update(self):
		self.x += self.xDirection
			
	def collision(self):
		if self.x < 0:
			self.x = 0
		elif self.x > 1024 - 90:
			self.x = 1024 - 90
		
	def draw(self):
		# pretty straight forward, draw the ship to the screen
		winScreen.blit(self.image, (self.x, self.y))
		

	
Player = MyShip()

print(Player.image.get_rect())

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
		
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_d or pygame.K_a:
				Player.xDirection = 0
		

#~-~-~-~-~-~-~-~-~-~-~-~-~-UPDATES~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-	
	
	Player.update()
	Player.collision()
 
#~-~-~-~-~-~-~-~-~-~-~-~-~-DRAWING~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-	
	winScreen.blit(BG, (0,0))
	Player.draw()	
	pygame.display.update()
	FPSspeed.tick(60) # this limits our game speed to 32 fps
	




	
