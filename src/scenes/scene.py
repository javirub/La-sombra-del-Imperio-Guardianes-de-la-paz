import pygame
import src.settings
import sys


class Scene:
    def __init__(self, screen):
        self.screen = screen
        self.done = False
        self.next_scene = None

    def run(self):
        while not self.done:
            self.handle_events()
            self.update()
            self.draw()
            pygame.display.flip()
            pygame.time.Clock().tick(src.settings.FPS)
        pygame.mixer.music.stop()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

    def update(self):
        pass

    def draw(self):
        pass
