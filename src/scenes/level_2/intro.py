import sys

import pygame

from settings import *
from ..scene import Scene  # Importa la clase Scene desde el módulo scene.py
from game_objects.arcade.spaceships import TeslaRoadster


class IntroScene2(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        # Inicializa la escena
        self.next_scene = "Arcadedon"  # Define a qué escena cambiar después

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
        LA TIERRA SE ENFRENTA A SU DESTINO


        En los ecos de una amenaza silenciada, la humanidad se encuentra
        al borde de una guerra intergaláctica sin precedentes. 
        Tras el inesperado ataque fallido hacia la Tierra, 
        liderado por el temible General Vader, los humanos, 
        ahora conscientes de la existencia de la fuerza imperial, 
        se movilizan bajo la guía de Elon Musk. 
        Con la resolución ardiente de proteger su hogar y explorar
        los misterios de este nuevo adversario, la Tierra se convierte 
        en un hervidero de actividad científica y militar.

        Mientras tanto, en Marte, el ejército imperial se sumerge 
        en un debate interno, dividido entre aquellos que desean 
        mantener su aislamiento y los que abogan por un enfrentamiento
        directo con los humanos. La revelación accidental de su existencia
        ha desencadenado un cambio irreversible en la dinámica de poder galáctico.
        En un intento desesperado por salvaguardar sus secretos y su supervivencia, 
        el General Vader convoca a los más grandes estrategas y científicos de
        su imperio para idear un plan que asegure la victoria sobre la humanidad.

        El escenario está listo para un encuentro épico, donde la ingeniería y 
        el valor humano se enfrentarán a las avanzadas tecnologías 
        y la sabiduría milenaria del Imperio. 
        
        Código: Arcadedon
        """

        # Dividir el texto en líneas
        self.lines = self.intro_text.split('\n')

        # Configuración inicial para el desplazamiento del texto
        self.text_pos_y = HEIGHT
        self.offset = 0

        # Definimos el fondo de pantalla
        self.background = pygame.image.load(BACKGROUND_INTRO).convert_alpha()

        self.sound_narrator = pygame.mixer.Sound(LEVEL2_NARRATOR)

        # Bajamos el volumen de la musica
        pygame.mixer.music.set_volume(0.5)

        # Contador para el narrador
        self.timer = 0

        # Precargar enemigos siguiente nivel
        self.TESLA_SPRITE = pygame.image.load(ARCADE_TESLA_SPRITE).convert_alpha()  # This way only one time is loaded
        self.resources = []
        self.enemies_created = 0

    def load_resources(self):
        if self.enemies_created < LEVEL2_ENEMIES:
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
