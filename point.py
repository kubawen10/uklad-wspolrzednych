import pygame




class Point:
    show = False

    def __init__(self, x, y, name):
        self.x = x
        self.y = y
        self.name = name

    def draw(self, centerx, centery, space, surface):
        pygame.draw.circle(surface, "black", (centerx + self.x * space, centery - self.y * space), space / 10)
        if Point.show:
            print(f"{self.name} = ({self.x}, {self.y})")
