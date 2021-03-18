import pygame


# calculates next button's y
def btty(len, height):
    if len == 0:
        return 20 + len * height
    return 20 + len * height + 1


def get_unspecified_value(dict):
    for key, value in dict.items():
        if value == None:
            return key
    return "Done"


class Panel:
    def __init__(self, x, width, win_height, surface):
        self.x = x
        self.width = width
        self.y = win_height - 100
        self.surface = surface
        self.mode = Button.active_btt
        self.font = pygame.font.SysFont("comicsansms", 30)
        self.cur_input = ""

    def draw(self):
        pygame.draw.line(self.surface, "black", (self.x, self.y), (self.x + self.width, self.y))

    def input(self, event):
        pass


class Point_panel(Panel):
    def __init__(self, x, width, win_height, surface):
        super().__init__(x, width, win_height, surface)
        self.msg = "pointName = (x, y)"
        self.var = {"x = ": None, "y = ": None, "name = ": None}
        self.cur_var = get_unspecified_value(self.var)

    def draw(self):
        pygame.draw.line(self.surface, "black", (self.x, self.y), (self.x + self.width, self.y))
        title = self.font.render(self.msg, True, (0, 0, 0))
        self.surface.blit(title, (self.x, self.y))

        input_text = self.font.render(self.cur_var + self.cur_input, True, (0, 0, 0))
        self.surface.blit(input_text, (self.x, self.y + 30))

    def input(self, event):
        numpad_keys = ("[0]", "[1]", "[2]", "[3]", "[4]", "[5]", "[6]", "[7]", "[8]", "[9]", "[.]")
        num_keys = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "-")
        if self.cur_var != "Done":
            key_pressed = pygame.key.name(event.key)
            print(key_pressed)
            if key_pressed in numpad_keys:
                key_pressed = key_pressed[1]
                self.cur_input += key_pressed
            elif self.cur_var != "name = " and key_pressed in num_keys:
                if key_pressed == "-" and len(self.cur_input) == 0:
                    self.cur_input += key_pressed
                elif key_pressed != "-":
                    self.cur_input += key_pressed
            elif key_pressed == "backspace":
                self.cur_input = self.cur_input[:-1]
            elif self.cur_var == "name = " and len(key_pressed) == 1:
                self.cur_input += key_pressed.upper()

            elif key_pressed == "return" or key_pressed == "enter":
                self.var[self.cur_var] = self.cur_input
                self.cur_var = get_unspecified_value(self.var)
                self.cur_input = ""
                if self.cur_var=="Done":
                    Button.active_btt = 0
                    self.var["type"] = "Point"
                    return self.var.values()
        return False




class Circle_panel(Panel):
    def __init__(self, x, width, win_height, surface):
        super().__init__(x, width, win_height, surface)
        self.msg = "S = (x, y), r="
        self.var = {"x = ": None, "y= ": None, "r = ": None, "name =": None}
        self.cur_var = get_unspecified_value(self.var)

    def draw(self):
        pygame.draw.line(self.surface, "black", (self.x, self.y), (self.x + self.width, self.y))
        title = self.font.render(self.msg, True, (0, 0, 0))
        self.surface.blit(title, (self.x, self.y))

        input_text = self.font.render(self.cur_var + self.cur_input, True, (0, 0, 0))
        self.surface.blit(input_text, (self.x, self.y + 30))

    def input(self, event):
        numpad_keys = ("[0]", "[1]", "[2]", "[3]", "[4]", "[5]", "[6]", "[7]", "[8]", "[9]", "[.]")
        num_keys = ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", ".", "-")
        if self.cur_var != "Done":
            key_pressed = pygame.key.name(event.key)
            print(key_pressed)
            if key_pressed in numpad_keys:
                key_pressed = key_pressed[1]
                self.cur_input += key_pressed
            elif self.cur_var != "name = " and key_pressed in num_keys:
                if key_pressed == "-" and len(self.cur_input) == 0:
                    self.cur_input += key_pressed
                elif key_pressed != "-":
                    self.cur_input += key_pressed
            elif key_pressed == "backspace":
                self.cur_input = self.cur_input[:-1]
            elif self.cur_var == "name = " and len(key_pressed) == 1:
                self.cur_input += key_pressed.upper()

            elif key_pressed == "return" or key_pressed == "enter":
                self.var[self.cur_var] = self.cur_input
                self.cur_var = get_unspecified_value(self.var)
                self.cur_input = ""
                if self.cur_var == "Done":
                    Button.active_btt = 0
                    self.var["type"] = "Circle"
                    return self.var.values()
        return False


class Button:
    active_btt = 0  # currently clicked button

    def __init__(self, rect, text, color_active, color_inactive, surface):
        self.rect = pygame.Rect(rect)
        self.text = text
        self.color_active = color_active
        self.color_inactive = color_inactive
        self.font = pygame.font.SysFont("comicsansms", 30)
        self.surface = surface
        self.mousehover = False  # checks if mouse is on the button

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


def createPanel(x, width, height, surface):
    act = Button.active_btt
    if act == "Point":
        return Point_panel(x, width, height, surface)
    if act == "Circle":
        return Circle_panel(x, width, height, surface)


class Menu:
    def __init__(self, x, width, height, surface):
        self.x = x  # x position of the menu, just after the board
        self.width = width  # width of the menu, from x to windows width
        self.surface = surface
        self.height = height
        self.buttons = []  # button array
        self.panel = Panel(x, width, height, surface)

        COLOR_INACTIVE = (100, 80, 255)  # color of not active button
        COLOR_ACTIVE = (100, 200, 255)  # color of active button, mousehover or clicked
        BUTTON_WIDTH = 200
        BUTTON_HEIGHT = 50
        buttonx = x + (width - BUTTON_WIDTH) / 2  # centers the button in the menu

        # adding new buttons
        buttony = btty(len(self.buttons), BUTTON_HEIGHT)  # button y based on the amount of buttons
        pointbutton = Button((buttonx, buttony, BUTTON_WIDTH, BUTTON_HEIGHT), "Point", COLOR_ACTIVE, COLOR_INACTIVE,
                             self.surface)
        self.buttons.append(pointbutton)

        buttony = btty(len(self.buttons), BUTTON_HEIGHT)
        circlebutton = Button((buttonx, buttony, BUTTON_WIDTH, BUTTON_HEIGHT), "Circle", COLOR_ACTIVE, COLOR_INACTIVE,
                              self.surface)
        self.buttons.append(circlebutton)

    # draws buttons and panel
    def draw(self):
        pygame.draw.line(self.surface, "black", (self.x, 0), (self.x, self.height))

        for button in self.buttons:
            button.draw()
        self.panel.draw()

    # checks if any of the buttons was pressed, returns the name of this button, if not returns 0
    def click(self):
        for button in self.buttons:
            if button.clicked():
                self.panel = createPanel(self.x, self.width, self.height, self.surface)
                return Button.active_btt
        self.panel = Panel(self.x, self.width, self.height, self.surface)
        Button.active_btt = 0
        return 0
