import pygame
from settings import WIDTH, HEIGHT, ICON_PATH
from scenes.intro import IntroScene
from scenes.menu import MenuScene
from scenes.game import GameScene
from scenes.localMP import LocalMPScene

def get_scene_by_name(scene_name, screen):
    if scene_name == "menu":
        return MenuScene(screen)
    elif scene_name == "game":
        return GameScene(screen)
    elif scene_name == "intro":
        return IntroScene(screen)
    elif scene_name == "localMP":
        return LocalMPScene(screen)
    # Añade más escenas aquí según sea necesario
    else:
        return None


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
