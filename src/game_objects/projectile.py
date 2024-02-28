import pygame
import math


class Projectile:
    def __init__(self, start_pos, angle):
        self.x, self.y = start_pos
        self.speed = 10  # Ajusta según la velocidad deseada para el proyectil
        self.angle = angle  # Dirección del proyectil
        self.length = 30  # Longitud del proyectil

    def update(self):
        # Mueve el proyectil en la dirección del ángulo
        self.x -= self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)

    def draw(self, screen):
        # Calcula el ángulo corregido para la rotación
        angle_corrected = -self.angle
        cos_angle = math.cos(angle_corrected)
        sin_angle = math.sin(angle_corrected)
        offset_y1 = -10
        offset_y2 = 8

        # Calcula las nuevas posiciones de inicio y fin considerando la rotación
        start_x1 = self.x + offset_y1 * sin_angle
        start_y1 = self.y - offset_y1 * cos_angle
        end_x1 = start_x1 - self.length * cos_angle
        end_y1 = start_y1 - self.length * sin_angle

        start_x2 = self.x + offset_y2 * sin_angle
        start_y2 = self.y - offset_y2 * cos_angle
        end_x2 = start_x2 - self.length * cos_angle
        end_y2 = start_y2 - self.length * sin_angle


        # Dibuja el proyectil
        projectile1 = pygame.draw.line(screen, (0, 255, 0), (start_x1, start_y1), (end_x1, end_y1),
                                       2)  # Dibuja una línea verde
        projectile2 = pygame.draw.line(screen, (0, 255, 0), (start_x2, start_y2), (end_x2,end_y2),
                                       2)  # Dibuja una línea verde


class EnemyProjectile:
    def __init__(self, start_pos):
        self.x, self.y = start_pos
        self.speed = 10  # Ajusta según la velocidad deseada para el proyectil

    def update(self):
        self.y += self.speed  # Mover el proyectil hacia abajo

    def draw(self, screen):
        pygame.draw.line(screen, (255, 0, 0), (self.x, self.y), (self.x, self.y - 30), 2)  # Dibuja una línea roja
