#imports
import pygame
from consts import *

game_display = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))


def draw_screen(field, given_row, given_col):
    """
    func that draws the screen and creates a background
    :param given_col:
    :param given_row:
    :param field: field is a list of lists of numbers - each representing if something is in the block (used in draw_bushes and draw_mines)
    :return: none
    """
    bg = pygame.image.load(BACKGROUND)
    bg = pygame.transform.scale(bg, (WINDOW_WIDTH, WINDOW_HEIGHT))
    game_display.blit(bg)
    draw_bushes(field)
    draw_flag()
    draw_soldier(given_row, given_col)
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
                game_display.blit(bush, (j*CELL_SIZE, i*CELL_SIZE))



def draw_flag():
    """
    func that draws a flag at the bottom of the screen
    :return: none
    """
    flag_row = BOARD_ROWS - FLAG_ROWS - 0.5
    flag_col = BOARD_COLS - FLAG_COLS
    flag = pygame.image.load(FLAG)
    flag = pygame.transform.scale(flag, (FLAG_COLS*CELL_SIZE, FLAG_ROWS*CELL_SIZE))
    game_display.blit(flag, (flag_col*CELL_SIZE, flag_row*CELL_SIZE))


def draw_soldier(given_row, given_col):
    """
    func that receives a given row and column and draws a soldier in this location
    :param given_row: our y
    :param given_col: our x
    :return: none
    """
    soldier = pygame.image.load(SOLDIER)
    soldier = pygame.transform.scale(soldier, (SOLDIER_ROWS*CELL_SIZE, SOLDIER_COLS*CELL_SIZE))
    game_display.blit(soldier, (given_col*CELL_SIZE, given_row*CELL_SIZE))



def draw_mines(field, given_row, given_col):
    """
    func that handles what happens when the player presses enter - initializes the board,
    draws the grid lines, receives random locations of mines (using numbers) and
    draws mines in those locations, and creates a new soldier
    :param field: field is a list of lists of numbers - each representing if something is in the block
    :return: none
    """
    #first we're going to create a new screen to overwrite the bushes, soldier, and flag
    bg = pygame.image.load(BACKGROUND)
    bg = pygame.transform.scale(bg, (WINDOW_WIDTH, WINDOW_HEIGHT))
    game_display.blit(bg)
    #then we are going to create the grid lines
    for x in range(0, WINDOW_WIDTH, CELL_SIZE):
        for y in range(0, WINDOW_HEIGHT, CELL_SIZE):
            rect = pygame.Rect(x, y, CELL_SIZE, CELL_SIZE)
            pygame.draw.rect(game_display, GREEN, rect, 1)
    #afterward we're placing mines in random places
    for i in range (BOARD_ROWS):
        for j in range (BOARD_COLS):
            if field[i][j] == MINE_SQUARE or field[i][j] == BUSH_N_MINE_SQUARE:
                mine = pygame.image.load(MINE)
                mine = pygame.transform.scale(mine, (MINE_COLS*CELL_SIZE, MINE_ROWS*CELL_SIZE))
                game_display.blit(mine, (j*CELL_SIZE, i*CELL_SIZE))
    #and finally we're going to draw a new soldier
    night_soldier = pygame.image.load(SOLDIER_NIGHT)
    night_soldier = pygame.transform.scale(night_soldier, (SOLDIER_ROWS*CELL_SIZE, SOLDIER_COLS*CELL_SIZE))
    game_display.blit(night_soldier, (given_col*CELL_SIZE, given_row*CELL_SIZE))
    pygame.display.flip()



def screen_win():
    """
    func that creates a new screen and declares a victory
    :return: none
    """
    pink_bg = pygame.image.load(PINK_BACKGROUND)
    pink_bg = pygame.transform.scale(pink_bg, (WINDOW_WIDTH, WINDOW_HEIGHT))
    game_display.blit(pink_bg)
    font = pygame.font.Font('Butterpop.ttf', 32)
    text = font.render("You've won!!!", True, WHITE, GOLD)
    textRect = text.get_rect()
    textRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
    game_display.blit(text, textRect)
    pygame.display.flip()



def screen_lose():
    """
    func that creates a new screen and declares a loss
    :return: none
    """
    pink_bg = pygame.image.load(PINK_BACKGROUND)
    pink_bg = pygame.transform.scale(pink_bg, (WINDOW_WIDTH, WINDOW_HEIGHT))
    game_display.blit(pink_bg)
    font = pygame.font.Font('Nightcore Demo.ttf', 32)
    text = font.render("You've lost", True, WHITE, GOLD)
    textRect = text.get_rect()
    textRect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)
    game_display.blit(text, textRect)
    pygame.display.flip()
