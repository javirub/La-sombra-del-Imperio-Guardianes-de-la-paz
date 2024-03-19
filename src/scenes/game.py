import sys

import src.settings
from src.game_objects.projectile import *
from src.scenes.scene import Scene
from src.settings import *
from src.game_objects.spaceship import TieFighter, XWing


class GameScene(Scene):
    def __init__(self, screen):
        super().__init__(screen)  # Inicializa la clase padre Scene
        self.next_scene = "menu"
        self.background = pygame.image.load(BACKGROUND_PATH).convert()
        self.bg_y = 0  # Posición inicial del fondo
        self.bgSpeed = 2  # Velocidad de desplazamiento del fondo
        self.player = TieFighter((WIDTH // 2, HEIGHT - 100), 0)
        self.player_projectiles = []
        pygame.mixer.set_num_channels(20)
        pygame.mixer.music.load('../assets/music/game_song.ogg')
        pygame.mixer.music.play(-1)
        # TODO: Añadir enemigos "en pruebas".
        self.enemy_projectiles = []
        self.enemy = XWing((WIDTH // 2, 100), 0)

    def run(self):
        super().run()
        pygame.mixer.music.stop()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # Movimiento nave espacial teclado
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.player.rotate(1)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.player.rotate(-1)

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.player.increase_speed()
        if keys[pygame.K_DOWN] or keys[pygame.K_s]:
            self.player.decrease_speed()

        if keys[pygame.K_SPACE]:
            if self.player.shoot(pygame.time.get_ticks()):
                # Posición inicial proyectiles
                start_pos_left = (self.player.rect.centerx, self.player.rect.centery)
                start_pos_right = (self.player.rect.centerx, self.player.rect.centery)

                # Crear proyectiles
                projectile_left = Projectile(start_pos_left, self.player.radians, (0, 255, 0))
                projectile_right = Projectile(start_pos_right, self.player.radians, (0, 255, 0))

                # Añadir proyectiles a la lista después de crear ambos (para evitar desincronización)
                self.player_projectiles.extend([projectile_left, projectile_right])

    def update(self):
        # Actualizar la posición del fondo para que se desplace
        self.bg_y += self.bgSpeed
        self.player.move_forward()
        if self.bg_y >= HEIGHT:
            self.bg_y = 0  # Reiniciar la posición del fondo para el efecto de bucle

        # Actualizar la posición de los proyectiles
        for projectile in self.player_projectiles:
            projectile.update()
            if projectile.y < 0:
                self.player_projectiles.remove(projectile)

        for projectile in self.enemy_projectiles:
            projectile.update()
            if projectile.y > HEIGHT:
                self.enemy_projectiles.remove(projectile)

    def draw(self):
        ''' Deprecated, antes iba a ser un juego de scroll vertical
        self.screen.blit(self.background, (0, self.bg_y - HEIGHT))
        self.screen.blit(self.background, (0, self.bg_y))'''
        self.screen.blit(self.background, (0, 0))
        self.player.draw(self.screen)
        self.enemy.draw(self.screen)
        for projectile in self.player_projectiles:
            projectile.draw(self.screen)

        for projectile in self.enemy_projectiles:
            projectile.draw(self.screen)
