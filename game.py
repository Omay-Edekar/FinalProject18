import pygame
import pieces
import constants
import random

# initialize variables and game
pygame.init()
screen = pygame.display.set_mode((810, 810))
pygame.display.set_caption("Copycat Chess")
pawn_list = pygame.sprite.Group()
all_sprites_list = pygame.sprite.Group()
pawn_count = 0
turn = 1

start_button = constants.Button(225, 495, 360, 90, "Controls", constants.BLACK, constants.LIGHTBLACK, constants.WHITE)
play_button = constants.Button(225, 595, 360, 90, "Start Game", constants.BLACK, constants.LIGHTBLACK, constants.WHITE)

# initialize pieces and players
piece = pieces.Piece(405, 405)
all_sprites_list.add(piece)


def turn_text(turn, pawn_count, screen):
    turn_font = pygame.font.Font('GaramondNo8-Regular.ttf', 15)
    turn_number = "Turn #"
    turn_number += str(turn)
    pawns_left = "Pawns left: "
    pawns_left += str(pawn_count)
    text_surface, text_rect = constants.TEXTOBJECT(turn_number, paragraph_font, constants.BLACK)
    text_rect.center = (405/3, 45/2)
    screen.blit(text_surface, text_rect)
    text_surface, text_rect = constants.TEXTOBJECT(pawns_left, paragraph_font, constants.BLACK)
    text_rect.center = (910/3, 45/2)
    screen.blit(text_surface, text_rect)


def pawn_spawn(num):
    global pawn_count
    for i in range(num):
        # Set a random location for the block
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

        pawn_count += 1


# game play
while not constants.DONE:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            constants.DONE = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and constants.S == 2 and constants.C == 0:
                constants.C = 1
    if pawn_count == 0 and constants.S == 2:
        constants.S = 500

    if constants.S == 0:
        screen.fill(constants.WHITE)
        title_font = pygame.font.Font('GaramondNo8-Regular.ttf', 90)
        text_surface, text_rect = constants.TEXTOBJECT("Copycat Chess", title_font, constants.BLACK)
        text_rect.center = (405, 300)
        screen.blit(text_surface, text_rect)

        start_button.click(screen, constants.INCREASESTO1)

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

        text_surface, text_rect = constants.TEXTOBJECT("Use Arrow Keys to select your move", paragraph_font, constants.BLACK)
        text_rect.center = (405, 405)
        screen.blit(text_surface, text_rect)

        text_surface, text_rect = constants.TEXTOBJECT("Press Enter to confirm your move", paragraph_font, constants.BLACK)
        text_rect.center = (405, 450)
        screen.blit(text_surface, text_rect)

        text_surface, text_rect = constants.TEXTOBJECT("You may have to press Enter multiple times", paragraph_font, constants.BLACK)
        text_rect.center = (405, 495)
        screen.blit(text_surface, text_rect)

        text_surface, text_rect = constants.TEXTOBJECT("Objective: Capture all pawns", paragraph_font, constants.BLACK)
        text_rect.center = (405, 540)
        screen.blit(text_surface, text_rect)

        play_button.click(screen, constants.INCREASESTO2)

    if constants.S == 2:

        screen.blit(constants.GETIMAGE("chessboard.png"), (0, 0))

        all_sprites_list.update(screen)
        all_sprites_list.draw(screen)

        turn_text(turn, pawn_count, screen)

        if constants.C == -1:
            pawn_spawn(16)
            piece.update_sprite()
            constants.C = 0

        if constants.C == 1:
            piece.move(screen, all_sprites_list)
            piece.update_sprite()
            turn_text(turn, pawn_count, screen)

        if constants.C == 2:
            pawn_count = piece.capture(pawn_list, pawn_count, screen, all_sprites_list)
            piece.update_sprite()
            turn_text(turn, pawn_count, screen)
            constants.C = 3

        if constants.C == 3:
            for i in range(50):
                screen.blit(constants.GETIMAGE("chessboard.png"), (0, 0))
                all_sprites_list.draw(screen)
                turn_text(turn, pawn_count, screen)
                pygame.display.flip()
                pygame.time.wait(1)

            constants.C = 4

        if constants.C == 4:
            for pawn in pawn_list:
                pawn.move(screen, all_sprites_list)
                pawn.turn(screen, all_sprites_list)
                all_sprites_list.draw(screen)
                turn_text(turn, pawn_count, screen)
                pygame.display.flip()
                pygame.time.wait(25)
            constants.C = 5

        if constants.C == 5:
            for i in range(50):
                screen.blit(constants.GETIMAGE("chessboard.png"), (0, 0))
                all_sprites_list.draw(screen)
                turn_text(turn, pawn_count, screen)
                pygame.display.flip()
                pygame.time.wait(1)

            constants.C = 6

        if constants.C == 6:
            for pawn in pawn_list:
                pawn.capture(piece, screen, all_sprites_list)
                all_sprites_list.draw(screen)
                turn_text(turn, pawn_count, screen)
                pygame.display.flip()

            turn += 1
            constants.C = 0

    if constants.S == 500:
        if pawn_count > 0:
            screen.fill(constants.WHITE)
            title_font = pygame.font.Font('GaramondNo8-Regular.ttf', 90)
            text_surface, text_rect = constants.TEXTOBJECT("You Lose", title_font, constants.BLACK)
            text_rect.center = (405, 360)
            screen.blit(text_surface, text_rect)
            text_surface1, text_rect1 = constants.TEXTOBJECT(":(", title_font, constants.BLACK)
            text_rect1.center = (405, 450)
            screen.blit(text_surface1, text_rect1)
        else:
            screen.fill(constants.WHITE)
            title_font = pygame.font.Font('GaramondNo8-Regular.ttf', 90)
            text_surface, text_rect = constants.TEXTOBJECT("You Win!", title_font, constants.BLACK)
            text_rect.center = (405, 383)
            screen.blit(text_surface, text_rect)

    pygame.display.flip()
    constants.CLOCK.tick(15)
