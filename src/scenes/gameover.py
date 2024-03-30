import sys
import pygame

from settings import *
from scenes.scene import Scene  # Importa la clase Scene desde el módulo scene.py


class GameOver(Scene):
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
        self.intro_text = """GAME OVER

        La humanidad, unida bajo el estandarte de la exploración y la esperanza,
        ha enfrentado el tormento de la guerra intergaláctica, 
        emergiendo victoriosa contra un enemigo cuyo poder parecía invencible. 
        Con cada planeta salvado y cada vida preservada, 
        se ha tejido una saga de resistencia, demostrando que incluso en la oscuridad más profunda,
        la luz de la humanidad puede brillar con una fuerza que desafía a las estrellas.

        El sacrificio y la innovación han sido sus armas; 
        la solidaridad y el sueño de un futuro mejor, su escudo. 
        En este momento definitivo, Elon Musk, el arquitecto de esta nueva era, 
        se dirige a los corazones y mentes de todos los seres del cosmos, 
        proclamando que más allá de la devastación de la guerra, 
        yace la promesa de la paz y la cooperación intergaláctica.

        Hoy, mientras las naves regresan a casa y las familias se 
        reencuentran en un mundo que ha conocido el filo del abismo, 
        se cierra un capítulo de nuestra historia, pero se abre el vasto libro del mañana. 
        La victoria de la humanidad no es solo el fin del Imperio, 
        sino el amanecer de una nueva era de exploración, 
        donde los secretos del universo esperan ser descubiertos por 
        aquellos lo suficientemente valientes como para mirar hacia las estrellas. 

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

    def update(self):
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
