import pygame
from pygame import math
from UiSprite import *

######################## Functions ##############################
def drawGroup():
    active_main_group = ""
    layring_dict = {}
    ## remove unwanted groups
    if excluded_dict["start_state"] == 1:
        active_main_group = "start_list"
    else:
        active_main_group = "game_list"

    for i in range(max_layer):
        layring_dict.update({f"layer{1 + i}": []})

    for group, state in excluded_dict[active_main_group].items():
        if state == 1:
            for item in draw_dict[group].values():
                layring_dict[f"layer{item.layer}"].append(item)

    for layer in layring_dict.values():
        for item in layer:
            if item.border_width > 0:
                pygame.draw.rect(screen, item.border_color, item.border_rect)
            if item.name[:2] == "GR":
                continue
            elif item.name[:2] == "SL":
                pygame.draw.rect(screen, item.bar_color, item.rect)
                pygame.draw.rect(screen, item.bar_fill_color, item.bar_fill_rect)
                pygame.draw.rect(screen, item.handle_color, item.handle_rect)
            elif item.name[:2] == "CI":
                pygame.draw.circle(screen, item.active_color, item.rect.center, item.radius)
            elif item.name[:3] == "IMG":
                screen.blit(item.image, item.rect)
            elif item.name[:3] == "IBT":
                screen.blit(item.button_state, item.rect)
            else:
                surface = pygame.Surface(item.rect.size)
                pygame.draw.rect(surface, item.active_color, item.rect)
                surface.set_alpha(round(255 * item.opacity))
                screen.blit(surface, item.rect)

            screen.blit(item.ren_text, item.rect_text)

def createGroup(group):
    draw_dict.update({group : {}})

def drawRectPattern():
    for row in range(20):
        for col in range(10):
            pat_obj = PyRect("INCrectPattern", "rectPat", (1, 1), (0 + col * 2 + (row % 2), 0 + row))
            pat_obj.active_color = "#49a252"
            pat_obj.layer = 2

def randomPattern(count, randint, choice, color_list):
    for row in range(count):
        random_x = randint(0, screen_width)
        random_y = randint(0, screen_height)
        pat_obj = PyRect("INCrectPattern", "rectPat", (1, 1), (0, 0))
        pat_obj.rect.x = random_x
        pat_obj.rect.y = random_y
        pat_obj.active_color = choice(color_list)
        pat_obj.addPadding(-25, -25)

def readUiFile(ui_data):
    for name, data in ui_data.items():
        if type(data["size"]) == list:
            size = (data["size"][0], data["size"][1])
        else:
            size = data["size"]
        pos = (data["pos"][0], data["pos"][1])

        if name[:2] == "BT":
            element = PyButton(data["group"], name[2:], size, pos, data["grab"], data["frame"])
        elif name[:2] == "SL":
            element = PySlider(data["group"], name[2:], size, pos, data["grab"], data["frame"])
        elif name[:2] == "FR":
            element = PyFrame(data["group"], name[2:], size, pos, data["grab"])
        elif name[:3] == "IMG":
            element = PyImage(data["group"], name[3:], data["url"], pos, data["grab"], data["frame"], data["size"])
        elif name[:3] == "IBT":
            element = PyIButton(data["group"], name[3:], data["urls"], pos, data["grab"], data["frame"], data["size"])
        else:
            element = PyRect(data["group"], name, size, pos, data["grab"], data["frame"])

        for attr_name, attr_data in data.items():
            setattr(element, attr_name, attr_data)

        element.updateText(fonts_dict[data["font"]], data["text"], data["text_color"], data["text_align"])
        element.setBorder(element.border_width, element.border_color)
