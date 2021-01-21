import pygame
from pygame.locals import *

# size = 640, 320
# width, height = size

width = 640
height = 320

size = (width,height)
GREEN = (150, 255, 255)
RED = (255, 0, 0)

pygame.init()
screen = pygame.display.set_mode(size)
running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            
pygame.quit()
            