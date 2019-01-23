import pygame
import os
import sys
import random
import variables
import classes


_image_library = {}


def get_image(path):
    """Grabs image"""
    global _image_library
    image = _image_library.get(path)
    if image is None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image

def text_object(text, font, color):
    """Creates object for text to be created on"""
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()

def render_text(font_size, text, color, x, y):
    """function to render centered text"""
    font = pygame.font.Font(variables.font, font_size)
    text_surface, text_rect = text_object(text, font, color)
    text_rect.center = (x, y)
    variables.screen.blit(text_surface, text_rect)

def sets_phase_to_one():
    """sets variables.phase to 1 (Home Screen)"""
    variables.phase = 1

def sets_phase_to_two():
    """sets variables.phase to 2 (Controls and Directions)"""
    variables.phase = 2

def sets_phase_to_three():
    """sets variables.phase to 3 (Game)"""
    variables.phase = 3

def difficulty_easy():
    """reduces pawn_spawn_position_list to len 20"""
    variables.win_number = 20
    pawn_pos = []
    for i in range(variables.win_number):
        pos = random.choice(variables.pawn_spawn_position_list)
        pawn_pos.append(pos)
    variables.pawn_spawn_position_list = pawn_pos
    variables.phase = 3

def difficulty_medium():
    """reduces pawn_spawn_position_list to len 40"""
    variables.win_number = 40
    pawn_pos = []
    for i in range(variables.win_number):
        pos = random.choice(variables.pawn_spawn_position_list)
        pawn_pos.append(pos)
    variables.pawn_spawn_position_list = pawn_pos
    variables.phase = 3

def difficulty_hard():
    """keeps pawn_spawn_position_list len 56"""
    variables.win_number = 56
    pawn_pos = []
    for i in range(variables.win_number):
        pos = random.choice(variables.pawn_spawn_position_list)
        pawn_pos.append(pos)
    variables.pawn_spawn_position_list = pawn_pos
    variables.phase = 3

def header_text():
    """renders text at top of board during game"""
    header_font = pygame.font.Font(variables.font, 30)

    turn = "Turn #"
    turn += str(variables.turn)

    pawns_killed = "Pawns killed: "
    pawns_killed += str(variables.pawns_killed)

    lives_left = "Lives: "
    lives_left += "*" * variables.lives

    text_surface, text_rect = text_object(turn, header_font, variables.BLACK)
    text_rect.center = (135, 45/2)
    variables.screen.blit(text_surface, text_rect)

    text_surface, text_rect = text_object(pawns_killed,
                                          header_font, variables.BLACK)
    text_rect.center = (315, 45/2)
    variables.screen.blit(text_surface, text_rect)

    text_surface, text_rect = text_object(lives_left,
                                          header_font, variables.BLACK)
    text_rect.center = (585, 45/2)
    variables.screen.blit(text_surface, text_rect)

def spawn_player():
    """spawns in player at beginning of game or after killed"""
    pos = random.choice(variables.player_spawn_locations)
    player = classes.Player(pos[0], pos[1])
    player.update_sprite()
    variables.all_sprites_list.add(player)
    return player

def spawn_pawns(num):
    """spawns in num amount of pawns from pawn_spawn_position_list"""
    for i in range(num):
        try:
            spawn_position = random.choice(variables.pawn_spawn_position_list)
            rect_x = spawn_position[0]
            rect_y = spawn_position[1]

            variables.pawn_spawn_position_list.remove(spawn_position)

            pawn = classes.EnemyPawn(rect_x, rect_y)

            variables.pawn_list.add(pawn)
            variables.all_sprites_list.add(pawn)

            variables.pawns_spawned += 1

        except IndexError:
            pass

def reset_game():
    """resets game and all variables after you play"""
    for piece in variables.all_sprites_list:
        del piece

    variables.array_index = 0
    variables.queue = -1
    variables.phase = 1
    variables.turn = 1
    variables.capture_turns = 0
    variables.lives = 3

    variables.pawns_count = 0
    # variables.knights_count = 0
    # variables.bishops_count = 0
    # variables.rooks_count = 0
    # variables.queens_count = 0
    # variables.kings_count = 0

    variables. pawns_spawned = 0
    # variables.knights_spawned = 0
    # variables.bishops_spawned = 0
    # variables.rooks_spawned = 0
    # variables.queens_spawned = 0
    # variables.kings_spawned = 0

    variables.pawns_killed = 0
    # variables.knights_killed = 0
    # variables.bishops_killed = 0
    # variables.rooks_killed = 0
    # variables.queens_killed = 0
    # variables.kings_killed = 0

    variables.all_sprites_list = pygame.sprite.Group()
    variables.pawn_list = pygame.sprite.Group()
    # variables.knight_list = pygame.sprite.Group()
    # variables.bishop_list = pygame.sprite.Group()
    # variables.rook_list = pygame.sprite.Group()
    # variables.queen_list = pygame.sprite.Group()
    # variables.king_list = pygame.sprite.Group()

    variables.done = False
    variables.can_spawn_pawns = True
    # variables.can_spawn_knights = True
    # variables.can_spawn_bishops = True
    # variables.can_spawn_rooks = True
    # variables.can_spawn_queens = True
    # variables.can_spawn_kings = True

    variables.piece_types = ['pawn', 'knight', 'bishop',
                             'rook', 'queen', 'king']

    variables.x_position_list = [45, 90, 135, 180, 225, 270, 315,
                                 360, 405, 450, 495, 540, 585, 630, 675, 720]

    variables.y_position_list = [45, 90, 135, 180, 225, 270, 315,
                                 360, 405, 450, 495, 540, 585, 630, 675, 720]

    variables.position_list = [(45, 45), (45, 720), (90, 45), (90, 720), (135, 45),
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

    variables.pawn_spawn_position_list = [(90, 45), (90, 720), (135, 45), (135, 720),
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
