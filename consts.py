#to create a game board
BOARD_ROWS = 25
BOARD_COLS = 50
CELL_SIZE = 20 # pixels per cell
WINDOW_WIDTH = BOARD_COLS * CELL_SIZE
WINDOW_HEIGHT = BOARD_ROWS * CELL_SIZE

#to create a soldier
SOLDIER_ROWS = 4
SOLDIER_COLS = 2
SOLDIER_BODY_ROWS = 3 # the upper part
SOLDIER_FEET_ROWS = 1 # the lower part

#to create a flag
FLAG_ROWS = 3
FLAG_COLS = 4

#to create mines
MINES_COUNT = 20
MINE_ROWS = 1
MINE_COLS = 3

# For the game_field grid
EMPTY_SQUARE = 0
BUSH_SQUARE = 1
MINE_SQUARE = 2
BUSH_N_MINE_SQUARE = 3

STATE_RUNNING = 0
STATE_LOST = 1

# Movement markers
MOVE_UP = 0
MOVE_DOWN = 1
MOVE_LEFT = 2
MOVE_RIGHT = 3