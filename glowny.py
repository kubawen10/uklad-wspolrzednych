import pygame
from board import Board

FPS = 20
SURFACE_W = 1600
SURFACE_H = 900
BOARD_W = 1300
PANEL_W = SURFACE_W - BOARD_W

pygame.init()
running = True
pygame.init()
surface = pygame.display.set_mode((SURFACE_W, SURFACE_H))
pygame.display.set_caption("Układ!")
fpsClock = pygame.time.Clock()

board = Board((BOARD_W / 2, SURFACE_H / 2), 50, surface)

while running:
    surface.fill((224, 235, 235))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    board.draw()


    pygame.draw.line(surface, "black", (SURFACE_W - PANEL_W, 0), (SURFACE_W - PANEL_W, SURFACE_H))

    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()
