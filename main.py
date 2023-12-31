################### packges ###################
import pygame
import sys

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
from repeatedFuns import *

#### Once Packges ####

################### Game Init ###################
Drawer.PyImageBase.loadImages("Sprites/Images")

main_json = dataHandler.readJson("GameSavedData\\mainSetting.txt")
start_ui_json = dataHandler.readJson("GameSavedData\\StartStaticUi.txt")
game_ui_json = dataHandler.readJson("GameSavedData\\GameStaticUi.txt")
map_json = dataHandler.readJson("GameSavedData\\GameMapData.txt")

Drawer.readUiFile(start_ui_json, "start_list")
Drawer.readUiFile(game_ui_json, "game_list")
readMapFile(map_json)

music = mixerControl.Music("Sounds\\bgm", "bgm.mp3", main_json["bgm"])
pygame.mixer.music.play(-1)

hover_sound = mixerControl.Sound("Sounds\\sfx", "button_hover.mp3", main_json["sfx"])
select_sound = mixerControl.Sound("Sounds\\sfx", "button_select.mp3", main_json["sfx"])
disabled_sound = mixerControl.Sound("Sounds\\sfx", "button_disabled.mp3", main_json["sfx"])
sounds_list.append(hover_sound)
sounds_list.append(select_sound)
sounds_list.append(disabled_sound)

################### Game Varibales ###################
AUTOSAVE = pygame.USEREVENT + 1
pygame.time.set_timer(AUTOSAVE, 1000)

if main_json["playerName"]:
    game_state = 1
    Drawer.excluded_dict["start_state"] = -1
    Drawer.excluded_dict["game_state"] = 1

mon_max_hp, mon_name = resetBattle("startVillege", Map, main_json)

attack_timer = timeControl.Timer(1000)
attack_timer.startTimer()
regen_timer = timeControl.Timer(2500)
regen_timer.startTimer()
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

Drawer.excluded_dict["game_list"]["statsMenu"] = 1
Drawer.excluded_dict["game_list"]["mapMenu"] = -1
Drawer.excluded_dict["game_list"]["bossMenu"] = -1
Drawer.excluded_dict["game_list"]["settingMenu"] = -1

