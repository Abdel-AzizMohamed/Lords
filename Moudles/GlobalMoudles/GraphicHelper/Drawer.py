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
            if getattr(item, "border_width", 0) > 0:
                pygame.draw.rect(screen, item.border_color, item.border_rect)

            if item.type == "CI":
                pygame.draw.circle(screen, item.active_color, item.rect.center, item.radius)
            elif item.type == "BT":
                pygame.draw.rect(screen, item.active_color, item.rect)
            elif item.type == "IN":
                pygame.draw.rect(screen, item.active_color, item.rect)
            elif item.type == "GR":
                continue
            elif item.type == "SL":
                pygame.draw.rect(screen, item.bar_color, item.rect)
                pygame.draw.rect(screen, item.bar_fill_color, item.bar_fill_rect)
                pygame.draw.rect(screen, item.handle_color, item.handle_rect)
            elif item.type == "MA":
                for text_ele in item.text_elements:
                    screen.blit(text_ele.ren_text, text_ele.rect_text)

            elif item.type == "IMG":
                screen.blit(item.image, item.rect)
            elif item.type == "IBT":
                screen.blit(item.button_state, item.rect)
            elif item.type == "IPR":
                screen.blit(item.fill_image, item.rect)
                pygame.draw.rect(screen, item.base_bar_color, item.base_bar_rect)
                screen.blit(item.bar_image, item.rect)
            elif item.type == "ISL":
                screen.blit(item.fill_image, item.rect)
                pygame.draw.rect(screen, item.base_bar_color, item.base_bar_rect)
                screen.blit(item.bar_image, item.rect)
                screen.blit(item.handle_state, item.handle_rect)
            elif item.type == "IIN":
                screen.blit(item.input_state, item.rect)
                screen.blit(item.field_image, item.rect)

            else:
                surface = pygame.Surface(item.rect.size)
                surface.fill(item.active_color)
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

        if data["type"] == "BT":
            element = PyButton(data["group"], name, data["size"], data["pos"], data["grab"])
        if data["type"] == "IN":
            element = PyInput(data["group"], name, data["size"], data["pos"], data["grab"])
        elif data["type"] == "SL":
            element = PySlider(data["group"], name, data["size"], data["pos"], data["grab"])
        elif data["type"] == "FR":
            element = PyFrame(data["group"], name, data["size"], data["pos"], data["grab"])
        elif data["type"] == "MA":
            element = PyMultiArea(data["group"], name, data["size"], data["pos"], data["grab"], data["lines"], data["line_height"])
        elif data["type"] == "IMG":
            element = PyImage(data["group"], name, data["url"], data["pos"], data["grab"], data["scale"])
        elif data["type"] == "IBT":
            element = PyIButton(data["group"], name, data["urls"], data["pos"], data["grab"], data["scale"])
        elif data["type"] == "IPR":
            element = PyIProgress(data["group"], name, data["urls"], data["pos"], data["grab"], data["scale"])
        elif data["type"] == "ISL":
            element = PyISlider(data["group"], name, data["urls"], data["pos"], data["grab"], data["scale"])
        elif data["type"] == "IIN":
            element = PyIInput(data["group"], name, data["urls"], data["pos"], data["grab"], data["scale"])
        else:
            element = PyRect(data["group"], name, data["size"], data["pos"], data["grab"])

        for attr_name, attr_data in data.items():
            setattr(element, attr_name, attr_data)

        if getattr(element, "text_align", -1) != -1:
            element.updateText(fonts_dict[data["font"]], data["text"], data["text_color"], data["text_align"])
        if getattr(element, "border_width", -1) != -1:
            element.setBorder(element.border_width, element.border_color)

def getElementByName(name):
    for group in draw_dict.values():
        for key, element in group.items():
            if key == name:
                return element
