# menu.py

import pygame
import sys
from .scene import Scene
from settings import *

class MenuScene(Scene):
    def __init__(self, screen):
        super().__init__(screen)  # Inicializa la clase padre Scene
        # Configura aquí los elementos del menú
        self.options = ["Jugar campaña", "Multijugador local", "Multijugador en linea", "Introducir codigo", "Opciones",
                        "Salir"]
        self.font = pygame.font.Font(None, 36)
        self.current_option = 0
        self.background = pygame.image.load(BACKGROUND_MENU).convert_alpha()
        pygame.mixer.music.load(MENU_SONG_PATH)
        pygame.mixer.music.play(-1)

    def run(self):
        super().run()
        pygame.mixer.music.stop()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    self.current_option = (self.current_option - 1) % len(self.options)
                elif event.key == pygame.K_DOWN:
                    self.current_option = (self.current_option + 1) % len(self.options)
                elif event.key == pygame.K_RETURN:
                    self.option_selected()

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.draw_options()

    def draw_options(self):
        for i, option in enumerate(self.options):
            color = (255, 255, 255) if i == self.current_option else (128, 128, 128)
            text = self.font.render(option, True, color)
            text_rect = text.get_rect(center=(400, 300 + i * 50))
            self.screen.blit(text, text_rect)

    def option_selected(self):
        selected_option = self.options[self.current_option]
        if selected_option == "Jugar campaña":
            self.next_scene = "intro"
            self.done = True
        elif selected_option == "Multijugador local":
            self.next_scene = "localMP"
            self.done = True
        elif selected_option == "Opciones":
            print("Opciones")
        elif selected_option == "Multijugador en linea":
            print("Multijugador en linea")
        elif selected_option == "Introducir codigo":
            self.next_scene = "inputCode"
            self.done = True
        elif selected_option == "Salir":
            pygame.quit()
            sys.exit()
