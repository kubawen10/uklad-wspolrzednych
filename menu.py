import pygame


class Button:
    active_btt = 0  # currently clicked button

    def __init__(self, rect, text, color_active, color_inactive, surface):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.color_active = color_active
        self.color_inactive = color_inactive
        self.font = pygame.font.SysFont("comicsansms", 30)
        self.surface = surface
        self.mousehover = False     # checks if mouse is on the button

    # draws the button with a right color
    def draw(self):
        mpos = pygame.mouse.get_pos()
        self.mousehover = self.rect.collidepoint(mpos)

        if self.mousehover or self.text == Button.active_btt:
            pygame.draw.rect(self.surface, self.color_active, self.rect)
        else:
            pygame.draw.rect(self.surface, self.color_inactive, self.rect)

        msg = self.font.render(self.text, True, (0, 0, 0))
        self.surface.blit(msg, msg.get_rect(center=self.rect.center))

    # changes a currently clicked button
    def clicked(self):
        mpos = pygame.mouse.get_pos()

        if self.rect.collidepoint(mpos):
            if Button.active_btt == self.text:
                Button.active_btt = 0
                return False
            else:
                Button.active_btt = self.text
                return True

        return False

# calculates next button's y
def btty(len, height):
    if len==0:
        return 20 + len * height
    return 20 + len * height + 1


class Menu:
    def __init__(self, x, width, surface):
        self.x = x          # x position of the menu, just after the board
        self.width = width  # width of the menu, from x to windows width
        self.surface = surface
        self.buttons = []   # button array

        COLOR_INACTIVE = (100, 80, 255)     # color of not active button
        COLOR_ACTIVE = (100, 200, 255)      # color of active button, mousehover or clicked
        BUTTON_WIDTH = 200
        BUTTON_HEIGHT = 50
        buttonx = x + (width - BUTTON_WIDTH) / 2            # centers the button in the menu

        # adding new buttons
        buttony = btty(len(self.buttons), BUTTON_HEIGHT)     # button y based on the amount of buttons
        pointbutton = Button((buttonx, buttony, BUTTON_WIDTH, BUTTON_HEIGHT), "Point", COLOR_ACTIVE, COLOR_INACTIVE, self.surface)
        self.buttons.append(pointbutton)

        buttony = btty(len(self.buttons), BUTTON_HEIGHT)
        circlebutton = Button((buttonx, buttony, BUTTON_WIDTH, BUTTON_HEIGHT), "Circle", COLOR_ACTIVE, COLOR_INACTIVE, self.surface)
        self.buttons.append(circlebutton)

    # draws buttons
    def draw(self):
        for button in self.buttons:
            button.draw()

    # checks if any of the buttons was pressed, returns the name of this button, if not returns 0
    def click(self):
        for button in self.buttons:
            if button.clicked():
                return Button.active_btt
        Button.active_btt = 0
        return 0
