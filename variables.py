import pygame

pygame.init()

# initialize pygame variables
screen = pygame.display.set_mode((810, 810))
clock = pygame.time.Clock()

# Counting Variables
array_index = 0
queue = -1
phase = 1
turn = 1
capture_turns = 0
lives = 3
win_number = 0

pawns_count = 0
# knights_count = 0
# bishops_count = 0
# rooks_count = 0
# queens_count = 0
# kings_count = 0

pawns_spawned = 0
# knights_spawned = 0
# bishops_spawned = 0
# rooks_spawned = 0
# queens_spawned = 0
# kings_spawned = 0

pawns_killed = 0
# knights_killed = 0
# bishops_killed = 0
# rooks_killed = 0
# queens_killed = 0
# kings_killed = 0

# List Variables
all_sprites_list = pygame.sprite.Group()
pawn_list = pygame.sprite.Group()
# knight_list = pygame.sprite.Group()
# bishop_list = pygame.sprite.Group()
# rook_list = pygame.sprite.Group()
# queen_list = pygame.sprite.Group()
# king_list = pygame.sprite.Group()

# Color Constants
WHITE = (232, 221, 201)
BLACK = (57, 59, 58)
LIGHTBLACK = (70, 72, 71)
BROWN = (150, 81, 16)

# Boolean Variables
done = False
can_spawn_pawns = True
# can_spawn_knights = True
# can_spawn_bishops = True
# can_spawn_rooks = True
# can_spawn_queens = True
# can_spawn_kings = True

# Space Constants
allowed_move = pygame.Surface((45, 45))
allowed_move.set_alpha(128)
allowed_move.fill((79, 121, 66))

selected_move = pygame.Surface((45, 45))
selected_move.set_alpha(192)
selected_move.fill((255, 0, 0))

# Array Variables

player_spawn_locations = [(405, 405), (360, 360), (405, 360), (360, 405)]

piece_types = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']

x_position_list = [45, 90, 135, 180, 225, 270, 315,
                   360, 405, 450, 495, 540, 585, 630, 675, 720]

y_position_list = [45, 90, 135, 180, 225, 270, 315,
                   360, 405, 450, 495, 540, 585, 630, 675, 720]

position_list = [(45, 45), (45, 720), (90, 45), (90, 720), (135, 45),
                 (135, 720), (180, 45), (180, 720), (225, 45),
                 (225, 720), (270, 45), (270, 720), (315, 45),
                 (315, 720), (360, 45), (360, 720), (405, 45),
                 (405, 720), (450, 45), (450, 720), (495, 45),
                 (495, 720), (540, 45), (540, 720), (585, 45),
                 (585, 720), (630, 45), (630, 720), (675, 45),
                 (675, 720), (720, 45), (720, 720), (45, 90),
                 (45, 135), (45, 180), (45, 225), (45, 270),
                 (45, 315), (45, 360), (45, 405), (45, 450),
                 (45, 495), (45, 540), (45, 585), (45, 630),
                 (45, 675), (720, 90), (720, 135), (720, 180),
                 (720, 225), (720, 270), (720, 315), (720, 360),
                 (720, 405), (720, 450), (720, 495), (720, 540),
                 (720, 585), (720, 630), (720, 675)]

pawn_spawn_position_list = [(90, 45), (90, 720), (135, 45), (135, 720),
                            (180, 45), (180, 720), (225, 45), (225, 720),
                            (270, 45), (270, 720), (315, 45), (315, 720),
                            (360, 45), (360, 720), (405, 45), (405, 720),
                            (450, 45), (450, 720), (495, 45), (495, 720),
                            (540, 45), (540, 720), (585, 45), (585, 720),
                            (630, 45), (630, 720), (675, 45), (675, 720),
                            (45, 90), (45, 135), (45, 180), (45, 225),
                            (45, 270), (45, 315), (45, 360), (45, 405),
                            (45, 450), (45, 495), (45, 540), (45, 585),
                            (45, 630), (45, 675), (720, 90), (720, 135),
                            (720, 180), (720, 225), (720, 270), (720, 315),
                            (720, 360), (720, 405), (720, 450), (720, 495),
                            (720, 540), (720, 585), (720, 630), (720, 675)]

# Random Variables
font = "GaramondNo8-Regular.ttf"
