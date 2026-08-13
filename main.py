import pygame
import sys

from consts import *
from game_field import *

pygame.init()

screen = pygame.display.set_mode((LENGTH_WINDOW, HEIGHT_WINDOW))
pygame.display.set_caption("The Flag Game")

matrix = create_matrix()

flag_row, flag_col = add_flag_to_matrix(matrix)

add_mines_to_matrix(matrix)

soldier_row = 0
soldier_col = 0

cell_width = LENGTH_WINDOW // BOARD_NUM_COLS
cell_height = HEIGHT_WINDOW // BOARD_NUM_ROWS

soldier_image = pygame.transform.scale(SOLDIER_IMAGE, (cell_width * 2, cell_height * 4))

flag_image = pygame.transform.scale(FLAG_IMAGE, (cell_width * 4, cell_height * 3))

mine_image = pygame.transform.scale(MINE_IMAGE, (cell_width * 3, cell_height))

grass_image = pygame.transform.scale(GRASS_IMAGE, (LENGTH_GRASS, HEIGHT_GRASS))
grass_locations = []

show_mines = False
show_mines_start_time = 0

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            # show_mines = True


        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                show_mines = True
                show_mines_start_time = pygame.time.get_ticks()

                soldier_image = pygame.transform.scale(SOLDIER_IMAGE_NIGHT, (cell_width * 2, cell_height * 4))
                screen.blit(soldier_image, (soldier_col * cell_width, soldier_row * cell_height))

                screen.fill(BACKGROUND_COLOR)

            # if event.key == pygame.K_KP_ENTER:
            # elif event.key == pygame.K_KP_ENTER:
            #     screen.fill(BACKGROUND_COLOR_FOR_NIGHT_MODE)

            # else:
            #     soldier_image = pygame.transform.scale(SOLDIER_IMAGE_NIGHT, (cell_width * 2, cell_height * 4))
            #     screen.blit(soldier_image, (soldier_col * cell_width, soldier_row * cell_height))
            #     screen.fill(BACKGROUND_COLOR_FOR_NIGHT_MODE)

            if not show_mines:
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

    if show_mines:
        current_time = pygame.time.get_ticks()

        if current_time - show_mines_start_time >= 1000:
            show_mines = False
            soldier_image = pygame.transform.scale(SOLDIER_IMAGE, (cell_width * 2, cell_height * 4))
            # screen.fill(BACKGROUND_COLOR_FOR_NIGHT_MODE)
    # else:
    #     screen.fill(BACKGROUND_COLOR_FOR_NIGHT_MODE)

        pygame.display.flip()

    legs_row = soldier_row + SOLDIER_NUM_ROWS - 1

    for col in range(soldier_col, soldier_col + SOLDIER_NUM_COLS):
        if matrix[legs_row][col] == MINE:
            print("You Lost!")
            running = False
    if show_mines:
        screen.fill(BACKGROUND_COLOR_FOR_NIGHT_MODE)
    else:
        screen.fill(BACKGROUND_COLOR)

    if show_mines:
        # for row in range(BOARD_NUM_ROWS):
        #     for col in range(SOLDIER_NUM_COLS):
        #         if matrix[row][col] = MINE
        for row in range(BOARD_NUM_ROWS):
            for col in range(BOARD_NUM_COLS):
                if matrix[row][col] == MINE:
                    x = col * cell_width
                    y = row * cell_height
                    screen.blit(mine_image, (x, y))

    screen.blit(soldier_image, (soldier_col * cell_width, soldier_row * cell_height))

    screen.blit(flag_image, (flag_col * cell_width, flag_row * cell_height))

    pygame.display.flip()

pygame.quit()
sys.exit()

