import pygame
import os
import sys

pygame.init()

#Utility Constants
CLOCK = pygame.time.Clock()

#Counting Constants
N = 0
C = -1
S = 0

#Color Constants
WHITE = (232, 221, 201)
BLACK = (57, 59, 58)
LIGHTBLACK = (70, 72, 71)
BROWN = (150, 81, 16)


#Boolean Constants
DONE = False
CANSPAWNPAWNS = True # 
CANSPAWNKNIGHTS = True
CANSPAWNBISHOPS = True
CANSPAWNROOKS = True
CANSPAWNQUEENS = True
CANSPAWNKINGS = True

#Space Constants
ALLOWEDMOVE = pygame.Surface((45, 45))
ALLOWEDMOVE.set_alpha(128)
ALLOWEDMOVE.fill((79, 121, 66))

SELECTEDMOVE = pygame.Surface((45, 45))
SELECTEDMOVE.set_alpha(192)
SELECTEDMOVE.fill((255, 0, 0))

#Array Constants
PIECETYPES = ['pawn', 'knight', 'bishop', 'rook', 'queen', 'king']

POSXLIST = [45, 90, 135, 180, 225, 270, 315, 360,
            405, 450, 495, 540, 585, 630, 675, 720]
POSYLIST = [45, 90, 135, 180, 225, 270, 315, 360,
            405, 450, 495, 540, 585, 630, 675, 720]
POSLIST = [(45, 45), (45, 720), (90, 45), (90, 720), (135, 45), (135, 720),
           (180, 45), (180, 720), (225, 45), (225, 720), (270, 45),
           (270, 720), (315, 45), (315, 720), (360, 45), (360, 720),
           (405, 45), (405, 720), (450, 45), (450, 720), (495, 45),
           (495, 720), (540, 45), (540, 720), (585, 45), (585, 720),
           (630, 45), (630, 720), (675, 45), (675, 720), (720, 45),
           (720, 720), (45, 90), (45, 135), (45, 180), (45, 225),
           (45, 270), (45, 315), (45, 360), (45, 405), (45, 450),
           (45, 495), (45, 540), (45, 585), (45, 630), (45, 675),
           (720, 90), (720, 135), (720, 180), (720, 225),
           (720, 270), (720, 315), (720, 360), (720, 405),
           (720, 450), (720, 495), (720, 540), (720, 585),
           (720, 630), (720, 675)]
PAWNPOSLIST = [(45, 45), (45, 720), (90, 45), (90, 720), (135, 45), (135, 720),
               (180, 45), (180, 720), (225, 45), (225, 720), (270, 45),
               (270, 720), (315, 45), (315, 720), (360, 45), (360, 720),
               (405, 45), (405, 720), (450, 45), (450, 720), (495, 45),
               (495, 720), (540, 45), (540, 720), (585, 45), (585, 720),
               (630, 45), (630, 720), (675, 45), (675, 720), (720, 45),
               (720, 720), (45, 90), (45, 135), (45, 180), (45, 225),
               (45, 270), (45, 315), (45, 360), (45, 405), (45, 450),
               (45, 495), (45, 540), (45, 585), (45, 630), (45, 675),
               (720, 90), (720, 135), (720, 180), (720, 225),
               (720, 270), (720, 315), (720, 360), (720, 405),
               (720, 450), (720, 495), (720, 540), (720, 585),
               (720, 630), (720, 675)]

#Function Constants
_image_library = {}

def GETIMAGE(path):
    global _image_library
    image = _image_library.get(path)
    if image is None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image


def TEXTOBJECT(text, font, color):
    """Creates object for text to be created on"""
    text_surface = font.render(text, True, color)
    return text_surface, text_surface.get_rect()


def INCREASESTO1():
    global S
    S = 1


def INCREASESTO2():
    global S
    S = 2


#Class Constants
class Button(pygame.Rect):

    def __init__(self, x, y, width, height, message, inactive_color, active_color, text_color):
        super().__init__(x, y, width, height)
        self.message = message
        self.inactive_color = inactive_color
        self.active_color = active_color
        self.text_color = text_color

    def click(self, screen, action=None):

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if self.x + self.width > mouse[0] > self.x and self.y + self.height > mouse[1] > self.y:
            pygame.draw.rect(screen, self.active_color, (self.x, self.y, self.width, self.height))

            if click[0] == 1 and action is not None:
                action()

        else:
            pygame.draw.rect(screen, self.inactive_color, (self.x, self.y, self.width, self.height))

        font = pygame.font.Font("GaramondNo8-Regular.ttf", 45)
        text_surface, text_rect = TEXTOBJECT(self.message, font, self.text_color)
        text_rect.center = ((self.x+(self.width/2)), (self.y+(self.height/2)))
        screen.blit(text_surface, text_rect)
