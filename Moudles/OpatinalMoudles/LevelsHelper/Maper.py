"""Define a Map Moudle that contains all the neeaded data about game maps

    Classes:
        Map()

    Functions:
        ReadMapFile(file)
"""
from MapEntities import *
from random import randint


class Map():
    """Define a map object that stores map data like: (collsion, ui, ..etc)

        Magic Methods:
            __init__(self, group, collsion)

        Attributes:
            current_map(object): current active map
                - used for desactive map ui if the current map changed

            current_map(dict): current active entities

            maps(dict): a dict that contains all of the initialized maps so you can access them
    """
    cureent_map = None
    current_entities = {
            "player": None,
            "monster": [],
            "npc": []
            }
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
        self.entities = {
            "player": None,
            "monster": [],
            "npc": []
        }

        Map.maps.update({name: self})

    @classmethod
    def changeMap(cls, map, ent_count=0):
        """Change the current map to the new map
            and also add a copy of specified amount from new map entities list
            to avoid editing the original values of map entities

            map(string): new map name to get from maps list

            ent_count(integer)=0: number of entities of this map
                - the deflaut value is 0 so that it will only add the player
         """
        cls.cureent_map = cls.maps[map]
        cls.current_entities["monster"].clear()
        cls.current_entities["npc"].clear()

        new_player = Entitie.createCopy(cls.cureent_map.entities["player"])

        cls.current_entities["player"] = new_player

        for i in range(ent_count):
            monster = cls.selectEntitie()
            new_monster = Entitie.createCopy(monster)
            cls.current_entities["monster"].append(monster)


    @staticmethod
    def selectEntitie():
        """ select a random monster from entities list

            Rerturn: selected monster
        """
        monster_list = Map.cureent_map.entities["monster"]
        random_int = randint(0, len(monster_list) - 1)

        return monster_list[random_int]

def readMapFile(file):
    """creates Map objects from given file data

        Args:
            file(dict): a dict that contains maps with its data
    """
    for key, item in file.items():
        map_item = Map(key, item["group"], item["collisions"])
        for ent in item["entities"]:
            ent_obj = Entitie(ent["name"], ent["type"], ent["hp"], ent["damge"])
            if ent_obj.type == "player":
                map_item.entities["player"] = ent_obj
            else:
                map_item.entities[ent_obj.type].append(ent_obj)
