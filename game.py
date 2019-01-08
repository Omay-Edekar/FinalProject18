import pygame
import pieces
import constants
import random

# initialize pygame variables
pygame.init()
screen = pygame.display.set_mode((810, 810))
pygame.display.set_caption("Copycat Chess")
pawn_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
pawns_killed = 0
turn = 1

# counting variables
pawn_count = 0
knight_count = 0
bishop_count = 0
rook_count = 0
queen_count = 0
king_count = 0

pawn_spawned = 0
knight_spawned = 0
bishop_spawned = 0
rook_spawned = 0
queen_spawned = 0
king_spawned = 0

# initialize buttons
start_button = constants.Button(225, 495, 360, 90, "Controls", constants.BLACK, constants.LIGHTBLACK, constants.WHITE)
play_button = constants.Button(225, 585, 360, 90, "Start Game", constants.BLACK, constants.LIGHTBLACK, constants.WHITE)
play_again_button = constants.Button(225, 585, 360, 90, "Go To Menu", constants.BLACK, constants.LIGHTBLACK, constants.WHITE)


# initialize pieces and players
player = pieces.Player(405, 405)
all_sprites_list.add(player)


def turn_text(turn, pawns_killed, screen):
    turn_font = pygame.font.Font("GaramondNo8-Regular.ttf", 15)
    turn_number = "Turn #"
    turn_number += str(turn)
    pawns_kill = "Pawns killed: "
    pawns_kill += str(pawns_killed)
    text_surface, text_rect = constants.TEXTOBJECT(turn_number, paragraph_font, constants.BLACK)
    text_rect.center = (405/3, 45/2)
    screen.blit(text_surface, text_rect)
    text_surface, text_rect = constants.TEXTOBJECT(pawns_kill, paragraph_font, constants.BLACK)
    text_rect.center = (910/3, 45/2)
    screen.blit(text_surface, text_rect)


def spawn(num):
    for i in range(num):
        # Set a random location for the block
        try:
            pos = random.choice(constants.PAWNPOSLIST)
            rect_x = pos[0]
            rect_y = pos[1]

            # removes possible position
            constants.PAWNPOSLIST.remove(pos)

            # This represents a pawn
            pawn = pieces.Enemy_Pawn(rect_x, rect_y)

            # Add the block to the list of objects
            pawn_list.add(pawn)
            all_sprites_list.add(pawn)

        except IndexError:
            pass
        

