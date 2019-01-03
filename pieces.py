import pygame
import constants
import random

pygame.init()

allowed_move = pygame.Surface((45, 45))
allowed_move.set_alpha(128)
allowed_move.fill((79, 121, 66))

selected_move = pygame.Surface((45, 45))
selected_move.set_alpha(192)
selected_move.fill((255, 0, 0))


class Piece(pygame.sprite.Sprite):
    def __init__(self, rect_x, rect_y):
        super().__init__()
        self.image = pygame.Surface((45, 45))
        self.image.fill((128, 128, 128))
        self.rect = self.image.get_rect()
        self.rect.x = rect_x
        self.rect.y = rect_y
        self.pos = (self.rect.x, self.rect.y)
        self.type = 'piece'

    def move(self, screen):
        key = pygame.key.get_pressed()
        move_spaces = []
        done = False

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

        screen.blit(constants.get_image("chessboard.png"), (0, 0))
        for tup in move_spaces:
            screen.blit(allowed_move, tup)
        screen.blit(selected_move, move_spaces[constants.n])
        if key[pygame.K_RIGHT]:
            print("right")
            constants.n += 1
        if key[pygame.K_LEFT]:
            print("left")
            constants.n -= 1
        print(constants.n)
        if constants.n >= 16:
            constants.n = 0
        if constants.n <= -16:
            constants.n = 0
        screen.blit(selected_move, move_spaces[constants.n])
            
    
# class Enemy_Pawn(Piece):
#     def __init__(self):
#         super().__init__()
#         self.image = constants.get_image("pieces/pd.png")
#         self.type = 'pawn'
#         if self.rect.x == 45:
#             self.direction = 'left'
#         elif self.rect.x == 720:
#             self.direction = 'right'
#         elif self.rect.y == 45:
#             self.direction = 'down'
#         elif self.rect.y == 720:
#             self.direction = 'up'


# class Enemy_Knight(Piece):
#     def __init__(self):
#         super().__init__()
#         self.image = constants.get_image("pieces/nd.png")
#         self.type = 'knight'


# class Enemy_Bishop(Piece):
#     def __init__(self):
#         super().__init__()
#         self.image = constants.get_image("pieces/bd.png")
#         self.type = 'bishop'


# class Enemy_Rook(Piece):
#     def __init__(self):
#         super().__init__()
#         self.image = constants.get_image("pieces/rd.png")
#         self.type = 'rook'


# class Enemy_Queen(Piece):
#     def __init__(self):
#         super().__init__()
#         self.image = constants.get_image("pieces/qd.png")
#         self.type = 'queen'


# class Enemy_King(Piece):
#     def __init__(self):
#         super().__init__()
#         self.image = constants.get_image("pieces/kd.png")
#         self.type = 'king'


# class Player(Piece):
#     def __init__(self):
#         super().__init__()
