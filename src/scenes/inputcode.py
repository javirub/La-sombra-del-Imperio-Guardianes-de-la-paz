import pygame
from settings import *
from scenes.scene import Scene
import sys


class InputCode(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.font = pygame.font.Font(FONT_PATH, 40)  # Define la fuente y tamaño del texto
        self.input_text = ''  # Texto que se va ingresando
        self.next_scene = None  # La escena a la que se navegará
        self.text_box_rect = pygame.Rect(0, 0, 600, 50)
        self.text_box_rect.center = (WIDTH // 2, HEIGHT // 2)  # Centra el rectángulo en la pantalla

    def handle_events(self):
        # Maneja la lógica de los eventos
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    self.next_scene = self.get_scene_from_code(self.input_text)
                    self.done = True
                elif event.key == pygame.K_BACKSPACE:
                    self.input_text = self.input_text[:-1]
                else:
                    self.input_text += event.unicode

    def draw(self):
        # Dibuja el fondo, el texto de entrada y cualquier otra interfaz gráfica
        self.screen.fill((0, 0, 0))  # Fondo negro, cambia según necesites
        pygame.draw.rect(self.screen, (30, 30, 30), self.text_box_rect)  # Fondo gris oscuro para el área de texto
        pygame.draw.rect(self.screen, (255, 255, 255), self.text_box_rect, 2)  # Borde blanco
        text_surface = self.font.render(self.input_text, True, (255, 255, 255))
        # Obtiene las dimensiones del texto y lo centra dentro del rectángulo
        text_rect = text_surface.get_rect(center=self.text_box_rect.center)
        self.screen.blit(text_surface, text_rect)

    def get_scene_from_code(self, code):

        if code == "estomereceun10":
            return "intro"
        elif code == "prueba":
            return "localMP"
        elif code == "largavidaalimperio":
            return "ImperiumWinner"
        elif code == "ElonMusk":
            return "Deathstar"
        elif code == "Arcadedon":
            return "Arcadedon"
        else:
            return "menu"  # Si la contraseña no coincide, vuelve al menú
