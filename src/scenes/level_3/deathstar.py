import sys
import time

import pygame

from game_objects.dialogueBox import DialogueBox
from game_objects.level_1.spaceships import DeathStar, DeathstarSpaceship
from scenes.scene import Scene
from settings import *
from utils.collision import *


class DeathstarScene2(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.story_stage = None
        self.next_scene = "menu"
        self.background = pygame.image.load(BACKGROUND_PATH).convert()
        pygame.mixer.music.load(EPIC_SONG_PATH)
        pygame.mixer.music.play(-1)
        self.last_second = time.time()
        self.deathstar = DeathStar((WIDTH / 2 - 600, HEIGHT - 350), 0)
        self.earth = pygame.image.load(EARTH_PLANET_SPRITE).convert_alpha()
        self.tesla = DeathstarSpaceship((WIDTH / 2 + 600, HEIGHT - 1200), SPY_SATELLITE_SPRITE)
        self.dialogue_box = DialogueBox(screen, FONT_PATH, 24)
        self.show_dialogue = False
        self.font = pygame.font.Font(None, 40)

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.earth, (WIDTH / 2 + 400, 0))
        self.deathstar.draw(self.screen)
        self.tesla.draw(self.screen)
        if self.show_dialogue:
            self.dialogue_box.draw(self.screen)
        if self.deathstar.energy == 0 and not self.show_dialogue:
            text = self.font.render("Presiona espacio para cargar la Estrella de la Muerte",
                                    True, (255, 255, 255))
            text_rect = text.get_rect(center=(WIDTH / 2, HEIGHT - 50))
            self.screen.blit(text, text_rect)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if self.tesla.isDestroyed and self.show_dialogue:
                        self.dialogue_box.next_line()
                    else:
                        self.deathstar.energy += 1

    def update(self):
        self.deathstar.update()
        self.tesla.update()
        if self.deathstar.hasShoot:
            self.tesla.speed = 8
            self.tesla.radians += 0.02
        if not self.show_dialogue:
            for projectile in self.deathstar.projectiles:
                if check_collision(projectile.hitbox, self.tesla):
                    self.deathstar.hasHit = True
                    self.deathstar.projectiles.remove(projectile)
                    self.tesla.start_hit_animation()
                    self.tesla.isDestroyed = True
                    self.show_dialogue = True
                    self.dialogue_box.current_speaker = 'Kim Jong Ill'
                    self.story_stage = 1
                    self.dialogue_box.add_dialogue([
                        "¿Quien se atreve a atacar mi satelite espia?"
                    ])
        if self.dialogue_box.finished and self.story_stage == 1:
            self.story_stage = 2
            self.dialogue_box.finished = False
            self.dialogue_box.current_speaker = 'darth_vader'
            self.dialogue_box.add_dialogue([
                "¿Por que razón estos humanos tienen llena de basura el espacio?",
                "Tendremos que volver a esperar a que se enfrie la estrella de la muerte",
                "para poder volver a disparar."
            ])

        elif self.dialogue_box.finished and self.story_stage == 2:
            self.story_stage = 3
            self.dialogue_box.finished = False
            self.dialogue_box.current_speaker = 'Kim Jong Ill'
            self.dialogue_box.add_dialogue([
                "¿Pretendes derrotar la tierra?",
                "No te lo permitiré, solo yo puedo usar armas de destrucción masiva",
            ])

        elif self.dialogue_box.finished and self.story_stage == 3:
            # Esto es para que no se muestre el mensaje de dialogo vacio mientras se carga el siguiente nivel
            self.dialogue_box.finished = False
            self.story_stage = 4
            self.dialogue_box.current_speaker = 'darth_vader'
            self.dialogue_box.add_dialogue([
                "¿Qué? ¿Quién eres tú?",
                "No importa, también acabaré contigo."
            ])

        elif self.dialogue_box.finished and self.story_stage == 4:
            # Esto es para que no se muestre el mensaje de dialogo vacio mientras se carga el siguiente nivel
            self.show_dialogue = False
            self.next_scene = "intro2"
            self.done = True
