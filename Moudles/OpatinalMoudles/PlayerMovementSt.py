import pygame
from MainSetting import *


class Player():
    def __init__(self):
        self.dira = (1, 0)
        self.ceil = ceil_size
        self.rect = None

        self.is_move = False
        self.revers = False
        self.in_talk = False

        self.map_index = [0, 0]
        self.player_index = [10, 10]

        self.current_map = None
        self.current_npc = None

    def setMoveDist(self):
        if self.player_index[0] == 0 and self.map_index[0] == 0 and self.dira[0] == -1:
            return 0
        if self.player_index[0] == 19 and self.map_index[0] == map_width - 1 and self.dira[0] == 1:
            return 0
        if self.player_index[1] == 0 and self.map_index[1] == 0 and self.dira[1] == -1:
            return 0
        if self.player_index[1] == 19 and self.map_index[1] == map_height - 1 and self.dira[1] == 1:
            return 0

        walls_check = self.checkWalls()
        if walls_check != 1:
            return 0

        self.current_x = self.rect.x + self.dira[0] * self.ceil
        self.current_y = self.rect.y + self.dira[1] * self.ceil

        self.player_index[0] = self.current_x // self.ceil
        self.player_index[1] = self.current_y // self.ceil

        if self.dira[0] < 0 or self.dira[1] < 0:
            self.revers = True
        else:
            self.revers = False

    def gridMove(self):
        if self.revers:
            if (self.current_x < self.rect.x):
                self.rect.x -= 10
            elif (self.current_y < self.rect.y):
                self.rect.y -= 10
            else:
                    self.is_move = False
        else:
            if (self.current_x > self.rect.x):
                self.rect.x += 10
            elif (self.current_y > self.rect.y):
                self.rect.y += 10
            else:
                self.is_move = False

    def checkMapChange(self, map_list, Drawer):
        map_changed = False

        self.current_map = map_list[self.map_index[1]][self.map_index[0]]

        if self.player_index[0] <= -1:
            self.map_index[0] += -1
            self.rect.x = 10 * self.ceil
            self.rect.y = 10 * self.ceil
            map_changed = True
        if self.player_index[0] >= ceil_count:
            self.map_index[0] += 1
            self.rect.x = 10 * self.ceil
            self.rect.y = 10 * self.ceil
            map_changed = True
        if self.player_index[1] <= -1:
            self.map_index[1] += -1
            self.rect.x = 10 * self.ceil
            self.rect.y = 10 * self.ceil
            map_changed = True
        if self.player_index[1] >= ceil_count:
            self.map_index[1] += 1
            self.rect.x = 10 * self.ceil
            self.rect.y = 10 * self.ceil
            map_changed = True

        if map_changed:
            Drawer.excluded_dict["game_list"][self.current_map.group] = -1
            self.player_index = [10, 10]
            self.current_map = map_list[self.map_index[1]][self.map_index[0]]
            Drawer.excluded_dict["game_list"][self.current_map.group] = 1
            self.is_move = False

    def checkWalls(self):
        plyer_next_pos_x = ((self.rect.x // self.ceil) + self.dira[0]) - 1
        plyer_next_pos_y = ((self.rect.y // self.ceil) + self.dira[1]) - 1
        current_wall = self.current_map.wall_list[plyer_next_pos_y][plyer_next_pos_x]

        if current_wall == 0:
            return 0
        elif current_wall != 1:
            return current_wall
        return 1
