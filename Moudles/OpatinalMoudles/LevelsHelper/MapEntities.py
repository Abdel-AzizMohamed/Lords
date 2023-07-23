"""Define a Entitie Moudle that contains all the neeaded data about game Entities

    Classes:
        Entitie()
"""
import pygame
from MainSetting import *


class Entitie():
    """Define a entitie object that stores entitie data: (name, hp, ui object, ..etc)

        Magic Methods:
            __init__(self, name, type, hp, damge)
    """
    def __init__(self, name, type, hp, damge):
        """Initalize a new object

            Args:
                name(string): name of the object
                type(string): type of the object (player, monster, npc, ...)
                hp(integer): health of the object
                damge(integer): damge of the object
        """
        self.name = name
        self.type = type
        self.hp = hp
        self.damge = damge

    @classmethod
    def createCopy(cls, obj):
        new_obj = cls(obj.name, obj.type, obj.hp, obj.damge)

        return new_obj
