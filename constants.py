import pygame
import os
import sys

pygame.init()

CLOCK = pygame.time.Clock()
N = 0
I = 0
C = 0

ALLOWEDMOVE = pygame.Surface((45, 45))
ALLOWEDMOVE.set_alpha(128)
ALLOWEDMOVE.fill((79, 121, 66))

SELECTEDMOVE = pygame.Surface((45, 45))
SELECTEDMOVE.set_alpha(192)
SELECTEDMOVE.fill((255, 0, 0))

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

_image_library = {}


def GETIMAGE(path):
    global _image_library
    image = _image_library.get(path)
    if image is None:
        canonicalized_path = path.replace('/', os.sep).replace('\\', os.sep)
        image = pygame.image.load(canonicalized_path)
        _image_library[path] = image
    return image
