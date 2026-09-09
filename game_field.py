import random

import consts

field = []

def create():
    """
    Function that initializes the game field with empty squares and then adds
    the mines and bushes to it
    :return:
    """
    for i in range(consts.BOARD_ROWS):
        row = []
        for j in range(consts.BOARD_COLS):
            if (j >= (consts.BOARD_COLS - consts.FLAG_COLS - 1)
                    and i >= (consts.BOARD_ROWS - consts.FLAG_ROWS - 1)):
                row.append(consts.FLAG_SQUARE)
            else:
                row.append(consts.EMPTY_SQUARE)
        field.append(row)
    add_mines()
    add_bushes()


def change_field(new_field):
    field = new_field


def add_mines():
    """
    Function that randomly adds 20 mines around the field
    :return:
    """
    for i in range(consts.MINES_COUNT):
        row = random.randint(0, consts.BOARD_ROWS - 1)
        col = random.randint(0, consts.BOARD_COLS - 1)
        while (field[row][col] != consts.EMPTY_SQUARE
               or row < 6 or col < 2):
            row = random.randint(0, consts.BOARD_ROWS - 1)
            col = random.randint(0, consts.BOARD_COLS - 1)
        field[row][col] = consts.MINE_SQUARE


def add_bushes():
    """
    Function that randomly adds 20 bushes around the field
    :return: None
    """
    for i in range(consts.MINES_COUNT):
        row = random.randint(0, consts.BOARD_ROWS - 1)
        col = random.randint(0, consts.BOARD_COLS - 1)
        while (field[row][col] == consts.BUSH_SQUARE
            or field[row][col] == consts.BUSH_N_MINE_SQUARE
            or field[row][col] == consts.FLAG_SQUARE
               or row < 6 or col < 2):
            row = random.randint(0, consts.BOARD_ROWS - 1)
            col = random.randint(0, consts.BOARD_COLS - 1)
        if field[row][col] == consts.MINE_SQUARE:
            field[row][col] = consts.BUSH_N_MINE_SQUARE
        else: field[row][col] = consts.BUSH_SQUARE


def flag_contact(coordinates):
    """
    Returns True if at least one of the coordinates int the list touches the flag
    :param coordinates: coordinates to check for contact with the flag (list(tuple(int)))
    :return: True if at least one of the coordinates int the list touches the flag (boolean)
    """
    for coordinate in coordinates:
        if field[coordinate[0]][coordinate[1]] == consts.FLAG_SQUARE:
            return True
    return False


def mine_contact(coordinates):
    """
    Returns true if at least one of the coordinates int the list touches a mine
    :param coordinates: coordinates to check for contact with the mine (list(tuple(int)))
    :return: True if at least one of the coordinates int the list touches a mine (boolean)
    """
    for coordinate in coordinates:
        for i in range(consts.MINE_COLS):
            if (field[coordinate[0]][coordinate[1] + i] == consts.MINE_SQUARE
                    or field[coordinate[0]][coordinate[1] + i] == consts.BUSH_N_MINE_SQUARE):
                return True
    return False


def print_field():
    """
    Prints the field on the screen
    TO BE DELETED LATER
    :return:
    """
    for i in range(consts.BOARD_ROWS):
        for j in range(consts.BOARD_COLS):
            print(field[i][j], end='\t')
        print()


