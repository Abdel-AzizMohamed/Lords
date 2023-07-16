import pygame


def groupCollision(group1, group2, kill=0):
    if len(group1) == 0 or len(group2) == 0:
        return False

    for key1, item1 in group1.items():
        for key2, item2 in group2.items():
            if item1.rect.colliderect(item2.rect):
                return (key1, key2)
    return False
