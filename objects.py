import pygame


class Point:
    show = True

    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name
        if Point.show:
            print(f"{self.name} = ({self.x}, {self.y})")

    def draw(self, centerx, centery, space, surface):
        pygame.draw.circle(surface, "black", (centerx + self.x * space, centery - self.y * space), space / 10)

class Circle:
    def __init__(self, x, y, r, name):
        self.x = x
        self.y = y
        self.r = r
        self.name = name
        if Point.show:
            print(f"{self.name} = ({self.x}, {self.y}), r = {self.r}")

    def draw(self, centerx, centery, space, surface):
        pygame.draw.circle(surface, "black", (centerx + self.x * space, centery - self.y * space), space / 10)
        pygame.draw.circle(surface, "black", (centerx + self.x * space, centery - self.y * space), self.r * space+space/24, space//12)

class Line:
    def __init__(self, a, b, name, board_w, board_h):
        self.a = a
        self.b = b
        self.name = name
        self.board_w = board_w
        self.board_h = board_h
        if Point.show:
            print(f"{self.name}: y = {self.a}x + {self.b}")

    def draw(self, centerx, centery, space, surface):
        if self.a == 0:
            pygame.draw.line(surface, "black", (0, centery - self.b * space), (self.board_w, centery - self.b * space), width=space//15)
        else:
            y_top = centery // space
            y_bottom = (self.board_h-centery)//space
            print(y_top, y_bottom)
            x=(y_top-self.b)/self.a
            print(x)
            # ogarnac linie!




