import pygame
from board import Board
from menu import Menu
import functions as f

FPS = 20
SURFACE_W = 1600
SURFACE_H = 900
BOARD_W = 1300
MENU_W = SURFACE_W - BOARD_W
unit_space = 50

pygame.init()
running = True
pygame.init()
surface = pygame.display.set_mode((SURFACE_W, SURFACE_H))
pygame.display.set_caption("Układ!")
fpsClock = pygame.time.Clock()

# creates board object
board = Board((BOARD_W, SURFACE_H), unit_space, surface)

# creates menu object
menu = Menu(BOARD_W, MENU_W, SURFACE_H, surface)

board.addline(1, +10)
while running:
    surface.fill((224, 235, 235))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYUP:
            # check for scaling or moving inputs
            if event.key == pygame.K_UP:
                board.centerY -= board.unit_space
            elif event.key == pygame.K_DOWN:
                board.centerY += board.unit_space
            elif event.key == pygame.K_LEFT:
                board.centerX -= board.unit_space
            elif event.key == pygame.K_RIGHT:
                board.centerX += board.unit_space
            elif event.key == pygame.K_KP_PLUS or event.key == pygame.K_PAGEUP:
                board.unit_space += 5
            elif event.key == pygame.K_KP_MINUS or event.key == pygame.K_PAGEDOWN:
                if board.unit_space > 5:
                    board.unit_space -= 5
            # check for panel input, if returns add object
            else:
                value = menu.panel.input(event)
                if value:
                    f.addobject(value, board)

        # checks if mouse clicked in the menu area
        if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pos()[0] > BOARD_W:
            # checks if any of the buttons clicked, 0 if not, button_text if yes
            buttonClicked = menu.click()

    # draws the board and all the points, lines etc
    board.draw()

    # draws the menu and the buttons
    menu.draw()

    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()
