import sys

import pygame

from settings import *
from ..scene import Scene  # Importa la clase Scene desde el módulo scene.py
from game_objects.arcade.spaceships import TeslaRoadster, ComunistSpaceship


class IntroScene4(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        # Inicializa la escena
        self.next_scene = "MilleniumFalcon"  # Define a qué escena cambiar después

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
        LA SOMBRA DEL IMPERIO
        DESTINO FINAL


        Tras el tercer ataque fallido del General Vader, la humanidad se encuentra
        unida contra su destrucción. 
        Korea del Norte, liderado por Kim Jong Ill, y Estados Unidos,
        liderado por Donald Trump, junto al magnate Elon Musk,
        han dejado de lado sus diferencias para enfrentar la amenaza imperial. 
        
        La humanidad se prepara para la batalla final,
        la batalla que decidirá el destino de la galaxia.
        
        Por su parte, el coronel Darth Vader, líder del Imperio, protegerá con su
        nave TIE Fighter a la Estrella de la Muerte, la cual se encuentra recargando
        energía para destruir la Tierra, harto de que la humanidad
        inunde el espacio con sus cohetes y basura espacial.
        
        Código: Trigonometria
        """

        # Dividir el texto en líneas
        self.lines = self.intro_text.split('\n')

        # Configuración inicial para el desplazamiento del texto
        self.text_pos_y = HEIGHT
        self.offset = 0

        # Definimos el fondo de pantalla
        self.background = pygame.image.load(BACKGROUND_INTRO).convert_alpha()

        self.sound_narrator = pygame.mixer.Sound(LEVEL4_NARRATOR)

        # Bajamos el volumen de la musica
        pygame.mixer.music.set_volume(0.5)

        # Contador para el narrador
        self.timer = 0

        # Precargar enemigos siguiente nivel
        self.TESLA_SPRITE = pygame.image.load(ARCADE_TESLA_SPRITE).convert_alpha()  # This way only one time is loaded
        self.KOREA_TANK_SPRITE = pygame.image.load(KOREA_TANK_SPRITE).convert_alpha()
        self.resources = []
        self.enemies_created = 0

    def load_resources(self):
        if self.enemies_created < LEVEL4_ENEMIES:
            if self.enemies_created % 5 == 0:
                self.resources.append(ComunistSpaceship((WIDTH - 220, 100), self.KOREA_TANK_SPRITE))
            else:
                self.resources.append(TeslaRoadster((WIDTH - 220, 100), self.TESLA_SPRITE))
            self.enemies_created += 1

    def update(self):
        self.load_resources()
        if self.timer < 230:
            self.timer += 1
        elif self.timer == 230:
            self.sound_narrator.play()
            self.timer += 1
        elif self.timer < 2500:
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

        self.text_pos_y -= 0.8  # Velocidad de desplazamiento del texto

        # Texto presione ESC para saltar parpadeante
        if self.timer % 20 < 10:
            text = self.font.render("Presione ESC para saltar", True, (255, 255, 255))
            text_rect = text.get_rect(center=(WIDTH - 300, HEIGHT - 50))
            self.screen.blit(text, text_rect)

    def run(self):
        super().run()
        self.sound_narrator.stop()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.done = True
