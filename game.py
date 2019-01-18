import pygame
import variables
import functions
import classes

pygame.init()

pygame.display.set_caption("Attack of the Pawns")

start_button = classes.Button(225, 495, 360, 90, "Controls and Directions", 'small', variables.BLACK, variables.LIGHTBLACK, variables.WHITE)
easy_button = classes.Button(90, 675, 180, 90, "Easy", 'regular', variables.BLACK, variables.LIGHTBLACK, variables.WHITE)
medium_button = classes.Button(315, 675, 180, 90, "Medium", 'regular', variables.BLACK, variables.LIGHTBLACK, variables.WHITE)
hard_button = classes.Button(540, 675, 180, 90, "Hard", 'regular', variables.BLACK, variables.LIGHTBLACK, variables.WHITE)
reset_button = classes.Button(315, 675, 180, 90, "Reset", 'regular', variables.BLACK, variables.LIGHTBLACK, variables.WHITE)
play_again_button = classes.Button(225, 585, 360, 90, "Go To Menu", 'regular', variables.BLACK, variables.LIGHTBLACK, variables.WHITE)

while not variables.done:

    key = pygame.key.get_pressed()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            variables.done = True

    if variables.phase == 1:
        variables.screen.fill(variables.WHITE)
        functions.render_text(80, "Attack of the Pawns", variables.BLACK, 405, 300)

        start_button.click(functions.sets_phase_to_two)
        # reset_button.click(functions.reset_game)

    if variables.phase == 2:
        variables.screen.fill(variables.WHITE)

        functions.render_text(60, "Controls", variables.BLACK, 405, 45)
        functions.render_text(30, "Press Space to start each turn", variables.BLACK, 405, 135)
        functions.render_text(30, "Use the Left and Right Arrow Keys to select your move", variables.BLACK, 405, 180)
        functions.render_text(30, "Press Enter to confirm your move", variables.BLACK, 405, 225)

        functions.render_text(60, "Directions", variables.BLACK, 405, 315)
        functions.render_text(30, "Kill all pawns to win", variables.BLACK, 405, 405)
        functions.render_text(30, "Easy: 20 pawns   Medium: 40 pawns    Hard: 56 pawns", variables.BLACK, 405, 450)
        functions.render_text(30, "If you get captured, you'll lose a life", variables.BLACK, 405, 495)
        functions.render_text(30, "If you don't capture a pawn in 16 turns,", variables.BLACK, 405, 540)
        functions.render_text(30, "you'll lose a life and change type", variables.BLACK, 405, 585)
        functions.render_text(30, "IMPORTANT: Pawns only capture in front", variables.BLACK, 405, 630)

        easy_button.click(functions.difficulty_easy)
        medium_button.click(functions.difficulty_medium)
        hard_button.click(functions.difficulty_hard)

        # reset_button.click(functions.reset_game)

    if variables.phase == 3:

        variables.screen.blit(functions.get_image("chessboard.png"), (0, 0))
        variables.all_sprites_list.draw(variables.screen)
        functions.header_text()

        if variables.pawns_killed >= variables.win_number:
            variables.phase = 'END'
            variables.queue = 'SKIP'

        if variables.lives <= 0:
            variables.phase = 'END'
            variables.queue = 'SKIP'
            variables.all_sprites_list.remove(player)

        if key[pygame.K_SPACE] and variables.queue == 0:
            variables.queue = 1

        if variables.queue == -1:
            player = functions.spawn_player()
            functions.spawn_pawns(16)
            player.update_sprite()
            for pawn in variables.pawn_list:
                pawn.update_sprite()
            variables.queue = 0

        if variables.queue == 1:
            if variables.turn % 1 == 0:
                functions.spawn_pawns(1)
                for pawn in variables.pawn_list:
                    pawn.update_sprite()
            variables.queue = 2

        if variables.queue == 2:
            player.move()
            player.update_sprite()
            functions.header_text()

        if variables.queue == 3:
            player.capture()
            player.update_sprite()
            functions.header_text()
            variables.queue = 4

        if variables.queue == 4:
            for pawn in variables.pawn_list:
                pawn.move()
                pawn.turn()
                pawn.update_sprite()
                variables.all_sprites_list.draw(variables.screen)
                functions.header_text()
                pygame.display.flip()
                # pygame.time.wait(50)
            variables.queue = 5

        if variables.queue == 5:
            for pawn in variables.pawn_list:
                pawn.capture(player)
                variables.all_sprites_list.draw(variables.screen)
                functions.header_text()
                pygame.display.flip()
            player.get_new_type()
            variables.all_sprites_list.add(player)
            variables.all_sprites_list.draw(variables.screen)

            variables.turn += 1
            variables.queue = 0

    if variables.phase == 'END':
        if variables.pawns_killed < variables.win_number:
            variables.screen.fill(variables.WHITE)
            functions.render_text(90, "You Lose", variables.BLACK, 405, 360)
            functions.render_text(90, ":(", variables.BLACK, 405, 450)
            play_again_button.click(functions.reset_game)
        else:
            variables.screen.fill(variables.WHITE)
            functions.render_text(90, "You Win!", variables.BLACK, 405, 270)

            you_won_in_turns = "You won in "
            you_won_in_turns += str(variables.turn)
            you_won_in_turns += " turns!"
            functions.render_text(30, you_won_in_turns, variables.BLACK, 405, 360)

            you_won_with_lives = "You won with "
            you_won_with_lives += str(variables.lives)
            you_won_with_lives += " lives left!"
            functions.render_text(30, you_won_with_lives, variables.BLACK, 405, 405)

            play_again_button.click(functions.reset_game)

    pygame.display.flip()
    variables.clock.tick(10)
