import pygame
import sys
from pygame.locals import *
from settings import WIDTH, HEIGHT, ICON_PATH
from scenes.intro import IntroScene
from scenes.menu import MenuScene

def main():

    # Initialize the game
    pygame.init()
    # Set up the window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    current_scene = IntroScene(screen)

    # Set up the window title, icon and background
    pygame.display.set_caption('La sombra del Imperio: Guardianes de la paz')
    ICON = pygame.image.load(ICON_PATH)
    pygame.display.set_icon(ICON)

    # Run the game loop
    while True:
        if isinstance(current_scene, IntroScene):
            next_scene = current_scene.run()
            if next_scene == "menu":
                current_scene = MenuScene(screen)
            elif isinstance(current_scene, MenuScene):
                current_scene.run()

if __name__ == "__main__":
    main()

