import random
import sys
from ..scene import Scene

from game_objects.level_2.spaceships import *
from game_objects.dialogueBox import DialogueBox
from utils.collision import *


class Arcadedon(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.next_scene = "Arcadedon"
        pygame.mixer.init()
        pygame.mixer.music.load(INTRO_SONG_PATH)
        self.background = pygame.image.load(BACKGROUND_PATH).convert_alpha()
        self.earth = pygame.image.load(EARTH_PLANET_SPRITE).convert_alpha()

        self.deathstar = Deathstar((WIDTH / 2, HEIGHT + 100), 5)
        self.player = Tie((WIDTH / 2, HEIGHT - 200))
        self.time_to_shoot = random.randint(500, 4000)
        self.last_shoot_time = pygame.time.get_ticks()
        self.enemy_spawn = 50
        self.last_time_spawn = pygame.time.get_ticks()

        self.TESLA_SPRITE = pygame.image.load(ARCADE_TESLA_SPRITE).convert_alpha()  # This way only one time is loaded
        # Sorry for preloading the enemies, but it's necessary to avoid lag, not asynchrony in pygame
        self.enemies = [TeslaRoadster((WIDTH - 220, 100), self.TESLA_SPRITE) for _ in range(50)]

        self.dialogue_box = DialogueBox(screen, FONT_PATH, 24)
        self.dialogue_box.current_speaker = 'darth_vader'
        self.show_dialogue = False
        self.font = pygame.font.Font(None, 40)
        self.story_stage = 0

    def update(self):
        # Game actions
        self.player.update()
        for enemy in self.enemies:
            if enemy.activated:
                enemy.update()
        self.check_collisions()
        self.enemy_shoot()
        self.enemy_movement()

        # Spawn enemies every 500ms
        if pygame.time.get_ticks() - self.last_time_spawn > 500 and self.enemy_spawn >= 0:
            self.enemy_spawn -= 1
            self.enemies[self.enemy_spawn].activated = True
            self.last_time_spawn = pygame.time.get_ticks()

        # Story dialogue
        if self.show_dialogue and self.story_stage == 0:
            self.story_stage = 1
            self.dialogue_box.add_dialogue([
                "Vaya, eso ha sido fácil, 50 a 0."
            ])
        elif self.story_stage == 1 and self.dialogue_box.finished:
            self.story_stage = 2
            self.dialogue_box.finished = False
            self.dialogue_box.current_speaker = 'laughing_musk'
            self.dialogue_box.add_dialogue([
                "JAJAJA, ¿Pero que ha sido ese ruido?.",
                "Era como si una persona estuviese diciendo PIU PIU PIU."
            ])
        elif self.story_stage == 2 and self.dialogue_box.finished:
            self.story_stage = 3
            self.dialogue_box.finished = False
            self.dialogue_box.current_speaker = 'darth_vader'
            self.dialogue_box.add_dialogue([
                "Quizás perdisteis mucho tiempo en desarrollar un ruido de disparo.",
                "Mientras nosotros estuvimos desarrollando un improvisado caza TIE."
            ])
        elif self.story_stage == 3 and self.dialogue_box.finished:
            self.story_stage = 4
            self.dialogue_box.finished = False
            self.dialogue_box.current_speaker = 'elon_musk'
            self.dialogue_box.add_dialogue([
                "Quizás tengas razón, pero no nos rendiremos tan facilmente.",
                "Desarrollaremos un nuevo caza especial para esta ocasión,",
                "Capaz de hacerte frente, esta vez no podrás contra nosotros."
            ])
        elif self.story_stage == 4 and self.dialogue_box.finished:
            self.story_stage = 5
            self.dialogue_box.finished = False
            self.dialogue_box.current_speaker = 'laughing_musk'
            self.dialogue_box.add_dialogue([
                "Pero no hará PIU PIU."
            ])
        elif self.story_stage == 5 and self.dialogue_box.finished:
            self.dialogue_box.finished = False
            self.story_stage = 6
            self.dialogue_box.current_speaker = 'darth_vader'
            self.dialogue_box.add_dialogue([
                "¿Osas reirte del general Vader?",
                "Bueno, no importa, pronto la Estrella de la Muerte volverá a tener energia,",
                "Y entonces, vuestras burlas se convertirán en polvo junto con vuestros cuerpos."
            ])
        elif self.dialogue_box.finished and self.story_stage == 6:
            self.show_dialogue = False
            self.next_scene = "intro3"
            self.done = True

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.deathstar.draw(self.screen)
        self.player.draw(self.screen)

        for enemy in self.enemies:
            if enemy.activated:
                enemy.draw(self.screen)

        self.screen.blit(self.earth, (WIDTH - 200, -100))

        if self.show_dialogue:
            self.dialogue_box.draw(self.screen)

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            # Player movement and shooting, dialogue handling
            if event.type == pygame.KEYDOWN:
                # Uses booleans to avoid the delay in the movement caused by the key repetition
                if event.key == pygame.K_LEFT or event.key == pygame.K_a:
                    self.player.moving_left = True
                elif event.key == pygame.K_RIGHT or event.key == pygame.K_d:
                    self.player.moving_right = True
                elif event.key == pygame.K_SPACE or event.key == pygame.K_LCTRL:
                    if not self.show_dialogue:
                        self.player.shooting = True
                    else:
                        self.dialogue_box.next_line()

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
            if self.enemy_spawn < 0:
                self.next_scene = "intro3"
                self.show_dialogue = True
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
