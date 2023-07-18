import pygame
from MainSetting import *



def displayGrid(rows, columns, color="#FFFFFF"):
    base_x = screen_width / y_ceil
    base_y = screen_height / x_ceil

    for i in range(rows):
        pygame.draw.aaline(screen, color, (0, base_y * i), (screen_width, base_y * i))
    pygame.draw.aaline(screen, color, (0, screen_height - 1), (screen_width, screen_height - 1))

    for i in range(columns + 1):
        pygame.draw.aaline(screen, color, (base_x * i, 0), (base_x * i, screen_height))
    pygame.draw.aaline(screen, color, (screen_width - 1, 0), (screen_width - 1, screen_height))
