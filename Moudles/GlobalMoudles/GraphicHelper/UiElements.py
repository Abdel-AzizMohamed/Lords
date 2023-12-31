import pygame
from UiFunctions import *

######################## Main Element ##############################
####################################################################
class PygameBase(UiDesgin):
    def __init__(self, group, name, ui_prifix=""):
        self.name = name
        self.type = ui_prifix
        self.group = group

        self.checkInc()

        self.layer = 1

        draw_dict[group].update({self.name : self})

    def checkInc(self):
        if self.group[0:3] == "INC":
            try:
                inc_dict[self.group]
            except KeyError:
                inc_dict.update({self.group : 0})
            self.name = f"{inc_dict[self.group]}{self.name}"
            inc_dict[self.group] += 1

    def createBorder(self):
        self.border_rect = pygame.Rect((self.rect.x, self.rect.y), self.rect.size)
        self.border_width = 0
        self.border_color = "#FFFFFF"
        super().setBorder(self.border_width, self.border_color)

    def createText(self):
        self.ren_text, self.rect_text = super().setText(self.rect)
        self.text_align = "center"

        self.text_margin_x = 0
        self.text_margin_y = 0


######################## Derived Elements ##############################
########################################################################
######################## Pygame Shapes #################################
class PyRect(PygameBase):
    def __init__(self, group, name, size, pos, grab=""):
        super().__init__(group, name, "")

        self.rect = super().setGeo(size, pos, grab)

        self.active_color = "#FFFFFF"

        super().createBorder()
        super().createText()

class PyCircle(PygameBase):
    def __init__(self, group, name, radius, pos, grab=""):
        super().__init__(group, name, group, "CI")

        self.active_color = "#FFFFFF"
        self.rect = super().setGeo((0, 0), pos, grab)
        self.radius = radius

######################## My Ui Elements ##############################
class PyButton(PygameBase):
    def __init__(self, group, name, size, pos, grab=""):
        super().__init__(group, name, "BT")

        self.rect = super().setGeo(size, pos, grab)

        self.base_color = "#FFFFFF"
        self.active_color = self.base_color
        self.hover_color = "#999999"
        self.select_color = "#666666"
        self.disabled_color = "#333333"

        super().createBorder()
        super().createText()

        self.disabled = False

class PyInput(PygameBase):
    def __init__(self, group, name, width, pos, grab=""):
        super().__init__(group, name, "IN")

        self.rect = super().setGeo((width, 1), pos, grab)
        super().createBorder()

        self.text = ""

class PyProgressBar(PygameBase):
    def __init__(self, group, name, width, pos, grab="", ui_prifix="PR"):
        super().__init__(group, name, ui_prifix)

        self.bar = super().setGeo((width, 1), pos, grab)
        self.bar_fill = super().setGeo((width, 1), pos, grab)

        self.start_pos = self.rect.centerx - self.rect.width / 2
        self.end_pos = self.rect.centerx + self.rect.width / 2
        self.precent = 0

        self.bar_color = "#FFF000"
        self.bar_fill_color = "#333333"

        self.disabled = False

        super().createBorder()
        super().createText()

    def setSlider(self, new_precent):
        self.precent = new_precent
        self.bar_fill_rect.width = self.handle_rect.x - self.start_pos

class PySlider(PyProgressBar):
    def __init__(self, group, name, width, pos, grab=""):
        super().__init__(group, name, width, pos, grab, "SL")

        self.handle_rect = super().setGeo((1, 1), pos, grab)

        self.handle_color = "#FFFFFF"

    def setSlider(self, new_precent):
        self.precent = new_precent
        self.handle_rect.x = self.start_pos + (self.rect.width * self.precent)
        self.bar_fill_rect.width = self.handle_rect.x - self.start_pos

# class PyFrame(PyRect):
#     def __init__(self, group, name, size, pos, grab):
#         super().__init__(group, name, size, pos, grab, "FR")

#         self.children = []

#     def moveChildren(self, x, y):
#         for child in self.children:
#             child.addMargin(x, y)

class PyMultiArea(PygameBase):
    def __init__(self, group, name, size, pos, grab, lines, line_height):
        super().__init__(group, name, "MA")

        self.rect = super().setGeo(size, pos, grab)

        self.line_height = line_height
        self.text_elements = []
        self.text_list = ["", "", "", ""]

        self.createTextFields(size, pos, grab, lines)

    def createTextFields(self, size, pos, grab, lines):
        for ele in range(lines):
            new_obj = PyRect(self.group, f"{self.name}_text{ele + 1}", (1, 1), (pos[0], pos[1] + 1), grab)

            if not len(self.text_elements):
                new_obj.addMargin(0, self.line_height)
            else:
                if self.line_height > 0:
                    new_obj.rect.y = self.text_elements[ele - 1].rect.y + (self.text_elements[ele - 1].rect.height)
                else:
                    new_obj.rect.y = self.text_elements[ele - 1].rect.y - (self.text_elements[ele - 1].rect.height)
                new_obj.addMargin(0, self.line_height)

            new_obj.opacity = 0
            self.text_elements.append(new_obj)

    def setText(self, text):
        text_split = text.split(" ")

        for ele in self.text_elements:
            ele.updateText(sm_mid_font, "", "#FFFFFF", "left")

        current_length = 0
        current_str = ""
        ele_index = 0
        current_ele = self.text_elements[ele_index]

        for word in text_split:
            current_length += len(word) + 1

            if current_length > self.line_width and ele_index < len(self.text_elements) - 1:
                current_ele.updateText(sm_mid_font, current_str, "#FFFFFF", "left")
                ele_index += 1
                current_ele = self.text_elements[ele_index]
                current_length = 0
                current_str = ""

            current_str += word
            current_str += " "
        current_ele.updateText(sm_mid_font, current_str, "#FFFFFF", "left")

    def addQueue(self, text):
        for i in range(0, len(self.text_list) - 1):
            self.text_list[-1 - i] = self.text_list[-1 - i - 1]
        self.text_list[0] = text

        for ele in range(len(self.text_elements)):
            self.text_elements[ele].updateText(sm_mid_font, self.text_list[ele], "#FFFFFF", "left")
