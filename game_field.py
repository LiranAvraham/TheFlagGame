import random

from consts import *

def add_flag_to_matrix(matrix):
    flag_row = BOARD_NUM_ROWS - FLAG_NUM_ROWS
    flag_col = BOARD_NUM_COLS - FLAG_NUM_COLS

    for row in range(flag_row, flag_row + FLAG_NUM_ROWS):
        for col in range(flag_col, flag_col + FLAG_NUM_COLS):
            matrix[row][col] = FLAG

    return flag_row, flag_col

def add_mines_to_matrix(matrix):
    mines_created = 0

    while mines_created < NUM_OF_MINES:
        row = random.randint(0, BOARD_NUM_ROWS - 1)
        col = random.randint(0, BOARD_NUM_COLS - MINE_NUM_COLS)

        can_place_mine = True

        for i in range(MINE_NUM_COLS):
            if matrix[row][col] != EMPTY_PLACE:
                can_place_mine = False

        if can_place_mine:
            for i in range(MINE_NUM_COLS):
                matrix[row][col] = MINE

            mines_created += 1
def create_matrix_grass():
    grass_created = 0
    matrix_grass= []
    can_place_GRASS = True
    for row in range(BOARD_NUM_ROWS):
        row = []

        for col in range(BOARD_NUM_COLS):
            row.append(EMPTY_PLACE)

        matrix_grass.append(row)
    while grass_created< NUM_OF_GRASS:
        row = random.randint(0, BOARD_NUM_ROWS - 1)
        col = random.randint(0, BOARD_NUM_COLS -GRASS_NUM_COLS)

        for i in range(GRASS_NUM_COLS):
            if matrix_grass[row][col] != EMPTY_PLACE:
                can_place_GRASS = False
        if can_place_GRASS:
            for i in range(GRASS_NUM_COLS):
                matrix_grass[row][col] =GRASS
            grass_created += 1
    return matrix_grass

# def show_image_grass(matrix_grass):
#     for row in matrix_grass:
#         for col in row:
#             if col == GRASS:
#                 pygame.transform.scale(GRASS_IMAGE, (LENGTH_GRASS, HEIGHT_GRASS))
#
