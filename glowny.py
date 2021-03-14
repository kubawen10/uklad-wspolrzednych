import pygame


FPS = 20
SURFACE_W = 1600
SURFACE_H = 900
BOARD_W = 1300
PANEL_W = SURFACE_W - BOARD_W

pygame.init()
running = True #na czas nauki tkinter
pygame.init()
surface = pygame.display.set_mode((SURFACE_W, SURFACE_H))
pygame.display.set_caption("Układ!")
fpsClock = pygame.time.Clock()



while running:
    surface.fill("black")
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.line(surface, "white", (SURFACE_W - PANEL_W, 0), (SURFACE_W- PANEL_W, SURFACE_H))

    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()
