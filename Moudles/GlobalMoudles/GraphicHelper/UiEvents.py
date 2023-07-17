import pygame

################### Varibales ###################
grabed_slide = False
slider_pos = 0
current_item = None

def sliderGrab(event, ui_dict):
    global grabed_slide, grabed_slide, current_item

    for group in ui_dict.keys():
        for name, item in ui_dict[group].items():
            if item.type == "SL":
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if not grabed_slide and item.handle_rect.collidepoint(pygame.mouse.get_pos()):
                        grabed_slide = True
                        slider_pos = pygame.mouse.get_pos()[0]
                        current_item = item
                if event.type == pygame.MOUSEBUTTONUP:
                    grabed_slide = False

    if grabed_slide:
        return sliderMove()
    return None

def sliderMove():
    current_pos = pygame.mouse.get_pos()[0]
    if current_pos != slider_pos:
        if current_pos >= current_item.end_pos:
            current_item.precent = 1
        elif current_pos <= current_item.start_pos:
            current_item.precent = 0
        else:
            current_item.precent = (current_pos - current_item.start_pos) / current_item.rect.width

        current_item.setSlider(current_item.precent)

        return [current_item.name[2:], current_item.precent]

def checkButtonState(event, ui_dict, sounds_list):
    for group in ui_dict.keys():
        for item in ui_dict[group].values():
            if item.type == "BT":
                if item.disabled:
                    item.active_color = item.disabled_color
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        sounds_list[2].sound.play()

                elif item.rect.collidepoint(pygame.mouse.get_pos()):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        sounds_list[1].sound.play()
                        item.active_color = item.select_color
                    elif item.active_color != item.hover_color:
                        sounds_list[0].sound.play()
                        item.active_color = item.hover_color
                else:
                    item.active_color = item.base_color
            elif item.type == "IBT":
                if item.disabled:
                    item.button_state = item.disabled_image

                elif item.rect.collidepoint(pygame.mouse.get_pos()):
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        sounds_list[1].sound.play()
                        item.button_state = item.select_image
                    elif item.button_state != item.hover_image:
                        sounds_list[0].sound.play()
                        item.button_state = item.hover_image
                else:
                    item.button_state = item.image
