import pygame
import math, sys, os
from pygame.locals import *

BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)


pygame.init()
w, h = 800, 800
screen = pygame.display.set_mode((w, h))

# On met "à zéro" les valeurs de base(lancement de l'interface, mouvements de la souris)
running = True
moving = False
drawing = False

# variable pour le sprite
image = []
img = pygame.image.load('pacman.png')
img.convert()
rect = img.get_rect()
rect.center = w//2, h//2

# Variables pour les dessins
start = (0, 0)
size = (0, 0)
color = RED
width = 1
type_ = 'r'
shapes = []

rect0 = Rect(50, 60, 200, 80)
rect = rect0.copy()

dir = {K_LEFT: (-5, 0), K_RIGHT: (5, 0), K_UP: (0, -5), K_DOWN: (0, 5)}

# définir une classe de formes (shape) avec rectangle, couleur, épaisseur
# type_  'r' = rectangle, 'e' = ellipse
class Shape:
    def __init__(self, rect, color=RED, width=0, type_ = 'r'):
        self.rect = rect
        self.color = color
        self.width = width
        self.type = type_
        
    def draw(self):
        if self.type == 'r':
            pygame.draw.rect(screen, self.color, self.rect, self.width)
        if self.type == 'e':
            pygame.draw.ellipse(screen, self.color, self.rect, self.width)
            
            
    def do_event(self, event):
        if event.type == KEYDOWN:
            if event.key in dir:
                self.rect.move_ip(dir[event.key])



while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
#         Pour faire apparaître l'image
            if event.key == K_a:
                img = pygame.image.load('pacman.png')
                img.convert()
                rect = img.get_rect()
                rect.center = w//2, h//2
                image.append(1)
            
#             Pour faire disparaître l'image
            elif event.key == K_z:
                image.pop()
        
#             Pour déplacer le sprite (en haut, en bas, à gauche et à droite)
            elif event.key == K_UP:
                rect.center = w//2, h//2 - 100
                
            elif event.key == K_DOWN:
                rect.center = w//2, h//2 + 100
                
            elif event.key == K_RIGHT:
                rect.center = w//2 + 100, h//2

            elif event.key == K_LEFT:
                rect.center = w//2 - 100, h//2
                
#             Pour modifier l'épaisseur des rectangles
            elif event.key == K_0:
                width = 0
            elif event.key == K_1:
                width = 1
            elif event.key == K_3:
                width = 3
        
#             Pour modifier la couleur des rectangles
            elif event.key == K_r:
                color = RED
            elif event.key == K_g:
                color = GREEN
            elif event.key == K_b:
                color = BLUE
            elif event.key == K_y:
                color = YELLOW
            elif event.key == K_m:
                color = MAGENTA
            elif event.key == K_c:
                color = CYAN
            elif event.key == K_q:
                color = BLACK
            elif event.key == K_s:
                color = GRAY
            elif event.key == K_w:
                color = WHITE
        
        
#             Pour supprimer les rectangles dessinés
            elif event.key == K_BACKSPACE:
                if len(shapes) >1:
                    shapes.pop()
                    color = shapes[-1].color
                    width = shapes[-1].width
            
                    shapes[-1].width = width
                    shapes[-1].color = color
                    shapes[-1].type = type_
            
            
        elif event.type == MOUSEBUTTONDOWN:
            start = event.pos
            s = Shape(Rect(start, (0, 0)), color, width)
            shapes.append(s)
            drawing = True
            
        elif event.type == MOUSEBUTTONUP:
            drawing = False

        elif event.type == MOUSEMOTION and drawing:
            end = event.pos
            size = end[0]-start[0], end[1]-start[1]
            shapes[-1].rect.size = size


#         pour le dernier élément (en train d'etre édité)
        if len(shapes) > 0:
            shapes[-1].do_event(event)
        
            
    screen.fill(GRAY)
    for a in image:
        if image == [1]:
            screen.blit(img, rect)
    for s in shapes[1:]: 
        s.draw() 
    pygame.display.update()

pygame.quit()