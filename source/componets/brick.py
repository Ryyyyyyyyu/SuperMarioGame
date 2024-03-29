import pygame
from source import constants as C
from source import setup, tools


class Brick(pygame.sprite.Sprite):
    def __init__(self, x, y, brick_type, color=None):
        pygame.sprite.Sprite.__init__(self)
        self.x = x
        self.y = y
        self.brick_type = brick_type
        bright_frames_rects = [(16, 0, 16, 16), (48, 0, 16, 16)]
        dark_frames_rects = [(16, 32, 16, 16), (48, 32, 16, 16)]

        if not color:
            self.frame_rects = bright_frames_rects
        else:
            self.frame_rects = dark_frames_rects

        self.frames = []
        for frame_rect in self.frame_rects:
            self.frames.append(tools.get_image(setup.GRAPHICS.get('tile_set'), *frame_rect, (0, 0, 0), C.BRICK_MULTI))

        self.frame_index = 0
        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
