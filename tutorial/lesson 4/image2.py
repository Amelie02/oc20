import pygame
from pygame.locals import *

SIZE = 500, 500
RED = (255, 0, 0)
GRAY = (150, 150, 150)

pygame.init()
screen = pygame.display.set_mode(SIZE)

img0 = pygame.image.load(path)
img0.convert()

rect0 = img0.get_rect()
pygame.draw.rect(img0, GREEN, rect0, 1)

center = 250, 250
img = img0
rect = img.get_rect()
rect.center = center