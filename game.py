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

    screen.blit(constants.get_image("chessboard.png"), (0, 0))

    all_sprites_list.update(screen)
    all_sprites_list.draw(screen)

    piece.move(screen)
    constants.i += 1
    print(constants.i)

    pygame.display.flip()
    constants.clock.tick(60)
