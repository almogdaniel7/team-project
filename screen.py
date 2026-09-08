#imports
import pygame
from consts import *

game_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


def draw_screen(field):
    """
    func that draws the screen and creates a background
    :param field: field is a list of lists of numbers - each representing if something is in the block (used in draw_bushes and draw_mines)
    :return: none
    """
    bg = pygame.image.load(BACKGROUND)
    bg = pygame.transform.scale(bg, (WINDOW_WIDTH, WINDOW_HEIGHT))
    game_display.blit(bg)
    draw_bushes(field)
    draw_flag()
    pygame.display.flip()



def draw_bushes(field):
    """
    func that receives random locations of bushes (using numbers) and draws bushes in those locations
    :param field: field is a list of lists of numbers - each representing if something is in the block
    :return: none
    """
    for i in range (BOARD_ROWS):
        for j in range (BOARD_COLS):
            if field[i][j] == BUSH_SQUARE or field[i][j] == BUSH_N_MINE_SQUARE:
                bush = pygame.image.load(GRASS)
                bush = pygame.transform.scale(bush, (BUSH_ROWS*CELL_SIZE, BUSH_COLS*CELL_SIZE))
                game_display.blit(bush, bush.get_rect(center=(j*CELL_SIZE, i*CELL_SIZE)))



def draw_mines(field):
    """
    func that receives random locations of mines (using numbers) and draws mines in those locations
    :param field: field is a list of lists of numbers - each representing if something is in the block
    :return: none
    """
    for i in range (BOARD_ROWS):
        for j in range (BOARD_COLS):
            if field[i][j] == MINE_SQUARE or field[i][j] == BUSH_N_MINE_SQUARE:
                mine = pygame.image.load(MINE)
                mine = pygame.transform.scale(mine, (MINE_COLS*CELL_SIZE, MINE_ROWS*CELL_SIZE))
                game_display.blit(mine, mine.get_rect(center=(j*CELL_SIZE, i*CELL_SIZE)))
    pygame.display.flip()



def draw_flag():
    flag_row = BOARD_ROWS - FLAG_ROWS + 0.75
    flag_col = BOARD_COLS - FLAG_COLS + 2.2
    flag = pygame.image.load(FLAG)
    flag = pygame.transform.scale(flag, (FLAG_ROWS*CELL_SIZE, FLAG_COLS*CELL_SIZE))
    game_display.blit(flag, flag.get_rect(center=(flag_col*CELL_SIZE, flag_row*CELL_SIZE)))




def draw_soldier(given_row, given_col):
    soldier = pygame.image.load(SOLDIER)
    soldier = pygame.transform.scale(soldier, (SOLDIER_ROWS*CELL_SIZE, SOLDIER_COLS*CELL_SIZE))
    game_display.blit(soldier, soldier.get_rect(center=(given_row*CELL_SIZE, given_col*CELL_SIZE)))

