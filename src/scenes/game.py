import sys

import pygame

from src.game_objects.projectile import Projectile, EnemyProjectile
from src.settings import WIDTH, HEIGHT, BACKGROUND_PATH
from src.game_objects.spaceship import TieFighter, XWing


class GameScene:
    def __init__(self, screen):
        self.screen = screen
        self.done = False
        self.next_scene = "menu"
        self.background = pygame.image.load(BACKGROUND_PATH).convert()
        self.bg_y = 0  # Posición inicial del fondo
        self.bgSpeed = 2  # Velocidad de desplazamiento del fondo
        self.player = TieFighter((WIDTH // 2, HEIGHT - 100))
        self.player_projectiles = []
        pygame.mixer.set_num_channels(20)
        # TODO: Añadir enemigos "en pruebas".
        self.enemy_projectiles = []
        self.enemy = XWing((WIDTH // 2, 100))
        pygame.mixer.music.load('../assets/music/game_song.ogg')
        pygame.mixer.music.play(-1)

    def run(self):
        while not self.done:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
            pygame.time.Clock().tick(60) / 1000.0
        pygame.mixer.music.stop()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
        # Movimiento nave espacial teclado
        keys = pygame.key.get_pressed()
        dx, dy = 0, 0  # Desplazamiento en x y y

        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
            self.player.rotate(1)
        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
            self.player.rotate(-1)

        if keys[pygame.K_UP] or keys[pygame.K_w]:
            self.player.move_forward()  # TODO: self.player.speedup() Para acelerar la nave
        # if keys[pygame.K_DOWN] or keys[pygame.K_s]:
        # TODO: self.player.slowdown() Para frenar la nave

        if keys[pygame.K_z]:
            if self.enemy.shoot(pygame.time.get_ticks()):
                # Posición inicial proyectiles
                if self.enemy.left:
                    start_pos_left = (self.enemy.rect.midbottom[0] - 85, self.enemy.rect.midbottom[1] - 20)
                    enemy_projectile_left = EnemyProjectile(start_pos_left)
                    self.enemy.left = False
                    self.enemy_projectiles.append(enemy_projectile_left)
                else:
                    self.enemy.left = True
                    start_pos_right = (self.enemy.rect.midbottom[0] + 85, self.enemy.rect.midbottom[1] - 20)
                    enemy_projectile_right = EnemyProjectile(start_pos_right)
                    self.enemy_projectiles.append(enemy_projectile_right)

        if keys[pygame.K_SPACE]:
            if self.player.shoot(pygame.time.get_ticks()):
                # Posición inicial proyectiles
                start_pos_left = (self.player.rect.centerx, self.player.rect.centery)
                start_pos_right = (self.player.rect.centerx, self.player.rect.centery)

                # Crear proyectiles
                projectile_left = Projectile(start_pos_left, self.player.radians)
                projectile_right = Projectile(start_pos_right, self.player.radians)

                # Añadir proyectiles a la lista después de crear ambos (para evitar desincronización)
                self.player_projectiles.extend([projectile_left, projectile_right])

    def update(self):
        # Actualizar la posición del fondo para que se desplace
        self.bg_y += self.bgSpeed
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
        # Dibujar el fondo en dos partes para el efecto de scrolling continuo
        self.screen.blit(self.background, (0, self.bg_y - HEIGHT))
        self.screen.blit(self.background, (0, self.bg_y))
        self.player.draw(self.screen)
        self.enemy.draw(self.screen)
        for projectile in self.player_projectiles:
            projectile.draw(self.screen)

        for projectile in self.enemy_projectiles:
            projectile.draw(self.screen)
