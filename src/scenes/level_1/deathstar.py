# Nivel: Estrella de la muerte
from scenes.scene import Scene
from settings import *
import sys
import time
from game_objects.level_1.spaceships import DeathStar, TeslaRoadster
from utils.collision import *
from game_objects.dialogueBox import DialogueBox


class DeathstarScene(Scene):
    '''En este nivel tendremos que cargar energia a la estrella de la muerte para destruír la Tierra,
    pero ocurre un giro inesperado, golpeamos el Tesla Roadster de Elon Musk, advirtiendo a los humanos
    de la amenaza inminente. La Tierra se prepara para la batalla final.'''

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
        self.tesla = TeslaRoadster((WIDTH / 2 + 600, HEIGHT - 1200))
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
                    self.story_stage = 1
                    self.dialogue_box.add_dialogue([
                        "Elon Musk: ¿¡Quien ha atacado a mi Tesla Roadster!?"
                    ])
        if self.dialogue_box.finished and self.story_stage == 1:
            self.story_stage = 2
            self.dialogue_box.finished = False
            self.dialogue_box.current_speaker = 'darth_vader'
            self.dialogue_box.add_dialogue([
                "Darth Vader: ¿Que demonios hace un coche orbitando el planeta?"
            ])

        if self.dialogue_box.finished and self.story_stage == 2:
            self.story_stage = 3
            self.dialogue_box.finished = False
            self.dialogue_box.current_speaker = 'elon_musk'
            self.dialogue_box.add_dialogue([
                "Elon Musk: Era una demostración de lo que el ser humano puede lograr.",
                "Elon Musk: Toda mi vida he soñado con llegar a las estrellas.",
                "Elon Musk: Pero ahora, la humanidad está en peligro.",
                "Elon Musk: Debemos unirnos para enfrentar esta amenaza."
            ])
        if self.dialogue_box.finished and self.story_stage == 3:
            self.next_scene = "intro2"
            self.done = True

