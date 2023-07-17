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
#### Importent Packges ####
import Drawer
from MainSetting import *
import UiEvents
import dataHandler
import mixerControl

import GridDisplay
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
# Drawer.draw_dict["settingMenu"]["SLbgm"].setSlider(main_json["bgm"])
# Drawer.draw_dict["settingMenu"]["SLsfx"].setSlider(main_json["sfx"])

hover_sound = mixerControl.Sound("Sounds\\sfx", "button_hover.mp3", main_json["sfx"])
select_sound = mixerControl.Sound("Sounds\\sfx", "button_select.mp3", main_json["sfx"])
disabled_sound = mixerControl.Sound("Sounds\\sfx", "button_disabled.mp3", main_json["sfx"])
sounds_list.append(hover_sound)
sounds_list.append(select_sound)
sounds_list.append(disabled_sound)

AUTOSAVE = pygame.USEREVENT + 1
pygame.time.set_timer(AUTOSAVE, 1000)


################### Ui small edits ###################
Drawer.getElementByName("start").updateText(sm_mid_font, "uwu", "#FFFFFF", "center")
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
    new_precnt = UiEvents.sliderGrab(event, Drawer.draw_dict)

    return new_precnt

def startEvents(event, data):
    global game_state

    if data:
        if data[0] == "bgm":
            main_json["bgm"] = data[1]
            pygame.mixer.music.set_volume(data[1])
        if data[0] == "sfx":
            main_json["sfx"] = data[1]
            for item in sounds_list:
                item.sound.set_volume(data[1])

def gameEvents(event):
    pass

def pauseEvents(event):
    pass


def checkEvents():
    for event in pygame.event.get():
        data = globalEvents(event)
        if game_state == 0:
            startEvents(event, data)
        if game_state == 1:
            gameEvents(event)
        if game_state == 2:
            pauseEvents(event)

def gameStart():
    pass

while True:
    checkEvents()
    if game_state:
        gameStart()
    Drawer.drawGroup()
    GridDisplay.displayGrid(x_ceil, y_ceil, "#FFFFFF")
    pygame.display.update()
    clock.tick(60)
