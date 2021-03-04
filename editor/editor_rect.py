"""Place multiple rectangles with the mouse."""
import pygame
from pygame.locals import *

BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)

RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
GRAY = (127, 127, 127)

YELLOW = (255, 255, 0)
CYAN = (0, 255, 255)
MAGENTA = (255, 0, 255)

pygame.init()
screen = pygame.display.set_mode((640, 500))

start = (0, 0)
size = (0, 0)
drawing = False
color = RED
width = 0
type_ = 'r'
shapes = []

rect0 = Rect(50, 60, 200, 80)
rect = rect0.copy()

dir = {K_LEFT: (-5, 0), K_RIGHT: (5, 0), K_UP: (0, -5), K_DOWN: (0, 5)}

# définir une classe de formes (shape) avec rectangle, couleur, épaisseur
# type_  'r' = rectangle, 'e' = elipsse
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

running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        if event.type == KEYDOWN:
            if event.key == K_1:
                width = 0
            elif event.key == K_2:
                width = 1
            elif event.key == K_3:
                width = 3
        
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
            
        elif event.type == KEYDOWN:
            if event.key in dir:
                v = dir[event.key]
                rect.move_ip(v)

    screen.fill(GRAY)
    for s in shapes[1:]: 
        s.draw()    
    pygame.display.update()
    

pygame.quit()
