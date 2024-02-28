import sys

import pygame

import src.settings
from src.game_objects.projectile import Projectile, EnemyProjectile
from src.settings import *
from src.game_objects.spaceship import TieFighter, XWing


class LocalMPScene:
    def __init__(self, screen):
        self.screen = screen
        self.done = False
        self.next_scene = "menu"
        self.background = pygame.image.load(BACKGROUND_PATH).convert()
        self.bg_y = 0  # Posición inicial del fondo
        self.bgSpeed = 2  # Velocidad de desplazamiento del fondo
        self.player1 = TieFighter((100, 100), 180)
        self.player1_projectiles = []
        pygame.mixer.set_num_channels(20)
        pygame.mixer.music.load('../assets/music/game_song.ogg')
        pygame.mixer.music.play(-1)
        self.player2_projectiles = []
        self.player2 = XWing((WIDTH - 100, HEIGHT - 200), 0)

    def run(self):
        while not self.done:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
            pygame.time.Clock().tick(src.settings.FPS)
        pygame.mixer.music.stop()

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
            if self.player1.shoot(pygame.time.get_ticks()):
                # Posición inicial proyectiles
                start_pos_left = (self.player1.rect.centerx, self.player1.rect.centery)
                start_pos_right = (self.player1.rect.centerx, self.player1.rect.centery)

                # Crear proyectiles
                projectile_left = Projectile(start_pos_left, self.player1.radians, (0, 255, 0))
                projectile_right = Projectile(start_pos_right, self.player1.radians, (0, 255, 0))

                # Añadir proyectiles a la lista después de crear ambos (para evitar desincronización)
                self.player1_projectiles.extend([projectile_left, projectile_right])

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
            if self.player2.shoot(pygame.time.get_ticks()):
                # Posición inicial proyectiles
                start_pos_left = (self.player2.rect.centerx, self.player2.rect.centery)
                start_pos_right = (self.player2.rect.centerx, self.player2.rect.centery)

                # Crear proyectiles
                projectile_left = Projectile(start_pos_left, self.player2.radians, (255, 0, 0))
                projectile_right = Projectile(start_pos_right, self.player2.radians, (255, 0, 0))

                # Añadir proyectiles a la lista después de crear ambos (para evitar desincronización)
                self.player2_projectiles.extend([projectile_left, projectile_right])



    def update(self):
        # Actualizar la posición del fondo para que se desplace
        '''Deprecated
        self.bg_y += self.bgSpeed
        if self.bg_y >= HEIGHT:
            self.bg_y = 0  # Reiniciar la posición del fondo para el efecto de bucle'''
        # Movimiento de los jugadores
        self.player1.move_forward()
        self.player2.move_forward()

        # Actualizar la posición de los proyectiles
        for projectile in self.player1_projectiles:
            projectile.update()
            if projectile.y < 0 or projectile.y > HEIGHT or projectile.x < 0 or projectile.x > WIDTH:
                self.player1_projectiles.remove(projectile)

        for projectile in self.player2_projectiles:
            projectile.update()
            if projectile.y < 0 or projectile.y > HEIGHT or projectile.x < 0 or projectile.x > WIDTH:
                self.player2_projectiles.remove(projectile)

    def draw(self):
        ''' Deprecated, antes iba a ser un juego de scroll vertical
        self.screen.blit(self.background, (0, self.bg_y - HEIGHT))
        self.screen.blit(self.background, (0, self.bg_y))'''
        self.screen.blit(self.background, (0, 0))
        self.player1.draw(self.screen)
        self.player2.draw(self.screen)
        for projectile in self.player1_projectiles:
            projectile.draw(self.screen)

        for projectile in self.player2_projectiles:
            projectile.draw(self.screen)
