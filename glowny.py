import pygame
from board import Board

FPS = 20
SURFACE_W = 1600
SURFACE_H = 900
BOARD_W = 1300
PANEL_W = SURFACE_W - BOARD_W
unit_space = 50

pygame.init()
running = True
pygame.init()
surface = pygame.display.set_mode((SURFACE_W, SURFACE_H))
pygame.display.set_caption("Układ!")
fpsClock = pygame.time.Clock()

board = Board((BOARD_W, SURFACE_H), unit_space, surface)
board.addpoint(1,2,"A")


while running:
    surface.fill((224, 235, 235))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                board.centerY -= board.unit_space
            elif event.key == pygame.K_DOWN:
                board.centerY += board.unit_space
            elif event.key == pygame.K_LEFT:
                board.centerX -= board.unit_space
            elif event.key == pygame.K_RIGHT:
                board.centerX += board.unit_space
            elif event.key == pygame.K_KP_PLUS:
                board.unit_space += 5
            elif event.key == pygame.K_KP_MINUS:
                if board.unit_space > 5:
                    board.unit_space -= 5

    board.draw()

    pygame.draw.line(surface, "black", (SURFACE_W - PANEL_W, 0), (SURFACE_W - PANEL_W, SURFACE_H))

    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()
