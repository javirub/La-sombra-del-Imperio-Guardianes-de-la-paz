# intro.py

import pygame
import sys
from settings import *
from ..scene import Scene  # Importa la clase Scene desde el módulo scene.py


class IntroScene(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        # Inicializa la escena
        self.next_scene = "Deathstar"  # Define a qué escena cambiar después

        # Iniciamos el módulo mixer de pygame
        pygame.mixer.init()
        pygame.mixer.music.load(INTRO_SONG_PATH)
        pygame.mixer.music.play(-1)

        # Configuración del texto
        self.font_size = 40
        self.font = pygame.font.Font(None, self.font_size)
        self.text_color = (255, 255, 0)  # Color amarillo

        # Texto de la intro
        self.intro_text = """Hace mucho tiempo, en una galaxia muy, muy lejana...

        LA SOMBRA DEL IMPERIO
        EL FIN DEL PLANETA TIERRA


        En una galaxia no muy distante, una era de exploración y ambición
        ha llevado a la humanidad hacia los confines del espacio conocido. 
        Con la Tierra al borde de su capacidad, los ojos de la humanidad
        se fijan en Marte, el rojo y misterioso vecino, como su nueva frontera.

        Sin embargo, en las sombras de este desolado desierto se esconde un
        secreto ancestral: una base secreta imperial, testigo silencioso de un 
        poder que trasciende las estrellas. Este bastión, olvidado por eones, 
        alberga a los últimos vestigios de un ejército imperial, descendientes 
        de una civilización que una vez dominó la galaxia.
        
        Al descubrir los planes humanos de colonización, el ejército imperial 
        se enfrenta a un dilema. Temiendo que la presencia humana en Marte pueda 
        desvelar sus secretos y amenazar su existencia, deciden tomar una decisión 
        drástica: eliminar la Tierra, borrando de un solo golpe la posibilidad de 
        que los humanos alcancen su santuario marciano.
        
        Código: ElonMusk
        """

        # Dividir el texto en líneas
        self.lines = self.intro_text.split('\n')

        # Configuración inicial para el desplazamiento del texto
        self.text_pos_y = HEIGHT
        self.offset = 0

        # Definimos el fondo de pantalla
        self.background = pygame.image.load(BACKGROUND_INTRO).convert_alpha()

        self.sound_narrator = pygame.mixer.Sound(LEVEL1_NARRATOR)

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
