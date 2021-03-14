import pygame


def draw_main_lines(centerx, centery, surface):
    # draws main lines of the board
    # vertical
    pygame.draw.line(surface, "black", (centerx, centery - centery + 5), (centerx, centery + centery - 5), 3)
    # horizontal
    pygame.draw.line(surface, "Black", (centerx - centerx + 5, centery), (centerx + centerx - 5, centery), 3)


def draw_helpful_lines(centerx, centery, space, surface):
    # draw vertical lines
    ammount = int(centerx // space) + 1
    for i in range(1, ammount):
        pygame.draw.line(surface, "grey", (centerx + i * space, centery - centery + 5),
                         (centerx + i * space, centery + centery - 5))
        pygame.draw.line(surface, "grey", (centerx - i * space, centery - centery + 5),
                         (centerx - i * space, centery + centery - 5))

    # draw horizontal lines
    ammount = int(centery // space) + 1
    for i in range(1, ammount):
        pygame.draw.line(surface, "grey", (centerx - centerx + 5, centery + i * space),
                         (centerx + centerx - 5, centery + i * space))
        pygame.draw.line(surface, "grey", (centerx - centerx + 5, centery - i * space),
                         (centerx + centerx - 5, centery - i * space))


class Board:
    def __init__(self, center, unit_space, surface):
        self.centerX = center[0]
        self.centerY = center[1]
        self.unit_space = unit_space
        self.surface = surface

    def draw(self):
        draw_helpful_lines(self.centerX, self.centerY, self.unit_space, self.surface)
        draw_main_lines(self.centerX, self.centerY, self.surface)

