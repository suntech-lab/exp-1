# Pygame Demo - Keyboard Events
# GrumpyOgre Pygame Demo

import pygame, random
from pygame.locals import *
import sys



# define window parameters
# the only new things in this section are the 
# image load, and the sound mixer stuff
# External Images "must be" in the same folder as your .py file
#.convert() changes pixel format to that of the surface you are drawing to
#.convert_alpha() as above but retains transparency in image file
# IF YOU WANT TRANSPARENCY USE A PNG FILE FORMAT. 

pygame.init()
winScreen = pygame.display.set_mode((1024, 768), 0, 32)
pygame.display.set_caption("Hello, Alien World!")
FPSspeed = pygame.time.Clock()
imgBGImage = 'space.jpg'
BG = pygame.image.load('C:/Users/Eric/Desktop/FunnyPrograms/exp-1/smd_dude/annaspacegame/' + imgBGImage).convert()
pygame.mixer.pre_init(44100, -16, 2, 2048)




class MyShip():
	def __init__(self):

		self.image = pygame.image.load('C:/Users/Eric/Desktop/FunnyPrograms/exp-1/smd_dude/annaspacegame/' + 'Player.png').convert_alpha()
		self.x = random.randrange(20, 780) 	# start player somewhere on the horizontal axis
		self.y = 600						# start player near the bottom of window
		self.xDirection = 0
		self.laser = pygame.mixer.Sound('C:/Users/Eric/Desktop/FunnyPrograms/exp-1/smd_dude/annaspacegame/' + 'blaster.wav') 

	
	def update(self):
		# our xDirection variable will contain either a - or a + value
		# if it is a - value, adding a - value moves us to the left
		# if it is a + value, adding a + value moves us to the right
		self.x += self.xDirection
			
	def collision(self):
		pass
		# create a "wall collision" codeblock here (replace "pass" with your code)
		# the idea is simple enough, make sure the player ship doesn't
		# go past the right wall or the left wall. It should "bounce"
		# off the wall when it hits it. 
	
		
		
	def draw(self):
		# pretty straight forward, draw the ship to the screen
		winScreen.blit(self.image, (self.x, self.y))
		


	
Player = MyShip()

RunGame = True
while RunGame==True:
	
	
#~-~-~-~-~-~-~-~-~-~-~-~-~-EVENT PUMP-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			RunGame = False
			pygame.quit()
			sys.exit()

		elif event.type == pygame.KEYDOWN:
			# notice below that I've put the if statement and its
			# codeblock on the same line. This is good practice
			# if your code block is just a single line			
			if event.key == pygame.K_d:Player.xDirection = 6
			elif event.key == pygame.K_a: Player.xDirection = -6
		

#~-~-~-~-~-~-~-~-~-~-~-~-~-UPDATES~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-	
	
	Player.update()
	# call your player collision function here. 
 
	
#~-~-~-~-~-~-~-~-~-~-~-~-~-DRAWING~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-~-	
	winScreen.blit(BG, (0,0))
	Player.draw()	
	pygame.display.update()
	FPSspeed.tick(32) # this limits our game speed to 32 fps
	




	
