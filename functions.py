import pygame
import os
import sys
import random
import variables
import classes

_image_library = {}


def get_image(path):
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
    font = pygame.font.Font(variables.font, font_size)
    text_surface, text_rect = text_object(text, font, color)
    text_rect.center = (x, y)
    variables.screen.blit(text_surface, text_rect)


def sets_phase_to_one():
    variables.phase = 1


def sets_phase_to_two():
    variables.phase = 2


def sets_phase_to_three():
    variables.phase = 3


def header_text():
    header_font = pygame.font.Font(variables.font, 30)

    turn = "Turn #"
    turn += str(variables.turn)

    pawns_killed = "Pawns killed: "
    pawns_killed += str(variables.pawns_killed)

    text_surface, text_rect = text_object(turn, header_font, variables.BLACK)
    text_rect.center = (405/3, 45/2)
    variables.screen.blit(text_surface, text_rect)

    text_surface, text_rect = text_object(pawns_killed,
                                          header_font, variables.BLACK)
    text_rect.center = (910/3, 45/2)
    variables.screen.blit(text_surface, text_rect)


def spawn_pawns(num):
    for i in range(num):
        try:
            spawn_position = random.choice(variables.pawn_spawn_position_list)
            rect_x = spawn_position[0]
            rect_y = spawn_position[1]

            variables.pawn_spawn_position_list.remove(spawn_position)

            pawn = classes.EnemyPawn(rect_x, rect_y)

            variables.pawn_list.add(pawn)
            variables.all_sprites_list.add(pawn)

        except IndexError:
            pass

def reset_game(player):

    for pawn in variables.pawn_list:
        del pawn

    del player

    array_index = 0
    queue = -1
    phase = 1
    turn = 1
    
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

    all_sprites_list = pygame.sprite.Group()
    pawn_list = pygame.sprite.Group()
    # knight_list = pygame.sprite.Group()
    # bishop_list = pygame.sprite.Group()
    # rook_list = pygame.sprite.Group()
    # queen_list = pygame.sprite.Group()
    # king_list = pygame.sprite.Group()

    done = False
    can_spawn_pawns = True
    # can_spawn_knights = True
    # can_spawn_bishops = True
    # can_spawn_rooks = True
    # can_spawn_queens = True
    # can_spawn_kings = True

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

    pawn_spawn_position_list = [(45, 45), (45, 720), (90, 45), (90, 720),
                                (135, 45), (135, 720), (180, 45), (180, 720),
                                (225, 45), (225, 720), (270, 45), (270, 720),
                                (315, 45), (315, 720), (360, 45), (360, 720),
                                (405, 45), (405, 720), (450, 45), (450, 720),
                                (495, 45), (495, 720), (540, 45), (540, 720),
                                (585, 45), (585, 720), (630, 45), (630, 720),
                                (675, 45), (675, 720), (720, 45), (720, 720),
                                (45, 90), (45, 135), (45, 180), (45, 225),
                                (45, 270), (45, 315), (45, 360), (45, 405),
                                (45, 450), (45, 495), (45, 540), (45, 585),
                                (45, 630), (45, 675), (720, 90), (720, 135),
                                (720, 180), (720, 225), (720, 270), (720, 315),
                                (720, 360), (720, 405), (720, 450), (720, 495),
                                (720, 540), (720, 585), (720, 630), (720, 675)]
