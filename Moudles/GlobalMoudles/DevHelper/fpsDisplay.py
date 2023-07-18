import pygame
from MainSetting import *


def displayFps(color="#FFFFFF"):
    print(round(clock.get_fps()))
    ren_font = sm_mid_font.render(str(round(clock.get_fps())), False, color)
    rec_font = ren_font.get_rect(center=(100, 100))

    screen.blit(ren_font, rec_font)
