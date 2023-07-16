################### packges ###################
import pygame
import sys
from random import randint, choice

################### Paths ###################
sys.path.append("Moudles\\GlobalMoudles")
sys.path.append("Moudles\\GlobalMoudles\\GraphicHelper")
sys.path.append("Moudles\\OpatinalMoudles")
sys.path.append("Moudles\\OnceMoudles")

################### My Packges ###################
#### Importent Packges ####
import Drawer
from MainSetting import *
import UiEvents
import dataHandler
import mixerControl

#### Opatinal Packges ####
import timeControl

#### Once Packges ####

################### Game Varibales ###################

################### Game Init ###################
main_json = dataHandler.readJson("GameSavedData\\mainSetting.txt")
start_ui_json = dataHandler.readJson("GameSavedData\\StartStaticUi.txt")
game_ui_json = dataHandler.readJson("GameSavedData\\GameStaticUi.txt")

Drawer.readUiFile(start_ui_json)
Drawer.readUiFile(game_ui_json)

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
################### Game Events ###################
def checkEvents():
    global game_state, body_count, delete_count
    ############ Global Events ############
    ## basic events ##
    for event in pygame.event.get():
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

        if new_precnt:
            if new_precnt[0] == "bgm":
                main_json["bgm"] = new_precnt[1]
                pygame.mixer.music.set_volume(new_precnt[1])
            if new_precnt[0] == "sfx":
                main_json["sfx"] = new_precnt[1]
                for item in sounds_list:
                    item.sound.set_volume(new_precnt[1])

        # if event.type == pygame.MOUSEBUTTONDOWN:
        #     if Drawer.draw_dict["gameplay"]["IMGcoin"].rect.collidepoint(pygame.mouse.get_pos()):
        #         main_json["coins"] += 1
        #     if Drawer.draw_dict["gameplay"]["IBTsetting"].rect.collidepoint(pygame.mouse.get_pos()):
        #         Drawer.excluded_dict["game_list"]["settingMenu"] *= -1
        #         Drawer.excluded_dict["game_list"]["upgradeMenu"] = -1
        #     if Drawer.draw_dict["gameplay"]["IBTupgrade"].rect.collidepoint(pygame.mouse.get_pos()):
        #         Drawer.excluded_dict["game_list"]["upgradeMenu"] *= -1
        #         Drawer.excluded_dict["game_list"]["settingMenu"] = -1
        #     if Drawer.draw_dict["gameplay"]["IBTexit"].rect.collidepoint(pygame.mouse.get_pos()):
        #         pygame.quit()
        #         sys.exit()


def gameStart():
    pass

while True:
    checkEvents()
    if game_state:
        gameStart()

    Drawer.drawGroup()
    pygame.display.update()
    clock.tick(60)
