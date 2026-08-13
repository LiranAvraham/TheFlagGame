from consts import *
import pygame

def create_matrix():
    matrix = []

    for row in range(BOARD_NUM_ROWS):
        row = []

        for col in range(BOARD_NUM_COLS):
            row.append(EMPTY_PLACE)

        matrix.append(row)

    return matrix

def create_bord_cells():
    screen_matrix = []
    for row in range(BOARD_NUM_ROWS):
        screen_matrix.append([])
        for col in range(BOARD_NUM_COLS):
            screen_matrix[row].append(EMPTY_PLACE)
    return screen_matrix
pygame.init()
SCREEN =pygame.display.set_mode((LENGTH_WINDOW,HEIGHT_WINDOW))
def x_and_y(screen_matrix):
    for row in range(len(screen_matrix)):
        for col in range(len(screen_matrix[row])):
            x =col*CELL_SIZE
            y= row * CELL_SIZE

            rect = pygame.Rect(x,y,CELL_SIZE-1, CELL_SIZE-1)
            pygame.draw.rect(SCREEN, BACKGROUND_COLOR,rect)
            pygame.display.flip()
print(create_bord_cells())
x_and_y(create_bord_cells())

