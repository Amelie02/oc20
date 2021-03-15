"""Move an image with the mouse."""

import pygame
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

key_dict = {K_k:BLACK, K_r:RED, K_g:GREEN, K_b:BLUE, 
    K_y:YELLOW, K_c:CYAN, K_m:MAGENTA, K_w:WHITE}

pygame.init()
w, h = 800, 800
screen = pygame.display.set_mode((w, h))
running = True

img = pygame.image.load('pacman.png')
img.convert()
rect = img.get_rect()
rect.center = w//2, h//2
# image = []
moving = False
screen.fill(event.key)

angle = 0

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
#         Pour faire apparaître ou disparaître l'image
        elif event.type == KEYDOWN:
            if event.key == K_a:
                i = screen.blit(img, rect)
                image.append(i)
            elif event.key == K_BACKSPACE:
                image.pop()
                
#                         
#                 class Objet (pygame.sprite.Sprite):
#             """Création de la classe "Objet" """
#             def __init__(self, objet_x, objet_y):
#                 pygame.sprite.Sprite.__init__(self)
#                 self.image = img = pygame.image.load('pacman.png').convert()
#                 self.x = objet_x
#                 self.y = objet_y
#          
#         def Spawnobjet(objet_x, objet_y):
#             return objet(objet_x, objet_y)
        
#         Pour qu'on puisse bouger l'image avec la souris
        elif event.type == MOUSEBUTTONDOWN:
#             if rect.collidepoint(event.pos):
            moving = True

        elif event.type == MOUSEBUTTONUP:
            moving = False

        elif event.type == MOUSEMOTION and moving:
            rect.move_ip(event.rel)
            

#         Pour que le fantôme regarde de l'autre côté
        elif event.type == KEYDOWN:
            if event.key == K_h:
                img = pygame.transform.flip(img, True, False)
#             Pour que le fantôme soit upside-down
            elif event.key == K_v:
                img = pygame.transform.flip(img, False, True)
    
    screen.fill(GRAY)
    screen.blit(img, rect)
#     pygame.draw.rect(screen, RED, rect, 2)
    pygame.display.update()

pygame.quit()