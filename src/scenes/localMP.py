import sys


from game_objects.projectile import *
from settings import *
from game_objects.spaceship import TieFighter, XWing
from utils.collision import *
from scenes.scene import Scene


class LocalMPScene(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.next_scene = "menu"
        self.background = pygame.image.load(BACKGROUND_PATH).convert()
        self.bg_y = 0  # Posición inicial del fondo
        self.bgSpeed = 2  # Velocidad de desplazamiento del fondo
        self.player1 = TieFighter((100, 100), 180)
        pygame.mixer.set_num_channels(20)
        pygame.mixer.music.load(GAME_SONG_PATH)
        pygame.mixer.music.play(-1)
        self.player2 = XWing((WIDTH - 100, HEIGHT - 200), 0)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # Movimiento nave espacial teclado
        keys = pygame.key.get_pressed()
        # Controles jugador 1
        if keys[pygame.K_a]:
            self.player1.rotate(1)
        if keys[pygame.K_d]:
            self.player1.rotate(-1)

        if keys[pygame.K_w]:
            self.player1.increase_speed()
        if keys[pygame.K_s]:
            self.player1.decrease_speed()

        if keys[pygame.K_SPACE]:
            self.player1.shoot(pygame.time.get_ticks())

        # Controles jugador 2
        if keys[pygame.K_LEFT]:
            self.player2.rotate(1)
        if keys[pygame.K_RIGHT]:
            self.player2.rotate(-1)

        if keys[pygame.K_UP]:
            self.player2.increase_speed()
        if keys[pygame.K_DOWN]:
            self.player2.decrease_speed()

        if keys[pygame.K_RCTRL]:
            self.player2.shoot(pygame.time.get_ticks())

    def update(self):
        """A cada frame, realiza las comprobaciones y movimientos correspondientes."""
        '''Deprecated
        self.bg_y += self.bgSpeed
        if self.bg_y >= HEIGHT:
            self.bg_y = 0  # Reiniciar la posición del fondo para el efecto de bucle'''

        # Comprobación vida de las naves
        if self.player1.life <= 0:
            self.next_scene = "RebelWinner"
            self.done = True
        if self.player2.life <= 0:
            self.next_scene = "ImperiumWinner"
            self.done = True

        # Movimiento de los jugadores
        self.player1.update()
        self.player2.update()

        # Comprobación de colisiones
        self.check_hit()

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.player1.draw(self.screen)
        self.player2.draw(self.screen)

    def check_hit(self):
        for projectile in self.player1.projectiles:
            if check_collision(projectile.hitbox, self.player2.rect):
                self.player2.start_hit_animation()
                self.player1.projectiles.remove(projectile)
                break
        for projectile in self.player2.projectiles:
            if check_collision(projectile.hitbox, self.player1.rect):
                self.player1.start_hit_animation()
                self.player2.projectiles.remove(projectile)
                break
        if check_collision(self.player1.rect, self.player2.rect):
            # TODO: Implementar colisión entre naves espaciales
            # self.player1.start_hit_animation()
            # self.player2.start_hit_animation()
            pass
