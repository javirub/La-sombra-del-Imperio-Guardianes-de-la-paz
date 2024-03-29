import sys
from settings import *
from utils.collision import *
from .scene import Scene


class Winner(Scene):
    """Escena de victoria de jugador padre."""

    def __init__(self, screen):
        super().__init__(screen)
        self.next_scene = "menu"
        # Configura aquí los elementos del menú
        self.options = ["Jugar otra vez", "Volver al menu", "Salir del juego"]
        self.font = pygame.font.Font(None, 36)
        self.current_option = 0
        self.background = pygame.image.load(BACKGROUND_PATH).convert_alpha()
        self.song = IMPERIUM_WINNER_SONG_PATH
        pygame.mixer.music.load(self.song)
        pygame.mixer.music.play(-1)
        self.winner = "Ha vencido el VENCEDOR"

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
        # Dibujar opciones
        for i, option in enumerate(self.options):
            color = (255, 255, 255) if i == self.current_option else (128, 128, 128)
            text = self.font.render(option, True, color)
            text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2 + i * 50))
            self.screen.blit(text, text_rect)
        # Dibujar ganador
        text = self.font.render(self.winner, True, (255, 255, 255))
        text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT / 2 - 100))
        self.screen.blit(text, text_rect)

    def option_selected(self):
        selected_option = self.options[self.current_option]
        if selected_option == "Jugar otra vez":
            self.next_scene = "localMP"
            self.done = True
        elif selected_option == "Volver al menu":
            self.next_scene = "menu"
            self.done = True
        elif selected_option == "Salir del juego":
            pygame.quit()
            sys.exit()


class ImperiumWinner(Winner):
    """Escena de victoria del Imperio."""

    def __init__(self, screen):
        super().__init__(screen)
        self.winner = "Ha vencido el Imperio"
        self.song = IMPERIUM_WINNER_SONG_PATH
        pygame.mixer.music.load(self.song)
        pygame.mixer.music.play(-1)


class RebelWinner(Winner):
    """Escena de victoria de la Rebelión."""

    def __init__(self, screen):
        super().__init__(screen)
        self.winner = "Ha vencido la Rebelión"
        self.song = REBEL_WINNER_SONG_PATH
        pygame.mixer.music.load(self.song)
        pygame.mixer.music.play(-1)
