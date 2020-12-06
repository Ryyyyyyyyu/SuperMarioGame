import pygame

from source import constants as C
from source.componets import coin


class Info:

    def __init__(self, state):
        self.state = state
        self.create_state_labels()
        self.create_info_labels()
        self.flash_coin = coin.FlashingCoin()

    def create_label(self, label, size=40, width_scale=1.25, height_scale=1):
        font = pygame.font.SysFont(C.FONT, size)
        label_image = font.render(label, 1, (255, 255, 255))
        # rect = label_image.get_rect()
        # label_image = pygame.transform.scale(label_image,
        # (int(rect.width * width_scale), int(rect.height * height_scale)))

        return label_image

    def create_state_labels(self):
        self.state_labels = []
        if self.state == 'main_menu':
            self.state_labels.append((self.create_label('1  PLAYER  GAME'), (272, 360)))
            self.state_labels.append((self.create_label('2  PLAYERS GAME'), (272, 405)))
            self.state_labels.append((self.create_label('TOP  -'), (290, 465)))
            self.state_labels.append((self.create_label('000000'), (390, 465)))

    def create_info_labels(self):
        self.info_labels = []
        self.info_labels.append((self.create_label('MARIO'), (75, 30)))
        self.info_labels.append((self.create_label('WORLD'), (450, 30)))
        self.info_labels.append((self.create_label('TIME'), (625, 30)))
        self.info_labels.append((self.create_label('000000'), (75, 55)))
        self.info_labels.append((self.create_label('x00'), (300, 55)))
        self.info_labels.append((self.create_label('1 - 1'), (475, 55)))

    def update(self):
        self.flash_coin.update()

    def draw(self, surface):
        for lable in self.state_labels:
            surface.blit(lable[0], lable[1])
        for lable in self.info_labels:
            surface.blit(lable[0], lable[1])
        surface.blit(self.flash_coin.image, self.flash_coin.rect)
