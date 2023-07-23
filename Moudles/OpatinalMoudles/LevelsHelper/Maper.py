"""Define a Map Moudle that contains all the neeaded data about game maps

    Classes:
        Map()

    Functions:
        ReadMapFile(file)
"""
import pygame
from MainSetting import *


class Map():
    """Define a map object that stores map data like: (collsion, ui, ..etc)

        Magic Methods:
            __init__(self, group, collsion)

        Attributes:
            current_map(object): current active map
                - used for desactive map ui if the current map changed

            maps(dict): a dict that contains all of the initialized maps so you can access them
    """
    cureent_map = None
    maps = {}

    def __init__(self, name, group, collisions):
        """Initalize a new object

            Args:
                group(string): map ui group name
                    - used to active the given group from execlude_list

                collisions(list of integers): collision list that contains 0, 1 represent a ceil in the grid
                    - 1 represent an ceil that the player can go through it, 0 is the same but he can't go throght it

                entities(list of objects): this list contains all the movenable objects in this map object
                    - this will tell you what are the entities in this map so you can handle them in your way
                    - example of entities: monsters, npc, ...

        """
        self.name = name
        self.group = group
        self.collisions = collisions
        self.entities = []

        Map.maps.update({name: self})


def readMapFile(file):
    """creates Map objects from given file data

        Args:
            file(dict): a dict that contains maps with its data
    """
    for key, item in file.items():
        map_item = Map(key, item["group"], item["collisions"])
