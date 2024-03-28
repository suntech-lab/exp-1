import pygame
import os
import random
from pygame.locals import (
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
)

pygame.init()
pygame.display.set_caption('erics game')

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.surf = pygame.transform.scale(pygame.image.load(os.path.join('pygame', 'yellow (2).png')), (40, 40))
        self.rect = self.surf.get_rect(center = (SCREEN_WIDTH/2, SCREEN_HEIGHT/2))

    def update(self, pressed_keys):
        if pressed_keys[K_UP]:
            if self.rect.bottom == SCREEN_HEIGHT:
                self.rect.move(0, -10)
        if pressed_keys[K_DOWN]:
            self.rect.move_ip(0, 3)
        if pressed_keys[K_LEFT]:
            self.rect.move_ip(-3, 0)
        if pressed_keys[K_RIGHT]:
            self.rect.move_ip(3, 0)

        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > SCREEN_WIDTH:
            self.rect.right = SCREEN_WIDTH
        if self.rect.top <= 0:
            self.rect.top = 0
        if self.rect.bottom >= SCREEN_HEIGHT:
            self.rect.bottom = SCREEN_HEIGHT

        self.rect.clamp_ip(screen.get_rect())

class Object(pygame.sprite.Sprite):
    def __init__(self):
        super(Object, self).__init__()
        self.surf = pygame.transform.scale(pygame.image.load(os.path.join('pygame', 'whitecircle.png')), (50, 50))
        self.rect = self.surf.get_rect()
        self.spawn()

    def spawn(self):
        self.rect.x = random.randint(0, SCREEN_WIDTH - self.rect.width)
        self.rect.y = 0

    def update(self):
        self.rect.move_ip(0, 7)

SPAWN_OBJECT = pygame.USEREVENT + 1
pygame.time.set_timer(SPAWN_OBJECT, 100)

player = Player()
object = Object()


objects = []

player_x, player_y = (SCREEN_WIDTH - 40) // 2, SCREEN_HEIGHT - 40 - 20

running = True

while running:

    screen.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == KEYDOWN:
            if event.key == K_ESCAPE:
                running = False

        elif event.type == QUIT:
            running = False

        elif event.type == SPAWN_OBJECT:
            new_object = Object()
            new_object.spawn()
            objects.append(new_object)

    pressed_keys = pygame.key.get_pressed()

    if player.rect.bottom != SCREEN_HEIGHT:
        player.rect.move_ip(0, 3)
    player.update(pressed_keys)

    for obj in objects:
        obj.update()
        if obj.rect.top >= SCREEN_HEIGHT:
            objects.remove(obj)

    screen.blit(player.surf, player.rect)
    
    for obj in objects:
        screen.blit(obj.surf, obj.rect)

    pygame.display.flip()

    pygame.time.Clock().tick(100)


running = False
