import pygame

from settings import *


class Powerup:
    def __init__(self, position, sprite):
        self.x, self.y = position
        self.image = pygame.image.load(sprite).convert_alpha()
        self.rect = self.image.get_rect(center=position)
        self.type = None

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def update(self):
        #self.y += 5
        self.rect.bottom = self.rect.bottom + 5


class CadencePowerup(Powerup):
    def __init__(self, position):
        super().__init__(position, CADENCE_POWERUP_SPRITE)
        self.type = 1


class SpeedPowerup(Powerup):
    def __init__(self, position):
        super().__init__(position, SPEED_POWERUP_SPRITE)
        self.type = 2


class HealthPowerup(Powerup):
    def __init__(self, position):
        super().__init__(position, HEALTH_POWERUP_SPRITE)
        self.type = 3
