import pygame
import sys

from consts import *
from game_field import *

pygame.init()

screen = pygame.display.set_mode((LENGTH_WINDOW, HEIGHT_WINDOW))
pygame.display.set_caption("The Flag Game")

matrix = create_matrix()

flag_row, flag_col = add_flag_to_matrix(matrix)

soldier_row = 0
soldier_col = 0

cell_width = LENGTH_WINDOW // BOARD_NUM_COLS
cell_height = HEIGHT_WINDOW // BOARD_NUM_ROWS

soldier_image = pygame.transform.scale(SOLDIER_IMAGE, (cell_width * 8, cell_height * 4))

flag_image = pygame.transform.scale(FLAG_IMAGE, (cell_width * 8, cell_height * 4))

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if soldier_row > 0:
                    soldier_row -= 1

            elif event.key == pygame.K_DOWN:
                if soldier_row + SOLDIER_NUM_ROWS < BOARD_NUM_ROWS:
                    soldier_row += 1

            elif event.key == pygame.K_LEFT:
                if soldier_col > 0:
                    soldier_col -= 1

            elif event.key == pygame.K_RIGHT:
                if soldier_col + SOLDIER_NUM_COLS < BOARD_NUM_COLS:
                    soldier_col += 1


    screen.fill(BACKGROUND_COLOR)

    screen.blit(soldier_image, (soldier_col * cell_width, soldier_row * cell_height))

    screen.blit(flag_image, (flag_col * cell_width, flag_row * cell_height))

    pygame.display.flip()

pygame.quit()
sys.exit()