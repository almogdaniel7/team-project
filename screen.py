#imports
import pygame
from consts import *

game_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))

def draw_screen(field):
    bg = pygame.image.load(BACKGROUND)
    bg = pygame.transform.scale(bg, (WINDOW_WIDTH, WINDOW_HEIGHT))
    game_display.blit(bg)
    pygame.display.flip()
    draw_bushes(field)

def draw_bushes(field):
    for i in range (BOARD_ROWS):
        for j in range (BOARD_COLS):
            if field[i][j] == BUSH_SQUARE or field[i][j] == BUSH_N_MINE_SQUARE:
                bush = pygame.image.load(GRASS)
                bush = pygame.transform.scale(bush, (BUSH_ROWS, BUSH_COLS))
                game_display.blit(bush)
                pygame.display.flip()
