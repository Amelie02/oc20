from rect import *

rect0 = Rect(50, 60, 100, 80)
rect = rect0.copy()
dir = {K_LEFT: (-5, 0), K_RIGHT: (5, 0), K_UP: (0, -5), K_DOWN: (0, 5)}

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False
        
        if event.type == KEYDOWN:
            if event.key in dir:
                v = dir[event.key]
                rect.move_ip(v)

    screen.fill(BLACK)
    pygame.draw.rect(screen, BLUE, rect0, 4)
    pygame.draw.rect(screen, RED, rect, 8)
    pygame.display.flip()

pygame.quit()