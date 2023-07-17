import pygame
from MainSetting import *
from UiElements import *


class PyImage(PyRect):
    def __init__(self, group, name, url, pos, grab="", frame="", scale=1, prefix="IMG"):
        super().__init__(group, name, (0, 0), pos, grab, "IMG", frame)
        self.image = pygame.image.load(url)
        self.image = pygame.transform.rotozoom(self.image, 0, scale)

        self.rect.size = self.image.get_rect().size
        self.border_rect.size = self.image.get_rect().size

class PyIButton(PyRect):
    def __init__(self, group, name, urls, pos, grab="", frame="", scale=1):
        super().__init__(group, name, (0, 0), pos, grab, "IBT", frame)

        self.image = pygame.image.load(url[0])
        self.hover_image = pygame.image.load(urls[1])
        self.select_image = pygame.image.load(urls[2])
        self.disabled_image = pygame.image.load(urls[3])

        self.image = pygame.transform.rotozoom(self.image, 0, scale)
        self.hover_image = pygame.transform.rotozoom(self.hover_image, 0, scale)
        self.select_image = pygame.transform.rotozoom(self.select_image, 0, scale)
        self.disabled_image = pygame.transform.rotozoom(self.disabled_image, 0, scale)

        self.rect.size = self.image.get_rect().size
        self.border_rect.size = self.image.get_rect().size

        self.button_state = self.image

        self.disabled = False
