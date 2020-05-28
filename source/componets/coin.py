import pygame
from .. import tools,setup
from .. import constants as C


class FlashingCoin(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.farmes= []
        self.farme_index = 0
        farme_rects = [(1, 160, 5, 8), (9, 160, 5, 8), (17, 160, 5, 8), (9, 160, 5, 8)]
        self.load_frames(farme_rects)
        self.image = self.farmes[self.farme_index]
        self.rect = self.image.get_rect()
        self.rect.x = 280
        self.rect.y = 58
        self.timer = 0


    def load_frames(self, frame_rects):
        sheet= setup.GRAPHICS['item_objects']
        for frame_rect in frame_rects:
            self.farmes.append(tools.get_image(sheet, *frame_rect, (0, 0, 0), C.BG_MULTI))


    def update(self, *args):
        self.current_time = pygame.time.get_ticks()
        frame_durations = [375, 125, 125, 125]

        if self.timer == 0:
            self.timer = self.current_time
        elif self.current_time - self.timer > frame_durations[self.farme_index]:
            self.farme_index += 1
            self.farme_index %= 4
            self.timer = self.current_time

        self.image = self.farmes[self.farme_index]