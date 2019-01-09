import pygame
import variables
import functions
import classes

pygame.init()

pygame.display.set_caption("Attack of the Pawns")

start_button = classes.Button(225, 495, 360, 90, "Controls", variables.BLACK, variables.LIGHTBLACK, variables.WHITE)
play_button = classes.Button(225, 585, 360, 90, "Start Game", variables.BLACK, variables.LIGHTBLACK, variables.WHITE)
play_again_button = classes.Button(225, 585, 360, 90, "Go To Menu", variables.BLACK, variables.LIGHTBLACK, variables.WHITE)

player = classes.Player(405, 405)
variables.all_sprites_list.add(player)

while not variables.done:

    key = pygame.key.get_pressed()

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            variables.done = True

        if key[pygame.K_SPACE] and variables.phase == 3 and variables.queue == 0:
            variables.queue = 1

    if variables.pawns_killed >= 60 and variables.phase == 2:
        variables.phase = 'END'

    if variables.phase == 1:
        variables.screen.fill(variables.WHITE)
        functions.render_text(80, "Attack of the Pawns", variables.BLACK, 405, 300)

        start_button.click(functions.sets_phase_to_two)

    if variables.phase == 2:
        variables.screen.fill(variables.WHITE)

        functions.render_text(90, "Controls", variables.BLACK, 405, 225)
        functions.render_text(30, "Press Space to start each turn", variables.BLACK, 405, 360)
        functions.render_text(30, "Use the Left and Right Arrow Keys to select your move", variables.BLACK, 405, 405)
        functions.render_text(30, "Press Enter to confirm your move", variables.BLACK, 405, 450)
        functions.render_text(30, "Objective: Capture 60 pawns", variables.BLACK, 405, 595)

        play_button.click(functions.sets_phase_to_three)

    if variables.phase == 3:

        variables.screen.blit(functions.get_image("chessboard.png"), (0, 0))
        variables.all_sprites_list.draw(variables.screen)
        functions.header_text()

        if variables.queue == -1:
            functions.spawn_pawns(16)
            player.update_sprite()
            for pawn in variables.pawn_list:
                pawn.update_sprite()
            variables.queue = 0
        
        if variables.queue == 1:
            if variables.turn % 4 == 0:
                functions.spawn_pawns(4)
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
                pygame.time.wait(50)
            variables.queue = 5
        
        if variables.queue == 5:
            for pawn in variables.pawn_list:
                pawn.capture(player)
                variables.all_sprites_list.draw(variables.screen)
                functions.header_text()
                pygame.display.flip()

            variables.turn += 1
            variables.queue = 0

    if variables.phase == 'END':
        if variables.pawns_killed < 60:
            variables.screen.fill(variables.WHITE)
            functions.render_text(90, "You Lose", variables.BLACK, 405, 360)
            functions.render_text(90, ":(", variables.BLACK, 405, 450)
            play_again_button.click(functions.reset_game(player))
        else:
            variables.screen.fill(variables.WHITE)
            functions.render_text(90, "You Win!", variables.BLACK, 405, 360)
            play_again_button.click(functions.reset_game(player))
            
    pygame.display.flip()
    variables.clock.tick(15)
