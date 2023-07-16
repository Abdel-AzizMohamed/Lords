import pygame
import os


################### pygame main variables ###################
screen_width = 600
screen_height = 600
ceil_count = 20
max_layer = 10
map_width = 3
map_height = 3
ceil_size = screen_height // ceil_count
################### pygame Setting ###################
pygame.init()
pygame.mixer.init()

os.environ['SDL_VIDEO_CENTERED'] = "1"
screen_info = pygame.display.Info()
moniter_width, moniter_height = screen_info.current_w, screen_info.current_h
# os.environ['SDL_VIDEO_WINDOW_POS'] = f"{1366},{moniter_height // 2}"

clock = pygame.time.Clock()
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("PyDating")
# pygame.display.toggle_fullscreen()
# pygame.mouse.set_visible(False)

game_state = True
sounds_list = []

################### Game Fonts ###################
sm_font = pygame.font.Font(r"fonts\Pixeltype.ttf", 20)
sm_mid_font = pygame.font.Font(r"fonts\Pixeltype.ttf", 25)
mid_font = pygame.font.Font(r"fonts\Pixeltype.ttf", 35)
big_font = pygame.font.Font(r"fonts\Pixeltype.ttf", 50)
fonts_dict = {"sm_font": sm_font, "sm_mid_font": sm_mid_font, "mid_font": mid_font, "big_font": big_font}
