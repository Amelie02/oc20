import pygame
from pygame.locals import * #afiche toutes les variables existantes

BLACK = (0, 0, 0)
GRAY = (127, 127, 127)
WHITE = (255, 255, 255)

# 1er = rouge, 2eme = vert, 3eme = bleu
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

#on peut nuancer en diminuant les chiffres
YELLOW = (250, 250, 0)
CYAN = (0, 250, 250)
MAGENTA = (250, 0, 250)

background = GRAY

#on crée un dictionnaire pour chaque couleur
key_dict = {K_k:BLACK, K_r:RED, K_b:BLUE, K_y:YELLOW, K_g:GREEN, K_w:WHITE}

pygame.init()



screen = pygame.display.set_mode((640, 480))
screen.fill(background)
pygame.display.update() #nécessaire pour relancer avec les changements

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: #cliquer sur le bouton rouge(x)
            running = False
        
        elif event.type == pygame.KEYDOWN: #une touche du clavier est enfoncée
            print(event)
        #on peut faire de deux manières:avec un dict ou appeler chaque couleur
            if event.key in key_dict: #la touche enfoncée est une des 8 touches du dictionnaire
                background = key_dict[event.key]
                
                caption = 'background color = ' + str(background)
                pygame.display.set_caption(caption)
                
        #chaque bouton à sa variable : pygame.K_....
#             if event.key == pygame.K_r:
#                 background = RED
#             elif event.key == pygame.K_g:
#                 background = GREEN
#             elif event.key == pygame.K_m:
#                 background = MAGENTA
                    
            screen.fill(background)
            pygame.display.update()

pygame.quit()