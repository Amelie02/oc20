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

rect = Rect(50, 60, 250, 100)
rect0 = Rect(150, 160, 200, 180)
rect = rect0.copy()
r1 = Rect(100, 20, 80, 170)

pygame.init()
w, h = 500, 500
screen = pygame.display.set_mode((w, h))
running = True
background = BLACK



while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_l:
                rect.left = 1
            if event.key == K_r:
                rect.right = width

            if event.key == K_t:
                rect.top = 1
            if event.key == K_b:
                rect.bottom = height
                
            if event.key == K_c:
                rect.centerx = width//2
                rect.centery = height//2
                
#         elif event.type == KEYDOWN:
#             if event.key in dir:
#                 v = dir[event.key]
#                 rect0.inflate_ip(v)

        if event.type == KEYDOWN:
            if event.key in dir:
                r1.move_ip(dir[event.key])

    screen.fill(GRAY)
    pygame.draw.rect(screen, BLUE, rect0, 1)
    pygame.draw.rect(screen, RED, rect, 4)
    pygame.draw.rect(screen, MAGENTA, rect)
    pygame.display.flip()

#     pygame.draw.rect(screen, MAGENTA, rect)
#     pygame.display.flip()

pygame.quit()