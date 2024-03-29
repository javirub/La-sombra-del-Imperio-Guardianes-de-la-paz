import pygame
from settings import WIDTH, HEIGHT, ICON_PATH
from scenes.menu import MenuScene
from scenes.level_1.intro import IntroScene
from scenes.level_1.deathstar import DeathstarScene
from scenes.localMP import LocalMPScene
from scenes.winner import RebelWinner, ImperiumWinner
from scenes.inputcode import InputCode  
from scenes.level_2.arcadedon import Arcadedon
from scenes.level_2.intro import IntroScene2

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
    # Set up the window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    # Set up the current scene
    current_scene = MenuScene(screen)

    # Set up the window title, icon and background
    pygame.display.set_caption('La sombra del Imperio: Guardianes de la paz')
    ICON = pygame.image.load(ICON_PATH)
    pygame.display.set_icon(ICON)

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