Drawer.getElementByName("boss1Bt").disabled = main_json["boss1"]
Drawer.getElementByName("boss2Bt").disabled = main_json["boss2"]
Drawer.getElementByName("boss3Bt").disabled = main_json["boss3"]
Drawer.getElementByName("boss4Bt").disabled = main_json["boss4"]
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
                Map.current_entities["player"].damge = main_json["str"]
        elif Drawer.getElementByName("vitIncBt").rect.collidepoint(pygame.mouse.get_pos()):
            if main_json["playerStats"] >= 1:
                main_json["vit"] += 1
                main_json["playerStats"] -= 1

        elif Drawer.getElementByName("map1Bt").rect.collidepoint(pygame.mouse.get_pos()) and Drawer.excluded_dict["game_list"]["mapMenu"] == 1:
            mon_max_hp, mon_name = resetBattle("startVillege", Map, main_json)
        elif Drawer.getElementByName("map2Bt").rect.collidepoint(pygame.mouse.get_pos()) and Drawer.excluded_dict["game_list"]["mapMenu"] == 1:
            mon_max_hp, mon_name = resetBattle("forst", Map, main_json)
        elif Drawer.getElementByName("map3Bt").rect.collidepoint(pygame.mouse.get_pos()) and Drawer.excluded_dict["game_list"]["mapMenu"] == 1:
            mon_max_hp, mon_name = resetBattle("plains", Map, main_json)
        elif Drawer.getElementByName("map4Bt").rect.collidepoint(pygame.mouse.get_pos()) and Drawer.excluded_dict["game_list"]["mapMenu"] == 1:
            mon_max_hp, mon_name = resetBattle("banditLair", Map, main_json)
        elif Drawer.getElementByName("map5Bt").rect.collidepoint(pygame.mouse.get_pos()) and Drawer.excluded_dict["game_list"]["mapMenu"] == 1:
            mon_max_hp, mon_name = resetBattle("magicForst", Map, main_json)
        elif Drawer.getElementByName("map6Bt").rect.collidepoint(pygame.mouse.get_pos()) and Drawer.excluded_dict["game_list"]["mapMenu"] == 1:
            mon_max_hp, mon_name = resetBattle("DemonsArea", Map, main_json)
        elif Drawer.getElementByName("map7Bt").rect.collidepoint(pygame.mouse.get_pos()) and Drawer.excluded_dict["game_list"]["mapMenu"] == 1:
            mon_max_hp, mon_name = resetBattle("viceCastle", Map, main_json)
        elif Drawer.getElementByName("map8Bt").rect.collidepoint(pygame.mouse.get_pos()) and Drawer.excluded_dict["game_list"]["mapMenu"] == 1:
            mon_max_hp, mon_name = resetBattle("demonKingCastle", Map, main_json)
        elif Drawer.getElementByName("boss1Bt").rect.collidepoint(pygame.mouse.get_pos()) and main_json["boss1"] == 0:
            mon_max_hp, mon_name = resetBattle("deepForst", Map, main_json)
        elif Drawer.getElementByName("boss2Bt").rect.collidepoint(pygame.mouse.get_pos()) and main_json["boss2"] == 0:
            mon_max_hp, mon_name = resetBattle("BanditLeaderRoom", Map, main_json)
        elif Drawer.getElementByName("boss3Bt").rect.collidepoint(pygame.mouse.get_pos()) and main_json["boss3"] == 0:
            mon_max_hp, mon_name = resetBattle("ViceRoom", Map, main_json)
        elif Drawer.getElementByName("boss4Bt").rect.collidepoint(pygame.mouse.get_pos()) and main_json["boss4"] == 0:
            mon_max_hp, mon_name = resetBattle("DemonKingRoom", Map, main_json)


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
    global mon_max_hp, mon_name

    Drawer.getElementByName("strPoints").updateText(sm_mid_font, f"{main_json['str']}", "#FFFFFF", "left")
    Drawer.getElementByName("vitPoints").updateText(sm_mid_font, f"{main_json['vit']}", "#FFFFFF", "left")
    Drawer.getElementByName("playerStats").updateText(sm_mid_font, f"{main_json['playerStats']}", "#FFFFFF", "left")

    Drawer.getElementByName("mapName").updateText(mid_font, Map.cureent_map.name, "#FFFFFF", "left")

    mon_current_hp = Map.current_entities['monster'][0].hp
    Drawer.getElementByName("monsterHphBar").updateText(mid_font, f"HP ({mon_current_hp}/{mon_max_hp})", "#FFFFFF", "center")
    Drawer.getElementByName("monsterName").updateText(mid_font, mon_name, "#FFFFFF", "center")
    Drawer.getElementByName("monsterHphBar").setSlider(mon_current_hp / mon_max_hp)

    pl_current_hp = Map.current_entities['player'].hp
    pl_max_hp = main_json["vit"] * 10
    Drawer.getElementByName("healthBar").updateText(mid_font, f"HP ({pl_current_hp}/{pl_max_hp})", "#FFFFFF", "center")
    Drawer.getElementByName("xpBar").updateText(mid_font, f"XP ({main_json['xp']}/{xpCalc(main_json['playerLevel'])})", "#000000", "center")
    Drawer.getElementByName("healthBar").setSlider(pl_current_hp / pl_max_hp)
    Drawer.getElementByName("xpBar").setSlider(main_json['xp'] / xpCalc(main_json['playerLevel']))

    if main_json["playerStats"] == 0:
        Drawer.getElementByName("strIncBt").disabled = 1
        Drawer.getElementByName("vitIncBt").disabled = 1
    else:
        Drawer.getElementByName("strIncBt").disabled = 0
        Drawer.getElementByName("vitIncBt").disabled = 0

    if attack_timer.checkTimer():
        mon_damge, pl_damge = calc_attack(Map)

        Drawer.getElementByName("playerNoti").addQueue(f"You Damged {pl_damge}")
        Drawer.getElementByName("monsterNoti").addQueue(f"Monster Damge {mon_damge}")

        if Map.current_entities['monster'][0].hp <= 0:
            map_name = Map.cureent_map.name
            if map_name == "deepForst":
                main_json["boss1"] = 1
                Drawer.getElementByName("boss1Bt").disabled = 1
                mon_max_hp, mon_name = resetBattle("startVillege", Map, main_json)
                Drawer.getElementByName("playerNoti").addQueue(f"You Have Killed Black Wolf!!")
            elif map_name == "BanditLeaderRoom":
                main_json["boss2"] = 1
                Drawer.getElementByName("boss2Bt").disabled = 1
                mon_max_hp, mon_name = resetBattle("startVillege", Map, main_json)
                Drawer.getElementByName("playerNoti").addQueue(f"You Have Killed Bandit Leader!!")
            elif map_name == "ViceRoom":
                main_json["boss3"] = 1
                Drawer.getElementByName("boss3Bt").disabled = 1
                mon_max_hp, mon_name = resetBattle("startVillege", Map, main_json)
                Drawer.getElementByName("playerNoti").addQueue(f"You Have Killed Vice Demon King!!")
            elif map_name == "DemonKingRoom":
                main_json["boss4"] = 1
                Drawer.getElementByName("boss4Bt").disabled = 1
                mon_max_hp, mon_name = resetBattle("startVillege", Map, main_json)
                Drawer.getElementByName("playerNoti").addQueue(f"You Have Killed Demon King!!")

            else:
                mon_max_hp, mon_name = resetBattle(map_name, Map, main_json)
                main_json["xp"] += Map.current_entities['monster'][0].xp
                Drawer.getElementByName("playerNoti").addQueue(f"You Gained {Map.current_entities['monster'][0].xp} XP!")


                if main_json["xp"] >= xpCalc(main_json['playerLevel']):
                    Drawer.getElementByName("playerNoti").addQueue(f"Level UP!!")
                    main_json["xp"] -= xpCalc(main_json['playerLevel'])
                    main_json['playerLevel'] += 1
                    main_json['str'] += 1
                    main_json['vit'] += 1
                    main_json['playerStats'] += 3
                    Drawer.getElementByName("playerLevelText").updateText(mid_font, f"Lv.<{main_json['playerLevel']}>", "#FFFFFF", "right")

        elif Map.current_entities['player'].hp <= 0:
            mon_max_hp, mon_name = resetBattle("startVillege", Map, main_json)

        attack_timer.startTimer()

    if regen_timer.checkTimer():
        Map.current_entities['player'].hp += round(Map.current_entities['player'].hp * .1)
        if Map.current_entities['player'].hp > main_json["vit"] * 10:
            Map.current_entities['player'].hp = main_json["vit"] * 10
        regen_timer.startTimer()

while True:
    checkEvents()
    if game_state:
        gameStart()
    Drawer.drawGroup()
    # GridDisplay.displayGrid(x_ceil, y_ceil)
    fpsDisplay.displayFps()
    pygame.display.update()
    clock.tick(60)
