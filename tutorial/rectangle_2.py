import pygame
from pygame.locals import *


start = (0, 0)
size = (0, 0)
drawing = False

elif event.type == MOUSEBUTTONDOWN:
    start = event.pos
    size = 0, 0
    drawing = True
elif event.type == MOUSEBUTTONUP:
    end = event.pos
    size = end[0] - start[0], end[1] - start[1]
    drawing = False
    
elif event.type == MOUSEMOTION and drawing:
    end = event.pos
    size = end[0] - start[0], end[1] - start[1]
    
    screen.fill(GRAY)
pygame.draw.rect(screen, RED, (start, size), 2)
pygame.display.update()