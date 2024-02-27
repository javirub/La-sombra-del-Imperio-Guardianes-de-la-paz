import pygame
import math

class Projectile:
    def __init__(self, start_pos, angle):
        self.x, self.y = start_pos
        self.speed = 10  # Ajusta según la velocidad deseada para el proyectil
        self.angle = angle # Dirección del proyectil
        self.length = 30  # Longitud del proyectil

    def update(self):
        # Mueve el proyectil en la dirección del ángulo
        self.x -= self.speed * math.cos(self.angle)
        self.y += self.speed * math.sin(self.angle)

    def draw(self, screen):
        #TODO: No se dibuja bien aún
        x_inicial = self.x - 25 * math.cos(self.angle)
        y_inicial = self.y - 30 * math.sin(self.angle)


        # Calcula el punto final del proyectil
        end_x = x_inicial + self.length * math.cos(self.angle)
        end_y = y_inicial - self.length * math.sin(self.angle)

        pygame.draw.line(screen, (0, 255, 0), (x_inicial, y_inicial), (end_x, end_y), 2)  # Dibuja una línea verde


class EnemyProjectile:
    def __init__(self, start_pos):
        self.x, self.y = start_pos
        self.speed = 10  # Ajusta según la velocidad deseada para el proyectil

    def update(self):
        self.y += self.speed  # Mover el proyectil hacia abajo

    def draw(self, screen):
        pygame.draw.line(screen, (255, 0, 0), (self.x, self.y), (self.x, self.y - 30), 2)  # Dibuja una línea roja
