import pygame


class PlayerProjectile:
    def __init__(self, start_pos, offset_y=0, colour=(0, 255, 0)):
        self.x, self.y = start_pos
        self.colour = colour
        self.length = 2  # Longitud del proyectil
        self.width = 1  # Ancho del proyectil
        self.position_x1 = self.x - 7
        self.position_x2 = self.x + 5
        self.position_y = self.y + offset_y
        self.end_y = self.position_y - self.length
        self.hitbox = pygame.Rect(self.position_x1, self.end_y, 12, self.length)
        self.speed = 4

    def update(self):
        self.position_y -= self.speed
        self.end_y = self.position_y - self.length
        self.hitbox.top = self.end_y
        self.hitbox.bottom = self.position_y

    def draw(self, screen):
        pygame.draw.line(screen, self.colour, (self.position_x1, self.position_y), (self.position_x1, self.end_y),
                         self.width)
        pygame.draw.line(screen, self.colour, (self.position_x2, self.position_y), (self.position_x2, self.end_y),
                         self.width)


class EnemyProjectile:
    def __init__(self, start_pos, offset_x, offset_y, colour=(0, 255, 255)):
        self.x = start_pos[0] + offset_x
        self.y = start_pos[1] + offset_y
        self.colour = colour
        self.length = 2
        self.width = 1
        self.hitbox = pygame.Rect(self.x, self.y, self.length, self.width)
        self.speed = 6

    def update(self):
        self.y += self.speed
        self.hitbox.top = self.y
        self.hitbox.bottom = self.y + self.length

    def draw(self, screen):
        end_y = self.y + self.length
        pygame.draw.line(screen, self.colour, (self.x, self.y), (self.x, end_y),
                         self.width)
