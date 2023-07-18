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

class PyIProgress(PyRect):
    def __init__(self, group, name, urls, pos, grab="", frame="", scale=1):
        super().__init__(group, name, (0, 0), pos, grab, "IPR", frame)

        self.bar_image = pygame.image.load(urls[0]).convert_alpha()
        self.fill_image = pygame.image.load(urls[1]).convert_alpha()

        self.bar_image = pygame.transform.rotozoom(self.bar_image, 0, scale)
        self.fill_image = pygame.transform.rotozoom(self.fill_image, 0, scale)

        self.rect.size = self.bar_image.get_rect().size
        self.border_rect.size = self.bar_image.get_rect().size

        self.base_bar_rect = pygame.Rect((self.rect.x, self.rect.y), self.rect.size)
        self.base_bar_color = "#333333"

        self.precent = 0

    def setSlider(self, new_precent):
        self.precent = new_precent
        self.base_bar_rect.width = self.rect.width - (self.rect.width * new_precent)
        self.base_bar_rect.x = self.rect.width * new_precent + self.rect.x
