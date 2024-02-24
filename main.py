import pygame, sys
from pygame.locals import *

# Initialize the game

pygame.init()

SCREEN = pygame.display.set_mode((720, 1280))
pygame.display.set_caption('Game')

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)

SCREEN.fill(WHITE)

# Draw a rectangle TODO: put the player sprite here
player = pygame.draw.rect(SCREEN, RED, (300, 1100, 100, 100))

# Test bullet TODO: put the bullet sprite here, and make it move
bullet1 = pygame.draw.line(SCREEN, BLACK, (320, 1100), (320, 1000), 5)
bullet2 = pygame.draw.line(SCREEN, BLACK, (380, 1100), (380, 1000), 5)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

