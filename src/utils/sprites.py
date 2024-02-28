import pygame


def load_sprite_sheet(sheet_path, cols, rows):
    sheet = pygame.image.load(sheet_path).convert_alpha()
    sheet_width, sheet_height = sheet.get_size()
    sprite_width = sheet_width // cols
    sprite_height = sheet_height // rows
    sprites = []

    for row in range(rows):
        for col in range(cols):
            x = col * sprite_width
            y = row * sprite_height
            sprite = sheet.subsurface(pygame.Rect(x, y, sprite_width, sprite_height))
            sprites.append(sprite)

    return sprites
