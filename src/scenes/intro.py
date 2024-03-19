# intro.py

import pygame
import sys
from src.settings import WIDTH, HEIGHT  # Asegúrate de definir estas constantes en settings.py
from .scene import Scene  # Importa la clase Scene desde el módulo scene.py


class IntroScene(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        # Inicializa la escena
        self.next_scene = "game"  # Define a qué escena cambiar después

        # Iniciamos el módulo mixer de pygame
        pygame.mixer.init()
        pygame.mixer.music.load('../assets/music/intro_song.ogg')
        pygame.mixer.music.play(-1)

        # Configuración del texto
        self.font_size = 40
        self.font = pygame.font.Font(None, self.font_size)
        self.text_color = (255, 255, 0)  # Color amarillo

        # Texto de la intro
        intro_text = """Hace mucho tiempo, en una galaxia muy, muy lejana...

        LA SOMBRA DEL IMPERIO
        GUARDIANES DE LA PAZ


        En una galaxia donde reina una paz forjada por la inquebrantable
        dominación del Imperio Galáctico, un valiente piloto de TIE, bajo la
        sombra del legendario Darth Vader, vuela a través de los confines
        estelares. Este piloto, un defensor del orden imperial, se enfrenta a la
        disidencia que amenaza la tranquilidad impuesta por el imperio. A bordo
        de su veloz caza TIE, ejecuta con precisión las órdenes de Vader,
        dedicado a preservar la estabilidad que el Imperio ofrece a las
        innumerables civilizaciones bajo su manto.

        En esta era de paz vigilada, los rebeldes, vistos como agentes del caos,
        intentan desestabilizar la armonía que el Imperio ha trabajado arduamente
        para establecer. Nuestro piloto se ve inmerso en una lucha no solo física
        sino también ideológica, donde cada misión es una oportunidad para
        demostrar la superioridad del orden sobre el caos.

        La galaxia, un vasto lienzo de estrellas y misterios, es testigo de esta
        tensión creciente. En el corazón de esta lucha, el piloto emerge como un
        campeón del orden, enfrentando valientemente a aquellos que desearían ver
        desmoronarse la estructura sobre la cual se ha construido la paz. Este es
        el relato de un guardián del imperio, un narrador de la historia desde las
        líneas del frente, donde la verdad se cuenta en el silencio entre disparos
        de bláster."""

        # Dividir el texto en líneas
        self.lines = intro_text.split('\n')

        # Configuración inicial para el desplazamiento del texto
        self.text_pos_y = HEIGHT
        self.offset = 0

        # Definimos el fondo de pantalla
        self.background = pygame.image.load('../assets/images/backgrounds/bgIntro.jpg').convert_alpha()

        self.sound_narrator = pygame.mixer.Sound('../assets/sounds/narradorIntro.mp3')

        # Bajamos el volumen de la musica
        pygame.mixer.music.set_volume(0.5)

        # Contador para el narrador
        self.timer = 0

    def update(self):
        if self.timer < 230:
            self.timer += 1
        elif self.timer == 230:
            self.sound_narrator.play()
            self.timer += 1
        elif self.timer < 2000:
            self.timer += 1
        else:
            self.done = True

    def draw(self):
        self.screen.blit(self.background, (0, 0))  # Fondo estrellas

        # Renderizar el texto
        for i, line in enumerate(self.lines):
            line_surf = self.font.render(line, True, self.text_color)
            line_pos = line_surf.get_rect(center=(WIDTH / 2, self.text_pos_y + i * self.font_size - self.offset))
            self.screen.blit(line_surf, line_pos)

        self.text_pos_y -= 0.5  # Velocidad de desplazamiento del texto
        self.offset += 0.5  # Incremento para crear el efecto de perspectiva

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
