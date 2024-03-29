from ..spaceship import Spaceship
from settings import *
from game_objects.level_1.projectiles import DeathStarProjectile
import pygame
from moviepy.editor import VideoFileClip
import time


class DeathStar(Spaceship):
    def __init__(self, position: object, energy: object) -> object:
        super().__init__(position, 0, DEATHSTAR_SPRITE, DEATHSTAR_SOUND)
        self.energy = energy
        self.projectiles = []
        self.hasShoot = False
        self.hasHit = False
        self.last_second = time.time()

    def draw(self, screen):
        screen.blit(self.rotated, self.rect)

        if 0 < self.energy < 30 and not self.hasShoot:
            pygame.draw.circle(screen, (0, 255, 0), (self.rect.centerx + 100, self.rect.centery - 120),
                               self.energy)
        elif self.energy >= 30 and not self.hasShoot:
            self.hasShoot = True
            self.projectiles.append(DeathStarProjectile((self.rect.centerx, self.rect.centery)))
            self.play_video()
            pygame.mixer.Sound(self.sound_path).play()
        elif self.hasShoot and not self.hasHit:
            pygame.draw.circle(screen, (0, 255, 0), (self.rect.centerx + 100, self.rect.centery - 120), 30)
            for projectile in self.projectiles:
                projectile.draw(screen)

    def update(self):
        for projectile in self.projectiles:
            projectile.update()
            if projectile.y < 0 or projectile.y > HEIGHT or projectile.x < 0 or projectile.x > WIDTH:
                self.projectiles.remove(projectile)
        current_time = time.time()

        # Si ha pasado un segundo reduce la energía
        if current_time - self.last_second >= 1:
            if self.energy > 0:
                self.energy -= 3
            self.last_second = current_time

    def play_video(self):
        clip = VideoFileClip(DEATHSTAR_SHOOT_VIDEO)
        clip.preview()
        clip.close()


class TeslaRoadster(Spaceship):
    def __init__(self, position):
        super().__init__(position, 2, TESLA_ROADSTER_SPRITE, None)
        self.isDestroyed = False

    def draw(self, screen):
        if not self.isDestroyed:
            self.rotated = pygame.transform.rotate(self.image, self.angle)
            screen.blit(self.rotated, self.rect)
        elif self.animating:
            self.current_sprite_index += 1
            if self.current_sprite_index >= len(self.explosion_sprite):
                self.animating = False
            else:
                # Calculamos la posición de la explosión en base al centro de la nave y el tamaño de la explosión
                explosion_x = self.rect.centerx - self.explosion_sprite[int(self.current_sprite_index)].get_width() / 2
                explosion_y = self.rect.centery - self.explosion_sprite[int(self.current_sprite_index)].get_height() / 2
                # Dibujamos la explosión
                screen.blit(self.explosion_sprite[int(self.current_sprite_index)], (explosion_x, explosion_y))
