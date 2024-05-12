import sys
import random

from game_objects.dialogueBox import DialogueBox
from game_objects.arcade.spaceships import *
from game_objects.arcade.powerups import *
from utils.collision import *
from scenes.scene import Scene


class Arcadedon_with_steroids(Scene):
    def __init__(self, screen, enemies=None):
        super().__init__(screen)
        self.active_enemies = None
        self.next_scene = "menu"
        pygame.mixer.init()
        pygame.mixer.set_num_channels(20)
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
        self.enemies = []
        self.enemy_spawn = LEVEL4_ENEMIES
        self.TESLA_SPRITE = pygame.image.load(TESLA_UPGRADED_SPRITE).convert_alpha()  # This way only one time is loaded
        self.KOREA_TANK_SPRITE = pygame.image.load(KOREA_TANK_SPRITE).convert_alpha()
        # Si hemos precargado los enemigos en la escena anterior, los cargamos, si no, los creamos
        # Es necesario precargar ya que la creación de los enemigos es muy costosa y ralentiza el juego
        if enemies is not None:
            enemy_count = len(enemies)
            # Si se han cargado todos los enemigos, no creamos nuevos. Si no, creamos los que falten
            self.enemies = enemies
            while self.enemy_spawn - enemy_count > 0:
                if enemy_count % 5 == 0:
                    self.enemies.append(ComunistSpaceship((WIDTH - 220, 100), self.KOREA_TANK_SPRITE))
                else:
                    self.enemies.append(TeslaRoadster((WIDTH - 220, 100), self.TESLA_SPRITE))
                enemy_count += 1
        # Si no se ha cargado ningún enemigo, creamos todos
        else:
            for enemy in range(self.enemy_spawn):
                if enemy % 5 == 0:
                    self.enemies.append(ComunistSpaceship((WIDTH - 220, 100), self.KOREA_TANK_SPRITE))
                else:
                    self.enemies.append(TeslaRoadster((WIDTH - 220, 100), self.TESLA_SPRITE))
        self.last_time_spawn = pygame.time.get_ticks()
        self.time_to_shoot = random.randint(500, 2000)

        self.powerups = []

    def update(self):
        # Spawn enemies
        self.spawn_enemies()
        self.check_active_enemies()
        # Game actions
        self.player.update()
        for enemy in self.active_enemies:
            enemy.update()
        for powerup in self.powerups:
            powerup.update()
        self.check_collisions()
        self.enemy_shoot()
        self.enemy_movement()

        self.check_win_condition()
        # Story dialogue
        self.show_dialogues()

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.earth, (WIDTH - 200, -100))
        self.deathstar.draw(self.screen)
        self.player.draw(self.screen)

        for enemy in self.active_enemies:
            enemy.draw(self.screen)

        for powerup in self.powerups:
            powerup.draw(self.screen)

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
                        self.check_powerup(enemy)
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

        for powerup in self.powerups:
            if check_collision(powerup.rect, self.player.rect):
                if isinstance(powerup, CadencePowerup):
                    if self.player.cadence > 300:
                        self.player.cadence -= 100
                elif isinstance(powerup, SpeedPowerup):
                    if self.player.speed < 10:
                        self.player.speed += 1
                elif isinstance(powerup, HealthPowerup):
                    if self.player.life < 3:
                        self.player.life += 1
                self.powerups.remove(powerup)

    def enemy_shoot(self):
        if self.active_enemies:
            random_enemy = random.choice(self.active_enemies)
            current_time = pygame.time.get_ticks()

            if current_time - self.last_shoot_time > self.time_to_shoot:
                self.last_shoot_time = current_time
                random_enemy.shooting = True
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

    def check_powerup(self, enemy):
        random_number = random.randint(0, 50)
        if random_number in range(0, 5):
            # Cadence powerup
            self.powerups.append(CadencePowerup(enemy.rect.center))
        elif random_number in range(10, 15):
            # Speed powerup
            self.powerups.append(SpeedPowerup(enemy.rect.center))
        elif random_number in range(20, 25):
            # Health powerup
            self.powerups.append(HealthPowerup(enemy.rect.center))
        else:
            return None

    def show_dialogues(self):
        if self.show_dialogue and self.story_stage == 0:
            self.story_stage = 1
            self.dialogue_box.add_dialogue([
                "¿Eso es todo?",
                "Ni uniendo vuestras fuerzas podéis conmigo."
            ])
        elif self.story_stage == 1 and self.dialogue_box.finished:
            self.story_stage = 2
            self.dialogue_box.finished = False
            self.dialogue_box.current_speaker = 'elon_musk'
            self.dialogue_box.add_dialogue([
                "La cosa se ha puesto seria.",
                "Ahora sus naves suenan temibles."
            ])
        elif self.story_stage == 2 and self.dialogue_box.finished:
            self.story_stage = 3
            self.dialogue_box.finished = False
            self.dialogue_box.current_speaker = 'Kim Jong Ill'
            self.dialogue_box.add_dialogue([
                "¿Que vamos a hacer?",
                "Ni tan siquiera unidos podemos con él."
            ])
        elif self.story_stage == 3 and self.dialogue_box.finished:
            self.story_stage = 4
            self.dialogue_box.finished = False
            self.dialogue_box.current_speaker = 'darth_vader'
            self.dialogue_box.add_dialogue([
                "No tenéis que hacer nada.",
                "El fin del planeta tierra ha llegado."
            ])
        elif self.story_stage == 4 and self.dialogue_box.finished:
            self.show_dialogue = False
            self.next_scene = "deathstar3"
            self.done = True
