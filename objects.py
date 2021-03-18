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



