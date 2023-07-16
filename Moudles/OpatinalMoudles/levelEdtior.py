import pygame
from MainSetting import *


map_list = []

class Map():
    def __init__(self, group, wall_list):
        self.group = group
        self.wall_list = wall_list

    def setIndex(self):
        if len(map_list) == 0:
            map_list.append([self])
        elif len(map_list[-1]) < map_width:
            map_list[-1].append(self)
        else:
            map_list.append([self])

def readMapFile(file):
    for key, item in file.items():
        map_item = Map(item["group"], item["wall_list"])
        map_item.setIndex()
