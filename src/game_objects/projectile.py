import pygame
import math


class Projectile:
    def __init__(self, start_pos, angle, offset_x=0, offset_y=0, colour=(0, 0, 0)):
        self.x, self.y = start_pos
        self.speed = 25  # Ajusta según la velocidad deseada para el proyectil
        self.angle = angle  # Dirección del proyectil
        self.length = 30  # Longitud del proyectil
        self.width = 2  # Ancho del proyectil
        self.colour = colour
        self.rect = pygame.Rect(start_pos[0], start_pos[1], self.width, self.length)
        self.offset_x, self.offset_y = offset_x, offset_y
        self.hitbox = pygame.Rect(self.x, self.y, self.width, self.length)

    def update(self):
        # Mueve el proyectil en la dirección del ángulo
        self.x -= self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)
        # Hitboxes de cada bala.
        self.hitbox.x = self.x + self.offset_x
        self.hitbox.y = self.y + self.offset_y

    def draw(self, screen):
        # Calcula el ángulo corregido para la rotación
        angle_corrected = -self.angle
        cos_angle = math.cos(angle_corrected)
        sin_angle = math.sin(angle_corrected)

        # Calcula las nuevas posiciones de inicio y fin considerando la rotación
        start_x = self.x + self.offset_y * sin_angle + self.offset_x * cos_angle
        start_y = self.y - self.offset_y * cos_angle + self.offset_x * sin_angle
        end_x = start_x - self.length * cos_angle
        end_y = start_y - self.length * sin_angle

        # Dibuja el proyectil
        pygame.draw.line(screen, self.colour, (start_x, start_y), (end_x, end_y),
                         self.width)  # Dibuja una línea verde



