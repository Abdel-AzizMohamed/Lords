################### packges ###################
import pygame
import sys
from random import randint, choice

################### Paths ###################
sys.path.append("Moudles\\GlobalMoudles")
sys.path.append("Moudles\\GlobalMoudles\\GraphicHelper")
sys.path.append("Moudles\\GlobalMoudles\\DevHelper")
sys.path.append("Moudles\\OpatinalMoudles")
sys.path.append("Moudles\\OpatinalMoudles\\LevelsHelper")
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
from Maper import *

#### Once Packges ####

################### Game Init ###################
main_json = dataHandler.readJson("GameSavedData\\mainSetting.txt")
start_ui_json = dataHandler.readJson("GameSavedData\\StartStaticUi.txt")
game_ui_json = dataHandler.readJson("GameSavedData\\GameStaticUi.txt")
map_json = dataHandler.readJson("GameSavedData\\GameMapData.txt")

Drawer.readUiFile(start_ui_json, "start_list")
Drawer.readUiFile(game_ui_json, "game_list")
readMapFile(map_json)

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

Map.changeMap("startVillege", 1)
Map.current_entities["player"].hp = main_json["vit"] * 10
Map.current_entities["player"].damge = main_json["str"]
mon_max_hp = Map.current_entities['monster'][0].hp
mon_name = Map.current_entities['monster'][0].name

################### Game Varibales ###################

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

Drawer.getElementByName("playerNameText").updateText(mid_font, main_json["playerName"], "#FFFFFF", "left")
Drawer.getElementByName("playerName").updateText(mid_font, main_json["playerName"], "#FFFFFF", "left")
Drawer.getElementByName("playerLevelText").updateText(mid_font, f"Lv.<{main_json['playerLevel']}>", "#FFFFFF", "right")
Drawer.getElementByName("playerStats").updateText(sm_mid_font, f"{main_json['playerStats']}", "#FFFFFF", "left")
Drawer.getElementByName("strPoints").updateText(sm_mid_font, f"{main_json['str']}", "#FFFFFF", "left")
Drawer.getElementByName("vitPoints").updateText(sm_mid_font, f"{main_json['vit']}", "#FFFFFF", "left")

Drawer.getElementByName("playerStatsLine").addPadding(0, -40)
Drawer.getElementByName("playerStatsLine").addMargin(0, 33)
Drawer.getElementByName("strLine").addPadding(0, -40)
Drawer.getElementByName("strLine").addMargin(0, 33)
Drawer.getElementByName("vitLine").addPadding(0, -40)
Drawer.getElementByName("vitLine").addMargin(0, 33)

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
    global mon_max_hp, mon_name

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

        elif Drawer.getElementByName("strIncBt").rect.collidepoint(pygame.mouse.get_pos()):
            if main_json["playerStats"] >= 1:
                main_json["str"] += 1
                main_json["playerStats"] -= 1
        elif Drawer.getElementByName("vitIncBt").rect.collidepoint(pygame.mouse.get_pos()):
            if main_json["playerStats"] >= 1:
                main_json["vit"] += 1
                main_json["playerStats"] -= 1

        elif Drawer.getElementByName("map1Bt").rect.collidepoint(pygame.mouse.get_pos()):
            Map.changeMap("startVillege", 1)
            Map.current_entities["player"].hp = main_json["vit"] * 10
            Map.current_entities["player"].damge = main_json["str"]
            mon_max_hp = Map.current_entities['monster'][0].hp
            mon_name = Map.current_entities['monster'][0].name
        elif Drawer.getElementByName("map2Bt").rect.collidepoint(pygame.mouse.get_pos()):
            Map.changeMap("forst", 1)
            Map.current_entities["player"].hp = main_json["vit"] * 10
            Map.current_entities["player"].damge = main_json["str"]
            mon_max_hp = Map.current_entities['monster'][0].hp
            mon_name = Map.current_entities['monster'][0].name

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
    Drawer.getElementByName("strPoints").updateText(sm_mid_font, f"{main_json['str']}", "#FFFFFF", "left")
    Drawer.getElementByName("vitPoints").updateText(sm_mid_font, f"{main_json['vit']}", "#FFFFFF", "left")
    Drawer.getElementByName("playerStats").updateText(sm_mid_font, f"{main_json['playerStats']}", "#FFFFFF", "left")

    Drawer.getElementByName("mapName").updateText(mid_font, Map.cureent_map.name, "#FFFFFF", "left")

    mon_current_hp = Map.current_entities['monster'][0].hp
    Drawer.getElementByName("monsterHphBar").updateText(mid_font, f"HP ({mon_current_hp}/{mon_max_hp})", "#FFFFFF", "center")
    Drawer.getElementByName("monsterName").updateText(mid_font, mon_name, "#FFFFFF", "center")

    pl_current_hp = Map.current_entities['player'].hp
    pl_max_hp = main_json["vit"] * 10
    Drawer.getElementByName("healthBar").updateText(mid_font, f"HP ({pl_current_hp}/{pl_max_hp})", "#FFFFFF", "center")

    if main_json["playerStats"] == 0:
        Drawer.getElementByName("strIncBt").disabled = 1
        Drawer.getElementByName("vitIncBt").disabled = 1
    else:
        Drawer.getElementByName("strIncBt").disabled = 0
        Drawer.getElementByName("vitIncBt").disabled = 0

while True:
    checkEvents()
    if game_state:
        gameStart()
    Drawer.drawGroup()
    # GridDisplay.displayGrid(x_ceil, y_ceil)
    fpsDisplay.displayFps()
    pygame.display.update()
    clock.tick(60)
