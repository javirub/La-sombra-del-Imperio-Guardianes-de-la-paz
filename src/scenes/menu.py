# menu.py

import pygame
import sys




class MenuScene:
    def __init__(self, screen):
        self.screen = screen
        self.done = False
        # Configura aquí los elementos del menú

    def run(self):
        while not self.done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            # Aquí iría la lógica del menú (mostrar opciones, manejar entradas, etc.)

            pygame.display.flip()
