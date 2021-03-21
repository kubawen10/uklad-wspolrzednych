import pygame
import objects

pointNames = ("A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "P", "Q", "R", "S", "T")
circleNames = ("O", "O2", "O3", "O4", "O5", "O6")
lineNames = ("k", "l", "m", "n", "p", "q", "t")

# draws X axis and Y axis
def draw_main_lines(centerx, centery, board_w, board_h, surface):
    # draws main lines of the board
    if centerx<board_w:
        # vertical
        pygame.draw.line(surface, "black", (centerx, centery - centery + 5), (centerx, board_h - 5), 5)
    # horizontal
    pygame.draw.line(surface, "Black", (centerx - centerx + 5, centery), (board_w - 5, centery), 5)

# draws unit lines
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
        if centerx - i * space <= board_w:
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

# checks for used point names and picks first available
def getfreename_points(points):
    namesused = []
    for point in points:
        namesused.append(point.name)

    for name in pointNames:
        if name not in namesused:
            return name

def getfreename_circles(circles):
    namesused = []
    for circle in circles:
        namesused.append(circle.name)

    for name in circleNames:
        if name not in namesused:
            return name

def getfreename_line(lines):
    namesused=[]
    for line in lines:
        namesused.append(line.name)

    for name in lineNames:
        if name not in namesused:
            return name


class Board:
    def __init__(self, center, unit_space, surface):
        self.board_w = center[0]  # board width
        self.board_h = center[1]  # board height
        self.centerX = self.board_w / 2  # center X of main lines
        self.centerY = self.board_h / 2  # center Y of main lines
        self.unit_space = unit_space  # space between units
        self.surface = surface
        self.points = []    # array of points
        self.circles = []
        self.lines = []

    # draws the lines and points
    def draw(self):
        draw_helpful_lines(self.centerX, self.centerY, self.board_w, self.board_h, self.unit_space, self.surface)
        draw_main_lines(self.centerX, self.centerY, self.board_w, self.board_h, self.surface)
        for point in self.points:
            point.draw(self.centerX, self.centerY, self.unit_space, self.surface)
        for circle in self.circles:
            circle.draw(self.centerX, self.centerY, self.unit_space, self.surface)
        for line in self.lines:
            line.draw(self.centerX, self.centerY, self.unit_space, self.surface)

    # adds point (point_x, point_y, name), if name is not specified picks a first free letter
    def addpoint(self, x, y, name=""):
        if name == "":
            name = getfreename_points(self.points)
        self.points.append(objects.Point(x, y, name))

    def addcircle(self, x, y, r, name=""):
        if name == "":
            name = getfreename_circles(self.circles)
        self.circles.append((objects.Circle(x, y, r, name)))

    def addline(self, a, b, name=""):
        if name == "":
            name = getfreename_line(self.lines)
        self.lines.append(objects.Line(a, b, name, self.board_w, self.board_h))



