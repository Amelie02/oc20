"""Place multiple rectangles with the mouse."""

import pygame
from pygame.locals import *

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GRAY = (127, 127, 127)
GREEN = (0, 255, 0)

pygame.init()
screen = pygame.display.set_mode((640, 240))

start = (0, 0)
size = (0, 0)
drawing = False
rect_list = []

#définir une classe de formes (shape) avec rectangle, couleur et épaisseur
class Shape:
    def __init__(self, rect, color=RED, width=1):
        self.rect = rect
        self.color = color
        self.width = width

#créer une instance(--> n objet)
current_shape = Shape(pygame.Rect(10, 10, 100, 500))

#afficher les attributs de cet objet
print('rect =', current_shape.rect)
print('color =', current_shape.color)
print('width =', current_shape.width)

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_0:
                current_shape.width = 0
            elif event.key == K_1:
                current_shape.width = 1
            elif event.key == K_3:
                current_shape.width = 3
                
            elif event.key == K_r:
                current_shape.color = RED
            elif event.key == K_g:
                current_shape.color = GREEN
            elif event.key == K_b:
                current_shape.color = BLUE
            

        elif event.type == MOUSEBUTTONDOWN:
            start = event.pos
            size = 0, 0
            drawing = True
            current_shape = Shape(pygame.Rect(start, size))
            
        elif event.type == MOUSEBUTTONUP:
            end = event.pos
            size = end[0]-start[0], end[1]-start[1]
            rect = pygame.Rect(start, size)
            
            current_shape.rect = rect
            
            shape_list.append(current_shape)
            drawing = False

        elif event.type == MOUSEMOTION and drawing:
            end = event.pos
            size = end[0]-start[0], end[1]-start[1]
            

    screen.fill(GRAY)
    for s in shape_list:
        pygame.draw.rect(screen, s.color, s.rect, s.width)
    pygame.draw.rect(screen, BLUE, current_shape.rect)
    pygame.display.update()

pygame.quit()