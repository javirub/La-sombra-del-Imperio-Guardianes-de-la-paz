import pygame, math
from src.settings import WIDTH, HEIGHT


class TieFighter:
    def __init__(self, position):
        self.image = pygame.image.load("../assets/images/spaceships/tie.png").convert_alpha()
        self.rect = self.image.get_rect(center=position)
        self.speed = 8  # Velocidad de la nave
        self.angle = 0  # Ángulo inicial de la nave
        self.radians = math.radians(self.angle)
        self.rotated = pygame.transform.rotate(self.image, self.angle)
        self.cadence = 500  # Velocidad de disparo
        self.last_shot_time = 0  # Tiempo del último disparo
        self.rotation_speed = 2  # Velocidad de rotación

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

        self.rotated = pygame.transform.rotate(self.image, self.angle)
        self.rect = self.image.get_rect(center=self.rect.center)
        self.radians = math.radians(self.angle)

    def move_forward(self):
        """Mueve la nave hacia adelante."""
        self.rect.x -= self.speed * math.cos(self.radians)
        self.rect.y += self.speed * math.sin(self.radians)


    def can_shoot(self, current_time):
        return current_time - self.last_shot_time >= self.cadence

    def shoot(self, current_time):
        if self.can_shoot(current_time):
            pygame.mixer.Sound("../assets/sounds/tieblast.ogg").play()
            self.last_shot_time = current_time
            return True
        return False


class XWing:
    def __init__(self, position):
        self.image = pygame.image.load("../assets/images/spaceships/xwing.png").convert_alpha()
        self.rect = self.image.get_rect(center=position)
        self.speed = 8  # Velocidad de la nave
        self.cadence = 400  # Velocidad de disparo
        self.last_shot_time = 0  # Tiempo del último disparo
        self.left = True  # Dispara el cañon de la izquierda

    def draw(self, screen):
        screen.blit(self.image, self.rect)

    def move(self, dx, dy):
        # Actualizar la posición de la nave
        self.rect.x += dx
        self.rect.y += dy

        # Limitar la posición de la nave a la pantalla
        if self.rect.left < 0:
            self.rect.left = 0
        elif self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        elif self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def can_shoot(self, current_time):
        return current_time - self.last_shot_time >= self.cadence

    def shoot(self, current_time):
        if self.can_shoot(current_time):
            pygame.mixer.Sound("../assets/sounds/tieblast.ogg").play()
            self.last_shot_time = current_time
            return True
        return False
