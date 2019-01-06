import pygame
import constants
import random

pygame.init()

class Piece(pygame.sprite.Sprite):
    def __init__(self, rect_x, rect_y):
        super().__init__()
        self.image = pygame.Surface((45, 45))
        self.image.fill((0, 0, 255))
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
        self.pos = (self.rect.x, self.rect.y)
        self.type = 'piece'

    def move(self, screen, all_sprites_list):
        key = pygame.key.get_pressed()
        move_spaces = []
        not_selected = True

        pos_1 = (self.rect.x - 90, self.rect.y - 90)
        pos_2 = (self.rect.x - 90, self.rect.y - 45)
        pos_3 = (self.rect.x - 90, self.rect.y)
        pos_4 = (self.rect.x - 90, self.rect.y + 45)
        pos_5 = (self.rect.x - 90, self.rect.y + 90)
        pos_6 = (self.rect.x - 45, self.rect.y + 90)
        pos_7 = (self.rect.x, self.rect.y + 90)
        pos_8 = (self.rect.x + 45, self.rect.y + 90)
        pos_9 = (self.rect.x + 90, self.rect.y + 90)
        pos_10 = (self.rect.x + 90, self.rect.y + 45)
        pos_11 = (self.rect.x + 90, self.rect.y)
        pos_12 = (self.rect.x + 90, self.rect.y - 45)
        pos_13 = (self.rect.x + 90, self.rect.y - 90)
        pos_14 = (self.rect.x + 45, self.rect.y - 90)
        pos_15 = (self.rect.x, self.rect.y - 90)
        pos_16 = (self.rect.x - 45, self.rect.y - 90)

        move_spaces.append(pos_1)
        move_spaces.append(pos_2)
        move_spaces.append(pos_3)
        move_spaces.append(pos_4)
        move_spaces.append(pos_5)
        move_spaces.append(pos_6)
        move_spaces.append(pos_7)
        move_spaces.append(pos_8)
        move_spaces.append(pos_9)
        move_spaces.append(pos_10)
        move_spaces.append(pos_11)
        move_spaces.append(pos_12)
        move_spaces.append(pos_13)
        move_spaces.append(pos_14)
        move_spaces.append(pos_15)
        move_spaces.append(pos_16)

        move_spaces[:] = [tup for tup in move_spaces if not (tup[0] < 45 or tup[0] > 720 or tup[1] < 45 or tup[1] > 720)]
        
        screen.blit(constants.GETIMAGE("chessboard.png"), (0, 0))
        all_sprites_list.draw(screen)
        for tup in move_spaces:
            screen.blit(constants.ALLOWEDMOVE, tup)
        if key[pygame.K_RIGHT]:
            constants.N += 1
        if key[pygame.K_LEFT]:
            constants.N -= 1

        try:
            screen.blit(constants.SELECTEDMOVE, move_spaces[constants.N])
        except IndexError:
            constants.N = 0
            screen.blit(constants.SELECTEDMOVE, move_spaces[constants.N])

        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    screen.blit(constants.GETIMAGE("chessboard.png"), (0, 0))
                    all_sprites_list.draw(screen)
                    pygame.display.flip()

                    self.rect.x = move_spaces[constants.N][0]
                    self.rect.y = move_spaces[constants.N][1]
                    self.pos = move_spaces[constants.N]
                    screen.blit(constants.GETIMAGE("chessboard.png"), (0, 0))
                    all_sprites_list.draw(screen)

                    constants.N = 0
                    constants.C = 2

    def capture(self, enemy_list, enemy_count, screen, all_sprites_list):
        for enemy in enemy_list:
            if enemy.pos == self.pos:
                enemy_count -= 1
                self.type = enemy.type
                all_sprites_list.remove(enemy)
                enemy_list.remove(enemy)
                enemy = None
        screen.blit(constants.GETIMAGE("chessboard.png"), (0, 0))
        all_sprites_list.draw(screen)
        return enemy_count


class Enemy_Pawn(Piece):
    def __init__(self, rect_x, rect_y):
        super().__init__(rect_x, rect_y)
        self.image = constants.GETIMAGE("pieces/pd.png")
        self.type = 'pawn'
        if self.rect.x == 45:
            self.direction = 'left'
        elif self.rect.x == 720:
            self.direction = 'right'
        elif self.rect.y == 45:
            self.direction = 'down'
        elif self.rect.y == 720:
            self.direction = 'up'
    
    def move(self, screen, all_sprites_list):
        screen.blit(constants.GETIMAGE("chessboard.png"), (0, 0))
        all_sprites_list.draw(screen)
        if self.direction == 'left':
            self.rect.x += 45
        elif self.direction == 'right':
            self.rect.x -= 45
        elif self.direction == 'down':
            self.rect.y += 45
        elif self.direction == "up":
            self.rect.y -= 45    
        self.pos = (self.rect.x, self.rect.y)

    def turn(self, screen, all_sprites_list):
        screen.blit(constants.GETIMAGE("chessboard.png"), (0, 0))
        all_sprites_list.draw(screen)
        if self.direction == 'left' and self.rect.x == 720:
            self.direction = 'right'
        elif self.direction == 'right' and self.rect.x == 45:
            self.direction = 'left'
        elif self.direction == 'down' and self.rect.y == 720:
            self.direction = 'up'
        elif self.direction == "up" and self.rect.y == 45:
            self.direction = 'down'

    def capture(self, player, screen, all_sprites_list):
        if self.pos == player.pos:
            all_sprites_list.remove(player)
            player = None
            constants.S = 500
        screen.blit(constants.GETIMAGE("chessboard.png"), (0, 0))
        all_sprites_list.draw(screen)



# class Enemy_Knight(Piece):
#     def __init__(self):
#         super().__init__()
#         self.image = constants.GETIMAGE("pieces/nd.png")
#         self.type = 'knight'


# class Enemy_Bishop(Piece):
#     def __init__(self):
#         super().__init__()
#         self.image = constants.GETIMAGE("pieces/bd.png")
#         self.type = 'bishop'


# class Enemy_Rook(Piece):
#     def __init__(self):
#         super().__init__()
#         self.image = constants.GETIMAGE("pieces/rd.png")
#         self.type = 'rook'


# class Enemy_Queen(Piece):
#     def __init__(self):
#         super().__init__()
#         self.image = constants.GETIMAGE("pieces/qd.png")
#         self.type = 'queen'


# class Enemy_King(Piece):
#     def __init__(self):
#         super().__init__()
#         self.image = constants.GETIMAGE("pieces/kd.png")
#         self.type = 'king'


# class Player(Piece):
#     def __init__(self):
#         super().__init__()
