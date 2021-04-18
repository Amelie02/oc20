import os
import sys
import random
import pygame
from pygame.locals import *

TITRE = "bluisnake"

GREY = (179, 177, 145)
ORANGE = (237, 127, 16)
ROUGE = (255, 0, 0)
VERT = (52, 201, 36)

MIAM_TIME_MS = 250
FPS = 10

def event_loop():
    """Gestion des événements utilisateur."""
    global partieTerminee,dx,dy
    
    for event in pygame.event.get():
        if event.type == KEYUP:
            if event.key == K_ESCAPE:
                if dx == 0 and dy == 0:
                    partieTerminee = True
                else:
                    initialisation_partie()

        elif event.type == KEYDOWN:
            if event.key == K_UP:
                dx=0
                dy=-1
            elif event.key == K_DOWN:
                dx=0
                dy=1
            elif event.key == K_RIGHT:
                dx=1
                dy=0
            elif event.key == K_LEFT:
                dx=-1
                dy=0
                
def update():
    """Mise à jour des éléments du jeu."""
    global score,foodPosition,dx,dy,scoreSurface,miamTimerDebut


    # tous les morceaux du serpent sont mis dans une liste en finissant par la tête
    # en bouclant dans cette liste on attribue à l'index n la valeur de l'index n+1
    # la tête voie ses coordonnées incrémentées du déplacement unitaire par le pas (de déplacement, ici 20)
    # on mémorise la position du premier morceau qui sera la position d'un nouveau si la tête touche la nourriture
    if dx != 0 or dy != 0:
        memPosQueue = snakePosition[0]
        for index in range(len(snakePosition)):
            if index == len(snakePosition)-1:
                snakePosition[index][0] += dx*20
                snakePosition[index][1] += dy*20

            else:
                snakePosition[index] = snakePosition[index+1][:] #<- attention : sans [:] l'attribution affecte l'emplacement mémoire des index de la liste
                                                                 # liste[n] sera bien égal à liste[n+1] mais quand liste[n+2] sera affecté à liste[n+1]
                                                                 # liste[n] aura la valeur de liste[n+2] aussi etc...
                                                                 # tous les index pointeront vers l'emplacement mémoire du dernier index

        # le serpent sort du cadre ou se mord la queue
        if not (0<=snakePosition[-1][0]<500 and 100<=snakePosition[-1][1]<500) or snakePosition[-1] in snakePosition[:-1]:
            dx = 0
            dy = 0
            draw()# on raffraichie l'affichage avant d'afficher le menu game over pour voir le dernier déplacement
            pygame.display.flip()
            game_over()
            return

        # le serpent mange la nourriture
        elif snakePosition[-1] == foodPosition:
            score += 7
            scoreSurface = californiaFont.render("SCORE: "+ str(score), True, (ORANGE))
            snakePosition.insert(0,memPosQueue)
            while True:
                foodPosition = [random.randrange(0, 500, 20), random.randrange(100, 500, 20)]
                if foodPosition not in snakePosition:
                    break
            miamTimerDebut = pygame.time.get_ticks()
                                            
def draw():
    """Redessine tous les éléments du jeu."""
    
    screen.fill((0,0,0))
    # le serpent
    for index in range(len(snakePosition)):
        if index == len(snakePosition)-1:
            pygame.draw.rect(screen, (ORANGE), Rect(snakePosition[index][0],snakePosition[index][1], 20, 20), 2) #<- tête du serpent
        else:
            pygame.draw.rect(screen, (VERT), Rect(snakePosition[index][0],snakePosition[index][1], 20, 20), 2)

    # la nourriture
    pygame.draw.rect(screen, (GREY), Rect(foodPosition[0],foodPosition[1], 20, 20), 2)
    
    pygame.draw.rect(screen, (VERT), Rect(0, 0, 500, 100), 1) # cadre info sup
    pygame.draw.rect(screen, (VERT), Rect(0, 100, 500, 400), 1) # cadre terrain de jeu
    
    screen.blit(scoreSurface,(4,4))
    screen.blit(bestScoreSurface,(4,40))
    screen.blit(cartoonSnake,(240,10))

    if pygame.time.get_ticks() - miamTimerDebut < MIAM_TIME_MS:
        screen.blit(miamSurface,(180,0))

