import pygame


class Timer():
    def __init__(self, time):
        self.timer = 0
        self.time = time
        self.current_time = 0
        self.timer_state = False

    def startTimer(self):
        self.current_time = pygame.time.get_ticks()
        self.timer = self.time + self.current_time
        self.timer_state = True

    def checkTimer(self):
        if not self.timer_state:
            return False

        elif self.current_time - self.timer > 0:
            self.timer_state = False
            return True

        self.current_time = pygame.time.get_ticks()
        return False
