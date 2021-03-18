import pygame
from board import Board
from menu import Menu

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


while running:
    surface.fill((224, 235, 235))

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            running = False

        # checks if user wants to move the board or scale it (arrows and numpad + -)
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

            else:
                value = menu.panel.input(event)
                if value:
                    value = list(value)
                    if value[-1] == "Point":
                        x = float(value[0])
                        y = float(value[1])
                        name = value[2]
                        if int(x) == x:
                            x=int(x)
                        if int(y) == y:
                            y = int(y)
                        board.addpoint(x, y, name)
                    elif value[-1] == "Circle":
                        x = float(value[0])
                        y = float(value[1])
                        r = float(value[2])
                        name = value[3]
                        if int(x) == x:
                            x = int(x)
                        if int(y) == y:
                            y = int(y)
                        if int(r) == r:
                            r = int(r)
                        board.addcircle(x, y, r, name)



        # checks if mouse clicked in the menu area
        if event.type == pygame.MOUSEBUTTONUP and pygame.mouse.get_pos()[0] > BOARD_W:
            # checks if any of the buttons clicked, 0 if not, button_text if yes
            buttonClicked = menu.click()
            if buttonClicked != 0:
                print(buttonClicked)

    # draws the board and all the points, lines etc
    board.draw()

    # draws the menu and the buttons
    menu.draw()

    pygame.display.update()
    fpsClock.tick(FPS)

pygame.quit()
