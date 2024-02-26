import pygame

class Spaceship:
    def __init__(self, image_path, position):
       self.image = pygame.image.load(image_path).convert_alpha()
       self.rect = self.image.get_rect(center=position)

    def draw(self, screen):
        screen.blit(self.image, self.rect)