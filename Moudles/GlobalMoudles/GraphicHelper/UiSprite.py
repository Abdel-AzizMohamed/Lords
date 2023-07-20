import pygame
from MainSetting import *
from UiElements import *


class PyImage(PyRect):
    def __init__(self, group, name, url, pos, grab="", frame="", scale=1, prefix="IMG"):
        super().__init__(group, name, (0, 0), pos, grab, "IMG", frame)
        self.image = pygame.image.load(url).convert_alpha()
        self.image = pygame.transform.rotozoom(self.image, 0, scale)

        self.rect.size = self.image.get_rect().size
        self.border_rect.size = self.image.get_rect().size

class PyIButton(PyRect):
    def __init__(self, group, name, urls, pos, grab="", frame="", scale=1):
        super().__init__(group, name, (0, 0), pos, grab, "IBT", frame)

        self.image = pygame.image.load(urls[0]).convert_alpha()
        self.hover_image = pygame.image.load(urls[1]).convert_alpha()
        self.select_image = pygame.image.load(urls[2]).convert_alpha()
        self.disabled_image = pygame.image.load(urls[3]).convert_alpha()

        self.image = pygame.transform.rotozoom(self.image, 0, scale)
        self.hover_image = pygame.transform.rotozoom(self.hover_image, 0, scale)
        self.select_image = pygame.transform.rotozoom(self.select_image, 0, scale)
        self.disabled_image = pygame.transform.rotozoom(self.disabled_image, 0, scale)

        self.rect.size = self.image.get_rect().size
        self.border_rect.size = self.image.get_rect().size

        self.button_state = self.image

        self.disabled = False

class PyIInput(PyRect):
    def __init__(self, group, name, urls, pos, grab="", frame="", scale=1):
        super().__init__(group, name, (0, 0), pos, grab, "IIN", frame)

        self.border_image = pygame.image.load(urls["border"]).convert_alpha()
        self.focus_image = pygame.image.load(urls["focus"]).convert_alpha()
        self.field_image = pygame.image.load(urls["field"]).convert_alpha()

        self.border_image = pygame.transform.rotozoom(self.border_image, 0, scale)
        self.focus_image = pygame.transform.rotozoom(self.focus_image, 0, scale)
        self.field_image = pygame.transform.rotozoom(self.field_image, 0, scale)

        self.rect.size = self.field_image.get_rect().size
        self.border_rect.size = self.field_image.get_rect().size

        self.text = ""
        self.input_state = self.border_image

class PyIProgress(PyRect):
    def __init__(self, group, name, urls, pos, grab="", frame="", scale=1, uiPrifix="IPR"):
        super().__init__(group, name, (0, 0), pos, grab, uiPrifix, frame)

        self.bar_image = pygame.image.load(urls["bar"]).convert_alpha()
        self.fill_image = pygame.image.load(urls["fill"]).convert_alpha()

        self.bar_image = pygame.transform.rotozoom(self.bar_image, 0, scale)
        self.fill_image = pygame.transform.rotozoom(self.fill_image, 0, scale)

        self.rect.size = self.bar_image.get_rect().size
        self.border_rect.size = self.bar_image.get_rect().size

        self.base_bar_rect = pygame.Rect((self.rect.x, self.rect.y), self.rect.size)
        self.base_bar_color = "#333333"


        self.start_pos = self.rect.centerx - self.rect.width / 2
        self.end_pos = self.rect.centerx + self.rect.width / 2
        self.precent = 0

    def setSlider(self, new_precent):
        self.precent = new_precent
        self.base_bar_rect.width = self.rect.width - (self.rect.width * new_precent)
        self.base_bar_rect.x = self.rect.width * new_precent + self.rect.x

class PyISlider(PyIProgress):
    def __init__(self, group, name, urls, pos, grab="", frame="", scale=1):
        super().__init__(group, name, urls, pos, grab, frame, scale, "ISL")

        self.handle_image = pygame.image.load(urls["handle"]).convert_alpha()
        self.handle_hover_image = pygame.image.load(urls["hover"]).convert_alpha()
        self.handle_select_image = pygame.image.load(urls["select"]).convert_alpha()

        self.handle_image = pygame.transform.rotozoom(self.handle_image, 0, scale)
        self.handle_hover_image = pygame.transform.rotozoom(self.handle_hover_image, 0, scale)
        self.handle_select_image = pygame.transform.rotozoom(self.handle_select_image, 0, scale)

        self.handle_rect = self.handle_image.get_rect()
        self.handle_rect.center = self.rect.center
        self.handle_rect.y += 2

        self.handle_state = self.handle_image

    def setSlider(self, new_precent):
        self.precent = new_precent
        self.handle_rect.x = self.rect.x + (self.rect.width * self.precent) - self.handle_rect.width
        self.base_bar_rect.width = self.rect.width - (self.rect.width * new_precent)
        self.base_bar_rect.x = self.rect.width * new_precent + self.rect.x
