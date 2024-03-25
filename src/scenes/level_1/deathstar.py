# Nivel: Estrella de la muerte
from src.scenes.scene import Scene
from src.settings import *
import pygame
import sys
import time
from src.game_objects.spaceship import DeathStar

class DeathstarScene(Scene):
    '''En este nivel tendremos que cargar energia a la estrella de la muerte para destruír la Tierra.'''

    def __init__(self, screen):
        super().__init__(screen)
        self.next_scene = "menu"
        self.background = pygame.image.load(BACKGROUND_PATH).convert()
        pygame.mixer.music.load(EPIC_SONG_PATH)
        pygame.mixer.music.play(-1)
        self.earth_planet = pygame.image.load(EARTH_PLANET_SPRITE).convert_alpha()
        self.energy = 0
        self.last_second = time.time()
        self.deathstar = DeathStar((WIDTH / 2 - 600, HEIGHT - 350), self.energy)

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.deathstar.draw(self.screen)
        self.screen.blit(self.earth_planet, (WIDTH / 2 + 600, 0))

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    self.deathstar.energy += 1

    def update(self):
        current_time = time.time()
        if current_time - self.last_second >= 1:
            if self.deathstar.energy > 0:
                self.deathstar.energy -= 3
            self.last_second = current_time
