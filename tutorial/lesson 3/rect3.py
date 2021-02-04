from rect import *

rect = Rect(50, 60, 250, 100)

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

        if event.type == KEYDOWN:
            if event.key == K_l:
                rect.left = 1
            if event.key == K_c:
                rect.centerx = width//2
            if event.key == K_r:
                rect.right = width

            if event.key == K_t:
                rect.top = 1
            if event.key == K_m:
                rect.centery = height//2
            if event.key == K_b:
                rect.bottom = height

    screen.fill(GRAY)
    pygame.draw.rect(screen, MAGENTA, rect)
    pygame.display.flip()

pygame.quit()