def game_over():
    """Partie terminée."""
    global bestScore,bestScoreSurface,partieTerminee

    if score > int(bestScore):
        fichier = open("best_score2.txt","w")
        fichier.write(str(score))
        fichier.close()
        bestScore = score
        bestScoreSurface = californiaFont.render("Best: " + str(bestScore), True, (ORANGE))
    
    pygame.mouse.set_visible(True)
    
    userChoice = 0
    while not userChoice:
        for event in pygame.event.get():        
            if event.type == KEYUP:
                if event.key == K_ESCAPE:
                    userChoice = 1

            elif event.type == MOUSEBUTTONDOWN and rejouerSurfaceRect.collidepoint(event.pos[0],event.pos[1]):
                userChoice = 2

        screen.blit(gameOverSurface, gameOverSurfaceRect)
        screen.blit(rejouerSurface, rejouerSurfaceRect)

        pygame.display.flip()
        clock.tick(FPS)

    if userChoice == 2:
        initialisation_partie()
    else:
        partieTerminee = True

def display_fps():
    """Montre le taux de FPS."""

    caption = "{} - FPS: {:.0f}/{}".format(TITRE, clock.get_fps(),FPS)
    pygame.display.set_caption(caption)

def initialisation_partie():
    """Remise à l'initiale des variables de jeu."""
    global score,snakePosition,foodPosition,dx,dy,miamTimerDebut,partieTerminee,scoreSurface

    score = 0
    snakePosition = [[0, 280],[0, 260],[0, 240]]
    foodPosition = [240,240]
    dx, dy = 0, 0
    miamTimerDebut = 0    
    partieTerminee = False
    scoreSurface = californiaFont.render("SCORE: "+ str(score), True, (ORANGE))
    pygame.mouse.set_visible(False)
    
def main_loop():
    """Boucle principale."""
    
    initialisation_partie()
    
    while not partieTerminee:
        event_loop()
        update()
        draw()
        pygame.display.flip()
        clock.tick(FPS)
        display_fps()

#--- INITIALISATION JEU ---------------------------------
pygame.init()

screen = pygame.display.set_mode((500, 500))             #<- mode fenêtré
#screen = pygame.display.set_mode((500, 500),FULLSCREEN) #<- mode plein écran

californiaFont = pygame.font.Font("./California.ttf", 32)

cartoonSnake = pygame.image.load("./cartoon_snake.png").convert_alpha()

#----- Variables
partieTerminee = False

snakePosition = [[0, 280],[0, 260],[0, 240]] # coord xy des morceaux du serpent (coin sup gauche), la tête est en dernier
dx, dy = 0, 0 # déplacement unitaire de la tête suivant les 2 axes (dx=-1:gauche dx=1:droite)
score = 0 

foodPosition = [240, 240] # coord de la pomme

miamTimerDebut = 0 # temps de départ de l'apparition du "MIAM". Quand le temps présent moins cette valeur est supérieur à MIAM_TIME_MS, MIAM disparait

#------

clock = pygame.time.Clock()

scoreSurface = californiaFont.render("SCORE: "+ str(score), True, (ORANGE))

miamSurface = californiaFont.render("MIAM!", True, (ORANGE))

gameOverSurface = californiaFont.render("G A M E    O V E R!", True, (ROUGE)) 
gameOverSurfaceRect = gameOverSurface.get_rect(midtop=(500/2, 240))

rejouerSurface = californiaFont.render("PLAY AGAIN", True, (ORANGE)) 
rejouerSurfaceRect = rejouerSurface.get_rect(midtop=(500/2, 320))

#---- Chargement fichier meilleur score
try:
    fichier = open("best_score2.txt","r")
    bestScore = fichier.read()
    bestScoreSurface = californiaFont.render("Best: " + str(bestScore), True, (ORANGE))
    fichier.close()
except:
    bestScore = "0"
    bestScoreSurface = californiaFont.render("Best: " + str(bestScore), True, (ORANGE)) 

#---- Lancement de la boucle principale
main_loop()

pygame.quit()
try:
    sys.exit()
except :
    pass