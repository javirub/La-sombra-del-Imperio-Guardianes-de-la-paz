import pygame
from src.settings import *

class InputCode:
    def __init__(self, screen):
        self.screen = screen
        self.done = False
        self.font = pygame.font.Font(None, 50)  # Define la fuente y tamaño del texto
        self.input_text = ''  # Texto que se va ingresando
        self.next_scene = ''  # La escena a la que se navegará
        self.text_box_rect = pygame.Rect(0, 0, 600, 50)
        self.text_box_rect.center = (WIDTH // 2, HEIGHT // 2)  # Centra el rectángulo en la pantalla

    def run(self):
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                elif event.type == pygame.KEYDOWN:
                    self.handle_event(event)
            self.update()
            self.draw()
            pygame.display.flip()
            pygame.time.Clock().tick(FPS)

    def handle_event(self, event):
        # Maneja los eventos de teclado
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                # Aquí defines la lógica para decidir a qué escena ir basado en la contraseña
                self.next_scene = self.get_scene_from_code(self.input_text)
                self.done = True
            elif event.key == pygame.K_BACKSPACE:
                self.input_text = self.input_text[:-1]
            else:
                self.input_text += event.unicode

    def update(self):
        # Actualiza cualquier lógica de la escena si es necesario
        pass

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

        else:
            return "menu"  # Si la contraseña no coincide, vuelve al menú
