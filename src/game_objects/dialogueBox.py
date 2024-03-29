import pygame
from settings import *


class DialogueBox:
    def __init__(self, screen, font_path, font_size=24):
        self.screen = screen
        self.font = pygame.font.Font(font_path, font_size)
        self.rect = pygame.Rect(50, screen.get_height() - 150, screen.get_width() - 100, 100)
        self.text_color = pygame.Color('white')
        self.background_color = pygame.Color('black')
        self.border_color = pygame.Color('red')
        self.sprites = {
            'darth_vader': pygame.image.load(DARTH_VADER_SPRITE),
            'elon_musk': pygame.image.load(ELON_MUSK_SPRITE),
            'laughing_musk': pygame.image.load(LAUGHING_MUSK_SPRITE)
        }
        self.current_speaker = 'elon_musk'
        self.dialogue_lines = []
        self.current_line_index = 0
        self.finished = False

    def add_dialogue(self, dialogue):
        self.dialogue_lines = dialogue
        self.current_line_index = 0

    def next_line(self):
        if self.current_line_index < len(self.dialogue_lines) - 1:
            self.current_line_index += 1
        else:
            self.dialogue_lines = []
            self.finished = True
            self.current_line_index = 0

    def draw_text(self, text):
        wrapped_text = self.wrap_text(text, self.rect.width - 10)
        total_height = sum([self.font.render(line, True, self.text_color).get_height() for line in wrapped_text])
        y_offset = (self.rect.height - total_height) // 2  # Centro verticalmente
        for line in wrapped_text:
            text_surface = self.font.render(line, True, self.text_color)
            # Centro horizontalmente dentro de self.rect
            x_pos = self.rect.x + (self.rect.width - text_surface.get_width()) // 2
            self.screen.blit(text_surface, (x_pos, self.rect.y + y_offset))
            y_offset += text_surface.get_height()

    def wrap_text(self, text, max_width):
        words = text.split(' ')
        wrapped_lines = []
        current_line = ''
        for word in words:
            test_line = f"{current_line} {word}".strip()
            text_surface = self.font.render(test_line, True, self.text_color)
            if text_surface.get_width() > max_width:
                wrapped_lines.append(current_line)
                current_line = word
            else:
                current_line = test_line
        wrapped_lines.append(current_line)  # Add the last line
        return wrapped_lines

    def draw(self, text):
        # Draw background rectangle
        pygame.draw.rect(self.screen, self.background_color, self.rect)
        pygame.draw.rect(self.screen, self.border_color, self.rect, 3)

        # Determine sprite based on current speaker
        sprite = self.sprites[self.current_speaker]
        if self.current_speaker == 'darth_vader':
            self.screen.blit(sprite, (self.rect.x - sprite.get_width() / 2, self.rect.y - sprite.get_height() / 2))
        else:
            self.screen.blit(sprite, (self.rect.right - sprite.get_width() / 2, self.rect.y - sprite.get_height() / 2))

        # Draw the text
        if self.dialogue_lines:
            self.draw_text(self.dialogue_lines[self.current_line_index])
