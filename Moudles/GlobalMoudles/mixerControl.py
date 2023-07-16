import pygame

class Music():
    def __init__(self, path, file, volume):
        self.music = pygame.mixer.music.load(f"{path}\\{file}")
        self.volume = volume
        pygame.mixer.music.set_volume(volume)

class Sound():
    def __init__(self, path, file, volume):
        self.sound = pygame.mixer.Sound(f"{path}\\{file}")
        self.volume = volume
        self.sound.set_volume(volume)
