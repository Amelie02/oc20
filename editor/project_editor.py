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
w, h = 640, 240
screen = pygame.display.set_mode((w, h))
running = True
background = BLACK

path = os.path.join(path, 'pacman2.png')

img0 = pygame.image.load(path)
img0.convert()

# draw a green border around img0
rect0 = img0.get_rect()
pygame.draw.rect(img0, RED, rect0, 1)

# rect = Rect(50, 60, 250, 100)
# rect0 = Rect(150, 160, 200, 180)
# rect = rect0.copy()
# r1 = Rect(100, 20, 80, 170)

center = w//2, h//2
img = img0
rect = img.get_rect()
rect.center = center

angle = 0
scale = 1

mouse = pygame.mouse.get_pos()

# img = pygame.image.load('pacman2.png')
# img.convert()
# rect = img.get_ellipse()
# ellipse.center = w//2, h//2
# moving = False

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
            
        elif event.type == KEYDOWN:
            if event.key in key_dict:
                background = key_dict[event.key]
        
        elif event.type == MOUSEBUTTONDOWN:
            if rect.collidepoint(event.pos):
                moving = True

        elif event.type == MOUSEBUTTONUP:
            moving = False

#         elif event.type == MOUSEMOTION and moving:
#             rect.move_ip(event.rel)
    
        elif event.key == K_h:
            img = pygame.transform.flip(img, True, False)
        elif event.key == K_v:
            img = pygame.transform.flip(img, False, True)
                

    screen.fill(background)
    screen.blit(img, rect)
    pygame.draw.rect(screen, key_dict[event.key], rect, 2)
    pygame.display.update()

pygame.quit()