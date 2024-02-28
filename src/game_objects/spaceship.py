import pygame, math

import src.settings
from src.settings import *


class Spaceship:  # Clase padre de las naves espaciales
    def __init__(self, position, rotation, image_path, sound_path):
        self.image = pygame.image.load(image_path).convert_alpha()
        self.rect = self.image.get_rect(center=position)
        self.speed = 0
        self.max_speed = 15
        self.min_speed = 0
        self.angle = rotation
        self.radians = math.radians(self.angle)
        self.rotated = pygame.transform.rotate(self.image, self.angle)
        self.cadence = 500
        self.last_shot_time = 0
        self.rotation_speed = 4
        self.speed_change_per_update = (self.max_speed - self.min_speed) / (60 * 3)
        self.sound_path = sound_path

    def draw(self, screen):
        screen.blit(self.rotated, self.rect)

        if self.rect.x > WIDTH:
            self.rect.x = -self.rect.width
        elif self.rect.x < -self.rect.width:
            self.rect.x = WIDTH

        if self.rect.y > HEIGHT:
            self.rect.y = -self.rect.height
        elif self.rect.y < -self.rect.height:
            self.rect.y = HEIGHT

    def rotate(self, angle):
        """Rota la nave en el ángulo específicado."""
        rotation_amount = self.rotation_speed * angle
        self.angle += rotation_amount
        self.radians = math.radians(self.angle)
        self.rotated = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)

    def move_forward(self):
        """Mueve la nave hacia adelante."""
        self.rect.x -= self.speed * math.cos(self.radians)
        self.rect.y += self.speed * math.sin(self.radians)

    def increase_speed(self):
        """Aumenta la velocidad de la nave."""
        self.speed = min(self.speed + self.speed_change_per_update, self.max_speed)
        self.update_rotation_speed()

    def decrease_speed(self):
        """Disminuye la velocidad de la nave."""
        self.speed = max(self.speed - self.speed_change_per_update, self.min_speed)
        self.update_rotation_speed()

    def can_shoot(self, current_time):
        return current_time - self.last_shot_time >= self.cadence

    def shoot(self, current_time):
        if self.can_shoot(current_time):
            pygame.mixer.Sound(self.sound_path).play()
            self.last_shot_time = current_time
            return True
        return False

    def update_rotation_speed(self):
        """Actualiza la velocidad de rotación de la nave."""
        self.rotation_speed = 3 - (self.speed - self.min_speed) * (1.0 / (self.max_speed - self.min_speed))


class TieFighter(Spaceship):
    def __init__(self, position, rotation):
        super().__init__(position, rotation, src.settings.TIE_SPRITE, src.settings.TIE_SOUND)


class XWing(Spaceship):
    def __init__(self, position, rotation):
        super().__init__(position, rotation, src.settings.XWING_SPRITE, src.settings.XWING_SOUND)