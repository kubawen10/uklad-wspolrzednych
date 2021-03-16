import pygame


def draw_main_lines(centerx, centery, board_w, board_h, surface):
    # draws main lines of the board
    # vertical
    pygame.draw.line(surface, "black", (centerx, centery - centery + 5), (centerx, board_h - 5), 3)
    # horizontal
    pygame.draw.line(surface, "Black", (centerx - centerx + 5, centery), (board_w - 5, centery), 3)


def draw_helpful_lines(centerx, centery, board_w, board_h, space, surface):
    # draw vertical lines to the right from the y axis
    amount = int((board_w - centerx) // space) + 1
    for i in range(1, amount):

        if (centerx + i * space) > 0:  # draws only visible lines
            pygame.draw.line(surface, "grey", (centerx + i * space, centery - centery + 5),
                             (centerx + i * space, board_h - 5))

    # draw vertical lines to the left from the y axis
    amount = int(centerx // space) + 1
    for i in range(1, amount):
        pygame.draw.line(surface, "grey", (centerx - i * space, centery - centery + 5),
                         (centerx - i * space, board_h - 5))

    # draw horizontal lines above x axis
    amount = int(centery // space) + 1
    for i in range(1, amount):
        pygame.draw.line(surface, "grey", (centerx - centerx + 5, centery - i * space),
                         (board_w - 5, centery - i * space))

    # draw horizontal lines under x axis
    amount = int((board_h - centery) // space) + 1
    for i in range(1, amount):
        pygame.draw.line(surface, "grey", (centerx - centerx + 5, centery + i * space),
                         (board_w - 5, centery + i * space))


class Board:
    def __init__(self, center, unit_space, surface):
        self.board_w = center[0]  # board width
        self.board_h = center[1]  # board height
        self.centerX = self.board_w / 2  # center X of main lines
        self.centerY = self.board_h / 2  # center Y of main lines
        self.unit_space = unit_space  # space between units
        self.surface = surface

    def draw(self):
        draw_helpful_lines(self.centerX, self.centerY, self.board_w, self.board_h, self.unit_space, self.surface)
        draw_main_lines(self.centerX, self.centerY, self.board_w, self.board_h, self.surface)
