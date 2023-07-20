################### packges ###################
import pygame
import sys
from random import randint, choice

################### Paths ###################
sys.path.append("Moudles\\GlobalMoudles")
sys.path.append("Moudles\\GlobalMoudles\\GraphicHelper")
sys.path.append("Moudles\\GlobalMoudles\\DevHelper")
sys.path.append("Moudles\\OpatinalMoudles")
sys.path.append("Moudles\\OnceMoudles")

################### My Packges ###################
#### Importent Packges ####C
import Drawer
from MainSetting import *
import UiEvents
import dataHandler
import mixerControl

import GridDisplay
import fpsDisplay
#### Opatinal Packges ####
import timeControl

#### Once Packges ####

################### Game Varibales ###################

################### Game Init ###################
main_json = dataHandler.readJson("GameSavedData\\mainSetting.txt")
start_ui_json = dataHandler.readJson("GameSavedData\\StartStaticUi.txt")
game_ui_json = dataHandler.readJson("GameSavedData\\GameStaticUi.txt")

Drawer.readUiFile(start_ui_json, "start_list")
Drawer.readUiFile(game_ui_json, "game_list")

music = mixerControl.Music("Sounds\\bgm", "Ultrakill.mp3", main_json["bgm"])
pygame.mixer.music.play(-1)

hover_sound = mixerControl.Sound("Sounds\\sfx", "button_hover.mp3", main_json["sfx"])
select_sound = mixerControl.Sound("Sounds\\sfx", "button_select.mp3", main_json["sfx"])
disabled_sound = mixerControl.Sound("Sounds\\sfx", "button_disabled.mp3", main_json["sfx"])
sounds_list.append(hover_sound)
sounds_list.append(select_sound)
sounds_list.append(disabled_sound)

AUTOSAVE = pygame.USEREVENT + 1
pygame.time.set_timer(AUTOSAVE, 1000)

if main_json["playerName"]:
    game_state = 1
    Drawer.excluded_dict["start_state"] = -1
    Drawer.excluded_dict["game_state"] = 1

################### Ui small edits ###################
Drawer.getElementByName("statsBt").addMargin(-25, -25)
Drawer.getElementByName("mapsBt").addMargin(-25, -25)
Drawer.getElementByName("bossesBt").addMargin(-25, -25)
Drawer.getElementByName("settingBt").addMargin(-25, -25)
Drawer.getElementByName("exitBt").addMargin(-25, -25)
Drawer.getElementByName("healthBar").setSlider(.5)
Drawer.getElementByName("xpBar").setSlider(.5)
Drawer.getElementByName("monsterHphBar").setSlider(1)
Drawer.getElementByName("bgm").setSlider(main_json["bgm"])
Drawer.getElementByName("bgm").addMargin(0, -40, "text")
Drawer.getElementByName("sfx").setSlider(main_json["sfx"])
Drawer.getElementByName("sfx").addMargin(0, -40, "text")

Drawer.excluded_dict["game_list"]["statsMenu"] = -1
Drawer.excluded_dict["game_list"]["mapMenu"] = -1
Drawer.excluded_dict["game_list"]["bossMenu"] = -1
Drawer.excluded_dict["game_list"]["settingMenu"] = -1
################### Game Events ###################
def globalEvents(event):
    if event.type == pygame.QUIT:
        pygame.quit()
        sys.exit()
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_ESCAPE:
            pygame.quit()
            sys.exit()
    if event.type == AUTOSAVE:
        dataHandler.SaveJson("GameSavedData\\mainSetting.txt", main_json)

    ## Ui events ##
    UiEvents.checkButtonState(event, Drawer.draw_dict, sounds_list)
    input_data = UiEvents.checkInput(event, Drawer.draw_dict)
    new_precnt = UiEvents.sliderGrab(event, Drawer.draw_dict)

    return (new_precnt, input_data)

def startEvents(event, data):
    global game_state

    if data:
        main_json["playerName"] = Drawer.getElementByName("playerNameIin").text
        game_state = 1
        Drawer.excluded_dict["start_state"] = -1
        Drawer.excluded_dict["game_state"] = 1

    if event.type == pygame.MOUSEBUTTONUP:
        if Drawer.getElementByName("startBt").rect.collidepoint(pygame.mouse.get_pos()):
            main_json["playerName"] = Drawer.getElementByName("playerNameIin").text
            game_state = 1
            Drawer.excluded_dict["start_state"] = -1
            Drawer.excluded_dict["game_state"] = 1

def gameEvents(event, data):
    if data:
        if data[0] == "bgm":
            main_json["bgm"] = data[1]
            pygame.mixer.music.set_volume(data[1])
        if data[0] == "sfx":
            main_json["sfx"] = data[1]
            for item in sounds_list:
                item.sound.set_volume(data[1])

    if event.type == pygame.MOUSEBUTTONUP:
        if Drawer.getElementByName("statsBt").rect.collidepoint(pygame.mouse.get_pos()):
            Drawer.excluded_dict["game_list"]["statsMenu"] *= -1
            Drawer.excluded_dict["game_list"]["mapMenu"] = -1
            Drawer.excluded_dict["game_list"]["bossMenu"] = -1
            Drawer.excluded_dict["game_list"]["settingMenu"] = -1
        elif Drawer.getElementByName("mapsBt").rect.collidepoint(pygame.mouse.get_pos()):
            Drawer.excluded_dict["game_list"]["statsMenu"] = -1
            Drawer.excluded_dict["game_list"]["mapMenu"] *= -1
            Drawer.excluded_dict["game_list"]["bossMenu"] = -1
            Drawer.excluded_dict["game_list"]["settingMenu"] = -1
        elif Drawer.getElementByName("bossesBt").rect.collidepoint(pygame.mouse.get_pos()):
            Drawer.excluded_dict["game_list"]["statsMenu"] = -1
            Drawer.excluded_dict["game_list"]["mapMenu"] = -1
            Drawer.excluded_dict["game_list"]["bossMenu"] *= -1
            Drawer.excluded_dict["game_list"]["settingMenu"] = -1
        elif Drawer.getElementByName("settingBt").rect.collidepoint(pygame.mouse.get_pos()):
            Drawer.excluded_dict["game_list"]["statsMenu"] = -1
            Drawer.excluded_dict["game_list"]["mapMenu"] = -1
            Drawer.excluded_dict["game_list"]["bossMenu"] = -1
            Drawer.excluded_dict["game_list"]["settingMenu"] *= -1
        elif Drawer.getElementByName("exitBt").rect.collidepoint(pygame.mouse.get_pos()):
            pygame.quit()
            sys.exit()
        elif Drawer.getElementByName("saveBt").rect.collidepoint(pygame.mouse.get_pos()):
            dataHandler.SaveJson("GameSavedData\\mainSetting.txt", main_json)
        elif Drawer.getElementByName("eraseBt").rect.collidepoint(pygame.mouse.get_pos()):
            dataHandler.SaveJson("GameSavedData\\mainSetting.txt", main_json)

def pauseEvents(event):
    pass


def checkEvents():
    for event in pygame.event.get():
        data = globalEvents(event)
        if game_state == 0:
            startEvents(event, data[1])
        if game_state == 1:
            gameEvents(event, data[0])
        if game_state == 2:
            pauseEvents(event)

def gameStart():
    pass

while True:
    checkEvents()
    if game_state:
        gameStart()
    Drawer.drawGroup()
    # GridDisplay.displayGrid(x_ceil, y_ceil)
    fpsDisplay.displayFps()
    pygame.display.update()
    clock.tick(60)
