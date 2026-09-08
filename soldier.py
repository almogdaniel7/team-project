import consts

position = {}

def create():
    position['x'] = 0
    position['y'] = 0

def move(direction):
    if direction == consts.MOVE_UP and position['y'] > 0:
        position['y'] -= 1
    elif direction == consts.MOVE_DOWN and position['y'] < consts.BOARD_ROWS - 1:
        position['y'] += 1
    elif direction == consts.MOVE_LEFT and  position['x'] > 0:
        position['x'] -= 1
    elif direction == consts.MOVE_RIGHT and position['x'] < consts.BOARD_COLS - 1:
        position['x'] += 1

def get_upper_body():
    coordinates = []
    for row in range(consts.SOLDIER_BODY_ROWS + 1):
        for col in range(consts.SOLDIER_COLS + 1):
            coordinates.append((position['x'] + row, position['y'] + col))
    return coordinates

def get_feet():
    coordinates = []
    for row in range(consts.SOLDIER_FEET_ROWS):
        for col in range(consts.SOLDIER_COLS):
            coordinates.append((position['x'] + row, position['y'] + col))
    return coordinates