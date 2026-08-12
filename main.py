import pygame
import sys
from game_field import *

# Initialize pygame
pygame.init()

# Set up the window display
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Loading Images in Pygame")

# 1. Load the image and optimize its pixel format
# Use .convert_alpha() for transparent PNGs, or .convert() for JPGs
character_image = pygame.image.load("soldier.png").convert_alpha()
character_image = pygame.transform.scale(character_image, (100, 100))

# Game Loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False



            # 2. Draw (blit) the image onto the screen at coordinates (X, Y)
            screen.blit(character_image, (0, 0))

            # 3. Update the display to show changes
            pygame.display.flip()



    # Clear the screen with a color (R, G, B)

pygame.quit()
sys.exit()
