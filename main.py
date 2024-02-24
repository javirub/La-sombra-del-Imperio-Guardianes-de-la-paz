import pygame, sys
from pygame.locals import *

# Initialize the game

pygame.init()

SCREEN = pygame.display.set_mode((720, 1280))
pygame.display.set_caption('Game')

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()

