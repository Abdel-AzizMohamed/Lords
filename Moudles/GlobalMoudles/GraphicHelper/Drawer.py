import pygame
from pygame import math
from UiSprite import *

######################## Functions ##############################
def excludedGroups():
    if excluded_dict["start_state"] == 1:
        return "start_list"
    return "game_list"

def getLayers(active_group):
    layring_dict = {}

    for i in range(max_layer):
        layring_dict.update({f"layer{1 + i}": []})

    for group, state in excluded_dict[active_group].items():
        if state == 1:
            for item in draw_dict[group].values():
                layring_dict[f"layer{item.layer}"].append(item)

    return layring_dict

def drawGroup():
    active_group = excludedGroups()
    elements = getLayers(active_group)

    for layer in elements.values():
        for item in layer:
            if item.border_width > 0:
                pygame.draw.rect(screen, item.border_color, item.border_rect)
            if item.type == "GR":
                continue
            elif item.type == "SL":
                pygame.draw.rect(screen, item.bar_color, item.rect)
                pygame.draw.rect(screen, item.bar_fill_color, item.bar_fill_rect)
                pygame.draw.rect(screen, item.handle_color, item.handle_rect)
            elif item.type == "CI":
                pygame.draw.circle(screen, item.active_color, item.rect.center, item.radius)
            elif item.type == "IMG":
                screen.blit(item.image, item.rect)
            elif item.type == "IBT":
                screen.blit(item.button_state, item.rect)
            elif item.type == "BT":
                pygame.draw.rect(screen, item.active_color, item.rect)
            else:
                surface = pygame.Surface(item.rect.size)
                pygame.draw.rect(surface, item.active_color, item.rect)
                surface.set_alpha(round(255 * item.opacity))
                screen.blit(surface, item.rect)

            screen.blit(item.ren_text, item.rect_text)

def createGroup(name, group):
    if name not in draw_dict:
        draw_dict.update({name : {}})
        excluded_dict[group].update({name : 1})

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

def readUiFile(ui_data, ui_group):
    for name, data in ui_data.items():
        createGroup(data["group"], ui_group)

        if type(data["size"]) == list:
            size = (data["size"][0], data["size"][1])
        else:
            size = data["size"]
        pos = (data["pos"][0], data["pos"][1])

        if data["type"] == "BT":
            element = PyButton(data["group"], name, size, pos, data["grab"], data["frame"])
        elif data["type"] == "SL":
            element = PySlider(data["group"], name, size, pos, data["grab"], data["frame"])
        elif data["type"] == "FR":
            element = PyFrame(data["group"], name, size, pos, data["grab"])
        elif data["type"] == "IMG":
            element = PyImage(data["group"], name, data["url"], pos, data["grab"], data["frame"], data["size"])
        elif data["type"] == "IBT":
            element = PyIButton(data["group"], name, data["urls"], pos, data["grab"], data["frame"], data["size"])
        else:
            element = PyRect(data["group"], name, size, pos, data["grab"], data["frame"])

        for attr_name, attr_data in data.items():
            setattr(element, attr_name, attr_data)

        element.updateText(fonts_dict[data["font"]], data["text"], data["text_color"], data["text_align"])
        element.setBorder(element.border_width, element.border_color)
