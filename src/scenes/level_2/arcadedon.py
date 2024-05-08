import random
import sys

from game_objects.dialogueBox import DialogueBox
from game_objects.level_2.spaceships import *
from utils.collision import *
from ..scene import Scene


class Arcadedon(Scene):
    def __init__(self, screen, enemies=None):
        super().__init__(screen)
        self.active_enemies = None
        self.next_scene = "menu"
        pygame.mixer.init()
        self.background = pygame.image.load(BACKGROUND_PATH).convert_alpha()
        self.earth = pygame.image.load(EARTH_PLANET_SPRITE).convert_alpha()

        # Player
        self.deathstar = Deathstar((WIDTH / 2, HEIGHT + 100), 5)
        self.last_shoot_time = pygame.time.get_ticks()
        self.TIE_SPRITE = pygame.image.load(ARCADE_TIE_SPRITE).convert_alpha()
        self.player = Tie((WIDTH / 2, HEIGHT - 200), self.TIE_SPRITE)

        # Dialogue
        self.dialogue_box = DialogueBox(screen, FONT_PATH, 24)
        self.dialogue_box.current_speaker = 'darth_vader'
        self.show_dialogue = False
        self.font = pygame.font.Font(None, 40)
        self.story_stage = 0

        # Enemies
        self.enemy_spawn = LEVEL2_ENEMIES
        self.TESLA_SPRITE = pygame.image.load(ARCADE_TESLA_SPRITE).convert_alpha()  # This way only one time is loaded
        # Si hemos precargado los enemigos en la escena anterior, los cargamos, si no, los creamos
        # Es necesario precargar ya que la creación de los enemigos es muy costosa y ralentiza el juego
        if enemies is not None:
            enemy_count = len(enemies)
            if enemy_count >= self.enemy_spawn:
                self.enemies = enemies
            else:
                self.enemies = enemies + [TeslaRoadster((WIDTH - 220, 100), self.TESLA_SPRITE)
                                          for _ in range(self.enemy_spawn - enemy_count)]
        else:
            self.enemies = [TeslaRoadster((WIDTH - 220, 100), self.TESLA_SPRITE) for _ in range(self.enemy_spawn)]
        self.enemy_projectiles = []  # This is necessary to avoid a bug in the game when the enemy dies
        self.last_time_spawn = pygame.time.get_ticks()
        self.time_to_shoot = random.randint(500, 4000)

    def update(self):
        # Game actions
        self.player.update()
        # Spawn enemies
        self.spawn_enemies()
        self.check_active_enemies()
        for enemy in self.active_enemies:
            enemy.update()
        self.check_collisions()
        self.enemy_shoot()
        self.enemy_movement()
        self.check_win_condition()
        # Story dialogue
        self.show_dialogues()

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.deathstar.draw(self.screen)
        self.player.draw(self.screen)

        for enemy in self.active_enemies:
            enemy.draw(self.screen)
        # TODO: Enemy projectiles disappear when spaceship is destroyed
        self.screen.blit(self.earth, (WIDTH - 200, -100))

        if self.show_dialogue:
            self.dialogue_box.draw(self.screen)

        if self.player.life == 3:
            self.screen.blit(self.TIE_SPRITE, (WIDTH - 200, HEIGHT - 100))
            self.screen.blit(self.TIE_SPRITE, (WIDTH - 150, HEIGHT - 100))
            self.screen.blit(self.TIE_SPRITE, (WIDTH - 100, HEIGHT - 100))
        elif self.player.life == 2:
            self.screen.blit(self.TIE_SPRITE, (WIDTH - 200, HEIGHT - 100))
            self.screen.blit(self.TIE_SPRITE, (WIDTH - 150, HEIGHT - 100))
        elif self.player.life == 1:
            self.screen.blit(self.TIE_SPRITE, (WIDTH - 200, HEIGHT - 100))

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
            for enemy in self.active_enemies:
                if check_collision(projectile.hitbox, enemy.rect):
                    enemy.life -= 1
                    try:
                        self.player.projectiles.remove(projectile)
                    except ValueError:
                        pass  # If the projectile is already removed, ignore the exception
                    if enemy.life <= 0:
                        enemy.activated = False
        for enemy in self.active_enemies:
            if check_collision(self.player.rect, enemy.rect):
                self.player.start_hit_animation()
                enemy.activated = False
            if check_collision(self.deathstar.rect, enemy.rect):
                self.next_scene = "menu"
                self.done = True
            for projectile in enemy.projectiles:
                if check_collision(projectile.hitbox, self.player.rect):
                    self.player.start_hit_animation()
                    try:
                        enemy.projectiles.remove(projectile)
                    except ValueError:
                        pass

    def enemy_shoot(self):
        if self.active_enemies:
            random_enemy = random.choice(self.active_enemies)
            current_time = pygame.time.get_ticks()

            if current_time - self.last_shoot_time > self.time_to_shoot:
                self.last_shoot_time = current_time
                random_enemy.shooting = True
                self.enemy_projectiles.append(random_enemy.create_projectile())
                self.time_to_shoot = random.randint(500, 1500)

    def enemy_movement(self):
        for enemy in self.active_enemies:
            if enemy.rect.x + enemy.rect.width > (WIDTH - 180) or enemy.rect.x < 0:
                enemy.speed = -enemy.speed * 1.25
                enemy.rect.y += 70
            enemy.rect.x -= enemy.speed

    def spawn_enemies(self):
        if pygame.time.get_ticks() - self.last_time_spawn > 300 and self.enemy_spawn > 0:
            self.enemy_spawn -= 1
            self.enemies[self.enemy_spawn].activated = True
            self.last_time_spawn = pygame.time.get_ticks()

    def check_active_enemies(self):
        self.active_enemies = [enemy for enemy in self.enemies if enemy.activated]

    def check_win_condition(self):
        if not self.active_enemies and self.enemy_spawn <= 0:
            self.next_scene = "menu"
            self.show_dialogue = True
        if self.player.life <= 0 and not self.player.animating:
            self.next_scene = "Gameover"
            self.done = True

    def show_dialogues(self):
        if self.show_dialogue and self.story_stage == 0:
            self.story_stage = 1
            if self.player.life == 0:
                player_deaths = 1
            else:
                player_deaths = 0

            self.dialogue_box.add_dialogue([
                f"Vaya, eso ha sido fácil, 50 a {player_deaths}."
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
