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

background = GRAY

# On crée un dictionnaire de couleurs pour le fond
key_color = {K_9:BLACK, K_8: GRAY, K_7:WHITE}

pygame.init()
w, h = 1400, 700
screen = pygame.display.set_mode((w, h))

# On met "à zéro" les valeurs de base(lancement de l'interface, mouvements de la souris)
running = True
moving = False
drawing = False

# Variables pour les formes
color = RED
width = 1

# On crée un dictionnaire pour les flèches du clavier
dir = {K_LEFT: (-5, 0), K_RIGHT: (5, 0), K_UP: (0, -5), K_DOWN: (0, 5)}

# On définit une classe rectangle et on définit la couleur, l'épaisseur, les mouvements
class Rectangle:
    def __init__(self, color=RED, width=1):
        self.rect = pygame.Rect(0, 0, 20, 20)
        self.color = color
        self.width = width
        
    def do_event(self, event):
        global drawing
        
        if event.type == KEYDOWN:
            if event.key in dir:
                self.rect.move_ip(dir[event.key])
                
        # Pour dessiner un rectangle    
        elif event.type == MOUSEBUTTONDOWN:
            self.rect.topleft = event.pos
            drawing = True
            
        elif event.type == MOUSEBUTTONUP:
            drawing = False

        elif event.type == MOUSEMOTION and drawing:
            self.rect.width = event.pos[0] - self.rect.left
            self.rect.height = event.pos[1] - self.rect.top                
        
    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect, self.width)
        
# On crée une classe ellipse avec les mêmes propriétés que la classe rectangles
class Ellipse(Rectangle):
    def draw(self):
        pygame.draw.ellipse(screen, self.color, self.rect, self.width)
            
# On crée une classe image et on définit l'image downloader, les mouvements qu'elle pourra effectuer 
class Image:
    def __init__(self):
        file_name = input('enter file name: ')
        self.img = pygame.image.load(file_name)
        self.rect = self.img.get_rect()
        self.color = None
        self.width = None
        
    def draw(self):
        screen.blit(self.img, self.rect)
        
    def do_event(self, event):
        if event.type == KEYDOWN:
            print('image keydown')
            
# Pour faire regarder de l'autre côté
            if event.key == K_h:
                print('flip')
                self.img = pygame.transform.flip(self.img, True, False)
                
# Pour faire tourner l'imge de haut en bas
            elif event.key == K_v:
                self.img = pygame.transform.flip(self.img, False, True)
                
# Pour déplacer l'image avec les flèches
            elif event.key in dir:
                self.rect.move_ip(dir[event.key])
                
       
    def load(self):
        self.img = pygame.image.load(file_name)
        self.rect = self.img.get_rect()

objects = [Rectangle()]


while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
    # Pour changer la couleur de fond       
        elif event.type == KEYDOWN:
            if event.key in key_color:
                background = key_color[event.key]
            
        # Pour faire apparaître l'image
            if event.key == K_i:
                print('add image')
                objects.append(Image())
               
        # Pour dessiner un rectangle
            elif event.key == K_r:
                print('add rectangle')
                objects.append(Rectangle())
                
        # Pour dessiner un ovale
            elif event.key == K_e:
                print('add ellipse')
                objects.append(Ellipse())
                            
        # Pour modifier l'épaisseur de l'objet
            elif event.key == K_0:
                objects[-1].width = 0
            elif event.key == K_1:
                objects[-1].width = 1
            elif event.key == K_5:
                objects[-1].width = 5
        
        #  Pour modifier la couleur de l'objet
            elif event.key == K_a:
                objects[-1].color = RED
            elif event.key == K_b:
                objects[-1].color = GREEN
            elif event.key == K_c:
                objects[-1].color = BLUE
            elif event.key == K_d:
                objects[-1].color = YELLOW
            elif event.key == K_f:
                objects[-1].color = MAGENTA
            elif event.key == K_g:
                objects[-1].color = CYAN
            elif event.key == K_j:
                objects[-1].color = BLACK
            elif event.key == K_k:
                objects[-1].color = GRAY
            elif event.key == K_m:
                objects[-1].color = WHITE   
        
        # Pour supprimer le dernier objet edité
            elif event.key == K_BACKSPACE:
                if len(objects) >1:
                    objects.pop()
            
        objects[-1].do_event(event)
            
    screen.fill(background)
    for obj in objects:
        obj.draw()

    pygame.display.update()

pygame.quit()