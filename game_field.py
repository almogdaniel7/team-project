import random

import consts

field = []

def create():
    for i in range(consts.BOARD_ROWS):
        row = []
        for j in range(consts.BOARD_COLS):
            row.append(consts.EMPTY_SQUARE)
        field.append(row)
    add_mines()
    add_bushes()


def add_mines():
    for i in range(consts.MINES_COUNT):
        row = random.randint(0, consts.BOARD_ROWS - 1)
        col = random.randint(0, consts.BOARD_COLS - 1)
        while (field[row][col] != consts.EMPTY_SQUARE
               or row < 6 or col < 2):
            row = random.randint(0, consts.BOARD_ROWS - 1)
            col = random.randint(0, consts.BOARD_COLS - 1)
        field[row][col] = consts.MINE_SQUARE


def add_bushes():
    for i in range(consts.MINES_COUNT):
        row = random.randint(0, consts.BOARD_ROWS - 1)
        col = random.randint(0, consts.BOARD_COLS - 1)
        while (field[row][col] != consts.EMPTY_SQUARE
               or row < 6 or col < 2):
            row = random.randint(0, consts.BOARD_ROWS - 1)
            col = random.randint(0, consts.BOARD_COLS - 1)
        if field[row][col] == consts.MINE_SQUARE:
            field[row][col] = consts.BUSH_N_MINE_SQUARE
        else: field[row][col] = consts.BUSH_SQUARE


def flag_contact(coordinates):
    """
    Returns True if at least one of the coordinates int the list touches the flag
    :param coordinates:
    :return:
    """
    for coordinate in coordinates:
        if (coordinates[0] >= consts.BOARD_ROWS - consts.FLAG_ROWS - 1
                or coordinates[1] >= consts.BOARD_COLS - consts.FLAG_COLS - 1):
            return True
    return False



def print_field():
    for i in range(consts.BOARD_ROWS):
        for j in range(consts.BOARD_COLS):
            print(field[i][j], end='\t')
        print()


