# file: simple_2d_game.py
import pygame
import random
import sys

# Initialize Pygame
pygame.init()

# Screen settings
SCREEN_WIDTH, SCREEN_HEIGHT = 800, 600
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Collect Items and Avoid Obstacles")

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

# Game settings
PLAYER_SIZE = 50
OBSTACLE_SIZE = 30
ITEM_SIZE = 20
SPEED = 5
OBSTACLE_COUNT = 5
ITEM_COUNT = 10

# Initialize player
player_pos = [SCREEN_WIDTH // 2, SCREEN_HEIGHT - 2 * PLAYER_SIZE]

# Initialize items and obstacles
items = [[random.randint(0, SCREEN_WIDTH - ITEM_SIZE), random.randint(0, SCREEN_HEIGHT - ITEM_SIZE)] for _ in range(ITEM_COUNT)]
obstacles = [[random.randint(0, SCREEN_WIDTH - OBSTACLE_SIZE), random.randint(0, SCREEN_HEIGHT - OBSTACLE_SIZE)] for _ in range(OBSTACLE_COUNT)]

# Game variables
score = 0
game_over = False

# Game loop
clock = pygame.time.Clock()
while not game_over:
    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Player movement
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player_pos[0] > 0:
        player_pos[0] -= SPEED
    if keys[pygame.K_RIGHT] and player_pos[0] < SCREEN_WIDTH - PLAYER_SIZE:
        player_pos[0] += SPEED
    if keys[pygame.K_UP] and player_pos[1] > 0:
        player_pos[1] -= SPEED
    if keys[pygame.K_DOWN] and player_pos[1] < SCREEN_HEIGHT - PLAYER_SIZE:
        player_pos[1] += SPEED

    # Check for collisions with items
    for item in items[:]:
        if (player_pos[0] < item[0] + ITEM_SIZE and
            player_pos[0] + PLAYER_SIZE > item[0] and
            player_pos[1] < item[1] + ITEM_SIZE and
            player_pos[1] + PLAYER_SIZE > item[1]):
            items.remove(item)
            score += 1

    # Check for collisions with obstacles
    for obstacle in obstacles:
        if (player_pos[0] < obstacle[0] + OBSTACLE_SIZE and
            player_pos[0] + PLAYER_SIZE > obstacle[0] and
            player_pos[1] < obstacle[1] + OBSTACLE_SIZE and
            player_pos[1] + PLAYER_SIZE > obstacle[1]):
            game_over = True

    # Win condition
    if score == ITEM_COUNT:
        print("You Win!")
        pygame.quit()
        sys.exit()

    # Clear screen
    SCREEN.fill(BLACK)

    # Draw player
    pygame.draw.rect(SCREEN, GREEN, (player_pos[0], player_pos[1], PLAYER_SIZE, PLAYER_SIZE))

    # Draw items
    for item in items:
        pygame.draw.rect(SCREEN, WHITE, (item[0], item[1], ITEM_SIZE, ITEM_SIZE))

    # Draw obstacles
    for obstacle in obstacles:
        pygame.draw.rect(SCREEN, RED, (obstacle[0], obstacle[1], OBSTACLE_SIZE, OBSTACLE_SIZE))

    # Update display
    pygame.display.flip()

    # Frame rate
    clock.tick(30)

# End the game
pygame.quit()
