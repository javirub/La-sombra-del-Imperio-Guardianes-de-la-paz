import random
import threading

from ..scene import Scene
import sys
from src.game_objects.level_2.spaceships import *
from src.utils.collision import *


class Arcadedon(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.next_scene = "Arcadedon"
        pygame.mixer.init()
        pygame.mixer.music.load(INTRO_SONG_PATH)
        self.background = pygame.image.load(BACKGROUND_PATH).convert_alpha()
        self.deathstar = Deathstar((WIDTH / 2, HEIGHT + 100), 5)
        self.player = Tie((WIDTH / 2, HEIGHT - 200))
        self.time_to_shoot = random.randint(500, 4000)
        self.last_shoot_time = pygame.time.get_ticks()
        self.enemy_spawn = 50
        self.last_time_spawn = pygame.time.get_ticks()
        self.TESLA_SPRITE = pygame.image.load(ARCADE_TESLA_SPRITE).convert_alpha()  # This way only one time is loaded
        self.enemies = [TeslaRoadster((WIDTH - 220, 100), self.TESLA_SPRITE) for _ in range(50)]
        self.earth = pygame.image.load(EARTH_PLANET_SPRITE).convert_alpha()

    def update(self):
        self.player.update()
        for enemy in self.enemies:
            if enemy.activated:
                enemy.update()
        self.check_collisions()
        self.enemy_shoot()
        self.enemy_movement()
        if pygame.time.get_ticks() - self.last_time_spawn > 1000 and self.enemy_spawn >= 0:
            self.enemy_spawn -= 1
            self.enemies[self.enemy_spawn].activated = True
            self.last_time_spawn = pygame.time.get_ticks()

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.deathstar.draw(self.screen)
        self.player.draw(self.screen)
        for enemy in self.enemies:
            if enemy.activated:
                enemy.draw(self.screen)
        self.screen.blit(self.earth, (WIDTH - 200, -100))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            # Movimiento nave espacial teclado
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.player.moving_left = True
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.player.moving_right = True
                elif event.key == pygame.K_SPACE or event.key == pygame.K_LCTRL:
                    self.player.shooting = True
                elif event.key == pygame.K_z:
                    self.enemies[0].shooting = True
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.player.moving_left = False
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.player.moving_right = False
                elif event.key == pygame.K_SPACE or event.key == pygame.K_LCTRL:
                    self.player.shooting = False

    def check_collisions(self):
        for projectile in self.player.projectiles:
            for enemy in self.enemies:
                if enemy.activated and check_collision(projectile.hitbox, enemy.rect):
                    enemy.life -= 1
                    self.player.projectiles.remove(projectile)
                    if enemy.life <= 0:
                        enemy.activated = False
        for enemy in self.enemies:
            if enemy.activated and check_collision(self.deathstar.rect, enemy.rect):
                self.deathstar.life -= 1
                enemy.activated = False

    def enemy_shoot(self):

        active_enemies = [enemy for enemy in self.enemies if enemy.activated]
        if not active_enemies:
            return
        random_enemy = random.choice(active_enemies)
        current_time = pygame.time.get_ticks()

        if current_time - self.last_shoot_time > self.time_to_shoot:
            self.last_shoot_time = current_time
            random_enemy.shooting = True
            self.time_to_shoot = random.randint(500, 4000)

    def enemy_movement(self):
        for enemy in self.enemies:
            if enemy.activated:
                if enemy.rect.x + enemy.rect.width > (WIDTH - 180) or enemy.rect.x < 0:
                    enemy.speed = -enemy.speed * 1.25
                    enemy.rect.y += 70
                enemy.rect.x -= enemy.speed

    def load_additional_enemies(self, lock, number_of_enemies=45):
        for _ in range(number_of_enemies):
            new_enemy = TeslaRoadster((WIDTH - 220, 100), self.TESLA_SPRITE)
            with lock:
                self.enemies.append(new_enemy)