# game play
while not constants.DONE:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            constants.DONE = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and constants.S == 2 and constants.C == 0:
                constants.C = 1
    if pawns_killed >= 60 and constants.S == 2:
        constants.S = 'END'

    if constants.S == 0:
        screen.fill(constants.WHITE)
        title_font = pygame.font.Font('GaramondNo8-Regular.ttf', 90)
        text_surface, text_rect = constants.TEXTOBJECT("Copycat Chess", title_font, constants.BLACK)
        text_rect.center = (405, 300)
        screen.blit(text_surface, text_rect)

        start_button.click(screen, constants.SETSTO1)

    if constants.S == 1:
        screen.fill(constants.WHITE)
        title_font = pygame.font.Font('GaramondNo8-Regular.ttf', 90)
        text_surface, text_rect = constants.TEXTOBJECT("Controls", title_font, constants.BLACK)
        text_rect.center = (405, 270)
        screen.blit(text_surface, text_rect)

        paragraph_font = pygame.font.Font('GaramondNo8-Regular.ttf', 30)
        text_surface, text_rect = constants.TEXTOBJECT("Press Space to start each turn", paragraph_font, constants.BLACK)
        text_rect.center = (405, 360)
        screen.blit(text_surface, text_rect)

        text_surface, text_rect = constants.TEXTOBJECT("Use Left and Right Arrow Keys to select your move", paragraph_font, constants.BLACK)
        text_rect.center = (405, 405)
        screen.blit(text_surface, text_rect)

        text_surface, text_rect = constants.TEXTOBJECT("Press Enter to confirm your move", paragraph_font, constants.BLACK)
        text_rect.center = (405, 450)
        screen.blit(text_surface, text_rect)

        text_surface, text_rect = constants.TEXTOBJECT("You may have to press Enter multiple times", paragraph_font, constants.BLACK)
        text_rect.center = (405, 495)
        screen.blit(text_surface, text_rect)

        text_surface, text_rect = constants.TEXTOBJECT("Objective: Capture 60 pawns", paragraph_font, constants.BLACK)
        text_rect.center = (405, 540)
        screen.blit(text_surface, text_rect)

        play_button.click(screen, constants.SETSTO2)

    if constants.S == 2:

        screen.blit(constants.GETIMAGE("chessboard.png"), (0, 0))

        all_sprites_list.update(screen)
        all_sprites_list.draw(screen)

        turn_text(turn, pawns_killed, screen)

        if constants.C == -1:
            spawn(16)
            player.update_sprite()
            for pawn in pawn_list:
                pawn.update_sprite()
            constants.C = 0

        if constants.C == 1:
            if turn % 4 == 0:
                spawn(4)
                for pawn in pawn_list:
                    pawn.update_sprite()
            constants.C = 2

        if constants.C == 2:
            player.move(screen, all_sprites_list)
            player.update_sprite()
            turn_text(turn, pawns_killed, screen)

        if constants.C == 3:
            pawns_killed = player.capture(pawn_list, pawns_killed, screen, all_sprites_list)
            player.update_sprite()
            turn_text(turn, pawns_killed, screen)
            constants.C = 4

        if constants.C == 4:
            for i in range(50):
                screen.blit(constants.GETIMAGE("chessboard.png"), (0, 0))
                all_sprites_list.draw(screen)
                turn_text(turn, pawns_killed, screen)
                pygame.display.flip()
                pygame.time.wait(1)

            constants.C = 5

        if constants.C == 5:
            for pawn in pawn_list:
                pawn.move(screen, all_sprites_list)
                pawn.turn(screen, all_sprites_list)
                all_sprites_list.draw(screen)
                turn_text(turn, pawns_killed, screen)
                pawn.update_sprite()
                pygame.display.flip()
                pygame.time.wait(50)
            constants.C = 6

        if constants.C == 6:
            for i in range(50):
                screen.blit(constants.GETIMAGE("chessboard.png"), (0, 0))
                all_sprites_list.draw(screen)
                turn_text(turn, pawns_killed, screen)
                pygame.display.flip()
                pygame.time.wait(1)

            constants.C = 7

        if constants.C == 7:
            for pawn in pawn_list:
                pawn.capture(player, screen, all_sprites_list)
                all_sprites_list.draw(screen)
                turn_text(turn, pawns_killed, screen)
                pygame.display.flip()

            constants.T += 1
            constants.C = 0

    if constants.S == 'END':
        if pawns_killed < 60:
            screen.fill(constants.WHITE)
            title_font = pygame.font.Font("GaramondNo8-Regular.ttf", 90)
            text_surface, text_rect = constants.TEXTOBJECT("You Lose", title_font, constants.BLACK)
            text_rect.center = (405, 360)
            screen.blit(text_surface, text_rect)
            text_surface1, text_rect1 = constants.TEXTOBJECT(":(", title_font, constants.BLACK)
            text_rect1.center = (405, 450)
            screen.blit(text_surface1, text_rect1)

            play_again_button.click(screen, constants.SETSTO0)

        else:
            screen.fill(constants.WHITE)
            title_font = pygame.font.Font("GaramondNo8-Regular.ttf", 90)
            text_surface, text_rect = constants.TEXTOBJECT("You Win!", title_font, constants.BLACK)
            text_rect.center = (405, 383)
            screen.blit(text_surface, text_rect)

            play_again_button.click(screen, constants.SETSTO0)

    pygame.display.flip()
    constants.CLOCK.tick(15)
