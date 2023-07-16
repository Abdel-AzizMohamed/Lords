import pygame
from MainSetting import *
from UiElements import *


class PyImage(UiDesgin):
    def __init__(self, group, name, url, pos, grab="", frame="", scale=1, prefix="IMG"):
        self.name = f"{prefix}{name}"
        self.group = group

        self.checkInc()
        if not isinstance(url, list):
            self.image = pygame.image.load(url)
        else:
            self.image = pygame.image.load(url[0])
        self.image = pygame.transform.rotozoom(self.image, 0, scale)
        self.attObj = None
        self.setFrame(frame)

        self.rect = super().setGeo((0, 0), pos, grab)
        self.border_rect = super().setGeo((0, 0), pos, grab)
        self.rect.size = self.image.get_rect().size
        self.border_rect.size = self.image.get_rect().size

        self.ren_text, self.rect_text = super().setText(self.rect)
        self.text_align = "center"

        self.active_color = "#FFFFFF"

        self.border_width = 0
        self.border_color = "#000000"
        super().setBorder(self.border_width, self.border_color)

        self.text_margin_x = 0
        self.text_margin_y = 0

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

    def setFrame(self, frame):
        if frame == "":
            self.frame = None
        else:
            self.frame = draw_dict[self.group][frame]
            draw_dict[self.group][frame].children.append(self)

class PyIButton(PyImage):
    def __init__(self, group, name, urls, pos, grab="", frame="", scale=1):
        super().__init__(group, name, urls[0], pos, grab, frame, scale, "IBT")

        self.hover_image = pygame.image.load(urls[1])
        self.select_image = pygame.image.load(urls[2])
        self.disabled_image = pygame.image.load(urls[3])

        self.hover_image = pygame.transform.rotozoom(self.hover_image, 0, scale)
        self.select_image = pygame.transform.rotozoom(self.select_image, 0, scale)
        self.disabled_image = pygame.transform.rotozoom(self.disabled_image, 0, scale)

        self.button_state = self.image

        self.disabled = False
