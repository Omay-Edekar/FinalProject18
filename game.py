import pygame
import pieces
import constants

pygame.init()
screen = pygame.display.set_mode((810, 810))
pygame.display.set_caption("Copycat Chess")
all_sprites_list = pygame.sprite.Group()

done = False
finished = False

piece = pieces.Piece(405, 405)
all_sprites_list.add(piece)

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and constants.C == 0:
                constants.C = 1

    screen.blit(constants.GETIMAGE("chessboard.png"), (0, 0))

    all_sprites_list.update(screen)
    all_sprites_list.draw(screen)

    if constants.C == 1:
        piece.move(screen, all_sprites_list)

    if constants.C == 2:
        #enemy movements
        #set C to 3
        pass
    
    if constants.C == 3:
        constants.C = 0

    constants.I += 1
    print(f"I: {constants.I}")
    print(f"C: {constants.C}")

    pygame.display.flip()
    constants.CLOCK.tick(10)
