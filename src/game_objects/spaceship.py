import pygame.draw

from game_objects.projectile import *
from settings import *
from utils.sprites import *


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
        self.animating = False
        self.explosion_sprite = load_sprite_sheet(EXPLOSION_SPRITE, 8, 6)
        self.current_sprite_index = None
        self.life = 100
        self.projectiles = []

    def start_hit_animation(self):
        self.animating = True
        self.current_sprite_index = 0
        pygame.mixer.Sound(EXPLOSION_SOUND).play()
        self.life -= 10

    def draw(self, screen):
        # Dibujar nave espacial
        screen.blit(self.rotated, self.rect)

        # Si la nave sale de la pantalla, aparece por el otro lado
        if self.rect.x > WIDTH:
            self.rect.x = -self.rect.width
        elif self.rect.x < -self.rect.width:
            self.rect.x = WIDTH

        if self.rect.y > HEIGHT:
            self.rect.y = -self.rect.height
        elif self.rect.y < -self.rect.height:
            self.rect.y = HEIGHT

        # Dibujar animación de explosión
        if self.animating:
            self.current_sprite_index += 1
            if self.current_sprite_index >= len(self.explosion_sprite):
                self.animating = False
            else:
                # Calculamos la posición de la explosión en base al centro de la nave y el tamaño de la explosión
                explosion_x = self.rect.centerx - self.explosion_sprite[int(self.current_sprite_index)].get_width() / 2
                explosion_y = self.rect.centery - self.explosion_sprite[int(self.current_sprite_index)].get_height() / 2
                # Dibujamos la explosión
                screen.blit(self.explosion_sprite[int(self.current_sprite_index)], (explosion_x, explosion_y))

        for projectile in self.projectiles:
            projectile.draw(screen)

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
            self.create_projectile()
            print(f'')
            pass
        return None

    def update_rotation_speed(self):
        """Actualiza la velocidad de rotación de la nave."""
        self.rotation_speed = 3 - (self.speed - self.min_speed) * (1.0 / (self.max_speed - self.min_speed))

    def create_projectile(self):
        """Debe ser sobreescrito por subclases."""
        self.projectiles.append(Projectile((self.rect.centerx, self.rect.centery), self.radians, 0, 0, (0, 0, 0)))

    def update(self):
        if self.life > 0:
            self.move_forward()
        for projectile in self.projectiles:
            projectile.update()
            if projectile.y < 0 or projectile.y > HEIGHT or projectile.x < 0 or projectile.x > WIDTH:
                self.projectiles.remove(projectile)


class TieFighter(Spaceship):
    def __init__(self, position, rotation):
        super().__init__(position, rotation, TIE_SPRITE, TIE_SOUND)

    def create_projectile(self):
        self.projectiles.append(Projectile((self.rect.centerx, self.rect.centery), self.radians, 0, 10, (0, 255, 0)))
        self.projectiles.append(Projectile((self.rect.centerx, self.rect.centery), self.radians, 0, -10, (0, 255, 0)))


class XWing(Spaceship):
    def __init__(self, position, rotation):
        super().__init__(position, rotation, XWING_SPRITE, XWING_SOUND)
        self.fire_toggle = False

    def create_projectile(self):
        self.fire_toggle = not self.fire_toggle
        offset_y = 50 if self.fire_toggle else -50
        self.projectiles.append(
            Projectile((self.rect.centerx, self.rect.centery), self.radians, 0, offset_y, (255, 0, 0)))
