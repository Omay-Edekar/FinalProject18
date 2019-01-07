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
        self.type = random.choice(constants.PIECETYPES)
        self.direction = None

    def move(self, screen, all_sprites_list):
        key = pygame.key.get_pressed()
        move_spaces = []

        if self.type == 'test':
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

        if self.type == 'pawn':
            pos_1 = (self.rect.x, self.rect.y - 45)
            pos_2 = (self.rect.x + 45, self.rect.y)
            pos_3 = (self.rect.x, self.rect.y + 45)
            pos_4 = (self.rect.x - 45, self.rect.y) 
            pos_6 = None

            if self.direction == 'up':
                pos_5 = (self.rect.x, self.rect.y - 90)
            if self.direction == 'down':
                pos_5 = (self.rect.x, self.rect.y + 90)
            if self.direction == 'left':
                pos_5 = (self.rect.x - 90, self.rect.y)
            if self.direction == 'right':
                pos_5 = (self.rect.x + 90, self.rect.y)

            if self.rect.x == 45 and self.direction != 'right':
                pos_6 = (self.rect.x + 90, self.rect.y)
            if self.rect.x == 720 and self.direction != 'left':
                pos_6 = (self.rect.x - 90, self.rect.y)
            if self.rect.y == 45 and self.direction != 'down':
                if pos_6 is None:
                    pos_6 = (self.rect.x, self.rect.y + 90)
                else:
                    pos_7 = (self.rect.x, self.rect.y + 90)
            if self.rect.y == 720 and self.direction != 'up':
                if pos_6 is None:
                    pos_6 = (self.rect.x, self.rect.y - 90)
                else:
                    pos_7 = (self.rect.x, self.rect.y - 90)
            if pos_6 is None:
                del pos_6
            
            move_spaces.append(pos_1)
            move_spaces.append(pos_2)
            move_spaces.append(pos_3)
            move_spaces.append(pos_4)
            try:
                move_spaces.append(pos_5)
            except UnboundLocalError:
                pass
            try:
                move_spaces.append(pos_6)
            except UnboundLocalError:
                pass                
            try:
                move_spaces.append(pos_7)
            except UnboundLocalError:
                pass                

        if self.type == 'knight':
            pos_1 = (self.rect.x - 45, self.rect.y - 90)
            pos_2 = (self.rect.x + 45, self.rect.y - 90)
            pos_3 = (self.rect.x + 90, self.rect.y - 45)
            pos_4 = (self.rect.x + 90, self.rect.y + 45)
            pos_5 = (self.rect.x + 45, self.rect.y + 90)
            pos_6 = (self.rect.x - 45, self.rect.y + 90)
            pos_7 = (self.rect.x - 90, self.rect.y + 45)
            pos_8 = (self.rect.x - 90, self.rect.y - 45)

            move_spaces.append(pos_1)
            move_spaces.append(pos_2)
            move_spaces.append(pos_3)
            move_spaces.append(pos_4)
            move_spaces.append(pos_5)
            move_spaces.append(pos_6)
            move_spaces.append(pos_7)
            move_spaces.append(pos_8)

        if self.type == 'bishop':
            #++
            pos_1 = (self.rect.x + 45, self.rect.y + 45)
            pos_2 = (self.rect.x + 90, self.rect.y + 90)
            pos_3 = (self.rect.x + 135, self.rect.y + 135)
            pos_4 = (self.rect.x + 180, self.rect.y + 180)
            pos_5 = (self.rect.x + 225, self.rect.y + 225)
            pos_6 = (self.rect.x + 270, self.rect.y + 270)
            pos_7 = (self.rect.x + 315, self.rect.y + 315)
            pos_8 = (self.rect.x + 360, self.rect.y + 360)
            pos_9 = (self.rect.x + 405, self.rect.y + 405)
            pos_10 = (self.rect.x + 450, self.rect.y + 450)
            pos_11 = (self.rect.x + 495, self.rect.y + 495)
            pos_12 = (self.rect.x + 540, self.rect.y + 540)
            pos_13 = (self.rect.x + 585, self.rect.y + 585)
            pos_14 = (self.rect.x + 630, self.rect.y + 630)
            pos_15 = (self.rect.x + 675, self.rect.y + 675)
            #--
            pos_16 = (self.rect.x - 45, self.rect.y - 45)
            pos_17 = (self.rect.x - 90, self.rect.y - 90)
            pos_18 = (self.rect.x - 135, self.rect.y - 135)
            pos_19 = (self.rect.x - 180, self.rect.y - 180)
            pos_20 = (self.rect.x - 225, self.rect.y - 225)
            pos_21 = (self.rect.x - 270, self.rect.y - 270)
            pos_22 = (self.rect.x - 315, self.rect.y - 315)
            pos_23 = (self.rect.x - 360, self.rect.y - 360)
            pos_24 = (self.rect.x - 405, self.rect.y - 405)
            pos_25 = (self.rect.x - 450, self.rect.y - 450)
            pos_26 = (self.rect.x - 495, self.rect.y - 495)
            pos_27 = (self.rect.x - 540, self.rect.y - 540)
            pos_28 = (self.rect.x - 585, self.rect.y - 585)
            pos_29 = (self.rect.x - 630, self.rect.y - 630)
            pos_30 = (self.rect.x - 675, self.rect.y - 675)
            #+-
            pos_31 = (self.rect.x + 45, self.rect.y - 45)
            pos_32 = (self.rect.x + 90, self.rect.y - 90)
            pos_33 = (self.rect.x + 135, self.rect.y - 135)
            pos_34 = (self.rect.x + 180, self.rect.y - 180)
            pos_35 = (self.rect.x + 225, self.rect.y - 225)
            pos_36 = (self.rect.x + 270, self.rect.y - 270)
            pos_37 = (self.rect.x + 315, self.rect.y - 315)
            pos_38 = (self.rect.x + 360, self.rect.y - 360)
            pos_39 = (self.rect.x + 405, self.rect.y - 405)
            pos_40 = (self.rect.x + 450, self.rect.y - 450)
            pos_41 = (self.rect.x + 495, self.rect.y - 495)
            pos_42 = (self.rect.x + 540, self.rect.y - 540)
            pos_43 = (self.rect.x + 585, self.rect.y - 585)
            pos_44 = (self.rect.x + 630, self.rect.y - 630)
            pos_45 = (self.rect.x + 675, self.rect.y - 675)
            #-+
            pos_46 = (self.rect.x - 45, self.rect.y + 45)
            pos_47 = (self.rect.x - 90, self.rect.y + 90)
            pos_48 = (self.rect.x - 135, self.rect.y + 135)
            pos_49 = (self.rect.x - 180, self.rect.y + 180)
            pos_50 = (self.rect.x - 225, self.rect.y + 225)
            pos_51 = (self.rect.x - 270, self.rect.y + 270)
            pos_52 = (self.rect.x - 315, self.rect.y + 315)
            pos_53 = (self.rect.x - 360, self.rect.y + 360)
            pos_54 = (self.rect.x - 405, self.rect.y + 405)
            pos_55 = (self.rect.x - 450, self.rect.y + 450)
            pos_56 = (self.rect.x - 495, self.rect.y + 495)
            pos_57 = (self.rect.x - 540, self.rect.y + 540)
            pos_58 = (self.rect.x - 585, self.rect.y + 585)
            pos_59 = (self.rect.x - 630, self.rect.y + 630)
            pos_60 = (self.rect.x - 675, self.rect.y + 675)

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
            move_spaces.append(pos_17)
            move_spaces.append(pos_18)
            move_spaces.append(pos_19)
            move_spaces.append(pos_20)
            move_spaces.append(pos_21)
            move_spaces.append(pos_22)
            move_spaces.append(pos_23)
            move_spaces.append(pos_24)
            move_spaces.append(pos_25)
            move_spaces.append(pos_26)
            move_spaces.append(pos_27)
            move_spaces.append(pos_28)
            move_spaces.append(pos_29)
            move_spaces.append(pos_30)
            move_spaces.append(pos_31)
            move_spaces.append(pos_32)
            move_spaces.append(pos_33)
            move_spaces.append(pos_34)
            move_spaces.append(pos_35)
            move_spaces.append(pos_36)
            move_spaces.append(pos_37)
            move_spaces.append(pos_38)
            move_spaces.append(pos_39)
            move_spaces.append(pos_40)
            move_spaces.append(pos_41)
            move_spaces.append(pos_42)
            move_spaces.append(pos_43)
            move_spaces.append(pos_44)
            move_spaces.append(pos_45)
            move_spaces.append(pos_46)
            move_spaces.append(pos_47)
            move_spaces.append(pos_48)
            move_spaces.append(pos_49)
            move_spaces.append(pos_50)
            move_spaces.append(pos_51)
            move_spaces.append(pos_52)
            move_spaces.append(pos_53)
            move_spaces.append(pos_54)
            move_spaces.append(pos_55)
            move_spaces.append(pos_56)
            move_spaces.append(pos_57)
            move_spaces.append(pos_58)
            move_spaces.append(pos_59)
            move_spaces.append(pos_60)

        if self.type == 'rook':
            pos_1 = (self.rect.x + 45, self.rect.y)
            pos_2 = (self.rect.x + 90, self.rect.y)
            pos_3 = (self.rect.x + 135, self.rect.y)
            pos_4 = (self.rect.x + 180, self.rect.y)
            pos_5 = (self.rect.x + 225, self.rect.y)
            pos_6 = (self.rect.x + 270, self.rect.y)
            pos_7 = (self.rect.x + 315, self.rect.y)
            pos_8 = (self.rect.x + 360, self.rect.y)
            pos_9 = (self.rect.x + 405, self.rect.y)
            pos_10 = (self.rect.x + 450, self.rect.y)
            pos_11 = (self.rect.x + 495, self.rect.y)
            pos_12 = (self.rect.x + 540, self.rect.y)
            pos_13 = (self.rect.x + 585, self.rect.y)
            pos_14 = (self.rect.x + 630, self.rect.y)
            pos_15 = (self.rect.x + 675, self.rect.y)

            pos_16 = (self.rect.x - 45, self.rect.y)
            pos_17 = (self.rect.x - 90, self.rect.y)
            pos_18 = (self.rect.x - 135, self.rect.y)
            pos_19 = (self.rect.x - 180, self.rect.y)
            pos_20 = (self.rect.x - 225, self.rect.y)
            pos_21 = (self.rect.x - 270, self.rect.y)
            pos_22 = (self.rect.x - 315, self.rect.y)
            pos_23 = (self.rect.x - 360, self.rect.y)
            pos_24 = (self.rect.x - 405, self.rect.y)
            pos_25 = (self.rect.x - 450, self.rect.y)
            pos_26 = (self.rect.x - 495, self.rect.y)
            pos_27 = (self.rect.x - 540, self.rect.y)
            pos_28 = (self.rect.x - 585, self.rect.y)
            pos_29 = (self.rect.x - 630, self.rect.y)
            pos_30 = (self.rect.x - 675, self.rect.y)

            pos_31 = (self.rect.x, self.rect.y - 45)
            pos_32 = (self.rect.x, self.rect.y - 90)
            pos_33 = (self.rect.x, self.rect.y - 135)
            pos_34 = (self.rect.x, self.rect.y - 180)
            pos_35 = (self.rect.x, self.rect.y - 225)
            pos_36 = (self.rect.x, self.rect.y - 270)
            pos_37 = (self.rect.x, self.rect.y - 315)
            pos_38 = (self.rect.x, self.rect.y - 360)
            pos_39 = (self.rect.x, self.rect.y - 405)
            pos_40 = (self.rect.x, self.rect.y - 450)
            pos_41 = (self.rect.x, self.rect.y - 495)
            pos_42 = (self.rect.x, self.rect.y - 540)
            pos_43 = (self.rect.x, self.rect.y - 585)
            pos_44 = (self.rect.x, self.rect.y - 630)
            pos_45 = (self.rect.x, self.rect.y - 675)

            pos_46 = (self.rect.x, self.rect.y + 45)
            pos_47 = (self.rect.x, self.rect.y + 90)
            pos_48 = (self.rect.x, self.rect.y + 135)
            pos_49 = (self.rect.x, self.rect.y + 180)
            pos_50 = (self.rect.x, self.rect.y + 225)
            pos_51 = (self.rect.x, self.rect.y + 270)
            pos_52 = (self.rect.x, self.rect.y + 315)
            pos_53 = (self.rect.x, self.rect.y + 360)
            pos_54 = (self.rect.x, self.rect.y + 405)
            pos_55 = (self.rect.x, self.rect.y + 450)
            pos_56 = (self.rect.x, self.rect.y + 495)
            pos_57 = (self.rect.x, self.rect.y + 540)
            pos_58 = (self.rect.x, self.rect.y + 585)
            pos_59 = (self.rect.x, self.rect.y + 630)
            pos_60 = (self.rect.x, self.rect.y + 675)

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
            move_spaces.append(pos_17)
            move_spaces.append(pos_18)
            move_spaces.append(pos_19)
            move_spaces.append(pos_20)
            move_spaces.append(pos_21)
            move_spaces.append(pos_22)
            move_spaces.append(pos_23)
            move_spaces.append(pos_24)
            move_spaces.append(pos_25)
            move_spaces.append(pos_26)
            move_spaces.append(pos_27)
            move_spaces.append(pos_28)
            move_spaces.append(pos_29)
            move_spaces.append(pos_30)
            move_spaces.append(pos_31)
            move_spaces.append(pos_32)
            move_spaces.append(pos_33)
            move_spaces.append(pos_34)
            move_spaces.append(pos_35)
            move_spaces.append(pos_36)
            move_spaces.append(pos_37)
            move_spaces.append(pos_38)
            move_spaces.append(pos_39)
            move_spaces.append(pos_40)
            move_spaces.append(pos_41)
            move_spaces.append(pos_42)
            move_spaces.append(pos_43)
            move_spaces.append(pos_44)
            move_spaces.append(pos_45)
            move_spaces.append(pos_46)
            move_spaces.append(pos_47)
            move_spaces.append(pos_48)
            move_spaces.append(pos_49)
            move_spaces.append(pos_50)
            move_spaces.append(pos_51)
            move_spaces.append(pos_52)
            move_spaces.append(pos_53)
            move_spaces.append(pos_54)
            move_spaces.append(pos_55)
            move_spaces.append(pos_56)
            move_spaces.append(pos_57)
            move_spaces.append(pos_58)
            move_spaces.append(pos_59)
            move_spaces.append(pos_60)

        if self.type == 'queen':
            pos_1 = (self.rect.x + 45, self.rect.y + 45)
            pos_2 = (self.rect.x + 90, self.rect.y + 90)
            pos_3 = (self.rect.x + 135, self.rect.y + 135)
            pos_4 = (self.rect.x + 180, self.rect.y + 180)
            pos_5 = (self.rect.x + 225, self.rect.y + 225)
            pos_6 = (self.rect.x + 270, self.rect.y + 270)
            pos_7 = (self.rect.x + 315, self.rect.y + 315)
            pos_8 = (self.rect.x + 360, self.rect.y + 360)
            pos_9 = (self.rect.x + 405, self.rect.y + 405)
            pos_10 = (self.rect.x + 450, self.rect.y + 450)
            pos_11 = (self.rect.x + 495, self.rect.y + 495)
            pos_12 = (self.rect.x + 540, self.rect.y + 540)
            pos_13 = (self.rect.x + 585, self.rect.y + 585)
            pos_14 = (self.rect.x + 630, self.rect.y + 630)
            pos_15 = (self.rect.x + 675, self.rect.y + 675)
            
            pos_16 = (self.rect.x - 45, self.rect.y - 45)
            pos_17 = (self.rect.x - 90, self.rect.y - 90)
            pos_18 = (self.rect.x - 135, self.rect.y - 135)
            pos_19 = (self.rect.x - 180, self.rect.y - 180)
            pos_20 = (self.rect.x - 225, self.rect.y - 225)
            pos_21 = (self.rect.x - 270, self.rect.y - 270)
            pos_22 = (self.rect.x - 315, self.rect.y - 315)
            pos_23 = (self.rect.x - 360, self.rect.y - 360)
            pos_24 = (self.rect.x - 405, self.rect.y - 405)
            pos_25 = (self.rect.x - 450, self.rect.y - 450)
            pos_26 = (self.rect.x - 495, self.rect.y - 495)
            pos_27 = (self.rect.x - 540, self.rect.y - 540)
            pos_28 = (self.rect.x - 585, self.rect.y - 585)
            pos_29 = (self.rect.x - 630, self.rect.y - 630)
            pos_30 = (self.rect.x - 675, self.rect.y - 675)
            
            pos_31 = (self.rect.x + 45, self.rect.y - 45)
            pos_32 = (self.rect.x + 90, self.rect.y - 90)
            pos_33 = (self.rect.x + 135, self.rect.y - 135)
            pos_34 = (self.rect.x + 180, self.rect.y - 180)
            pos_35 = (self.rect.x + 225, self.rect.y - 225)
            pos_36 = (self.rect.x + 270, self.rect.y - 270)
            pos_37 = (self.rect.x + 315, self.rect.y - 315)
            pos_38 = (self.rect.x + 360, self.rect.y - 360)
            pos_39 = (self.rect.x + 405, self.rect.y - 405)
            pos_40 = (self.rect.x + 450, self.rect.y - 450)
            pos_41 = (self.rect.x + 495, self.rect.y - 495)
            pos_42 = (self.rect.x + 540, self.rect.y - 540)
            pos_43 = (self.rect.x + 585, self.rect.y - 585)
            pos_44 = (self.rect.x + 630, self.rect.y - 630)
            pos_45 = (self.rect.x + 675, self.rect.y - 675)

            pos_46 = (self.rect.x - 45, self.rect.y + 45)
            pos_47 = (self.rect.x - 90, self.rect.y + 90)
            pos_48 = (self.rect.x - 135, self.rect.y + 135)
            pos_49 = (self.rect.x - 180, self.rect.y + 180)
            pos_50 = (self.rect.x - 225, self.rect.y + 225)
            pos_51 = (self.rect.x - 270, self.rect.y + 270)
            pos_52 = (self.rect.x - 315, self.rect.y + 315)
            pos_53 = (self.rect.x - 360, self.rect.y + 360)
            pos_54 = (self.rect.x - 405, self.rect.y + 405)
            pos_55 = (self.rect.x - 450, self.rect.y + 450)
            pos_56 = (self.rect.x - 495, self.rect.y + 495)
            pos_57 = (self.rect.x - 540, self.rect.y + 540)
            pos_58 = (self.rect.x - 585, self.rect.y + 585)
            pos_59 = (self.rect.x - 630, self.rect.y + 630)
            pos_60 = (self.rect.x - 675, self.rect.y + 675)

            pos_61 = (self.rect.x + 45, self.rect.y)
            pos_62 = (self.rect.x + 90, self.rect.y)
            pos_63 = (self.rect.x + 135, self.rect.y)
            pos_64 = (self.rect.x + 180, self.rect.y)
            pos_65 = (self.rect.x + 225, self.rect.y)
            pos_66 = (self.rect.x + 270, self.rect.y)
            pos_67 = (self.rect.x + 315, self.rect.y)
            pos_68 = (self.rect.x + 360, self.rect.y)
            pos_69 = (self.rect.x + 405, self.rect.y)
            pos_70 = (self.rect.x + 450, self.rect.y)
            pos_71 = (self.rect.x + 495, self.rect.y)
            pos_72 = (self.rect.x + 540, self.rect.y)
            pos_73 = (self.rect.x + 585, self.rect.y)
            pos_74 = (self.rect.x + 630, self.rect.y)
            pos_75 = (self.rect.x + 675, self.rect.y)

            pos_76 = (self.rect.x - 45, self.rect.y)
            pos_77 = (self.rect.x - 90, self.rect.y)
            pos_78 = (self.rect.x - 135, self.rect.y)
            pos_79 = (self.rect.x - 180, self.rect.y)
            pos_80 = (self.rect.x - 225, self.rect.y)
            pos_81 = (self.rect.x - 270, self.rect.y)
            pos_82 = (self.rect.x - 315, self.rect.y)
            pos_83 = (self.rect.x - 360, self.rect.y)
            pos_84 = (self.rect.x - 405, self.rect.y)
            pos_85 = (self.rect.x - 450, self.rect.y)
            pos_86 = (self.rect.x - 495, self.rect.y)
            pos_87 = (self.rect.x - 540, self.rect.y)
            pos_88 = (self.rect.x - 585, self.rect.y)
            pos_89 = (self.rect.x - 630, self.rect.y)
            pos_90 = (self.rect.x - 675, self.rect.y)

            pos_91 = (self.rect.x, self.rect.y - 45)
            pos_92 = (self.rect.x, self.rect.y - 90)
            pos_93 = (self.rect.x, self.rect.y - 135)
            pos_94 = (self.rect.x, self.rect.y - 180)
            pos_95 = (self.rect.x, self.rect.y - 225)
            pos_96 = (self.rect.x, self.rect.y - 270)
            pos_97 = (self.rect.x, self.rect.y - 315)
            pos_98 = (self.rect.x, self.rect.y - 360)
            pos_99 = (self.rect.x, self.rect.y - 405)
            pos_100 = (self.rect.x, self.rect.y - 450)
            pos_101 = (self.rect.x, self.rect.y - 495)
            pos_102 = (self.rect.x, self.rect.y - 540)
            pos_103 = (self.rect.x, self.rect.y - 585)
            pos_104 = (self.rect.x, self.rect.y - 630)
            pos_105 = (self.rect.x, self.rect.y - 675)

            pos_106 = (self.rect.x, self.rect.y + 45)
            pos_107 = (self.rect.x, self.rect.y + 90)
            pos_108 = (self.rect.x, self.rect.y + 135)
            pos_109 = (self.rect.x, self.rect.y + 180)
            pos_110 = (self.rect.x, self.rect.y + 225)
            pos_111 = (self.rect.x, self.rect.y + 270)
            pos_112 = (self.rect.x, self.rect.y + 315)
            pos_113 = (self.rect.x, self.rect.y + 360)
            pos_114 = (self.rect.x, self.rect.y + 405)
            pos_115 = (self.rect.x, self.rect.y + 450)
            pos_116 = (self.rect.x, self.rect.y + 495)
            pos_117 = (self.rect.x, self.rect.y + 540)
            pos_118 = (self.rect.x, self.rect.y + 585)
            pos_119 = (self.rect.x, self.rect.y + 630)
            pos_120 = (self.rect.x, self.rect.y + 675)

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
            move_spaces.append(pos_17)
            move_spaces.append(pos_18)
            move_spaces.append(pos_19)
            move_spaces.append(pos_20)
            move_spaces.append(pos_21)
            move_spaces.append(pos_22)
            move_spaces.append(pos_23)
            move_spaces.append(pos_24)
            move_spaces.append(pos_25)
            move_spaces.append(pos_26)
            move_spaces.append(pos_27)
            move_spaces.append(pos_28)
            move_spaces.append(pos_29)
            move_spaces.append(pos_30)
            move_spaces.append(pos_31)
            move_spaces.append(pos_32)
            move_spaces.append(pos_33)
            move_spaces.append(pos_34)
            move_spaces.append(pos_35)
            move_spaces.append(pos_36)
            move_spaces.append(pos_37)
            move_spaces.append(pos_38)
            move_spaces.append(pos_39)
            move_spaces.append(pos_40)
            move_spaces.append(pos_41)
            move_spaces.append(pos_42)
            move_spaces.append(pos_43)
            move_spaces.append(pos_44)
            move_spaces.append(pos_45)
            move_spaces.append(pos_46)
            move_spaces.append(pos_47)
            move_spaces.append(pos_48)
            move_spaces.append(pos_49)
            move_spaces.append(pos_50)
            move_spaces.append(pos_51)
            move_spaces.append(pos_52)
            move_spaces.append(pos_53)
            move_spaces.append(pos_54)
            move_spaces.append(pos_55)
            move_spaces.append(pos_56)
            move_spaces.append(pos_57)
            move_spaces.append(pos_58)
            move_spaces.append(pos_59)
            move_spaces.append(pos_60)
            move_spaces.append(pos_61)
            move_spaces.append(pos_62)
            move_spaces.append(pos_63)
            move_spaces.append(pos_64)
            move_spaces.append(pos_65)
            move_spaces.append(pos_66)
            move_spaces.append(pos_67)
            move_spaces.append(pos_68)
            move_spaces.append(pos_69)
            move_spaces.append(pos_70)
            move_spaces.append(pos_71)
            move_spaces.append(pos_72)
            move_spaces.append(pos_73)
            move_spaces.append(pos_74)
            move_spaces.append(pos_75)
            move_spaces.append(pos_76)
            move_spaces.append(pos_77)
            move_spaces.append(pos_78)
            move_spaces.append(pos_79)
            move_spaces.append(pos_80)
            move_spaces.append(pos_81)
            move_spaces.append(pos_82)
            move_spaces.append(pos_83)
            move_spaces.append(pos_84)
            move_spaces.append(pos_85)
            move_spaces.append(pos_86)
            move_spaces.append(pos_87)
            move_spaces.append(pos_88)
            move_spaces.append(pos_89)
            move_spaces.append(pos_90)
            move_spaces.append(pos_91)
            move_spaces.append(pos_92)
            move_spaces.append(pos_93)
            move_spaces.append(pos_94)
            move_spaces.append(pos_95)
            move_spaces.append(pos_96)
            move_spaces.append(pos_97)
            move_spaces.append(pos_98)
            move_spaces.append(pos_99)
            move_spaces.append(pos_100)
            move_spaces.append(pos_101)
            move_spaces.append(pos_102)
            move_spaces.append(pos_103)
            move_spaces.append(pos_104)
            move_spaces.append(pos_105)
            move_spaces.append(pos_106)
            move_spaces.append(pos_107)
            move_spaces.append(pos_108)
            move_spaces.append(pos_109)
            move_spaces.append(pos_110)
            move_spaces.append(pos_111)
            move_spaces.append(pos_112)
            move_spaces.append(pos_113)
            move_spaces.append(pos_114)
            move_spaces.append(pos_115)
            move_spaces.append(pos_116)
            move_spaces.append(pos_117)
            move_spaces.append(pos_118)
            move_spaces.append(pos_119)
            move_spaces.append(pos_120)

        if self.type == 'king':
            pos_1 = (self.rect.x, self.rect.y - 45)
            pos_2 = (self.rect.x + 45, self.rect.y - 45)
            pos_3 = (self.rect.x + 45, self.rect.y)
            pos_4 = (self.rect.x + 45, self.rect.y + 45)
            pos_5 = (self.rect.x, self.rect.y + 45)
            pos_6 = (self.rect.x - 45, self.rect.y + 45)
            pos_7 = (self.rect.x - 45, self.rect.y)
            pos_8 = (self.rect.x - 45, self.rect.y - 45)

            move_spaces.append(pos_1)
            move_spaces.append(pos_2)
            move_spaces.append(pos_3)
            move_spaces.append(pos_4)
            move_spaces.append(pos_5)
            move_spaces.append(pos_6)
            move_spaces.append(pos_7)
            move_spaces.append(pos_8)

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

                    if move_spaces[constants.N][0] > self.rect.x:
                        self.direction = 'right'
                    if move_spaces[constants.N][0] < self.rect.x:
                        self.direction = 'left'
                    if move_spaces[constants.N][1] > self.rect.y:
                        self.direction = 'down'
                    if move_spaces[constants.N][1] < self.rect.y:
                        self.direction = 'up'

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
    
    def update_sprite(self):
        if self.type == 'pawn':
            self.image = constants.GETIMAGE('pieces/pl.png')
        elif self.type == 'knight':
            self.image = constants.GETIMAGE('pieces/nl.png')
        elif self.type == 'bishop':
            self.image = constants.GETIMAGE('pieces/bl.png')
        elif self.type == 'rook':
            self.image = constants.GETIMAGE('pieces/rl.png')
        elif self.type == 'queen':
            self.image = constants.GETIMAGE('pieces/ql.png')
        elif self.type == 'king':
            self.image = constants.GETIMAGE('pieces/kl.png')


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
            constants.S = 'END'
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
