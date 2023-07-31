import pygame
from MainSetting import *
from UiElements import *



class PyImageBase(PygameBase):
    image_list = {}
    def __init__(self, group, name, ui_prifix):
        super().__init__(group, name, ui_prifix)


    @staticmethod
    def loadImages(path):
        images = os.listdir(path)

        for image in images:
            if image.find(".jpg") != -1:
                loaded_image = pygame.image.load(f"{path}/{image}").convert()
                image_name = image[:-4]
                PyImageBase.image_list.update({image_name: loaded_image})
            elif image.find(".png") != -1:
                loaded_image = pygame.image.load(f"{path}/{image}").convert_alpha()
                image_name = image[:-4]
                PyImageBase.image_list.update({image_name: loaded_image})
            else:
                raise TypeError("Engine only support 2 types (jpg, png)")


class PyImage(PyImageBase):
    def __init__(self, group, name, url, pos, grab="", scale=1):
        super().__init__(group, name, "IMG")

        self.image = PyImageBase.image_list[url]

        self.image = pygame.transform.scale(self.image, (width_ratio * self.image.get_width(), height_ratio * self.image.get_height()))
        self.image = pygame.transform.rotozoom(self.image, 0, scale)

        self.rect = super().setGeo((0, 0), pos, grab)
        self.rect.size = self.image.get_rect().size

        super().createText()

class PyIButton(PygameBase):
    def __init__(self, group, name, urls, pos, grab="", scale=1):
        super().__init__(group, name, "IBT")

        self.image = PyImageBase.image_list[urls["normal"]]
        self.hover_image = PyImageBase.image_list[urls["hover"]]
        self.select_image = PyImageBase.image_list[urls["select"]]
        self.disabled_image = PyImageBase.image_list[urls["disabled"]]

        self.image = pygame.transform.scale(self.image, (width_ratio * self.image.get_width(), height_ratio * self.image.get_height()))
        self.hover_image = pygame.transform.scale(self.hover_image, (width_ratio * self.hover_image.get_width(), height_ratio * self.hover_image.get_height()))
        self.select_image = pygame.transform.scale(self.select_image, (width_ratio * self.select_image.get_width(), height_ratio * self.select_image.get_height()))
        self.disabled_image = pygame.transform.scale(self.disabled_image, (width_ratio * self.disabled_image.get_width(), height_ratio * self.disabled_image.get_height()))

        self.image = pygame.transform.rotozoom(self.image, 0, scale)
        self.hover_image = pygame.transform.rotozoom(self.hover_image, 0, scale)
        self.select_image = pygame.transform.rotozoom(self.select_image, 0, scale)
        self.disabled_image = pygame.transform.rotozoom(self.disabled_image, 0, scale)

        self.rect = super().setGeo((0, 0), pos, grab)
        self.rect.size = self.image.get_rect().size

        super().createText()

        self.button_state = self.image

        self.disabled = False


class PyIInput(PygameBase):
    def __init__(self, group, name, urls, pos, grab="", scale=1):
        super().__init__(group, name, "IIN")

        self.border_image = PyImageBase.image_list[urls["border"]]
        self.focus_image = PyImageBase.image_list[urls["focus"]]
        self.field_image = PyImageBase.image_list[urls["field"]]

        self.border_image = pygame.transform.scale(self.border_image, (width_ratio * self.border_image.get_width(), height_ratio * self.border_image.get_height()))
        self.focus_image = pygame.transform.scale(self.focus_image, (width_ratio * self.focus_image.get_width(), height_ratio * self.focus_image.get_height()))
        self.field_image = pygame.transform.scale(self.field_image, (width_ratio * self.field_image.get_width(), height_ratio * self.field_image.get_height()))

        self.border_image = pygame.transform.rotozoom(self.border_image, 0, scale)
        self.focus_image = pygame.transform.rotozoom(self.focus_image, 0, scale)
        self.field_image = pygame.transform.rotozoom(self.field_image, 0, scale)

        self.rect = super().setGeo((0, 0), pos, grab)
        self.rect.size = self.field_image.get_rect().size

        super().createText()

        self.text = ""
        self.input_state = self.border_image


class PyIProgress(PygameBase):
    def __init__(self, group, name, urls, pos, grab="", scale=1, ui_prifix="IPR"):
        super().__init__(group, name, ui_prifix)

        self.bar_image = PyImageBase.image_list[urls["bar"]]
        self.fill_image = PyImageBase.image_list[urls["fill"]]

        self.bar_image = pygame.transform.scale(self.bar_image, (width_ratio * self.bar_image.get_width(), height_ratio * self.bar_image.get_height()))
        self.fill_image = pygame.transform.scale(self.fill_image, (width_ratio * self.fill_image.get_width(), height_ratio * self.fill_image.get_height()))

        self.bar_image = pygame.transform.rotozoom(self.bar_image, 0, scale)
        self.fill_image = pygame.transform.rotozoom(self.fill_image, 0, scale)

        self.rect = super().setGeo((0, 0), pos, grab)
        self.rect.size = self.bar_image.get_rect().size

        super().createText()

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
    def __init__(self, group, name, urls, pos, grab="", scale=1):
        super().__init__(group, name, urls, pos, grab, scale, "ISL")

        self.handle_image = PyImageBase.image_list[urls["handle"]]
        self.handle_hover_image = PyImageBase.image_list[urls["hover"]]
        self.handle_select_image = PyImageBase.image_list[urls["select"]]

        self.handle_image = pygame.transform.scale(self.handle_image, (width_ratio * self.handle_image.get_width(), height_ratio * self.handle_image.get_height()))
        self.handle_hover_image = pygame.transform.scale(self.handle_hover_image, (width_ratio * self.handle_hover_image.get_width(), height_ratio * self.handle_hover_image.get_height()))
        self.handle_select_image = pygame.transform.scale(self.handle_select_image, (width_ratio * self.handle_select_image.get_width(), height_ratio * self.handle_select_image.get_height()))

        self.handle_image = pygame.transform.rotozoom(self.handle_image, 0, scale)
        self.handle_hover_image = pygame.transform.rotozoom(self.handle_hover_image, 0, scale)
        self.handle_select_image = pygame.transform.rotozoom(self.handle_select_image, 0, scale)

        self.handle_rect = self.handle_image.get_rect()
        self.handle_rect.center = self.rect.center
        self.handle_rect.y += 2

        super().createText()

        self.handle_state = self.handle_image

    def setSlider(self, new_precent):
        self.precent = new_precent
        self.handle_rect.x = self.rect.x + (self.rect.width * self.precent) - self.handle_rect.width
        self.base_bar_rect.width = self.rect.width - (self.rect.width * new_precent)
        self.base_bar_rect.x = self.rect.width * new_precent + self.rect.x
