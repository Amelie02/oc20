import pygame
from pygame.locals import *

SIZE = 500, 500
RED = (255, 0, 0)
GRAY = (150, 150, 150)

pygame.init()
screen = pygame.display.set_mode(SIZE)

img = pygame.image.load('bird.png')
img.convert()

rect = img.get_rect()
rect.center = 250, 250
moving = False
dir = {K_LEFT: (-5, 0), K_RIGHT: (5, 0), K_UP: (0, -5), K_DOWN: (0, 5)}

running = True
while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        #move with keyboard arrows            
        if event.type == KEYDOWN:
            if event.key in dir:
                v = dir[event.key]
                rect.move_ip(v)
        #move with mousebutton
        elif event.type == MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                moving = True
        
        elif event.type == MOUSEBUTTONUP:
            moving = False
        
        elif event.type == MOUSEMOTION and moving:
            rect.move_ip(event.rel)

    screen.fill(GRAY)
    pygame.draw.rect(screen, RED, rect, 2)
    screen.blit(img, rect)
    pygame.display.flip()

pygame.quit()