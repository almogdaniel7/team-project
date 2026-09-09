#to create a game board
BOARD_ROWS = 25
BOARD_COLS = 50
CELL_SIZE = 20 # pixels per cell
WINDOW_WIDTH = BOARD_COLS * CELL_SIZE
WINDOW_HEIGHT = BOARD_ROWS * CELL_SIZE

#to create a soldier
SOLDIER_ROWS = 4
SOLDIER_COLS = 4
SOLDIER_BODY_ROWS = 3 # the upper part
SOLDIER_FEET_ROWS = 1 # the lower part

#to create a flag
FLAG_ROWS = 4
FLAG_COLS = 4

#to create mines
MINES_COUNT = 15
MINE_ROWS = 2
MINE_COLS = 4

#to create bushes
BUSH_ROWS = 3
BUSH_COLS = 3

# For the game_field grid
EMPTY_SQUARE = 0
BUSH_SQUARE = 1
MINE_SQUARE = 2
BUSH_N_MINE_SQUARE = 3
FLAG_SQUARE = 4

# game states
STATE_RUNNING = 0
STATE_LOST = 1
STATE_WON = 2

# Movement markers
MOVE_UP = 0
MOVE_DOWN = 1
MOVE_LEFT = 2
MOVE_RIGHT = 3

#images
BACKGROUND = 'images/bg.jpg'
PINK_BACKGROUND = 'images/pink.jpg'
EXPLOSION = 'images/explosion.png'
FLAG = 'images/flag.png'
GRASS = 'images/kebab.png'
GUARD = 'images/guard.png'
INJURY = 'images/injury.png'
MINE = 'images/av.png'
SNAKE = 'images/snake.png'
SOLDIER = 'images/sap.png'
SOLDIER_NIGHT = 'images/sapsoldier.png'
TELEPORT = 'images/teleport.png'

#sound effects
LOSE_SOUND = 'sounds/explosion.mp3'
WIN_SOUND = 'sounds/success.mp3'
GAME_OVER_SOUND = 'sounds/game_over.mp3'

#colors
GOLD = (255, 215, 0, 255)
WHITE = (255, 255, 255)
GREEN =  (0, 255, 0, 255)

#database
DATA = 'data.csv'
