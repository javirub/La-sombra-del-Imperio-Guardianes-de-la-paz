import sys

import pygame.mixer

from game_objects.spaceship import *
from scenes.scene import Scene
from settings import *
from utils.collision import *
from game_objects.AI import enemy_ai
from game_objects.dialogueBox import DialogueBox


class FinalBattle(Scene):
    def __init__(self, screen):
        super().__init__(screen)
        self.next_scene = "menu"
        self.background = pygame.image.load(BACKGROUND_PATH).convert()
        self.bg_y = 0  # Posición inicial del fondo
        self.bgSpeed = 2  # Velocidad de desplazamiento del fondo
        self.player1 = TieFighter((100, 100), 180)
        pygame.mixer.set_num_channels(20)
        pygame.mixer.music.load(GAME_SONG_PATH)
        pygame.mixer.music.play(-1)
        # Enemigos
        self.korean_tank = KoreaTank((WIDTH - 100, 10), 0)
        self.korean_tank_count = 3
        self.tesla = TeslaRoadster((WIDTH - 100, HEIGHT - 10), 0)
        self.tesla_count = 3
        self.boss = MilleniumFalcon((WIDTH - 100, HEIGHT - 200), 0)
        self.enemy_ai = enemy_ai.EnemyAI()
        # Dialogos
        self.dialogue_box = DialogueBox(screen, FONT_PATH, 24)
        self.dialogue_box.current_speaker = 'darth_vader'
        self.show_dialogue = False
        self.font = pygame.font.Font(None, 40)
        self.story_stage = 0

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and self.show_dialogue:
                self.dialogue_box.next_line()
        # Movimiento nave espacial teclado
        keys = pygame.key.get_pressed()
        # Controles jugador 1
        if not self.show_dialogue:
            if keys[pygame.K_a]:
                self.player1.rotate(1)
            if keys[pygame.K_d]:
                self.player1.rotate(-1)

            if keys[pygame.K_w]:
                self.player1.increase_speed()
            if keys[pygame.K_s]:
                self.player1.decrease_speed()

            if keys[pygame.K_SPACE]:
                self.player1.shoot(pygame.time.get_ticks())

    def update(self):
        """A cada frame, realiza las comprobaciones y movimientos correspondientes."""
        '''Deprecated
        self.bg_y += self.bgSpeed
        if self.bg_y >= HEIGHT:
            self.bg_y = 0  # Reiniciar la posición del fondo para el efecto de bucle'''

        # Comprobación vida de las naves
        if self.player1.life <= 0:
            self.next_scene = "Gameover3"
            self.done = True
        if self.korean_tank.life <= 0:
            self.korean_tank_count -= 1
            self.korean_tank.life = 30
            self.korean_tank.rect.x = WIDTH - 100
            self.korean_tank.rect.y = 10
        if self.tesla.life <= 0:
            self.tesla_count -= 1
            self.tesla.life = 20
            self.tesla.rect.x = WIDTH - 100
            self.tesla.rect.y = HEIGHT - 10
        if self.boss.life <= 0:
            self.next_scene = "FinalScene"
            self.done = True

        if self.story_stage == 0 and self.korean_tank_count < 1 and self.tesla_count < 1:
            self.show_dialogue = True

        if self.story_stage == 5:
            self.boss.update()

        # IA enemiga
        if self.korean_tank_count > 0:
            self.enemy_ai.update(self.korean_tank, self.player1, 4)
            self.korean_tank.update()
        if self.tesla_count > 0:
            self.enemy_ai.update(self.tesla, self.player1, 6)
            self.tesla.update()
        if self.story_stage == 5:
            self.enemy_ai.update(self.boss, self.player1, 6)
            self.boss.update()

        # Movimiento de los jugadores
        if not self.show_dialogue:
            self.player1.update()

        # Comprobación de colisiones
        self.check_hit()
        self.show_dialogues()

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.player1.draw(self.screen)
        if self.korean_tank_count > 0:
            self.korean_tank.draw(self.screen)
        if self.tesla_count > 0:
            self.tesla.draw(self.screen)
        elif self.story_stage == 5:
            self.boss.draw(self.screen)

        if self.show_dialogue:
            self.dialogue_box.draw(self.screen)

    def check_hit(self):
        # Check
        for projectile in self.player1.projectiles:
            if self.story_stage == 5 and check_collision(projectile.hitbox, self.boss.rect):
                self.boss.start_hit_animation()
                self.player1.projectiles.remove(projectile)
                break
            if check_collision(projectile.hitbox, self.korean_tank.rect) and self.korean_tank_count > 0:
                self.korean_tank.start_hit_animation()
                self.player1.projectiles.remove(projectile)
                break
            if check_collision(projectile.hitbox, self.tesla.rect) and self.tesla_count > 0:
                self.tesla.start_hit_animation()
                self.player1.projectiles.remove(projectile)
                break
        for projectile in self.boss.projectiles:
            if check_collision(projectile.hitbox, self.player1.rect):
                self.player1.start_hit_animation()
                self.boss.projectiles.remove(projectile)

        for projectile in self.korean_tank.projectiles:
            if check_collision(projectile.hitbox, self.player1.rect):
                self.player1.start_hit_animation()
                self.korean_tank.projectiles.remove(projectile)

        for projectile in self.tesla.projectiles:
            if check_collision(projectile.hitbox, self.player1.rect):
                self.player1.start_hit_animation()
                self.tesla.projectiles.remove(projectile)

    def show_dialogues(self):
        if self.show_dialogue and self.story_stage == 0:
            self.story_stage = 1
            self.dialogue_box.add_dialogue([
                "Se acabo, llego vuestro fin insolentes humanos."
            ])
        elif self.story_stage == 1 and self.dialogue_box.finished:
            self.story_stage = 2
            self.dialogue_box.finished = False
            self.dialogue_box.current_speaker = 'Harrison Ford'
            self.dialogue_box.add_dialogue([
                "No tan rapido Darth Vader,",
                "todavía tienes que derrotarnos a nosotros."
            ])
        elif self.story_stage == 2 and self.dialogue_box.finished:
            self.story_stage = 3
            pygame.mixer.Sound(WOOKIE_SOUND).play()
            self.dialogue_box.finished = False
            self.dialogue_box.current_speaker = 'Chewbacca'
            self.dialogue_box.add_dialogue([
                "*wookie*"
            ])
        elif self.story_stage == 3 and self.dialogue_box.finished:
            self.story_stage = 4
            self.dialogue_box.finished = False
            self.dialogue_box.current_speaker = 'darth_vader'
            self.dialogue_box.add_dialogue([
                "No he entendido lo que ha dicho el bicho peludo.",
                "No importa, acabaré con vosotros,",
                "no tenéis nada que hacer contra mi."
            ])
        elif self.story_stage == 4 and self.dialogue_box.finished:
            self.story_stage = 5
            self.show_dialogue = False
