from source.componets import info
import pygame


class Level:
    def __init__(self):
        self.finished = False
        self.next = None

    def draw(self, surface):
        surface.fill((0, 255, 255))

    def update(self, surface, keys):
        self.draw(surface)
