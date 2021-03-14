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
moving = False

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        elif event.type == MOUSEBUTTONDOWN:
#             if rect.collidepoint(event.pos):
            moving = True

        elif event.type == MOUSEBUTTONUP:
            moving = False

        elif event.type == MOUSEMOTION and moving:
            rect.move_ip(event.rel)
    
    screen.fill(GRAY)
    screen.blit(img, rect)
#    pygame.draw.rect(screen, RED, rect, 2)
    pygame.display.update()

pygame.quit()