import sys
import time

import pygame

from game_objects.level_1.spaceships import FinalDeathstar
from scenes.scene import Scene
from settings import *
from game_objects.dialogueBox import DialogueBox


class FinalScene(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.story_stage = None
        self.next_scene = "menu"
        self.background = pygame.image.load(BACKGROUND_PATH).convert()
        pygame.mixer.music.load(EPIC_SONG_PATH)
        pygame.mixer.music.play(-1)
        self.last_second = time.time()
        self.earth = pygame.image.load(EARTH_PLANET_SPRITE).convert_alpha()
        self.deathstar = FinalDeathstar((WIDTH / 2 - 600, HEIGHT - 350))
        self.font = pygame.font.Font(None, 40)

        # Dialogo
        self.dialogue_box = DialogueBox(screen, FONT_PATH, 24)
        self.show_dialogue = False
        self.font = pygame.font.Font(None, 40)
        self.story_stage = 0

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        if not self.deathstar.hasShoot:
            self.screen.blit(self.earth, (WIDTH / 2 + 400, 0))
        self.deathstar.draw(self.screen)
        if self.deathstar.energy == 0:
            text = self.font.render("Presiona espacio para cargar la Estrella de la Muerte",
                                    True, (255, 255, 255))
            text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT - 50))
            self.screen.blit(text, text_rect)
        if self.show_dialogue:
            self.dialogue_box.draw(self.screen)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not self.deathstar.hasShoot:
                        self.deathstar.energy += 1
                    else:
                        self.dialogue_box.next_line()

    def update(self):
        self.deathstar.update()
        if self.deathstar.hasShoot:
            self.show_dialogue = True

    def show_dialogues(self):
        if self.show_dialogue and self.story_stage == 0:
            self.story_stage = 1
            self.dialogue_box.add_dialogue([
                "Ya era hora, al fin he destruido la tierra.",
                "Ahora en el universo reinará el orden,",
                "sin basura espacial ni humanos que la generen."
            ])
        elif self.story_stage == 1 and self.dialogue_box.finished:
            self.next_scene = "Credits"
            self.done = True
