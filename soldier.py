import consts

position = {}

def create():
    """
    Create soldier position initializes at 0,0
    :return: None
    """
    position['col'] = 0
    position['row'] = 0

def move(direction):
    """
    Move soldier
    :param direction: position where to move
    :return:
    """
    if direction == consts.MOVE_UP and position['row'] > 0:
        position['row'] -= 1
    elif direction == consts.MOVE_DOWN and position['row'] < consts.BOARD_ROWS - consts.SOLDIER_ROWS:
        position['row'] += 1
    elif direction == consts.MOVE_LEFT and  position['col'] > 0:
        position['col'] -= 1
    elif direction == consts.MOVE_RIGHT and position['col'] < consts.BOARD_COLS - consts.SOLDIER_COLS:
        position['col'] += 1


def update_location(coordinates):
    position['row'] = int(coordinates[0])
    position['col'] = int(coordinates[1])


def get_upper_body():
    """
    Return the indeces of the upper body of the soldier
    :return: the indeces in the field grid (list(tuple(int, int)))
    """
    coordinates = []
    for row in range(consts.SOLDIER_BODY_ROWS):
        for col in range(consts.SOLDIER_COLS):
            coordinates.append((position['row'] + col, position['col'] + row))
    return coordinates

def get_feet():
    """
    Return the indeces of the lower body of the soldier
    :return: the indeces in the field grid (list(tuple(int, int)))
    """
    coordinates = []
    for row in range(consts.SOLDIER_FEET_ROWS):
        for col in range(consts.SOLDIER_COLS):
            coordinates.append((position['row'] + col, position['col'] + row))
    return coordinates