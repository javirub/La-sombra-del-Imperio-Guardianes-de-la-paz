from game_objects.level_4.projectiles import *
from settings import *
from utils.sprites import load_sprite_sheet


class Deathstar:
    def __init__(self, position, life):
        self.image = pygame.image.load(DEATHSTAR_SPRITE).convert_alpha()
        self.rect = self.image.get_rect(center=position)
        self.life = life

    def draw(self, screen):
        screen.blit(self.image, self.rect)


class ArcadeSpaceship:
    def __init__(self, position, image_path, sound_path):
        self.image = image_path
        self.rect = self.image.get_rect(center=position)
        self.sound_path = sound_path
        self.cadence = 1000
        self.last_shot_time = 0
        self.animating = False
        self.explosion_sprite = load_sprite_sheet(EXPLOSION_SPRITE, 8, 6)
        self.current_sprite_index = 0
        self.life = 1
        self.projectiles = []
        self.moving_left = False
        self.moving_right = False
        self.shooting = False
        self.speed = 4
        self.activated = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)

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

    def move_right(self):
        if self.moving_right and self.rect.x + self.rect.width < WIDTH:
            self.rect.x += self.speed

    def move_left(self):
        if self.moving_left and self.rect.x > 0:
            self.rect.x -= self.speed

    def update(self):
        self.move_right()
        self.move_left()
        self.shoot(pygame.time.get_ticks())
        for projectile in self.projectiles:
            projectile.update()
            if projectile.y < 0 or projectile.y > HEIGHT:
                self.projectiles.remove(projectile)

    def can_shoot(self, current_time):
        return current_time - self.last_shot_time >= self.cadence

    def shoot(self, current_time):
        if self.shooting and self.can_shoot(current_time):
            pygame.mixer.Sound(self.sound_path).play()
            self.last_shot_time = current_time
            self.create_projectile()

    def create_projectile(self):
        """Debe ser sobreescrito por subclases."""
        assert NotImplementedError

    def start_hit_animation(self):
        self.animating = True
        self.current_sprite_index = 0
        pygame.mixer.Sound(EXPLOSION_SOUND).play()
        self.life -= 1


class Tie(ArcadeSpaceship):
    def __init__(self, position, image_path):
        super().__init__(position, image_path, TIE_FUNNY_SOUND)
        self.life = 3

    def create_projectile(self):
        self.projectiles.append(PlayerProjectile((self.rect.centerx, self.rect.y), 25))


class TeslaRoadster(ArcadeSpaceship):
    def __init__(self, position, image_path):
        super().__init__(position, image_path, XWING_SOUND)
        self.life = 3

    def create_projectile(self):
        self.projectiles.append(EnemyProjectile((self.rect.centerx, self.rect.y), 0, 0))
        self.shooting = False

    def create_powerup(self):
        pass


# TODO: One more class for Stronk Spaceship, with higher life and different shooting cadence and higher drop rate
