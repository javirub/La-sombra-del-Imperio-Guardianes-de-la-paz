import math

import pygame


class DeathStarProjectile:
    def __init__(self, start_pos):
        self.x, self.y = start_pos
        self.offset_x = 100
        self.offset_y = -120
        self.colour = (0, 255, 0)
        self.width = 2
        self.speed = 8
        self.length = 1
        self.angle = 0.28  # Angulo desde la estrella de la muerte hacía la tierra en radianes
        self.end_x = 0
        self.end_y = 0
        self.hitbox = pygame.Rect(self.end_x, self.end_y, self.width, self.length)

    def draw(self, screen):
        cos_angle = math.cos(self.angle)
        sin_angle = math.sin(self.angle)

        start_x = self.x + self.offset_x
        start_y = self.y + self.offset_y

        self.end_x = start_x + self.length * cos_angle
        self.end_y = start_y - self.length * sin_angle  # Se resta ya que en pygame el eje y crece hacia abajo

        pygame.draw.line(screen, self.colour, (start_x, start_y), (self.end_x, self.end_y), self.width)

    def update(self):
        # Alarga el proyectil hasta llegar a la tierra
        self.length += self.speed
        # Hitbox del disparo
        self.hitbox.x = self.end_x
        self.hitbox.y = self.end_y
