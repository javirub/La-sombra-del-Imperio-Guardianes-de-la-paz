import pygame

from scenes.inputcode import InputCode
from scenes.level_1.deathstar import DeathstarScene
from scenes.level_1.intro import IntroScene
from scenes.level_2.arcadedon import Arcadedon
from scenes.level_2.intro import IntroScene2
from scenes.level_3.deathstar import DeathstarScene2
from scenes.level_4.intro import IntroScene3
from scenes.level_4.arcadedon import Arcadedon_with_steroids
from scenes.level_5.deathstar import DeathstarScene3
from scenes.level_6.intro import IntroScene4
from scenes.level_6.final import FinalBattle
from scenes.localMP import LocalMPScene
from scenes.menu import MenuScene
from scenes.winner import RebelWinner, ImperiumWinner
from scenes.level_2.gameover import GameOver1
from scenes.level_4.gameover2 import GameOver2
from scenes.level_6.gameover3 import GameOver3
from scenes.gameover import GameOver
from settings import *


def get_scene_by_name(scene_name, screen, resources=None):
    # Menu
    if scene_name == "menu":
        return MenuScene(screen)
    elif scene_name == "inputCode":
        return InputCode(screen)
    # Story
    elif scene_name == "intro":
        return IntroScene(screen)
    # Checkpoint 0
    elif scene_name == "Deathstar":
        return DeathstarScene(screen)
    elif scene_name == "intro2":
        return IntroScene2(screen)
    # Checkpoint 1
    elif scene_name == "Arcadedon":
        return Arcadedon(screen, resources)
    elif scene_name == "Deathstar2":
        return DeathstarScene2(screen)
    elif scene_name == "intro3":
        return IntroScene3(screen)
    # Checkpoint 2
    elif scene_name == "Arcadedon2":
        return Arcadedon_with_steroids(screen, resources)
    elif scene_name == "Deathstar3":
        return DeathstarScene3(screen)
    elif scene_name == "intro4":
        return IntroScene4(screen)
    # Checkpoint 3
    elif scene_name == "final":
        return FinalBattle(screen)
    # Gameover
    elif scene_name == "Gameover1":
        return GameOver1(screen)
    elif scene_name == "Gameover2":
        return GameOver2(screen)
    elif scene_name == "Gameover3":
        return GameOver3(screen)
    elif scene_name == "Gameover":
        return GameOver(screen)
    # Multiplayer
    elif scene_name == "localMP":
        return LocalMPScene(screen)
    elif scene_name == "RebelWinner":
        return RebelWinner(screen)
    elif scene_name == "ImperiumWinner":
        return ImperiumWinner(screen)
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
    # current_scene = MenuScene(screen)
    current_scene = FinalBattle(screen)
    # Set up the window title, icon and background
    pygame.display.set_caption('La sombra del Imperio: Guardianes de la paz')
    icon = pygame.image.load(ICON_PATH)
    pygame.display.set_icon(icon)

    # Run the game loop
    while True:
        current_scene.run()
        if current_scene.done:
            next_scene = current_scene.next_scene
            try:
                current_scene = get_scene_by_name(next_scene, screen, current_scene.resources)
            except AttributeError:
                current_scene = get_scene_by_name(next_scene, screen)
                if current_scene is None:
                    break
            except Exception as e:
                print(f"Game raised an exception: {e}\n"
                      f"So we are going to the menu scene")
                current_scene = MenuScene(screen)


if __name__ == "__main__":
    main()
