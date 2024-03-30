import pygame

from scenes.inputcode import InputCode
from scenes.level_1.deathstar import DeathstarScene
from scenes.level_1.intro import IntroScene
from scenes.level_2.arcadedon import Arcadedon
from scenes.level_2.intro import IntroScene2
from scenes.localMP import LocalMPScene
from scenes.menu import MenuScene
from scenes.winner import RebelWinner, ImperiumWinner
from settings import *


def get_scene_by_name(scene_name, screen):
    if scene_name == "menu":
        return MenuScene(screen)
    elif scene_name == "intro":
        return IntroScene(screen)
    elif scene_name == "intro2":
        return IntroScene2(screen)
    elif scene_name == "Deathstar":
        return DeathstarScene(screen)
    elif scene_name == "localMP":
        return LocalMPScene(screen)
    elif scene_name == "RebelWinner":
        return RebelWinner(screen)
    elif scene_name == "ImperiumWinner":
        return ImperiumWinner(screen)
    elif scene_name == "inputCode":
        return InputCode(screen)
    elif scene_name == "Arcadedon":
        return Arcadedon(screen)
    else:
        return MenuScene(screen)


def main():
    # Initialize the game
    pygame.init()
    # Set up the screen on full screen mode, changing the resolution to 1920x1080
    screen = pygame.display.set_mode((WIDTH, HEIGHT), pygame.FULLSCREEN)
    # Hide the cursor
    pygame.mouse.set_visible(False)

    # Set up the current scene
    current_scene = MenuScene(screen)

    # Set up the window title, icon and background
    pygame.display.set_caption('La sombra del Imperio: Guardianes de la paz')
    icon = pygame.image.load(ICON_PATH)
    pygame.display.set_icon(icon)

    # Run the game loop
    while True:
        current_scene.run()
        if current_scene.done:
            next_scene = current_scene.next_scene
            current_scene = get_scene_by_name(next_scene, screen)
            if current_scene is None:
                break


if __name__ == "__main__":
    main()
