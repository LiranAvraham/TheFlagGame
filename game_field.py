import random

from consts import *


def create_matrix():
    matrix = []

    for row in range(BOARD_NUM_ROWS):
        row = []

        for col in range(BOARD_NUM_COLS):
            row.append(EMPTY_PLACE)

        matrix.append(row)

    return matrix


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
            if matrix[row][col + i] != EMPTY_PLACE:
                can_place_mine = False

        if can_place_mine:
            for i in range(MINE_NUM_COLS):
                matrix[row][col + i] = MINE

            mines_created += 1