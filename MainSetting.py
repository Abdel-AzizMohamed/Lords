import pygame
import os


pygame.init()
pygame.mixer.init()

################### pygame main variables ###################
os.environ['SDL_VIDEO_CENTERED'] = "1"
screen_info = pygame.display.Info()
moniter_width, moniter_height = screen_info.current_w, screen_info.current_h
# os.environ['SDL_VIDEO_WINDOW_POS'] = f"{1366},{moniter_height // 2}"
screen_width = moniter_width
screen_height = moniter_height

x_ceil = 18
y_ceil = 32
ceil_size = moniter_height // x_ceil
################### pygame Setting ###################

clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Lords")
# pygame.display.toggle_fullscreen()
# pygame.mouse.set_visible(False)

game_state = 0
sounds_list = []
max_layer = 10

################### Game Fonts ###################
sm_font = pygame.font.Font(r"fonts\Pixeltype.ttf", 20)
sm_mid_font = pygame.font.Font(r"fonts\Pixeltype.ttf", 25)
mid_font = pygame.font.Font(r"fonts\Pixeltype.ttf", 35)
big_font = pygame.font.Font(r"fonts\Pixeltype.ttf", 50)
fonts_dict = {"sm_font": sm_font, "sm_mid_font": sm_mid_font, "mid_font": mid_font, "big_font": big_font}
