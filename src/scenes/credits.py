import sys

import pygame

from settings import *
from .scene import Scene  # Importa la clase Scene desde el módulo scene.py


class Credits(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        # Inicializa la escena
        self.next_scene = "menu"  # Define a qué escena cambiar después

        # Iniciamos el módulo mixer de pygame
        pygame.mixer.init()
        pygame.mixer.music.load(INTRO_SONG_PATH)
        pygame.mixer.music.play(-1)

        # Configuración del texto
        self.font_size = 40
        self.font = pygame.font.Font(None, self.font_size)
        self.text_color = (255, 255, 0)  # Color amarillo

        # Texto de la intro
        self.intro_text = """
        THE END
        
        
        
        
        DEVELOPED BY:
        - Javier Rubio Roca
        
        
        GAME PROGRAMMER:
        - Javier Rubio Roca
        
        
        GAME DESIGNER:
        - Javier Rubio Roca
        
        
        GRAPHIC DESIGNER:
        - Random Google Images
        - DALL-E
        - RemoveBG
        
        
        SCRIPT WRITER:
        - Javier Rubio Roca aided by ChatGPT
        
        
        MUSIC COMPOSER:
        - Carl Orff for O Fortuna
        - John Williams for Star Wars themes
        
        
        SPECIAL THANKS:
        - Ivan Fuertes Torrecilla as teacher for introduction to game development
        - Javier Rubio Roca for making possible to hear sounds in the outer space
        - Pygame and moviepy libraries
        - Team America for the character Kim Jong Il
        - Elon Musk for the character Elon Musk and the Tesla Roadster Spaceship
        - Donald Trump for the character Donald Trump
        - George Lucas for the Star Wars franchise
        - Leonhard Euler for the Euler's formula
        - Github Copilot for the code suggestions
        - Pycharm for leave students use the professional version for free
        
        
        Disclaimer:
        This game is a non-profit educational project.
        Every character and image used in this game is for educational purposes only.
        It is not intended to be shared or distributed as there are several copyrighted images
        and real life characters used without permission.
        
        Código: estomereceun10
        """

        # Dividir el texto en líneas
        self.lines = self.intro_text.split('\n')

        # Configuración inicial para el desplazamiento del texto
        self.text_pos_y = HEIGHT
        self.offset = 0

        # Definimos el fondo de pantalla
        self.background = pygame.image.load(BACKGROUND_INTRO).convert_alpha()


        # Bajamos el volumen de la musica
        pygame.mixer.music.set_volume(0.5)

        # Contador para el narrador
        self.timer = 0

    def update(self):
        if self.timer < 6000:
            self.timer += 1
        else:
            self.done = True

    def draw(self):
        self.screen.blit(self.background, (0, 0))  # Fondo estrellas

        # Renderizar el texto
        for i, line in enumerate(self.lines):
            line_surf = self.font.render(line, True, self.text_color)
            line_pos = line_surf.get_rect(center=(WIDTH / 2, self.text_pos_y + i * self.font_size))
            self.screen.blit(line_surf, line_pos)

        self.text_pos_y -= 0.5  # Velocidad de desplazamiento del texto

        # Texto presione ESC para saltar parpadeante
        if self.timer % 20 < 10:
            text = self.font.render("Presione ESC para saltar", True, (255, 255, 255))
            text_rect = text.get_rect(center=(WIDTH - 300, HEIGHT - 50))
            self.screen.blit(text, text_rect)

    def run(self):
        super().run()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.done = True
