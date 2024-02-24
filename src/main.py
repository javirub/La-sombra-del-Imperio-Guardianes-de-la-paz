import pygame, sys
from pygame.locals import *

# Initialize the game
pygame.init()

# Define constants
WIDTH, HEIGHT = 576, 1024
FPS = 144
CLOCK = pygame.time.Clock()

# Set up the window
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))

# Set up the window title, icon and background
pygame.display.set_caption('Game')
ICON = pygame.image.load('assets/images/other/icon.png')
pygame.display.set_icon(ICON)
BACKGROUND = pygame.image.load('assets/images/backgrounds/Starfield 1.png').convert()

# Init y
y = 0

# Run the game loop
while True:
    for event in pygame.event.get():

        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Adds background scrolling
    relative_y = y % BACKGROUND.get_rect().height
    SCREEN.blit(BACKGROUND, (0, (relative_y - BACKGROUND.get_rect().height)))
    y += 0.1
    if relative_y < HEIGHT:
        SCREEN.blit(BACKGROUND, (0, relative_y))

    # Updates the display and sets the FPS
    pygame.display.update()
    CLOCK.tick(FPS)
